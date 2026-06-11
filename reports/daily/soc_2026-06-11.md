# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T14:46:02Z |
| **Shift Time** | 14:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **112** |
| Confirmed Threats | **97** |
| False Positives Filtered | **15** (13.4%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **16** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **47** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **14** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `admin` | 10 |
| `sol` | 4 |
| `solv` | 4 |
| `GET / HTTP/1.1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 8 |
| `LeitboGi0ro` | 6 |
| `123@@@` | 4 |
| `12345678` | 2 |
| `smo@@kkklss` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 2 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `45.148.10.121` | 2026-06-11T08:56:31 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-11T08:56:59 |
| `hayli` | `hayli` | `213.209.159.56` | 2026-06-11T09:24:51 |
| `admin` | `ctcnhf` | `2.57.121.112` | 2026-06-11T09:42:48 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-11T10:14:23 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-11T10:14:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-11T10:19:49 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-11T10:19:49 |
| `sol` | `sol` | `2.57.122.238` | 2026-06-11T10:33:14 |
| `solana` | `solana` | `2.57.122.238` | 2026-06-11T10:35:34 |
| `solv` | `solv` | `2.57.122.238` | 2026-06-11T10:38:02 |
| `solv` | `1234` | `2.57.122.238` | 2026-06-11T10:40:20 |
| `janay` | `janay` | `213.209.159.56` | 2026-06-11T10:42:04 |
| `solv` | `123456` | `2.57.122.238` | 2026-06-11T10:42:31 |
| `solv` | `12345678` | `2.57.122.238` | 2026-06-11T10:44:47 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-06-11T10:46:54 |
| `node` | `node` | `2.57.122.238` | 2026-06-11T10:49:11 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-06-11T10:51:36 |
| `validator` | `validator` | `2.57.122.238` | 2026-06-11T10:53:52 |
| `sol` | `sol123` | `2.57.122.238` | 2026-06-11T10:56:15 |
| `sol` | `123` | `2.57.122.238` | 2026-06-11T10:58:28 |
| `admin` | `cripple` | `2.57.121.112` | 2026-06-11T11:00:17 |
| `sol` | `12345678` | `2.57.122.238` | 2026-06-11T11:00:38 |
| `admin` | `admin` | `115.190.165.143` | 2026-06-11T11:13:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `194.195.210.47` | 2026-06-11T11:13:25 |
| `root` | ` ` | `171.244.38.3` | 2026-06-11T11:32:16 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-11T11:34:51 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-11T11:34:51 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-11T11:35:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.52` | 2026-06-11T11:56:05 |
| `pi` | `raspberry` | `103.205.240.57` | 2026-06-11T11:57:42 |
| `jeniffer` | `jeniffer` | `213.209.159.56` | 2026-06-11T11:58:53 |
| `root` | `12345` | `185.255.122.57` | 2026-06-11T11:59:49 |
| `root` | `this_is_a_fake_password_123456789` | `185.255.122.57` | 2026-06-11T11:59:52 |
| `admin` | `admin` | `47.77.182.54` | 2026-06-11T12:13:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-11T12:13:16 |
| `admin` | `council` | `2.57.121.112` | 2026-06-11T12:17:25 |
| `root` | `admin` | `176.65.139.99` | 2026-06-11T12:30:47 |
| `root` | `MUiesZL` | `213.209.159.217` | 2026-06-11T12:45:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.236.228.220` | 2026-06-11T12:54:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **112** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 24 |
| Paramiko (Python) | 13 |
| PuTTY | 6 |
| Unknown | 5 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 13 | 4 |
| `16443846184e...` | Generic scanner | 13 | 1 |
| `57446c12547a...` | Mirai/variant | 6 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 13 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 1 | Generic scanner |
| `57446c12547a...` | PuTTY | 6 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 4 | 4 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **34** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS208137` | Feo Prest SRL | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cbee3f250a99

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-11 08:56 |
| **Last Seen** | 2026-06-11 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:56:30` | `cowrie.session.connect` |
| `2026-06-11 08:56:30` | `cowrie.client.version` |
| `2026-06-11 08:56:30` | `cowrie.client.kex` |
| `2026-06-11 08:56:31` | `cowrie.login.success` |
| `2026-06-11 08:56:31` | `cowrie.direct-tcpip.request` |
| `2026-06-11 08:56:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 08:56:31` | `cowrie.direct-tcpip.data` |
| `2026-06-11 08:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1fbcd86f4e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-11 08:56 |
| **Last Seen** | 2026-06-11 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:56:31` | `cowrie.session.connect` |
| `2026-06-11 08:56:31` | `cowrie.client.version` |
| `2026-06-11 08:56:31` | `cowrie.client.kex` |
| `2026-06-11 08:56:32` | `cowrie.login.success` |
| `2026-06-11 08:56:32` | `cowrie.direct-tcpip.request` |
| `2026-06-11 08:56:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 08:56:32` | `cowrie.direct-tcpip.data` |
| `2026-06-11 08:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b45d4a2df6

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 09:24 |
| **Last Seen** | 2026-06-11 09:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 09:24:50` | `cowrie.session.connect` |
| `2026-06-11 09:24:50` | `cowrie.client.version` |
| `2026-06-11 09:24:50` | `cowrie.client.kex` |
| `2026-06-11 09:24:51` | `cowrie.login.success` |
| `2026-06-11 09:24:51` | `cowrie.direct-tcpip.request` |
| `2026-06-11 09:24:51` | `cowrie.direct-tcpip.data` |
| `2026-06-11 09:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100dccad995f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 09:42 |
| **Last Seen** | 2026-06-11 09:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 09:42:48` | `cowrie.session.connect` |
| `2026-06-11 09:42:48` | `cowrie.client.version` |
| `2026-06-11 09:42:48` | `cowrie.client.kex` |
| `2026-06-11 09:42:48` | `cowrie.login.success` |
| `2026-06-11 09:42:48` | `cowrie.direct-tcpip.request` |
| `2026-06-11 09:42:48` | `cowrie.direct-tcpip.data` |
| `2026-06-11 09:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d5858491c2

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 10:14 |
| **Last Seen** | 2026-06-11 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:14:22` | `cowrie.session.connect` |
| `2026-06-11 10:14:22` | `cowrie.client.version` |
| `2026-06-11 10:14:22` | `cowrie.client.kex` |
| `2026-06-11 10:14:23` | `cowrie.login.success` |
| `2026-06-11 10:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8502fdbc4ce4

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 10:14 |
| **Last Seen** | 2026-06-11 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:14:22` | `cowrie.session.connect` |
| `2026-06-11 10:14:22` | `cowrie.client.version` |
| `2026-06-11 10:14:22` | `cowrie.client.kex` |
| `2026-06-11 10:14:24` | `cowrie.login.success` |
| `2026-06-11 10:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a613cd55d098

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 10:14 |
| **Last Seen** | 2026-06-11 10:16 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:14:40` | `cowrie.session.connect` |
| `2026-06-11 10:14:40` | `cowrie.client.version` |
| `2026-06-11 10:14:40` | `cowrie.client.kex` |
| `2026-06-11 10:14:42` | `cowrie.login.success` |
| `2026-06-11 10:14:44` | `cowrie.session.file_upload` |
| `2026-06-11 10:14:45` | `cowrie.session.params` |
| `2026-06-11 10:14:45` | `cowrie.command.input` |
| `2026-06-11 10:14:45` | `cowrie.command.input` |
| `2026-06-11 10:14:45` | `cowrie.command.input` |
| `2026-06-11 10:14:45` | `cowrie.command.failed` |
| `2026-06-11 10:14:45` | `cowrie.log.closed` |
| `2026-06-11 10:14:46` | `cowrie.session.params` |
| `2026-06-11 10:14:46` | `cowrie.command.input` |
| `2026-06-11 10:14:47` | `cowrie.log.closed` |
| `2026-06-11 10:14:48` | `cowrie.session.params` |
| `2026-06-11 10:14:48` | `cowrie.command.input` |
| `2026-06-11 10:14:48` | `cowrie.log.closed` |
| `2026-06-11 10:14:49` | `cowrie.session.params` |
| `2026-06-11 10:14:49` | `cowrie.command.input` |
| `2026-06-11 10:14:49` | `cowrie.command.failed` |
| `2026-06-11 10:14:49` | `cowrie.command.failed` |
| `2026-06-11 10:15:51` | `cowrie.session.params` |
| `2026-06-11 10:15:51` | `cowrie.command.input` |
| `2026-06-11 10:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63a9b75cae9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 10:19 |
| **Last Seen** | 2026-06-11 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:19:49` | `cowrie.session.connect` |
| `2026-06-11 10:19:49` | `cowrie.client.version` |
| `2026-06-11 10:19:49` | `cowrie.client.kex` |
| `2026-06-11 10:19:49` | `cowrie.login.success` |
| `2026-06-11 10:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c49b5b2dc9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 10:19 |
| **Last Seen** | 2026-06-11 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:19:49` | `cowrie.session.connect` |
| `2026-06-11 10:19:49` | `cowrie.client.version` |
| `2026-06-11 10:19:49` | `cowrie.client.kex` |
| `2026-06-11 10:19:49` | `cowrie.login.success` |
| `2026-06-11 10:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e534267c6685

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:33 |
| **Last Seen** | 2026-06-11 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:33:14` | `cowrie.session.connect` |
| `2026-06-11 10:33:14` | `cowrie.client.version` |
| `2026-06-11 10:33:14` | `cowrie.client.kex` |
| `2026-06-11 10:33:14` | `cowrie.login.success` |
| `2026-06-11 10:33:15` | `cowrie.session.params` |
| `2026-06-11 10:33:15` | `cowrie.command.input` |
| `2026-06-11 10:33:15` | `cowrie.log.closed` |
| `2026-06-11 10:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08731646485

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:35 |
| **Last Seen** | 2026-06-11 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:35:34` | `cowrie.session.connect` |
| `2026-06-11 10:35:34` | `cowrie.client.version` |
| `2026-06-11 10:35:34` | `cowrie.client.kex` |
| `2026-06-11 10:35:34` | `cowrie.login.success` |
| `2026-06-11 10:35:35` | `cowrie.session.params` |
| `2026-06-11 10:35:35` | `cowrie.command.input` |
| `2026-06-11 10:35:35` | `cowrie.log.closed` |
| `2026-06-11 10:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa24b26c18f1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:38 |
| **Last Seen** | 2026-06-11 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:38:01` | `cowrie.session.connect` |
| `2026-06-11 10:38:01` | `cowrie.client.version` |
| `2026-06-11 10:38:01` | `cowrie.client.kex` |
| `2026-06-11 10:38:02` | `cowrie.login.success` |
| `2026-06-11 10:38:02` | `cowrie.session.params` |
| `2026-06-11 10:38:02` | `cowrie.command.input` |
| `2026-06-11 10:38:03` | `cowrie.log.closed` |
| `2026-06-11 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e14c4fed2b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:40 |
| **Last Seen** | 2026-06-11 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:40:19` | `cowrie.session.connect` |
| `2026-06-11 10:40:19` | `cowrie.client.version` |
| `2026-06-11 10:40:19` | `cowrie.client.kex` |
| `2026-06-11 10:40:20` | `cowrie.login.success` |
| `2026-06-11 10:40:20` | `cowrie.session.params` |
| `2026-06-11 10:40:20` | `cowrie.command.input` |
| `2026-06-11 10:40:20` | `cowrie.log.closed` |
| `2026-06-11 10:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fb48a75b71

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 10:42 |
| **Last Seen** | 2026-06-11 10:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:42:04` | `cowrie.session.connect` |
| `2026-06-11 10:42:04` | `cowrie.client.version` |
| `2026-06-11 10:42:04` | `cowrie.client.kex` |
| `2026-06-11 10:42:04` | `cowrie.login.success` |
| `2026-06-11 10:42:04` | `cowrie.direct-tcpip.request` |
| `2026-06-11 10:42:05` | `cowrie.direct-tcpip.data` |
| `2026-06-11 10:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ea3255ef47

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:42 |
| **Last Seen** | 2026-06-11 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:42:30` | `cowrie.session.connect` |
| `2026-06-11 10:42:30` | `cowrie.client.version` |
| `2026-06-11 10:42:30` | `cowrie.client.kex` |
| `2026-06-11 10:42:31` | `cowrie.login.success` |
| `2026-06-11 10:42:31` | `cowrie.session.params` |
| `2026-06-11 10:42:31` | `cowrie.command.input` |
| `2026-06-11 10:42:32` | `cowrie.log.closed` |
| `2026-06-11 10:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54e700f3e6a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:44 |
| **Last Seen** | 2026-06-11 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:44:46` | `cowrie.session.connect` |
| `2026-06-11 10:44:46` | `cowrie.client.version` |
| `2026-06-11 10:44:46` | `cowrie.client.kex` |
| `2026-06-11 10:44:47` | `cowrie.login.success` |
| `2026-06-11 10:44:48` | `cowrie.session.params` |
| `2026-06-11 10:44:48` | `cowrie.command.input` |
| `2026-06-11 10:44:48` | `cowrie.log.closed` |
| `2026-06-11 10:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2a489f810c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:46 |
| **Last Seen** | 2026-06-11 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:46:54` | `cowrie.session.connect` |
| `2026-06-11 10:46:54` | `cowrie.client.version` |
| `2026-06-11 10:46:54` | `cowrie.client.kex` |
| `2026-06-11 10:46:54` | `cowrie.login.success` |
| `2026-06-11 10:46:55` | `cowrie.session.params` |
| `2026-06-11 10:46:55` | `cowrie.command.input` |
| `2026-06-11 10:46:55` | `cowrie.log.closed` |
| `2026-06-11 10:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f248b89bc486

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:49 |
| **Last Seen** | 2026-06-11 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:49:10` | `cowrie.session.connect` |
| `2026-06-11 10:49:10` | `cowrie.client.version` |
| `2026-06-11 10:49:10` | `cowrie.client.kex` |
| `2026-06-11 10:49:11` | `cowrie.login.success` |
| `2026-06-11 10:49:12` | `cowrie.session.params` |
| `2026-06-11 10:49:12` | `cowrie.command.input` |
| `2026-06-11 10:49:12` | `cowrie.log.closed` |
| `2026-06-11 10:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e29703cc5c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:51 |
| **Last Seen** | 2026-06-11 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:51:35` | `cowrie.session.connect` |
| `2026-06-11 10:51:35` | `cowrie.client.version` |
| `2026-06-11 10:51:36` | `cowrie.client.kex` |
| `2026-06-11 10:51:36` | `cowrie.login.success` |
| `2026-06-11 10:51:37` | `cowrie.session.params` |
| `2026-06-11 10:51:37` | `cowrie.command.input` |
| `2026-06-11 10:51:37` | `cowrie.log.closed` |
| `2026-06-11 10:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ba431744a6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:53 |
| **Last Seen** | 2026-06-11 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:53:52` | `cowrie.session.connect` |
| `2026-06-11 10:53:52` | `cowrie.client.version` |
| `2026-06-11 10:53:52` | `cowrie.client.kex` |
| `2026-06-11 10:53:52` | `cowrie.login.success` |
| `2026-06-11 10:53:53` | `cowrie.session.params` |
| `2026-06-11 10:53:53` | `cowrie.command.input` |
| `2026-06-11 10:53:53` | `cowrie.log.closed` |
| `2026-06-11 10:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1b36d92759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:56 |
| **Last Seen** | 2026-06-11 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:56:14` | `cowrie.session.connect` |
| `2026-06-11 10:56:14` | `cowrie.client.version` |
| `2026-06-11 10:56:14` | `cowrie.client.kex` |
| `2026-06-11 10:56:15` | `cowrie.login.success` |
| `2026-06-11 10:56:15` | `cowrie.session.params` |
| `2026-06-11 10:56:15` | `cowrie.command.input` |
| `2026-06-11 10:56:16` | `cowrie.log.closed` |
| `2026-06-11 10:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25db8cdf7ea

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 10:58 |
| **Last Seen** | 2026-06-11 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:58:28` | `cowrie.session.connect` |
| `2026-06-11 10:58:28` | `cowrie.client.version` |
| `2026-06-11 10:58:28` | `cowrie.client.kex` |
| `2026-06-11 10:58:28` | `cowrie.login.success` |
| `2026-06-11 10:58:29` | `cowrie.session.params` |
| `2026-06-11 10:58:29` | `cowrie.command.input` |
| `2026-06-11 10:58:29` | `cowrie.log.closed` |
| `2026-06-11 10:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8523367a7422

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 11:00 |
| **Last Seen** | 2026-06-11 11:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:00:17` | `cowrie.session.connect` |
| `2026-06-11 11:00:17` | `cowrie.client.version` |
| `2026-06-11 11:00:17` | `cowrie.client.kex` |
| `2026-06-11 11:00:17` | `cowrie.login.success` |
| `2026-06-11 11:00:17` | `cowrie.direct-tcpip.request` |
| `2026-06-11 11:00:18` | `cowrie.direct-tcpip.data` |
| `2026-06-11 11:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389b909d233d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-11 11:00 |
| **Last Seen** | 2026-06-11 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:00:37` | `cowrie.session.connect` |
| `2026-06-11 11:00:37` | `cowrie.client.version` |
| `2026-06-11 11:00:37` | `cowrie.client.kex` |
| `2026-06-11 11:00:38` | `cowrie.login.success` |
| `2026-06-11 11:00:38` | `cowrie.session.params` |
| `2026-06-11 11:00:38` | `cowrie.command.input` |
| `2026-06-11 11:00:39` | `cowrie.log.closed` |
| `2026-06-11 11:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a66e59e032e

| Field | Detail |
|---|---|
| **Source IP** | `115.190.165[.]143` |
| **First Seen** | 2026-06-11 11:11 |
| **Last Seen** | 2026-06-11 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:11:05` | `cowrie.session.connect` |
| `2026-06-11 11:11:07` | `cowrie.telnet.option` |
| `2026-06-11 11:11:07` | `cowrie.telnet.option` |
| `2026-06-11 11:13:05` | `cowrie.login.success` |
| `2026-06-11 11:13:06` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `115.190.165[.]143` to AbuseIPDB if not already reported
- [ ] Block `115.190.165[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a256ed2ea6f6

| Field | Detail |
|---|---|
| **Source IP** | `194.195.210[.]47` |
| **First Seen** | 2026-06-11 11:13 |
| **Last Seen** | 2026-06-11 11:13 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:13:25` | `cowrie.session.connect` |
| `2026-06-11 11:13:25` | `cowrie.login.success` |
| `2026-06-11 11:13:26` | `cowrie.session.params` |
| `2026-06-11 11:13:26` | `cowrie.command.input` |
| `2026-06-11 11:13:26` | `cowrie.command.failed` |
| `2026-06-11 11:13:26` | `cowrie.command.input` |
| `2026-06-11 11:13:26` | `cowrie.command.failed` |
| `2026-06-11 11:13:26` | `cowrie.command.input` |
| `2026-06-11 11:13:26` | `cowrie.command.failed` |
| `2026-06-11 11:13:26` | `cowrie.command.input` |
| `2026-06-11 11:13:47` | `cowrie.log.closed` |
| `2026-06-11 11:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.195.210[.]47` to AbuseIPDB if not already reported
- [ ] Block `194.195.210[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a77c873a64

| Field | Detail |
|---|---|
| **Source IP** | `171.244.38[.]3` |
| **First Seen** | 2026-06-11 11:32 |
| **Last Seen** | 2026-06-11 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:32:15` | `cowrie.session.connect` |
| `2026-06-11 11:32:15` | `cowrie.client.version` |
| `2026-06-11 11:32:16` | `cowrie.client.kex` |
| `2026-06-11 11:32:16` | `cowrie.login.success` |
| `2026-06-11 11:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.38[.]3` to AbuseIPDB if not already reported
- [ ] Block `171.244.38[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43f5874a7b0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 11:34 |
| **Last Seen** | 2026-06-11 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:34:50` | `cowrie.session.connect` |
| `2026-06-11 11:34:50` | `cowrie.client.version` |
| `2026-06-11 11:34:50` | `cowrie.client.kex` |
| `2026-06-11 11:34:51` | `cowrie.login.success` |
| `2026-06-11 11:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcdb06d72956

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 11:34 |
| **Last Seen** | 2026-06-11 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:34:50` | `cowrie.session.connect` |
| `2026-06-11 11:34:50` | `cowrie.client.version` |
| `2026-06-11 11:34:51` | `cowrie.client.kex` |
| `2026-06-11 11:34:51` | `cowrie.login.success` |
| `2026-06-11 11:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15bf19720c58

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 11:35 |
| **Last Seen** | 2026-06-11 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:35:00` | `cowrie.session.connect` |
| `2026-06-11 11:35:00` | `cowrie.client.version` |
| `2026-06-11 11:35:01` | `cowrie.client.kex` |
| `2026-06-11 11:35:01` | `cowrie.login.success` |
| `2026-06-11 11:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe882caa5f4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 11:35 |
| **Last Seen** | 2026-06-11 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:35:01` | `cowrie.session.connect` |
| `2026-06-11 11:35:01` | `cowrie.client.version` |
| `2026-06-11 11:35:02` | `cowrie.client.kex` |
| `2026-06-11 11:35:02` | `cowrie.login.success` |
| `2026-06-11 11:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d662ea1b6d

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]52` |
| **First Seen** | 2026-06-11 11:56 |
| **Last Seen** | 2026-06-11 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.224 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:56:05` | `cowrie.session.connect` |
| `2026-06-11 11:56:05` | `cowrie.login.success` |
| `2026-06-11 11:56:05` | `cowrie.session.params` |
| `2026-06-11 11:56:05` | `cowrie.command.input` |
| `2026-06-11 11:56:05` | `cowrie.command.input` |
| `2026-06-11 11:56:05` | `cowrie.command.failed` |
| `2026-06-11 11:56:05` | `cowrie.command.input` |
| `2026-06-11 11:56:05` | `cowrie.command.failed` |
| `2026-06-11 11:56:05` | `cowrie.command.input` |
| `2026-06-11 11:56:06` | `cowrie.log.closed` |
| `2026-06-11 11:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]52` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a124d0cc8ec

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 11:58 |
| **Last Seen** | 2026-06-11 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:58:52` | `cowrie.session.connect` |
| `2026-06-11 11:58:52` | `cowrie.client.version` |
| `2026-06-11 11:58:52` | `cowrie.client.kex` |
| `2026-06-11 11:58:53` | `cowrie.login.success` |
| `2026-06-11 11:58:53` | `cowrie.direct-tcpip.request` |
| `2026-06-11 11:58:53` | `cowrie.direct-tcpip.data` |
| `2026-06-11 11:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92313b2936c6

| Field | Detail |
|---|---|
| **Source IP** | `185.255.122[.]57` |
| **First Seen** | 2026-06-11 11:59 |
| **Last Seen** | 2026-06-11 11:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo honeypottest` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:59:49` | `cowrie.session.connect` |
| `2026-06-11 11:59:49` | `cowrie.login.success` |
| `2026-06-11 11:59:50` | `cowrie.session.params` |
| `2026-06-11 11:59:50` | `cowrie.command.input` |
| `2026-06-11 11:59:51` | `cowrie.log.closed` |
| `2026-06-11 11:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.122[.]57` to AbuseIPDB if not already reported
- [ ] Block `185.255.122[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685081aff6ee

| Field | Detail |
|---|---|
| **Source IP** | `185.255.122[.]57` |
| **First Seen** | 2026-06-11 11:59 |
| **Last Seen** | 2026-06-11 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:59:51` | `cowrie.session.connect` |
| `2026-06-11 11:59:52` | `cowrie.login.success` |
| `2026-06-11 11:59:52` | `cowrie.session.params` |
| `2026-06-11 11:59:53` | `cowrie.log.closed` |
| `2026-06-11 11:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.122[.]57` to AbuseIPDB if not already reported
- [ ] Block `185.255.122[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5c55f1e856

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-06-11 12:13 |
| **Last Seen** | 2026-06-11 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:13:15` | `cowrie.session.connect` |
| `2026-06-11 12:13:15` | `cowrie.client.version` |
| `2026-06-11 12:13:15` | `cowrie.client.kex` |
| `2026-06-11 12:13:15` | `cowrie.login.success` |
| `2026-06-11 12:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b5537bb1b6

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-11 12:13 |
| **Last Seen** | 2026-06-11 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:13:15` | `cowrie.session.connect` |
| `2026-06-11 12:13:15` | `cowrie.client.version` |
| `2026-06-11 12:13:15` | `cowrie.client.kex` |
| `2026-06-11 12:13:16` | `cowrie.login.success` |
| `2026-06-11 12:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1cc0b065ea

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 12:17 |
| **Last Seen** | 2026-06-11 12:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:17:24` | `cowrie.session.connect` |
| `2026-06-11 12:17:24` | `cowrie.client.version` |
| `2026-06-11 12:17:24` | `cowrie.client.kex` |
| `2026-06-11 12:17:25` | `cowrie.login.success` |
| `2026-06-11 12:17:25` | `cowrie.direct-tcpip.request` |
| `2026-06-11 12:17:25` | `cowrie.direct-tcpip.data` |
| `2026-06-11 12:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19e6f1d264c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]99` |
| **First Seen** | 2026-06-11 12:30 |
| **Last Seen** | 2026-06-11 12:33 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:30:46` | `cowrie.session.connect` |
| `2026-06-11 12:30:47` | `cowrie.login.success` |
| `2026-06-11 12:30:47` | `cowrie.session.params` |
| `2026-06-11 12:33:47` | `cowrie.log.closed` |
| `2026-06-11 12:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]99` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-601b4b2ac21c

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]217` |
| **First Seen** | 2026-06-11 12:45 |
| **Last Seen** | 2026-06-11 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:45:54` | `cowrie.session.connect` |
| `2026-06-11 12:45:54` | `cowrie.client.version` |
| `2026-06-11 12:45:54` | `cowrie.client.kex` |
| `2026-06-11 12:45:54` | `cowrie.login.success` |
| `2026-06-11 12:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]217` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05176d83a74a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 12:54 |
| **Last Seen** | 2026-06-11 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:54:19` | `cowrie.session.connect` |
| `2026-06-11 12:54:19` | `cowrie.client.version` |
| `2026-06-11 12:54:19` | `cowrie.client.kex` |
| `2026-06-11 12:54:20` | `cowrie.login.success` |
| `2026-06-11 12:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-823073314e1a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 12:54 |
| **Last Seen** | 2026-06-11 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:54:19` | `cowrie.session.connect` |
| `2026-06-11 12:54:19` | `cowrie.client.version` |
| `2026-06-11 12:54:20` | `cowrie.client.kex` |
| `2026-06-11 12:54:21` | `cowrie.login.success` |
| `2026-06-11 12:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4de191776b2

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]220` |
| **First Seen** | 2026-06-11 12:54 |
| **Last Seen** | 2026-06-11 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:54:23` | `cowrie.session.connect` |
| `2026-06-11 12:54:23` | `cowrie.login.success` |
| `2026-06-11 12:54:23` | `cowrie.session.params` |
| `2026-06-11 12:54:23` | `cowrie.command.input` |
| `2026-06-11 12:54:23` | `cowrie.command.input` |
| `2026-06-11 12:54:23` | `cowrie.command.failed` |
| `2026-06-11 12:54:23` | `cowrie.command.input` |
| `2026-06-11 12:54:23` | `cowrie.command.failed` |
| `2026-06-11 12:54:23` | `cowrie.command.input` |
| `2026-06-11 12:54:23` | `cowrie.log.closed` |
| `2026-06-11 12:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]220` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb27591e63f

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 12:54 |
| **Last Seen** | 2026-06-11 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:54:43` | `cowrie.session.connect` |
| `2026-06-11 12:54:43` | `cowrie.client.version` |
| `2026-06-11 12:54:43` | `cowrie.client.kex` |
| `2026-06-11 12:54:45` | `cowrie.login.success` |
| `2026-06-11 12:54:47` | `cowrie.session.file_upload` |
| `2026-06-11 12:54:48` | `cowrie.session.params` |
| `2026-06-11 12:54:48` | `cowrie.command.input` |
| `2026-06-11 12:54:48` | `cowrie.command.input` |
| `2026-06-11 12:54:48` | `cowrie.command.input` |
| `2026-06-11 12:54:48` | `cowrie.command.failed` |
| `2026-06-11 12:54:48` | `cowrie.log.closed` |
| `2026-06-11 12:54:49` | `cowrie.session.params` |
| `2026-06-11 12:54:49` | `cowrie.command.input` |
| `2026-06-11 12:54:50` | `cowrie.log.closed` |
| `2026-06-11 12:54:51` | `cowrie.session.params` |
| `2026-06-11 12:54:51` | `cowrie.command.input` |
| `2026-06-11 12:54:51` | `cowrie.log.closed` |
| `2026-06-11 12:54:52` | `cowrie.session.params` |
| `2026-06-11 12:54:52` | `cowrie.command.input` |
| `2026-06-11 12:54:52` | `cowrie.command.failed` |
| `2026-06-11 12:54:52` | `cowrie.command.failed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **11** | 2026-06-11 09:25 | 2026-06-11 11:37 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **4** | 2026-06-11 09:54 | 2026-06-11 10:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `154.16.146[.]65` | **4** | 2026-06-11 12:25 | 2026-06-11 12:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-06-11 10:11 | 2026-06-11 10:44 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.174.211[.]117` | **2** | 2026-06-11 09:03 | 2026-06-11 09:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.32[.]182` | **2** | 2026-06-11 10:14 | 2026-06-11 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.226.253[.]35` | **2** | 2026-06-11 11:55 | 2026-06-11 11:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]144` | **2** | 2026-06-11 09:15 | 2026-06-11 09:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.42.108[.]100` | **2** | 2026-06-11 12:54 | 2026-06-11 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.16.45[.]245` | **2** | 2026-06-11 11:21 | 2026-06-11 11:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.44.136[.]115` | 1 | 2026-06-11 12:39 | 2026-06-11 12:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | 1 | 2026-06-11 12:13 | 2026-06-11 12:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `119.99.251[.]242` | 1 | 2026-06-11 12:40 | 2026-06-11 12:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-06-11 12:54 | 2026-06-11 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-06-11 12:13 | 2026-06-11 12:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.191.40[.]108` | 1 | 2026-06-11 08:59 | 2026-06-11 08:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]194` | 1 | 2026-06-11 11:13 | 2026-06-11 11:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.119.13[.]58` | 1 | 2026-06-11 09:37 | 2026-06-11 09:37 | 43s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]236` | 1 | 2026-06-11 11:32 | 2026-06-11 11:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-06-11 11:11 | 2026-06-11 11:13 | 112s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-06-11 10:30 | 2026-06-11 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-06-11 09:07 | 2026-06-11 09:08 | 40s | 0 | `T1592` | 🟢 LOW |
| `212.20.49[.]156` | 1 | 2026-06-11 12:16 | 2026-06-11 12:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]186` | 1 | 2026-06-11 09:41 | 2026-06-11 09:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.245.39[.]47` | 1 | 2026-06-11 12:18 | 2026-06-11 12:19 | 19s | 0 | `T1592` | 🟢 LOW |
| `59.127.237[.]110` | 1 | 2026-06-11 09:23 | 2026-06-11 09:23 | 14s | 0 | `T1592` | 🟢 LOW |
| `8.217.120[.]145` | 1 | 2026-06-11 10:30 | 2026-06-11 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]199` | 1 | 2026-06-11 12:33 | 2026-06-11 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]241` | 1 | 2026-06-11 12:33 | 2026-06-11 12:33 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `213.209.159[.]186` | DE | Feo Prest SRL | **100** ⚠️ | 2 |
| `119.99.251[.]242` | CN | CHINANET Hubei province network | **100** ⚠️ | 1 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `177.22.44[.]30` | BR | Conecta Tecnologia LTDA | **100** ⚠️ | 14 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `8.217.120[.]145` | HK | Aliyun Computing Co.LTD | **100** ⚠️ | 18 |
| `91.230.168[.]241` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `20.42.108[.]100` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 54 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 112 cases |
| Tool 34  | Credential Extractor        | ✅ 47 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (13.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 29 recon entry/entries in table (10 group(s) consolidating 34 session(s)).

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
_Report time: 2026-06-11T14:46:02Z_

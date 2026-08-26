# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-26 |
| **Generated At** | 2026-08-26T10:38:33Z |
| **Shift Time** | 10:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **75** |
| Confirmed Threats | **72** |
| False Positives Filtered | **3** (4.0%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **13** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **2** HIGH · **21** MED · 21 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **6** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `ubuntu` | 12 |
| `support` | 4 |
| `admin` | 4 |
| `pi` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `support` | 4 |
| `admin` | 4 |
| `abcd1234` | 2 |
| `centos` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `support` | `support` | 4 |
| `admin` | `admin` | 4 |
| `pi` | `abcd1234` | 2 |
| `root` | `centos` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `centos` | `117.176.220.76` | 2026-08-26T06:56:51 |
| `ubuntu` | `1234qwer!@#$` | `217.60.255.130` | 2026-08-26T07:01:56 |
| `root` | `ADMIN123` | `217.60.255.130` | 2026-08-26T07:01:59 |
| `ubuntu` | `Rainbow1` | `217.60.255.130` | 2026-08-26T07:11:24 |
| `root` | `Lucas@123` | `217.60.255.130` | 2026-08-26T07:11:28 |
| `root` | `---fuck_you----` | `47.184.58.103` | 2026-08-26T07:14:23 |
| `ubuntu` | `jojo` | `217.60.255.130` | 2026-08-26T07:20:51 |
| `root` | `Qwerty!123` | `217.60.255.130` | 2026-08-26T07:20:55 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-26T07:24:42 |
| `ubuntu` | `Start12345` | `217.60.255.130` | 2026-08-26T07:30:31 |
| `root` | `linux` | `217.60.255.130` | 2026-08-26T07:30:35 |
| `support` | `support` | `176.53.159.196` | 2026-08-26T07:36:49 |
| `ubuntu` | `Sohrab123` | `217.60.255.130` | 2026-08-26T07:39:51 |
| `root` | `Drs123` | `217.60.255.130` | 2026-08-26T07:39:54 |
| `ubuntu` | `Hadi@2026` | `217.60.255.130` | 2026-08-26T07:49:30 |
| `root` | `asdasd123` | `217.60.255.130` | 2026-08-26T07:49:34 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-26T07:52:25 |
| `ubuntu` | `Server123` | `217.60.255.130` | 2026-08-26T07:59:04 |
| `root` | `Admin123.` | `217.60.255.130` | 2026-08-26T07:59:08 |
| `support` | `support` | `10.0.0.73` | 2026-08-26T08:01:48 |
| `ubuntu` | `Info@123` | `217.60.255.130` | 2026-08-26T08:08:35 |
| `root` | `admin@888` | `217.60.255.130` | 2026-08-26T08:08:39 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-26T08:12:07 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-26T08:14:32 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-26T08:14:32 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `74.82.47.2` | 2026-08-26T08:17:38 |
| `ubuntu` | `Smart123` | `217.60.255.130` | 2026-08-26T08:18:01 |
| `root` | `praxis` | `217.60.255.130` | 2026-08-26T08:18:05 |
| `ubuntu` | `Pa55word` | `217.60.255.130` | 2026-08-26T08:27:42 |
| `root` | `ftpuser123!` | `217.60.255.130` | 2026-08-26T08:27:46 |
| `ubuntu` | `A@12345` | `217.60.255.130` | 2026-08-26T08:37:00 |
| `root` | `master#2025` | `217.60.255.130` | 2026-08-26T08:37:04 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-26T08:44:05 |
| `ubuntu` | `Kasra123` | `217.60.255.130` | 2026-08-26T08:46:38 |
| `root` | `xxx` | `217.60.255.130` | 2026-08-26T08:46:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **75** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 6 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **22** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS56041` | China Mobile communications corporation | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS204203` | Atrin Information & Communications Technology Company PJS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7b74487972da

| Field | Detail |
|---|---|
| **Source IP** | `117.176.220[.]76` |
| **First Seen** | 2026-08-26 06:56 |
| **Last Seen** | 2026-08-26 07:01 |
| **Session Duration** | 327s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 06:56:23` | `cowrie.session.connect` |
| `2026-08-26 06:56:50` | `cowrie.client.version` |
| `2026-08-26 06:56:50` | `cowrie.client.kex` |
| `2026-08-26 06:56:51` | `cowrie.login.success` |
| `2026-08-26 07:01:51` | `cowrie.session.file_upload` |
| `2026-08-26 07:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.176.220[.]76` to AbuseIPDB if not already reported
- [ ] Block `117.176.220[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c7d85d9385

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:01 |
| **Last Seen** | 2026-08-26 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:01:55` | `cowrie.session.connect` |
| `2026-08-26 07:01:55` | `cowrie.client.version` |
| `2026-08-26 07:01:55` | `cowrie.client.kex` |
| `2026-08-26 07:01:56` | `cowrie.login.success` |
| `2026-08-26 07:01:56` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:01:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:01:56` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621ddd8b5d43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:01 |
| **Last Seen** | 2026-08-26 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:01:58` | `cowrie.session.connect` |
| `2026-08-26 07:01:58` | `cowrie.client.version` |
| `2026-08-26 07:01:59` | `cowrie.client.kex` |
| `2026-08-26 07:01:59` | `cowrie.login.success` |
| `2026-08-26 07:02:00` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:02:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:02:00` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39dd5e25fc4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:11 |
| **Last Seen** | 2026-08-26 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:11:23` | `cowrie.session.connect` |
| `2026-08-26 07:11:23` | `cowrie.client.version` |
| `2026-08-26 07:11:23` | `cowrie.client.kex` |
| `2026-08-26 07:11:24` | `cowrie.login.success` |
| `2026-08-26 07:11:25` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:11:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:11:25` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045f9e07bdf4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:11 |
| **Last Seen** | 2026-08-26 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:11:27` | `cowrie.session.connect` |
| `2026-08-26 07:11:27` | `cowrie.client.version` |
| `2026-08-26 07:11:27` | `cowrie.client.kex` |
| `2026-08-26 07:11:28` | `cowrie.login.success` |
| `2026-08-26 07:11:28` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:11:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:11:29` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-953b3c66fa21

| Field | Detail |
|---|---|
| **Source IP** | `47.184.58[.]103` |
| **First Seen** | 2026-08-26 07:13 |
| **Last Seen** | 2026-08-26 07:14 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:13:26` | `cowrie.session.connect` |
| `2026-08-26 07:13:27` | `cowrie.client.version` |
| `2026-08-26 07:13:27` | `cowrie.client.kex` |
| `2026-08-26 07:14:23` | `cowrie.login.success` |
| `2026-08-26 07:14:33` | `cowrie.session.params` |
| `2026-08-26 07:14:33` | `cowrie.command.input` |
| `2026-08-26 07:14:41` | `cowrie.log.closed` |
| `2026-08-26 07:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.184.58[.]103` to AbuseIPDB if not already reported
- [ ] Block `47.184.58[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584e1ac7ab0b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:20 |
| **Last Seen** | 2026-08-26 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:20:50` | `cowrie.session.connect` |
| `2026-08-26 07:20:50` | `cowrie.client.version` |
| `2026-08-26 07:20:50` | `cowrie.client.kex` |
| `2026-08-26 07:20:51` | `cowrie.login.success` |
| `2026-08-26 07:20:51` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:20:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:20:51` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b2f2ae3074d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:20 |
| **Last Seen** | 2026-08-26 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:20:54` | `cowrie.session.connect` |
| `2026-08-26 07:20:54` | `cowrie.client.version` |
| `2026-08-26 07:20:54` | `cowrie.client.kex` |
| `2026-08-26 07:20:55` | `cowrie.login.success` |
| `2026-08-26 07:20:56` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:20:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:20:56` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17221aa219f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:30 |
| **Last Seen** | 2026-08-26 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:30:30` | `cowrie.session.connect` |
| `2026-08-26 07:30:30` | `cowrie.client.version` |
| `2026-08-26 07:30:30` | `cowrie.client.kex` |
| `2026-08-26 07:30:31` | `cowrie.login.success` |
| `2026-08-26 07:30:32` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:30:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:30:32` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5327d61f7235

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:30 |
| **Last Seen** | 2026-08-26 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:30:34` | `cowrie.session.connect` |
| `2026-08-26 07:30:34` | `cowrie.client.version` |
| `2026-08-26 07:30:34` | `cowrie.client.kex` |
| `2026-08-26 07:30:35` | `cowrie.login.success` |
| `2026-08-26 07:30:36` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:30:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:30:36` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9293713731

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 07:36 |
| **Last Seen** | 2026-08-26 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:36:49` | `cowrie.session.connect` |
| `2026-08-26 07:36:49` | `cowrie.client.version` |
| `2026-08-26 07:36:49` | `cowrie.client.kex` |
| `2026-08-26 07:36:49` | `cowrie.login.success` |
| `2026-08-26 07:36:50` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:36:50` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7999fdf0d275

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:39 |
| **Last Seen** | 2026-08-26 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:39:50` | `cowrie.session.connect` |
| `2026-08-26 07:39:50` | `cowrie.client.version` |
| `2026-08-26 07:39:50` | `cowrie.client.kex` |
| `2026-08-26 07:39:51` | `cowrie.login.success` |
| `2026-08-26 07:39:51` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:39:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:39:51` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba28cb8b1a6e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:39 |
| **Last Seen** | 2026-08-26 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:39:53` | `cowrie.session.connect` |
| `2026-08-26 07:39:53` | `cowrie.client.version` |
| `2026-08-26 07:39:53` | `cowrie.client.kex` |
| `2026-08-26 07:39:54` | `cowrie.login.success` |
| `2026-08-26 07:39:54` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:39:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:39:55` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a697b5e533c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:49 |
| **Last Seen** | 2026-08-26 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:49:30` | `cowrie.session.connect` |
| `2026-08-26 07:49:30` | `cowrie.client.version` |
| `2026-08-26 07:49:30` | `cowrie.client.kex` |
| `2026-08-26 07:49:30` | `cowrie.login.success` |
| `2026-08-26 07:49:31` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:49:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:49:31` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c554cafba6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:49 |
| **Last Seen** | 2026-08-26 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:49:33` | `cowrie.session.connect` |
| `2026-08-26 07:49:33` | `cowrie.client.version` |
| `2026-08-26 07:49:33` | `cowrie.client.kex` |
| `2026-08-26 07:49:34` | `cowrie.login.success` |
| `2026-08-26 07:49:34` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:49:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:49:34` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4c96e6ca46

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-26 07:51 |
| **Last Seen** | 2026-08-26 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:51:18` | `cowrie.session.connect` |
| `2026-08-26 07:51:25` | `cowrie.telnet.option` |
| `2026-08-26 07:51:25` | `cowrie.telnet.option` |
| `2026-08-26 07:52:25` | `cowrie.login.success` |
| `2026-08-26 07:52:25` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d239ced5fde7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:59 |
| **Last Seen** | 2026-08-26 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:59:03` | `cowrie.session.connect` |
| `2026-08-26 07:59:03` | `cowrie.client.version` |
| `2026-08-26 07:59:04` | `cowrie.client.kex` |
| `2026-08-26 07:59:04` | `cowrie.login.success` |
| `2026-08-26 07:59:05` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:59:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:59:05` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c132af5f79

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 07:59 |
| **Last Seen** | 2026-08-26 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 07:59:07` | `cowrie.session.connect` |
| `2026-08-26 07:59:07` | `cowrie.client.version` |
| `2026-08-26 07:59:07` | `cowrie.client.kex` |
| `2026-08-26 07:59:08` | `cowrie.login.success` |
| `2026-08-26 07:59:08` | `cowrie.direct-tcpip.request` |
| `2026-08-26 07:59:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 07:59:08` | `cowrie.direct-tcpip.data` |
| `2026-08-26 07:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f38df29964

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:08 |
| **Last Seen** | 2026-08-26 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:08:34` | `cowrie.session.connect` |
| `2026-08-26 08:08:34` | `cowrie.client.version` |
| `2026-08-26 08:08:35` | `cowrie.client.kex` |
| `2026-08-26 08:08:35` | `cowrie.login.success` |
| `2026-08-26 08:08:36` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:08:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:08:36` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7043c0f1241

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:08 |
| **Last Seen** | 2026-08-26 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:08:38` | `cowrie.session.connect` |
| `2026-08-26 08:08:38` | `cowrie.client.version` |
| `2026-08-26 08:08:38` | `cowrie.client.kex` |
| `2026-08-26 08:08:39` | `cowrie.login.success` |
| `2026-08-26 08:08:39` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:08:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:08:40` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cbcc635daff

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-26 08:11 |
| **Last Seen** | 2026-08-26 08:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:11:07` | `cowrie.session.connect` |
| `2026-08-26 08:11:07` | `cowrie.telnet.option` |
| `2026-08-26 08:11:07` | `cowrie.telnet.option` |
| `2026-08-26 08:12:07` | `cowrie.login.success` |
| `2026-08-26 08:12:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d696d187a526

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 08:14 |
| **Last Seen** | 2026-08-26 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:14:31` | `cowrie.session.connect` |
| `2026-08-26 08:14:31` | `cowrie.client.version` |
| `2026-08-26 08:14:31` | `cowrie.client.kex` |
| `2026-08-26 08:14:32` | `cowrie.login.success` |
| `2026-08-26 08:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f94c6904a4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 08:14 |
| **Last Seen** | 2026-08-26 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:14:31` | `cowrie.session.connect` |
| `2026-08-26 08:14:31` | `cowrie.client.version` |
| `2026-08-26 08:14:31` | `cowrie.client.kex` |
| `2026-08-26 08:14:32` | `cowrie.login.success` |
| `2026-08-26 08:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc9647a0684

| Field | Detail |
|---|---|
| **Source IP** | `74.82.47[.]2` |
| **First Seen** | 2026-08-26 08:17 |
| **Last Seen** | 2026-08-26 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:17:38` | `cowrie.session.connect` |
| `2026-08-26 08:17:38` | `cowrie.login.success` |
| `2026-08-26 08:17:39` | `cowrie.session.params` |
| `2026-08-26 08:17:39` | `cowrie.command.input` |
| `2026-08-26 08:17:39` | `cowrie.command.input` |
| `2026-08-26 08:17:39` | `cowrie.command.failed` |
| `2026-08-26 08:17:39` | `cowrie.command.input` |
| `2026-08-26 08:17:39` | `cowrie.command.failed` |
| `2026-08-26 08:17:39` | `cowrie.command.input` |
| `2026-08-26 08:17:39` | `cowrie.log.closed` |
| `2026-08-26 08:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.82.47[.]2` to AbuseIPDB if not already reported
- [ ] Block `74.82.47[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4293ab94d7d6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:18 |
| **Last Seen** | 2026-08-26 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:18:00` | `cowrie.session.connect` |
| `2026-08-26 08:18:00` | `cowrie.client.version` |
| `2026-08-26 08:18:00` | `cowrie.client.kex` |
| `2026-08-26 08:18:01` | `cowrie.login.success` |
| `2026-08-26 08:18:01` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:18:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:18:02` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a644f62a263

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:18 |
| **Last Seen** | 2026-08-26 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:18:04` | `cowrie.session.connect` |
| `2026-08-26 08:18:04` | `cowrie.client.version` |
| `2026-08-26 08:18:05` | `cowrie.client.kex` |
| `2026-08-26 08:18:05` | `cowrie.login.success` |
| `2026-08-26 08:18:06` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:18:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:18:06` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66bcb59d8140

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 08:18 |
| **Last Seen** | 2026-08-26 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:18:08` | `cowrie.session.connect` |
| `2026-08-26 08:18:08` | `cowrie.client.version` |
| `2026-08-26 08:18:09` | `cowrie.client.kex` |
| `2026-08-26 08:18:09` | `cowrie.login.success` |
| `2026-08-26 08:18:09` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:18:09` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461ebbee369e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:27 |
| **Last Seen** | 2026-08-26 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:27:41` | `cowrie.session.connect` |
| `2026-08-26 08:27:41` | `cowrie.client.version` |
| `2026-08-26 08:27:41` | `cowrie.client.kex` |
| `2026-08-26 08:27:42` | `cowrie.login.success` |
| `2026-08-26 08:27:42` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:27:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:27:42` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ac700fb78c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:27 |
| **Last Seen** | 2026-08-26 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:27:45` | `cowrie.session.connect` |
| `2026-08-26 08:27:45` | `cowrie.client.version` |
| `2026-08-26 08:27:45` | `cowrie.client.kex` |
| `2026-08-26 08:27:46` | `cowrie.login.success` |
| `2026-08-26 08:27:46` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:27:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:27:46` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24b5f49bf0d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:36 |
| **Last Seen** | 2026-08-26 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:36:59` | `cowrie.session.connect` |
| `2026-08-26 08:36:59` | `cowrie.client.version` |
| `2026-08-26 08:36:59` | `cowrie.client.kex` |
| `2026-08-26 08:37:00` | `cowrie.login.success` |
| `2026-08-26 08:37:00` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:37:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:37:00` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e6951673ed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:37 |
| **Last Seen** | 2026-08-26 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:37:03` | `cowrie.session.connect` |
| `2026-08-26 08:37:03` | `cowrie.client.version` |
| `2026-08-26 08:37:03` | `cowrie.client.kex` |
| `2026-08-26 08:37:04` | `cowrie.login.success` |
| `2026-08-26 08:37:04` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:37:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:37:04` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c03bfb739ce

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:46 |
| **Last Seen** | 2026-08-26 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:46:37` | `cowrie.session.connect` |
| `2026-08-26 08:46:37` | `cowrie.client.version` |
| `2026-08-26 08:46:37` | `cowrie.client.kex` |
| `2026-08-26 08:46:38` | `cowrie.login.success` |
| `2026-08-26 08:46:38` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:46:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:46:38` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1663ea0f3989

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 08:46 |
| **Last Seen** | 2026-08-26 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 08:46:41` | `cowrie.session.connect` |
| `2026-08-26 08:46:41` | `cowrie.client.version` |
| `2026-08-26 08:46:41` | `cowrie.client.kex` |
| `2026-08-26 08:46:42` | `cowrie.login.success` |
| `2026-08-26 08:46:42` | `cowrie.direct-tcpip.request` |
| `2026-08-26 08:46:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 08:46:42` | `cowrie.direct-tcpip.data` |
| `2026-08-26 08:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.37.220[.]188` | **9** | 2026-08-26 06:55 | 2026-08-26 08:48 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-26 07:10 | 2026-08-26 08:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.28.113[.]146` | **3** | 2026-08-26 08:50 | 2026-08-26 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.233.112[.]115` | **2** | 2026-08-26 07:50 | 2026-08-26 07:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-26 07:08 | 2026-08-26 08:08 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]220` | **2** | 2026-08-26 08:42 | 2026-08-26 08:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.206[.]137` | **2** | 2026-08-26 08:22 | 2026-08-26 08:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]65` | **2** | 2026-08-26 07:45 | 2026-08-26 07:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.152.240[.]15` | **2** | 2026-08-26 07:27 | 2026-08-26 07:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]98` | **2** | 2026-08-26 07:58 | 2026-08-26 07:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]217` | 1 | 2026-08-26 08:50 | 2026-08-26 08:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.176.220[.]76` | 1 | 2026-08-26 06:56 | 2026-08-26 06:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]30` | 1 | 2026-08-26 08:46 | 2026-08-26 08:47 | 29s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-08-26 07:06 | 2026-08-26 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-26 08:36 | 2026-08-26 08:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-26 08:36 | 2026-08-26 08:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.184.58[.]103` | 1 | 2026-08-26 07:13 | 2026-08-26 07:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]152` | 1 | 2026-08-26 07:38 | 2026-08-26 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]212` | 1 | 2026-08-26 08:10 | 2026-08-26 08:10 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `45.33.14[.]197` | US | Linode | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `135.233.112[.]115` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `20.106.206[.]137` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `213.230.92[.]65` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 4 |
| `117.176.220[.]76` | CN | China Mobile Communications Corporation | **100** ⚠️ | 49 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `47.85.8[.]171` | US | Alibaba Cloud LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 75 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 19 recon entry/entries in table (10 group(s) consolidating 30 session(s)).

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
_Report time: 2026-08-26T10:38:33Z_

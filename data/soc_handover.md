# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T21:51:20Z |
| **Shift Time** | 21:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **587** |
| Confirmed Threats | **560** |
| False Positives Filtered | **27** (4.6%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **16** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **572** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **3** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `admin` | 5 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 7 |
| `admin` | 5 |
| `lan123` | 2 |
| `smo@@kkklss` | 2 |
| `blender` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 7 |
| `admin` | `admin` | 5 |
| `root` | `lan123` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `blender` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `lan123` | `176.65.139.125` | 2026-06-12T17:22:31 |
| `root` | `blender` | `176.65.148.251` | 2026-06-12T17:45:09 |
| `root` | `` | `74.208.181.249` | 2026-06-12T18:14:53 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-12T19:24:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `128.1.132.136` | 2026-06-12T19:38:10 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-12T19:46:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-12T19:46:24 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-12T19:46:27 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-12T19:52:33 |
| `admin` | `admin` | `91.99.6.245` | 2026-06-12T20:03:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.88` | 2026-06-12T20:20:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **587** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| PuTTY | 14 |
| Go SSH scanner | 12 |
| Paramiko (Python) | 4 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `084386fa7ae5...` | Mirai/variant | 4 | 4 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 3 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | PuTTY | 14 | 9 | — |
| `084386fa7ae5...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |

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
Source IPs: `176.65.148.251`, `74.208.181.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **30** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | LOW |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 2 | HIGH |
| `AS265214` | NT NET TELECOM LTDA | 1 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d7a32bae266e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]125` |
| **First Seen** | 2026-06-12 17:22 |
| **Last Seen** | 2026-06-12 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 17:22:30` | `cowrie.session.connect` |
| `2026-06-12 17:22:31` | `cowrie.login.success` |
| `2026-06-12 17:22:32` | `cowrie.session.params` |
| `2026-06-12 17:22:32` | `cowrie.log.closed` |
| `2026-06-12 17:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]125` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74180340e00b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]251` |
| **First Seen** | 2026-06-12 17:45 |
| **Last Seen** | 2026-06-12 17:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 17:45:07` | `cowrie.session.connect` |
| `2026-06-12 17:45:09` | `cowrie.login.success` |
| `2026-06-12 17:45:09` | `cowrie.session.params` |
| `2026-06-12 17:45:10` | `cowrie.command.input` |
| `2026-06-12 17:45:11` | `cowrie.command.input` |
| `2026-06-12 17:45:11` | `cowrie.command.input` |
| `2026-06-12 17:45:12` | `cowrie.command.input` |
| `2026-06-12 17:45:12` | `cowrie.command.input` |
| `2026-06-12 17:45:12` | `cowrie.command.failed` |
| `2026-06-12 17:45:13` | `cowrie.log.closed` |
| `2026-06-12 17:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c480d2f71c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]125` |
| **First Seen** | 2026-06-12 17:54 |
| **Last Seen** | 2026-06-12 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 17:54:10` | `cowrie.session.connect` |
| `2026-06-12 17:54:10` | `cowrie.login.success` |
| `2026-06-12 17:54:10` | `cowrie.session.params` |
| `2026-06-12 17:54:10` | `cowrie.log.closed` |
| `2026-06-12 17:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]125` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572ade9b1445

| Field | Detail |
|---|---|
| **Source IP** | `74.208.181[.]249` |
| **First Seen** | 2026-06-12 18:14 |
| **Last Seen** | 2026-06-12 18:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:14:52` | `cowrie.session.connect` |
| `2026-06-12 18:14:53` | `cowrie.login.success` |
| `2026-06-12 18:14:53` | `cowrie.session.params` |
| `2026-06-12 18:14:54` | `cowrie.command.input` |
| `2026-06-12 18:14:54` | `cowrie.command.input` |
| `2026-06-12 18:14:55` | `cowrie.command.input` |
| `2026-06-12 18:14:55` | `cowrie.command.input` |
| `2026-06-12 18:14:55` | `cowrie.command.failed` |
| `2026-06-12 18:14:56` | `cowrie.log.closed` |
| `2026-06-12 18:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.181[.]249` to AbuseIPDB if not already reported
- [ ] Block `74.208.181[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea1f2adc58f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-12 19:24 |
| **Last Seen** | 2026-06-12 19:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:24:48` | `cowrie.session.connect` |
| `2026-06-12 19:24:48` | `cowrie.client.version` |
| `2026-06-12 19:24:48` | `cowrie.client.kex` |
| `2026-06-12 19:24:48` | `cowrie.login.success` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.request` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.data` |
| `2026-06-12 19:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02a0d165163

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-12 19:24 |
| **Last Seen** | 2026-06-12 19:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:24:49` | `cowrie.session.connect` |
| `2026-06-12 19:24:49` | `cowrie.client.version` |
| `2026-06-12 19:24:49` | `cowrie.client.kex` |
| `2026-06-12 19:24:49` | `cowrie.login.success` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.request` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-12 19:24:49` | `cowrie.direct-tcpip.data` |
| `2026-06-12 19:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c255ea2e1e0c

| Field | Detail |
|---|---|
| **Source IP** | `128.1.132[.]136` |
| **First Seen** | 2026-06-12 19:38 |
| **Last Seen** | 2026-06-12 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:38:10` | `cowrie.session.connect` |
| `2026-06-12 19:38:10` | `cowrie.login.success` |
| `2026-06-12 19:38:10` | `cowrie.session.params` |
| `2026-06-12 19:38:10` | `cowrie.command.input` |
| `2026-06-12 19:38:10` | `cowrie.command.failed` |
| `2026-06-12 19:38:10` | `cowrie.command.input` |
| `2026-06-12 19:38:11` | `cowrie.log.closed` |
| `2026-06-12 19:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.132[.]136` to AbuseIPDB if not already reported
- [ ] Block `128.1.132[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99af605b1bfa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 19:46 |
| **Last Seen** | 2026-06-12 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:46:24` | `cowrie.session.connect` |
| `2026-06-12 19:46:24` | `cowrie.client.version` |
| `2026-06-12 19:46:24` | `cowrie.client.kex` |
| `2026-06-12 19:46:24` | `cowrie.login.success` |
| `2026-06-12 19:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b0299a12c2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 19:46 |
| **Last Seen** | 2026-06-12 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:46:24` | `cowrie.session.connect` |
| `2026-06-12 19:46:24` | `cowrie.client.version` |
| `2026-06-12 19:46:24` | `cowrie.client.kex` |
| `2026-06-12 19:46:24` | `cowrie.login.success` |
| `2026-06-12 19:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb459c415939

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 19:46 |
| **Last Seen** | 2026-06-12 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:46:27` | `cowrie.session.connect` |
| `2026-06-12 19:46:27` | `cowrie.client.version` |
| `2026-06-12 19:46:27` | `cowrie.client.kex` |
| `2026-06-12 19:46:27` | `cowrie.login.success` |
| `2026-06-12 19:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187670bcdd95

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 19:46 |
| **Last Seen** | 2026-06-12 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:46:27` | `cowrie.session.connect` |
| `2026-06-12 19:46:27` | `cowrie.client.version` |
| `2026-06-12 19:46:27` | `cowrie.client.kex` |
| `2026-06-12 19:46:27` | `cowrie.login.success` |
| `2026-06-12 19:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c01de379f2e

| Field | Detail |
|---|---|
| **Source IP** | `91.99.6[.]245` |
| **First Seen** | 2026-06-12 20:02 |
| **Last Seen** | 2026-06-12 20:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:02:07` | `cowrie.session.connect` |
| `2026-06-12 20:02:07` | `cowrie.telnet.option` |
| `2026-06-12 20:02:07` | `cowrie.telnet.option` |
| `2026-06-12 20:03:07` | `cowrie.login.success` |
| `2026-06-12 20:03:08` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `91.99.6[.]245` to AbuseIPDB if not already reported
- [ ] Block `91.99.6[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **478** | 2026-06-12 16:55 | 2026-06-12 20:54 | 287m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **19** | 2026-06-12 17:02 | 2026-06-12 20:48 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `128.1.132[.]136` | **8** | 2026-06-12 19:37 | 2026-06-12 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **7** | 2026-06-12 17:25 | 2026-06-12 20:08 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-06-12 17:46 | 2026-06-12 20:43 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.154[.]126` | **3** | 2026-06-12 19:21 | 2026-06-12 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.33.242[.]50` | **2** | 2026-06-12 19:38 | 2026-06-12 19:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.102.116[.]62` | **2** | 2026-06-12 18:04 | 2026-06-12 18:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.221.68[.]159` | **2** | 2026-06-12 19:46 | 2026-06-12 19:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]41` | **2** | 2026-06-12 17:55 | 2026-06-12 17:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.41.186[.]9` | **2** | 2026-06-12 17:45 | 2026-06-12 17:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-12 19:06 | 2026-06-12 19:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-06-12 18:09 | 2026-06-12 18:11 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-06-12 18:38 | 2026-06-12 18:38 | 5s | 0 | `T1592` | 🟢 LOW |
| `167.250.158[.]32` | 1 | 2026-06-12 17:19 | 2026-06-12 17:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]125` | 1 | 2026-06-12 19:18 | 2026-06-12 19:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]251` | 1 | 2026-06-12 17:45 | 2026-06-12 17:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]183` | 1 | 2026-06-12 17:38 | 2026-06-12 17:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-12 17:08 | 2026-06-12 17:09 | 38s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-12 19:35 | 2026-06-12 19:36 | 35s | 0 | `T1592` | 🟢 LOW |
| `221.120.41[.]118` | 1 | 2026-06-12 20:32 | 2026-06-12 20:32 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.179.163[.]47` | 1 | 2026-06-12 17:51 | 2026-06-12 17:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-06-12 20:53 | 2026-06-12 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.99.154[.]64` | 1 | 2026-06-12 19:11 | 2026-06-12 19:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `74.208.181[.]249` | 1 | 2026-06-12 18:14 | 2026-06-12 18:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-12 18:33 | 2026-06-12 18:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.106.178[.]197` | 1 | 2026-06-12 16:55 | 2026-06-12 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]161` | 1 | 2026-06-12 17:42 | 2026-06-12 17:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]35` | 1 | 2026-06-12 17:42 | 2026-06-12 17:42 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `74.208.181[.]249` | US | IONOS Inc. | **100** ⚠️ | 3 |
| `176.65.139[.]125` | NL | Storm Industries | **100** ⚠️ | 24 |
| `91.99.6[.]245` | DE | Hetzner Online GmbH | **100** ⚠️ | 0 |
| `90.106.178[.]197` | ES | Orange Spain Network | **100** ⚠️ | 5 |
| `20.221.68[.]159` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `194.187.176[.]183` | DE | Alpha Strike Labs GmbH | **100** ⚠️ | 33 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `221.120.41[.]118` | TW | CHT-Mobile Business Group,Chunghwa | **100** ⚠️ | 34 |
| `128.1.132[.]136` | HK | UCLOUD | **100** ⚠️ | 44 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 587 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (4.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 29 recon entry/entries in table (13 group(s) consolidating 532 session(s)).

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
_Report time: 2026-06-12T21:51:20Z_

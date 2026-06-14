# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T21:17:11Z |
| **Shift Time** | 21:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **83** |
| Confirmed Threats | **42** |
| False Positives Filtered | **41** (49.4%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **13** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **3** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `admin` | 1 |
| `default` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 4 |
| `` | 4 |
| `123@@@` | 2 |
| `smo@@kkklss` | 2 |
| `ubuntu` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 4 |
| `root` | `` | 4 |
| `root` | `123@@@` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `ubuntu` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `165.1.75.106` | 2026-06-14T18:59:48 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-14T18:59:49 |
| `root` | `ubuntu` | `218.90.252.4` | 2026-06-14T19:37:17 |
| `admin` | `admin` | `47.110.149.159` | 2026-06-14T20:05:16 |
| `default` | `tlJwpbo6` | `176.65.148.251` | 2026-06-14T20:33:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T20:48:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T20:48:33 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-14T20:48:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **83** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 18 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 6 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 18 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
| Total IPs Analysed | **34** |
| Unique ASNs | **20** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS24757` | Ethio Telecom | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ab86576b68bb

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-14 18:59 |
| **Last Seen** | 2026-06-14 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:59:48` | `cowrie.session.connect` |
| `2026-06-14 18:59:48` | `cowrie.client.version` |
| `2026-06-14 18:59:48` | `cowrie.client.kex` |
| `2026-06-14 18:59:48` | `cowrie.login.success` |
| `2026-06-14 18:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51ba77a39ec

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-14 18:59 |
| **Last Seen** | 2026-06-14 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:59:48` | `cowrie.session.connect` |
| `2026-06-14 18:59:48` | `cowrie.client.version` |
| `2026-06-14 18:59:48` | `cowrie.client.kex` |
| `2026-06-14 18:59:49` | `cowrie.login.success` |
| `2026-06-14 18:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db5602ef524

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-14 19:00 |
| **Last Seen** | 2026-06-14 19:02 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 19:00:07` | `cowrie.session.connect` |
| `2026-06-14 19:00:07` | `cowrie.client.version` |
| `2026-06-14 19:00:07` | `cowrie.client.kex` |
| `2026-06-14 19:00:08` | `cowrie.login.success` |
| `2026-06-14 19:00:09` | `cowrie.session.file_upload` |
| `2026-06-14 19:00:10` | `cowrie.session.params` |
| `2026-06-14 19:00:10` | `cowrie.command.input` |
| `2026-06-14 19:00:10` | `cowrie.command.input` |
| `2026-06-14 19:00:10` | `cowrie.command.input` |
| `2026-06-14 19:00:10` | `cowrie.command.failed` |
| `2026-06-14 19:00:10` | `cowrie.log.closed` |
| `2026-06-14 19:00:10` | `cowrie.session.params` |
| `2026-06-14 19:00:10` | `cowrie.command.input` |
| `2026-06-14 19:00:11` | `cowrie.log.closed` |
| `2026-06-14 19:00:11` | `cowrie.session.params` |
| `2026-06-14 19:00:11` | `cowrie.command.input` |
| `2026-06-14 19:00:11` | `cowrie.log.closed` |
| `2026-06-14 19:00:12` | `cowrie.session.params` |
| `2026-06-14 19:00:12` | `cowrie.command.input` |
| `2026-06-14 19:00:12` | `cowrie.command.failed` |
| `2026-06-14 19:00:12` | `cowrie.command.failed` |
| `2026-06-14 19:01:13` | `cowrie.session.params` |
| `2026-06-14 19:01:13` | `cowrie.command.input` |
| `2026-06-14 19:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca00f1197bd9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-14 19:02 |
| **Last Seen** | 2026-06-14 19:04 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 19:02:29` | `cowrie.session.connect` |
| `2026-06-14 19:02:29` | `cowrie.client.version` |
| `2026-06-14 19:02:29` | `cowrie.client.kex` |
| `2026-06-14 19:02:29` | `cowrie.login.success` |
| `2026-06-14 19:02:30` | `cowrie.session.file_upload` |
| `2026-06-14 19:02:31` | `cowrie.session.params` |
| `2026-06-14 19:02:31` | `cowrie.command.input` |
| `2026-06-14 19:02:31` | `cowrie.command.input` |
| `2026-06-14 19:02:31` | `cowrie.command.input` |
| `2026-06-14 19:02:31` | `cowrie.command.failed` |
| `2026-06-14 19:02:31` | `cowrie.log.closed` |
| `2026-06-14 19:02:32` | `cowrie.session.params` |
| `2026-06-14 19:02:32` | `cowrie.command.input` |
| `2026-06-14 19:02:32` | `cowrie.log.closed` |
| `2026-06-14 19:02:32` | `cowrie.session.params` |
| `2026-06-14 19:02:32` | `cowrie.command.input` |
| `2026-06-14 19:02:32` | `cowrie.log.closed` |
| `2026-06-14 19:02:33` | `cowrie.session.params` |
| `2026-06-14 19:02:33` | `cowrie.command.input` |
| `2026-06-14 19:02:33` | `cowrie.command.failed` |
| `2026-06-14 19:02:33` | `cowrie.command.failed` |
| `2026-06-14 19:03:34` | `cowrie.session.params` |
| `2026-06-14 19:03:34` | `cowrie.command.input` |
| `2026-06-14 19:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2f49e4a91a

| Field | Detail |
|---|---|
| **Source IP** | `218.90.252[.]4` |
| **First Seen** | 2026-06-14 19:37 |
| **Last Seen** | 2026-06-14 19:38 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 19:37:17` | `cowrie.session.connect` |
| `2026-06-14 19:37:17` | `cowrie.client.version` |
| `2026-06-14 19:37:17` | `cowrie.client.kex` |
| `2026-06-14 19:37:17` | `cowrie.login.success` |
| `2026-06-14 19:38:25` | `cowrie.session.file_upload` |
| `2026-06-14 19:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.90.252[.]4` to AbuseIPDB if not already reported
- [ ] Block `218.90.252[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7b1f525020

| Field | Detail |
|---|---|
| **Source IP** | `47.110.149[.]159` |
| **First Seen** | 2026-06-14 20:03 |
| **Last Seen** | 2026-06-14 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:03:16` | `cowrie.session.connect` |
| `2026-06-14 20:03:17` | `cowrie.telnet.option` |
| `2026-06-14 20:03:17` | `cowrie.telnet.option` |
| `2026-06-14 20:05:16` | `cowrie.login.success` |
| `2026-06-14 20:05:17` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.110.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `47.110.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25deaa0b058f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]251` |
| **First Seen** | 2026-06-14 20:33 |
| **Last Seen** | 2026-06-14 20:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:33:44` | `cowrie.session.connect` |
| `2026-06-14 20:33:45` | `cowrie.login.success` |
| `2026-06-14 20:33:46` | `cowrie.session.params` |
| `2026-06-14 20:33:47` | `cowrie.command.input` |
| `2026-06-14 20:33:47` | `cowrie.command.input` |
| `2026-06-14 20:33:48` | `cowrie.command.input` |
| `2026-06-14 20:33:49` | `cowrie.command.input` |
| `2026-06-14 20:33:49` | `cowrie.command.input` |
| `2026-06-14 20:33:49` | `cowrie.command.failed` |
| `2026-06-14 20:33:50` | `cowrie.log.closed` |
| `2026-06-14 20:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9914fa2088

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 20:48 |
| **Last Seen** | 2026-06-14 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:48:33` | `cowrie.session.connect` |
| `2026-06-14 20:48:33` | `cowrie.client.version` |
| `2026-06-14 20:48:33` | `cowrie.client.kex` |
| `2026-06-14 20:48:33` | `cowrie.login.success` |
| `2026-06-14 20:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181a42ab126e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 20:48 |
| **Last Seen** | 2026-06-14 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:48:33` | `cowrie.session.connect` |
| `2026-06-14 20:48:33` | `cowrie.client.version` |
| `2026-06-14 20:48:33` | `cowrie.client.kex` |
| `2026-06-14 20:48:33` | `cowrie.login.success` |
| `2026-06-14 20:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be222dfe3e43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 20:48 |
| **Last Seen** | 2026-06-14 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:48:36` | `cowrie.session.connect` |
| `2026-06-14 20:48:36` | `cowrie.client.version` |
| `2026-06-14 20:48:36` | `cowrie.client.kex` |
| `2026-06-14 20:48:36` | `cowrie.login.success` |
| `2026-06-14 20:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78221bf761a6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 20:48 |
| **Last Seen** | 2026-06-14 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 20:48:36` | `cowrie.session.connect` |
| `2026-06-14 20:48:36` | `cowrie.client.version` |
| `2026-06-14 20:48:36` | `cowrie.client.kex` |
| `2026-06-14 20:48:36` | `cowrie.login.success` |
| `2026-06-14 20:48:36` | `cowrie.session.closed` |

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
| `188.166.223[.]22` | **9** | 2026-06-14 19:02 | 2026-06-14 20:20 | 7m | 0 | `T1592` | 🟢 LOW |
| `154.16.146[.]65` | **4** | 2026-06-14 19:30 | 2026-06-14 19:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **3** | 2026-06-14 20:32 | 2026-06-14 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]91` | **3** | 2026-06-14 20:32 | 2026-06-14 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]98` | **3** | 2026-06-14 20:33 | 2026-06-14 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-14 19:19 | 2026-06-14 20:20 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `193.8.186[.]29` | **2** | 2026-06-14 20:25 | 2026-06-14 20:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.93[.]206` | 1 | 2026-06-14 19:53 | 2026-06-14 19:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]251` | 1 | 2026-06-14 20:33 | 2026-06-14 20:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.190.224[.]62` | 1 | 2026-06-14 20:54 | 2026-06-14 20:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-06-14 19:03 | 2026-06-14 19:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-14 20:53 | 2026-06-14 20:53 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `134.209.93[.]206` | NL | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `66.132.172[.]128` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `47.110.149[.]159` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `193.8.186[.]29` | GB | Vlad Cojuhari | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 24 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 83 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (49.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 12 recon entry/entries in table (7 group(s) consolidating 26 session(s)).

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
_Report time: 2026-06-14T21:17:11Z_

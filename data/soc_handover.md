# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T23:10:12Z |
| **Shift Time** | 23:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **64** |
| False Positives Filtered | **15** (19.0%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **9** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **2** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 7 |
| `` | 5 |
| `123@@@` | 4 |
| `smo@@kkklss` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 7 |
| `root` | `` | 5 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 2 |
| `admin` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `OVpd4ZIGjw` | `101.133.169.42` | 2026-06-13T21:02:06 |
| `root` | `A9gh4qz1G6` | `101.133.169.42` | 2026-06-13T21:02:06 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-13T21:03:10 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-13T21:03:10 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-13T21:32:44 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-13T21:32:46 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-13T21:32:47 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-13T21:56:38 |
| `root` | `` | `74.208.181.249` | 2026-06-13T22:18:05 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-13T22:26:03 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-13T22:26:03 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-13T22:35:00 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-13T22:35:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **79** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 13 |
| Go SSH scanner | 8 |
| libssh | 6 |
| OpenSSH | 5 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 13 | 4 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 13 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 5 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

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
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `74.208.181.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **18** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | LOW |
| `AS12876` | Scaleway SAS | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-65e2f1bdfa53

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-13 21:03 |
| **Last Seen** | 2026-06-13 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:03:09` | `cowrie.session.connect` |
| `2026-06-13 21:03:09` | `cowrie.client.version` |
| `2026-06-13 21:03:09` | `cowrie.client.kex` |
| `2026-06-13 21:03:10` | `cowrie.login.success` |
| `2026-06-13 21:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2496f429c645

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-13 21:03 |
| **Last Seen** | 2026-06-13 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:03:09` | `cowrie.session.connect` |
| `2026-06-13 21:03:09` | `cowrie.client.version` |
| `2026-06-13 21:03:09` | `cowrie.client.kex` |
| `2026-06-13 21:03:10` | `cowrie.login.success` |
| `2026-06-13 21:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d6d0a7780e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 21:32 |
| **Last Seen** | 2026-06-13 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:32:44` | `cowrie.session.connect` |
| `2026-06-13 21:32:44` | `cowrie.client.version` |
| `2026-06-13 21:32:44` | `cowrie.client.kex` |
| `2026-06-13 21:32:44` | `cowrie.login.success` |
| `2026-06-13 21:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10c270c3a11

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 21:32 |
| **Last Seen** | 2026-06-13 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:32:46` | `cowrie.session.connect` |
| `2026-06-13 21:32:46` | `cowrie.client.version` |
| `2026-06-13 21:32:46` | `cowrie.client.kex` |
| `2026-06-13 21:32:46` | `cowrie.login.success` |
| `2026-06-13 21:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b482baf238

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 21:32 |
| **Last Seen** | 2026-06-13 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:32:47` | `cowrie.session.connect` |
| `2026-06-13 21:32:47` | `cowrie.client.version` |
| `2026-06-13 21:32:47` | `cowrie.client.kex` |
| `2026-06-13 21:32:47` | `cowrie.login.success` |
| `2026-06-13 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c091942ae57f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 21:32 |
| **Last Seen** | 2026-06-13 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:32:47` | `cowrie.session.connect` |
| `2026-06-13 21:32:47` | `cowrie.client.version` |
| `2026-06-13 21:32:47` | `cowrie.client.kex` |
| `2026-06-13 21:32:48` | `cowrie.login.success` |
| `2026-06-13 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc54c490f46

| Field | Detail |
|---|---|
| **Source IP** | `74.208.181[.]249` |
| **First Seen** | 2026-06-13 22:18 |
| **Last Seen** | 2026-06-13 22:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:18:05` | `cowrie.session.connect` |
| `2026-06-13 22:18:05` | `cowrie.login.success` |
| `2026-06-13 22:18:06` | `cowrie.session.params` |
| `2026-06-13 22:18:06` | `cowrie.command.input` |
| `2026-06-13 22:18:07` | `cowrie.command.input` |
| `2026-06-13 22:18:07` | `cowrie.command.input` |
| `2026-06-13 22:18:08` | `cowrie.command.input` |
| `2026-06-13 22:18:08` | `cowrie.command.failed` |
| `2026-06-13 22:18:09` | `cowrie.log.closed` |
| `2026-06-13 22:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.181[.]249` to AbuseIPDB if not already reported
- [ ] Block `74.208.181[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2dbc312c0b

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 22:26 |
| **Last Seen** | 2026-06-13 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:26:01` | `cowrie.session.connect` |
| `2026-06-13 22:26:01` | `cowrie.client.version` |
| `2026-06-13 22:26:02` | `cowrie.client.kex` |
| `2026-06-13 22:26:03` | `cowrie.login.success` |
| `2026-06-13 22:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001258a52260

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 22:26 |
| **Last Seen** | 2026-06-13 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:26:02` | `cowrie.session.connect` |
| `2026-06-13 22:26:02` | `cowrie.client.version` |
| `2026-06-13 22:26:02` | `cowrie.client.kex` |
| `2026-06-13 22:26:03` | `cowrie.login.success` |
| `2026-06-13 22:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10f4a7c87ec

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 22:26 |
| **Last Seen** | 2026-06-13 22:28 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:26:20` | `cowrie.session.connect` |
| `2026-06-13 22:26:20` | `cowrie.client.version` |
| `2026-06-13 22:26:20` | `cowrie.client.kex` |
| `2026-06-13 22:26:21` | `cowrie.login.success` |
| `2026-06-13 22:26:24` | `cowrie.session.file_upload` |
| `2026-06-13 22:26:25` | `cowrie.session.params` |
| `2026-06-13 22:26:25` | `cowrie.command.input` |
| `2026-06-13 22:26:25` | `cowrie.command.input` |
| `2026-06-13 22:26:25` | `cowrie.command.input` |
| `2026-06-13 22:26:25` | `cowrie.command.failed` |
| `2026-06-13 22:26:25` | `cowrie.log.closed` |
| `2026-06-13 22:26:26` | `cowrie.session.params` |
| `2026-06-13 22:26:26` | `cowrie.command.input` |
| `2026-06-13 22:26:27` | `cowrie.log.closed` |
| `2026-06-13 22:26:28` | `cowrie.session.params` |
| `2026-06-13 22:26:28` | `cowrie.command.input` |
| `2026-06-13 22:26:28` | `cowrie.log.closed` |
| `2026-06-13 22:26:29` | `cowrie.session.params` |
| `2026-06-13 22:26:29` | `cowrie.command.input` |
| `2026-06-13 22:26:29` | `cowrie.command.failed` |
| `2026-06-13 22:26:29` | `cowrie.command.failed` |
| `2026-06-13 22:27:31` | `cowrie.session.params` |
| `2026-06-13 22:27:31` | `cowrie.command.input` |
| `2026-06-13 22:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7dc5054df3

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-13 22:34 |
| **Last Seen** | 2026-06-13 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:34:59` | `cowrie.session.connect` |
| `2026-06-13 22:34:59` | `cowrie.client.version` |
| `2026-06-13 22:34:59` | `cowrie.client.kex` |
| `2026-06-13 22:35:00` | `cowrie.login.success` |
| `2026-06-13 22:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065e62e5246c

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-13 22:35 |
| **Last Seen** | 2026-06-13 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:35:01` | `cowrie.session.connect` |
| `2026-06-13 22:35:01` | `cowrie.client.version` |
| `2026-06-13 22:35:01` | `cowrie.client.kex` |
| `2026-06-13 22:35:01` | `cowrie.login.success` |
| `2026-06-13 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52980a104a6a

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-13 22:35 |
| **Last Seen** | 2026-06-13 22:37 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:35:17` | `cowrie.session.connect` |
| `2026-06-13 22:35:17` | `cowrie.client.version` |
| `2026-06-13 22:35:17` | `cowrie.client.kex` |
| `2026-06-13 22:35:17` | `cowrie.login.success` |
| `2026-06-13 22:35:19` | `cowrie.session.file_upload` |
| `2026-06-13 22:35:19` | `cowrie.session.params` |
| `2026-06-13 22:35:19` | `cowrie.command.input` |
| `2026-06-13 22:35:19` | `cowrie.command.input` |
| `2026-06-13 22:35:19` | `cowrie.command.input` |
| `2026-06-13 22:35:19` | `cowrie.command.failed` |
| `2026-06-13 22:35:19` | `cowrie.log.closed` |
| `2026-06-13 22:35:20` | `cowrie.session.params` |
| `2026-06-13 22:35:20` | `cowrie.command.input` |
| `2026-06-13 22:35:20` | `cowrie.log.closed` |
| `2026-06-13 22:35:21` | `cowrie.session.params` |
| `2026-06-13 22:35:21` | `cowrie.command.input` |
| `2026-06-13 22:35:21` | `cowrie.log.closed` |
| `2026-06-13 22:35:22` | `cowrie.session.params` |
| `2026-06-13 22:35:22` | `cowrie.command.input` |
| `2026-06-13 22:35:22` | `cowrie.command.failed` |
| `2026-06-13 22:35:22` | `cowrie.command.failed` |
| `2026-06-13 22:36:23` | `cowrie.session.params` |
| `2026-06-13 22:36:23` | `cowrie.command.input` |
| `2026-06-13 22:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9173eb1a1a

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-13 22:37 |
| **Last Seen** | 2026-06-13 22:39 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:37:39` | `cowrie.session.connect` |
| `2026-06-13 22:37:39` | `cowrie.client.version` |
| `2026-06-13 22:37:39` | `cowrie.client.kex` |
| `2026-06-13 22:37:40` | `cowrie.login.success` |
| `2026-06-13 22:37:41` | `cowrie.session.file_upload` |
| `2026-06-13 22:37:41` | `cowrie.session.params` |
| `2026-06-13 22:37:41` | `cowrie.command.input` |
| `2026-06-13 22:37:41` | `cowrie.command.input` |
| `2026-06-13 22:37:41` | `cowrie.command.input` |
| `2026-06-13 22:37:41` | `cowrie.command.failed` |
| `2026-06-13 22:37:41` | `cowrie.log.closed` |
| `2026-06-13 22:37:42` | `cowrie.session.params` |
| `2026-06-13 22:37:42` | `cowrie.command.input` |
| `2026-06-13 22:37:42` | `cowrie.log.closed` |
| `2026-06-13 22:37:43` | `cowrie.session.params` |
| `2026-06-13 22:37:43` | `cowrie.command.input` |
| `2026-06-13 22:37:43` | `cowrie.log.closed` |
| `2026-06-13 22:37:44` | `cowrie.session.params` |
| `2026-06-13 22:37:44` | `cowrie.command.input` |
| `2026-06-13 22:37:44` | `cowrie.command.failed` |
| `2026-06-13 22:37:44` | `cowrie.command.failed` |
| `2026-06-13 22:38:45` | `cowrie.session.params` |
| `2026-06-13 22:38:45` | `cowrie.command.input` |
| `2026-06-13 22:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **19** | 2026-06-13 20:55 | 2026-06-13 22:44 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **9** | 2026-06-13 20:56 | 2026-06-13 22:50 | 5m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-06-13 21:04 | 2026-06-13 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | **3** | 2026-06-13 21:17 | 2026-06-13 21:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-13 21:29 | 2026-06-13 22:29 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.171.8[.]85` | **2** | 2026-06-13 21:05 | 2026-06-13 21:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.28.214[.]81` | 1 | 2026-06-13 21:29 | 2026-06-13 21:29 | 17s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-13 21:13 | 2026-06-13 21:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-13 22:05 | 2026-06-13 22:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]164` | 1 | 2026-06-13 21:22 | 2026-06-13 21:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]165` | 1 | 2026-06-13 21:22 | 2026-06-13 21:22 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]167` | 1 | 2026-06-13 21:22 | 2026-06-13 21:22 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-06-13 21:16 | 2026-06-13 21:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-13 22:23 | 2026-06-13 22:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `74.208.181[.]249` | 1 | 2026-06-13 22:18 | 2026-06-13 22:18 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `45.156.129[.]164` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `74.208.181[.]249` | US | IONOS Inc. | **100** ⚠️ | 13 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 1 |
| `45.156.129[.]167` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `172.236.228[.]224` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (19.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 41 session(s)).

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
_Report time: 2026-06-13T23:10:12Z_

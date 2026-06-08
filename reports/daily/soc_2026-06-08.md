# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T08:13:29Z |
| **Shift Time** | 08:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **81** |
| Confirmed Threats | **67** |
| False Positives Filtered | **14** (17.3%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **11** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **5** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `admin` | 3 |
| `CONNECT www.baidu.com:443 HTTP/1.1` | 2 |
| `GET / HTTP/1.1` | 1 |
| `sol` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 9 |
| `admin` | 3 |
| `123@@@` | 3 |
| `` | 3 |
| `Host: www.baidu.com:443` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 9 |
| `admin` | `admin` | 3 |
| `root` | `123@@@` | 3 |
| `root` | `` | 3 |
| `CONNECT www.baidu.com:443 HTTP/1.1` | `Host: www.baidu.com:443` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `183.222.14.9` | 2026-06-08T06:20:35 |
| `CONNECT www.baidu.com:443 HTTP/1.1` | `Host: www.baidu.com:443` | `130.61.23.223` | 2026-06-08T06:25:15 |
| `root` | `123@@@` | `161.118.136.222` | 2026-06-08T06:32:10 |
| `root` | `LeitboGi0ro` | `161.118.136.222` | 2026-06-08T06:32:10 |
| `root` | `123@@@` | `155.248.205.117` | 2026-06-08T07:06:23 |
| `root` | `LeitboGi0ro` | `155.248.205.117` | 2026-06-08T07:06:23 |
| `admin` | `admin` | `107.172.204.15` | 2026-06-08T07:06:45 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-08T07:06:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.20.69` | 2026-06-08T07:14:22 |
| `root` | `` | `176.65.139.151` | 2026-06-08T07:17:12 |
| `root` | `` | `64.89.162.139` | 2026-06-08T07:22:35 |
| `root` | `LeitboGi0ro` | `161.118.237.181` | 2026-06-08T07:24:31 |
| `root` | `123@@@` | `161.118.237.181` | 2026-06-08T07:24:31 |
| `root` | `` | `10.0.0.73` | 2026-06-08T07:38:13 |
| `sol` | `sol` | `2.57.122.238` | 2026-06-08T08:02:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **81** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 12 |
| Unknown | 3 |
| libssh | 2 |
| Go SSH scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `6372ee695756...` | Modern SSH client | 8 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `5f904648ee89...` | Generic scanner | 1 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 3 | 2 | — |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `eeca2460550b...` | OpenSSH | 1 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
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
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.151`, `64.89.162.139`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS214472` | Offshore LC | 2 | HIGH |
| `AS36352` | HostPapa | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS56040` | China Mobile communications corporation | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-17b1693faf3b

| Field | Detail |
|---|---|
| **Source IP** | `183.222.14[.]9` |
| **First Seen** | 2026-06-08 06:20 |
| **Last Seen** | 2026-06-08 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:20:35` | `cowrie.login.success` |
| `2026-06-08 06:20:35` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `183.222.14[.]9` to AbuseIPDB if not already reported
- [ ] Block `183.222.14[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7446a35c82a2

| Field | Detail |
|---|---|
| **Source IP** | `130.61.23[.]223` |
| **First Seen** | 2026-06-08 06:25 |
| **Last Seen** | 2026-06-08 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:25:15` | `cowrie.session.connect` |
| `2026-06-08 06:25:15` | `cowrie.login.success` |
| `2026-06-08 06:25:15` | `cowrie.session.params` |
| `2026-06-08 06:25:15` | `cowrie.command.input` |
| `2026-06-08 06:25:15` | `cowrie.command.failed` |
| `2026-06-08 06:25:15` | `cowrie.command.input` |
| `2026-06-08 06:25:15` | `cowrie.log.closed` |
| `2026-06-08 06:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.23[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.61.23[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563e301fa153

| Field | Detail |
|---|---|
| **Source IP** | `130.61.23[.]223` |
| **First Seen** | 2026-06-08 06:25 |
| **Last Seen** | 2026-06-08 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:25:15` | `cowrie.session.connect` |
| `2026-06-08 06:25:15` | `cowrie.login.success` |
| `2026-06-08 06:25:16` | `cowrie.session.params` |
| `2026-06-08 06:25:16` | `cowrie.command.input` |
| `2026-06-08 06:25:16` | `cowrie.command.failed` |
| `2026-06-08 06:25:16` | `cowrie.command.input` |
| `2026-06-08 06:25:16` | `cowrie.log.closed` |
| `2026-06-08 06:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.23[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.61.23[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36ac8c8a414

| Field | Detail |
|---|---|
| **Source IP** | `161.118.136[.]222` |
| **First Seen** | 2026-06-08 06:32 |
| **Last Seen** | 2026-06-08 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:32:09` | `cowrie.session.connect` |
| `2026-06-08 06:32:09` | `cowrie.client.version` |
| `2026-06-08 06:32:09` | `cowrie.client.kex` |
| `2026-06-08 06:32:10` | `cowrie.login.success` |
| `2026-06-08 06:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.136[.]222` to AbuseIPDB if not already reported
- [ ] Block `161.118.136[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8fdc304479

| Field | Detail |
|---|---|
| **Source IP** | `161.118.136[.]222` |
| **First Seen** | 2026-06-08 06:32 |
| **Last Seen** | 2026-06-08 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:32:09` | `cowrie.session.connect` |
| `2026-06-08 06:32:09` | `cowrie.client.version` |
| `2026-06-08 06:32:09` | `cowrie.client.kex` |
| `2026-06-08 06:32:10` | `cowrie.login.success` |
| `2026-06-08 06:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.136[.]222` to AbuseIPDB if not already reported
- [ ] Block `161.118.136[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0c73d8b9f6

| Field | Detail |
|---|---|
| **Source IP** | `161.118.136[.]222` |
| **First Seen** | 2026-06-08 06:32 |
| **Last Seen** | 2026-06-08 06:34 |
| **Session Duration** | 134s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:32:30` | `cowrie.session.connect` |
| `2026-06-08 06:32:30` | `cowrie.client.version` |
| `2026-06-08 06:32:30` | `cowrie.client.kex` |
| `2026-06-08 06:32:31` | `cowrie.login.success` |
| `2026-06-08 06:32:33` | `cowrie.session.file_upload` |
| `2026-06-08 06:32:34` | `cowrie.session.params` |
| `2026-06-08 06:32:34` | `cowrie.command.input` |
| `2026-06-08 06:32:34` | `cowrie.command.input` |
| `2026-06-08 06:32:34` | `cowrie.command.input` |
| `2026-06-08 06:32:34` | `cowrie.command.failed` |
| `2026-06-08 06:32:34` | `cowrie.log.closed` |
| `2026-06-08 06:32:35` | `cowrie.session.params` |
| `2026-06-08 06:32:35` | `cowrie.command.input` |
| `2026-06-08 06:32:35` | `cowrie.log.closed` |
| `2026-06-08 06:32:36` | `cowrie.session.params` |
| `2026-06-08 06:32:36` | `cowrie.command.input` |
| `2026-06-08 06:32:36` | `cowrie.log.closed` |
| `2026-06-08 06:32:37` | `cowrie.session.params` |
| `2026-06-08 06:32:37` | `cowrie.command.input` |
| `2026-06-08 06:32:37` | `cowrie.command.failed` |
| `2026-06-08 06:32:37` | `cowrie.command.failed` |
| `2026-06-08 06:33:39` | `cowrie.session.params` |
| `2026-06-08 06:33:39` | `cowrie.command.input` |
| `2026-06-08 06:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.136[.]222` to AbuseIPDB if not already reported
- [ ] Block `161.118.136[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ba2dc7b7c4

| Field | Detail |
|---|---|
| **Source IP** | `161.118.136[.]222` |
| **First Seen** | 2026-06-08 06:35 |
| **Last Seen** | 2026-06-08 06:37 |
| **Session Duration** | 134s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:35:00` | `cowrie.session.connect` |
| `2026-06-08 06:35:00` | `cowrie.client.version` |
| `2026-06-08 06:35:00` | `cowrie.client.kex` |
| `2026-06-08 06:35:01` | `cowrie.login.success` |
| `2026-06-08 06:35:03` | `cowrie.session.file_upload` |
| `2026-06-08 06:35:04` | `cowrie.session.params` |
| `2026-06-08 06:35:04` | `cowrie.command.input` |
| `2026-06-08 06:35:04` | `cowrie.command.input` |
| `2026-06-08 06:35:04` | `cowrie.command.input` |
| `2026-06-08 06:35:04` | `cowrie.command.failed` |
| `2026-06-08 06:35:04` | `cowrie.log.closed` |
| `2026-06-08 06:35:05` | `cowrie.session.params` |
| `2026-06-08 06:35:05` | `cowrie.command.input` |
| `2026-06-08 06:35:05` | `cowrie.log.closed` |
| `2026-06-08 06:35:06` | `cowrie.session.params` |
| `2026-06-08 06:35:06` | `cowrie.command.input` |
| `2026-06-08 06:35:06` | `cowrie.log.closed` |
| `2026-06-08 06:35:07` | `cowrie.session.params` |
| `2026-06-08 06:35:07` | `cowrie.command.input` |
| `2026-06-08 06:35:07` | `cowrie.command.failed` |
| `2026-06-08 06:35:07` | `cowrie.command.failed` |
| `2026-06-08 06:36:08` | `cowrie.session.params` |
| `2026-06-08 06:36:08` | `cowrie.command.input` |
| `2026-06-08 06:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.136[.]222` to AbuseIPDB if not already reported
- [ ] Block `161.118.136[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f8288dbf8d

| Field | Detail |
|---|---|
| **Source IP** | `155.248.205[.]117` |
| **First Seen** | 2026-06-08 07:06 |
| **Last Seen** | 2026-06-08 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:06:23` | `cowrie.session.connect` |
| `2026-06-08 07:06:23` | `cowrie.client.version` |
| `2026-06-08 07:06:23` | `cowrie.client.kex` |
| `2026-06-08 07:06:23` | `cowrie.login.success` |
| `2026-06-08 07:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.248.205[.]117` to AbuseIPDB if not already reported
- [ ] Block `155.248.205[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c1349cf540

| Field | Detail |
|---|---|
| **Source IP** | `155.248.205[.]117` |
| **First Seen** | 2026-06-08 07:06 |
| **Last Seen** | 2026-06-08 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:06:23` | `cowrie.session.connect` |
| `2026-06-08 07:06:23` | `cowrie.client.version` |
| `2026-06-08 07:06:23` | `cowrie.client.kex` |
| `2026-06-08 07:06:23` | `cowrie.login.success` |
| `2026-06-08 07:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.248.205[.]117` to AbuseIPDB if not already reported
- [ ] Block `155.248.205[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97335f6d260

| Field | Detail |
|---|---|
| **Source IP** | `155.248.205[.]117` |
| **First Seen** | 2026-06-08 07:06 |
| **Last Seen** | 2026-06-08 07:08 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:06:42` | `cowrie.session.connect` |
| `2026-06-08 07:06:42` | `cowrie.client.version` |
| `2026-06-08 07:06:42` | `cowrie.client.kex` |
| `2026-06-08 07:06:42` | `cowrie.login.success` |
| `2026-06-08 07:06:43` | `cowrie.session.file_upload` |
| `2026-06-08 07:06:44` | `cowrie.session.params` |
| `2026-06-08 07:06:44` | `cowrie.command.input` |
| `2026-06-08 07:06:44` | `cowrie.command.input` |
| `2026-06-08 07:06:44` | `cowrie.command.input` |
| `2026-06-08 07:06:44` | `cowrie.command.failed` |
| `2026-06-08 07:06:44` | `cowrie.log.closed` |
| `2026-06-08 07:06:44` | `cowrie.session.params` |
| `2026-06-08 07:06:44` | `cowrie.command.input` |
| `2026-06-08 07:06:45` | `cowrie.log.closed` |
| `2026-06-08 07:06:45` | `cowrie.session.params` |
| `2026-06-08 07:06:45` | `cowrie.command.input` |
| `2026-06-08 07:06:45` | `cowrie.log.closed` |
| `2026-06-08 07:06:46` | `cowrie.session.params` |
| `2026-06-08 07:06:46` | `cowrie.command.input` |
| `2026-06-08 07:06:46` | `cowrie.command.failed` |
| `2026-06-08 07:06:46` | `cowrie.command.failed` |
| `2026-06-08 07:07:47` | `cowrie.session.params` |
| `2026-06-08 07:07:47` | `cowrie.command.input` |
| `2026-06-08 07:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.248.205[.]117` to AbuseIPDB if not already reported
- [ ] Block `155.248.205[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1119e00a54

| Field | Detail |
|---|---|
| **Source IP** | `107.172.204[.]15` |
| **First Seen** | 2026-06-08 07:06 |
| **Last Seen** | 2026-06-08 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:06:44` | `cowrie.session.connect` |
| `2026-06-08 07:06:44` | `cowrie.client.version` |
| `2026-06-08 07:06:45` | `cowrie.client.kex` |
| `2026-06-08 07:06:45` | `cowrie.login.success` |
| `2026-06-08 07:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.204[.]15` to AbuseIPDB if not already reported
- [ ] Block `107.172.204[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af19a7cfdac

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-08 07:06 |
| **Last Seen** | 2026-06-08 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:06:46` | `cowrie.session.connect` |
| `2026-06-08 07:06:46` | `cowrie.client.version` |
| `2026-06-08 07:06:46` | `cowrie.client.kex` |
| `2026-06-08 07:06:47` | `cowrie.login.success` |
| `2026-06-08 07:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38482ab38319

| Field | Detail |
|---|---|
| **Source IP** | `155.248.205[.]117` |
| **First Seen** | 2026-06-08 07:09 |
| **Last Seen** | 2026-06-08 07:11 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:09:07` | `cowrie.session.connect` |
| `2026-06-08 07:09:07` | `cowrie.client.version` |
| `2026-06-08 07:09:07` | `cowrie.client.kex` |
| `2026-06-08 07:09:07` | `cowrie.login.success` |
| `2026-06-08 07:09:09` | `cowrie.session.file_upload` |
| `2026-06-08 07:09:09` | `cowrie.session.params` |
| `2026-06-08 07:09:09` | `cowrie.command.input` |
| `2026-06-08 07:09:09` | `cowrie.command.input` |
| `2026-06-08 07:09:09` | `cowrie.command.input` |
| `2026-06-08 07:09:09` | `cowrie.command.failed` |
| `2026-06-08 07:09:09` | `cowrie.log.closed` |
| `2026-06-08 07:09:10` | `cowrie.session.params` |
| `2026-06-08 07:09:10` | `cowrie.command.input` |
| `2026-06-08 07:09:10` | `cowrie.log.closed` |
| `2026-06-08 07:09:11` | `cowrie.session.params` |
| `2026-06-08 07:09:11` | `cowrie.command.input` |
| `2026-06-08 07:09:11` | `cowrie.log.closed` |
| `2026-06-08 07:09:12` | `cowrie.session.params` |
| `2026-06-08 07:09:12` | `cowrie.command.input` |
| `2026-06-08 07:09:12` | `cowrie.command.failed` |
| `2026-06-08 07:09:12` | `cowrie.command.failed` |
| `2026-06-08 07:10:12` | `cowrie.session.params` |
| `2026-06-08 07:10:12` | `cowrie.command.input` |
| `2026-06-08 07:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.248.205[.]117` to AbuseIPDB if not already reported
- [ ] Block `155.248.205[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e584713b5b

| Field | Detail |
|---|---|
| **Source IP** | `65.49.20[.]69` |
| **First Seen** | 2026-06-08 07:14 |
| **Last Seen** | 2026-06-08 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0[.]0 Safari/537.36 OPR/120.0.0[.]0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:14:22` | `cowrie.session.connect` |
| `2026-06-08 07:14:22` | `cowrie.login.success` |
| `2026-06-08 07:14:22` | `cowrie.session.params` |
| `2026-06-08 07:14:22` | `cowrie.command.input` |
| `2026-06-08 07:14:22` | `cowrie.command.input` |
| `2026-06-08 07:14:22` | `cowrie.command.failed` |
| `2026-06-08 07:14:22` | `cowrie.command.input` |
| `2026-06-08 07:14:22` | `cowrie.command.failed` |
| `2026-06-08 07:14:22` | `cowrie.command.input` |
| `2026-06-08 07:14:22` | `cowrie.log.closed` |
| `2026-06-08 07:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.20[.]69` to AbuseIPDB if not already reported
- [ ] Block `65.49.20[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e3121819ff

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]151` |
| **First Seen** | 2026-06-08 07:17 |
| **Last Seen** | 2026-06-08 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:17:12` | `cowrie.session.connect` |
| `2026-06-08 07:17:12` | `cowrie.login.success` |
| `2026-06-08 07:17:13` | `cowrie.session.params` |
| `2026-06-08 07:17:13` | `cowrie.command.input` |
| `2026-06-08 07:17:14` | `cowrie.command.input` |
| `2026-06-08 07:17:15` | `cowrie.command.input` |
| `2026-06-08 07:17:15` | `cowrie.command.input` |
| `2026-06-08 07:17:15` | `cowrie.command.failed` |
| `2026-06-08 07:17:16` | `cowrie.log.closed` |
| `2026-06-08 07:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]151` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9100fe64a0b8

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]139` |
| **First Seen** | 2026-06-08 07:22 |
| **Last Seen** | 2026-06-08 07:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:22:35` | `cowrie.session.connect` |
| `2026-06-08 07:22:35` | `cowrie.login.success` |
| `2026-06-08 07:22:36` | `cowrie.session.params` |
| `2026-06-08 07:22:36` | `cowrie.command.input` |
| `2026-06-08 07:22:37` | `cowrie.command.input` |
| `2026-06-08 07:22:37` | `cowrie.command.input` |
| `2026-06-08 07:22:38` | `cowrie.command.input` |
| `2026-06-08 07:22:38` | `cowrie.command.failed` |
| `2026-06-08 07:22:39` | `cowrie.log.closed` |
| `2026-06-08 07:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]139` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36f13601993

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-08 07:24 |
| **Last Seen** | 2026-06-08 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:24:30` | `cowrie.session.connect` |
| `2026-06-08 07:24:30` | `cowrie.client.version` |
| `2026-06-08 07:24:30` | `cowrie.client.kex` |
| `2026-06-08 07:24:31` | `cowrie.login.success` |
| `2026-06-08 07:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc8128b8be8

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-08 07:24 |
| **Last Seen** | 2026-06-08 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:24:30` | `cowrie.session.connect` |
| `2026-06-08 07:24:30` | `cowrie.client.version` |
| `2026-06-08 07:24:30` | `cowrie.client.kex` |
| `2026-06-08 07:24:31` | `cowrie.login.success` |
| `2026-06-08 07:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446144e83849

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-08 07:24 |
| **Last Seen** | 2026-06-08 07:27 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:24:52` | `cowrie.session.connect` |
| `2026-06-08 07:24:52` | `cowrie.client.version` |
| `2026-06-08 07:24:52` | `cowrie.client.kex` |
| `2026-06-08 07:24:53` | `cowrie.login.success` |
| `2026-06-08 07:24:55` | `cowrie.session.file_upload` |
| `2026-06-08 07:24:57` | `cowrie.session.params` |
| `2026-06-08 07:24:57` | `cowrie.command.input` |
| `2026-06-08 07:24:57` | `cowrie.command.input` |
| `2026-06-08 07:24:57` | `cowrie.command.input` |
| `2026-06-08 07:24:57` | `cowrie.command.failed` |
| `2026-06-08 07:24:57` | `cowrie.log.closed` |
| `2026-06-08 07:24:58` | `cowrie.session.params` |
| `2026-06-08 07:24:58` | `cowrie.command.input` |
| `2026-06-08 07:24:58` | `cowrie.log.closed` |
| `2026-06-08 07:24:59` | `cowrie.session.params` |
| `2026-06-08 07:24:59` | `cowrie.command.input` |
| `2026-06-08 07:24:59` | `cowrie.log.closed` |
| `2026-06-08 07:25:01` | `cowrie.session.params` |
| `2026-06-08 07:25:01` | `cowrie.command.input` |
| `2026-06-08 07:25:01` | `cowrie.command.failed` |
| `2026-06-08 07:25:01` | `cowrie.command.failed` |
| `2026-06-08 07:26:02` | `cowrie.session.params` |
| `2026-06-08 07:26:02` | `cowrie.command.input` |
| `2026-06-08 07:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d89b426cd0

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-08 07:27 |
| **Last Seen** | 2026-06-08 07:29 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:27:18` | `cowrie.session.connect` |
| `2026-06-08 07:27:18` | `cowrie.client.version` |
| `2026-06-08 07:27:18` | `cowrie.client.kex` |
| `2026-06-08 07:27:19` | `cowrie.login.success` |
| `2026-06-08 07:27:22` | `cowrie.session.file_upload` |
| `2026-06-08 07:27:23` | `cowrie.session.params` |
| `2026-06-08 07:27:23` | `cowrie.command.input` |
| `2026-06-08 07:27:23` | `cowrie.command.input` |
| `2026-06-08 07:27:23` | `cowrie.command.input` |
| `2026-06-08 07:27:23` | `cowrie.command.failed` |
| `2026-06-08 07:27:23` | `cowrie.log.closed` |
| `2026-06-08 07:27:24` | `cowrie.session.params` |
| `2026-06-08 07:27:24` | `cowrie.command.input` |
| `2026-06-08 07:27:24` | `cowrie.log.closed` |
| `2026-06-08 07:27:26` | `cowrie.session.params` |
| `2026-06-08 07:27:26` | `cowrie.command.input` |
| `2026-06-08 07:27:26` | `cowrie.log.closed` |
| `2026-06-08 07:27:27` | `cowrie.session.params` |
| `2026-06-08 07:27:27` | `cowrie.command.input` |
| `2026-06-08 07:27:27` | `cowrie.command.failed` |
| `2026-06-08 07:27:27` | `cowrie.command.failed` |
| `2026-06-08 07:28:28` | `cowrie.session.params` |
| `2026-06-08 07:28:28` | `cowrie.command.input` |
| `2026-06-08 07:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a7bbab7c4a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:02 |
| **Last Seen** | 2026-06-08 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:02:39` | `cowrie.session.connect` |
| `2026-06-08 08:02:39` | `cowrie.client.version` |
| `2026-06-08 08:02:39` | `cowrie.client.kex` |
| `2026-06-08 08:02:39` | `cowrie.login.success` |
| `2026-06-08 08:02:40` | `cowrie.session.params` |
| `2026-06-08 08:02:40` | `cowrie.command.input` |
| `2026-06-08 08:02:40` | `cowrie.log.closed` |
| `2026-06-08 08:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.174.155[.]67` | **20** | 2026-06-08 06:31 | 2026-06-08 07:53 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **10** | 2026-06-08 06:21 | 2026-06-08 07:58 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `123.88.103[.]173` | **4** | 2026-06-08 06:20 | 2026-06-08 06:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `182.72.90[.]110` | **2** | 2026-06-08 07:40 | 2026-06-08 07:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.40[.]100` | **2** | 2026-06-08 06:32 | 2026-06-08 06:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]151` | 1 | 2026-06-08 07:17 | 2026-06-08 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]41` | 1 | 2026-06-08 07:52 | 2026-06-08 07:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.180.48[.]56` | 1 | 2026-06-08 06:52 | 2026-06-08 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-06-08 08:00 | 2026-06-08 08:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-08 07:08 | 2026-06-08 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-06-08 06:36 | 2026-06-08 06:37 | 8s | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]139` | 1 | 2026-06-08 07:22 | 2026-06-08 07:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-06-08 06:33 | 2026-06-08 06:33 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `183.222.14[.]9` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `66.228.40[.]100` | US | Linode | **100** ⚠️ | 12 |
| `123.88.103[.]173` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `64.89.162[.]139` | NL | PIO-Hosting GmbH | **100** ⚠️ | 11 |
| `182.72.90[.]110` | IN | SONA WINES LTD | **100** ⚠️ | 9 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `65.49.1[.]132` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 50 |
| `107.172.204[.]15` | US | HostPapa | **100** ⚠️ | 19 |
| `194.180.48[.]56` | PL | Neterra Ltd. | **100** ⚠️ | 6 |
| `161.118.136[.]222` | KR | 500 Oracle Parkway | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 21 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 81 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (17.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 13 recon entry/entries in table (5 group(s) consolidating 38 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-06-08T08:13:29Z_

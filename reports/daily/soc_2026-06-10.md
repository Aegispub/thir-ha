# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T18:33:41Z |
| **Shift Time** | 18:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **290** |
| Confirmed Threats | **270** |
| False Positives Filtered | **20** (6.9%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **10** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **240** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **17** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `solana` | 7 |
| `sol` | 6 |
| `solv` | 4 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 5 |
| `123@@@` | 3 |
| `solana` | 2 |
| `12345678` | 2 |
| `ubuntu` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `root` | `123@@@` | 3 |
| `solana` | `solana` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `ubuntu` | `1q2w3e4r` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `1q2w3e4r` | `80.94.92.182` | 2026-06-10T14:55:55 |
| `ubuntu` | `1qq2w3e4r5t` | `80.94.92.182` | 2026-06-10T14:59:58 |
| `minima` | `minima` | `80.94.92.182` | 2026-06-10T15:03:41 |
| `sol` | `sol` | `2.57.122.238` | 2026-06-10T15:04:31 |
| `solana` | `solana` | `2.57.122.238` | 2026-06-10T15:06:57 |
| `ops` | `ops` | `80.94.92.182` | 2026-06-10T15:07:34 |
| `solv` | `solv` | `2.57.122.238` | 2026-06-10T15:09:17 |
| `operation` | `operation` | `80.94.92.182` | 2026-06-10T15:11:14 |
| `solv` | `1234` | `2.57.122.238` | 2026-06-10T15:11:33 |
| `root` | `LeitboGi0ro` | `139.59.227.143` | 2026-06-10T15:13:28 |
| `root` | `MoeClub.org` | `139.59.227.143` | 2026-06-10T15:13:32 |
| `solv` | `123456` | `2.57.122.238` | 2026-06-10T15:13:47 |
| `admin` | `admin` | `176.65.139.130` | 2026-06-10T15:14:04 |
| `opadmin` | `opadmin` | `80.94.92.182` | 2026-06-10T15:15:07 |
| `solv` | `12345678` | `2.57.122.238` | 2026-06-10T15:15:53 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-06-10T15:18:01 |
| `psadmin` | `psadmin` | `80.94.92.182` | 2026-06-10T15:19:02 |
| `node` | `node` | `2.57.122.238` | 2026-06-10T15:20:14 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-06-10T15:22:26 |
| `root` | `fuckyou` | `80.94.92.182` | 2026-06-10T15:22:52 |
| `validator` | `validator` | `2.57.122.238` | 2026-06-10T15:24:41 |
| `root` | `fuckoff` | `80.94.92.182` | 2026-06-10T15:26:40 |
| `sol` | `sol123` | `2.57.122.238` | 2026-06-10T15:27:00 |
| `sol` | `123` | `2.57.122.238` | 2026-06-10T15:29:07 |
| `user` | `imzadi` | `2.57.121.25` | 2026-06-10T15:30:16 |
| `solana` | `solana` | `80.94.92.182` | 2026-06-10T15:30:29 |
| `sol` | `12345678` | `2.57.122.238` | 2026-06-10T15:31:19 |
| `solana` | `1234567890-=` | `80.94.92.182` | 2026-06-10T15:34:16 |
| `solana` | `qwer1234` | `80.94.92.182` | 2026-06-10T15:37:55 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-10T15:39:45 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-10T15:39:45 |
| `sol` | `ZXCVASDFQWER!@#$` | `80.94.92.182` | 2026-06-10T15:41:46 |
| `root` | `5nWt3P-fF4WosQm5O` | `2.57.121.112` | 2026-06-10T15:43:48 |
| `sana` | `sana` | `213.209.159.56` | 2026-06-10T15:45:28 |
| `sol` | `zxcvasdfqwer@1234` | `80.94.92.182` | 2026-06-10T15:45:30 |
| `root` | `!@#$%^` | `80.94.92.182` | 2026-06-10T15:49:24 |
| `solana` | `!@#$%^` | `80.94.92.182` | 2026-06-10T15:53:06 |
| `solana` | `pa2ssw0rd` | `80.94.92.182` | 2026-06-10T15:56:19 |
| `solana` | `p@ssw0rd` | `80.94.92.182` | 2026-06-10T15:59:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-10T16:04:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-10T16:04:01 |
| `root` | `ubuntu` | `115.190.117.228` | 2026-06-10T16:23:42 |
| `Alphanetworks` | `wrgg19_c_dlwbr_dir300` | `45.198.224.21` | 2026-06-10T16:25:28 |
| `user` | `1` | `45.198.224.21` | 2026-06-10T16:33:44 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-10T16:36:49 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-10T16:36:49 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-10T16:36:53 |
| `user` | `hondacivic` | `2.57.121.25` | 2026-06-10T16:43:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **290** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 41 |
| Paramiko (Python) | 9 |
| OpenSSH | 5 |
| PuTTY | 5 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 33 | 3 |
| `a2de0f306611...` | Mirai/variant | 9 | 3 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `57446c12547a...` | Mirai/variant | 4 | 3 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 33 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `57446c12547a...` | PuTTY | 4 | 3 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1082, T1105, T1059.004` |

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
Source IPs: `45.198.224.21`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **19** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS47890` | UNMANAGED LTD | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS208137` | Feo Prest SRL | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS17621` | China Unicom Shanghai network | 1 | LOW |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d162bf248a15

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:55 |
| **Last Seen** | 2026-06-10 14:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:55:53` | `cowrie.session.connect` |
| `2026-06-10 14:55:53` | `cowrie.client.version` |
| `2026-06-10 14:55:53` | `cowrie.client.kex` |
| `2026-06-10 14:55:55` | `cowrie.login.success` |
| `2026-06-10 14:55:56` | `cowrie.session.params` |
| `2026-06-10 14:55:56` | `cowrie.command.input` |
| `2026-06-10 14:55:57` | `cowrie.log.closed` |
| `2026-06-10 14:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4e6008c6fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:59 |
| **Last Seen** | 2026-06-10 15:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:59:56` | `cowrie.session.connect` |
| `2026-06-10 14:59:56` | `cowrie.client.version` |
| `2026-06-10 14:59:56` | `cowrie.client.kex` |
| `2026-06-10 14:59:58` | `cowrie.login.success` |
| `2026-06-10 14:59:59` | `cowrie.session.params` |
| `2026-06-10 14:59:59` | `cowrie.command.input` |
| `2026-06-10 15:00:00` | `cowrie.log.closed` |
| `2026-06-10 15:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa417d92b7f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:03 |
| **Last Seen** | 2026-06-10 15:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:03:39` | `cowrie.session.connect` |
| `2026-06-10 15:03:39` | `cowrie.client.version` |
| `2026-06-10 15:03:39` | `cowrie.client.kex` |
| `2026-06-10 15:03:41` | `cowrie.login.success` |
| `2026-06-10 15:03:43` | `cowrie.session.params` |
| `2026-06-10 15:03:43` | `cowrie.command.input` |
| `2026-06-10 15:03:44` | `cowrie.log.closed` |
| `2026-06-10 15:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bb251cd027

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:04 |
| **Last Seen** | 2026-06-10 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:04:31` | `cowrie.session.connect` |
| `2026-06-10 15:04:31` | `cowrie.client.version` |
| `2026-06-10 15:04:31` | `cowrie.client.kex` |
| `2026-06-10 15:04:31` | `cowrie.login.success` |
| `2026-06-10 15:04:32` | `cowrie.session.params` |
| `2026-06-10 15:04:32` | `cowrie.command.input` |
| `2026-06-10 15:04:32` | `cowrie.log.closed` |
| `2026-06-10 15:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388f96c45f97

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:06 |
| **Last Seen** | 2026-06-10 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:06:57` | `cowrie.session.connect` |
| `2026-06-10 15:06:57` | `cowrie.client.version` |
| `2026-06-10 15:06:57` | `cowrie.client.kex` |
| `2026-06-10 15:06:57` | `cowrie.login.success` |
| `2026-06-10 15:06:58` | `cowrie.session.params` |
| `2026-06-10 15:06:58` | `cowrie.command.input` |
| `2026-06-10 15:06:58` | `cowrie.log.closed` |
| `2026-06-10 15:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e692c49d670d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:07 |
| **Last Seen** | 2026-06-10 15:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:07:30` | `cowrie.session.connect` |
| `2026-06-10 15:07:30` | `cowrie.client.version` |
| `2026-06-10 15:07:30` | `cowrie.client.kex` |
| `2026-06-10 15:07:34` | `cowrie.login.success` |
| `2026-06-10 15:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c9c245c29a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:09 |
| **Last Seen** | 2026-06-10 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:09:16` | `cowrie.session.connect` |
| `2026-06-10 15:09:16` | `cowrie.client.version` |
| `2026-06-10 15:09:16` | `cowrie.client.kex` |
| `2026-06-10 15:09:17` | `cowrie.login.success` |
| `2026-06-10 15:09:17` | `cowrie.session.params` |
| `2026-06-10 15:09:17` | `cowrie.command.input` |
| `2026-06-10 15:09:18` | `cowrie.log.closed` |
| `2026-06-10 15:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb081160c1e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:11 |
| **Last Seen** | 2026-06-10 15:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:11:13` | `cowrie.session.connect` |
| `2026-06-10 15:11:13` | `cowrie.client.version` |
| `2026-06-10 15:11:13` | `cowrie.client.kex` |
| `2026-06-10 15:11:14` | `cowrie.login.success` |
| `2026-06-10 15:11:15` | `cowrie.session.params` |
| `2026-06-10 15:11:15` | `cowrie.command.input` |
| `2026-06-10 15:11:15` | `cowrie.log.closed` |
| `2026-06-10 15:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ec0cb5cc4c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:11 |
| **Last Seen** | 2026-06-10 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:11:32` | `cowrie.session.connect` |
| `2026-06-10 15:11:32` | `cowrie.client.version` |
| `2026-06-10 15:11:32` | `cowrie.client.kex` |
| `2026-06-10 15:11:33` | `cowrie.login.success` |
| `2026-06-10 15:11:33` | `cowrie.session.params` |
| `2026-06-10 15:11:33` | `cowrie.command.input` |
| `2026-06-10 15:11:34` | `cowrie.log.closed` |
| `2026-06-10 15:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df61e1e6bd61

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 15:13 |
| **Last Seen** | 2026-06-10 15:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:13:26` | `cowrie.session.connect` |
| `2026-06-10 15:13:26` | `cowrie.client.version` |
| `2026-06-10 15:13:27` | `cowrie.client.kex` |
| `2026-06-10 15:13:28` | `cowrie.login.success` |
| `2026-06-10 15:13:29` | `cowrie.session.params` |
| `2026-06-10 15:13:29` | `cowrie.command.input` |
| `2026-06-10 15:13:29` | `cowrie.log.closed` |
| `2026-06-10 15:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35fc0208a39

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 15:13 |
| **Last Seen** | 2026-06-10 15:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:13:30` | `cowrie.session.connect` |
| `2026-06-10 15:13:30` | `cowrie.client.version` |
| `2026-06-10 15:13:30` | `cowrie.client.kex` |
| `2026-06-10 15:13:32` | `cowrie.login.success` |
| `2026-06-10 15:13:33` | `cowrie.session.params` |
| `2026-06-10 15:13:33` | `cowrie.command.input` |
| `2026-06-10 15:13:34` | `cowrie.log.closed` |
| `2026-06-10 15:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9da6cb77cff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:13 |
| **Last Seen** | 2026-06-10 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:13:46` | `cowrie.session.connect` |
| `2026-06-10 15:13:46` | `cowrie.client.version` |
| `2026-06-10 15:13:47` | `cowrie.client.kex` |
| `2026-06-10 15:13:47` | `cowrie.login.success` |
| `2026-06-10 15:13:48` | `cowrie.session.params` |
| `2026-06-10 15:13:48` | `cowrie.command.input` |
| `2026-06-10 15:13:48` | `cowrie.log.closed` |
| `2026-06-10 15:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5184387ce6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-10 15:14 |
| **Last Seen** | 2026-06-10 15:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:14:03` | `cowrie.session.connect` |
| `2026-06-10 15:14:03` | `cowrie.client.version` |
| `2026-06-10 15:14:03` | `cowrie.client.kex` |
| `2026-06-10 15:14:04` | `cowrie.login.success` |
| `2026-06-10 15:14:04` | `cowrie.direct-tcpip.request` |
| `2026-06-10 15:14:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-10 15:14:04` | `cowrie.direct-tcpip.data` |
| `2026-06-10 15:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8ce73c88ea

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:15 |
| **Last Seen** | 2026-06-10 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:15:05` | `cowrie.session.connect` |
| `2026-06-10 15:15:05` | `cowrie.client.version` |
| `2026-06-10 15:15:05` | `cowrie.client.kex` |
| `2026-06-10 15:15:07` | `cowrie.login.success` |
| `2026-06-10 15:15:08` | `cowrie.session.params` |
| `2026-06-10 15:15:08` | `cowrie.command.input` |
| `2026-06-10 15:15:08` | `cowrie.log.closed` |
| `2026-06-10 15:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273204891806

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:15 |
| **Last Seen** | 2026-06-10 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:15:53` | `cowrie.session.connect` |
| `2026-06-10 15:15:53` | `cowrie.client.version` |
| `2026-06-10 15:15:53` | `cowrie.client.kex` |
| `2026-06-10 15:15:53` | `cowrie.login.success` |
| `2026-06-10 15:15:54` | `cowrie.session.params` |
| `2026-06-10 15:15:54` | `cowrie.command.input` |
| `2026-06-10 15:15:54` | `cowrie.log.closed` |
| `2026-06-10 15:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b682fe4237a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:18 |
| **Last Seen** | 2026-06-10 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:18:01` | `cowrie.session.connect` |
| `2026-06-10 15:18:01` | `cowrie.client.version` |
| `2026-06-10 15:18:01` | `cowrie.client.kex` |
| `2026-06-10 15:18:01` | `cowrie.login.success` |
| `2026-06-10 15:18:02` | `cowrie.session.params` |
| `2026-06-10 15:18:02` | `cowrie.command.input` |
| `2026-06-10 15:18:02` | `cowrie.log.closed` |
| `2026-06-10 15:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25f5dd7d8b1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:19 |
| **Last Seen** | 2026-06-10 15:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:19:01` | `cowrie.session.connect` |
| `2026-06-10 15:19:01` | `cowrie.client.version` |
| `2026-06-10 15:19:01` | `cowrie.client.kex` |
| `2026-06-10 15:19:02` | `cowrie.login.success` |
| `2026-06-10 15:19:03` | `cowrie.session.params` |
| `2026-06-10 15:19:03` | `cowrie.command.input` |
| `2026-06-10 15:19:04` | `cowrie.log.closed` |
| `2026-06-10 15:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e6bd1695f7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:20 |
| **Last Seen** | 2026-06-10 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:20:14` | `cowrie.session.connect` |
| `2026-06-10 15:20:14` | `cowrie.client.version` |
| `2026-06-10 15:20:14` | `cowrie.client.kex` |
| `2026-06-10 15:20:14` | `cowrie.login.success` |
| `2026-06-10 15:20:15` | `cowrie.session.params` |
| `2026-06-10 15:20:15` | `cowrie.command.input` |
| `2026-06-10 15:20:15` | `cowrie.log.closed` |
| `2026-06-10 15:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ac83fde7ea

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:22 |
| **Last Seen** | 2026-06-10 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:22:26` | `cowrie.session.connect` |
| `2026-06-10 15:22:26` | `cowrie.client.version` |
| `2026-06-10 15:22:26` | `cowrie.client.kex` |
| `2026-06-10 15:22:26` | `cowrie.login.success` |
| `2026-06-10 15:22:27` | `cowrie.session.params` |
| `2026-06-10 15:22:27` | `cowrie.command.input` |
| `2026-06-10 15:22:27` | `cowrie.log.closed` |
| `2026-06-10 15:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b3462fc0a5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:22 |
| **Last Seen** | 2026-06-10 15:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:22:50` | `cowrie.session.connect` |
| `2026-06-10 15:22:50` | `cowrie.client.version` |
| `2026-06-10 15:22:50` | `cowrie.client.kex` |
| `2026-06-10 15:22:52` | `cowrie.login.success` |
| `2026-06-10 15:22:53` | `cowrie.session.params` |
| `2026-06-10 15:22:53` | `cowrie.command.input` |
| `2026-06-10 15:22:54` | `cowrie.log.closed` |
| `2026-06-10 15:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68117fc4178

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:24 |
| **Last Seen** | 2026-06-10 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:24:41` | `cowrie.session.connect` |
| `2026-06-10 15:24:41` | `cowrie.client.version` |
| `2026-06-10 15:24:41` | `cowrie.client.kex` |
| `2026-06-10 15:24:41` | `cowrie.login.success` |
| `2026-06-10 15:24:42` | `cowrie.session.params` |
| `2026-06-10 15:24:42` | `cowrie.command.input` |
| `2026-06-10 15:24:42` | `cowrie.log.closed` |
| `2026-06-10 15:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e416fdab6116

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:26 |
| **Last Seen** | 2026-06-10 15:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:26:38` | `cowrie.session.connect` |
| `2026-06-10 15:26:38` | `cowrie.client.version` |
| `2026-06-10 15:26:38` | `cowrie.client.kex` |
| `2026-06-10 15:26:40` | `cowrie.login.success` |
| `2026-06-10 15:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114237767e44

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:26 |
| **Last Seen** | 2026-06-10 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:26:59` | `cowrie.session.connect` |
| `2026-06-10 15:26:59` | `cowrie.client.version` |
| `2026-06-10 15:26:59` | `cowrie.client.kex` |
| `2026-06-10 15:27:00` | `cowrie.login.success` |
| `2026-06-10 15:27:01` | `cowrie.session.params` |
| `2026-06-10 15:27:01` | `cowrie.command.input` |
| `2026-06-10 15:27:01` | `cowrie.log.closed` |
| `2026-06-10 15:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06515454479d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:29 |
| **Last Seen** | 2026-06-10 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:29:07` | `cowrie.session.connect` |
| `2026-06-10 15:29:07` | `cowrie.client.version` |
| `2026-06-10 15:29:07` | `cowrie.client.kex` |
| `2026-06-10 15:29:07` | `cowrie.login.success` |
| `2026-06-10 15:29:08` | `cowrie.session.params` |
| `2026-06-10 15:29:08` | `cowrie.command.input` |
| `2026-06-10 15:29:08` | `cowrie.log.closed` |
| `2026-06-10 15:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a8b12f787e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 15:30 |
| **Last Seen** | 2026-06-10 15:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:30:15` | `cowrie.session.connect` |
| `2026-06-10 15:30:15` | `cowrie.client.version` |
| `2026-06-10 15:30:16` | `cowrie.client.kex` |
| `2026-06-10 15:30:16` | `cowrie.login.success` |
| `2026-06-10 15:30:16` | `cowrie.direct-tcpip.request` |
| `2026-06-10 15:30:16` | `cowrie.direct-tcpip.data` |
| `2026-06-10 15:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0851e26a83

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:30 |
| **Last Seen** | 2026-06-10 15:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:30:25` | `cowrie.session.connect` |
| `2026-06-10 15:30:25` | `cowrie.client.version` |
| `2026-06-10 15:30:26` | `cowrie.client.kex` |
| `2026-06-10 15:30:29` | `cowrie.login.success` |
| `2026-06-10 15:30:31` | `cowrie.session.params` |
| `2026-06-10 15:30:31` | `cowrie.command.input` |
| `2026-06-10 15:30:31` | `cowrie.log.closed` |
| `2026-06-10 15:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d54a725d058

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-10 15:31 |
| **Last Seen** | 2026-06-10 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:31:19` | `cowrie.session.connect` |
| `2026-06-10 15:31:19` | `cowrie.client.version` |
| `2026-06-10 15:31:19` | `cowrie.client.kex` |
| `2026-06-10 15:31:19` | `cowrie.login.success` |
| `2026-06-10 15:31:20` | `cowrie.session.params` |
| `2026-06-10 15:31:20` | `cowrie.command.input` |
| `2026-06-10 15:31:20` | `cowrie.log.closed` |
| `2026-06-10 15:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31851854bd94

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:34 |
| **Last Seen** | 2026-06-10 15:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:34:13` | `cowrie.session.connect` |
| `2026-06-10 15:34:14` | `cowrie.client.version` |
| `2026-06-10 15:34:14` | `cowrie.client.kex` |
| `2026-06-10 15:34:16` | `cowrie.login.success` |
| `2026-06-10 15:34:17` | `cowrie.session.params` |
| `2026-06-10 15:34:17` | `cowrie.command.input` |
| `2026-06-10 15:34:19` | `cowrie.log.closed` |
| `2026-06-10 15:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7c752e36b0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:37 |
| **Last Seen** | 2026-06-10 15:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:37:53` | `cowrie.session.connect` |
| `2026-06-10 15:37:53` | `cowrie.client.version` |
| `2026-06-10 15:37:53` | `cowrie.client.kex` |
| `2026-06-10 15:37:55` | `cowrie.login.success` |
| `2026-06-10 15:37:57` | `cowrie.session.params` |
| `2026-06-10 15:37:57` | `cowrie.command.input` |
| `2026-06-10 15:37:57` | `cowrie.log.closed` |
| `2026-06-10 15:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5929ba2c1f2a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 15:39 |
| **Last Seen** | 2026-06-10 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:39:43` | `cowrie.session.connect` |
| `2026-06-10 15:39:43` | `cowrie.client.version` |
| `2026-06-10 15:39:43` | `cowrie.client.kex` |
| `2026-06-10 15:39:45` | `cowrie.login.success` |
| `2026-06-10 15:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952f23b1d1ac

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 15:39 |
| **Last Seen** | 2026-06-10 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:39:43` | `cowrie.session.connect` |
| `2026-06-10 15:39:43` | `cowrie.client.version` |
| `2026-06-10 15:39:44` | `cowrie.client.kex` |
| `2026-06-10 15:39:45` | `cowrie.login.success` |
| `2026-06-10 15:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933bd1f19197

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 15:40 |
| **Last Seen** | 2026-06-10 15:42 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:40:08` | `cowrie.session.connect` |
| `2026-06-10 15:40:08` | `cowrie.client.version` |
| `2026-06-10 15:40:09` | `cowrie.client.kex` |
| `2026-06-10 15:40:10` | `cowrie.login.success` |
| `2026-06-10 15:40:12` | `cowrie.session.file_upload` |
| `2026-06-10 15:40:13` | `cowrie.session.params` |
| `2026-06-10 15:40:13` | `cowrie.command.input` |
| `2026-06-10 15:40:13` | `cowrie.command.input` |
| `2026-06-10 15:40:13` | `cowrie.command.input` |
| `2026-06-10 15:40:13` | `cowrie.command.failed` |
| `2026-06-10 15:40:13` | `cowrie.log.closed` |
| `2026-06-10 15:40:14` | `cowrie.session.params` |
| `2026-06-10 15:40:14` | `cowrie.command.input` |
| `2026-06-10 15:40:15` | `cowrie.log.closed` |
| `2026-06-10 15:40:16` | `cowrie.session.params` |
| `2026-06-10 15:40:16` | `cowrie.command.input` |
| `2026-06-10 15:40:16` | `cowrie.log.closed` |
| `2026-06-10 15:40:17` | `cowrie.session.params` |
| `2026-06-10 15:40:17` | `cowrie.command.input` |
| `2026-06-10 15:40:17` | `cowrie.command.failed` |
| `2026-06-10 15:40:17` | `cowrie.command.failed` |
| `2026-06-10 15:41:18` | `cowrie.session.params` |
| `2026-06-10 15:41:18` | `cowrie.command.input` |
| `2026-06-10 15:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901dcaa5786f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:41 |
| **Last Seen** | 2026-06-10 15:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:41:42` | `cowrie.session.connect` |
| `2026-06-10 15:41:43` | `cowrie.client.version` |
| `2026-06-10 15:41:43` | `cowrie.client.kex` |
| `2026-06-10 15:41:46` | `cowrie.login.success` |
| `2026-06-10 15:41:48` | `cowrie.session.params` |
| `2026-06-10 15:41:48` | `cowrie.command.input` |
| `2026-06-10 15:41:48` | `cowrie.log.closed` |
| `2026-06-10 15:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1409a598b6bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 15:43 |
| **Last Seen** | 2026-06-10 15:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:43:47` | `cowrie.session.connect` |
| `2026-06-10 15:43:47` | `cowrie.client.version` |
| `2026-06-10 15:43:47` | `cowrie.client.kex` |
| `2026-06-10 15:43:48` | `cowrie.login.success` |
| `2026-06-10 15:43:48` | `cowrie.direct-tcpip.request` |
| `2026-06-10 15:43:48` | `cowrie.direct-tcpip.data` |
| `2026-06-10 15:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76471fe2edb4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:45 |
| **Last Seen** | 2026-06-10 15:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:45:27` | `cowrie.session.connect` |
| `2026-06-10 15:45:27` | `cowrie.client.version` |
| `2026-06-10 15:45:28` | `cowrie.client.kex` |
| `2026-06-10 15:45:30` | `cowrie.login.success` |
| `2026-06-10 15:45:32` | `cowrie.session.params` |
| `2026-06-10 15:45:32` | `cowrie.command.input` |
| `2026-06-10 15:45:32` | `cowrie.log.closed` |
| `2026-06-10 15:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c457db8a6c0e

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 15:45 |
| **Last Seen** | 2026-06-10 15:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:45:28` | `cowrie.session.connect` |
| `2026-06-10 15:45:28` | `cowrie.client.version` |
| `2026-06-10 15:45:28` | `cowrie.client.kex` |
| `2026-06-10 15:45:28` | `cowrie.login.success` |
| `2026-06-10 15:45:28` | `cowrie.direct-tcpip.request` |
| `2026-06-10 15:45:28` | `cowrie.direct-tcpip.data` |
| `2026-06-10 15:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b523a50baa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:49 |
| **Last Seen** | 2026-06-10 15:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:49:22` | `cowrie.session.connect` |
| `2026-06-10 15:49:22` | `cowrie.client.version` |
| `2026-06-10 15:49:23` | `cowrie.client.kex` |
| `2026-06-10 15:49:24` | `cowrie.login.success` |
| `2026-06-10 15:49:28` | `cowrie.session.params` |
| `2026-06-10 15:49:28` | `cowrie.command.input` |
| `2026-06-10 15:49:28` | `cowrie.log.closed` |
| `2026-06-10 15:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6acb06d10ec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:53 |
| **Last Seen** | 2026-06-10 15:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:53:01` | `cowrie.session.connect` |
| `2026-06-10 15:53:01` | `cowrie.client.version` |
| `2026-06-10 15:53:03` | `cowrie.client.kex` |
| `2026-06-10 15:53:06` | `cowrie.login.success` |
| `2026-06-10 15:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12068627fd27

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:56 |
| **Last Seen** | 2026-06-10 15:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:56:17` | `cowrie.session.connect` |
| `2026-06-10 15:56:18` | `cowrie.client.version` |
| `2026-06-10 15:56:18` | `cowrie.client.kex` |
| `2026-06-10 15:56:19` | `cowrie.login.success` |
| `2026-06-10 15:56:20` | `cowrie.session.params` |
| `2026-06-10 15:56:20` | `cowrie.command.input` |
| `2026-06-10 15:56:21` | `cowrie.log.closed` |
| `2026-06-10 15:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3c7cc48418

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 15:59 |
| **Last Seen** | 2026-06-10 15:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 15:59:36` | `cowrie.session.connect` |
| `2026-06-10 15:59:37` | `cowrie.client.version` |
| `2026-06-10 15:59:37` | `cowrie.client.kex` |
| `2026-06-10 15:59:38` | `cowrie.login.success` |
| `2026-06-10 15:59:39` | `cowrie.session.params` |
| `2026-06-10 15:59:39` | `cowrie.command.input` |
| `2026-06-10 15:59:40` | `cowrie.log.closed` |
| `2026-06-10 15:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bf265ccb20

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 16:03 |
| **Last Seen** | 2026-06-10 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:03:59` | `cowrie.session.connect` |
| `2026-06-10 16:03:59` | `cowrie.client.version` |
| `2026-06-10 16:04:00` | `cowrie.client.kex` |
| `2026-06-10 16:04:00` | `cowrie.login.success` |
| `2026-06-10 16:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be6f6880f7f7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 16:04 |
| **Last Seen** | 2026-06-10 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:04:00` | `cowrie.session.connect` |
| `2026-06-10 16:04:00` | `cowrie.client.version` |
| `2026-06-10 16:04:00` | `cowrie.client.kex` |
| `2026-06-10 16:04:01` | `cowrie.login.success` |
| `2026-06-10 16:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7fc1ec28b4

| Field | Detail |
|---|---|
| **Source IP** | `115.190.117[.]228` |
| **First Seen** | 2026-06-10 16:23 |
| **Last Seen** | 2026-06-10 16:28 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:23:40` | `cowrie.session.connect` |
| `2026-06-10 16:23:40` | `cowrie.client.version` |
| `2026-06-10 16:23:40` | `cowrie.client.kex` |
| `2026-06-10 16:23:42` | `cowrie.login.success` |
| `2026-06-10 16:28:42` | `cowrie.session.file_upload` |
| `2026-06-10 16:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.117[.]228` to AbuseIPDB if not already reported
- [ ] Block `115.190.117[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4bf48dbf58

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]21` |
| **First Seen** | 2026-06-10 16:25 |
| **Last Seen** | 2026-06-10 16:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:25:28` | `cowrie.session.connect` |
| `2026-06-10 16:25:28` | `cowrie.login.success` |
| `2026-06-10 16:25:29` | `cowrie.session.params` |
| `2026-06-10 16:25:29` | `cowrie.command.input` |
| `2026-06-10 16:25:30` | `cowrie.command.input` |
| `2026-06-10 16:25:30` | `cowrie.command.input` |
| `2026-06-10 16:25:31` | `cowrie.command.input` |
| `2026-06-10 16:25:31` | `cowrie.command.failed` |
| `2026-06-10 16:25:31` | `cowrie.log.closed` |
| `2026-06-10 16:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]21` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69cab1f1e534

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]21` |
| **First Seen** | 2026-06-10 16:33 |
| **Last Seen** | 2026-06-10 16:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:33:43` | `cowrie.session.connect` |
| `2026-06-10 16:33:44` | `cowrie.login.success` |
| `2026-06-10 16:33:44` | `cowrie.session.params` |
| `2026-06-10 16:33:45` | `cowrie.command.input` |
| `2026-06-10 16:33:45` | `cowrie.command.input` |
| `2026-06-10 16:33:46` | `cowrie.command.input` |
| `2026-06-10 16:33:46` | `cowrie.command.input` |
| `2026-06-10 16:33:46` | `cowrie.command.failed` |
| `2026-06-10 16:33:47` | `cowrie.log.closed` |
| `2026-06-10 16:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]21` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa589caa352

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 16:36 |
| **Last Seen** | 2026-06-10 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:36:48` | `cowrie.session.connect` |
| `2026-06-10 16:36:48` | `cowrie.client.version` |
| `2026-06-10 16:36:48` | `cowrie.client.kex` |
| `2026-06-10 16:36:49` | `cowrie.login.success` |
| `2026-06-10 16:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68abe1ae01b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 16:36 |
| **Last Seen** | 2026-06-10 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:36:48` | `cowrie.session.connect` |
| `2026-06-10 16:36:48` | `cowrie.client.version` |
| `2026-06-10 16:36:48` | `cowrie.client.kex` |
| `2026-06-10 16:36:49` | `cowrie.login.success` |
| `2026-06-10 16:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2199aba6fa04

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 16:36 |
| **Last Seen** | 2026-06-10 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:36:53` | `cowrie.session.connect` |
| `2026-06-10 16:36:53` | `cowrie.client.version` |
| `2026-06-10 16:36:53` | `cowrie.client.kex` |
| `2026-06-10 16:36:53` | `cowrie.login.success` |
| `2026-06-10 16:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7142644762ba

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 16:36 |
| **Last Seen** | 2026-06-10 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:36:54` | `cowrie.session.connect` |
| `2026-06-10 16:36:54` | `cowrie.client.version` |
| `2026-06-10 16:36:54` | `cowrie.client.kex` |
| `2026-06-10 16:36:54` | `cowrie.login.success` |
| `2026-06-10 16:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0953508596

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 16:43 |
| **Last Seen** | 2026-06-10 16:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:43:38` | `cowrie.session.connect` |
| `2026-06-10 16:43:38` | `cowrie.client.version` |
| `2026-06-10 16:43:38` | `cowrie.client.kex` |
| `2026-06-10 16:43:39` | `cowrie.login.success` |
| `2026-06-10 16:43:39` | `cowrie.direct-tcpip.request` |
| `2026-06-10 16:43:39` | `cowrie.direct-tcpip.data` |
| `2026-06-10 16:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.150[.]219` | **203** | 2026-06-10 14:55 | 2026-06-10 16:55 | 207m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **6** | 2026-06-10 15:19 | 2026-06-10 16:26 | 3m | 0 | `T1592` | 🟢 LOW |
| `180.76.103[.]111` | **2** | 2026-06-10 16:05 | 2026-06-10 16:07 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]21` | **2** | 2026-06-10 16:25 | 2026-06-10 16:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `138.204.117[.]174` | 1 | 2026-06-10 15:34 | 2026-06-10 15:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-06-10 15:02 | 2026-06-10 15:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-06-10 15:26 | 2026-06-10 15:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]91` | 1 | 2026-06-10 16:00 | 2026-06-10 16:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-10 16:07 | 2026-06-10 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]138` | 1 | 2026-06-10 15:12 | 2026-06-10 15:12 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-06-10 16:33 | 2026-06-10 16:33 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `45.198.224[.]21` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `176.65.139[.]130` | NL | Storm Industries | **100** ⚠️ | 50 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `115.190.117[.]228` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 3 |
| `139.59.227[.]143` | SG | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `213.177.179[.]91` | NL | wcd | **100** ⚠️ | 50 |
| `66.240.236[.]116` | US | CariNet, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 290 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 213 session(s)).

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
_Report time: 2026-06-10T18:33:41Z_

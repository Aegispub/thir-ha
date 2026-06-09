# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T18:11:01Z |
| **Shift Time** | 18:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **89** |
| Confirmed Threats | **63** |
| False Positives Filtered | **26** (29.2%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **11** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **8** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `solana` | 7 |
| `admin` | 7 |
| `sol` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 7 |
| `LeitboGi0ro` | 4 |
| `123@@@` | 3 |
| `solana` | 2 |
| `!@#$%^` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 3 |
| `solana` | `solana` | 2 |
| `root` | `smo@@kkklss` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `solana` | `solana` | `80.94.92.182` | 2026-06-09T14:55:08 |
| `solana` | `1234567890-=` | `80.94.92.182` | 2026-06-09T14:59:30 |
| `solana` | `qwer1234` | `80.94.92.182` | 2026-06-09T15:03:41 |
| `jalin` | `jalin` | `213.209.159.56` | 2026-06-09T15:06:23 |
| `root` | `` | `176.65.139.41` | 2026-06-09T15:06:29 |
| `sol` | `ZXCVASDFQWER!@#$` | `80.94.92.182` | 2026-06-09T15:07:33 |
| `sol` | `zxcvasdfqwer@1234` | `80.94.92.182` | 2026-06-09T15:11:10 |
| `root` | `!@#$%^` | `80.94.92.182` | 2026-06-09T15:14:36 |
| `solana` | `!@#$%^` | `80.94.92.182` | 2026-06-09T15:18:19 |
| `solana` | `pa2ssw0rd` | `80.94.92.182` | 2026-06-09T15:22:01 |
| `solana` | `p@ssw0rd` | `80.94.92.182` | 2026-06-09T15:25:42 |
| `user` | `nikit` | `2.57.121.25` | 2026-06-09T15:37:29 |
| `thunder` | `thunder` | `176.65.139.130` | 2026-06-09T15:51:55 |
| `user` | `user` | `176.65.139.130` | 2026-06-09T15:58:21 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-09T16:00:42 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-09T16:06:55 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-09T16:06:58 |
| `solana` | `solana` | `80.94.92.168` | 2026-06-09T16:07:31 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-09T16:15:11 |
| `jaret` | `jaret` | `213.209.159.56` | 2026-06-09T16:21:39 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-09T16:25:55 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-09T16:25:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-09T16:26:03 |
| `admin` | `admin` | `107.189.24.77` | 2026-06-09T16:37:42 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-09T16:37:43 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-09T16:53:38 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-09T16:53:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **89** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 27 |
| Paramiko (Python) | 9 |
| Nmap scanner | 7 |
| PuTTY | 5 |
| libssh | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 10 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `57446c12547a...` | Mirai/variant | 4 | 3 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 10 | 2 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 10 | 5 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `57446c12547a...` | PuTTY | 4 | 3 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `4c20a8895324...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
Source IPs: `176.65.139.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **18** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |
| `AS47890` | UNMANAGED LTD | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS214472` | Offshore LC | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-85500a223361

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 14:55 |
| **Last Seen** | 2026-06-09 14:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:55:06` | `cowrie.session.connect` |
| `2026-06-09 14:55:06` | `cowrie.client.version` |
| `2026-06-09 14:55:06` | `cowrie.client.kex` |
| `2026-06-09 14:55:08` | `cowrie.login.success` |
| `2026-06-09 14:55:09` | `cowrie.session.params` |
| `2026-06-09 14:55:09` | `cowrie.command.input` |
| `2026-06-09 14:55:09` | `cowrie.log.closed` |
| `2026-06-09 14:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2604e1d545e5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 14:59 |
| **Last Seen** | 2026-06-09 14:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:59:28` | `cowrie.session.connect` |
| `2026-06-09 14:59:28` | `cowrie.client.version` |
| `2026-06-09 14:59:28` | `cowrie.client.kex` |
| `2026-06-09 14:59:30` | `cowrie.login.success` |
| `2026-06-09 14:59:32` | `cowrie.session.params` |
| `2026-06-09 14:59:32` | `cowrie.command.input` |
| `2026-06-09 14:59:32` | `cowrie.log.closed` |
| `2026-06-09 14:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbbbb44e5cf6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:03 |
| **Last Seen** | 2026-06-09 15:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:03:37` | `cowrie.session.connect` |
| `2026-06-09 15:03:39` | `cowrie.client.version` |
| `2026-06-09 15:03:39` | `cowrie.client.kex` |
| `2026-06-09 15:03:41` | `cowrie.login.success` |
| `2026-06-09 15:03:42` | `cowrie.session.params` |
| `2026-06-09 15:03:42` | `cowrie.command.input` |
| `2026-06-09 15:03:43` | `cowrie.log.closed` |
| `2026-06-09 15:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f33f4e6a0d

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-09 15:06 |
| **Last Seen** | 2026-06-09 15:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:06:23` | `cowrie.session.connect` |
| `2026-06-09 15:06:23` | `cowrie.client.version` |
| `2026-06-09 15:06:23` | `cowrie.client.kex` |
| `2026-06-09 15:06:23` | `cowrie.login.success` |
| `2026-06-09 15:06:23` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:06:23` | `cowrie.direct-tcpip.data` |
| `2026-06-09 15:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975edf06c857

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]41` |
| **First Seen** | 2026-06-09 15:06 |
| **Last Seen** | 2026-06-09 15:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:06:29` | `cowrie.session.connect` |
| `2026-06-09 15:06:29` | `cowrie.login.success` |
| `2026-06-09 15:06:30` | `cowrie.session.params` |
| `2026-06-09 15:06:30` | `cowrie.command.input` |
| `2026-06-09 15:06:31` | `cowrie.command.input` |
| `2026-06-09 15:06:32` | `cowrie.command.input` |
| `2026-06-09 15:06:32` | `cowrie.command.input` |
| `2026-06-09 15:06:32` | `cowrie.command.failed` |
| `2026-06-09 15:06:33` | `cowrie.log.closed` |
| `2026-06-09 15:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]41` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b844bb905060

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:07 |
| **Last Seen** | 2026-06-09 15:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:07:29` | `cowrie.session.connect` |
| `2026-06-09 15:07:29` | `cowrie.client.version` |
| `2026-06-09 15:07:30` | `cowrie.client.kex` |
| `2026-06-09 15:07:33` | `cowrie.login.success` |
| `2026-06-09 15:07:34` | `cowrie.session.params` |
| `2026-06-09 15:07:34` | `cowrie.command.input` |
| `2026-06-09 15:07:34` | `cowrie.log.closed` |
| `2026-06-09 15:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2db85cc954a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:11 |
| **Last Seen** | 2026-06-09 15:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:11:07` | `cowrie.session.connect` |
| `2026-06-09 15:11:07` | `cowrie.client.version` |
| `2026-06-09 15:11:07` | `cowrie.client.kex` |
| `2026-06-09 15:11:10` | `cowrie.login.success` |
| `2026-06-09 15:11:11` | `cowrie.session.params` |
| `2026-06-09 15:11:11` | `cowrie.command.input` |
| `2026-06-09 15:11:12` | `cowrie.log.closed` |
| `2026-06-09 15:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e98d20d05682

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:14 |
| **Last Seen** | 2026-06-09 15:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:14:35` | `cowrie.session.connect` |
| `2026-06-09 15:14:35` | `cowrie.client.version` |
| `2026-06-09 15:14:35` | `cowrie.client.kex` |
| `2026-06-09 15:14:36` | `cowrie.login.success` |
| `2026-06-09 15:14:38` | `cowrie.session.params` |
| `2026-06-09 15:14:38` | `cowrie.command.input` |
| `2026-06-09 15:14:38` | `cowrie.log.closed` |
| `2026-06-09 15:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcd1551e9f2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:18 |
| **Last Seen** | 2026-06-09 15:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:18:17` | `cowrie.session.connect` |
| `2026-06-09 15:18:17` | `cowrie.client.version` |
| `2026-06-09 15:18:18` | `cowrie.client.kex` |
| `2026-06-09 15:18:19` | `cowrie.login.success` |
| `2026-06-09 15:18:21` | `cowrie.session.params` |
| `2026-06-09 15:18:21` | `cowrie.command.input` |
| `2026-06-09 15:18:22` | `cowrie.log.closed` |
| `2026-06-09 15:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3d2f4c78c8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:21 |
| **Last Seen** | 2026-06-09 15:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:21:59` | `cowrie.session.connect` |
| `2026-06-09 15:21:59` | `cowrie.client.version` |
| `2026-06-09 15:22:00` | `cowrie.client.kex` |
| `2026-06-09 15:22:01` | `cowrie.login.success` |
| `2026-06-09 15:22:02` | `cowrie.session.params` |
| `2026-06-09 15:22:02` | `cowrie.command.input` |
| `2026-06-09 15:22:02` | `cowrie.log.closed` |
| `2026-06-09 15:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e47891b276b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-09 15:25 |
| **Last Seen** | 2026-06-09 15:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:25:41` | `cowrie.session.connect` |
| `2026-06-09 15:25:41` | `cowrie.client.version` |
| `2026-06-09 15:25:41` | `cowrie.client.kex` |
| `2026-06-09 15:25:42` | `cowrie.login.success` |
| `2026-06-09 15:25:43` | `cowrie.session.params` |
| `2026-06-09 15:25:43` | `cowrie.command.input` |
| `2026-06-09 15:25:44` | `cowrie.log.closed` |
| `2026-06-09 15:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df237f633de

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-09 15:37 |
| **Last Seen** | 2026-06-09 15:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:37:28` | `cowrie.session.connect` |
| `2026-06-09 15:37:28` | `cowrie.client.version` |
| `2026-06-09 15:37:28` | `cowrie.client.kex` |
| `2026-06-09 15:37:29` | `cowrie.login.success` |
| `2026-06-09 15:37:29` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:37:29` | `cowrie.direct-tcpip.data` |
| `2026-06-09 15:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d7c811f202

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-09 15:51 |
| **Last Seen** | 2026-06-09 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:51:55` | `cowrie.session.connect` |
| `2026-06-09 15:51:55` | `cowrie.client.version` |
| `2026-06-09 15:51:55` | `cowrie.client.kex` |
| `2026-06-09 15:51:55` | `cowrie.login.success` |
| `2026-06-09 15:51:55` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:51:55` | `cowrie.direct-tcpip.ja4` |
| `2026-06-09 15:51:55` | `cowrie.direct-tcpip.data` |
| `2026-06-09 15:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2857436ced3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-09 15:53 |
| **Last Seen** | 2026-06-09 15:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:53:18` | `cowrie.session.connect` |
| `2026-06-09 15:53:18` | `cowrie.client.version` |
| `2026-06-09 15:53:18` | `cowrie.client.kex` |
| `2026-06-09 15:53:18` | `cowrie.login.success` |
| `2026-06-09 15:53:18` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:53:18` | `cowrie.direct-tcpip.data` |
| `2026-06-09 15:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0bf8fb9d893

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-09 15:58 |
| **Last Seen** | 2026-06-09 15:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:58:21` | `cowrie.session.connect` |
| `2026-06-09 15:58:21` | `cowrie.client.version` |
| `2026-06-09 15:58:21` | `cowrie.client.kex` |
| `2026-06-09 15:58:21` | `cowrie.login.success` |
| `2026-06-09 15:58:21` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:58:21` | `cowrie.direct-tcpip.ja4` |
| `2026-06-09 15:58:21` | `cowrie.direct-tcpip.data` |
| `2026-06-09 15:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d97e912cc9

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-09 16:06 |
| **Last Seen** | 2026-06-09 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:06:54` | `cowrie.session.connect` |
| `2026-06-09 16:06:54` | `cowrie.client.version` |
| `2026-06-09 16:06:54` | `cowrie.client.kex` |
| `2026-06-09 16:06:55` | `cowrie.login.success` |
| `2026-06-09 16:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee9a149a030

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-09 16:06 |
| **Last Seen** | 2026-06-09 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:06:56` | `cowrie.session.connect` |
| `2026-06-09 16:06:56` | `cowrie.client.version` |
| `2026-06-09 16:06:57` | `cowrie.client.kex` |
| `2026-06-09 16:06:58` | `cowrie.login.success` |
| `2026-06-09 16:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8704de6132dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]168` |
| **First Seen** | 2026-06-09 16:07 |
| **Last Seen** | 2026-06-09 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:07:29` | `cowrie.session.connect` |
| `2026-06-09 16:07:29` | `cowrie.client.version` |
| `2026-06-09 16:07:29` | `cowrie.client.kex` |
| `2026-06-09 16:07:31` | `cowrie.login.success` |
| `2026-06-09 16:07:32` | `cowrie.session.params` |
| `2026-06-09 16:07:32` | `cowrie.command.input` |
| `2026-06-09 16:07:33` | `cowrie.log.closed` |
| `2026-06-09 16:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]168` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0266b364665f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-09 16:15 |
| **Last Seen** | 2026-06-09 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:15:11` | `cowrie.session.connect` |
| `2026-06-09 16:15:11` | `cowrie.client.version` |
| `2026-06-09 16:15:11` | `cowrie.client.kex` |
| `2026-06-09 16:15:11` | `cowrie.login.success` |
| `2026-06-09 16:15:12` | `cowrie.direct-tcpip.request` |
| `2026-06-09 16:15:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-09 16:15:12` | `cowrie.direct-tcpip.data` |
| `2026-06-09 16:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25df4518d34e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-09 16:15 |
| **Last Seen** | 2026-06-09 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:15:12` | `cowrie.session.connect` |
| `2026-06-09 16:15:12` | `cowrie.client.version` |
| `2026-06-09 16:15:12` | `cowrie.client.kex` |
| `2026-06-09 16:15:12` | `cowrie.login.success` |
| `2026-06-09 16:15:12` | `cowrie.direct-tcpip.request` |
| `2026-06-09 16:15:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-09 16:15:13` | `cowrie.direct-tcpip.data` |
| `2026-06-09 16:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4446afd57b1e

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-09 16:21 |
| **Last Seen** | 2026-06-09 16:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:21:38` | `cowrie.session.connect` |
| `2026-06-09 16:21:38` | `cowrie.client.version` |
| `2026-06-09 16:21:38` | `cowrie.client.kex` |
| `2026-06-09 16:21:39` | `cowrie.login.success` |
| `2026-06-09 16:21:39` | `cowrie.direct-tcpip.request` |
| `2026-06-09 16:21:39` | `cowrie.direct-tcpip.data` |
| `2026-06-09 16:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421f16e9a41d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 16:25 |
| **Last Seen** | 2026-06-09 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:25:54` | `cowrie.session.connect` |
| `2026-06-09 16:25:54` | `cowrie.client.version` |
| `2026-06-09 16:25:54` | `cowrie.client.kex` |
| `2026-06-09 16:25:55` | `cowrie.login.success` |
| `2026-06-09 16:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5e374c6a85

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 16:25 |
| **Last Seen** | 2026-06-09 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:25:54` | `cowrie.session.connect` |
| `2026-06-09 16:25:54` | `cowrie.client.version` |
| `2026-06-09 16:25:54` | `cowrie.client.kex` |
| `2026-06-09 16:25:55` | `cowrie.login.success` |
| `2026-06-09 16:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25696823aed

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 16:26 |
| **Last Seen** | 2026-06-09 16:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:26:02` | `cowrie.session.connect` |
| `2026-06-09 16:26:02` | `cowrie.client.version` |
| `2026-06-09 16:26:02` | `cowrie.client.kex` |
| `2026-06-09 16:26:03` | `cowrie.login.success` |
| `2026-06-09 16:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8b286dc7b7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 16:26 |
| **Last Seen** | 2026-06-09 16:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:26:03` | `cowrie.session.connect` |
| `2026-06-09 16:26:03` | `cowrie.client.version` |
| `2026-06-09 16:26:03` | `cowrie.client.kex` |
| `2026-06-09 16:26:03` | `cowrie.login.success` |
| `2026-06-09 16:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34258d8b2685

| Field | Detail |
|---|---|
| **Source IP** | `107.189.24[.]77` |
| **First Seen** | 2026-06-09 16:37 |
| **Last Seen** | 2026-06-09 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:37:42` | `cowrie.session.connect` |
| `2026-06-09 16:37:42` | `cowrie.client.version` |
| `2026-06-09 16:37:42` | `cowrie.client.kex` |
| `2026-06-09 16:37:42` | `cowrie.login.success` |
| `2026-06-09 16:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.24[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.189.24[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d13ec0bd37c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-09 16:37 |
| **Last Seen** | 2026-06-09 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:37:42` | `cowrie.session.connect` |
| `2026-06-09 16:37:42` | `cowrie.client.version` |
| `2026-06-09 16:37:42` | `cowrie.client.kex` |
| `2026-06-09 16:37:43` | `cowrie.login.success` |
| `2026-06-09 16:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892573717516

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:53:37` | `cowrie.session.connect` |
| `2026-06-09 16:53:37` | `cowrie.client.version` |
| `2026-06-09 16:53:37` | `cowrie.client.kex` |
| `2026-06-09 16:53:38` | `cowrie.login.success` |
| `2026-06-09 16:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e93d285af15

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:53:37` | `cowrie.session.connect` |
| `2026-06-09 16:53:37` | `cowrie.client.version` |
| `2026-06-09 16:53:38` | `cowrie.client.kex` |
| `2026-06-09 16:53:38` | `cowrie.login.success` |
| `2026-06-09 16:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2782f6c5464

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:53:54` | `cowrie.session.connect` |
| `2026-06-09 16:53:54` | `cowrie.client.version` |
| `2026-06-09 16:53:54` | `cowrie.client.kex` |
| `2026-06-09 16:53:55` | `cowrie.login.success` |
| `2026-06-09 16:53:57` | `cowrie.session.file_upload` |
| `2026-06-09 16:53:58` | `cowrie.session.params` |
| `2026-06-09 16:53:58` | `cowrie.command.input` |
| `2026-06-09 16:53:58` | `cowrie.command.input` |
| `2026-06-09 16:53:58` | `cowrie.command.input` |
| `2026-06-09 16:53:58` | `cowrie.command.failed` |
| `2026-06-09 16:53:58` | `cowrie.log.closed` |
| `2026-06-09 16:53:59` | `cowrie.session.params` |
| `2026-06-09 16:53:59` | `cowrie.command.input` |
| `2026-06-09 16:54:00` | `cowrie.log.closed` |
| `2026-06-09 16:54:01` | `cowrie.session.params` |
| `2026-06-09 16:54:01` | `cowrie.command.input` |
| `2026-06-09 16:54:01` | `cowrie.log.closed` |
| `2026-06-09 16:54:02` | `cowrie.session.params` |
| `2026-06-09 16:54:02` | `cowrie.command.input` |
| `2026-06-09 16:54:02` | `cowrie.command.failed` |
| `2026-06-09 16:54:02` | `cowrie.command.failed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **11** | 2026-06-09 15:05 | 2026-06-09 16:29 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `79.105.232[.]90` | **3** | 2026-06-09 16:07 | 2026-06-09 16:42 | 6m | 0 | `T1592` | 🟢 LOW |
| `115.190.219[.]169` | **2** | 2026-06-09 16:26 | 2026-06-09 16:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.65.224[.]144` | **2** | 2026-06-09 16:00 | 2026-06-09 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-09 15:49 | 2026-06-09 15:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.174.155[.]67` | 1 | 2026-06-09 15:14 | 2026-06-09 15:15 | 47s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]41` | 1 | 2026-06-09 15:06 | 2026-06-09 15:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]53` | 1 | 2026-06-09 15:32 | 2026-06-09 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]14` | 1 | 2026-06-09 14:59 | 2026-06-09 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-06-09 15:30 | 2026-06-09 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-09 16:06 | 2026-06-09 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.237.200[.]170` | 1 | 2026-06-09 15:05 | 2026-06-09 15:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.79.20[.]59` | 1 | 2026-06-09 16:29 | 2026-06-09 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]113` | 1 | 2026-06-09 15:03 | 2026-06-09 15:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]5` | 1 | 2026-06-09 15:27 | 2026-06-09 15:27 | 2s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]168` | 1 | 2026-06-09 15:55 | 2026-06-09 15:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]114` | 1 | 2026-06-09 16:09 | 2026-06-09 16:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]167` | 1 | 2026-06-09 15:30 | 2026-06-09 15:30 | 9s | 0 | `T1592` | 🟢 LOW |

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
| `79.105.232[.]90` | RU | PJSC Rostelecom | **100** ⚠️ | 0 |
| `89.21.67[.]167` | NL | Infrawatch Limited | **100** ⚠️ | 17 |
| `107.174.155[.]67` | US | sally wang | **100** ⚠️ | 0 |
| `193.176.29[.]14` | GB | Infrawatch Limited | **100** ⚠️ | 14 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `81.19.216[.]114` | NL | Infrawatch Limited | **100** ⚠️ | 9 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `176.65.139[.]130` | NL | Storm Industries | **100** ⚠️ | 50 |
| `47.79.20[.]59` | HK | Alibaba Cloud LLC | **100** ⚠️ | 20 |
| `185.223.235[.]53` | NL | Infrawatch Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 4 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 89 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (29.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 18 recon entry/entries in table (5 group(s) consolidating 20 session(s)).

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
_Report time: 2026-06-09T18:11:01Z_

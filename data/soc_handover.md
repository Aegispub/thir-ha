# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T11:04:58Z |
| **Shift Time** | 11:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **213** |
| Confirmed Threats | **178** |
| False Positives Filtered | **35** (16.4%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **14** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **173** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **40** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **15** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `solv` | 4 |
| `GET / HTTP/1.0` | 4 |
| `sol` | 3 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 10 |
| `123@@@` | 5 |
| `Host: 129.80.119.236` | 4 |
| `12345678` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 10 |
| `root` | `123@@@` | 5 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | 4 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | 2 |
| `solana` | `solana` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `solana` | `solana` | `2.57.122.238` | 2026-06-08T08:05:06 |
| `solv` | `solv` | `2.57.122.238` | 2026-06-08T08:07:24 |
| `solv` | `1234` | `2.57.122.238` | 2026-06-08T08:09:39 |
| `solv` | `123456` | `2.57.122.238` | 2026-06-08T08:11:53 |
| `solv` | `12345678` | `2.57.122.238` | 2026-06-08T08:14:02 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-06-08T08:16:18 |
| `root` | `LeitboGi0ro` | `84.235.233.122` | 2026-06-08T08:18:35 |
| `root` | `123@@@` | `84.235.233.122` | 2026-06-08T08:18:35 |
| `node` | `node` | `2.57.122.238` | 2026-06-08T08:18:37 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-06-08T08:20:53 |
| `validator` | `validator` | `2.57.122.238` | 2026-06-08T08:23:17 |
| `sol` | `sol123` | `2.57.122.238` | 2026-06-08T08:25:30 |
| `root` | `LeitboGi0ro` | `168.138.54.39` | 2026-06-08T08:27:42 |
| `root` | `123@@@` | `168.138.54.39` | 2026-06-08T08:27:42 |
| `sol` | `123` | `2.57.122.238` | 2026-06-08T08:27:44 |
| `sol` | `12345678` | `2.57.122.238` | 2026-06-08T08:30:02 |
| `root` | `admin` | `45.198.224.143` | 2026-06-08T08:32:51 |
| `admin` | `admin` | `34.38.93.241` | 2026-06-08T08:42:26 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-08T08:53:09 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-08T08:53:09 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-08T08:55:39 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-08T08:55:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.241.233.50` | 2026-06-08T09:03:19 |
| `*1` | `$4` | `35.241.233.50` | 2026-06-08T09:03:28 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3181` | `35.241.233.50` | 2026-06-08T09:03:30 |
| `root` | `` | `176.65.139.174` | 2026-06-08T09:22:38 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `43.98.191.130` | 2026-06-08T09:38:13 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `43.98.191.130` | 2026-06-08T09:38:24 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `43.98.180.199` | 2026-06-08T09:39:12 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `43.98.180.199` | 2026-06-08T09:39:24 |
| `USER test` | `USER test` | `43.98.180.199` | 2026-06-08T09:39:32 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-08T10:45:41 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-08T10:45:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **213** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 15 |
| Go SSH scanner | 13 |
| OpenSSH | 10 |
| Nmap scanner | 9 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 15 | 5 |
| `16443846184e...` | Generic scanner | 12 | 1 |
| `a984ff804585...` | libssh-based | 10 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 15 | 5 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 1 | Generic scanner |
| `a984ff804585...` | OpenSSH | 10 | 2 | libssh-based |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | Nmap scanner | 2 | 2 | — |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
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
Source IPs: `176.65.139.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **19** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |
| `AS267784` | Flyservers S.A. | 1 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-945b8d9dfc86

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:05 |
| **Last Seen** | 2026-06-08 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:05:06` | `cowrie.session.connect` |
| `2026-06-08 08:05:06` | `cowrie.client.version` |
| `2026-06-08 08:05:06` | `cowrie.client.kex` |
| `2026-06-08 08:05:06` | `cowrie.login.success` |
| `2026-06-08 08:05:07` | `cowrie.session.params` |
| `2026-06-08 08:05:07` | `cowrie.command.input` |
| `2026-06-08 08:05:07` | `cowrie.log.closed` |
| `2026-06-08 08:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa4d48b1178

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:07 |
| **Last Seen** | 2026-06-08 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:07:24` | `cowrie.session.connect` |
| `2026-06-08 08:07:24` | `cowrie.client.version` |
| `2026-06-08 08:07:24` | `cowrie.client.kex` |
| `2026-06-08 08:07:24` | `cowrie.login.success` |
| `2026-06-08 08:07:25` | `cowrie.session.params` |
| `2026-06-08 08:07:25` | `cowrie.command.input` |
| `2026-06-08 08:07:25` | `cowrie.log.closed` |
| `2026-06-08 08:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf8387f4075

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:09 |
| **Last Seen** | 2026-06-08 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:09:39` | `cowrie.session.connect` |
| `2026-06-08 08:09:39` | `cowrie.client.version` |
| `2026-06-08 08:09:39` | `cowrie.client.kex` |
| `2026-06-08 08:09:39` | `cowrie.login.success` |
| `2026-06-08 08:09:40` | `cowrie.session.params` |
| `2026-06-08 08:09:40` | `cowrie.command.input` |
| `2026-06-08 08:09:40` | `cowrie.log.closed` |
| `2026-06-08 08:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bd1c253c13

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:11 |
| **Last Seen** | 2026-06-08 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:11:52` | `cowrie.session.connect` |
| `2026-06-08 08:11:52` | `cowrie.client.version` |
| `2026-06-08 08:11:52` | `cowrie.client.kex` |
| `2026-06-08 08:11:53` | `cowrie.login.success` |
| `2026-06-08 08:11:53` | `cowrie.session.params` |
| `2026-06-08 08:11:53` | `cowrie.command.input` |
| `2026-06-08 08:11:54` | `cowrie.log.closed` |
| `2026-06-08 08:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d04e75f0ce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:14 |
| **Last Seen** | 2026-06-08 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:14:02` | `cowrie.session.connect` |
| `2026-06-08 08:14:02` | `cowrie.client.version` |
| `2026-06-08 08:14:02` | `cowrie.client.kex` |
| `2026-06-08 08:14:02` | `cowrie.login.success` |
| `2026-06-08 08:14:03` | `cowrie.session.params` |
| `2026-06-08 08:14:03` | `cowrie.command.input` |
| `2026-06-08 08:14:03` | `cowrie.log.closed` |
| `2026-06-08 08:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4f5eda5f58

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:16 |
| **Last Seen** | 2026-06-08 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:16:17` | `cowrie.session.connect` |
| `2026-06-08 08:16:17` | `cowrie.client.version` |
| `2026-06-08 08:16:18` | `cowrie.client.kex` |
| `2026-06-08 08:16:18` | `cowrie.login.success` |
| `2026-06-08 08:16:19` | `cowrie.session.params` |
| `2026-06-08 08:16:19` | `cowrie.command.input` |
| `2026-06-08 08:16:19` | `cowrie.log.closed` |
| `2026-06-08 08:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b028718043c

| Field | Detail |
|---|---|
| **Source IP** | `84.235.233[.]122` |
| **First Seen** | 2026-06-08 08:18 |
| **Last Seen** | 2026-06-08 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:18:35` | `cowrie.session.connect` |
| `2026-06-08 08:18:35` | `cowrie.client.version` |
| `2026-06-08 08:18:35` | `cowrie.client.kex` |
| `2026-06-08 08:18:35` | `cowrie.login.success` |
| `2026-06-08 08:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.235.233[.]122` to AbuseIPDB if not already reported
- [ ] Block `84.235.233[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c95d385ff0f

| Field | Detail |
|---|---|
| **Source IP** | `84.235.233[.]122` |
| **First Seen** | 2026-06-08 08:18 |
| **Last Seen** | 2026-06-08 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:18:35` | `cowrie.session.connect` |
| `2026-06-08 08:18:35` | `cowrie.client.version` |
| `2026-06-08 08:18:35` | `cowrie.client.kex` |
| `2026-06-08 08:18:35` | `cowrie.login.success` |
| `2026-06-08 08:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.235.233[.]122` to AbuseIPDB if not already reported
- [ ] Block `84.235.233[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a5048ecb9b3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:18 |
| **Last Seen** | 2026-06-08 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:18:37` | `cowrie.session.connect` |
| `2026-06-08 08:18:37` | `cowrie.client.version` |
| `2026-06-08 08:18:37` | `cowrie.client.kex` |
| `2026-06-08 08:18:37` | `cowrie.login.success` |
| `2026-06-08 08:18:38` | `cowrie.session.params` |
| `2026-06-08 08:18:38` | `cowrie.command.input` |
| `2026-06-08 08:18:38` | `cowrie.log.closed` |
| `2026-06-08 08:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a432a99410b

| Field | Detail |
|---|---|
| **Source IP** | `84.235.233[.]122` |
| **First Seen** | 2026-06-08 08:18 |
| **Last Seen** | 2026-06-08 08:21 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:18:57` | `cowrie.session.connect` |
| `2026-06-08 08:18:57` | `cowrie.client.version` |
| `2026-06-08 08:18:57` | `cowrie.client.kex` |
| `2026-06-08 08:18:57` | `cowrie.login.success` |
| `2026-06-08 08:18:58` | `cowrie.session.file_upload` |
| `2026-06-08 08:18:59` | `cowrie.session.params` |
| `2026-06-08 08:18:59` | `cowrie.command.input` |
| `2026-06-08 08:18:59` | `cowrie.command.input` |
| `2026-06-08 08:18:59` | `cowrie.command.input` |
| `2026-06-08 08:18:59` | `cowrie.command.failed` |
| `2026-06-08 08:18:59` | `cowrie.log.closed` |
| `2026-06-08 08:19:00` | `cowrie.session.params` |
| `2026-06-08 08:19:00` | `cowrie.command.input` |
| `2026-06-08 08:19:00` | `cowrie.log.closed` |
| `2026-06-08 08:19:01` | `cowrie.session.params` |
| `2026-06-08 08:19:01` | `cowrie.command.input` |
| `2026-06-08 08:19:01` | `cowrie.log.closed` |
| `2026-06-08 08:19:02` | `cowrie.session.params` |
| `2026-06-08 08:19:02` | `cowrie.command.input` |
| `2026-06-08 08:19:02` | `cowrie.command.failed` |
| `2026-06-08 08:19:02` | `cowrie.command.failed` |
| `2026-06-08 08:20:03` | `cowrie.session.params` |
| `2026-06-08 08:20:03` | `cowrie.command.input` |
| `2026-06-08 08:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.235.233[.]122` to AbuseIPDB if not already reported
- [ ] Block `84.235.233[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354a782b00df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:20 |
| **Last Seen** | 2026-06-08 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:20:53` | `cowrie.session.connect` |
| `2026-06-08 08:20:53` | `cowrie.client.version` |
| `2026-06-08 08:20:53` | `cowrie.client.kex` |
| `2026-06-08 08:20:53` | `cowrie.login.success` |
| `2026-06-08 08:20:54` | `cowrie.session.params` |
| `2026-06-08 08:20:54` | `cowrie.command.input` |
| `2026-06-08 08:20:54` | `cowrie.log.closed` |
| `2026-06-08 08:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b0bd5e7963

| Field | Detail |
|---|---|
| **Source IP** | `84.235.233[.]122` |
| **First Seen** | 2026-06-08 08:21 |
| **Last Seen** | 2026-06-08 08:23 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:21:26` | `cowrie.session.connect` |
| `2026-06-08 08:21:26` | `cowrie.client.version` |
| `2026-06-08 08:21:26` | `cowrie.client.kex` |
| `2026-06-08 08:21:27` | `cowrie.login.success` |
| `2026-06-08 08:21:28` | `cowrie.session.file_upload` |
| `2026-06-08 08:21:29` | `cowrie.session.params` |
| `2026-06-08 08:21:29` | `cowrie.command.input` |
| `2026-06-08 08:21:29` | `cowrie.command.input` |
| `2026-06-08 08:21:29` | `cowrie.command.input` |
| `2026-06-08 08:21:29` | `cowrie.command.failed` |
| `2026-06-08 08:21:29` | `cowrie.log.closed` |
| `2026-06-08 08:21:29` | `cowrie.session.params` |
| `2026-06-08 08:21:29` | `cowrie.command.input` |
| `2026-06-08 08:21:30` | `cowrie.log.closed` |
| `2026-06-08 08:21:30` | `cowrie.session.params` |
| `2026-06-08 08:21:30` | `cowrie.command.input` |
| `2026-06-08 08:21:31` | `cowrie.log.closed` |
| `2026-06-08 08:21:31` | `cowrie.session.params` |
| `2026-06-08 08:21:31` | `cowrie.command.input` |
| `2026-06-08 08:21:31` | `cowrie.command.failed` |
| `2026-06-08 08:21:31` | `cowrie.command.failed` |
| `2026-06-08 08:22:32` | `cowrie.session.params` |
| `2026-06-08 08:22:32` | `cowrie.command.input` |
| `2026-06-08 08:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.235.233[.]122` to AbuseIPDB if not already reported
- [ ] Block `84.235.233[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d829d5b3b70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:23 |
| **Last Seen** | 2026-06-08 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:23:17` | `cowrie.session.connect` |
| `2026-06-08 08:23:17` | `cowrie.client.version` |
| `2026-06-08 08:23:17` | `cowrie.client.kex` |
| `2026-06-08 08:23:17` | `cowrie.login.success` |
| `2026-06-08 08:23:18` | `cowrie.session.params` |
| `2026-06-08 08:23:18` | `cowrie.command.input` |
| `2026-06-08 08:23:18` | `cowrie.log.closed` |
| `2026-06-08 08:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be85e8246d35

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:25 |
| **Last Seen** | 2026-06-08 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:25:30` | `cowrie.session.connect` |
| `2026-06-08 08:25:30` | `cowrie.client.version` |
| `2026-06-08 08:25:30` | `cowrie.client.kex` |
| `2026-06-08 08:25:30` | `cowrie.login.success` |
| `2026-06-08 08:25:31` | `cowrie.session.params` |
| `2026-06-08 08:25:31` | `cowrie.command.input` |
| `2026-06-08 08:25:31` | `cowrie.log.closed` |
| `2026-06-08 08:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2965e3428d79

| Field | Detail |
|---|---|
| **Source IP** | `168.138.54[.]39` |
| **First Seen** | 2026-06-08 08:27 |
| **Last Seen** | 2026-06-08 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:27:41` | `cowrie.session.connect` |
| `2026-06-08 08:27:41` | `cowrie.client.version` |
| `2026-06-08 08:27:41` | `cowrie.client.kex` |
| `2026-06-08 08:27:42` | `cowrie.login.success` |
| `2026-06-08 08:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.138.54[.]39` to AbuseIPDB if not already reported
- [ ] Block `168.138.54[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c28c78b6c3

| Field | Detail |
|---|---|
| **Source IP** | `168.138.54[.]39` |
| **First Seen** | 2026-06-08 08:27 |
| **Last Seen** | 2026-06-08 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:27:41` | `cowrie.session.connect` |
| `2026-06-08 08:27:41` | `cowrie.client.version` |
| `2026-06-08 08:27:41` | `cowrie.client.kex` |
| `2026-06-08 08:27:42` | `cowrie.login.success` |
| `2026-06-08 08:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.138.54[.]39` to AbuseIPDB if not already reported
- [ ] Block `168.138.54[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec58af1f1fa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:27 |
| **Last Seen** | 2026-06-08 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:27:43` | `cowrie.session.connect` |
| `2026-06-08 08:27:43` | `cowrie.client.version` |
| `2026-06-08 08:27:43` | `cowrie.client.kex` |
| `2026-06-08 08:27:44` | `cowrie.login.success` |
| `2026-06-08 08:27:45` | `cowrie.session.params` |
| `2026-06-08 08:27:45` | `cowrie.command.input` |
| `2026-06-08 08:27:45` | `cowrie.log.closed` |
| `2026-06-08 08:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62fb3ec5e121

| Field | Detail |
|---|---|
| **Source IP** | `168.138.54[.]39` |
| **First Seen** | 2026-06-08 08:27 |
| **Last Seen** | 2026-06-08 08:30 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:27:58` | `cowrie.session.connect` |
| `2026-06-08 08:27:58` | `cowrie.client.version` |
| `2026-06-08 08:27:58` | `cowrie.client.kex` |
| `2026-06-08 08:27:59` | `cowrie.login.success` |
| `2026-06-08 08:28:00` | `cowrie.session.file_upload` |
| `2026-06-08 08:28:01` | `cowrie.session.params` |
| `2026-06-08 08:28:01` | `cowrie.command.input` |
| `2026-06-08 08:28:01` | `cowrie.command.input` |
| `2026-06-08 08:28:01` | `cowrie.command.input` |
| `2026-06-08 08:28:01` | `cowrie.command.failed` |
| `2026-06-08 08:28:01` | `cowrie.log.closed` |
| `2026-06-08 08:28:02` | `cowrie.session.params` |
| `2026-06-08 08:28:02` | `cowrie.command.input` |
| `2026-06-08 08:28:02` | `cowrie.log.closed` |
| `2026-06-08 08:28:03` | `cowrie.session.params` |
| `2026-06-08 08:28:03` | `cowrie.command.input` |
| `2026-06-08 08:28:04` | `cowrie.log.closed` |
| `2026-06-08 08:28:05` | `cowrie.session.params` |
| `2026-06-08 08:28:05` | `cowrie.command.input` |
| `2026-06-08 08:28:05` | `cowrie.command.failed` |
| `2026-06-08 08:28:05` | `cowrie.command.failed` |
| `2026-06-08 08:29:06` | `cowrie.session.params` |
| `2026-06-08 08:29:06` | `cowrie.command.input` |
| `2026-06-08 08:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.138.54[.]39` to AbuseIPDB if not already reported
- [ ] Block `168.138.54[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a3314cf401

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-08 08:30 |
| **Last Seen** | 2026-06-08 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:30:01` | `cowrie.session.connect` |
| `2026-06-08 08:30:01` | `cowrie.client.version` |
| `2026-06-08 08:30:01` | `cowrie.client.kex` |
| `2026-06-08 08:30:02` | `cowrie.login.success` |
| `2026-06-08 08:30:03` | `cowrie.session.params` |
| `2026-06-08 08:30:03` | `cowrie.command.input` |
| `2026-06-08 08:30:03` | `cowrie.log.closed` |
| `2026-06-08 08:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9faf4099ebaa

| Field | Detail |
|---|---|
| **Source IP** | `168.138.54[.]39` |
| **First Seen** | 2026-06-08 08:30 |
| **Last Seen** | 2026-06-08 08:32 |
| **Session Duration** | 132s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:30:23` | `cowrie.session.connect` |
| `2026-06-08 08:30:23` | `cowrie.client.version` |
| `2026-06-08 08:30:23` | `cowrie.client.kex` |
| `2026-06-08 08:30:24` | `cowrie.login.success` |
| `2026-06-08 08:30:26` | `cowrie.session.file_upload` |
| `2026-06-08 08:30:27` | `cowrie.session.params` |
| `2026-06-08 08:30:27` | `cowrie.command.input` |
| `2026-06-08 08:30:27` | `cowrie.command.input` |
| `2026-06-08 08:30:27` | `cowrie.command.input` |
| `2026-06-08 08:30:27` | `cowrie.command.failed` |
| `2026-06-08 08:30:27` | `cowrie.log.closed` |
| `2026-06-08 08:30:28` | `cowrie.session.params` |
| `2026-06-08 08:30:28` | `cowrie.command.input` |
| `2026-06-08 08:30:28` | `cowrie.log.closed` |
| `2026-06-08 08:30:29` | `cowrie.session.params` |
| `2026-06-08 08:30:29` | `cowrie.command.input` |
| `2026-06-08 08:30:29` | `cowrie.log.closed` |
| `2026-06-08 08:30:30` | `cowrie.session.params` |
| `2026-06-08 08:30:30` | `cowrie.command.input` |
| `2026-06-08 08:30:30` | `cowrie.command.failed` |
| `2026-06-08 08:30:30` | `cowrie.command.failed` |
| `2026-06-08 08:31:31` | `cowrie.session.params` |
| `2026-06-08 08:31:31` | `cowrie.command.input` |
| `2026-06-08 08:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.138.54[.]39` to AbuseIPDB if not already reported
- [ ] Block `168.138.54[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89d2e78f0ca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]143` |
| **First Seen** | 2026-06-08 08:32 |
| **Last Seen** | 2026-06-08 08:35 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:32:50` | `cowrie.session.connect` |
| `2026-06-08 08:32:51` | `cowrie.login.success` |
| `2026-06-08 08:32:51` | `cowrie.session.params` |
| `2026-06-08 08:35:51` | `cowrie.log.closed` |
| `2026-06-08 08:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]143` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7970f61e9457

| Field | Detail |
|---|---|
| **Source IP** | `34.38.93[.]241` |
| **First Seen** | 2026-06-08 08:42 |
| **Last Seen** | 2026-06-08 08:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:42:24` | `cowrie.session.connect` |
| `2026-06-08 08:42:24` | `cowrie.client.version` |
| `2026-06-08 08:42:24` | `cowrie.client.kex` |
| `2026-06-08 08:42:26` | `cowrie.login.success` |
| `2026-06-08 08:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.93[.]241` to AbuseIPDB if not already reported
- [ ] Block `34.38.93[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc29a378ec5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 08:53 |
| **Last Seen** | 2026-06-08 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:53:09` | `cowrie.session.connect` |
| `2026-06-08 08:53:09` | `cowrie.client.version` |
| `2026-06-08 08:53:09` | `cowrie.client.kex` |
| `2026-06-08 08:53:09` | `cowrie.login.success` |
| `2026-06-08 08:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6a678b1169

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 08:53 |
| **Last Seen** | 2026-06-08 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:53:09` | `cowrie.session.connect` |
| `2026-06-08 08:53:09` | `cowrie.client.version` |
| `2026-06-08 08:53:09` | `cowrie.client.kex` |
| `2026-06-08 08:53:09` | `cowrie.login.success` |
| `2026-06-08 08:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15fa17a437bc

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-08 08:55 |
| **Last Seen** | 2026-06-08 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:55:38` | `cowrie.session.connect` |
| `2026-06-08 08:55:38` | `cowrie.client.version` |
| `2026-06-08 08:55:38` | `cowrie.client.kex` |
| `2026-06-08 08:55:39` | `cowrie.login.success` |
| `2026-06-08 08:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbd225f99cf

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-08 08:55 |
| **Last Seen** | 2026-06-08 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:55:38` | `cowrie.session.connect` |
| `2026-06-08 08:55:38` | `cowrie.client.version` |
| `2026-06-08 08:55:38` | `cowrie.client.kex` |
| `2026-06-08 08:55:39` | `cowrie.login.success` |
| `2026-06-08 08:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa690a4031b

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-08 08:57 |
| **Last Seen** | 2026-06-08 08:59 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:57:37` | `cowrie.session.connect` |
| `2026-06-08 08:57:37` | `cowrie.client.version` |
| `2026-06-08 08:57:38` | `cowrie.client.kex` |
| `2026-06-08 08:57:39` | `cowrie.login.success` |
| `2026-06-08 08:57:41` | `cowrie.session.file_upload` |
| `2026-06-08 08:57:42` | `cowrie.session.params` |
| `2026-06-08 08:57:42` | `cowrie.command.input` |
| `2026-06-08 08:57:42` | `cowrie.command.input` |
| `2026-06-08 08:57:42` | `cowrie.command.input` |
| `2026-06-08 08:57:42` | `cowrie.command.failed` |
| `2026-06-08 08:57:42` | `cowrie.log.closed` |
| `2026-06-08 08:57:43` | `cowrie.session.params` |
| `2026-06-08 08:57:43` | `cowrie.command.input` |
| `2026-06-08 08:57:44` | `cowrie.log.closed` |
| `2026-06-08 08:57:45` | `cowrie.session.params` |
| `2026-06-08 08:57:45` | `cowrie.command.input` |
| `2026-06-08 08:57:45` | `cowrie.log.closed` |
| `2026-06-08 08:57:46` | `cowrie.session.params` |
| `2026-06-08 08:57:46` | `cowrie.command.input` |
| `2026-06-08 08:57:46` | `cowrie.command.failed` |
| `2026-06-08 08:57:46` | `cowrie.command.failed` |
| `2026-06-08 08:58:47` | `cowrie.session.params` |
| `2026-06-08 08:58:47` | `cowrie.command.input` |
| `2026-06-08 08:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d2d7e19139

| Field | Detail |
|---|---|
| **Source IP** | `35.241.233[.]50` |
| **First Seen** | 2026-06-08 09:03 |
| **Last Seen** | 2026-06-08 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:03:19` | `cowrie.session.connect` |
| `2026-06-08 09:03:19` | `cowrie.login.success` |
| `2026-06-08 09:03:20` | `cowrie.session.params` |
| `2026-06-08 09:03:20` | `cowrie.command.input` |
| `2026-06-08 09:03:20` | `cowrie.command.input` |
| `2026-06-08 09:03:20` | `cowrie.command.failed` |
| `2026-06-08 09:03:20` | `cowrie.command.input` |
| `2026-06-08 09:03:20` | `cowrie.log.closed` |
| `2026-06-08 09:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.233[.]50` to AbuseIPDB if not already reported
- [ ] Block `35.241.233[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fc9533e1a2

| Field | Detail |
|---|---|
| **Source IP** | `35.241.233[.]50` |
| **First Seen** | 2026-06-08 09:03 |
| **Last Seen** | 2026-06-08 09:03 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:03:28` | `cowrie.session.connect` |
| `2026-06-08 09:03:28` | `cowrie.login.success` |
| `2026-06-08 09:03:28` | `cowrie.session.params` |
| `2026-06-08 09:03:28` | `cowrie.command.input` |
| `2026-06-08 09:03:28` | `cowrie.command.failed` |
| `2026-06-08 09:03:47` | `cowrie.log.closed` |
| `2026-06-08 09:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.233[.]50` to AbuseIPDB if not already reported
- [ ] Block `35.241.233[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c665502adde3

| Field | Detail |
|---|---|
| **Source IP** | `35.241.233[.]50` |
| **First Seen** | 2026-06-08 09:03 |
| **Last Seen** | 2026-06-08 09:03 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:03:30` | `cowrie.session.connect` |
| `2026-06-08 09:03:30` | `cowrie.login.success` |
| `2026-06-08 09:03:30` | `cowrie.session.params` |
| `2026-06-08 09:03:30` | `cowrie.command.input` |
| `2026-06-08 09:03:47` | `cowrie.log.closed` |
| `2026-06-08 09:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.233[.]50` to AbuseIPDB if not already reported
- [ ] Block `35.241.233[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e47430f367

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]174` |
| **First Seen** | 2026-06-08 09:22 |
| **Last Seen** | 2026-06-08 09:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:22:37` | `cowrie.session.connect` |
| `2026-06-08 09:22:38` | `cowrie.login.success` |
| `2026-06-08 09:22:39` | `cowrie.session.params` |
| `2026-06-08 09:22:39` | `cowrie.command.input` |
| `2026-06-08 09:22:40` | `cowrie.command.input` |
| `2026-06-08 09:22:41` | `cowrie.command.input` |
| `2026-06-08 09:22:42` | `cowrie.command.input` |
| `2026-06-08 09:22:42` | `cowrie.command.failed` |
| `2026-06-08 09:22:42` | `cowrie.log.closed` |
| `2026-06-08 09:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]174` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847250d81eaf

| Field | Detail |
|---|---|
| **Source IP** | `43.98.191[.]130` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:13` | `cowrie.session.connect` |
| `2026-06-08 09:38:13` | `cowrie.login.success` |
| `2026-06-08 09:38:13` | `cowrie.session.params` |
| `2026-06-08 09:38:13` | `cowrie.command.input` |
| `2026-06-08 09:38:13` | `cowrie.command.failed` |
| `2026-06-08 09:38:13` | `cowrie.command.input` |
| `2026-06-08 09:38:18` | `cowrie.log.closed` |
| `2026-06-08 09:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.98.191[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a14392986f24

| Field | Detail |
|---|---|
| **Source IP** | `43.98.191[.]130` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:24` | `cowrie.session.connect` |
| `2026-06-08 09:38:24` | `cowrie.login.success` |
| `2026-06-08 09:38:24` | `cowrie.session.params` |
| `2026-06-08 09:38:25` | `cowrie.log.closed` |
| `2026-06-08 09:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.98.191[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71da971f4e3c

| Field | Detail |
|---|---|
| **Source IP** | `43.98.191[.]130` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:25` | `cowrie.session.connect` |
| `2026-06-08 09:38:25` | `cowrie.login.success` |
| `2026-06-08 09:38:26` | `cowrie.session.params` |
| `2026-06-08 09:38:26` | `cowrie.command.input` |
| `2026-06-08 09:38:31` | `cowrie.log.closed` |
| `2026-06-08 09:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.98.191[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4136da033fac

| Field | Detail |
|---|---|
| **Source IP** | `43.98.180[.]199` |
| **First Seen** | 2026-06-08 09:39 |
| **Last Seen** | 2026-06-08 09:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:39:12` | `cowrie.session.connect` |
| `2026-06-08 09:39:12` | `cowrie.login.success` |
| `2026-06-08 09:39:13` | `cowrie.session.params` |
| `2026-06-08 09:39:13` | `cowrie.command.input` |
| `2026-06-08 09:39:13` | `cowrie.command.failed` |
| `2026-06-08 09:39:13` | `cowrie.command.input` |
| `2026-06-08 09:39:18` | `cowrie.log.closed` |
| `2026-06-08 09:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.180[.]199` to AbuseIPDB if not already reported
- [ ] Block `43.98.180[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1e496fde2f

| Field | Detail |
|---|---|
| **Source IP** | `43.98.180[.]199` |
| **First Seen** | 2026-06-08 09:39 |
| **Last Seen** | 2026-06-08 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:39:24` | `cowrie.session.connect` |
| `2026-06-08 09:39:24` | `cowrie.login.success` |
| `2026-06-08 09:39:24` | `cowrie.session.params` |
| `2026-06-08 09:39:24` | `cowrie.log.closed` |
| `2026-06-08 09:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.180[.]199` to AbuseIPDB if not already reported
- [ ] Block `43.98.180[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c55c556dca

| Field | Detail |
|---|---|
| **Source IP** | `43.98.180[.]199` |
| **First Seen** | 2026-06-08 09:39 |
| **Last Seen** | 2026-06-08 09:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:39:25` | `cowrie.session.connect` |
| `2026-06-08 09:39:25` | `cowrie.login.success` |
| `2026-06-08 09:39:25` | `cowrie.session.params` |
| `2026-06-08 09:39:25` | `cowrie.command.input` |
| `2026-06-08 09:39:31` | `cowrie.log.closed` |
| `2026-06-08 09:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.180[.]199` to AbuseIPDB if not already reported
- [ ] Block `43.98.180[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f109760d58a

| Field | Detail |
|---|---|
| **Source IP** | `43.98.180[.]199` |
| **First Seen** | 2026-06-08 09:39 |
| **Last Seen** | 2026-06-08 09:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `USER test, USER test, USER test, USER test` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:39:31` | `cowrie.session.connect` |
| `2026-06-08 09:39:32` | `cowrie.login.success` |
| `2026-06-08 09:39:33` | `cowrie.session.params` |
| `2026-06-08 09:39:33` | `cowrie.command.input` |
| `2026-06-08 09:39:33` | `cowrie.command.failed` |
| `2026-06-08 09:39:34` | `cowrie.command.input` |
| `2026-06-08 09:39:34` | `cowrie.command.failed` |
| `2026-06-08 09:39:35` | `cowrie.command.input` |
| `2026-06-08 09:39:35` | `cowrie.command.failed` |
| `2026-06-08 09:39:36` | `cowrie.command.input` |
| `2026-06-08 09:39:36` | `cowrie.command.failed` |
| `2026-06-08 09:39:36` | `cowrie.log.closed` |
| `2026-06-08 09:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.180[.]199` to AbuseIPDB if not already reported
- [ ] Block `43.98.180[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da393fe571ab

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-08 10:45 |
| **Last Seen** | 2026-06-08 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:45:40` | `cowrie.session.connect` |
| `2026-06-08 10:45:40` | `cowrie.client.version` |
| `2026-06-08 10:45:40` | `cowrie.client.kex` |
| `2026-06-08 10:45:41` | `cowrie.login.success` |
| `2026-06-08 10:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2228d10dd565

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-08 10:45 |
| **Last Seen** | 2026-06-08 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:45:40` | `cowrie.session.connect` |
| `2026-06-08 10:45:40` | `cowrie.client.version` |
| `2026-06-08 10:45:41` | `cowrie.client.kex` |
| `2026-06-08 10:45:41` | `cowrie.login.success` |
| `2026-06-08 10:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **41** | 2026-06-08 08:13 | 2026-06-08 10:51 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `35.241.233[.]50` | **30** | 2026-06-08 09:03 | 2026-06-08 09:03 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `107.174.155[.]67` | **29** | 2026-06-08 08:14 | 2026-06-08 10:54 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.93[.]241` | **11** | 2026-06-08 08:42 | 2026-06-08 08:42 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `80.151.14[.]195` | **9** | 2026-06-08 10:12 | 2026-06-08 10:54 | 16m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-06-08 09:43 | 2026-06-08 09:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.35.7[.]46` | 1 | 2026-06-08 10:30 | 2026-06-08 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.75[.]127` | 1 | 2026-06-08 08:56 | 2026-06-08 08:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.141.253[.]53` | 1 | 2026-06-08 09:48 | 2026-06-08 09:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-06-08 10:11 | 2026-06-08 10:13 | 84s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]174` | 1 | 2026-06-08 09:22 | 2026-06-08 09:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.62.39[.]8` | 1 | 2026-06-08 08:56 | 2026-06-08 08:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `3.21.163[.]185` | 1 | 2026-06-08 10:54 | 2026-06-08 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-08 10:06 | 2026-06-08 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-08 08:36 | 2026-06-08 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.79.20[.]59` | 1 | 2026-06-08 10:12 | 2026-06-08 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-08 09:07 | 2026-06-08 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.219.233[.]233` | 1 | 2026-06-08 09:23 | 2026-06-08 09:23 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `107.174.155[.]67` | US | sally wang | **100** ⚠️ | 0 |
| `3.21.163[.]185` | US | Amazon Technologies Inc. | **100** ⚠️ | 0 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `176.65.139[.]174` | NL | Storm Industries | **100** ⚠️ | 27 |
| `178.62.39[.]8` | GB | DigitalOcean London | **100** ⚠️ | 13 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `34.38.93[.]241` | BE | Google LLC | **100** ⚠️ | 0 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `80.151.14[.]195` | DE | Deutsche Telekom AG | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 213 cases |
| Tool 34  | Credential Extractor        | ✅ 40 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (16.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 126 session(s)).

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
_Report time: 2026-06-08T11:04:58Z_

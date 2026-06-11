# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T06:05:53Z |
| **Shift Time** | 06:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **156** |
| Confirmed Threats | **84** |
| False Positives Filtered | **72** (46.2%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **14** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **119** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **37** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **10** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `admin` | 3 |
| `GET / HTTP/1.1` | 3 |
| `*1` | 3 |
| `OPTIONS rtsp://example.com RTSP/1.0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 8 |
| `123@@@` | 5 |
| `smo@@kkklss` | 4 |
| `Host: 129.80.119.236:23` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 8 |
| `root` | `123@@@` | 5 |
| `root` | `smo@@kkklss` | 4 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `deftone` | `2.57.121.112` | 2026-06-11T03:03:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.6.211` | 2026-06-11T03:34:50 |
| `*1` | `$4` | `35.205.6.211` | 2026-06-11T03:34:58 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5903` | `35.205.6.211` | 2026-06-11T03:35:00 |
| `root` | `admin` | `45.198.224.143` | 2026-06-11T03:38:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-11T03:58:26 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-11T03:58:27 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-11T03:58:28 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-11T04:00:15 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-11T04:00:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.117.30` | 2026-06-11T04:01:59 |
| `*1` | `$4` | `34.38.117.30` | 2026-06-11T04:02:13 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3109` | `34.38.117.30` | 2026-06-11T04:02:15 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-11T04:02:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-11T04:02:22 |
| `wilfredo` | `wilfredo` | `213.209.159.56` | 2026-06-11T04:08:16 |
| `admin` | `daytona1` | `2.57.121.112` | 2026-06-11T04:24:32 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-11T04:32:38 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-11T04:32:39 |
| `admin` | `admin` | `116.99.174.228` | 2026-06-11T04:32:46 |
| `root` | `---fuck_you----` | `182.92.163.236` | 2026-06-11T04:34:12 |
| `root` | `admin` | `116.99.174.228` | 2026-06-11T04:39:41 |
| `installer` | `installer` | `116.99.174.228` | 2026-06-11T04:41:03 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.232.106` | 2026-06-11T04:41:13 |
| `*1` | `$4` | `34.38.232.106` | 2026-06-11T04:41:26 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5105` | `34.38.232.106` | 2026-06-11T04:41:28 |
| `user` | `user` | `116.99.174.228` | 2026-06-11T04:46:22 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-11T04:47:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-11T04:47:19 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-11T04:47:21 |
| `ubnt` | `ubnt` | `116.99.174.228` | 2026-06-11T04:51:29 |
| `squid` | `squid` | `116.99.174.228` | 2026-06-11T04:54:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **156** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 17 |
| AsyncSSH (Python) | 6 |
| Go SSH scanner | 6 |
| PuTTY | 4 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 13 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 6 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `57446c12547a...` | Mirai/variant | 3 | 2 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 13 | 4 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 6 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `57446c12547a...` | PuTTY | 3 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 3 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **18** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | LOW |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS28458` | IENTC S DE RL DE CV | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1fc2769756b3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 03:03 |
| **Last Seen** | 2026-06-11 03:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:03:38` | `cowrie.session.connect` |
| `2026-06-11 03:03:38` | `cowrie.client.version` |
| `2026-06-11 03:03:38` | `cowrie.client.kex` |
| `2026-06-11 03:03:39` | `cowrie.login.success` |
| `2026-06-11 03:03:39` | `cowrie.direct-tcpip.request` |
| `2026-06-11 03:03:39` | `cowrie.direct-tcpip.data` |
| `2026-06-11 03:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7691401b66c5

| Field | Detail |
|---|---|
| **Source IP** | `35.205.6[.]211` |
| **First Seen** | 2026-06-11 03:34 |
| **Last Seen** | 2026-06-11 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:34:50` | `cowrie.session.connect` |
| `2026-06-11 03:34:50` | `cowrie.login.success` |
| `2026-06-11 03:34:50` | `cowrie.session.params` |
| `2026-06-11 03:34:50` | `cowrie.command.input` |
| `2026-06-11 03:34:50` | `cowrie.command.input` |
| `2026-06-11 03:34:50` | `cowrie.command.failed` |
| `2026-06-11 03:34:50` | `cowrie.command.input` |
| `2026-06-11 03:34:51` | `cowrie.log.closed` |
| `2026-06-11 03:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.6[.]211` to AbuseIPDB if not already reported
- [ ] Block `35.205.6[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37999342ba99

| Field | Detail |
|---|---|
| **Source IP** | `35.205.6[.]211` |
| **First Seen** | 2026-06-11 03:34 |
| **Last Seen** | 2026-06-11 03:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:34:58` | `cowrie.session.connect` |
| `2026-06-11 03:34:58` | `cowrie.login.success` |
| `2026-06-11 03:34:59` | `cowrie.session.params` |
| `2026-06-11 03:34:59` | `cowrie.command.input` |
| `2026-06-11 03:34:59` | `cowrie.command.failed` |
| `2026-06-11 03:35:01` | `cowrie.log.closed` |
| `2026-06-11 03:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.6[.]211` to AbuseIPDB if not already reported
- [ ] Block `35.205.6[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb218ca2cd0c

| Field | Detail |
|---|---|
| **Source IP** | `35.205.6[.]211` |
| **First Seen** | 2026-06-11 03:35 |
| **Last Seen** | 2026-06-11 03:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:35:00` | `cowrie.session.connect` |
| `2026-06-11 03:35:00` | `cowrie.login.success` |
| `2026-06-11 03:35:01` | `cowrie.session.params` |
| `2026-06-11 03:35:01` | `cowrie.command.input` |
| `2026-06-11 03:35:16` | `cowrie.log.closed` |
| `2026-06-11 03:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.6[.]211` to AbuseIPDB if not already reported
- [ ] Block `35.205.6[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca5b2080175

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]143` |
| **First Seen** | 2026-06-11 03:38 |
| **Last Seen** | 2026-06-11 03:41 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:38:18` | `cowrie.session.connect` |
| `2026-06-11 03:38:18` | `cowrie.login.success` |
| `2026-06-11 03:38:19` | `cowrie.session.params` |
| `2026-06-11 03:41:19` | `cowrie.log.closed` |
| `2026-06-11 03:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]143` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac6f3ca4b22

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 03:58 |
| **Last Seen** | 2026-06-11 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:58:26` | `cowrie.session.connect` |
| `2026-06-11 03:58:26` | `cowrie.client.version` |
| `2026-06-11 03:58:26` | `cowrie.client.kex` |
| `2026-06-11 03:58:26` | `cowrie.login.success` |
| `2026-06-11 03:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c99ef6c119

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 03:58 |
| **Last Seen** | 2026-06-11 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:58:27` | `cowrie.session.connect` |
| `2026-06-11 03:58:27` | `cowrie.client.version` |
| `2026-06-11 03:58:27` | `cowrie.client.kex` |
| `2026-06-11 03:58:27` | `cowrie.login.success` |
| `2026-06-11 03:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4dc3951b3b1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 03:58 |
| **Last Seen** | 2026-06-11 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:58:28` | `cowrie.session.connect` |
| `2026-06-11 03:58:28` | `cowrie.client.version` |
| `2026-06-11 03:58:28` | `cowrie.client.kex` |
| `2026-06-11 03:58:28` | `cowrie.login.success` |
| `2026-06-11 03:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7299c97f642c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 03:58 |
| **Last Seen** | 2026-06-11 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 03:58:28` | `cowrie.session.connect` |
| `2026-06-11 03:58:28` | `cowrie.client.version` |
| `2026-06-11 03:58:28` | `cowrie.client.kex` |
| `2026-06-11 03:58:28` | `cowrie.login.success` |
| `2026-06-11 03:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb1eda24698

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 04:00 |
| **Last Seen** | 2026-06-11 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:00:13` | `cowrie.session.connect` |
| `2026-06-11 04:00:13` | `cowrie.client.version` |
| `2026-06-11 04:00:14` | `cowrie.client.kex` |
| `2026-06-11 04:00:15` | `cowrie.login.success` |
| `2026-06-11 04:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ce2381e5c7

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 04:00 |
| **Last Seen** | 2026-06-11 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:00:13` | `cowrie.session.connect` |
| `2026-06-11 04:00:13` | `cowrie.client.version` |
| `2026-06-11 04:00:14` | `cowrie.client.kex` |
| `2026-06-11 04:00:15` | `cowrie.login.success` |
| `2026-06-11 04:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0869137d9cc5

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 04:01 |
| **Last Seen** | 2026-06-11 04:03 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:01:13` | `cowrie.session.connect` |
| `2026-06-11 04:01:13` | `cowrie.client.version` |
| `2026-06-11 04:01:14` | `cowrie.client.kex` |
| `2026-06-11 04:01:15` | `cowrie.login.success` |
| `2026-06-11 04:01:17` | `cowrie.session.file_upload` |
| `2026-06-11 04:01:18` | `cowrie.session.params` |
| `2026-06-11 04:01:18` | `cowrie.command.input` |
| `2026-06-11 04:01:18` | `cowrie.command.input` |
| `2026-06-11 04:01:18` | `cowrie.command.input` |
| `2026-06-11 04:01:18` | `cowrie.command.failed` |
| `2026-06-11 04:01:18` | `cowrie.log.closed` |
| `2026-06-11 04:01:20` | `cowrie.session.params` |
| `2026-06-11 04:01:20` | `cowrie.command.input` |
| `2026-06-11 04:01:20` | `cowrie.log.closed` |
| `2026-06-11 04:01:21` | `cowrie.session.params` |
| `2026-06-11 04:01:21` | `cowrie.command.input` |
| `2026-06-11 04:01:21` | `cowrie.log.closed` |
| `2026-06-11 04:01:23` | `cowrie.session.params` |
| `2026-06-11 04:01:23` | `cowrie.command.input` |
| `2026-06-11 04:01:23` | `cowrie.command.failed` |
| `2026-06-11 04:01:23` | `cowrie.command.failed` |
| `2026-06-11 04:02:24` | `cowrie.session.params` |
| `2026-06-11 04:02:24` | `cowrie.command.input` |
| `2026-06-11 04:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d616abc1e5c

| Field | Detail |
|---|---|
| **Source IP** | `34.38.117[.]30` |
| **First Seen** | 2026-06-11 04:01 |
| **Last Seen** | 2026-06-11 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:01:59` | `cowrie.session.connect` |
| `2026-06-11 04:01:59` | `cowrie.login.success` |
| `2026-06-11 04:02:00` | `cowrie.session.params` |
| `2026-06-11 04:02:00` | `cowrie.command.input` |
| `2026-06-11 04:02:00` | `cowrie.command.input` |
| `2026-06-11 04:02:00` | `cowrie.command.failed` |
| `2026-06-11 04:02:00` | `cowrie.command.input` |
| `2026-06-11 04:02:00` | `cowrie.log.closed` |
| `2026-06-11 04:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.117[.]30` to AbuseIPDB if not already reported
- [ ] Block `34.38.117[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432c8d14cf65

| Field | Detail |
|---|---|
| **Source IP** | `34.38.117[.]30` |
| **First Seen** | 2026-06-11 04:02 |
| **Last Seen** | 2026-06-11 04:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:02:13` | `cowrie.session.connect` |
| `2026-06-11 04:02:13` | `cowrie.login.success` |
| `2026-06-11 04:02:13` | `cowrie.session.params` |
| `2026-06-11 04:02:13` | `cowrie.command.input` |
| `2026-06-11 04:02:13` | `cowrie.command.failed` |
| `2026-06-11 04:02:19` | `cowrie.log.closed` |
| `2026-06-11 04:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.117[.]30` to AbuseIPDB if not already reported
- [ ] Block `34.38.117[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64b4733ade7

| Field | Detail |
|---|---|
| **Source IP** | `34.38.117[.]30` |
| **First Seen** | 2026-06-11 04:02 |
| **Last Seen** | 2026-06-11 04:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:02:15` | `cowrie.session.connect` |
| `2026-06-11 04:02:15` | `cowrie.login.success` |
| `2026-06-11 04:02:15` | `cowrie.session.params` |
| `2026-06-11 04:02:15` | `cowrie.command.input` |
| `2026-06-11 04:02:19` | `cowrie.log.closed` |
| `2026-06-11 04:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.117[.]30` to AbuseIPDB if not already reported
- [ ] Block `34.38.117[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf2c2a45af0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 04:02 |
| **Last Seen** | 2026-06-11 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:02:21` | `cowrie.session.connect` |
| `2026-06-11 04:02:21` | `cowrie.client.version` |
| `2026-06-11 04:02:21` | `cowrie.client.kex` |
| `2026-06-11 04:02:22` | `cowrie.login.success` |
| `2026-06-11 04:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b492481798d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 04:02 |
| **Last Seen** | 2026-06-11 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:02:21` | `cowrie.session.connect` |
| `2026-06-11 04:02:21` | `cowrie.client.version` |
| `2026-06-11 04:02:22` | `cowrie.client.kex` |
| `2026-06-11 04:02:22` | `cowrie.login.success` |
| `2026-06-11 04:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf8d1b7c433

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 04:08 |
| **Last Seen** | 2026-06-11 04:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:08:15` | `cowrie.session.connect` |
| `2026-06-11 04:08:15` | `cowrie.client.version` |
| `2026-06-11 04:08:15` | `cowrie.client.kex` |
| `2026-06-11 04:08:16` | `cowrie.login.success` |
| `2026-06-11 04:08:16` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:08:16` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c839e5f802

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 04:24 |
| **Last Seen** | 2026-06-11 04:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:24:31` | `cowrie.session.connect` |
| `2026-06-11 04:24:31` | `cowrie.client.version` |
| `2026-06-11 04:24:31` | `cowrie.client.kex` |
| `2026-06-11 04:24:32` | `cowrie.login.success` |
| `2026-06-11 04:24:32` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:24:32` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e373b20bd0

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-11 04:32 |
| **Last Seen** | 2026-06-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:32:37` | `cowrie.session.connect` |
| `2026-06-11 04:32:37` | `cowrie.client.version` |
| `2026-06-11 04:32:37` | `cowrie.client.kex` |
| `2026-06-11 04:32:38` | `cowrie.login.success` |
| `2026-06-11 04:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e87d1fc0af

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-11 04:32 |
| **Last Seen** | 2026-06-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:32:38` | `cowrie.session.connect` |
| `2026-06-11 04:32:38` | `cowrie.client.version` |
| `2026-06-11 04:32:38` | `cowrie.client.kex` |
| `2026-06-11 04:32:39` | `cowrie.login.success` |
| `2026-06-11 04:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140ef761ad36

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:32 |
| **Last Seen** | 2026-06-11 04:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:32:43` | `cowrie.session.connect` |
| `2026-06-11 04:32:43` | `cowrie.client.version` |
| `2026-06-11 04:32:44` | `cowrie.client.kex` |
| `2026-06-11 04:32:46` | `cowrie.login.success` |
| `2026-06-11 04:32:47` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:32:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:32:48` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83476c2f84e6

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-11 04:33 |
| **Last Seen** | 2026-06-11 04:35 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:33:01` | `cowrie.session.connect` |
| `2026-06-11 04:33:01` | `cowrie.client.version` |
| `2026-06-11 04:33:01` | `cowrie.client.kex` |
| `2026-06-11 04:33:02` | `cowrie.login.success` |
| `2026-06-11 04:33:04` | `cowrie.session.file_upload` |
| `2026-06-11 04:33:05` | `cowrie.session.params` |
| `2026-06-11 04:33:05` | `cowrie.command.input` |
| `2026-06-11 04:33:05` | `cowrie.command.input` |
| `2026-06-11 04:33:05` | `cowrie.command.input` |
| `2026-06-11 04:33:05` | `cowrie.command.failed` |
| `2026-06-11 04:33:05` | `cowrie.log.closed` |
| `2026-06-11 04:33:06` | `cowrie.session.params` |
| `2026-06-11 04:33:06` | `cowrie.command.input` |
| `2026-06-11 04:33:07` | `cowrie.log.closed` |
| `2026-06-11 04:33:08` | `cowrie.session.params` |
| `2026-06-11 04:33:08` | `cowrie.command.input` |
| `2026-06-11 04:33:08` | `cowrie.log.closed` |
| `2026-06-11 04:33:09` | `cowrie.session.params` |
| `2026-06-11 04:33:09` | `cowrie.command.input` |
| `2026-06-11 04:33:09` | `cowrie.command.failed` |
| `2026-06-11 04:33:09` | `cowrie.command.failed` |
| `2026-06-11 04:34:10` | `cowrie.session.params` |
| `2026-06-11 04:34:10` | `cowrie.command.input` |
| `2026-06-11 04:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea4100e4e41

| Field | Detail |
|---|---|
| **Source IP** | `182.92.163[.]236` |
| **First Seen** | 2026-06-11 04:34 |
| **Last Seen** | 2026-06-11 04:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:34:09` | `cowrie.session.connect` |
| `2026-06-11 04:34:10` | `cowrie.client.version` |
| `2026-06-11 04:34:10` | `cowrie.client.kex` |
| `2026-06-11 04:34:12` | `cowrie.login.success` |
| `2026-06-11 04:34:14` | `cowrie.session.params` |
| `2026-06-11 04:34:14` | `cowrie.command.input` |
| `2026-06-11 04:34:14` | `cowrie.log.closed` |
| `2026-06-11 04:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.163[.]236` to AbuseIPDB if not already reported
- [ ] Block `182.92.163[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87ab6cb94d1

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-11 04:35 |
| **Last Seen** | 2026-06-11 04:37 |
| **Session Duration** | 132s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:35:27` | `cowrie.session.connect` |
| `2026-06-11 04:35:27` | `cowrie.client.version` |
| `2026-06-11 04:35:27` | `cowrie.client.kex` |
| `2026-06-11 04:35:28` | `cowrie.login.success` |
| `2026-06-11 04:35:30` | `cowrie.session.file_upload` |
| `2026-06-11 04:35:31` | `cowrie.session.params` |
| `2026-06-11 04:35:31` | `cowrie.command.input` |
| `2026-06-11 04:35:31` | `cowrie.command.input` |
| `2026-06-11 04:35:31` | `cowrie.command.input` |
| `2026-06-11 04:35:31` | `cowrie.command.failed` |
| `2026-06-11 04:35:31` | `cowrie.log.closed` |
| `2026-06-11 04:35:32` | `cowrie.session.params` |
| `2026-06-11 04:35:32` | `cowrie.command.input` |
| `2026-06-11 04:35:32` | `cowrie.log.closed` |
| `2026-06-11 04:35:33` | `cowrie.session.params` |
| `2026-06-11 04:35:33` | `cowrie.command.input` |
| `2026-06-11 04:35:34` | `cowrie.log.closed` |
| `2026-06-11 04:35:35` | `cowrie.session.params` |
| `2026-06-11 04:35:35` | `cowrie.command.input` |
| `2026-06-11 04:35:35` | `cowrie.command.failed` |
| `2026-06-11 04:35:35` | `cowrie.command.failed` |
| `2026-06-11 04:36:36` | `cowrie.session.params` |
| `2026-06-11 04:36:36` | `cowrie.command.input` |
| `2026-06-11 04:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f0bd8bb7dc

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:39 |
| **Last Seen** | 2026-06-11 04:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:39:38` | `cowrie.session.connect` |
| `2026-06-11 04:39:38` | `cowrie.client.version` |
| `2026-06-11 04:39:38` | `cowrie.client.kex` |
| `2026-06-11 04:39:41` | `cowrie.login.success` |
| `2026-06-11 04:39:42` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:39:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:39:43` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316e61921fcf

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:40 |
| **Last Seen** | 2026-06-11 04:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:40:59` | `cowrie.session.connect` |
| `2026-06-11 04:40:59` | `cowrie.client.version` |
| `2026-06-11 04:41:00` | `cowrie.client.kex` |
| `2026-06-11 04:41:03` | `cowrie.login.success` |
| `2026-06-11 04:41:03` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:41:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:41:03` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5306e745336

| Field | Detail |
|---|---|
| **Source IP** | `34.38.232[.]106` |
| **First Seen** | 2026-06-11 04:41 |
| **Last Seen** | 2026-06-11 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:41:13` | `cowrie.session.connect` |
| `2026-06-11 04:41:13` | `cowrie.login.success` |
| `2026-06-11 04:41:13` | `cowrie.session.params` |
| `2026-06-11 04:41:13` | `cowrie.command.input` |
| `2026-06-11 04:41:13` | `cowrie.command.input` |
| `2026-06-11 04:41:13` | `cowrie.command.failed` |
| `2026-06-11 04:41:13` | `cowrie.command.input` |
| `2026-06-11 04:41:13` | `cowrie.log.closed` |
| `2026-06-11 04:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.232[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.38.232[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781f5d97db2d

| Field | Detail |
|---|---|
| **Source IP** | `34.38.232[.]106` |
| **First Seen** | 2026-06-11 04:41 |
| **Last Seen** | 2026-06-11 04:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:41:26` | `cowrie.session.connect` |
| `2026-06-11 04:41:26` | `cowrie.login.success` |
| `2026-06-11 04:41:27` | `cowrie.session.params` |
| `2026-06-11 04:41:27` | `cowrie.command.input` |
| `2026-06-11 04:41:27` | `cowrie.command.failed` |
| `2026-06-11 04:41:40` | `cowrie.log.closed` |
| `2026-06-11 04:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.232[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.38.232[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b785731a1b

| Field | Detail |
|---|---|
| **Source IP** | `34.38.232[.]106` |
| **First Seen** | 2026-06-11 04:41 |
| **Last Seen** | 2026-06-11 04:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:41:28` | `cowrie.session.connect` |
| `2026-06-11 04:41:28` | `cowrie.login.success` |
| `2026-06-11 04:41:29` | `cowrie.session.params` |
| `2026-06-11 04:41:29` | `cowrie.command.input` |
| `2026-06-11 04:41:40` | `cowrie.log.closed` |
| `2026-06-11 04:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.232[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.38.232[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc98fad43ce

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:46 |
| **Last Seen** | 2026-06-11 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:46:20` | `cowrie.session.connect` |
| `2026-06-11 04:46:20` | `cowrie.client.version` |
| `2026-06-11 04:46:21` | `cowrie.client.kex` |
| `2026-06-11 04:46:22` | `cowrie.login.success` |
| `2026-06-11 04:46:22` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:46:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:46:22` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4055cde23f01

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 04:47 |
| **Last Seen** | 2026-06-11 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:47:18` | `cowrie.session.connect` |
| `2026-06-11 04:47:18` | `cowrie.client.version` |
| `2026-06-11 04:47:18` | `cowrie.client.kex` |
| `2026-06-11 04:47:19` | `cowrie.login.success` |
| `2026-06-11 04:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5cd21308b82

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 04:47 |
| **Last Seen** | 2026-06-11 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:47:18` | `cowrie.session.connect` |
| `2026-06-11 04:47:18` | `cowrie.client.version` |
| `2026-06-11 04:47:19` | `cowrie.client.kex` |
| `2026-06-11 04:47:19` | `cowrie.login.success` |
| `2026-06-11 04:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f271b15f6abc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 04:47 |
| **Last Seen** | 2026-06-11 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:47:21` | `cowrie.session.connect` |
| `2026-06-11 04:47:21` | `cowrie.client.version` |
| `2026-06-11 04:47:21` | `cowrie.client.kex` |
| `2026-06-11 04:47:21` | `cowrie.login.success` |
| `2026-06-11 04:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de20801bc1b5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 04:47 |
| **Last Seen** | 2026-06-11 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:47:21` | `cowrie.session.connect` |
| `2026-06-11 04:47:21` | `cowrie.client.version` |
| `2026-06-11 04:47:22` | `cowrie.client.kex` |
| `2026-06-11 04:47:22` | `cowrie.login.success` |
| `2026-06-11 04:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053d15416e9c

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:51 |
| **Last Seen** | 2026-06-11 04:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:51:25` | `cowrie.session.connect` |
| `2026-06-11 04:51:26` | `cowrie.client.version` |
| `2026-06-11 04:51:26` | `cowrie.client.kex` |
| `2026-06-11 04:51:29` | `cowrie.login.success` |
| `2026-06-11 04:51:29` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:51:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:51:29` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7d52bf2878

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:54 |
| **Last Seen** | 2026-06-11 04:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:54:13` | `cowrie.session.connect` |
| `2026-06-11 04:54:13` | `cowrie.client.version` |
| `2026-06-11 04:54:13` | `cowrie.client.kex` |
| `2026-06-11 04:54:15` | `cowrie.login.success` |
| `2026-06-11 04:54:15` | `cowrie.direct-tcpip.request` |
| `2026-06-11 04:54:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 04:54:16` | `cowrie.direct-tcpip.data` |
| `2026-06-11 04:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.38.232[.]106` | **30** | 2026-06-11 04:40 | 2026-06-11 04:41 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **6** | 2026-06-11 02:55 | 2026-06-11 04:01 | 3m | 0 | `T1592` | 🟢 LOW |
| `20.118.201[.]169` | **2** | 2026-06-11 03:33 | 2026-06-11 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `60.165.124[.]242` | **2** | 2026-06-11 04:13 | 2026-06-11 04:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `206.135.22[.]34` | 1 | 2026-06-11 04:42 | 2026-06-11 04:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-06-11 03:34 | 2026-06-11 03:35 | 71s | 0 | `T1592` | 🟢 LOW |
| `217.146.80[.]108` | 1 | 2026-06-11 03:26 | 2026-06-11 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-11 04:05 | 2026-06-11 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-06-11 04:36 | 2026-06-11 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]61` | 1 | 2026-06-11 03:58 | 2026-06-11 03:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]119` | 1 | 2026-06-11 03:26 | 2026-06-11 03:26 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `206.135.22[.]34` | MX | IENTC S DE RL DE CV | **100** ⚠️ | 9 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 5 |
| `158.178.141[.]210` | AU | Oracle Corporation | **100** ⚠️ | 1 |
| `116.99.174[.]228` | VN | Viettel Group | **100** ⚠️ | 1 |
| `60.165.124[.]242` | CN | CHINANET Gansu province network | **100** ⚠️ | 4 |
| `217.146.80[.]108` | GB | Infrawatch Limited | **100** ⚠️ | 15 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `2.57.121[.]112` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `213.209.159[.]56` | DE | Feo Prest SRL | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 65 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 156 cases |
| Tool 34  | Credential Extractor        | ✅ 37 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (46.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 40 session(s)).

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
_Report time: 2026-06-11T06:05:53Z_

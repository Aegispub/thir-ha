# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-15 |
| **Generated At** | 2026-06-15T12:24:50Z |
| **Shift Time** | 12:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **396** |
| Confirmed Threats | **314** |
| False Positives Filtered | **82** (20.7%) |
| Unique Attacker IPs | **81** |
| Countries of Origin | **21** |
| High Severity Cases | **82** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **314** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **91** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **14** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **56** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `admin` | 10 |
| `GET / HTTP/1.1` | 8 |
| `sol` | 4 |
| `solv` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 14 |
| `123@@@` | 11 |
| `smo@@kkklss` | 11 |
| `admin` | 10 |
| `` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 14 |
| `root` | `123@@@` | 11 |
| `root` | `smo@@kkklss` | 11 |
| `admin` | `admin` | 10 |
| `root` | `` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `10.0.0.73` | 2026-06-15T03:08:07 |
| `root` | `123456` | `80.94.92.178` | 2026-06-15T03:25:43 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-15T03:27:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-15T03:27:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `85.217.149.23` | 2026-06-15T03:33:03 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-15T03:39:00 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-15T03:39:00 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-15T03:39:13 |
| `root` | `1234` | `45.81.252.92` | 2026-06-15T03:42:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `85.217.149.0` | 2026-06-15T03:47:27 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-15T03:59:47 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-15T03:59:47 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-15T03:59:54 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-15T04:02:04 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-15T04:02:06 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-15T04:35:51 |
| `sol` | `sol` | `2.57.122.238` | 2026-06-15T04:42:51 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.235.41.245` | 2026-06-15T04:43:23 |
| `solana` | `solana` | `2.57.122.238` | 2026-06-15T04:45:13 |
| `solv` | `solv` | `2.57.122.238` | 2026-06-15T04:47:37 |
| `solv` | `1234` | `2.57.122.238` | 2026-06-15T04:49:49 |
| `solv` | `123456` | `2.57.122.238` | 2026-06-15T04:52:03 |
| `user` | `12345678` | `50.46.141.125` | 2026-06-15T04:54:19 |
| `solv` | `12345678` | `2.57.122.238` | 2026-06-15T04:54:20 |
| `user` | `12345678~` | `50.46.141.125` | 2026-06-15T04:54:20 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-06-15T04:56:30 |
| `node` | `node` | `2.57.122.238` | 2026-06-15T04:58:50 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-06-15T05:01:11 |
| `validator` | `validator` | `2.57.122.238` | 2026-06-15T05:03:30 |
| `sol` | `sol123` | `2.57.122.238` | 2026-06-15T05:05:49 |
| `sol` | `123` | `2.57.122.238` | 2026-06-15T05:08:03 |
| `sol` | `12345678` | `2.57.122.238` | 2026-06-15T05:10:14 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.246.133` | 2026-06-15T05:13:11 |
| `*1` | `$4` | `34.79.246.133` | 2026-06-15T05:13:20 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6931` | `34.79.246.133` | 2026-06-15T05:13:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.31.205` | 2026-06-15T05:51:43 |
| `*1` | `$4` | `34.38.31.205` | 2026-06-15T05:51:56 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9641` | `34.38.31.205` | 2026-06-15T05:51:58 |
| `admin` | `admin` | `172.96.161.212` | 2026-06-15T06:06:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.104.11.51` | 2026-06-15T06:20:02 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `85.217.149.73` | 2026-06-15T06:34:29 |
| `admin` | `admin` | `132.243.18.154` | 2026-06-15T06:40:57 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-15T06:40:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.14.47.195` | 2026-06-15T06:43:57 |
| `*1` | `$4` | `34.14.47.195` | 2026-06-15T06:44:10 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2384` | `34.14.47.195` | 2026-06-15T06:44:12 |
| `root` | `---fuck_you----` | `101.96.202.189` | 2026-06-15T07:47:46 |
| `root` | `123@@@` | `168.156.171.11` | 2026-06-15T08:15:08 |
| `root` | `LeitboGi0ro` | `168.156.171.11` | 2026-06-15T08:15:08 |
| `root` | `KPfR1UxWYf` | `10.0.0.73` | 2026-06-15T08:19:52 |
| `scan` | `scan` | `107.173.85.94` | 2026-06-15T08:40:51 |
| `root` | `LeitboGi0ro` | `107.173.85.94` | 2026-06-15T09:14:45 |
| `root` | `MoeClub.org` | `107.173.85.94` | 2026-06-15T09:14:46 |
| `admin` | `admin` | `47.253.156.31` | 2026-06-15T10:37:26 |
| `root` | `LeitboGi0ro` | `161.118.237.181` | 2026-06-15T10:47:24 |
| `root` | `123@@@` | `161.118.237.181` | 2026-06-15T10:47:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **396** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| Go SSH scanner | 38 |
| Paramiko (Python) | 35 |
| OpenSSH | 8 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 27 | 3 |
| `16443846184e...` | Generic scanner | 17 | 2 |
| `6372ee695756...` | Modern SSH client | 8 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 6 | 1 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 46 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 27 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 17 | 2 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 8 | 3 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
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
Source IPs: `45.81.252.92`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **81** |
| Unique ASNs | **41** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 10 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS209334` | Modat B.V. | 5 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (77)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f0003c886c91

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]178` |
| **First Seen** | 2026-06-15 03:25 |
| **Last Seen** | 2026-06-15 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /proc/self/maps` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:25:42` | `cowrie.session.connect` |
| `2026-06-15 03:25:42` | `cowrie.client.version` |
| `2026-06-15 03:25:42` | `cowrie.client.kex` |
| `2026-06-15 03:25:43` | `cowrie.login.success` |
| `2026-06-15 03:25:43` | `cowrie.session.params` |
| `2026-06-15 03:25:43` | `cowrie.command.input` |
| `2026-06-15 03:25:44` | `cowrie.log.closed` |
| `2026-06-15 03:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]178` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3fb1d2c716

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 03:27 |
| **Last Seen** | 2026-06-15 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:27:30` | `cowrie.session.connect` |
| `2026-06-15 03:27:30` | `cowrie.client.version` |
| `2026-06-15 03:27:30` | `cowrie.client.kex` |
| `2026-06-15 03:27:31` | `cowrie.login.success` |
| `2026-06-15 03:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e61d08a9bd2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 03:27 |
| **Last Seen** | 2026-06-15 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:27:30` | `cowrie.session.connect` |
| `2026-06-15 03:27:30` | `cowrie.client.version` |
| `2026-06-15 03:27:30` | `cowrie.client.kex` |
| `2026-06-15 03:27:31` | `cowrie.login.success` |
| `2026-06-15 03:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b947b82bc8c

| Field | Detail |
|---|---|
| **Source IP** | `85.217.149[.]23` |
| **First Seen** | 2026-06-15 03:33 |
| **Last Seen** | 2026-06-15 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; ModatScanner/1.2; +hxxps://modat.io/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:33:03` | `cowrie.session.connect` |
| `2026-06-15 03:33:03` | `cowrie.login.success` |
| `2026-06-15 03:33:04` | `cowrie.session.params` |
| `2026-06-15 03:33:04` | `cowrie.command.input` |
| `2026-06-15 03:33:04` | `cowrie.command.input` |
| `2026-06-15 03:33:04` | `cowrie.command.failed` |
| `2026-06-15 03:33:04` | `cowrie.command.input` |
| `2026-06-15 03:33:04` | `cowrie.command.failed` |
| `2026-06-15 03:33:04` | `cowrie.command.input` |
| `2026-06-15 03:33:04` | `cowrie.log.closed` |
| `2026-06-15 03:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.217.149[.]23` to AbuseIPDB if not already reported
- [ ] Block `85.217.149[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7bd4605de1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 03:39 |
| **Last Seen** | 2026-06-15 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:39:00` | `cowrie.session.connect` |
| `2026-06-15 03:39:00` | `cowrie.client.version` |
| `2026-06-15 03:39:00` | `cowrie.client.kex` |
| `2026-06-15 03:39:00` | `cowrie.login.success` |
| `2026-06-15 03:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e0489f9670

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 03:39 |
| **Last Seen** | 2026-06-15 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:39:00` | `cowrie.session.connect` |
| `2026-06-15 03:39:00` | `cowrie.client.version` |
| `2026-06-15 03:39:00` | `cowrie.client.kex` |
| `2026-06-15 03:39:00` | `cowrie.login.success` |
| `2026-06-15 03:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b6a6c6e4a4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 03:39 |
| **Last Seen** | 2026-06-15 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:39:13` | `cowrie.session.connect` |
| `2026-06-15 03:39:13` | `cowrie.client.version` |
| `2026-06-15 03:39:13` | `cowrie.client.kex` |
| `2026-06-15 03:39:13` | `cowrie.login.success` |
| `2026-06-15 03:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e034f69140f6

| Field | Detail |
|---|---|
| **Source IP** | `45.81.252[.]92` |
| **First Seen** | 2026-06-15 03:42 |
| **Last Seen** | 2026-06-15 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:42:47` | `cowrie.session.connect` |
| `2026-06-15 03:42:48` | `cowrie.login.success` |
| `2026-06-15 03:42:48` | `cowrie.session.params` |
| `2026-06-15 03:42:49` | `cowrie.command.input` |
| `2026-06-15 03:42:49` | `cowrie.command.input` |
| `2026-06-15 03:42:50` | `cowrie.command.input` |
| `2026-06-15 03:42:50` | `cowrie.command.input` |
| `2026-06-15 03:42:50` | `cowrie.command.failed` |
| `2026-06-15 03:42:51` | `cowrie.log.closed` |
| `2026-06-15 03:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.81.252[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.81.252[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9fa0e77757

| Field | Detail |
|---|---|
| **Source IP** | `85.217.149[.]0` |
| **First Seen** | 2026-06-15 03:47 |
| **Last Seen** | 2026-06-15 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; ModatScanner/1.2; +hxxps://modat.io/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:47:27` | `cowrie.session.connect` |
| `2026-06-15 03:47:27` | `cowrie.login.success` |
| `2026-06-15 03:47:28` | `cowrie.session.params` |
| `2026-06-15 03:47:28` | `cowrie.command.input` |
| `2026-06-15 03:47:28` | `cowrie.command.input` |
| `2026-06-15 03:47:28` | `cowrie.command.failed` |
| `2026-06-15 03:47:28` | `cowrie.command.input` |
| `2026-06-15 03:47:28` | `cowrie.command.failed` |
| `2026-06-15 03:47:28` | `cowrie.command.input` |
| `2026-06-15 03:47:28` | `cowrie.log.closed` |
| `2026-06-15 03:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.217.149[.]0` to AbuseIPDB if not already reported
- [ ] Block `85.217.149[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea038a0540d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:59:47` | `cowrie.session.connect` |
| `2026-06-15 03:59:47` | `cowrie.client.version` |
| `2026-06-15 03:59:47` | `cowrie.client.kex` |
| `2026-06-15 03:59:47` | `cowrie.login.success` |
| `2026-06-15 03:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2052a321e752

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:59:47` | `cowrie.session.connect` |
| `2026-06-15 03:59:47` | `cowrie.client.version` |
| `2026-06-15 03:59:47` | `cowrie.client.kex` |
| `2026-06-15 03:59:47` | `cowrie.login.success` |
| `2026-06-15 03:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a986be902a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:59:53` | `cowrie.session.connect` |
| `2026-06-15 03:59:53` | `cowrie.client.version` |
| `2026-06-15 03:59:53` | `cowrie.client.kex` |
| `2026-06-15 03:59:54` | `cowrie.login.success` |
| `2026-06-15 03:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe64840742c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:59:54` | `cowrie.session.connect` |
| `2026-06-15 03:59:54` | `cowrie.client.version` |
| `2026-06-15 03:59:54` | `cowrie.client.kex` |
| `2026-06-15 03:59:55` | `cowrie.login.success` |
| `2026-06-15 03:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51b8a444675

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-15 04:02 |
| **Last Seen** | 2026-06-15 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:02:04` | `cowrie.session.connect` |
| `2026-06-15 04:02:04` | `cowrie.client.version` |
| `2026-06-15 04:02:04` | `cowrie.client.kex` |
| `2026-06-15 04:02:04` | `cowrie.login.success` |
| `2026-06-15 04:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4b223f4fc4

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-15 04:02 |
| **Last Seen** | 2026-06-15 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:02:05` | `cowrie.session.connect` |
| `2026-06-15 04:02:05` | `cowrie.client.version` |
| `2026-06-15 04:02:06` | `cowrie.client.kex` |
| `2026-06-15 04:02:06` | `cowrie.login.success` |
| `2026-06-15 04:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2f8b8d6a20

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-15 04:02 |
| **Last Seen** | 2026-06-15 04:04 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:02:27` | `cowrie.session.connect` |
| `2026-06-15 04:02:27` | `cowrie.client.version` |
| `2026-06-15 04:02:27` | `cowrie.client.kex` |
| `2026-06-15 04:02:28` | `cowrie.login.success` |
| `2026-06-15 04:02:29` | `cowrie.session.file_upload` |
| `2026-06-15 04:02:30` | `cowrie.session.params` |
| `2026-06-15 04:02:30` | `cowrie.command.input` |
| `2026-06-15 04:02:30` | `cowrie.command.input` |
| `2026-06-15 04:02:30` | `cowrie.command.input` |
| `2026-06-15 04:02:30` | `cowrie.command.failed` |
| `2026-06-15 04:02:30` | `cowrie.log.closed` |
| `2026-06-15 04:02:30` | `cowrie.session.params` |
| `2026-06-15 04:02:30` | `cowrie.command.input` |
| `2026-06-15 04:02:31` | `cowrie.log.closed` |
| `2026-06-15 04:02:32` | `cowrie.session.params` |
| `2026-06-15 04:02:32` | `cowrie.command.input` |
| `2026-06-15 04:02:32` | `cowrie.log.closed` |
| `2026-06-15 04:02:32` | `cowrie.session.params` |
| `2026-06-15 04:02:32` | `cowrie.command.input` |
| `2026-06-15 04:02:32` | `cowrie.command.failed` |
| `2026-06-15 04:02:32` | `cowrie.command.failed` |
| `2026-06-15 04:03:33` | `cowrie.session.params` |
| `2026-06-15 04:03:33` | `cowrie.command.input` |
| `2026-06-15 04:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966f0bfa9a8c

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-15 04:05 |
| **Last Seen** | 2026-06-15 04:07 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:05:00` | `cowrie.session.connect` |
| `2026-06-15 04:05:00` | `cowrie.client.version` |
| `2026-06-15 04:05:00` | `cowrie.client.kex` |
| `2026-06-15 04:05:00` | `cowrie.login.success` |
| `2026-06-15 04:05:01` | `cowrie.session.file_upload` |
| `2026-06-15 04:05:02` | `cowrie.session.params` |
| `2026-06-15 04:05:02` | `cowrie.command.input` |
| `2026-06-15 04:05:02` | `cowrie.command.input` |
| `2026-06-15 04:05:02` | `cowrie.command.input` |
| `2026-06-15 04:05:02` | `cowrie.command.failed` |
| `2026-06-15 04:05:02` | `cowrie.log.closed` |
| `2026-06-15 04:05:03` | `cowrie.session.params` |
| `2026-06-15 04:05:03` | `cowrie.command.input` |
| `2026-06-15 04:05:03` | `cowrie.log.closed` |
| `2026-06-15 04:05:04` | `cowrie.session.params` |
| `2026-06-15 04:05:04` | `cowrie.command.input` |
| `2026-06-15 04:05:04` | `cowrie.log.closed` |
| `2026-06-15 04:05:05` | `cowrie.session.params` |
| `2026-06-15 04:05:05` | `cowrie.command.input` |
| `2026-06-15 04:05:05` | `cowrie.command.failed` |
| `2026-06-15 04:05:05` | `cowrie.command.failed` |
| `2026-06-15 04:06:06` | `cowrie.session.params` |
| `2026-06-15 04:06:06` | `cowrie.command.input` |
| `2026-06-15 04:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a37179a63c5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-15 04:35 |
| **Last Seen** | 2026-06-15 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:35:50` | `cowrie.session.connect` |
| `2026-06-15 04:35:50` | `cowrie.client.version` |
| `2026-06-15 04:35:50` | `cowrie.client.kex` |
| `2026-06-15 04:35:51` | `cowrie.login.success` |
| `2026-06-15 04:35:51` | `cowrie.direct-tcpip.request` |
| `2026-06-15 04:35:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-15 04:35:51` | `cowrie.direct-tcpip.data` |
| `2026-06-15 04:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-573eeb2956e2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-15 04:35 |
| **Last Seen** | 2026-06-15 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:35:51` | `cowrie.session.connect` |
| `2026-06-15 04:35:51` | `cowrie.client.version` |
| `2026-06-15 04:35:51` | `cowrie.client.kex` |
| `2026-06-15 04:35:51` | `cowrie.login.success` |
| `2026-06-15 04:35:51` | `cowrie.direct-tcpip.request` |
| `2026-06-15 04:35:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-15 04:35:52` | `cowrie.direct-tcpip.data` |
| `2026-06-15 04:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1511c793b53

| Field | Detail |
|---|---|
| **Source IP** | `45.79.211[.]97` |
| **First Seen** | 2026-06-15 04:38 |
| **Last Seen** | 2026-06-15 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:38:31` | `cowrie.session.connect` |
| `2026-06-15 04:38:31` | `cowrie.login.success` |
| `2026-06-15 04:38:31` | `cowrie.session.params` |
| `2026-06-15 04:38:33` | `cowrie.log.closed` |
| `2026-06-15 04:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.211[.]97` to AbuseIPDB if not already reported
- [ ] Block `45.79.211[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7e361a0f8b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:42 |
| **Last Seen** | 2026-06-15 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:42:51` | `cowrie.session.connect` |
| `2026-06-15 04:42:51` | `cowrie.client.version` |
| `2026-06-15 04:42:51` | `cowrie.client.kex` |
| `2026-06-15 04:42:51` | `cowrie.login.success` |
| `2026-06-15 04:42:52` | `cowrie.session.params` |
| `2026-06-15 04:42:52` | `cowrie.command.input` |
| `2026-06-15 04:42:52` | `cowrie.log.closed` |
| `2026-06-15 04:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431c7759d68e

| Field | Detail |
|---|---|
| **Source IP** | `172.235.41[.]245` |
| **First Seen** | 2026-06-15 04:43 |
| **Last Seen** | 2026-06-15 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:43:23` | `cowrie.session.connect` |
| `2026-06-15 04:43:23` | `cowrie.login.success` |
| `2026-06-15 04:43:23` | `cowrie.session.params` |
| `2026-06-15 04:43:23` | `cowrie.command.input` |
| `2026-06-15 04:43:23` | `cowrie.command.input` |
| `2026-06-15 04:43:23` | `cowrie.command.failed` |
| `2026-06-15 04:43:23` | `cowrie.command.input` |
| `2026-06-15 04:43:23` | `cowrie.command.failed` |
| `2026-06-15 04:43:23` | `cowrie.command.input` |
| `2026-06-15 04:43:24` | `cowrie.log.closed` |
| `2026-06-15 04:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.235.41[.]245` to AbuseIPDB if not already reported
- [ ] Block `172.235.41[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952b44c9b046

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:45 |
| **Last Seen** | 2026-06-15 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:45:12` | `cowrie.session.connect` |
| `2026-06-15 04:45:12` | `cowrie.client.version` |
| `2026-06-15 04:45:12` | `cowrie.client.kex` |
| `2026-06-15 04:45:13` | `cowrie.login.success` |
| `2026-06-15 04:45:13` | `cowrie.session.params` |
| `2026-06-15 04:45:13` | `cowrie.command.input` |
| `2026-06-15 04:45:14` | `cowrie.log.closed` |
| `2026-06-15 04:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e161f377f97b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:47 |
| **Last Seen** | 2026-06-15 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:47:37` | `cowrie.session.connect` |
| `2026-06-15 04:47:37` | `cowrie.client.version` |
| `2026-06-15 04:47:37` | `cowrie.client.kex` |
| `2026-06-15 04:47:37` | `cowrie.login.success` |
| `2026-06-15 04:47:38` | `cowrie.session.params` |
| `2026-06-15 04:47:38` | `cowrie.command.input` |
| `2026-06-15 04:47:38` | `cowrie.log.closed` |
| `2026-06-15 04:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e7d46a0c21

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:49 |
| **Last Seen** | 2026-06-15 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:49:48` | `cowrie.session.connect` |
| `2026-06-15 04:49:48` | `cowrie.client.version` |
| `2026-06-15 04:49:48` | `cowrie.client.kex` |
| `2026-06-15 04:49:49` | `cowrie.login.success` |
| `2026-06-15 04:49:49` | `cowrie.session.params` |
| `2026-06-15 04:49:49` | `cowrie.command.input` |
| `2026-06-15 04:49:50` | `cowrie.log.closed` |
| `2026-06-15 04:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1c0a242d4a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:52 |
| **Last Seen** | 2026-06-15 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:52:03` | `cowrie.session.connect` |
| `2026-06-15 04:52:03` | `cowrie.client.version` |
| `2026-06-15 04:52:03` | `cowrie.client.kex` |
| `2026-06-15 04:52:03` | `cowrie.login.success` |
| `2026-06-15 04:52:04` | `cowrie.session.params` |
| `2026-06-15 04:52:04` | `cowrie.command.input` |
| `2026-06-15 04:52:04` | `cowrie.log.closed` |
| `2026-06-15 04:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9520da9b5d9b

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-15 04:54 |
| **Last Seen** | 2026-06-15 04:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:54:19` | `cowrie.session.connect` |
| `2026-06-15 04:54:19` | `cowrie.client.version` |
| `2026-06-15 04:54:19` | `cowrie.client.kex` |
| `2026-06-15 04:54:19` | `cowrie.login.success` |
| `2026-06-15 04:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e28273c3c990

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:54 |
| **Last Seen** | 2026-06-15 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:54:19` | `cowrie.session.connect` |
| `2026-06-15 04:54:19` | `cowrie.client.version` |
| `2026-06-15 04:54:19` | `cowrie.client.kex` |
| `2026-06-15 04:54:20` | `cowrie.login.success` |
| `2026-06-15 04:54:20` | `cowrie.session.params` |
| `2026-06-15 04:54:20` | `cowrie.command.input` |
| `2026-06-15 04:54:21` | `cowrie.log.closed` |
| `2026-06-15 04:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb2b2bb9743

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-15 04:54 |
| **Last Seen** | 2026-06-15 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:54:19` | `cowrie.session.connect` |
| `2026-06-15 04:54:19` | `cowrie.client.version` |
| `2026-06-15 04:54:19` | `cowrie.client.kex` |
| `2026-06-15 04:54:20` | `cowrie.login.success` |
| `2026-06-15 04:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d8a1d6ad05

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:56 |
| **Last Seen** | 2026-06-15 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:56:30` | `cowrie.session.connect` |
| `2026-06-15 04:56:30` | `cowrie.client.version` |
| `2026-06-15 04:56:30` | `cowrie.client.kex` |
| `2026-06-15 04:56:30` | `cowrie.login.success` |
| `2026-06-15 04:56:31` | `cowrie.session.params` |
| `2026-06-15 04:56:31` | `cowrie.command.input` |
| `2026-06-15 04:56:31` | `cowrie.log.closed` |
| `2026-06-15 04:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297ab58b6bb2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 04:58 |
| **Last Seen** | 2026-06-15 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:58:50` | `cowrie.session.connect` |
| `2026-06-15 04:58:50` | `cowrie.client.version` |
| `2026-06-15 04:58:50` | `cowrie.client.kex` |
| `2026-06-15 04:58:50` | `cowrie.login.success` |
| `2026-06-15 04:58:51` | `cowrie.session.params` |
| `2026-06-15 04:58:51` | `cowrie.command.input` |
| `2026-06-15 04:58:51` | `cowrie.log.closed` |
| `2026-06-15 04:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6833d6c9f6fb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 05:01 |
| **Last Seen** | 2026-06-15 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:01:11` | `cowrie.session.connect` |
| `2026-06-15 05:01:11` | `cowrie.client.version` |
| `2026-06-15 05:01:11` | `cowrie.client.kex` |
| `2026-06-15 05:01:11` | `cowrie.login.success` |
| `2026-06-15 05:01:12` | `cowrie.session.params` |
| `2026-06-15 05:01:12` | `cowrie.command.input` |
| `2026-06-15 05:01:12` | `cowrie.log.closed` |
| `2026-06-15 05:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e0ed4f0157

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 05:03 |
| **Last Seen** | 2026-06-15 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:03:29` | `cowrie.session.connect` |
| `2026-06-15 05:03:29` | `cowrie.client.version` |
| `2026-06-15 05:03:29` | `cowrie.client.kex` |
| `2026-06-15 05:03:30` | `cowrie.login.success` |
| `2026-06-15 05:03:30` | `cowrie.session.params` |
| `2026-06-15 05:03:30` | `cowrie.command.input` |
| `2026-06-15 05:03:31` | `cowrie.log.closed` |
| `2026-06-15 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd55c81b1ad

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 05:05 |
| **Last Seen** | 2026-06-15 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:05:49` | `cowrie.session.connect` |
| `2026-06-15 05:05:49` | `cowrie.client.version` |
| `2026-06-15 05:05:49` | `cowrie.client.kex` |
| `2026-06-15 05:05:49` | `cowrie.login.success` |
| `2026-06-15 05:05:50` | `cowrie.session.params` |
| `2026-06-15 05:05:50` | `cowrie.command.input` |
| `2026-06-15 05:05:50` | `cowrie.log.closed` |
| `2026-06-15 05:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8441e9e5c32a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 05:08 |
| **Last Seen** | 2026-06-15 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:08:02` | `cowrie.session.connect` |
| `2026-06-15 05:08:02` | `cowrie.client.version` |
| `2026-06-15 05:08:02` | `cowrie.client.kex` |
| `2026-06-15 05:08:03` | `cowrie.login.success` |
| `2026-06-15 05:08:03` | `cowrie.session.params` |
| `2026-06-15 05:08:03` | `cowrie.command.input` |
| `2026-06-15 05:08:04` | `cowrie.log.closed` |
| `2026-06-15 05:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c306c2422101

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-15 05:10 |
| **Last Seen** | 2026-06-15 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:10:14` | `cowrie.session.connect` |
| `2026-06-15 05:10:14` | `cowrie.client.version` |
| `2026-06-15 05:10:14` | `cowrie.client.kex` |
| `2026-06-15 05:10:14` | `cowrie.login.success` |
| `2026-06-15 05:10:15` | `cowrie.session.params` |
| `2026-06-15 05:10:15` | `cowrie.command.input` |
| `2026-06-15 05:10:15` | `cowrie.log.closed` |
| `2026-06-15 05:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1fd0110b56

| Field | Detail |
|---|---|
| **Source IP** | `34.79.246[.]133` |
| **First Seen** | 2026-06-15 05:13 |
| **Last Seen** | 2026-06-15 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:13:11` | `cowrie.session.connect` |
| `2026-06-15 05:13:11` | `cowrie.login.success` |
| `2026-06-15 05:13:12` | `cowrie.session.params` |
| `2026-06-15 05:13:12` | `cowrie.command.input` |
| `2026-06-15 05:13:12` | `cowrie.command.input` |
| `2026-06-15 05:13:12` | `cowrie.command.failed` |
| `2026-06-15 05:13:12` | `cowrie.command.input` |
| `2026-06-15 05:13:12` | `cowrie.log.closed` |
| `2026-06-15 05:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.246[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.79.246[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4142508797

| Field | Detail |
|---|---|
| **Source IP** | `34.79.246[.]133` |
| **First Seen** | 2026-06-15 05:13 |
| **Last Seen** | 2026-06-15 05:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:13:20` | `cowrie.session.connect` |
| `2026-06-15 05:13:20` | `cowrie.login.success` |
| `2026-06-15 05:13:20` | `cowrie.session.params` |
| `2026-06-15 05:13:20` | `cowrie.command.input` |
| `2026-06-15 05:13:20` | `cowrie.command.failed` |
| `2026-06-15 05:13:35` | `cowrie.log.closed` |
| `2026-06-15 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.246[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.79.246[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00965618fe4

| Field | Detail |
|---|---|
| **Source IP** | `34.79.246[.]133` |
| **First Seen** | 2026-06-15 05:13 |
| **Last Seen** | 2026-06-15 05:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:13:21` | `cowrie.session.connect` |
| `2026-06-15 05:13:21` | `cowrie.login.success` |
| `2026-06-15 05:13:22` | `cowrie.session.params` |
| `2026-06-15 05:13:22` | `cowrie.command.input` |
| `2026-06-15 05:13:35` | `cowrie.log.closed` |
| `2026-06-15 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.246[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.79.246[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d3e4c06c99

| Field | Detail |
|---|---|
| **Source IP** | `34.38.31[.]205` |
| **First Seen** | 2026-06-15 05:51 |
| **Last Seen** | 2026-06-15 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:51:43` | `cowrie.session.connect` |
| `2026-06-15 05:51:43` | `cowrie.login.success` |
| `2026-06-15 05:51:43` | `cowrie.session.params` |
| `2026-06-15 05:51:43` | `cowrie.command.input` |
| `2026-06-15 05:51:43` | `cowrie.command.input` |
| `2026-06-15 05:51:43` | `cowrie.command.failed` |
| `2026-06-15 05:51:43` | `cowrie.command.input` |
| `2026-06-15 05:51:43` | `cowrie.log.closed` |
| `2026-06-15 05:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.31[.]205` to AbuseIPDB if not already reported
- [ ] Block `34.38.31[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53bea9e7b59e

| Field | Detail |
|---|---|
| **Source IP** | `34.38.31[.]205` |
| **First Seen** | 2026-06-15 05:51 |
| **Last Seen** | 2026-06-15 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:51:56` | `cowrie.session.connect` |
| `2026-06-15 05:51:56` | `cowrie.login.success` |
| `2026-06-15 05:51:57` | `cowrie.session.params` |
| `2026-06-15 05:51:57` | `cowrie.command.input` |
| `2026-06-15 05:51:57` | `cowrie.command.failed` |
| `2026-06-15 05:51:57` | `cowrie.log.closed` |
| `2026-06-15 05:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.31[.]205` to AbuseIPDB if not already reported
- [ ] Block `34.38.31[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54519453b09

| Field | Detail |
|---|---|
| **Source IP** | `34.38.31[.]205` |
| **First Seen** | 2026-06-15 05:51 |
| **Last Seen** | 2026-06-15 05:52 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:51:58` | `cowrie.session.connect` |
| `2026-06-15 05:51:58` | `cowrie.login.success` |
| `2026-06-15 05:51:59` | `cowrie.session.params` |
| `2026-06-15 05:51:59` | `cowrie.command.input` |
| `2026-06-15 05:52:12` | `cowrie.log.closed` |
| `2026-06-15 05:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.31[.]205` to AbuseIPDB if not already reported
- [ ] Block `34.38.31[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9a4ec4d3f80

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 06:01 |
| **Last Seen** | 2026-06-15 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:01:29` | `cowrie.session.connect` |
| `2026-06-15 06:01:29` | `cowrie.client.version` |
| `2026-06-15 06:01:29` | `cowrie.client.kex` |
| `2026-06-15 06:01:29` | `cowrie.login.success` |
| `2026-06-15 06:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91897cb6961a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 06:01 |
| **Last Seen** | 2026-06-15 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:01:30` | `cowrie.session.connect` |
| `2026-06-15 06:01:30` | `cowrie.client.version` |
| `2026-06-15 06:01:30` | `cowrie.client.kex` |
| `2026-06-15 06:01:30` | `cowrie.login.success` |
| `2026-06-15 06:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638891fc243e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 06:01 |
| **Last Seen** | 2026-06-15 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:01:38` | `cowrie.session.connect` |
| `2026-06-15 06:01:38` | `cowrie.client.version` |
| `2026-06-15 06:01:38` | `cowrie.client.kex` |
| `2026-06-15 06:01:39` | `cowrie.login.success` |
| `2026-06-15 06:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb897521888d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 06:01 |
| **Last Seen** | 2026-06-15 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:01:39` | `cowrie.session.connect` |
| `2026-06-15 06:01:39` | `cowrie.client.version` |
| `2026-06-15 06:01:39` | `cowrie.client.kex` |
| `2026-06-15 06:01:39` | `cowrie.login.success` |
| `2026-06-15 06:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5b9bbd4066

| Field | Detail |
|---|---|
| **Source IP** | `172.96.161[.]212` |
| **First Seen** | 2026-06-15 06:05 |
| **Last Seen** | 2026-06-15 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:05:08` | `cowrie.session.connect` |
| `2026-06-15 06:05:08` | `cowrie.telnet.option` |
| `2026-06-15 06:05:08` | `cowrie.telnet.option` |
| `2026-06-15 06:06:08` | `cowrie.login.success` |
| `2026-06-15 06:06:09` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `172.96.161[.]212` to AbuseIPDB if not already reported
- [ ] Block `172.96.161[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac98fc77de6

| Field | Detail |
|---|---|
| **Source IP** | `172.104.11[.]51` |
| **First Seen** | 2026-06-15 06:20 |
| **Last Seen** | 2026-06-15 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:20:02` | `cowrie.session.connect` |
| `2026-06-15 06:20:02` | `cowrie.login.success` |
| `2026-06-15 06:20:02` | `cowrie.session.params` |
| `2026-06-15 06:20:02` | `cowrie.command.input` |
| `2026-06-15 06:20:02` | `cowrie.command.input` |
| `2026-06-15 06:20:02` | `cowrie.command.failed` |
| `2026-06-15 06:20:02` | `cowrie.command.input` |
| `2026-06-15 06:20:02` | `cowrie.command.failed` |
| `2026-06-15 06:20:02` | `cowrie.command.input` |
| `2026-06-15 06:20:03` | `cowrie.log.closed` |
| `2026-06-15 06:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.104.11[.]51` to AbuseIPDB if not already reported
- [ ] Block `172.104.11[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1be5bebd71c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 06:32 |
| **Last Seen** | 2026-06-15 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:32:06` | `cowrie.session.connect` |
| `2026-06-15 06:32:06` | `cowrie.client.version` |
| `2026-06-15 06:32:06` | `cowrie.client.kex` |
| `2026-06-15 06:32:06` | `cowrie.login.success` |
| `2026-06-15 06:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7215b0c75faa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 06:32 |
| **Last Seen** | 2026-06-15 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:32:07` | `cowrie.session.connect` |
| `2026-06-15 06:32:07` | `cowrie.client.version` |
| `2026-06-15 06:32:07` | `cowrie.client.kex` |
| `2026-06-15 06:32:07` | `cowrie.login.success` |
| `2026-06-15 06:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ddb4fe5610

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 06:32 |
| **Last Seen** | 2026-06-15 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:32:11` | `cowrie.session.connect` |
| `2026-06-15 06:32:11` | `cowrie.client.version` |
| `2026-06-15 06:32:11` | `cowrie.client.kex` |
| `2026-06-15 06:32:12` | `cowrie.login.success` |
| `2026-06-15 06:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243abdf95ab6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 06:32 |
| **Last Seen** | 2026-06-15 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:32:12` | `cowrie.session.connect` |
| `2026-06-15 06:32:12` | `cowrie.client.version` |
| `2026-06-15 06:32:12` | `cowrie.client.kex` |
| `2026-06-15 06:32:13` | `cowrie.login.success` |
| `2026-06-15 06:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b13e3eaca87

| Field | Detail |
|---|---|
| **Source IP** | `85.217.149[.]73` |
| **First Seen** | 2026-06-15 06:34 |
| **Last Seen** | 2026-06-15 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; ModatScanner/1.2; +hxxps://modat.io/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:34:29` | `cowrie.session.connect` |
| `2026-06-15 06:34:29` | `cowrie.login.success` |
| `2026-06-15 06:34:29` | `cowrie.session.params` |
| `2026-06-15 06:34:29` | `cowrie.command.input` |
| `2026-06-15 06:34:29` | `cowrie.command.input` |
| `2026-06-15 06:34:29` | `cowrie.command.failed` |
| `2026-06-15 06:34:29` | `cowrie.command.input` |
| `2026-06-15 06:34:29` | `cowrie.command.failed` |
| `2026-06-15 06:34:29` | `cowrie.command.input` |
| `2026-06-15 06:34:29` | `cowrie.log.closed` |
| `2026-06-15 06:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.217.149[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.217.149[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee99b1259fd

| Field | Detail |
|---|---|
| **Source IP** | `132.243.18[.]154` |
| **First Seen** | 2026-06-15 06:40 |
| **Last Seen** | 2026-06-15 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:40:57` | `cowrie.session.connect` |
| `2026-06-15 06:40:57` | `cowrie.client.version` |
| `2026-06-15 06:40:57` | `cowrie.client.kex` |
| `2026-06-15 06:40:57` | `cowrie.login.success` |
| `2026-06-15 06:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.243.18[.]154` to AbuseIPDB if not already reported
- [ ] Block `132.243.18[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea340962a04c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-15 06:40 |
| **Last Seen** | 2026-06-15 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:40:58` | `cowrie.session.connect` |
| `2026-06-15 06:40:58` | `cowrie.client.version` |
| `2026-06-15 06:40:58` | `cowrie.client.kex` |
| `2026-06-15 06:40:58` | `cowrie.login.success` |
| `2026-06-15 06:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257ebb4a7ba7

| Field | Detail |
|---|---|
| **Source IP** | `34.14.47[.]195` |
| **First Seen** | 2026-06-15 06:43 |
| **Last Seen** | 2026-06-15 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:43:57` | `cowrie.session.connect` |
| `2026-06-15 06:43:57` | `cowrie.login.success` |
| `2026-06-15 06:43:57` | `cowrie.session.params` |
| `2026-06-15 06:43:57` | `cowrie.command.input` |
| `2026-06-15 06:43:57` | `cowrie.command.input` |
| `2026-06-15 06:43:57` | `cowrie.command.failed` |
| `2026-06-15 06:43:57` | `cowrie.command.input` |
| `2026-06-15 06:43:57` | `cowrie.log.closed` |
| `2026-06-15 06:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.47[.]195` to AbuseIPDB if not already reported
- [ ] Block `34.14.47[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edee82c8534

| Field | Detail |
|---|---|
| **Source IP** | `34.14.47[.]195` |
| **First Seen** | 2026-06-15 06:44 |
| **Last Seen** | 2026-06-15 06:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:44:10` | `cowrie.session.connect` |
| `2026-06-15 06:44:10` | `cowrie.login.success` |
| `2026-06-15 06:44:11` | `cowrie.session.params` |
| `2026-06-15 06:44:11` | `cowrie.command.input` |
| `2026-06-15 06:44:11` | `cowrie.command.failed` |
| `2026-06-15 06:44:26` | `cowrie.log.closed` |
| `2026-06-15 06:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.47[.]195` to AbuseIPDB if not already reported
- [ ] Block `34.14.47[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dab73d674fc

| Field | Detail |
|---|---|
| **Source IP** | `34.14.47[.]195` |
| **First Seen** | 2026-06-15 06:44 |
| **Last Seen** | 2026-06-15 06:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:44:12` | `cowrie.session.connect` |
| `2026-06-15 06:44:12` | `cowrie.login.success` |
| `2026-06-15 06:44:12` | `cowrie.session.params` |
| `2026-06-15 06:44:12` | `cowrie.command.input` |
| `2026-06-15 06:44:26` | `cowrie.log.closed` |
| `2026-06-15 06:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.47[.]195` to AbuseIPDB if not already reported
- [ ] Block `34.14.47[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ba47162443

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]189` |
| **First Seen** | 2026-06-15 07:47 |
| **Last Seen** | 2026-06-15 07:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:47:45` | `cowrie.session.connect` |
| `2026-06-15 07:47:45` | `cowrie.client.version` |
| `2026-06-15 07:47:45` | `cowrie.client.kex` |
| `2026-06-15 07:47:46` | `cowrie.login.success` |
| `2026-06-15 07:47:47` | `cowrie.session.params` |
| `2026-06-15 07:47:47` | `cowrie.command.input` |
| `2026-06-15 07:47:47` | `cowrie.log.closed` |
| `2026-06-15 07:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]189` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f479aad64c0c

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-15 08:15 |
| **Last Seen** | 2026-06-15 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:15:07` | `cowrie.session.connect` |
| `2026-06-15 08:15:07` | `cowrie.client.version` |
| `2026-06-15 08:15:07` | `cowrie.client.kex` |
| `2026-06-15 08:15:08` | `cowrie.login.success` |
| `2026-06-15 08:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9210e2a9f998

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-15 08:15 |
| **Last Seen** | 2026-06-15 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:15:07` | `cowrie.session.connect` |
| `2026-06-15 08:15:07` | `cowrie.client.version` |
| `2026-06-15 08:15:07` | `cowrie.client.kex` |
| `2026-06-15 08:15:08` | `cowrie.login.success` |
| `2026-06-15 08:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a7c1e0e828

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-15 08:40 |
| **Last Seen** | 2026-06-15 08:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:40:51` | `cowrie.session.connect` |
| `2026-06-15 08:40:51` | `cowrie.client.version` |
| `2026-06-15 08:40:51` | `cowrie.client.kex` |
| `2026-06-15 08:40:51` | `cowrie.login.success` |
| `2026-06-15 08:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ba69305f2e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 08:45 |
| **Last Seen** | 2026-06-15 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:45:15` | `cowrie.session.connect` |
| `2026-06-15 08:45:15` | `cowrie.client.version` |
| `2026-06-15 08:45:15` | `cowrie.client.kex` |
| `2026-06-15 08:45:16` | `cowrie.login.success` |
| `2026-06-15 08:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ffdbccc695d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 08:45 |
| **Last Seen** | 2026-06-15 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:45:15` | `cowrie.session.connect` |
| `2026-06-15 08:45:15` | `cowrie.client.version` |
| `2026-06-15 08:45:15` | `cowrie.client.kex` |
| `2026-06-15 08:45:16` | `cowrie.login.success` |
| `2026-06-15 08:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13bce5b8c95

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:13` | `cowrie.session.connect` |
| `2026-06-15 09:14:13` | `cowrie.client.version` |
| `2026-06-15 09:14:13` | `cowrie.client.kex` |
| `2026-06-15 09:14:14` | `cowrie.login.success` |
| `2026-06-15 09:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa977660d131

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:13` | `cowrie.session.connect` |
| `2026-06-15 09:14:13` | `cowrie.client.version` |
| `2026-06-15 09:14:14` | `cowrie.client.kex` |
| `2026-06-15 09:14:14` | `cowrie.login.success` |
| `2026-06-15 09:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-523fa8380b04

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:22` | `cowrie.session.connect` |
| `2026-06-15 09:14:22` | `cowrie.client.version` |
| `2026-06-15 09:14:22` | `cowrie.client.kex` |
| `2026-06-15 09:14:22` | `cowrie.login.success` |
| `2026-06-15 09:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1622c9578a83

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:23` | `cowrie.session.connect` |
| `2026-06-15 09:14:23` | `cowrie.client.version` |
| `2026-06-15 09:14:23` | `cowrie.client.kex` |
| `2026-06-15 09:14:23` | `cowrie.login.success` |
| `2026-06-15 09:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87712c1b48a

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:45` | `cowrie.session.connect` |
| `2026-06-15 09:14:45` | `cowrie.client.version` |
| `2026-06-15 09:14:45` | `cowrie.client.kex` |
| `2026-06-15 09:14:45` | `cowrie.login.success` |
| `2026-06-15 09:14:46` | `cowrie.session.params` |
| `2026-06-15 09:14:46` | `cowrie.command.input` |
| `2026-06-15 09:14:46` | `cowrie.log.closed` |
| `2026-06-15 09:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac424d3f30bc

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-15 09:14 |
| **Last Seen** | 2026-06-15 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:14:46` | `cowrie.session.connect` |
| `2026-06-15 09:14:46` | `cowrie.client.version` |
| `2026-06-15 09:14:46` | `cowrie.client.kex` |
| `2026-06-15 09:14:46` | `cowrie.login.success` |
| `2026-06-15 09:14:47` | `cowrie.session.params` |
| `2026-06-15 09:14:47` | `cowrie.command.input` |
| `2026-06-15 09:14:47` | `cowrie.log.closed` |
| `2026-06-15 09:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f847a6268b1c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 09:36 |
| **Last Seen** | 2026-06-15 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:36:13` | `cowrie.session.connect` |
| `2026-06-15 09:36:13` | `cowrie.client.version` |
| `2026-06-15 09:36:13` | `cowrie.client.kex` |
| `2026-06-15 09:36:13` | `cowrie.login.success` |
| `2026-06-15 09:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce78df3e06b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 09:36 |
| **Last Seen** | 2026-06-15 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:36:16` | `cowrie.session.connect` |
| `2026-06-15 09:36:16` | `cowrie.client.version` |
| `2026-06-15 09:36:16` | `cowrie.client.kex` |
| `2026-06-15 09:36:16` | `cowrie.login.success` |
| `2026-06-15 09:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146f16630cb7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 09:36 |
| **Last Seen** | 2026-06-15 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:36:21` | `cowrie.session.connect` |
| `2026-06-15 09:36:21` | `cowrie.client.version` |
| `2026-06-15 09:36:21` | `cowrie.client.kex` |
| `2026-06-15 09:36:21` | `cowrie.login.success` |
| `2026-06-15 09:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8831a4cc80d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 09:36 |
| **Last Seen** | 2026-06-15 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 09:36:21` | `cowrie.session.connect` |
| `2026-06-15 09:36:21` | `cowrie.client.version` |
| `2026-06-15 09:36:21` | `cowrie.client.kex` |
| `2026-06-15 09:36:21` | `cowrie.login.success` |
| `2026-06-15 09:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b795dfc85701

| Field | Detail |
|---|---|
| **Source IP** | `47.253.156[.]31` |
| **First Seen** | 2026-06-15 10:36 |
| **Last Seen** | 2026-06-15 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:36:26` | `cowrie.session.connect` |
| `2026-06-15 10:36:26` | `cowrie.telnet.option` |
| `2026-06-15 10:36:26` | `cowrie.telnet.option` |
| `2026-06-15 10:37:26` | `cowrie.login.success` |
| `2026-06-15 10:37:27` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.156[.]31` to AbuseIPDB if not already reported
- [ ] Block `47.253.156[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2ecae58110

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-15 10:47 |
| **Last Seen** | 2026-06-15 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:47:23` | `cowrie.session.connect` |
| `2026-06-15 10:47:23` | `cowrie.client.version` |
| `2026-06-15 10:47:23` | `cowrie.client.kex` |
| `2026-06-15 10:47:24` | `cowrie.login.success` |
| `2026-06-15 10:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be75b3f1d88c

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-15 10:47 |
| **Last Seen** | 2026-06-15 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:47:26` | `cowrie.session.connect` |
| `2026-06-15 10:47:26` | `cowrie.client.version` |
| `2026-06-15 10:47:26` | `cowrie.client.kex` |
| `2026-06-15 10:47:27` | `cowrie.login.success` |
| `2026-06-15 10:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **57** | 2026-06-15 03:11 | 2026-06-15 10:52 | 46m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.47[.]195` | **30** | 2026-06-15 06:43 | 2026-06-15 06:44 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.31[.]205` | **30** | 2026-06-15 05:51 | 2026-06-15 05:51 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.246[.]133` | **30** | 2026-06-15 05:13 | 2026-06-15 05:13 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **24** | 2026-06-15 03:16 | 2026-06-15 10:39 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **6** | 2026-06-15 03:14 | 2026-06-15 09:10 | 1m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `216.70.97[.]74` | **6** | 2026-06-15 09:33 | 2026-06-15 10:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **3** | 2026-06-15 08:36 | 2026-06-15 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.173.85[.]94` | **2** | 2026-06-15 08:40 | 2026-06-15 09:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.53[.]174` | **2** | 2026-06-15 03:27 | 2026-06-15 03:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.29.196[.]194` | **2** | 2026-06-15 07:33 | 2026-06-15 07:35 | 2m | 0 | `T1592` | 🟢 LOW |
| `18.222.106[.]88` | **2** | 2026-06-15 08:47 | 2026-06-15 08:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-15 04:20 | 2026-06-15 04:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | **2** | 2026-06-15 03:50 | 2026-06-15 03:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.81.252[.]92` | **2** | 2026-06-15 03:42 | 2026-06-15 03:42 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `47.74.213[.]140` | **2** | 2026-06-15 08:34 | 2026-06-15 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | **2** | 2026-06-15 07:26 | 2026-06-15 07:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]189` | 1 | 2026-06-15 07:47 | 2026-06-15 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.115.126[.]6` | 1 | 2026-06-15 06:31 | 2026-06-15 06:31 | 18s | 0 | `T1592` | 🟢 LOW |
| `109.63.118[.]196` | 1 | 2026-06-15 09:36 | 2026-06-15 09:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `122.246.222[.]217` | 1 | 2026-06-15 04:42 | 2026-06-15 04:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `134.209.93[.]206` | 1 | 2026-06-15 09:41 | 2026-06-15 09:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-15 03:43 | 2026-06-15 03:44 | 45s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-15 06:39 | 2026-06-15 06:40 | 73s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]51` | 1 | 2026-06-15 06:20 | 2026-06-15 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-15 08:35 | 2026-06-15 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]245` | 1 | 2026-06-15 04:43 | 2026-06-15 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-06-15 05:28 | 2026-06-15 05:28 | 9s | 0 | `T1592` | 🟢 LOW |
| `197.44.114[.]250` | 1 | 2026-06-15 07:28 | 2026-06-15 07:29 | 15s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-06-15 04:40 | 2026-06-15 04:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.98.214[.]120` | 1 | 2026-06-15 09:52 | 2026-06-15 09:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-15 07:04 | 2026-06-15 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-15 10:03 | 2026-06-15 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-15 06:39 | 2026-06-15 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-06-15 04:38 | 2026-06-15 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-06-15 08:35 | 2026-06-15 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.16.66[.]255` | 1 | 2026-06-15 08:45 | 2026-06-15 08:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.158.44[.]17` | 1 | 2026-06-15 08:02 | 2026-06-15 08:02 | 37s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-15 04:03 | 2026-06-15 04:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-15 07:47 | 2026-06-15 07:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-15 10:04 | 2026-06-15 10:04 | 54s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]94` | 1 | 2026-06-15 08:16 | 2026-06-15 08:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-06-15 06:46 | 2026-06-15 06:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]6` | 1 | 2026-06-15 04:11 | 2026-06-15 04:11 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | 1 | 2026-06-15 04:40 | 2026-06-15 04:40 | 41s | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | 1 | 2026-06-15 07:45 | 2026-06-15 07:46 | 42s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]23` | 1 | 2026-06-15 08:08 | 2026-06-15 08:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-15 07:37 | 2026-06-15 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]30` | 1 | 2026-06-15 09:54 | 2026-06-15 09:55 | 28s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]63` | 1 | 2026-06-15 09:40 | 2026-06-15 09:41 | 28s | 0 | `T1592` | 🟢 LOW |

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
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `172.235.41[.]245` | US | Linode | **100** ⚠️ | 9 |
| `107.173.85[.]94` | US | HostPapa | **100** ⚠️ | 39 |
| `34.79.246[.]133` | BE | Google LLC | **100** ⚠️ | 0 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `134.209.93[.]206` | NL | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `34.38.31[.]205` | BE | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 137 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 82 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |

---

## 🔕 False Positive Summary (82 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 50 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 396 cases |
| Tool 34  | Credential Extractor        | ✅ 91 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 81 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 82 filtered (20.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 77 priority case(s) shown individually · 50 recon entry/entries in table (17 group(s) consolidating 204 session(s)).

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
_Report time: 2026-06-15T12:24:50Z_

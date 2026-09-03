# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-03 |
| **Generated At** | 2026-09-03T22:24:54Z |
| **Shift Time** | 22:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **93** |
| Confirmed Threats | **80** |
| False Positives Filtered | **13** (14.0%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **18** |
| High Severity Cases | **56** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **61** |
| Unique Credential Pairs | **57** |
| Unique Usernames | **5** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `admin` | 20 |
| `user` | 6 |
| `support` | 3 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 3 |
| `support` | 3 |
| `admin` | 3 |
| `matteo` | 2 |
| `111111` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 3 |
| `admin` | `123456` | 2 |
| `root` | `admin` | 2 |
| `root` | `Hung@2026` | 1 |
| `admin` | `matteo` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123456` | `217.60.255.130` | 2026-09-03T18:56:37 |
| `root` | `Hung@2026` | `217.60.255.130` | 2026-09-03T18:57:23 |
| `admin` | `matteo` | `217.60.255.130` | 2026-09-03T19:06:09 |
| `root` | `Huy@1234` | `217.60.255.130` | 2026-09-03T19:08:24 |
| `support` | `support` | `176.53.159.196` | 2026-09-03T19:13:26 |
| `root` | `111111` | `80.94.92.55` | 2026-09-03T19:14:04 |
| `admin` | `default` | `217.60.255.130` | 2026-09-03T19:15:53 |
| `root` | `123123` | `80.94.92.55` | 2026-09-03T19:16:12 |
| `root` | `1234` | `80.94.92.55` | 2026-09-03T19:18:14 |
| `root` | `Roger@123` | `217.60.255.130` | 2026-09-03T19:19:19 |
| `root` | `12345` | `80.94.92.55` | 2026-09-03T19:20:18 |
| `root` | `12345678` | `80.94.92.55` | 2026-09-03T19:24:25 |
| `postgres` | `P@ssword` | `217.60.255.130` | 2026-09-03T19:25:35 |
| `root` | `123456789` | `80.94.92.55` | 2026-09-03T19:26:23 |
| `root` | `Password1` | `80.94.92.55` | 2026-09-03T19:28:31 |
| `root` | `Khoa@123` | `217.60.255.130` | 2026-09-03T19:30:24 |
| `root` | `admin` | `80.94.92.55` | 2026-09-03T19:30:37 |
| `root` | `admin123` | `80.94.92.55` | 2026-09-03T19:32:48 |
| `root` | `default` | `80.94.92.55` | 2026-09-03T19:34:58 |
| `admin` | `root123!` | `217.60.255.130` | 2026-09-03T19:35:27 |
| `support` | `support` | `10.0.0.73` | 2026-09-03T19:36:51 |
| `root` | `letmein` | `80.94.92.55` | 2026-09-03T19:37:10 |
| `root` | `passw0rd` | `80.94.92.55` | 2026-09-03T19:39:19 |
| `root` | `matteo` | `217.60.255.130` | 2026-09-03T19:41:21 |
| `root` | `password` | `80.94.92.55` | 2026-09-03T19:41:31 |
| `root` | `qwerty` | `80.94.92.55` | 2026-09-03T19:43:34 |
| `user` | `net@2025` | `217.60.255.130` | 2026-09-03T19:44:54 |
| `root` | `system` | `80.94.92.55` | 2026-09-03T19:47:44 |
| `root` | `toor` | `80.94.92.55` | 2026-09-03T19:49:47 |
| `admin` | `111111` | `80.94.92.55` | 2026-09-03T19:51:51 |
| `root` | `Khiem123@` | `217.60.255.130` | 2026-09-03T19:52:18 |
| `admin` | `123123` | `80.94.92.55` | 2026-09-03T19:53:57 |
| `admin` | `Test!234` | `217.60.255.130` | 2026-09-03T19:54:41 |
| `admin` | `1234` | `80.94.92.55` | 2026-09-03T19:56:03 |
| `admin` | `12345` | `80.94.92.55` | 2026-09-03T19:58:13 |
| `admin` | `123456` | `80.94.92.55` | 2026-09-03T20:00:25 |
| `admin` | `12345678` | `80.94.92.55` | 2026-09-03T20:02:27 |
| `root` | `Computer@2023` | `217.60.255.130` | 2026-09-03T20:03:25 |
| `admin` | `123456789` | `80.94.92.55` | 2026-09-03T20:04:23 |
| `user` | `Server@12` | `217.60.255.130` | 2026-09-03T20:04:32 |
| `admin` | `Administrator` | `80.94.92.55` | 2026-09-03T20:06:16 |
| `admin` | `access` | `80.94.92.55` | 2026-09-03T20:08:14 |
| `admin` | `admin` | `80.94.92.55` | 2026-09-03T20:10:09 |
| `admin` | `admin123` | `80.94.92.55` | 2026-09-03T20:12:12 |
| `user` | `123qwe` | `217.60.255.130` | 2026-09-03T20:14:08 |
| `admin` | `adminadmin` | `80.94.92.55` | 2026-09-03T20:14:09 |
| `root` | `adminadmin` | `217.60.255.130` | 2026-09-03T20:14:18 |
| `admin` | `letmein` | `80.94.92.55` | 2026-09-03T20:16:11 |
| `admin` | `passw0rd` | `80.94.92.55` | 2026-09-03T20:18:24 |
| `user` | `admin12345` | `217.60.255.130` | 2026-09-03T20:23:46 |
| `root` | `ht` | `217.60.255.130` | 2026-09-03T20:25:21 |
| `user` | `Admin123456` | `217.60.255.130` | 2026-09-03T20:33:25 |
| `root` | `francesca` | `217.60.255.130` | 2026-09-03T20:36:00 |
| `admin` | `Ll2024` | `217.60.255.130` | 2026-09-03T20:42:55 |
| `root` | `enterprise` | `217.60.255.130` | 2026-09-03T20:46:55 |
| `user` | `A@1234567` | `217.60.255.130` | 2026-09-03T20:52:32 |
| `root` | `admin` | `82.153.138.57` | 2026-09-03T20:54:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **93** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 33 |
| libssh | 25 |
| Unknown | 2 |
| PuTTY | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 32 | 1 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 32 | 1 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `d00d43d15d59...` | OpenSSH | 1 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 30 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `80.94.92.55`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **18** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 7 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS7155` | ViaSat,Inc. | 1 | HIGH |
| `AS211101` | Nasteka Maksim Viktorovich | 1 | LOW |
| `AS267869` | CABLE Y TELECOMUNICACIONES DE COLOMBIA S.A.S (CABLETELCO) | 1 | MEDIUM |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (56)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7b28c74c9868

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:56 |
| **Last Seen** | 2026-09-03 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:56:35` | `cowrie.session.connect` |
| `2026-09-03 18:56:35` | `cowrie.client.version` |
| `2026-09-03 18:56:35` | `cowrie.client.kex` |
| `2026-09-03 18:56:37` | `cowrie.login.success` |
| `2026-09-03 18:56:37` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:56:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:56:37` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15aa676d16bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:57 |
| **Last Seen** | 2026-09-03 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:57:22` | `cowrie.session.connect` |
| `2026-09-03 18:57:22` | `cowrie.client.version` |
| `2026-09-03 18:57:22` | `cowrie.client.kex` |
| `2026-09-03 18:57:23` | `cowrie.login.success` |
| `2026-09-03 18:57:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:57:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:57:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c70bae429ce

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:06 |
| **Last Seen** | 2026-09-03 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:06:08` | `cowrie.session.connect` |
| `2026-09-03 19:06:08` | `cowrie.client.version` |
| `2026-09-03 19:06:08` | `cowrie.client.kex` |
| `2026-09-03 19:06:09` | `cowrie.login.success` |
| `2026-09-03 19:06:09` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:06:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:06:10` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10015bddf8d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:08 |
| **Last Seen** | 2026-09-03 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:08:23` | `cowrie.session.connect` |
| `2026-09-03 19:08:23` | `cowrie.client.version` |
| `2026-09-03 19:08:23` | `cowrie.client.kex` |
| `2026-09-03 19:08:24` | `cowrie.login.success` |
| `2026-09-03 19:08:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:08:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:08:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14be67d84dd6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 19:13 |
| **Last Seen** | 2026-09-03 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:13:25` | `cowrie.session.connect` |
| `2026-09-03 19:13:25` | `cowrie.client.version` |
| `2026-09-03 19:13:26` | `cowrie.client.kex` |
| `2026-09-03 19:13:26` | `cowrie.login.success` |
| `2026-09-03 19:13:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:13:26` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b34de38cc29a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:14 |
| **Last Seen** | 2026-09-03 19:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:14:00` | `cowrie.session.connect` |
| `2026-09-03 19:14:01` | `cowrie.client.version` |
| `2026-09-03 19:14:01` | `cowrie.client.kex` |
| `2026-09-03 19:14:04` | `cowrie.login.success` |
| `2026-09-03 19:14:06` | `cowrie.session.params` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.success` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.command.input` |
| `2026-09-03 19:14:06` | `cowrie.log.closed` |
| `2026-09-03 19:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e610d90bf2bd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:15 |
| **Last Seen** | 2026-09-03 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:15:52` | `cowrie.session.connect` |
| `2026-09-03 19:15:52` | `cowrie.client.version` |
| `2026-09-03 19:15:52` | `cowrie.client.kex` |
| `2026-09-03 19:15:53` | `cowrie.login.success` |
| `2026-09-03 19:15:53` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:15:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:15:53` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5fe3f44f21

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:16 |
| **Last Seen** | 2026-09-03 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:16:06` | `cowrie.session.connect` |
| `2026-09-03 19:16:07` | `cowrie.client.version` |
| `2026-09-03 19:16:07` | `cowrie.client.kex` |
| `2026-09-03 19:16:12` | `cowrie.login.success` |
| `2026-09-03 19:16:13` | `cowrie.session.params` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.success` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:13` | `cowrie.command.input` |
| `2026-09-03 19:16:14` | `cowrie.log.closed` |
| `2026-09-03 19:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c237d5008d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:18 |
| **Last Seen** | 2026-09-03 19:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:18:11` | `cowrie.session.connect` |
| `2026-09-03 19:18:11` | `cowrie.client.version` |
| `2026-09-03 19:18:11` | `cowrie.client.kex` |
| `2026-09-03 19:18:14` | `cowrie.login.success` |
| `2026-09-03 19:18:16` | `cowrie.session.params` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.success` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.command.input` |
| `2026-09-03 19:18:16` | `cowrie.log.closed` |
| `2026-09-03 19:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fef66af8ca9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:19 |
| **Last Seen** | 2026-09-03 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:19:18` | `cowrie.session.connect` |
| `2026-09-03 19:19:18` | `cowrie.client.version` |
| `2026-09-03 19:19:18` | `cowrie.client.kex` |
| `2026-09-03 19:19:19` | `cowrie.login.success` |
| `2026-09-03 19:19:20` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:19:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:19:20` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc6fcbabffc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:20 |
| **Last Seen** | 2026-09-03 19:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:20:16` | `cowrie.session.connect` |
| `2026-09-03 19:20:16` | `cowrie.client.version` |
| `2026-09-03 19:20:16` | `cowrie.client.kex` |
| `2026-09-03 19:20:18` | `cowrie.login.success` |
| `2026-09-03 19:20:20` | `cowrie.session.params` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.success` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:20` | `cowrie.command.input` |
| `2026-09-03 19:20:21` | `cowrie.log.closed` |
| `2026-09-03 19:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4c5bd2e0a6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:24 |
| **Last Seen** | 2026-09-03 19:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:24:22` | `cowrie.session.connect` |
| `2026-09-03 19:24:23` | `cowrie.client.version` |
| `2026-09-03 19:24:23` | `cowrie.client.kex` |
| `2026-09-03 19:24:25` | `cowrie.login.success` |
| `2026-09-03 19:24:27` | `cowrie.session.params` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.success` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.command.input` |
| `2026-09-03 19:24:27` | `cowrie.log.closed` |
| `2026-09-03 19:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eaeb32e8fd8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:25 |
| **Last Seen** | 2026-09-03 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:25:34` | `cowrie.session.connect` |
| `2026-09-03 19:25:34` | `cowrie.client.version` |
| `2026-09-03 19:25:34` | `cowrie.client.kex` |
| `2026-09-03 19:25:35` | `cowrie.login.success` |
| `2026-09-03 19:25:35` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:25:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:25:35` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080ef86c368a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:26 |
| **Last Seen** | 2026-09-03 19:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:26:21` | `cowrie.session.connect` |
| `2026-09-03 19:26:21` | `cowrie.client.version` |
| `2026-09-03 19:26:21` | `cowrie.client.kex` |
| `2026-09-03 19:26:23` | `cowrie.login.success` |
| `2026-09-03 19:26:25` | `cowrie.session.params` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.success` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.command.input` |
| `2026-09-03 19:26:25` | `cowrie.log.closed` |
| `2026-09-03 19:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a6518d9294

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:28 |
| **Last Seen** | 2026-09-03 19:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:28:29` | `cowrie.session.connect` |
| `2026-09-03 19:28:29` | `cowrie.client.version` |
| `2026-09-03 19:28:29` | `cowrie.client.kex` |
| `2026-09-03 19:28:31` | `cowrie.login.success` |
| `2026-09-03 19:28:32` | `cowrie.session.params` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.success` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:32` | `cowrie.command.input` |
| `2026-09-03 19:28:33` | `cowrie.log.closed` |
| `2026-09-03 19:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f49f51ae5bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:30 |
| **Last Seen** | 2026-09-03 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:30:23` | `cowrie.session.connect` |
| `2026-09-03 19:30:23` | `cowrie.client.version` |
| `2026-09-03 19:30:23` | `cowrie.client.kex` |
| `2026-09-03 19:30:24` | `cowrie.login.success` |
| `2026-09-03 19:30:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:30:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:30:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ce017edae1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:30 |
| **Last Seen** | 2026-09-03 19:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:30:35` | `cowrie.session.connect` |
| `2026-09-03 19:30:35` | `cowrie.client.version` |
| `2026-09-03 19:30:35` | `cowrie.client.kex` |
| `2026-09-03 19:30:37` | `cowrie.login.success` |
| `2026-09-03 19:30:39` | `cowrie.session.params` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.success` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.command.input` |
| `2026-09-03 19:30:39` | `cowrie.log.closed` |
| `2026-09-03 19:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7cc6a67c86

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:32 |
| **Last Seen** | 2026-09-03 19:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:32:46` | `cowrie.session.connect` |
| `2026-09-03 19:32:46` | `cowrie.client.version` |
| `2026-09-03 19:32:46` | `cowrie.client.kex` |
| `2026-09-03 19:32:48` | `cowrie.login.success` |
| `2026-09-03 19:32:49` | `cowrie.session.params` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.success` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:49` | `cowrie.command.input` |
| `2026-09-03 19:32:50` | `cowrie.log.closed` |
| `2026-09-03 19:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61889f92254f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:34 |
| **Last Seen** | 2026-09-03 19:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:34:56` | `cowrie.session.connect` |
| `2026-09-03 19:34:56` | `cowrie.client.version` |
| `2026-09-03 19:34:56` | `cowrie.client.kex` |
| `2026-09-03 19:34:58` | `cowrie.login.success` |
| `2026-09-03 19:34:59` | `cowrie.session.params` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.success` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.command.input` |
| `2026-09-03 19:34:59` | `cowrie.log.closed` |
| `2026-09-03 19:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1131dff8fef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:35 |
| **Last Seen** | 2026-09-03 19:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:35:25` | `cowrie.session.connect` |
| `2026-09-03 19:35:25` | `cowrie.client.version` |
| `2026-09-03 19:35:25` | `cowrie.client.kex` |
| `2026-09-03 19:35:27` | `cowrie.login.success` |
| `2026-09-03 19:35:27` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:35:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:35:27` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6afdcbeefe

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:37 |
| **Last Seen** | 2026-09-03 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:37:08` | `cowrie.session.connect` |
| `2026-09-03 19:37:09` | `cowrie.client.version` |
| `2026-09-03 19:37:09` | `cowrie.client.kex` |
| `2026-09-03 19:37:10` | `cowrie.login.success` |
| `2026-09-03 19:37:12` | `cowrie.session.params` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.success` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.command.input` |
| `2026-09-03 19:37:12` | `cowrie.log.closed` |
| `2026-09-03 19:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2625080d3f78

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:39 |
| **Last Seen** | 2026-09-03 19:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:39:17` | `cowrie.session.connect` |
| `2026-09-03 19:39:17` | `cowrie.client.version` |
| `2026-09-03 19:39:17` | `cowrie.client.kex` |
| `2026-09-03 19:39:19` | `cowrie.login.success` |
| `2026-09-03 19:39:20` | `cowrie.session.params` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.success` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:20` | `cowrie.command.input` |
| `2026-09-03 19:39:21` | `cowrie.log.closed` |
| `2026-09-03 19:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b028d970c7c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:41 |
| **Last Seen** | 2026-09-03 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:41:20` | `cowrie.session.connect` |
| `2026-09-03 19:41:20` | `cowrie.client.version` |
| `2026-09-03 19:41:20` | `cowrie.client.kex` |
| `2026-09-03 19:41:21` | `cowrie.login.success` |
| `2026-09-03 19:41:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:41:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:41:21` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c70b2ab5770

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:41 |
| **Last Seen** | 2026-09-03 19:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:41:28` | `cowrie.session.connect` |
| `2026-09-03 19:41:29` | `cowrie.client.version` |
| `2026-09-03 19:41:29` | `cowrie.client.kex` |
| `2026-09-03 19:41:31` | `cowrie.login.success` |
| `2026-09-03 19:41:33` | `cowrie.session.params` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.success` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.command.input` |
| `2026-09-03 19:41:33` | `cowrie.log.closed` |
| `2026-09-03 19:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61482f8c4270

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:43 |
| **Last Seen** | 2026-09-03 19:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:43:32` | `cowrie.session.connect` |
| `2026-09-03 19:43:33` | `cowrie.client.version` |
| `2026-09-03 19:43:33` | `cowrie.client.kex` |
| `2026-09-03 19:43:34` | `cowrie.login.success` |
| `2026-09-03 19:43:35` | `cowrie.session.params` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.success` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.command.input` |
| `2026-09-03 19:43:35` | `cowrie.log.closed` |
| `2026-09-03 19:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2754b59fdf9e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:44 |
| **Last Seen** | 2026-09-03 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:44:53` | `cowrie.session.connect` |
| `2026-09-03 19:44:53` | `cowrie.client.version` |
| `2026-09-03 19:44:53` | `cowrie.client.kex` |
| `2026-09-03 19:44:54` | `cowrie.login.success` |
| `2026-09-03 19:44:55` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:44:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:44:55` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15d317ed802

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:47 |
| **Last Seen** | 2026-09-03 19:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:47:43` | `cowrie.session.connect` |
| `2026-09-03 19:47:43` | `cowrie.client.version` |
| `2026-09-03 19:47:43` | `cowrie.client.kex` |
| `2026-09-03 19:47:44` | `cowrie.login.success` |
| `2026-09-03 19:47:46` | `cowrie.session.params` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.success` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.command.input` |
| `2026-09-03 19:47:46` | `cowrie.log.closed` |
| `2026-09-03 19:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814aac584bd0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:49 |
| **Last Seen** | 2026-09-03 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:49:44` | `cowrie.session.connect` |
| `2026-09-03 19:49:45` | `cowrie.client.version` |
| `2026-09-03 19:49:45` | `cowrie.client.kex` |
| `2026-09-03 19:49:47` | `cowrie.login.success` |
| `2026-09-03 19:49:48` | `cowrie.session.params` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.success` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.command.input` |
| `2026-09-03 19:49:48` | `cowrie.log.closed` |
| `2026-09-03 19:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe57454d1db

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:51 |
| **Last Seen** | 2026-09-03 19:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:51:49` | `cowrie.session.connect` |
| `2026-09-03 19:51:49` | `cowrie.client.version` |
| `2026-09-03 19:51:49` | `cowrie.client.kex` |
| `2026-09-03 19:51:51` | `cowrie.login.success` |
| `2026-09-03 19:51:52` | `cowrie.session.params` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.success` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:52` | `cowrie.command.input` |
| `2026-09-03 19:51:53` | `cowrie.log.closed` |
| `2026-09-03 19:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fb0a5cc025

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:52 |
| **Last Seen** | 2026-09-03 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:52:16` | `cowrie.session.connect` |
| `2026-09-03 19:52:16` | `cowrie.client.version` |
| `2026-09-03 19:52:16` | `cowrie.client.kex` |
| `2026-09-03 19:52:18` | `cowrie.login.success` |
| `2026-09-03 19:52:18` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:52:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:52:18` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5318aa8c2523

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:53 |
| **Last Seen** | 2026-09-03 19:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:53:56` | `cowrie.session.connect` |
| `2026-09-03 19:53:56` | `cowrie.client.version` |
| `2026-09-03 19:53:56` | `cowrie.client.kex` |
| `2026-09-03 19:53:57` | `cowrie.login.success` |
| `2026-09-03 19:53:59` | `cowrie.session.params` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.success` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.command.input` |
| `2026-09-03 19:53:59` | `cowrie.log.closed` |
| `2026-09-03 19:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c767e431ac1c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 19:54 |
| **Last Seen** | 2026-09-03 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:54:39` | `cowrie.session.connect` |
| `2026-09-03 19:54:39` | `cowrie.client.version` |
| `2026-09-03 19:54:40` | `cowrie.client.kex` |
| `2026-09-03 19:54:41` | `cowrie.login.success` |
| `2026-09-03 19:54:41` | `cowrie.direct-tcpip.request` |
| `2026-09-03 19:54:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 19:54:41` | `cowrie.direct-tcpip.data` |
| `2026-09-03 19:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647ca789cd15

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:56 |
| **Last Seen** | 2026-09-03 19:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:56:02` | `cowrie.session.connect` |
| `2026-09-03 19:56:02` | `cowrie.client.version` |
| `2026-09-03 19:56:02` | `cowrie.client.kex` |
| `2026-09-03 19:56:03` | `cowrie.login.success` |
| `2026-09-03 19:56:04` | `cowrie.session.params` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.success` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.command.input` |
| `2026-09-03 19:56:04` | `cowrie.log.closed` |
| `2026-09-03 19:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-303781cc6064

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 19:58 |
| **Last Seen** | 2026-09-03 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 19:58:12` | `cowrie.session.connect` |
| `2026-09-03 19:58:12` | `cowrie.client.version` |
| `2026-09-03 19:58:12` | `cowrie.client.kex` |
| `2026-09-03 19:58:13` | `cowrie.login.success` |
| `2026-09-03 19:58:14` | `cowrie.session.params` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.success` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:14` | `cowrie.command.input` |
| `2026-09-03 19:58:15` | `cowrie.log.closed` |
| `2026-09-03 19:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fcc3c9a6f11

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:00 |
| **Last Seen** | 2026-09-03 20:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:00:24` | `cowrie.session.connect` |
| `2026-09-03 20:00:24` | `cowrie.client.version` |
| `2026-09-03 20:00:24` | `cowrie.client.kex` |
| `2026-09-03 20:00:25` | `cowrie.login.success` |
| `2026-09-03 20:00:26` | `cowrie.session.params` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.success` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.command.input` |
| `2026-09-03 20:00:26` | `cowrie.log.closed` |
| `2026-09-03 20:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f94c52af4a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:02 |
| **Last Seen** | 2026-09-03 20:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:02:25` | `cowrie.session.connect` |
| `2026-09-03 20:02:25` | `cowrie.client.version` |
| `2026-09-03 20:02:25` | `cowrie.client.kex` |
| `2026-09-03 20:02:27` | `cowrie.login.success` |
| `2026-09-03 20:02:28` | `cowrie.session.params` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.success` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:28` | `cowrie.command.input` |
| `2026-09-03 20:02:29` | `cowrie.log.closed` |
| `2026-09-03 20:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8087d75c611

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:03 |
| **Last Seen** | 2026-09-03 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:03:24` | `cowrie.session.connect` |
| `2026-09-03 20:03:24` | `cowrie.client.version` |
| `2026-09-03 20:03:24` | `cowrie.client.kex` |
| `2026-09-03 20:03:25` | `cowrie.login.success` |
| `2026-09-03 20:03:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:03:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:03:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c472a4fad1a3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:04 |
| **Last Seen** | 2026-09-03 20:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:04:21` | `cowrie.session.connect` |
| `2026-09-03 20:04:22` | `cowrie.client.version` |
| `2026-09-03 20:04:22` | `cowrie.client.kex` |
| `2026-09-03 20:04:23` | `cowrie.login.success` |
| `2026-09-03 20:04:24` | `cowrie.session.params` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.success` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.command.input` |
| `2026-09-03 20:04:24` | `cowrie.log.closed` |
| `2026-09-03 20:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a82dfaa0e3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:04 |
| **Last Seen** | 2026-09-03 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:04:31` | `cowrie.session.connect` |
| `2026-09-03 20:04:31` | `cowrie.client.version` |
| `2026-09-03 20:04:31` | `cowrie.client.kex` |
| `2026-09-03 20:04:32` | `cowrie.login.success` |
| `2026-09-03 20:04:33` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:04:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:04:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f4ccf6dc71

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:06 |
| **Last Seen** | 2026-09-03 20:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:06:15` | `cowrie.session.connect` |
| `2026-09-03 20:06:15` | `cowrie.client.version` |
| `2026-09-03 20:06:15` | `cowrie.client.kex` |
| `2026-09-03 20:06:16` | `cowrie.login.success` |
| `2026-09-03 20:06:18` | `cowrie.session.params` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.success` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:18` | `cowrie.command.input` |
| `2026-09-03 20:06:19` | `cowrie.log.closed` |
| `2026-09-03 20:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339a1058e8af

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:08 |
| **Last Seen** | 2026-09-03 20:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:08:12` | `cowrie.session.connect` |
| `2026-09-03 20:08:12` | `cowrie.client.version` |
| `2026-09-03 20:08:12` | `cowrie.client.kex` |
| `2026-09-03 20:08:14` | `cowrie.login.success` |
| `2026-09-03 20:08:16` | `cowrie.session.params` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.success` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.command.input` |
| `2026-09-03 20:08:16` | `cowrie.log.closed` |
| `2026-09-03 20:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553e46878589

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:10 |
| **Last Seen** | 2026-09-03 20:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:10:07` | `cowrie.session.connect` |
| `2026-09-03 20:10:07` | `cowrie.client.version` |
| `2026-09-03 20:10:07` | `cowrie.client.kex` |
| `2026-09-03 20:10:09` | `cowrie.login.success` |
| `2026-09-03 20:10:10` | `cowrie.session.params` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.success` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.command.input` |
| `2026-09-03 20:10:10` | `cowrie.log.closed` |
| `2026-09-03 20:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0067739c52f0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:12 |
| **Last Seen** | 2026-09-03 20:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:12:10` | `cowrie.session.connect` |
| `2026-09-03 20:12:10` | `cowrie.client.version` |
| `2026-09-03 20:12:10` | `cowrie.client.kex` |
| `2026-09-03 20:12:12` | `cowrie.login.success` |
| `2026-09-03 20:12:13` | `cowrie.session.params` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.success` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.command.input` |
| `2026-09-03 20:12:13` | `cowrie.log.closed` |
| `2026-09-03 20:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f00ab71c74

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:14 |
| **Last Seen** | 2026-09-03 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:14:07` | `cowrie.session.connect` |
| `2026-09-03 20:14:07` | `cowrie.client.version` |
| `2026-09-03 20:14:07` | `cowrie.client.kex` |
| `2026-09-03 20:14:08` | `cowrie.login.success` |
| `2026-09-03 20:14:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:14:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:14:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d842d62a64

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:14 |
| **Last Seen** | 2026-09-03 20:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:14:08` | `cowrie.session.connect` |
| `2026-09-03 20:14:08` | `cowrie.client.version` |
| `2026-09-03 20:14:08` | `cowrie.client.kex` |
| `2026-09-03 20:14:09` | `cowrie.login.success` |
| `2026-09-03 20:14:11` | `cowrie.session.params` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.success` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.command.input` |
| `2026-09-03 20:14:11` | `cowrie.log.closed` |
| `2026-09-03 20:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-948c749808de

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:14 |
| **Last Seen** | 2026-09-03 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:14:17` | `cowrie.session.connect` |
| `2026-09-03 20:14:17` | `cowrie.client.version` |
| `2026-09-03 20:14:17` | `cowrie.client.kex` |
| `2026-09-03 20:14:18` | `cowrie.login.success` |
| `2026-09-03 20:14:18` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:14:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:14:19` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd0d45a22ab

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:16 |
| **Last Seen** | 2026-09-03 20:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:16:10` | `cowrie.session.connect` |
| `2026-09-03 20:16:11` | `cowrie.client.version` |
| `2026-09-03 20:16:11` | `cowrie.client.kex` |
| `2026-09-03 20:16:11` | `cowrie.login.success` |
| `2026-09-03 20:16:13` | `cowrie.session.params` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.success` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.command.input` |
| `2026-09-03 20:16:13` | `cowrie.log.closed` |
| `2026-09-03 20:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b799ad5bbf3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-09-03 20:18 |
| **Last Seen** | 2026-09-03 20:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:18:23` | `cowrie.session.connect` |
| `2026-09-03 20:18:23` | `cowrie.client.version` |
| `2026-09-03 20:18:24` | `cowrie.client.kex` |
| `2026-09-03 20:18:24` | `cowrie.login.success` |
| `2026-09-03 20:18:25` | `cowrie.session.params` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.success` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.command.input` |
| `2026-09-03 20:18:25` | `cowrie.log.closed` |
| `2026-09-03 20:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4e12671018

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:23 |
| **Last Seen** | 2026-09-03 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:23:45` | `cowrie.session.connect` |
| `2026-09-03 20:23:45` | `cowrie.client.version` |
| `2026-09-03 20:23:45` | `cowrie.client.kex` |
| `2026-09-03 20:23:46` | `cowrie.login.success` |
| `2026-09-03 20:23:46` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:23:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:23:46` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d907d3261d17

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:25 |
| **Last Seen** | 2026-09-03 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:25:20` | `cowrie.session.connect` |
| `2026-09-03 20:25:20` | `cowrie.client.version` |
| `2026-09-03 20:25:20` | `cowrie.client.kex` |
| `2026-09-03 20:25:21` | `cowrie.login.success` |
| `2026-09-03 20:25:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:25:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:25:22` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199fd6cbbf5d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:33 |
| **Last Seen** | 2026-09-03 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:33:24` | `cowrie.session.connect` |
| `2026-09-03 20:33:24` | `cowrie.client.version` |
| `2026-09-03 20:33:24` | `cowrie.client.kex` |
| `2026-09-03 20:33:25` | `cowrie.login.success` |
| `2026-09-03 20:33:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:33:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:33:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7db28c1f20d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:35 |
| **Last Seen** | 2026-09-03 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:35:59` | `cowrie.session.connect` |
| `2026-09-03 20:35:59` | `cowrie.client.version` |
| `2026-09-03 20:35:59` | `cowrie.client.kex` |
| `2026-09-03 20:36:00` | `cowrie.login.success` |
| `2026-09-03 20:36:01` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:36:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:36:01` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b604f0f28d06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:42 |
| **Last Seen** | 2026-09-03 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:42:54` | `cowrie.session.connect` |
| `2026-09-03 20:42:54` | `cowrie.client.version` |
| `2026-09-03 20:42:54` | `cowrie.client.kex` |
| `2026-09-03 20:42:55` | `cowrie.login.success` |
| `2026-09-03 20:42:55` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:42:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:42:55` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a5a0c23054

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:46 |
| **Last Seen** | 2026-09-03 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:46:54` | `cowrie.session.connect` |
| `2026-09-03 20:46:54` | `cowrie.client.version` |
| `2026-09-03 20:46:54` | `cowrie.client.kex` |
| `2026-09-03 20:46:55` | `cowrie.login.success` |
| `2026-09-03 20:46:55` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:46:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:46:55` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414ea454a33b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 20:52 |
| **Last Seen** | 2026-09-03 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:52:30` | `cowrie.session.connect` |
| `2026-09-03 20:52:30` | `cowrie.client.version` |
| `2026-09-03 20:52:31` | `cowrie.client.kex` |
| `2026-09-03 20:52:32` | `cowrie.login.success` |
| `2026-09-03 20:52:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:52:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 20:52:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10b82958243

| Field | Detail |
|---|---|
| **Source IP** | `82.153.138[.]57` |
| **First Seen** | 2026-09-03 20:54 |
| **Last Seen** | 2026-09-03 20:54 |
| **Session Duration** | 23s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 20:54:21` | `cowrie.session.connect` |
| `2026-09-03 20:54:21` | `cowrie.client.version` |
| `2026-09-03 20:54:22` | `cowrie.client.kex` |
| `2026-09-03 20:54:23` | `cowrie.client.fingerprint` |
| `2026-09-03 20:54:23` | `cowrie.login.failed` |
| `2026-09-03 20:54:23` | `cowrie.login.success` |
| `2026-09-03 20:54:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 20:54:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-03 20:54:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 20:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.153.138[.]57` to AbuseIPDB if not already reported
- [ ] Block `82.153.138[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.253.118[.]132` | **3** | 2026-09-03 20:47 | 2026-09-03 20:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **3** | 2026-09-03 19:10 | 2026-09-03 19:45 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.242.20[.]181` | **2** | 2026-09-03 19:09 | 2026-09-03 19:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `219.104.130[.]252` | **2** | 2026-09-03 19:24 | 2026-09-03 19:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.107.125[.]120` | **2** | 2026-09-03 19:28 | 2026-09-03 19:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-09-03 19:04 | 2026-09-03 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-09-03 20:38 | 2026-09-03 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.94.47[.]95` | 1 | 2026-09-03 19:46 | 2026-09-03 19:46 | 14s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-03 19:22 | 2026-09-03 19:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-09-03 19:03 | 2026-09-03 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-09-03 19:44 | 2026-09-03 19:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-03 19:43 | 2026-09-03 19:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `5.44.170[.]92` | 1 | 2026-09-03 19:57 | 2026-09-03 19:57 | 14s | 0 | `T1592` | 🟢 LOW |
| `76.94.141[.]3` | 1 | 2026-09-03 20:54 | 2026-09-03 20:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `79.117.224[.]178` | 1 | 2026-09-03 20:03 | 2026-09-03 20:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.134.124[.]8` | 1 | 2026-09-03 20:37 | 2026-09-03 20:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]192` | 1 | 2026-09-03 20:10 | 2026-09-03 20:10 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `45.148.10[.]157` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `172.242.20[.]181` | US | ViaSat,Inc. | **100** ⚠️ | 0 |
| `79.117.224[.]178` | ES | Digi Spain Telecom | **100** ⚠️ | 2 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `47.107.125[.]120` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 6 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 56 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 30 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 30 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 93 cases |
| Tool 34  | Credential Extractor        | ✅ 61 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (14.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 56 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 12 session(s)).

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
_Report time: 2026-09-03T22:24:54Z_

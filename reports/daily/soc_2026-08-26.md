# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-26 |
| **Generated At** | 2026-08-26T16:50:32Z |
| **Shift Time** | 16:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **87** |
| Confirmed Threats | **74** |
| False Positives Filtered | **13** (14.9%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **19** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **2** HIGH · **21** MED · 21 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **38** |
| Unique Usernames | **8** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **37** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `ubuntu` | 11 |
| `admin` | 3 |
| `support` | 2 |
| `installer` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `admin` | 4 |
| `support` | 2 |
| `Hamid1234` | 1 |
| `qwe123!@#` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `admin` | `admin` | 3 |
| `support` | `support` | 2 |
| `ubuntu` | `Hamid1234` | 1 |
| `root` | `qwe123!@#` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Hamid1234` | `217.60.255.130` | 2026-08-26T13:03:04 |
| `root` | `qwe123!@#` | `217.60.255.130` | 2026-08-26T13:03:08 |
| `admin` | `admin` | `116.110.156.150` | 2026-08-26T13:08:00 |
| `root` | `admin` | `116.110.156.150` | 2026-08-26T13:11:01 |
| `ubuntu` | `Amir@1234` | `217.60.255.130` | 2026-08-26T13:12:49 |
| `root` | `nexus2025` | `217.60.255.130` | 2026-08-26T13:12:49 |
| `installer` | `installer` | `116.110.156.150` | 2026-08-26T13:16:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-26T13:18:37 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-26T13:18:37 |
| `ubuntu` | `Saeid@123` | `217.60.255.130` | 2026-08-26T13:22:11 |
| `root` | `localadmin` | `217.60.255.130` | 2026-08-26T13:22:13 |
| `ubnt` | `ubnt` | `116.110.156.150` | 2026-08-26T13:26:12 |
| `squid` | `squid` | `116.110.156.150` | 2026-08-26T13:30:56 |
| `ubuntu` | `Yousef1234` | `217.60.255.130` | 2026-08-26T13:31:42 |
| `root` | `Changeme_123` | `217.60.255.130` | 2026-08-26T13:31:46 |
| `config` | `config` | `171.231.190.48` | 2026-08-26T13:37:14 |
| `ubuntu` | `Abolfazl@1234` | `217.60.255.130` | 2026-08-26T13:41:48 |
| `root` | `nagios2024` | `217.60.255.130` | 2026-08-26T13:41:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-26T13:42:19 |
| `root` | `@` | `171.231.190.48` | 2026-08-26T13:45:10 |
| `ubuntu` | `Abolfazl2026` | `217.60.255.130` | 2026-08-26T13:51:09 |
| `root` | `sistemas` | `217.60.255.130` | 2026-08-26T13:51:13 |
| `ubuntu` | `qwe@123` | `217.60.255.130` | 2026-08-26T14:00:47 |
| `root` | `Admin2025` | `217.60.255.130` | 2026-08-26T14:00:52 |
| `ubuntu` | `123qweasd` | `217.60.255.130` | 2026-08-26T14:10:47 |
| `root` | `Servidor@123` | `217.60.255.130` | 2026-08-26T14:10:51 |
| `ubuntu` | `1qaz@WSX3edc` | `217.60.255.130` | 2026-08-26T14:20:20 |
| `root` | `server2022` | `217.60.255.130` | 2026-08-26T14:20:23 |
| `ubuntu` | `Asd1234` | `217.60.255.130` | 2026-08-26T14:29:51 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-26T14:29:54 |
| `root` | `123mudar` | `217.60.255.130` | 2026-08-26T14:29:57 |
| `ubuntu` | `Xx123456` | `217.60.255.130` | 2026-08-26T14:39:35 |
| `root` | `q1w2e3R$` | `217.60.255.130` | 2026-08-26T14:39:39 |
| `root` | `!root` | `195.178.110.227` | 2026-08-26T14:48:35 |
| `root` | `111111` | `195.178.110.227` | 2026-08-26T14:50:25 |
| `root` | `123123` | `195.178.110.227` | 2026-08-26T14:52:19 |
| `root` | `123321` | `195.178.110.227` | 2026-08-26T14:54:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **87** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 28 |
| Go SSH scanner | 11 |
| AsyncSSH (Python) | 9 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 9 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 4 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `fda360b1b4f4...` | AsyncSSH (Python) | 9 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 4 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `195.178.110.227`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS202425` | IP Volume inc | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS401661` | EMBNEX, LLC | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS204203` | Atrin Information & Communications Technology Company PJS | 1 | HIGH |
| `AS6876` | TENET Scientific Production Enterprise LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a591977d016

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:03 |
| **Last Seen** | 2026-08-26 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:03:03` | `cowrie.session.connect` |
| `2026-08-26 13:03:03` | `cowrie.client.version` |
| `2026-08-26 13:03:03` | `cowrie.client.kex` |
| `2026-08-26 13:03:04` | `cowrie.login.success` |
| `2026-08-26 13:03:04` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:03:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:03:04` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ae5a4e7b6b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:03 |
| **Last Seen** | 2026-08-26 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:03:06` | `cowrie.session.connect` |
| `2026-08-26 13:03:06` | `cowrie.client.version` |
| `2026-08-26 13:03:07` | `cowrie.client.kex` |
| `2026-08-26 13:03:08` | `cowrie.login.success` |
| `2026-08-26 13:03:08` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:03:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:03:08` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707493c58422

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]150` |
| **First Seen** | 2026-08-26 13:07 |
| **Last Seen** | 2026-08-26 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:07:59` | `cowrie.session.connect` |
| `2026-08-26 13:07:59` | `cowrie.client.version` |
| `2026-08-26 13:07:59` | `cowrie.client.kex` |
| `2026-08-26 13:08:00` | `cowrie.login.success` |
| `2026-08-26 13:08:01` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:08:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:08:02` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131920576015

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]150` |
| **First Seen** | 2026-08-26 13:10 |
| **Last Seen** | 2026-08-26 13:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:10:59` | `cowrie.session.connect` |
| `2026-08-26 13:10:59` | `cowrie.client.version` |
| `2026-08-26 13:11:00` | `cowrie.client.kex` |
| `2026-08-26 13:11:01` | `cowrie.login.success` |
| `2026-08-26 13:11:01` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:11:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:11:02` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765fc5abc2f4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:12 |
| **Last Seen** | 2026-08-26 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:12:47` | `cowrie.session.connect` |
| `2026-08-26 13:12:47` | `cowrie.client.version` |
| `2026-08-26 13:12:48` | `cowrie.client.kex` |
| `2026-08-26 13:12:49` | `cowrie.login.success` |
| `2026-08-26 13:12:49` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:12:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:12:49` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9d5ad0b732

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:12 |
| **Last Seen** | 2026-08-26 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:12:48` | `cowrie.session.connect` |
| `2026-08-26 13:12:48` | `cowrie.client.version` |
| `2026-08-26 13:12:48` | `cowrie.client.kex` |
| `2026-08-26 13:12:49` | `cowrie.login.success` |
| `2026-08-26 13:12:49` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:12:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:12:50` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a55511176ba

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]150` |
| **First Seen** | 2026-08-26 13:16 |
| **Last Seen** | 2026-08-26 13:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:16:15` | `cowrie.session.connect` |
| `2026-08-26 13:16:15` | `cowrie.client.version` |
| `2026-08-26 13:16:15` | `cowrie.client.kex` |
| `2026-08-26 13:16:17` | `cowrie.login.success` |
| `2026-08-26 13:16:17` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:16:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:16:18` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42eba043295

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 13:18 |
| **Last Seen** | 2026-08-26 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:18:36` | `cowrie.session.connect` |
| `2026-08-26 13:18:36` | `cowrie.client.version` |
| `2026-08-26 13:18:36` | `cowrie.client.kex` |
| `2026-08-26 13:18:37` | `cowrie.login.success` |
| `2026-08-26 13:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc22a373075

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 13:18 |
| **Last Seen** | 2026-08-26 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:18:36` | `cowrie.session.connect` |
| `2026-08-26 13:18:36` | `cowrie.client.version` |
| `2026-08-26 13:18:36` | `cowrie.client.kex` |
| `2026-08-26 13:18:37` | `cowrie.login.success` |
| `2026-08-26 13:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9685f5d15051

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:22 |
| **Last Seen** | 2026-08-26 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:22:10` | `cowrie.session.connect` |
| `2026-08-26 13:22:10` | `cowrie.client.version` |
| `2026-08-26 13:22:10` | `cowrie.client.kex` |
| `2026-08-26 13:22:11` | `cowrie.login.success` |
| `2026-08-26 13:22:11` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:22:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:22:11` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-841136da336d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:22 |
| **Last Seen** | 2026-08-26 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:22:12` | `cowrie.session.connect` |
| `2026-08-26 13:22:12` | `cowrie.client.version` |
| `2026-08-26 13:22:12` | `cowrie.client.kex` |
| `2026-08-26 13:22:13` | `cowrie.login.success` |
| `2026-08-26 13:22:13` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:22:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:22:13` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5d57a659fa

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]150` |
| **First Seen** | 2026-08-26 13:26 |
| **Last Seen** | 2026-08-26 13:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:26:06` | `cowrie.session.connect` |
| `2026-08-26 13:26:06` | `cowrie.client.version` |
| `2026-08-26 13:26:07` | `cowrie.client.kex` |
| `2026-08-26 13:26:12` | `cowrie.login.success` |
| `2026-08-26 13:26:12` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:26:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:26:13` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402da92178cf

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]150` |
| **First Seen** | 2026-08-26 13:30 |
| **Last Seen** | 2026-08-26 13:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:30:40` | `cowrie.session.connect` |
| `2026-08-26 13:30:40` | `cowrie.client.version` |
| `2026-08-26 13:30:51` | `cowrie.client.kex` |
| `2026-08-26 13:30:56` | `cowrie.login.success` |
| `2026-08-26 13:30:57` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:30:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:30:58` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83314dd8db7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:31 |
| **Last Seen** | 2026-08-26 13:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:31:39` | `cowrie.session.connect` |
| `2026-08-26 13:31:39` | `cowrie.client.version` |
| `2026-08-26 13:31:40` | `cowrie.client.kex` |
| `2026-08-26 13:31:42` | `cowrie.login.success` |
| `2026-08-26 13:31:42` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:31:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:31:42` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25c8119e6eb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:31 |
| **Last Seen** | 2026-08-26 13:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:31:43` | `cowrie.session.connect` |
| `2026-08-26 13:31:43` | `cowrie.client.version` |
| `2026-08-26 13:31:43` | `cowrie.client.kex` |
| `2026-08-26 13:31:46` | `cowrie.login.success` |
| `2026-08-26 13:31:46` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:31:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:31:47` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6edfb4d24056

| Field | Detail |
|---|---|
| **Source IP** | `171.231.190[.]48` |
| **First Seen** | 2026-08-26 13:35 |
| **Last Seen** | 2026-08-26 13:37 |
| **Session Duration** | 116s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:35:24` | `cowrie.session.connect` |
| `2026-08-26 13:35:25` | `cowrie.client.version` |
| `2026-08-26 13:35:26` | `cowrie.client.kex` |
| `2026-08-26 13:37:14` | `cowrie.login.success` |
| `2026-08-26 13:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.190[.]48` to AbuseIPDB if not already reported
- [ ] Block `171.231.190[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385fba95340d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:41 |
| **Last Seen** | 2026-08-26 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:41:47` | `cowrie.session.connect` |
| `2026-08-26 13:41:47` | `cowrie.client.version` |
| `2026-08-26 13:41:47` | `cowrie.client.kex` |
| `2026-08-26 13:41:48` | `cowrie.login.success` |
| `2026-08-26 13:41:48` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:41:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:41:48` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d697b9f8ea

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:41 |
| **Last Seen** | 2026-08-26 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:41:51` | `cowrie.session.connect` |
| `2026-08-26 13:41:51` | `cowrie.client.version` |
| `2026-08-26 13:41:51` | `cowrie.client.kex` |
| `2026-08-26 13:41:52` | `cowrie.login.success` |
| `2026-08-26 13:41:52` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:41:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:41:52` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a579b2e6a2f0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 13:42 |
| **Last Seen** | 2026-08-26 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:42:19` | `cowrie.session.connect` |
| `2026-08-26 13:42:19` | `cowrie.client.version` |
| `2026-08-26 13:42:19` | `cowrie.client.kex` |
| `2026-08-26 13:42:19` | `cowrie.login.success` |
| `2026-08-26 13:42:19` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:42:19` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b84dd7a7806c

| Field | Detail |
|---|---|
| **Source IP** | `171.231.190[.]48` |
| **First Seen** | 2026-08-26 13:44 |
| **Last Seen** | 2026-08-26 13:46 |
| **Session Duration** | 89s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:44:44` | `cowrie.session.connect` |
| `2026-08-26 13:44:44` | `cowrie.client.version` |
| `2026-08-26 13:44:44` | `cowrie.client.kex` |
| `2026-08-26 13:45:10` | `cowrie.login.success` |
| `2026-08-26 13:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.190[.]48` to AbuseIPDB if not already reported
- [ ] Block `171.231.190[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2995ee1a8bc3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 13:51 |
| **Last Seen** | 2026-08-26 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:51:01` | `cowrie.session.connect` |
| `2026-08-26 13:51:01` | `cowrie.client.version` |
| `2026-08-26 13:51:01` | `cowrie.client.kex` |
| `2026-08-26 13:51:01` | `cowrie.login.success` |
| `2026-08-26 13:51:01` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:51:01` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e2718139aa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:51 |
| **Last Seen** | 2026-08-26 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:51:08` | `cowrie.session.connect` |
| `2026-08-26 13:51:08` | `cowrie.client.version` |
| `2026-08-26 13:51:08` | `cowrie.client.kex` |
| `2026-08-26 13:51:09` | `cowrie.login.success` |
| `2026-08-26 13:51:09` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:51:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:51:10` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57943e3f245c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 13:51 |
| **Last Seen** | 2026-08-26 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 13:51:12` | `cowrie.session.connect` |
| `2026-08-26 13:51:12` | `cowrie.client.version` |
| `2026-08-26 13:51:12` | `cowrie.client.kex` |
| `2026-08-26 13:51:13` | `cowrie.login.success` |
| `2026-08-26 13:51:13` | `cowrie.direct-tcpip.request` |
| `2026-08-26 13:51:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 13:51:13` | `cowrie.direct-tcpip.data` |
| `2026-08-26 13:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2122bc70d0c9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:00 |
| **Last Seen** | 2026-08-26 14:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:00:44` | `cowrie.session.connect` |
| `2026-08-26 14:00:44` | `cowrie.client.version` |
| `2026-08-26 14:00:44` | `cowrie.client.kex` |
| `2026-08-26 14:00:47` | `cowrie.login.success` |
| `2026-08-26 14:00:47` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:00:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:00:48` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9476bafd7ff4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:00 |
| **Last Seen** | 2026-08-26 14:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:00:49` | `cowrie.session.connect` |
| `2026-08-26 14:00:50` | `cowrie.client.version` |
| `2026-08-26 14:00:50` | `cowrie.client.kex` |
| `2026-08-26 14:00:52` | `cowrie.login.success` |
| `2026-08-26 14:00:53` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:00:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:00:53` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c236ca3d7f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:10 |
| **Last Seen** | 2026-08-26 14:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:10:45` | `cowrie.session.connect` |
| `2026-08-26 14:10:45` | `cowrie.client.version` |
| `2026-08-26 14:10:45` | `cowrie.client.kex` |
| `2026-08-26 14:10:47` | `cowrie.login.success` |
| `2026-08-26 14:10:48` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:10:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:10:56` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4567585bbab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:10 |
| **Last Seen** | 2026-08-26 14:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:10:49` | `cowrie.session.connect` |
| `2026-08-26 14:10:49` | `cowrie.client.version` |
| `2026-08-26 14:10:50` | `cowrie.client.kex` |
| `2026-08-26 14:10:51` | `cowrie.login.success` |
| `2026-08-26 14:10:52` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:10:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:10:52` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a360ab6a280

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:20 |
| **Last Seen** | 2026-08-26 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:20:19` | `cowrie.session.connect` |
| `2026-08-26 14:20:19` | `cowrie.client.version` |
| `2026-08-26 14:20:19` | `cowrie.client.kex` |
| `2026-08-26 14:20:20` | `cowrie.login.success` |
| `2026-08-26 14:20:20` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:20:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:20:20` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37dd8fae02b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:20 |
| **Last Seen** | 2026-08-26 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:20:22` | `cowrie.session.connect` |
| `2026-08-26 14:20:22` | `cowrie.client.version` |
| `2026-08-26 14:20:22` | `cowrie.client.kex` |
| `2026-08-26 14:20:23` | `cowrie.login.success` |
| `2026-08-26 14:20:23` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:20:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:20:23` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c61f1d0281

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:29 |
| **Last Seen** | 2026-08-26 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:29:50` | `cowrie.session.connect` |
| `2026-08-26 14:29:50` | `cowrie.client.version` |
| `2026-08-26 14:29:50` | `cowrie.client.kex` |
| `2026-08-26 14:29:51` | `cowrie.login.success` |
| `2026-08-26 14:29:51` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:29:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:29:51` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae06d2b2fad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:29 |
| **Last Seen** | 2026-08-26 14:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:29:55` | `cowrie.session.connect` |
| `2026-08-26 14:29:55` | `cowrie.client.version` |
| `2026-08-26 14:29:55` | `cowrie.client.kex` |
| `2026-08-26 14:29:57` | `cowrie.login.success` |
| `2026-08-26 14:29:57` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:29:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:29:57` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68273f365706

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:39 |
| **Last Seen** | 2026-08-26 14:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:39:34` | `cowrie.session.connect` |
| `2026-08-26 14:39:34` | `cowrie.client.version` |
| `2026-08-26 14:39:34` | `cowrie.client.kex` |
| `2026-08-26 14:39:35` | `cowrie.login.success` |
| `2026-08-26 14:39:36` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:39:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:39:36` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54e99669d41

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 14:39 |
| **Last Seen** | 2026-08-26 14:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:39:38` | `cowrie.session.connect` |
| `2026-08-26 14:39:38` | `cowrie.client.version` |
| `2026-08-26 14:39:38` | `cowrie.client.kex` |
| `2026-08-26 14:39:39` | `cowrie.login.success` |
| `2026-08-26 14:39:39` | `cowrie.direct-tcpip.request` |
| `2026-08-26 14:39:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 14:39:39` | `cowrie.direct-tcpip.data` |
| `2026-08-26 14:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c461296868

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:48 |
| **Last Seen** | 2026-08-26 14:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:48:32` | `cowrie.session.connect` |
| `2026-08-26 14:48:33` | `cowrie.client.version` |
| `2026-08-26 14:48:33` | `cowrie.client.kex` |
| `2026-08-26 14:48:35` | `cowrie.login.success` |
| `2026-08-26 14:48:36` | `cowrie.session.params` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.success` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:36` | `cowrie.command.input` |
| `2026-08-26 14:48:37` | `cowrie.log.closed` |
| `2026-08-26 14:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7066707c4246

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:50 |
| **Last Seen** | 2026-08-26 14:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:50:23` | `cowrie.session.connect` |
| `2026-08-26 14:50:23` | `cowrie.client.version` |
| `2026-08-26 14:50:23` | `cowrie.client.kex` |
| `2026-08-26 14:50:25` | `cowrie.login.success` |
| `2026-08-26 14:50:26` | `cowrie.session.params` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.success` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:26` | `cowrie.command.input` |
| `2026-08-26 14:50:27` | `cowrie.log.closed` |
| `2026-08-26 14:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e2b5789d4b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:52 |
| **Last Seen** | 2026-08-26 14:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:52:18` | `cowrie.session.connect` |
| `2026-08-26 14:52:18` | `cowrie.client.version` |
| `2026-08-26 14:52:18` | `cowrie.client.kex` |
| `2026-08-26 14:52:19` | `cowrie.login.success` |
| `2026-08-26 14:52:20` | `cowrie.session.params` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.success` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.command.input` |
| `2026-08-26 14:52:20` | `cowrie.log.closed` |
| `2026-08-26 14:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e9fee5d600

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:54 |
| **Last Seen** | 2026-08-26 14:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:54:14` | `cowrie.session.connect` |
| `2026-08-26 14:54:14` | `cowrie.client.version` |
| `2026-08-26 14:54:14` | `cowrie.client.kex` |
| `2026-08-26 14:54:15` | `cowrie.login.success` |
| `2026-08-26 14:54:16` | `cowrie.session.params` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.success` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:16` | `cowrie.command.input` |
| `2026-08-26 14:54:17` | `cowrie.log.closed` |
| `2026-08-26 14:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.37.220[.]188` | **5** | 2026-08-26 12:55 | 2026-08-26 14:45 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-26 13:16 | 2026-08-26 14:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.78[.]145` | **4** | 2026-08-26 13:55 | 2026-08-26 13:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `73.193.6[.]60` | **3** | 2026-08-26 13:47 | 2026-08-26 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **3** | 2026-08-26 13:01 | 2026-08-26 13:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-26 13:03 | 2026-08-26 14:03 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `171.231.190[.]48` | **2** | 2026-08-26 13:51 | 2026-08-26 13:55 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-26 13:43 | 2026-08-26 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.191.193[.]162` | **2** | 2026-08-26 14:10 | 2026-08-26 14:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-08-26 14:04 | 2026-08-26 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.156[.]150` | 1 | 2026-08-26 13:20 | 2026-08-26 13:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]133` | 1 | 2026-08-26 14:23 | 2026-08-26 14:23 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-08-26 14:30 | 2026-08-26 14:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.61.64[.]135` | 1 | 2026-08-26 14:45 | 2026-08-26 14:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-26 13:07 | 2026-08-26 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-26 13:37 | 2026-08-26 13:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]17` | 1 | 2026-08-26 12:59 | 2026-08-26 12:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-26 14:03 | 2026-08-26 14:03 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `116.110.156[.]150` | VN | Viettel Group | **100** ⚠️ | 0 |
| `102.37.220[.]188` | ZA | Microsoft (S.A.) (Proprietary) Limited | **100** ⚠️ | 19 |
| `16.5.0[.]133` | BR | EMBNEX. LLC | **100** ⚠️ | 15 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `171.231.190[.]48` | VN | Viettel Group | **100** ⚠️ | 0 |
| `73.193.6[.]60` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 2 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `210.61.64[.]135` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 4 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 87 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 18 recon entry/entries in table (10 group(s) consolidating 29 session(s)).

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
_Report time: 2026-08-26T16:50:32Z_

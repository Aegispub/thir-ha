# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T16:40:51Z |
| **Shift Time** | 16:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **143** |
| Confirmed Threats | **93** |
| False Positives Filtered | **50** (35.0%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **17** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **105** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **42** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **8** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `ubuntu` | 12 |
| `GET / HTTP/1.0` | 4 |
| `admin` | 2 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `Host: 129.80.119.236` | 4 |
| `CSeq:1` | 2 |
| `root123` | 1 |
| `root2026` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | 4 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | 2 |
| `root` | `root123` | 1 |
| `root` | `root2026` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root123` | `80.94.92.55` | 2026-08-25T12:55:58 |
| `root` | `root2026` | `80.94.92.55` | 2026-08-25T12:57:48 |
| `root` | `welcome` | `80.94.92.55` | 2026-08-25T13:00:08 |
| `ubuntu` | `abcd@1234` | `217.60.255.130` | 2026-08-25T13:00:52 |
| `root` | `qazwsx` | `217.60.255.130` | 2026-08-25T13:00:56 |
| `admin` | `123456` | `80.94.92.55` | 2026-08-25T13:02:14 |
| `admin` | `123qwe` | `80.94.92.55` | 2026-08-25T13:05:17 |
| `ubuntu` | `Qwe123` | `217.60.255.130` | 2026-08-25T13:10:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T13:10:36 |
| `root` | `@dm!n1234` | `217.60.255.130` | 2026-08-25T13:10:37 |
| `ubuntu` | `Berbidvps.ir` | `217.60.255.130` | 2026-08-25T13:20:09 |
| `root` | `Password@123` | `217.60.255.130` | 2026-08-25T13:20:13 |
| `ubuntu` | `Asd123` | `217.60.255.130` | 2026-08-25T13:29:59 |
| `root` | `Password@12345` | `217.60.255.130` | 2026-08-25T13:30:03 |
| `ubuntu` | `Qwer!234` | `217.60.255.130` | 2026-08-25T13:40:04 |
| `root` | `P@ssw0rd123#` | `217.60.255.130` | 2026-08-25T13:40:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `111.113.89.59` | 2026-08-25T13:46:01 |
| `ubuntu` | `Admin1234!` | `217.60.255.130` | 2026-08-25T13:50:05 |
| `root` | `Info@2024` | `217.60.255.130` | 2026-08-25T13:50:12 |
| `ubuntu` | `qwert1234` | `217.60.255.130` | 2026-08-25T14:00:09 |
| `root` | `123456aa` | `217.60.255.130` | 2026-08-25T14:00:13 |
| `ubuntu` | `Aa123321` | `217.60.255.130` | 2026-08-25T14:09:55 |
| `root` | `-1234567890` | `217.60.255.130` | 2026-08-25T14:09:59 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `43.106.56.236` | 2026-08-25T14:17:03 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `43.106.56.236` | 2026-08-25T14:17:14 |
| `USER test` | `USER test` | `43.106.56.236` | 2026-08-25T14:17:23 |
| `ubuntu` | `A123456` | `217.60.255.130` | 2026-08-25T14:19:58 |
| `root` | `123456789aA@` | `217.60.255.130` | 2026-08-25T14:20:05 |
| `ubuntu` | `QAZwsx@123` | `217.60.255.130` | 2026-08-25T14:30:16 |
| `root` | `Password@2` | `217.60.255.130` | 2026-08-25T14:30:22 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `43.106.51.179` | 2026-08-25T14:33:11 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `43.106.51.179` | 2026-08-25T14:33:22 |
| `ubuntu` | `Oracle@2025` | `217.60.255.130` | 2026-08-25T14:40:42 |
| `root` | `woaini520` | `217.60.255.130` | 2026-08-25T14:40:46 |
| `ubuntu` | `Pan@123` | `217.60.255.130` | 2026-08-25T14:50:36 |
| `root` | `Aa.123456` | `217.60.255.130` | 2026-08-25T14:50:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **143** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 9 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 5 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1078, T1083` |

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
| Total IPs Analysed | **41** |
| Unique ASNs | **28** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | LOW |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | MEDIUM |
| `AS215930` | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | 1 | HIGH |
| `AS3320` | Deutsche Telekom AG | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f861f881eb95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:55 |
| **Last Seen** | 2026-08-25 12:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:55:56` | `cowrie.session.connect` |
| `2026-08-25 12:55:56` | `cowrie.client.version` |
| `2026-08-25 12:55:56` | `cowrie.client.kex` |
| `2026-08-25 12:55:58` | `cowrie.login.success` |
| `2026-08-25 12:56:00` | `cowrie.session.params` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.success` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:00` | `cowrie.command.input` |
| `2026-08-25 12:56:01` | `cowrie.log.closed` |
| `2026-08-25 12:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d316998d0d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:57 |
| **Last Seen** | 2026-08-25 12:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:57:46` | `cowrie.session.connect` |
| `2026-08-25 12:57:46` | `cowrie.client.version` |
| `2026-08-25 12:57:46` | `cowrie.client.kex` |
| `2026-08-25 12:57:48` | `cowrie.login.success` |
| `2026-08-25 12:57:49` | `cowrie.session.params` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.success` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.command.input` |
| `2026-08-25 12:57:49` | `cowrie.log.closed` |
| `2026-08-25 12:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fb7225ff22

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 13:00 |
| **Last Seen** | 2026-08-25 13:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:00:07` | `cowrie.session.connect` |
| `2026-08-25 13:00:07` | `cowrie.client.version` |
| `2026-08-25 13:00:07` | `cowrie.client.kex` |
| `2026-08-25 13:00:08` | `cowrie.login.success` |
| `2026-08-25 13:00:09` | `cowrie.session.params` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.success` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.command.input` |
| `2026-08-25 13:00:09` | `cowrie.log.closed` |
| `2026-08-25 13:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4272089c5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:00 |
| **Last Seen** | 2026-08-25 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:00:51` | `cowrie.session.connect` |
| `2026-08-25 13:00:51` | `cowrie.client.version` |
| `2026-08-25 13:00:51` | `cowrie.client.kex` |
| `2026-08-25 13:00:52` | `cowrie.login.success` |
| `2026-08-25 13:00:52` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:00:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:00:52` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d627404801

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:00 |
| **Last Seen** | 2026-08-25 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:00:54` | `cowrie.session.connect` |
| `2026-08-25 13:00:54` | `cowrie.client.version` |
| `2026-08-25 13:00:55` | `cowrie.client.kex` |
| `2026-08-25 13:00:56` | `cowrie.login.success` |
| `2026-08-25 13:00:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:00:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:00:56` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd8fd343eb0c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 13:02 |
| **Last Seen** | 2026-08-25 13:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:02:13` | `cowrie.session.connect` |
| `2026-08-25 13:02:13` | `cowrie.client.version` |
| `2026-08-25 13:02:13` | `cowrie.client.kex` |
| `2026-08-25 13:02:14` | `cowrie.login.success` |
| `2026-08-25 13:02:15` | `cowrie.session.params` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.success` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.command.input` |
| `2026-08-25 13:02:15` | `cowrie.log.closed` |
| `2026-08-25 13:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19858f07fca6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 13:05 |
| **Last Seen** | 2026-08-25 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:05:16` | `cowrie.session.connect` |
| `2026-08-25 13:05:16` | `cowrie.client.version` |
| `2026-08-25 13:05:17` | `cowrie.client.kex` |
| `2026-08-25 13:05:17` | `cowrie.login.success` |
| `2026-08-25 13:05:18` | `cowrie.session.params` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.success` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.command.input` |
| `2026-08-25 13:05:18` | `cowrie.log.closed` |
| `2026-08-25 13:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7e6f4fbbf7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:10 |
| **Last Seen** | 2026-08-25 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:10:32` | `cowrie.session.connect` |
| `2026-08-25 13:10:32` | `cowrie.client.version` |
| `2026-08-25 13:10:33` | `cowrie.client.kex` |
| `2026-08-25 13:10:34` | `cowrie.login.success` |
| `2026-08-25 13:10:34` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:10:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:10:34` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3182d118e1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 13:10 |
| **Last Seen** | 2026-08-25 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:10:35` | `cowrie.session.connect` |
| `2026-08-25 13:10:35` | `cowrie.client.version` |
| `2026-08-25 13:10:35` | `cowrie.client.kex` |
| `2026-08-25 13:10:36` | `cowrie.login.success` |
| `2026-08-25 13:10:36` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:10:36` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aaaddb05e8d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:10 |
| **Last Seen** | 2026-08-25 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:10:36` | `cowrie.session.connect` |
| `2026-08-25 13:10:36` | `cowrie.client.version` |
| `2026-08-25 13:10:36` | `cowrie.client.kex` |
| `2026-08-25 13:10:37` | `cowrie.login.success` |
| `2026-08-25 13:10:37` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:10:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:10:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877cab7fd5fb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:20 |
| **Last Seen** | 2026-08-25 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:20:08` | `cowrie.session.connect` |
| `2026-08-25 13:20:08` | `cowrie.client.version` |
| `2026-08-25 13:20:08` | `cowrie.client.kex` |
| `2026-08-25 13:20:09` | `cowrie.login.success` |
| `2026-08-25 13:20:09` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:20:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:20:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46b856c8627

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:20 |
| **Last Seen** | 2026-08-25 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:20:12` | `cowrie.session.connect` |
| `2026-08-25 13:20:12` | `cowrie.client.version` |
| `2026-08-25 13:20:12` | `cowrie.client.kex` |
| `2026-08-25 13:20:13` | `cowrie.login.success` |
| `2026-08-25 13:20:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:20:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:20:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf574ec3a8cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:29 |
| **Last Seen** | 2026-08-25 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:29:58` | `cowrie.session.connect` |
| `2026-08-25 13:29:58` | `cowrie.client.version` |
| `2026-08-25 13:29:58` | `cowrie.client.kex` |
| `2026-08-25 13:29:59` | `cowrie.login.success` |
| `2026-08-25 13:29:59` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:30:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:30:00` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb9205aff48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:30 |
| **Last Seen** | 2026-08-25 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:30:02` | `cowrie.session.connect` |
| `2026-08-25 13:30:02` | `cowrie.client.version` |
| `2026-08-25 13:30:02` | `cowrie.client.kex` |
| `2026-08-25 13:30:03` | `cowrie.login.success` |
| `2026-08-25 13:30:03` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:30:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:30:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f84ad6d6b83

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:40 |
| **Last Seen** | 2026-08-25 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:40:03` | `cowrie.session.connect` |
| `2026-08-25 13:40:03` | `cowrie.client.version` |
| `2026-08-25 13:40:03` | `cowrie.client.kex` |
| `2026-08-25 13:40:04` | `cowrie.login.success` |
| `2026-08-25 13:40:04` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:40:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:40:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4473d4a1ba5e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:40 |
| **Last Seen** | 2026-08-25 13:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:40:09` | `cowrie.session.connect` |
| `2026-08-25 13:40:09` | `cowrie.client.version` |
| `2026-08-25 13:40:09` | `cowrie.client.kex` |
| `2026-08-25 13:40:13` | `cowrie.login.success` |
| `2026-08-25 13:40:15` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:40:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:40:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235c91cc9924

| Field | Detail |
|---|---|
| **Source IP** | `111.113.89[.]59` |
| **First Seen** | 2026-08-25 13:46 |
| **Last Seen** | 2026-08-25 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:46:00` | `cowrie.session.connect` |
| `2026-08-25 13:46:01` | `cowrie.login.success` |
| `2026-08-25 13:46:01` | `cowrie.session.params` |
| `2026-08-25 13:46:01` | `cowrie.command.input` |
| `2026-08-25 13:46:01` | `cowrie.command.failed` |
| `2026-08-25 13:46:01` | `cowrie.command.input` |
| `2026-08-25 13:46:02` | `cowrie.log.closed` |
| `2026-08-25 13:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.113.89[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.113.89[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb391b9accc0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:50 |
| **Last Seen** | 2026-08-25 13:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:50:02` | `cowrie.session.connect` |
| `2026-08-25 13:50:03` | `cowrie.client.version` |
| `2026-08-25 13:50:03` | `cowrie.client.kex` |
| `2026-08-25 13:50:05` | `cowrie.login.success` |
| `2026-08-25 13:50:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:50:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:50:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed1c277d170

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 13:50 |
| **Last Seen** | 2026-08-25 13:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 13:50:10` | `cowrie.session.connect` |
| `2026-08-25 13:50:10` | `cowrie.client.version` |
| `2026-08-25 13:50:11` | `cowrie.client.kex` |
| `2026-08-25 13:50:12` | `cowrie.login.success` |
| `2026-08-25 13:50:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 13:50:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 13:50:12` | `cowrie.direct-tcpip.data` |
| `2026-08-25 13:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05116072b2fc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:00 |
| **Last Seen** | 2026-08-25 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:00:08` | `cowrie.session.connect` |
| `2026-08-25 14:00:08` | `cowrie.client.version` |
| `2026-08-25 14:00:08` | `cowrie.client.kex` |
| `2026-08-25 14:00:09` | `cowrie.login.success` |
| `2026-08-25 14:00:09` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:00:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:00:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4c0975c547

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:00 |
| **Last Seen** | 2026-08-25 14:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:00:12` | `cowrie.session.connect` |
| `2026-08-25 14:00:12` | `cowrie.client.version` |
| `2026-08-25 14:00:13` | `cowrie.client.kex` |
| `2026-08-25 14:00:13` | `cowrie.login.success` |
| `2026-08-25 14:00:14` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:00:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:00:14` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63a72c3e105

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:09 |
| **Last Seen** | 2026-08-25 14:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:09:54` | `cowrie.session.connect` |
| `2026-08-25 14:09:54` | `cowrie.client.version` |
| `2026-08-25 14:09:54` | `cowrie.client.kex` |
| `2026-08-25 14:09:55` | `cowrie.login.success` |
| `2026-08-25 14:09:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:09:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:09:57` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7738c2de44b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:09 |
| **Last Seen** | 2026-08-25 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:09:58` | `cowrie.session.connect` |
| `2026-08-25 14:09:58` | `cowrie.client.version` |
| `2026-08-25 14:09:59` | `cowrie.client.kex` |
| `2026-08-25 14:09:59` | `cowrie.login.success` |
| `2026-08-25 14:10:00` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:10:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:10:00` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c48d80c06a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:19 |
| **Last Seen** | 2026-08-25 14:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:19:56` | `cowrie.session.connect` |
| `2026-08-25 14:19:56` | `cowrie.client.version` |
| `2026-08-25 14:19:57` | `cowrie.client.kex` |
| `2026-08-25 14:19:58` | `cowrie.login.success` |
| `2026-08-25 14:19:58` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:19:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:19:59` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c101bf388662

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:20 |
| **Last Seen** | 2026-08-25 14:20 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:20:02` | `cowrie.session.connect` |
| `2026-08-25 14:20:02` | `cowrie.client.version` |
| `2026-08-25 14:20:02` | `cowrie.client.kex` |
| `2026-08-25 14:20:05` | `cowrie.login.success` |
| `2026-08-25 14:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-245bd7b5ef7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:30 |
| **Last Seen** | 2026-08-25 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:30:15` | `cowrie.session.connect` |
| `2026-08-25 14:30:15` | `cowrie.client.version` |
| `2026-08-25 14:30:16` | `cowrie.client.kex` |
| `2026-08-25 14:30:16` | `cowrie.login.success` |
| `2026-08-25 14:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:30:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:30:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ed31b7e84e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:30 |
| **Last Seen** | 2026-08-25 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:30:21` | `cowrie.session.connect` |
| `2026-08-25 14:30:21` | `cowrie.client.version` |
| `2026-08-25 14:30:21` | `cowrie.client.kex` |
| `2026-08-25 14:30:22` | `cowrie.login.success` |
| `2026-08-25 14:30:22` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:30:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:30:22` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0480cb63a2f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:40 |
| **Last Seen** | 2026-08-25 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:40:41` | `cowrie.session.connect` |
| `2026-08-25 14:40:41` | `cowrie.client.version` |
| `2026-08-25 14:40:41` | `cowrie.client.kex` |
| `2026-08-25 14:40:42` | `cowrie.login.success` |
| `2026-08-25 14:40:43` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:40:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:40:43` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288a594655b5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:40 |
| **Last Seen** | 2026-08-25 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:40:45` | `cowrie.session.connect` |
| `2026-08-25 14:40:45` | `cowrie.client.version` |
| `2026-08-25 14:40:45` | `cowrie.client.kex` |
| `2026-08-25 14:40:46` | `cowrie.login.success` |
| `2026-08-25 14:40:46` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:40:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:40:46` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea734ec77f04

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:50 |
| **Last Seen** | 2026-08-25 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:50:35` | `cowrie.session.connect` |
| `2026-08-25 14:50:35` | `cowrie.client.version` |
| `2026-08-25 14:50:36` | `cowrie.client.kex` |
| `2026-08-25 14:50:36` | `cowrie.login.success` |
| `2026-08-25 14:50:37` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:50:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:50:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6975f3bdf9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 14:50 |
| **Last Seen** | 2026-08-25 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 14:50:39` | `cowrie.session.connect` |
| `2026-08-25 14:50:39` | `cowrie.client.version` |
| `2026-08-25 14:50:39` | `cowrie.client.kex` |
| `2026-08-25 14:50:40` | `cowrie.login.success` |
| `2026-08-25 14:50:40` | `cowrie.direct-tcpip.request` |
| `2026-08-25 14:50:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 14:50:40` | `cowrie.direct-tcpip.data` |
| `2026-08-25 14:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **25** | 2026-08-25 13:06 | 2026-08-25 14:41 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.229[.]23` | **7** | 2026-08-25 13:09 | 2026-08-25 14:50 | 11m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]164` | **5** | 2026-08-25 14:42 | 2026-08-25 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-25 13:13 | 2026-08-25 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.233.112[.]103` | **2** | 2026-08-25 13:01 | 2026-08-25 13:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-25 13:20 | 2026-08-25 14:18 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `14.29.208[.]128` | **2** | 2026-08-25 12:55 | 2026-08-25 12:58 | 7m | 0 | `T1592` | 🟢 LOW |
| `45.224.153[.]13` | **2** | 2026-08-25 13:04 | 2026-08-25 13:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.24.16[.]6` | 1 | 2026-08-25 13:46 | 2026-08-25 13:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.178.210[.]250` | 1 | 2026-08-25 13:45 | 2026-08-25 13:45 | 4s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]9` | 1 | 2026-08-25 13:39 | 2026-08-25 13:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-25 13:35 | 2026-08-25 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-25 13:00 | 2026-08-25 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.65.233[.]63` | 1 | 2026-08-25 14:43 | 2026-08-25 14:43 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-25 14:34 | 2026-08-25 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-08-25 14:34 | 2026-08-25 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.84.107[.]182` | 1 | 2026-08-25 14:27 | 2026-08-25 14:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-08-25 13:06 | 2026-08-25 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]103` | 1 | 2026-08-25 13:32 | 2026-08-25 13:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | 1 | 2026-08-25 14:46 | 2026-08-25 14:47 | 66s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]32` | 1 | 2026-08-25 13:36 | 2026-08-25 13:36 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `134.209.229[.]23` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `151.243.11[.]9` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 9 |
| `66.132.172[.]103` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.65.233[.]63` | CO | COLOMBIA MAS TV S.A.S | **100** ⚠️ | 6 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `62.60.130[.]201` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 37 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 13 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 143 cases |
| Tool 34  | Credential Extractor        | ✅ 42 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (35.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 21 recon entry/entries in table (8 group(s) consolidating 49 session(s)).

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
_Report time: 2026-08-25T16:40:51Z_

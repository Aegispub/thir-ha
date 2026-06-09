# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T23:19:30Z |
| **Shift Time** | 23:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **61** |
| Confirmed Threats | **50** |
| False Positives Filtered | **11** (18.0%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **25** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **5** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `user` | 3 |
| `slade` | 1 |
| `telnet` | 1 |
| `amaiya` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 6 |
| `123@@@` | 4 |
| `smo@@kkklss` | 4 |
| `user` | 2 |
| `ankurkudintzi` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `user` | `user` | 2 |
| `root` | `ankurkudintzi` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password` | `2.57.121.112` | 2026-06-09T21:06:41 |
| `user` | `user` | `176.65.139.130` | 2026-06-09T21:15:30 |
| `slade` | `slade` | `213.209.159.56` | 2026-06-09T21:17:45 |
| `root` | `ankurkudintzi` | `45.156.87.117` | 2026-06-09T21:44:07 |
| `root` | `ankurkudintzi` | `176.65.139.250` | 2026-06-09T22:03:18 |
| `user` | `medicina` | `2.57.121.25` | 2026-06-09T22:03:25 |
| `root` | `` | `176.65.139.41` | 2026-06-09T22:05:45 |
| `root` | `centos` | `117.176.220.76` | 2026-06-09T22:14:03 |
| `telnet` | `telnet` | `2.57.121.112` | 2026-06-09T22:22:58 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-09T22:24:37 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-09T22:24:37 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-09T22:24:44 |
| `amaiya` | `amaiya` | `213.209.159.56` | 2026-06-09T22:30:07 |
| `root` | `123@@@` | `152.69.219.209` | 2026-06-09T22:41:55 |
| `root` | `LeitboGi0ro` | `152.69.219.209` | 2026-06-09T22:41:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-09T22:44:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-09T22:44:05 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-09T22:44:05 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-09T22:45:14 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-09T22:45:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **61** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 14 |
| PuTTY | 5 |
| Go SSH scanner | 5 |
| libssh | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `57446c12547a...` | Mirai/variant | 5 | 3 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `4c20a8895324...` | Mirai/variant | 2 | 1 |
| `16443846184e...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `57446c12547a...` | PuTTY | 5 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `4c20a8895324...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **14** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS214472` | Offshore LC | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS0` |  | 1 | LOW |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS8926` | Moldtelecom SA | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-61610ea5649f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-09 21:06 |
| **Last Seen** | 2026-06-09 21:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:06:41` | `cowrie.session.connect` |
| `2026-06-09 21:06:41` | `cowrie.client.version` |
| `2026-06-09 21:06:41` | `cowrie.client.kex` |
| `2026-06-09 21:06:41` | `cowrie.login.success` |
| `2026-06-09 21:06:41` | `cowrie.direct-tcpip.request` |
| `2026-06-09 21:06:41` | `cowrie.direct-tcpip.data` |
| `2026-06-09 21:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce61813ae5d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-09 21:15 |
| **Last Seen** | 2026-06-09 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:15:29` | `cowrie.session.connect` |
| `2026-06-09 21:15:30` | `cowrie.client.version` |
| `2026-06-09 21:15:30` | `cowrie.client.kex` |
| `2026-06-09 21:15:30` | `cowrie.login.success` |
| `2026-06-09 21:15:30` | `cowrie.direct-tcpip.request` |
| `2026-06-09 21:15:30` | `cowrie.direct-tcpip.ja4` |
| `2026-06-09 21:15:30` | `cowrie.direct-tcpip.data` |
| `2026-06-09 21:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6245a756222b

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-09 21:17 |
| **Last Seen** | 2026-06-09 21:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:17:45` | `cowrie.session.connect` |
| `2026-06-09 21:17:45` | `cowrie.client.version` |
| `2026-06-09 21:17:45` | `cowrie.client.kex` |
| `2026-06-09 21:17:45` | `cowrie.login.success` |
| `2026-06-09 21:17:45` | `cowrie.direct-tcpip.request` |
| `2026-06-09 21:17:45` | `cowrie.direct-tcpip.data` |
| `2026-06-09 21:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f643cd35a53

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]117` |
| **First Seen** | 2026-06-09 21:44 |
| **Last Seen** | 2026-06-09 21:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:44:04` | `cowrie.session.connect` |
| `2026-06-09 21:44:05` | `cowrie.client.version` |
| `2026-06-09 21:44:05` | `cowrie.client.kex` |
| `2026-06-09 21:44:07` | `cowrie.login.success` |
| `2026-06-09 21:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]117` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab1ed1f30215

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]250` |
| **First Seen** | 2026-06-09 22:03 |
| **Last Seen** | 2026-06-09 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:03:17` | `cowrie.session.connect` |
| `2026-06-09 22:03:17` | `cowrie.client.version` |
| `2026-06-09 22:03:18` | `cowrie.client.kex` |
| `2026-06-09 22:03:18` | `cowrie.login.success` |
| `2026-06-09 22:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]250` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0a4020d0fe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-09 22:03 |
| **Last Seen** | 2026-06-09 22:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:03:25` | `cowrie.session.connect` |
| `2026-06-09 22:03:25` | `cowrie.client.version` |
| `2026-06-09 22:03:25` | `cowrie.client.kex` |
| `2026-06-09 22:03:25` | `cowrie.login.success` |
| `2026-06-09 22:03:26` | `cowrie.direct-tcpip.request` |
| `2026-06-09 22:03:26` | `cowrie.direct-tcpip.data` |
| `2026-06-09 22:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88960283bed7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]41` |
| **First Seen** | 2026-06-09 22:05 |
| **Last Seen** | 2026-06-09 22:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:05:45` | `cowrie.session.connect` |
| `2026-06-09 22:05:45` | `cowrie.login.success` |
| `2026-06-09 22:05:46` | `cowrie.session.params` |
| `2026-06-09 22:05:46` | `cowrie.command.input` |
| `2026-06-09 22:05:47` | `cowrie.command.input` |
| `2026-06-09 22:05:48` | `cowrie.command.input` |
| `2026-06-09 22:05:48` | `cowrie.command.input` |
| `2026-06-09 22:05:48` | `cowrie.command.failed` |
| `2026-06-09 22:05:49` | `cowrie.log.closed` |
| `2026-06-09 22:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]41` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db144c821b81

| Field | Detail |
|---|---|
| **Source IP** | `117.176.220[.]76` |
| **First Seen** | 2026-06-09 22:14 |
| **Last Seen** | 2026-06-09 22:19 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:14:02` | `cowrie.session.connect` |
| `2026-06-09 22:14:02` | `cowrie.client.version` |
| `2026-06-09 22:14:02` | `cowrie.client.kex` |
| `2026-06-09 22:14:03` | `cowrie.login.success` |
| `2026-06-09 22:19:03` | `cowrie.session.file_upload` |
| `2026-06-09 22:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.176.220[.]76` to AbuseIPDB if not already reported
- [ ] Block `117.176.220[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4db26ebed0a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-09 22:22 |
| **Last Seen** | 2026-06-09 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:22:05` | `cowrie.session.connect` |
| `2026-06-09 22:22:05` | `cowrie.client.version` |
| `2026-06-09 22:22:05` | `cowrie.client.kex` |
| `2026-06-09 22:22:05` | `cowrie.login.success` |
| `2026-06-09 22:22:06` | `cowrie.direct-tcpip.request` |
| `2026-06-09 22:22:06` | `cowrie.direct-tcpip.ja4` |
| `2026-06-09 22:22:06` | `cowrie.direct-tcpip.data` |
| `2026-06-09 22:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c6732fa247

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-09 22:22 |
| **Last Seen** | 2026-06-09 22:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:22:57` | `cowrie.session.connect` |
| `2026-06-09 22:22:57` | `cowrie.client.version` |
| `2026-06-09 22:22:58` | `cowrie.client.kex` |
| `2026-06-09 22:22:58` | `cowrie.login.success` |
| `2026-06-09 22:22:58` | `cowrie.direct-tcpip.request` |
| `2026-06-09 22:22:58` | `cowrie.direct-tcpip.data` |
| `2026-06-09 22:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7540356ab0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 22:24 |
| **Last Seen** | 2026-06-09 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:24:37` | `cowrie.session.connect` |
| `2026-06-09 22:24:37` | `cowrie.client.version` |
| `2026-06-09 22:24:37` | `cowrie.client.kex` |
| `2026-06-09 22:24:37` | `cowrie.login.success` |
| `2026-06-09 22:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74cd01127029

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 22:24 |
| **Last Seen** | 2026-06-09 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:24:37` | `cowrie.session.connect` |
| `2026-06-09 22:24:37` | `cowrie.client.version` |
| `2026-06-09 22:24:37` | `cowrie.client.kex` |
| `2026-06-09 22:24:37` | `cowrie.login.success` |
| `2026-06-09 22:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc362c63e62d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 22:24 |
| **Last Seen** | 2026-06-09 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:24:43` | `cowrie.session.connect` |
| `2026-06-09 22:24:43` | `cowrie.client.version` |
| `2026-06-09 22:24:44` | `cowrie.client.kex` |
| `2026-06-09 22:24:44` | `cowrie.login.success` |
| `2026-06-09 22:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2c57d9e649

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-09 22:24 |
| **Last Seen** | 2026-06-09 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:24:44` | `cowrie.session.connect` |
| `2026-06-09 22:24:44` | `cowrie.client.version` |
| `2026-06-09 22:24:44` | `cowrie.client.kex` |
| `2026-06-09 22:24:45` | `cowrie.login.success` |
| `2026-06-09 22:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a18f468671dd

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-09 22:30 |
| **Last Seen** | 2026-06-09 22:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:30:06` | `cowrie.session.connect` |
| `2026-06-09 22:30:06` | `cowrie.client.version` |
| `2026-06-09 22:30:07` | `cowrie.client.kex` |
| `2026-06-09 22:30:07` | `cowrie.login.success` |
| `2026-06-09 22:30:07` | `cowrie.direct-tcpip.request` |
| `2026-06-09 22:30:07` | `cowrie.direct-tcpip.data` |
| `2026-06-09 22:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0571d2d0c5a

| Field | Detail |
|---|---|
| **Source IP** | `152.69.219[.]209` |
| **First Seen** | 2026-06-09 22:41 |
| **Last Seen** | 2026-06-09 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:41:53` | `cowrie.session.connect` |
| `2026-06-09 22:41:53` | `cowrie.client.version` |
| `2026-06-09 22:41:54` | `cowrie.client.kex` |
| `2026-06-09 22:41:55` | `cowrie.login.success` |
| `2026-06-09 22:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.69.219[.]209` to AbuseIPDB if not already reported
- [ ] Block `152.69.219[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e351b38712

| Field | Detail |
|---|---|
| **Source IP** | `152.69.219[.]209` |
| **First Seen** | 2026-06-09 22:41 |
| **Last Seen** | 2026-06-09 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:41:54` | `cowrie.session.connect` |
| `2026-06-09 22:41:54` | `cowrie.client.version` |
| `2026-06-09 22:41:54` | `cowrie.client.kex` |
| `2026-06-09 22:41:55` | `cowrie.login.success` |
| `2026-06-09 22:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.69.219[.]209` to AbuseIPDB if not already reported
- [ ] Block `152.69.219[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aada2b2eaa7

| Field | Detail |
|---|---|
| **Source IP** | `152.69.219[.]209` |
| **First Seen** | 2026-06-09 22:42 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:42:12` | `cowrie.session.connect` |
| `2026-06-09 22:42:12` | `cowrie.client.version` |
| `2026-06-09 22:42:12` | `cowrie.client.kex` |
| `2026-06-09 22:42:13` | `cowrie.login.success` |
| `2026-06-09 22:42:16` | `cowrie.session.file_upload` |
| `2026-06-09 22:42:17` | `cowrie.session.params` |
| `2026-06-09 22:42:17` | `cowrie.command.input` |
| `2026-06-09 22:42:17` | `cowrie.command.input` |
| `2026-06-09 22:42:17` | `cowrie.command.input` |
| `2026-06-09 22:42:17` | `cowrie.command.failed` |
| `2026-06-09 22:42:17` | `cowrie.log.closed` |
| `2026-06-09 22:42:18` | `cowrie.session.params` |
| `2026-06-09 22:42:18` | `cowrie.command.input` |
| `2026-06-09 22:42:18` | `cowrie.log.closed` |
| `2026-06-09 22:42:19` | `cowrie.session.params` |
| `2026-06-09 22:42:19` | `cowrie.command.input` |
| `2026-06-09 22:42:20` | `cowrie.log.closed` |
| `2026-06-09 22:42:21` | `cowrie.session.params` |
| `2026-06-09 22:42:21` | `cowrie.command.input` |
| `2026-06-09 22:42:21` | `cowrie.command.failed` |
| `2026-06-09 22:42:21` | `cowrie.command.failed` |
| `2026-06-09 22:43:22` | `cowrie.session.params` |
| `2026-06-09 22:43:22` | `cowrie.command.input` |
| `2026-06-09 22:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.69.219[.]209` to AbuseIPDB if not already reported
- [ ] Block `152.69.219[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4acb05c5a341

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:04` | `cowrie.session.connect` |
| `2026-06-09 22:44:04` | `cowrie.client.version` |
| `2026-06-09 22:44:04` | `cowrie.client.kex` |
| `2026-06-09 22:44:05` | `cowrie.login.success` |
| `2026-06-09 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859c6680eb50

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:04` | `cowrie.session.connect` |
| `2026-06-09 22:44:04` | `cowrie.client.version` |
| `2026-06-09 22:44:05` | `cowrie.client.kex` |
| `2026-06-09 22:44:05` | `cowrie.login.success` |
| `2026-06-09 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8257a0ebeb5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:05` | `cowrie.session.connect` |
| `2026-06-09 22:44:05` | `cowrie.client.version` |
| `2026-06-09 22:44:05` | `cowrie.client.kex` |
| `2026-06-09 22:44:05` | `cowrie.login.success` |
| `2026-06-09 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61626f749813

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:05` | `cowrie.session.connect` |
| `2026-06-09 22:44:05` | `cowrie.client.version` |
| `2026-06-09 22:44:05` | `cowrie.client.kex` |
| `2026-06-09 22:44:05` | `cowrie.login.success` |
| `2026-06-09 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01bfeca69eb

| Field | Detail |
|---|---|
| **Source IP** | `152.69.219[.]209` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:46 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:38` | `cowrie.session.connect` |
| `2026-06-09 22:44:38` | `cowrie.client.version` |
| `2026-06-09 22:44:39` | `cowrie.client.kex` |
| `2026-06-09 22:44:40` | `cowrie.login.success` |
| `2026-06-09 22:44:42` | `cowrie.session.file_upload` |
| `2026-06-09 22:44:43` | `cowrie.session.params` |
| `2026-06-09 22:44:43` | `cowrie.command.input` |
| `2026-06-09 22:44:43` | `cowrie.command.input` |
| `2026-06-09 22:44:43` | `cowrie.command.input` |
| `2026-06-09 22:44:43` | `cowrie.command.failed` |
| `2026-06-09 22:44:43` | `cowrie.log.closed` |
| `2026-06-09 22:44:44` | `cowrie.session.params` |
| `2026-06-09 22:44:44` | `cowrie.command.input` |
| `2026-06-09 22:44:45` | `cowrie.log.closed` |
| `2026-06-09 22:44:46` | `cowrie.session.params` |
| `2026-06-09 22:44:46` | `cowrie.command.input` |
| `2026-06-09 22:44:46` | `cowrie.log.closed` |
| `2026-06-09 22:44:47` | `cowrie.session.params` |
| `2026-06-09 22:44:47` | `cowrie.command.input` |
| `2026-06-09 22:44:47` | `cowrie.command.failed` |
| `2026-06-09 22:44:47` | `cowrie.command.failed` |
| `2026-06-09 22:45:49` | `cowrie.session.params` |
| `2026-06-09 22:45:49` | `cowrie.command.input` |
| `2026-06-09 22:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.69.219[.]209` to AbuseIPDB if not already reported
- [ ] Block `152.69.219[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731f235c6981

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-09 22:45 |
| **Last Seen** | 2026-06-09 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:45:13` | `cowrie.session.connect` |
| `2026-06-09 22:45:13` | `cowrie.client.version` |
| `2026-06-09 22:45:13` | `cowrie.client.kex` |
| `2026-06-09 22:45:14` | `cowrie.login.success` |
| `2026-06-09 22:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a04fedc35c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-09 22:45 |
| **Last Seen** | 2026-06-09 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:45:13` | `cowrie.session.connect` |
| `2026-06-09 22:45:13` | `cowrie.client.version` |
| `2026-06-09 22:45:13` | `cowrie.client.kex` |
| `2026-06-09 22:45:14` | `cowrie.login.success` |
| `2026-06-09 22:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **14** | 2026-06-09 20:55 | 2026-06-09 22:41 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `117.176.220[.]76` | **2** | 2026-06-09 22:10 | 2026-06-09 22:14 | 4m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]250` | 1 | 2026-06-09 22:02 | 2026-06-09 22:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]41` | 1 | 2026-06-09 22:05 | 2026-06-09 22:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.199.65[.]248` | 1 | 2026-06-09 21:23 | 2026-06-09 21:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]201` | 1 | 2026-06-09 21:09 | 2026-06-09 21:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.0.217[.]26` | 1 | 2026-06-09 21:34 | 2026-06-09 21:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.166.84[.]36` | 1 | 2026-06-09 22:13 | 2026-06-09 22:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.87[.]117` | 1 | 2026-06-09 21:43 | 2026-06-09 21:43 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-06-09 22:11 | 2026-06-09 22:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]96` | 1 | 2026-06-09 22:16 | 2026-06-09 22:16 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `187.199.65[.]248` | MX | UNINET | **100** ⚠️ | 3 |
| `81.19.216[.]96` | NL | Infrawatch Limited | **100** ⚠️ | 19 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `117.176.220[.]76` | CN | China Mobile Communications Corporation | **100** ⚠️ | 36 |
| `195.206.182[.]201` | GB | Infrawatch Limited | **100** ⚠️ | 13 |
| `45.156.87[.]117` | NL | VMHeaven.io | **100** ⚠️ | 23 |
| `213.166.84[.]36` | GB | Infrawatch Limited | **100** ⚠️ | 8 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 4 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 61 cases |
| Tool 34  | Credential Extractor        | ✅ 25 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (18.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 11 recon entry/entries in table (2 group(s) consolidating 16 session(s)).

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
_Report time: 2026-06-09T23:19:30Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-23 |
| **Generated At** | 2026-11-23T04:34:43Z |
| **Shift Time** | 04:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **52** |
| Confirmed Threats | **38** |
| False Positives Filtered | **14** (26.9%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **18** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **33** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **46** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **8** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `admin` | 8 |
| `nobody` | 6 |
| `support` | 4 |
| `git` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 7 |
| `admin` | 6 |
| `root` | 5 |
| `support` | 4 |
| `git` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `` | 6 |
| `root` | `root` | 5 |
| `admin` | `admin` | 5 |
| `support` | `support` | 4 |
| `git` | `git` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-11-23T00:01:55 |
| `root` | `admin` | `45.135.194.105` | 2026-11-23T00:02:43 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-23T00:05:36 |
| `usuario` | `usuario` | `138.226.239.233` | 2026-11-23T00:24:30 |
| `nobody` | `` | `138.226.239.233` | 2026-11-23T00:24:37 |
| `mysql` | `` | `10.0.0.73` | 2026-11-23T00:25:57 |
| `git` | `git` | `10.0.0.73` | 2026-11-23T00:26:38 |
| `nobody` | `` | `10.0.0.73` | 2026-11-23T00:26:39 |
| `admin` | `1qaz2wsx` | `138.226.239.233` | 2026-11-23T00:27:47 |
| `usuario` | `usuario` | `138.226.239.234` | 2026-11-23T00:28:08 |
| `git` | `git` | `138.226.239.234` | 2026-11-23T00:31:11 |
| `root` | `999` | `78.128.112.74` | 2026-11-23T00:50:57 |
| `root` | `abc` | `78.128.112.74` | 2026-11-23T00:50:57 |
| `support` | `support` | `10.0.0.73` | 2026-11-23T01:05:41 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-23T01:08:49 |
| `admin` | `7777` | `10.0.0.73` | 2026-11-23T01:13:25 |
| `root` | `------fuck------` | `192.9.130.35` | 2026-11-23T01:18:30 |
| `root` | `vizxv` | `143.203.219.50` | 2026-11-23T01:59:20 |
| `nobody` | `` | `138.226.239.234` | 2026-11-23T02:40:14 |
| `admin` | `1qaz2wsx` | `138.226.239.234` | 2026-11-23T02:43:58 |
_… 6 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **52** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 17 |
| Unknown | 4 |
| AsyncSSH (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 7 | 2 |
| `7d01d047ace6...` | Mirai/variant | 4 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 3 | 3 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `d1c5d296d532...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 2 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `d1c5d296d532...` | AsyncSSH (Python) | 2 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
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
echo SHELL_TEST_OK
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
Source IPs: `143.203.219.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **16** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS10103` | HK Broadband Network Ltd. | 1 | HIGH |
| `AS8151` | Uninet S.A. de C.V. | 1 | LOW |
| `AS47890` | UNMANAGED LTD | 1 | HIGH |
| `AS207043` | DEDIK SERVICES LIMITED | 1 | HIGH |
| `AS36903` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 1 | LOW |
| `AS211298` | Driftnet Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8dc8bdd69bc4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-23 00:01 |
| **Last Seen** | 2026-11-23 00:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:01:54` | `cowrie.session.connect` |
| `2026-11-23 00:01:54` | `cowrie.client.version` |
| `2026-11-23 00:01:54` | `cowrie.client.kex` |
| `2026-11-23 00:01:55` | `cowrie.login.success` |
| `2026-11-23 00:01:55` | `cowrie.direct-tcpip.request` |
| `2026-11-23 00:01:55` | `cowrie.direct-tcpip.data` |
| `2026-11-23 00:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6303d346e7b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]105` |
| **First Seen** | 2026-11-23 00:02 |
| **Last Seen** | 2026-11-23 00:05 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:02:43` | `cowrie.session.connect` |
| `2026-11-23 00:02:43` | `cowrie.login.success` |
| `2026-11-23 00:02:44` | `cowrie.session.params` |
| `2026-11-23 00:05:44` | `cowrie.log.closed` |
| `2026-11-23 00:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]105` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c1935b4bde

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-23 00:05 |
| **Last Seen** | 2026-11-23 00:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:05:35` | `cowrie.session.connect` |
| `2026-11-23 00:05:36` | `cowrie.login.success` |
| `2026-11-23 00:05:36` | `cowrie.session.params` |
| `2026-11-23 00:05:36` | `cowrie.log.closed` |
| `2026-11-23 00:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a78f327d12f

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-23 00:24 |
| **Last Seen** | 2026-11-23 00:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:24:30` | `cowrie.session.connect` |
| `2026-11-23 00:24:30` | `cowrie.client.version` |
| `2026-11-23 00:24:30` | `cowrie.client.kex` |
| `2026-11-23 00:24:30` | `cowrie.login.success` |
| `2026-11-23 00:24:31` | `cowrie.direct-tcpip.request` |
| `2026-11-23 00:24:31` | `cowrie.direct-tcpip.ja4` |
| `2026-11-23 00:24:31` | `cowrie.direct-tcpip.data` |
| `2026-11-23 00:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75ecd174a7e

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-23 00:28 |
| **Last Seen** | 2026-11-23 00:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:28:07` | `cowrie.session.connect` |
| `2026-11-23 00:28:07` | `cowrie.client.version` |
| `2026-11-23 00:28:08` | `cowrie.client.kex` |
| `2026-11-23 00:28:08` | `cowrie.login.success` |
| `2026-11-23 00:28:08` | `cowrie.direct-tcpip.request` |
| `2026-11-23 00:28:08` | `cowrie.direct-tcpip.ja4` |
| `2026-11-23 00:28:08` | `cowrie.direct-tcpip.data` |
| `2026-11-23 00:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f5c336eb83

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-23 00:50 |
| **Last Seen** | 2026-11-23 00:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 00:50:56` | `cowrie.session.connect` |
| `2026-11-23 00:50:56` | `cowrie.client.version` |
| `2026-11-23 00:50:56` | `cowrie.client.kex` |
| `2026-11-23 00:50:57` | `cowrie.login.success` |
| `2026-11-23 00:50:58` | `cowrie.session.params` |
| `2026-11-23 00:50:58` | `cowrie.command.input` |
| `2026-11-23 00:50:59` | `cowrie.log.closed` |
| `2026-11-23 00:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebed43a8d0a

| Field | Detail |
|---|---|
| **Source IP** | `192.9.130[.]35` |
| **First Seen** | 2026-11-23 01:18 |
| **Last Seen** | 2026-11-23 01:18 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 01:18:20` | `cowrie.session.connect` |
| `2026-11-23 01:18:23` | `cowrie.client.version` |
| `2026-11-23 01:18:23` | `cowrie.client.kex` |
| `2026-11-23 01:18:30` | `cowrie.login.success` |
| `2026-11-23 01:18:33` | `cowrie.session.params` |
| `2026-11-23 01:18:33` | `cowrie.command.input` |
| `2026-11-23 01:18:35` | `cowrie.log.closed` |
| `2026-11-23 01:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.9.130[.]35` to AbuseIPDB if not already reported
- [ ] Block `192.9.130[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283e3e313efb

| Field | Detail |
|---|---|
| **Source IP** | `143.203.219[.]50` |
| **First Seen** | 2026-11-23 01:59 |
| **Last Seen** | 2026-11-23 01:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST_OK, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 01:59:20` | `cowrie.session.connect` |
| `2026-11-23 01:59:20` | `cowrie.login.success` |
| `2026-11-23 01:59:21` | `cowrie.session.params` |
| `2026-11-23 01:59:21` | `cowrie.command.input` |
| `2026-11-23 01:59:23` | `cowrie.command.input` |
| `2026-11-23 01:59:24` | `cowrie.command.input` |
| `2026-11-23 01:59:24` | `cowrie.command.input` |
| `2026-11-23 01:59:24` | `cowrie.command.failed` |
| `2026-11-23 01:59:25` | `cowrie.log.closed` |
| `2026-11-23 01:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.203.219[.]50` to AbuseIPDB if not already reported
- [ ] Block `143.203.219[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd257cd9279d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-23 02:30 |
| **Last Seen** | 2026-11-23 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:30:54` | `cowrie.session.connect` |
| `2026-11-23 02:30:54` | `cowrie.login.success` |
| `2026-11-23 02:30:55` | `cowrie.session.params` |
| `2026-11-23 02:30:55` | `cowrie.log.closed` |
| `2026-11-23 02:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-363c43f7b9be

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-23 02:40 |
| **Last Seen** | 2026-11-23 02:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:40:14` | `cowrie.session.connect` |
| `2026-11-23 02:40:14` | `cowrie.client.version` |
| `2026-11-23 02:40:14` | `cowrie.client.kex` |
| `2026-11-23 02:40:14` | `cowrie.login.success` |
| `2026-11-23 02:40:15` | `cowrie.direct-tcpip.request` |
| `2026-11-23 02:40:15` | `cowrie.direct-tcpip.ja4` |
| `2026-11-23 02:40:15` | `cowrie.direct-tcpip.data` |
| `2026-11-23 02:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdec8ca975ec

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-23 02:43 |
| **Last Seen** | 2026-11-23 02:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:43:05` | `cowrie.session.connect` |
| `2026-11-23 02:43:05` | `cowrie.client.version` |
| `2026-11-23 02:43:05` | `cowrie.client.kex` |
| `2026-11-23 02:43:06` | `cowrie.login.success` |
| `2026-11-23 02:43:06` | `cowrie.direct-tcpip.request` |
| `2026-11-23 02:43:06` | `cowrie.direct-tcpip.ja4` |
| `2026-11-23 02:43:06` | `cowrie.direct-tcpip.data` |
| `2026-11-23 02:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b2f6b0c702

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:45 |
| **Last Seen** | 2026-11-23 02:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_47e761a2686f14d5619c755c748fe9be_small_control'"'"' '"'"'check_47e761a2686f14d5619c755c748fe9be'"'"'', printf '\n%s|%s\n' 'check_47e761a2686f14d5619c755c748fe9be_small_control' 'check_47e761a2686f14d5619c755c748fe9be', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_47e761a2686f14d5619c755c748fe9be_small_math'"'"' "$((462*220+75))"', (462*220+75, printf '\n%s|%s\n' 'check_47e761a2686f14d5619c755c748fe9be_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:45:45` | `cowrie.session.connect` |
| `2026-11-23 02:45:45` | `cowrie.client.version` |
| `2026-11-23 02:45:45` | `cowrie.client.kex` |
| `2026-11-23 02:45:48` | `cowrie.login.success` |
| `2026-11-23 02:45:50` | `cowrie.client.size` |
| `2026-11-23 02:45:51` | `cowrie.session.params` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:51` | `cowrie.command.input` |
| `2026-11-23 02:45:52` | `cowrie.command.input` |
| `2026-11-23 02:45:52` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791118891a33

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:47 |
| **Last Seen** | 2026-11-23 02:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5b4166e93cd62585ea530794c6a96bf_small_control'"'"' '"'"'check_e5b4166e93cd62585ea530794c6a96bf'"'"'', printf '\n%s|%s\n' 'check_e5b4166e93cd62585ea530794c6a96bf_small_control' 'check_e5b4166e93cd62585ea530794c6a96bf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5b4166e93cd62585ea530794c6a96bf_small_math'"'"' "$((979*788+23))"', (979*788+23, printf '\n%s|%s\n' 'check_e5b4166e93cd62585ea530794c6a96bf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:47:59` | `cowrie.session.connect` |
| `2026-11-23 02:48:00` | `cowrie.client.version` |
| `2026-11-23 02:48:00` | `cowrie.client.kex` |
| `2026-11-23 02:48:03` | `cowrie.login.success` |
| `2026-11-23 02:48:05` | `cowrie.client.size` |
| `2026-11-23 02:48:06` | `cowrie.session.params` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| `2026-11-23 02:48:06` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5c9f16be7d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:50 |
| **Last Seen** | 2026-11-23 02:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_342a0177ca43e64b8f92defe59aa607a_small_control'"'"' '"'"'check_342a0177ca43e64b8f92defe59aa607a'"'"'', printf '\n%s|%s\n' 'check_342a0177ca43e64b8f92defe59aa607a_small_control' 'check_342a0177ca43e64b8f92defe59aa607a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_342a0177ca43e64b8f92defe59aa607a_small_math'"'"' "$((394*376+66))"', (394*376+66, printf '\n%s|%s\n' 'check_342a0177ca43e64b8f92defe59aa607a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:50:15` | `cowrie.session.connect` |
| `2026-11-23 02:50:16` | `cowrie.client.version` |
| `2026-11-23 02:50:16` | `cowrie.client.kex` |
| `2026-11-23 02:50:19` | `cowrie.login.success` |
| `2026-11-23 02:50:21` | `cowrie.client.size` |
| `2026-11-23 02:50:21` | `cowrie.session.params` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| `2026-11-23 02:50:22` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5c53533ede

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 02:52 |
| **Last Seen** | 2026-11-23 02:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e817881ea413f80b2b9c10352ed9475_small_control'"'"' '"'"'check_8e817881ea413f80b2b9c10352ed9475'"'"'', printf '\n%s|%s\n' 'check_8e817881ea413f80b2b9c10352ed9475_small_control' 'check_8e817881ea413f80b2b9c10352ed9475', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e817881ea413f80b2b9c10352ed9475_small_math'"'"' "$((590*129+10))"', (590*129+10, printf '\n%s|%s\n' 'check_8e817881ea413f80b2b9c10352ed9475_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:52:38` | `cowrie.session.connect` |
| `2026-11-23 02:52:39` | `cowrie.client.version` |
| `2026-11-23 02:52:39` | `cowrie.client.kex` |
| `2026-11-23 02:52:41` | `cowrie.login.success` |
| `2026-11-23 02:52:43` | `cowrie.client.size` |
| `2026-11-23 02:52:44` | `cowrie.session.params` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| `2026-11-23 02:52:44` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f37de731c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 02:54 |
| **Last Seen** | 2026-11-23 02:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58b7aaf76cf18a4a48c15a7bac38dbe8_small_control'"'"' '"'"'check_58b7aaf76cf18a4a48c15a7bac38dbe8'"'"'', printf '\n%s|%s\n' 'check_58b7aaf76cf18a4a48c15a7bac38dbe8_small_control' 'check_58b7aaf76cf18a4a48c15a7bac38dbe8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58b7aaf76cf18a4a48c15a7bac38dbe8_small_math'"'"' "$((778*164+14))"', (778*164+14, printf '\n%s|%s\n' 'check_58b7aaf76cf18a4a48c15a7bac38dbe8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:54:26` | `cowrie.session.connect` |
| `2026-11-23 02:54:27` | `cowrie.client.version` |
| `2026-11-23 02:54:27` | `cowrie.client.kex` |
| `2026-11-23 02:54:29` | `cowrie.login.success` |
| `2026-11-23 02:54:31` | `cowrie.client.size` |
| `2026-11-23 02:54:32` | `cowrie.session.params` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| `2026-11-23 02:54:32` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88434de1cbcc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:54 |
| **Last Seen** | 2026-11-23 02:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2516296e4c776129b683d5e81a13721b_small_control'"'"' '"'"'check_2516296e4c776129b683d5e81a13721b'"'"'', printf '\n%s|%s\n' 'check_2516296e4c776129b683d5e81a13721b_small_control' 'check_2516296e4c776129b683d5e81a13721b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2516296e4c776129b683d5e81a13721b_small_math'"'"' "$((522*697+86))"', (522*697+86, printf '\n%s|%s\n' 'check_2516296e4c776129b683d5e81a13721b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:54:41` | `cowrie.session.connect` |
| `2026-11-23 02:54:42` | `cowrie.client.version` |
| `2026-11-23 02:54:42` | `cowrie.client.kex` |
| `2026-11-23 02:54:45` | `cowrie.login.success` |
| `2026-11-23 02:54:47` | `cowrie.client.size` |
| `2026-11-23 02:54:48` | `cowrie.session.params` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| `2026-11-23 02:54:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.84.166[.]194` | **2** | 2026-11-23 01:45 | 2026-11-23 02:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-23 00:36 | 2026-11-23 02:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-23 01:51 | 2026-11-23 01:52 | 44s | 0 | `T1592` | 🟢 LOW |
| `143.203.219[.]50` | 1 | 2026-11-23 01:59 | 2026-11-23 01:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.122.54[.]62` | 1 | 2026-11-23 02:33 | 2026-11-23 02:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.9.130[.]35` | 1 | 2026-11-23 01:18 | 2026-11-23 01:18 | 1s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-23 02:52 | 2026-11-23 02:52 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.12.243[.]187` | 1 | 2026-11-23 01:37 | 2026-11-23 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-23 00:59 | 2026-11-23 00:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | 1 | 2026-11-23 01:10 | 2026-11-23 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.205.55[.]240` | 1 | 2026-11-23 01:17 | 2026-11-23 01:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-23 01:12 | 2026-11-23 01:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-11-23 00:55 | 2026-11-23 00:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-23 00:05 | 2026-11-23 00:05 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-23 02:30 | 2026-11-23 02:30 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 00:50 | 2026-11-23 00:51 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.219.222[.]66` | 1 | 2026-11-23 02:46 | 2026-11-23 02:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]250` | 1 | 2026-11-23 01:31 | 2026-11-23 01:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-23 02:44 | 2026-11-23 02:44 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `143.198.208[.]150` | SG | DigitalOcean, LLC | **100** ⚠️ | 32 |
| `64.62.197[.]2` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `77.239.124[.]252` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 26 |
| `165.84.166[.]194` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 2 |
| `143.203.219[.]50` | DE | DEDIK SERVICES LIMITED | **100** ⚠️ | 7 |
| `192.9.130[.]35` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `54.205.55[.]240` | US | Amazon.com, Inc. | **100** ⚠️ | 4 |
| `77.239.124[.]132` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 5 |
| `45.148.10[.]61` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 52 cases |
| Tool 34  | Credential Extractor        | ✅ 46 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (26.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 19 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-23T04:34:43Z_

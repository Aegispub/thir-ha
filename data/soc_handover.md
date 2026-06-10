# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T10:10:33Z |
| **Shift Time** | 10:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1003** |
| Confirmed Threats | **983** |
| False Positives Filtered | **20** (2.0%) |
| Unique Attacker IPs | **52** |
| Countries of Origin | **14** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **923** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **13** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `admin` | 6 |
| `user` | 5 |
| `GET / HTTP/1.1` | 5 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 24 |
| `123@@@` | 11 |
| `smo@@kkklss` | 6 |
| `Host: 129.80.119.236:23` | 4 |
| `` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 24 |
| `root` | `123@@@` | 11 |
| `root` | `smo@@kkklss` | 6 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 4 |
| `root` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `lind` | `2.57.121.25` | 2026-06-10T03:06:52 |
| `kim` | `kim` | `213.209.159.56` | 2026-06-10T03:15:30 |
| `support` | `support` | `2.57.121.112` | 2026-06-10T03:26:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-10T03:26:56 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-10T03:26:56 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-10T03:26:59 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-10T03:34:06 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-10T03:34:08 |
| `root` | `LeitboGi0ro` | `129.153.86.229` | 2026-06-10T03:45:54 |
| `root` | `123@@@` | `129.153.86.229` | 2026-06-10T03:45:54 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-10T03:50:33 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-10T03:50:33 |
| `root` | `LeitboGi0ro` | `129.153.90.200` | 2026-06-10T04:00:30 |
| `root` | `123@@@` | `129.153.90.200` | 2026-06-10T04:00:36 |
| `root` | `` | `176.65.139.41` | 2026-06-10T04:05:15 |
| `user` | `laracrof` | `2.57.121.25` | 2026-06-10T04:22:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.215.249` | 2026-06-10T04:23:46 |
| `*1` | `$4` | `34.79.215.249` | 2026-06-10T04:23:55 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7862` | `34.79.215.249` | 2026-06-10T04:23:57 |
| `pilar` | `pilar` | `213.209.159.56` | 2026-06-10T04:25:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `66.228.53.46` | 2026-06-10T04:29:56 |
| `admin1` | `admin1` | `2.57.121.112` | 2026-06-10T04:42:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.174.174` | 2026-06-10T04:57:57 |
| `*1` | `$4` | `34.78.174.174` | 2026-06-10T04:58:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9046` | `34.78.174.174` | 2026-06-10T04:58:13 |
| `admin` | `admin` | `104.236.83.40` | 2026-06-10T05:01:00 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-10T05:01:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.102` | 2026-06-10T05:27:24 |
| `rileigh` | `rileigh` | `213.209.159.56` | 2026-06-10T05:36:04 |
| `user` | `kochanie` | `2.57.121.25` | 2026-06-10T05:37:26 |
| `root` | `LeitboGi0ro` | `140.245.67.111` | 2026-06-10T05:39:07 |
| `root` | `123@@@` | `140.245.67.111` | 2026-06-10T05:39:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.89.181` | 2026-06-10T05:45:12 |
| `*1` | `$4` | `207.175.89.181` | 2026-06-10T05:45:25 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7192` | `207.175.89.181` | 2026-06-10T05:45:27 |
| `admin` | `1234` | `2.57.121.112` | 2026-06-10T05:58:26 |
| `root` | `` | `176.65.139.214` | 2026-06-10T06:23:54 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-10T06:38:18 |
| `selah` | `selah` | `213.209.159.56` | 2026-06-10T06:46:09 |
| `admin` | `admin` | `34.38.45.137` | 2026-06-10T06:51:06 |
| `user` | `kenya` | `2.57.121.25` | 2026-06-10T06:52:41 |
| `admin` | `admin1234` | `2.57.121.112` | 2026-06-10T07:10:40 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-10T07:13:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-10T07:13:31 |
| `root` | `Pwd@Linux` | `107.173.85.94` | 2026-06-10T07:30:31 |
| `root` | `LeitboGi0ro` | `107.173.85.94` | 2026-06-10T07:30:37 |
| `root` | `cxthhhhh.com` | `107.173.85.94` | 2026-06-10T07:30:46 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-10T07:35:55 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-10T07:35:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-10T07:36:02 |
| `root` | `LeitboGi0ro` | `56.124.92.130` | 2026-06-10T07:55:00 |
| `root` | `MoeClub.org` | `56.124.92.130` | 2026-06-10T07:55:04 |
| `susannah` | `susannah` | `213.209.159.56` | 2026-06-10T07:55:05 |
| `user` | `kapusta` | `2.57.121.25` | 2026-06-10T08:07:31 |
| `root` | `S6J25UaCMg` | `10.0.0.73` | 2026-06-10T08:16:36 |
| `admin` | `Xpon@Olt9417#` | `2.57.121.112` | 2026-06-10T08:21:52 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-10T08:41:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1003** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 38 |
| PuTTY | 16 |
| Go SSH scanner | 15 |
| libssh | 5 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 30 | 6 |
| `57446c12547a...` | Mirai/variant | 15 | 3 |
| `6372ee695756...` | Modern SSH client | 8 | 2 |
| `16443846184e...` | Generic scanner | 7 | 2 |
| `98f63c4d9c87...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 30 | 6 | Mirai/variant |
| `57446c12547a...` | PuTTY | 15 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 7 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 2 | `T1082, T1105, T1059.004` |

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
Source IPs: `176.65.139.214`, `176.65.139.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **52** |
| Unique ASNs | **23** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | HIGH |
| `AS31898` | Oracle Corporation | 8 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS36352` | HostPapa | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS214472` | Offshore LC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8ecb7a6c5c0c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 03:06 |
| **Last Seen** | 2026-06-10 03:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:06:51` | `cowrie.session.connect` |
| `2026-06-10 03:06:51` | `cowrie.client.version` |
| `2026-06-10 03:06:51` | `cowrie.client.kex` |
| `2026-06-10 03:06:52` | `cowrie.login.success` |
| `2026-06-10 03:06:52` | `cowrie.direct-tcpip.request` |
| `2026-06-10 03:06:52` | `cowrie.direct-tcpip.data` |
| `2026-06-10 03:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74695a548955

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 03:15 |
| **Last Seen** | 2026-06-10 03:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:15:30` | `cowrie.session.connect` |
| `2026-06-10 03:15:30` | `cowrie.client.version` |
| `2026-06-10 03:15:30` | `cowrie.client.kex` |
| `2026-06-10 03:15:30` | `cowrie.login.success` |
| `2026-06-10 03:15:30` | `cowrie.direct-tcpip.request` |
| `2026-06-10 03:15:30` | `cowrie.direct-tcpip.data` |
| `2026-06-10 03:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed7748cc1c7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 03:26 |
| **Last Seen** | 2026-06-10 03:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:26:26` | `cowrie.session.connect` |
| `2026-06-10 03:26:26` | `cowrie.client.version` |
| `2026-06-10 03:26:26` | `cowrie.client.kex` |
| `2026-06-10 03:26:27` | `cowrie.login.success` |
| `2026-06-10 03:26:27` | `cowrie.direct-tcpip.request` |
| `2026-06-10 03:26:27` | `cowrie.direct-tcpip.data` |
| `2026-06-10 03:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5064511d0f49

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 03:26 |
| **Last Seen** | 2026-06-10 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:26:56` | `cowrie.session.connect` |
| `2026-06-10 03:26:56` | `cowrie.client.version` |
| `2026-06-10 03:26:56` | `cowrie.client.kex` |
| `2026-06-10 03:26:56` | `cowrie.login.success` |
| `2026-06-10 03:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a48508b7ad

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 03:26 |
| **Last Seen** | 2026-06-10 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:26:56` | `cowrie.session.connect` |
| `2026-06-10 03:26:56` | `cowrie.client.version` |
| `2026-06-10 03:26:56` | `cowrie.client.kex` |
| `2026-06-10 03:26:56` | `cowrie.login.success` |
| `2026-06-10 03:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3873708fca96

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 03:26 |
| **Last Seen** | 2026-06-10 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:26:59` | `cowrie.session.connect` |
| `2026-06-10 03:26:59` | `cowrie.client.version` |
| `2026-06-10 03:26:59` | `cowrie.client.kex` |
| `2026-06-10 03:26:59` | `cowrie.login.success` |
| `2026-06-10 03:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6377b80098

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 03:26 |
| **Last Seen** | 2026-06-10 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:26:59` | `cowrie.session.connect` |
| `2026-06-10 03:26:59` | `cowrie.client.version` |
| `2026-06-10 03:26:59` | `cowrie.client.kex` |
| `2026-06-10 03:26:59` | `cowrie.login.success` |
| `2026-06-10 03:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8907e16892e6

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 03:34 |
| **Last Seen** | 2026-06-10 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:34:05` | `cowrie.session.connect` |
| `2026-06-10 03:34:05` | `cowrie.client.version` |
| `2026-06-10 03:34:05` | `cowrie.client.kex` |
| `2026-06-10 03:34:06` | `cowrie.login.success` |
| `2026-06-10 03:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e28a6a837db

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 03:34 |
| **Last Seen** | 2026-06-10 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:34:06` | `cowrie.session.connect` |
| `2026-06-10 03:34:06` | `cowrie.client.version` |
| `2026-06-10 03:34:07` | `cowrie.client.kex` |
| `2026-06-10 03:34:08` | `cowrie.login.success` |
| `2026-06-10 03:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b60bc23d19b

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 03:34 |
| **Last Seen** | 2026-06-10 03:36 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:34:29` | `cowrie.session.connect` |
| `2026-06-10 03:34:29` | `cowrie.client.version` |
| `2026-06-10 03:34:29` | `cowrie.client.kex` |
| `2026-06-10 03:34:30` | `cowrie.login.success` |
| `2026-06-10 03:34:32` | `cowrie.session.file_upload` |
| `2026-06-10 03:34:33` | `cowrie.session.params` |
| `2026-06-10 03:34:33` | `cowrie.command.input` |
| `2026-06-10 03:34:33` | `cowrie.command.input` |
| `2026-06-10 03:34:33` | `cowrie.command.input` |
| `2026-06-10 03:34:33` | `cowrie.command.failed` |
| `2026-06-10 03:34:34` | `cowrie.log.closed` |
| `2026-06-10 03:34:35` | `cowrie.session.params` |
| `2026-06-10 03:34:35` | `cowrie.command.input` |
| `2026-06-10 03:34:35` | `cowrie.log.closed` |
| `2026-06-10 03:34:36` | `cowrie.session.params` |
| `2026-06-10 03:34:36` | `cowrie.command.input` |
| `2026-06-10 03:34:37` | `cowrie.log.closed` |
| `2026-06-10 03:34:38` | `cowrie.session.params` |
| `2026-06-10 03:34:38` | `cowrie.command.input` |
| `2026-06-10 03:34:38` | `cowrie.command.failed` |
| `2026-06-10 03:34:38` | `cowrie.command.failed` |
| `2026-06-10 03:35:39` | `cowrie.session.params` |
| `2026-06-10 03:35:39` | `cowrie.command.input` |
| `2026-06-10 03:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff1b2a79f8a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 03:36 |
| **Last Seen** | 2026-06-10 03:39 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:36:55` | `cowrie.session.connect` |
| `2026-06-10 03:36:55` | `cowrie.client.version` |
| `2026-06-10 03:36:56` | `cowrie.client.kex` |
| `2026-06-10 03:36:57` | `cowrie.login.success` |
| `2026-06-10 03:36:59` | `cowrie.session.file_upload` |
| `2026-06-10 03:37:00` | `cowrie.session.params` |
| `2026-06-10 03:37:00` | `cowrie.command.input` |
| `2026-06-10 03:37:00` | `cowrie.command.input` |
| `2026-06-10 03:37:00` | `cowrie.command.input` |
| `2026-06-10 03:37:00` | `cowrie.command.failed` |
| `2026-06-10 03:37:00` | `cowrie.log.closed` |
| `2026-06-10 03:37:02` | `cowrie.session.params` |
| `2026-06-10 03:37:02` | `cowrie.command.input` |
| `2026-06-10 03:37:02` | `cowrie.log.closed` |
| `2026-06-10 03:37:03` | `cowrie.session.params` |
| `2026-06-10 03:37:03` | `cowrie.command.input` |
| `2026-06-10 03:37:03` | `cowrie.log.closed` |
| `2026-06-10 03:37:04` | `cowrie.session.params` |
| `2026-06-10 03:37:04` | `cowrie.command.input` |
| `2026-06-10 03:37:04` | `cowrie.command.failed` |
| `2026-06-10 03:37:04` | `cowrie.command.failed` |
| `2026-06-10 03:38:06` | `cowrie.session.params` |
| `2026-06-10 03:38:06` | `cowrie.command.input` |
| `2026-06-10 03:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f319bf84990

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-10 03:45 |
| **Last Seen** | 2026-06-10 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:45:54` | `cowrie.session.connect` |
| `2026-06-10 03:45:54` | `cowrie.client.version` |
| `2026-06-10 03:45:54` | `cowrie.client.kex` |
| `2026-06-10 03:45:54` | `cowrie.login.success` |
| `2026-06-10 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba563accb1ac

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-10 03:45 |
| **Last Seen** | 2026-06-10 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:45:54` | `cowrie.session.connect` |
| `2026-06-10 03:45:54` | `cowrie.client.version` |
| `2026-06-10 03:45:54` | `cowrie.client.kex` |
| `2026-06-10 03:45:54` | `cowrie.login.success` |
| `2026-06-10 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c27aa24db3b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-10 03:46 |
| **Last Seen** | 2026-06-10 03:48 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:46:17` | `cowrie.session.connect` |
| `2026-06-10 03:46:17` | `cowrie.client.version` |
| `2026-06-10 03:46:17` | `cowrie.client.kex` |
| `2026-06-10 03:46:17` | `cowrie.login.success` |
| `2026-06-10 03:46:18` | `cowrie.session.file_upload` |
| `2026-06-10 03:46:18` | `cowrie.session.params` |
| `2026-06-10 03:46:18` | `cowrie.command.input` |
| `2026-06-10 03:46:18` | `cowrie.command.input` |
| `2026-06-10 03:46:18` | `cowrie.command.input` |
| `2026-06-10 03:46:18` | `cowrie.command.failed` |
| `2026-06-10 03:46:19` | `cowrie.log.closed` |
| `2026-06-10 03:46:19` | `cowrie.session.params` |
| `2026-06-10 03:46:19` | `cowrie.command.input` |
| `2026-06-10 03:46:19` | `cowrie.log.closed` |
| `2026-06-10 03:46:20` | `cowrie.session.params` |
| `2026-06-10 03:46:20` | `cowrie.command.input` |
| `2026-06-10 03:46:20` | `cowrie.log.closed` |
| `2026-06-10 03:46:21` | `cowrie.session.params` |
| `2026-06-10 03:46:21` | `cowrie.command.input` |
| `2026-06-10 03:46:21` | `cowrie.command.failed` |
| `2026-06-10 03:46:21` | `cowrie.command.failed` |
| `2026-06-10 03:47:22` | `cowrie.session.params` |
| `2026-06-10 03:47:22` | `cowrie.command.input` |
| `2026-06-10 03:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4b45b84e2e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-10 03:48 |
| **Last Seen** | 2026-06-10 03:50 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:48:37` | `cowrie.session.connect` |
| `2026-06-10 03:48:37` | `cowrie.client.version` |
| `2026-06-10 03:48:37` | `cowrie.client.kex` |
| `2026-06-10 03:48:38` | `cowrie.login.success` |
| `2026-06-10 03:48:39` | `cowrie.session.file_upload` |
| `2026-06-10 03:48:39` | `cowrie.session.params` |
| `2026-06-10 03:48:39` | `cowrie.command.input` |
| `2026-06-10 03:48:39` | `cowrie.command.input` |
| `2026-06-10 03:48:39` | `cowrie.command.input` |
| `2026-06-10 03:48:39` | `cowrie.command.failed` |
| `2026-06-10 03:48:39` | `cowrie.log.closed` |
| `2026-06-10 03:48:40` | `cowrie.session.params` |
| `2026-06-10 03:48:40` | `cowrie.command.input` |
| `2026-06-10 03:48:40` | `cowrie.log.closed` |
| `2026-06-10 03:48:41` | `cowrie.session.params` |
| `2026-06-10 03:48:41` | `cowrie.command.input` |
| `2026-06-10 03:48:41` | `cowrie.log.closed` |
| `2026-06-10 03:48:42` | `cowrie.session.params` |
| `2026-06-10 03:48:42` | `cowrie.command.input` |
| `2026-06-10 03:48:42` | `cowrie.command.failed` |
| `2026-06-10 03:48:42` | `cowrie.command.failed` |
| `2026-06-10 03:49:42` | `cowrie.session.params` |
| `2026-06-10 03:49:42` | `cowrie.command.input` |
| `2026-06-10 03:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2b3458765b

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 03:50 |
| **Last Seen** | 2026-06-10 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:50:32` | `cowrie.session.connect` |
| `2026-06-10 03:50:32` | `cowrie.client.version` |
| `2026-06-10 03:50:32` | `cowrie.client.kex` |
| `2026-06-10 03:50:33` | `cowrie.login.success` |
| `2026-06-10 03:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce1ebbceb6f

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 03:50 |
| **Last Seen** | 2026-06-10 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:50:32` | `cowrie.session.connect` |
| `2026-06-10 03:50:32` | `cowrie.client.version` |
| `2026-06-10 03:50:33` | `cowrie.client.kex` |
| `2026-06-10 03:50:33` | `cowrie.login.success` |
| `2026-06-10 03:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e625297a1f

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 03:50 |
| **Last Seen** | 2026-06-10 03:53 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:50:51` | `cowrie.session.connect` |
| `2026-06-10 03:50:51` | `cowrie.client.version` |
| `2026-06-10 03:50:51` | `cowrie.client.kex` |
| `2026-06-10 03:50:51` | `cowrie.login.success` |
| `2026-06-10 03:50:53` | `cowrie.session.file_upload` |
| `2026-06-10 03:50:53` | `cowrie.session.params` |
| `2026-06-10 03:50:53` | `cowrie.command.input` |
| `2026-06-10 03:50:53` | `cowrie.command.input` |
| `2026-06-10 03:50:53` | `cowrie.command.input` |
| `2026-06-10 03:50:53` | `cowrie.command.failed` |
| `2026-06-10 03:50:53` | `cowrie.log.closed` |
| `2026-06-10 03:50:54` | `cowrie.session.params` |
| `2026-06-10 03:50:54` | `cowrie.command.input` |
| `2026-06-10 03:50:54` | `cowrie.log.closed` |
| `2026-06-10 03:50:55` | `cowrie.session.params` |
| `2026-06-10 03:50:55` | `cowrie.command.input` |
| `2026-06-10 03:50:55` | `cowrie.log.closed` |
| `2026-06-10 03:50:56` | `cowrie.session.params` |
| `2026-06-10 03:50:56` | `cowrie.command.input` |
| `2026-06-10 03:50:56` | `cowrie.command.failed` |
| `2026-06-10 03:50:56` | `cowrie.command.failed` |
| `2026-06-10 03:51:57` | `cowrie.session.params` |
| `2026-06-10 03:51:57` | `cowrie.command.input` |
| `2026-06-10 03:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe216b2df355

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 03:53 |
| **Last Seen** | 2026-06-10 03:55 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 03:53:23` | `cowrie.session.connect` |
| `2026-06-10 03:53:23` | `cowrie.client.version` |
| `2026-06-10 03:53:23` | `cowrie.client.kex` |
| `2026-06-10 03:53:24` | `cowrie.login.success` |
| `2026-06-10 03:53:25` | `cowrie.session.file_upload` |
| `2026-06-10 03:53:26` | `cowrie.session.params` |
| `2026-06-10 03:53:26` | `cowrie.command.input` |
| `2026-06-10 03:53:26` | `cowrie.command.input` |
| `2026-06-10 03:53:26` | `cowrie.command.input` |
| `2026-06-10 03:53:26` | `cowrie.command.failed` |
| `2026-06-10 03:53:26` | `cowrie.log.closed` |
| `2026-06-10 03:53:27` | `cowrie.session.params` |
| `2026-06-10 03:53:27` | `cowrie.command.input` |
| `2026-06-10 03:53:27` | `cowrie.log.closed` |
| `2026-06-10 03:53:27` | `cowrie.session.params` |
| `2026-06-10 03:53:27` | `cowrie.command.input` |
| `2026-06-10 03:53:27` | `cowrie.log.closed` |
| `2026-06-10 03:53:28` | `cowrie.session.params` |
| `2026-06-10 03:53:28` | `cowrie.command.input` |
| `2026-06-10 03:53:28` | `cowrie.command.failed` |
| `2026-06-10 03:53:28` | `cowrie.command.failed` |
| `2026-06-10 03:54:29` | `cowrie.session.params` |
| `2026-06-10 03:54:29` | `cowrie.command.input` |
| `2026-06-10 03:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a3f5f33d17

| Field | Detail |
|---|---|
| **Source IP** | `129.153.90[.]200` |
| **First Seen** | 2026-06-10 04:00 |
| **Last Seen** | 2026-06-10 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:00:29` | `cowrie.session.connect` |
| `2026-06-10 04:00:29` | `cowrie.client.version` |
| `2026-06-10 04:00:30` | `cowrie.client.kex` |
| `2026-06-10 04:00:30` | `cowrie.login.success` |
| `2026-06-10 04:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.90[.]200` to AbuseIPDB if not already reported
- [ ] Block `129.153.90[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6fc0e26a97

| Field | Detail |
|---|---|
| **Source IP** | `129.153.90[.]200` |
| **First Seen** | 2026-06-10 04:00 |
| **Last Seen** | 2026-06-10 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:00:36` | `cowrie.session.connect` |
| `2026-06-10 04:00:36` | `cowrie.client.version` |
| `2026-06-10 04:00:36` | `cowrie.client.kex` |
| `2026-06-10 04:00:36` | `cowrie.login.success` |
| `2026-06-10 04:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.90[.]200` to AbuseIPDB if not already reported
- [ ] Block `129.153.90[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94776fc4a1c8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.90[.]200` |
| **First Seen** | 2026-06-10 04:00 |
| **Last Seen** | 2026-06-10 04:02 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:00:50` | `cowrie.session.connect` |
| `2026-06-10 04:00:50` | `cowrie.client.version` |
| `2026-06-10 04:00:50` | `cowrie.client.kex` |
| `2026-06-10 04:00:50` | `cowrie.login.success` |
| `2026-06-10 04:00:51` | `cowrie.session.file_upload` |
| `2026-06-10 04:00:52` | `cowrie.session.params` |
| `2026-06-10 04:00:52` | `cowrie.command.input` |
| `2026-06-10 04:00:52` | `cowrie.command.input` |
| `2026-06-10 04:00:52` | `cowrie.command.input` |
| `2026-06-10 04:00:52` | `cowrie.command.failed` |
| `2026-06-10 04:00:52` | `cowrie.log.closed` |
| `2026-06-10 04:00:53` | `cowrie.session.params` |
| `2026-06-10 04:00:53` | `cowrie.command.input` |
| `2026-06-10 04:00:53` | `cowrie.log.closed` |
| `2026-06-10 04:00:53` | `cowrie.session.params` |
| `2026-06-10 04:00:53` | `cowrie.command.input` |
| `2026-06-10 04:00:54` | `cowrie.log.closed` |
| `2026-06-10 04:00:54` | `cowrie.session.params` |
| `2026-06-10 04:00:54` | `cowrie.command.input` |
| `2026-06-10 04:00:54` | `cowrie.command.failed` |
| `2026-06-10 04:00:54` | `cowrie.command.failed` |
| `2026-06-10 04:01:55` | `cowrie.session.params` |
| `2026-06-10 04:01:55` | `cowrie.command.input` |
| `2026-06-10 04:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.90[.]200` to AbuseIPDB if not already reported
- [ ] Block `129.153.90[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb54a9002343

| Field | Detail |
|---|---|
| **Source IP** | `129.153.90[.]200` |
| **First Seen** | 2026-06-10 04:03 |
| **Last Seen** | 2026-06-10 04:05 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:03:11` | `cowrie.session.connect` |
| `2026-06-10 04:03:11` | `cowrie.client.version` |
| `2026-06-10 04:03:11` | `cowrie.client.kex` |
| `2026-06-10 04:03:11` | `cowrie.login.success` |
| `2026-06-10 04:03:12` | `cowrie.session.file_upload` |
| `2026-06-10 04:03:13` | `cowrie.session.params` |
| `2026-06-10 04:03:13` | `cowrie.command.input` |
| `2026-06-10 04:03:13` | `cowrie.command.input` |
| `2026-06-10 04:03:13` | `cowrie.command.input` |
| `2026-06-10 04:03:13` | `cowrie.command.failed` |
| `2026-06-10 04:03:13` | `cowrie.log.closed` |
| `2026-06-10 04:03:13` | `cowrie.session.params` |
| `2026-06-10 04:03:13` | `cowrie.command.input` |
| `2026-06-10 04:03:13` | `cowrie.log.closed` |
| `2026-06-10 04:03:14` | `cowrie.session.params` |
| `2026-06-10 04:03:14` | `cowrie.command.input` |
| `2026-06-10 04:03:14` | `cowrie.log.closed` |
| `2026-06-10 04:03:15` | `cowrie.session.params` |
| `2026-06-10 04:03:15` | `cowrie.command.input` |
| `2026-06-10 04:03:15` | `cowrie.command.failed` |
| `2026-06-10 04:03:15` | `cowrie.command.failed` |
| `2026-06-10 04:04:16` | `cowrie.session.params` |
| `2026-06-10 04:04:16` | `cowrie.command.input` |
| `2026-06-10 04:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.90[.]200` to AbuseIPDB if not already reported
- [ ] Block `129.153.90[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a209849185

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]41` |
| **First Seen** | 2026-06-10 04:05 |
| **Last Seen** | 2026-06-10 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:05:14` | `cowrie.session.connect` |
| `2026-06-10 04:05:15` | `cowrie.login.success` |
| `2026-06-10 04:05:16` | `cowrie.session.params` |
| `2026-06-10 04:05:16` | `cowrie.command.input` |
| `2026-06-10 04:05:16` | `cowrie.command.input` |
| `2026-06-10 04:05:17` | `cowrie.command.input` |
| `2026-06-10 04:05:18` | `cowrie.command.input` |
| `2026-06-10 04:05:18` | `cowrie.command.failed` |
| `2026-06-10 04:05:18` | `cowrie.log.closed` |
| `2026-06-10 04:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]41` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd223a4482a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 04:22 |
| **Last Seen** | 2026-06-10 04:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:22:06` | `cowrie.session.connect` |
| `2026-06-10 04:22:06` | `cowrie.client.version` |
| `2026-06-10 04:22:06` | `cowrie.client.kex` |
| `2026-06-10 04:22:07` | `cowrie.login.success` |
| `2026-06-10 04:22:07` | `cowrie.direct-tcpip.request` |
| `2026-06-10 04:22:07` | `cowrie.direct-tcpip.data` |
| `2026-06-10 04:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fde7d218b51

| Field | Detail |
|---|---|
| **Source IP** | `34.79.215[.]249` |
| **First Seen** | 2026-06-10 04:23 |
| **Last Seen** | 2026-06-10 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:23:46` | `cowrie.session.connect` |
| `2026-06-10 04:23:46` | `cowrie.login.success` |
| `2026-06-10 04:23:47` | `cowrie.session.params` |
| `2026-06-10 04:23:47` | `cowrie.command.input` |
| `2026-06-10 04:23:47` | `cowrie.command.input` |
| `2026-06-10 04:23:47` | `cowrie.command.failed` |
| `2026-06-10 04:23:47` | `cowrie.command.input` |
| `2026-06-10 04:23:47` | `cowrie.log.closed` |
| `2026-06-10 04:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.215[.]249` to AbuseIPDB if not already reported
- [ ] Block `34.79.215[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d45d01452b6

| Field | Detail |
|---|---|
| **Source IP** | `34.79.215[.]249` |
| **First Seen** | 2026-06-10 04:23 |
| **Last Seen** | 2026-06-10 04:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:23:55` | `cowrie.session.connect` |
| `2026-06-10 04:23:55` | `cowrie.login.success` |
| `2026-06-10 04:23:55` | `cowrie.session.params` |
| `2026-06-10 04:23:55` | `cowrie.command.input` |
| `2026-06-10 04:23:55` | `cowrie.command.failed` |
| `2026-06-10 04:24:04` | `cowrie.log.closed` |
| `2026-06-10 04:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.215[.]249` to AbuseIPDB if not already reported
- [ ] Block `34.79.215[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48aeaaf3f234

| Field | Detail |
|---|---|
| **Source IP** | `34.79.215[.]249` |
| **First Seen** | 2026-06-10 04:23 |
| **Last Seen** | 2026-06-10 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:23:57` | `cowrie.session.connect` |
| `2026-06-10 04:23:57` | `cowrie.login.success` |
| `2026-06-10 04:23:57` | `cowrie.session.params` |
| `2026-06-10 04:23:57` | `cowrie.command.input` |
| `2026-06-10 04:24:04` | `cowrie.log.closed` |
| `2026-06-10 04:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.215[.]249` to AbuseIPDB if not already reported
- [ ] Block `34.79.215[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9406a85ffe89

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 04:25 |
| **Last Seen** | 2026-06-10 04:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:25:51` | `cowrie.session.connect` |
| `2026-06-10 04:25:51` | `cowrie.client.version` |
| `2026-06-10 04:25:52` | `cowrie.client.kex` |
| `2026-06-10 04:25:52` | `cowrie.login.success` |
| `2026-06-10 04:25:52` | `cowrie.direct-tcpip.request` |
| `2026-06-10 04:25:52` | `cowrie.direct-tcpip.data` |
| `2026-06-10 04:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2e775334c6

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]46` |
| **First Seen** | 2026-06-10 04:29 |
| **Last Seen** | 2026-06-10 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:29:56` | `cowrie.session.connect` |
| `2026-06-10 04:29:56` | `cowrie.login.success` |
| `2026-06-10 04:29:56` | `cowrie.session.params` |
| `2026-06-10 04:29:56` | `cowrie.command.input` |
| `2026-06-10 04:29:56` | `cowrie.command.input` |
| `2026-06-10 04:29:56` | `cowrie.command.failed` |
| `2026-06-10 04:29:56` | `cowrie.command.input` |
| `2026-06-10 04:29:56` | `cowrie.command.failed` |
| `2026-06-10 04:29:56` | `cowrie.command.input` |
| `2026-06-10 04:29:56` | `cowrie.log.closed` |
| `2026-06-10 04:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]46` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e49d147627f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 04:41 |
| **Last Seen** | 2026-06-10 04:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:41:59` | `cowrie.session.connect` |
| `2026-06-10 04:41:59` | `cowrie.client.version` |
| `2026-06-10 04:41:59` | `cowrie.client.kex` |
| `2026-06-10 04:42:00` | `cowrie.login.success` |
| `2026-06-10 04:42:00` | `cowrie.direct-tcpip.request` |
| `2026-06-10 04:42:00` | `cowrie.direct-tcpip.data` |
| `2026-06-10 04:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41b2b859bd5

| Field | Detail |
|---|---|
| **Source IP** | `34.78.174[.]174` |
| **First Seen** | 2026-06-10 04:57 |
| **Last Seen** | 2026-06-10 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:57:57` | `cowrie.session.connect` |
| `2026-06-10 04:57:57` | `cowrie.login.success` |
| `2026-06-10 04:57:58` | `cowrie.session.params` |
| `2026-06-10 04:57:58` | `cowrie.command.input` |
| `2026-06-10 04:57:58` | `cowrie.command.input` |
| `2026-06-10 04:57:58` | `cowrie.command.failed` |
| `2026-06-10 04:57:58` | `cowrie.command.input` |
| `2026-06-10 04:57:58` | `cowrie.log.closed` |
| `2026-06-10 04:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.174[.]174` to AbuseIPDB if not already reported
- [ ] Block `34.78.174[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0cabad94c5

| Field | Detail |
|---|---|
| **Source IP** | `34.78.174[.]174` |
| **First Seen** | 2026-06-10 04:58 |
| **Last Seen** | 2026-06-10 04:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:58:11` | `cowrie.session.connect` |
| `2026-06-10 04:58:11` | `cowrie.login.success` |
| `2026-06-10 04:58:11` | `cowrie.session.params` |
| `2026-06-10 04:58:11` | `cowrie.command.input` |
| `2026-06-10 04:58:11` | `cowrie.command.failed` |
| `2026-06-10 04:58:15` | `cowrie.log.closed` |
| `2026-06-10 04:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.174[.]174` to AbuseIPDB if not already reported
- [ ] Block `34.78.174[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c4acd42dc0

| Field | Detail |
|---|---|
| **Source IP** | `34.78.174[.]174` |
| **First Seen** | 2026-06-10 04:58 |
| **Last Seen** | 2026-06-10 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:58:13` | `cowrie.session.connect` |
| `2026-06-10 04:58:13` | `cowrie.login.success` |
| `2026-06-10 04:58:13` | `cowrie.session.params` |
| `2026-06-10 04:58:13` | `cowrie.command.input` |
| `2026-06-10 04:58:15` | `cowrie.log.closed` |
| `2026-06-10 04:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.174[.]174` to AbuseIPDB if not already reported
- [ ] Block `34.78.174[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3b80e2f923

| Field | Detail |
|---|---|
| **Source IP** | `104.236.83[.]40` |
| **First Seen** | 2026-06-10 05:01 |
| **Last Seen** | 2026-06-10 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:01:00` | `cowrie.session.connect` |
| `2026-06-10 05:01:00` | `cowrie.client.version` |
| `2026-06-10 05:01:00` | `cowrie.client.kex` |
| `2026-06-10 05:01:00` | `cowrie.login.success` |
| `2026-06-10 05:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.83[.]40` to AbuseIPDB if not already reported
- [ ] Block `104.236.83[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6860e1b1d866

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-10 05:01 |
| **Last Seen** | 2026-06-10 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:01:00` | `cowrie.session.connect` |
| `2026-06-10 05:01:00` | `cowrie.client.version` |
| `2026-06-10 05:01:00` | `cowrie.client.kex` |
| `2026-06-10 05:01:01` | `cowrie.login.success` |
| `2026-06-10 05:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6d5dc01d3e

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 05:36 |
| **Last Seen** | 2026-06-10 05:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:36:03` | `cowrie.session.connect` |
| `2026-06-10 05:36:03` | `cowrie.client.version` |
| `2026-06-10 05:36:03` | `cowrie.client.kex` |
| `2026-06-10 05:36:04` | `cowrie.login.success` |
| `2026-06-10 05:36:04` | `cowrie.direct-tcpip.request` |
| `2026-06-10 05:36:04` | `cowrie.direct-tcpip.data` |
| `2026-06-10 05:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9156f115396

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 05:37 |
| **Last Seen** | 2026-06-10 05:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:37:25` | `cowrie.session.connect` |
| `2026-06-10 05:37:25` | `cowrie.client.version` |
| `2026-06-10 05:37:25` | `cowrie.client.kex` |
| `2026-06-10 05:37:26` | `cowrie.login.success` |
| `2026-06-10 05:37:26` | `cowrie.direct-tcpip.request` |
| `2026-06-10 05:37:26` | `cowrie.direct-tcpip.data` |
| `2026-06-10 05:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94cafa8cd69

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-10 05:39 |
| **Last Seen** | 2026-06-10 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:39:06` | `cowrie.session.connect` |
| `2026-06-10 05:39:06` | `cowrie.client.version` |
| `2026-06-10 05:39:06` | `cowrie.client.kex` |
| `2026-06-10 05:39:07` | `cowrie.login.success` |
| `2026-06-10 05:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae10c42abcf0

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-10 05:39 |
| **Last Seen** | 2026-06-10 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:39:06` | `cowrie.session.connect` |
| `2026-06-10 05:39:06` | `cowrie.client.version` |
| `2026-06-10 05:39:07` | `cowrie.client.kex` |
| `2026-06-10 05:39:07` | `cowrie.login.success` |
| `2026-06-10 05:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25ac097b114

| Field | Detail |
|---|---|
| **Source IP** | `207.175.89[.]181` |
| **First Seen** | 2026-06-10 05:45 |
| **Last Seen** | 2026-06-10 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:45:12` | `cowrie.session.connect` |
| `2026-06-10 05:45:12` | `cowrie.login.success` |
| `2026-06-10 05:45:12` | `cowrie.session.params` |
| `2026-06-10 05:45:12` | `cowrie.command.input` |
| `2026-06-10 05:45:12` | `cowrie.command.input` |
| `2026-06-10 05:45:12` | `cowrie.command.failed` |
| `2026-06-10 05:45:12` | `cowrie.command.input` |
| `2026-06-10 05:45:12` | `cowrie.log.closed` |
| `2026-06-10 05:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.89[.]181` to AbuseIPDB if not already reported
- [ ] Block `207.175.89[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea17efde8e9f

| Field | Detail |
|---|---|
| **Source IP** | `207.175.89[.]181` |
| **First Seen** | 2026-06-10 05:45 |
| **Last Seen** | 2026-06-10 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:45:25` | `cowrie.session.connect` |
| `2026-06-10 05:45:25` | `cowrie.login.success` |
| `2026-06-10 05:45:26` | `cowrie.session.params` |
| `2026-06-10 05:45:26` | `cowrie.command.input` |
| `2026-06-10 05:45:26` | `cowrie.command.failed` |
| `2026-06-10 05:45:26` | `cowrie.log.closed` |
| `2026-06-10 05:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.89[.]181` to AbuseIPDB if not already reported
- [ ] Block `207.175.89[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4f39842744

| Field | Detail |
|---|---|
| **Source IP** | `207.175.89[.]181` |
| **First Seen** | 2026-06-10 05:45 |
| **Last Seen** | 2026-06-10 05:45 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:45:27` | `cowrie.session.connect` |
| `2026-06-10 05:45:27` | `cowrie.login.success` |
| `2026-06-10 05:45:28` | `cowrie.session.params` |
| `2026-06-10 05:45:28` | `cowrie.command.input` |
| `2026-06-10 05:45:44` | `cowrie.log.closed` |
| `2026-06-10 05:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.89[.]181` to AbuseIPDB if not already reported
- [ ] Block `207.175.89[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572d62c2bd7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 05:58 |
| **Last Seen** | 2026-06-10 05:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:58:25` | `cowrie.session.connect` |
| `2026-06-10 05:58:25` | `cowrie.client.version` |
| `2026-06-10 05:58:25` | `cowrie.client.kex` |
| `2026-06-10 05:58:26` | `cowrie.login.success` |
| `2026-06-10 05:58:26` | `cowrie.direct-tcpip.request` |
| `2026-06-10 05:58:26` | `cowrie.direct-tcpip.data` |
| `2026-06-10 05:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a993ed238860

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:21:37` | `cowrie.session.connect` |
| `2026-06-10 06:21:37` | `cowrie.client.version` |
| `2026-06-10 06:21:37` | `cowrie.client.kex` |
| `2026-06-10 06:21:37` | `cowrie.login.success` |
| `2026-06-10 06:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106ad13cad82

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:21:38` | `cowrie.session.connect` |
| `2026-06-10 06:21:38` | `cowrie.client.version` |
| `2026-06-10 06:21:38` | `cowrie.client.kex` |
| `2026-06-10 06:21:38` | `cowrie.login.success` |
| `2026-06-10 06:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e69ba045f60

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:21:46` | `cowrie.session.connect` |
| `2026-06-10 06:21:46` | `cowrie.client.version` |
| `2026-06-10 06:21:46` | `cowrie.client.kex` |
| `2026-06-10 06:21:46` | `cowrie.login.success` |
| `2026-06-10 06:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5200409f38

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:21:46` | `cowrie.session.connect` |
| `2026-06-10 06:21:46` | `cowrie.client.version` |
| `2026-06-10 06:21:46` | `cowrie.client.kex` |
| `2026-06-10 06:21:46` | `cowrie.login.success` |
| `2026-06-10 06:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4458c9ead9f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]214` |
| **First Seen** | 2026-06-10 06:23 |
| **Last Seen** | 2026-06-10 06:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:23:53` | `cowrie.session.connect` |
| `2026-06-10 06:23:54` | `cowrie.login.success` |
| `2026-06-10 06:23:54` | `cowrie.session.params` |
| `2026-06-10 06:23:55` | `cowrie.command.input` |
| `2026-06-10 06:23:55` | `cowrie.command.input` |
| `2026-06-10 06:23:56` | `cowrie.command.input` |
| `2026-06-10 06:23:56` | `cowrie.command.input` |
| `2026-06-10 06:23:56` | `cowrie.command.failed` |
| `2026-06-10 06:23:57` | `cowrie.log.closed` |
| `2026-06-10 06:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]214` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d0ce92db6f

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 06:46 |
| **Last Seen** | 2026-06-10 06:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:46:08` | `cowrie.session.connect` |
| `2026-06-10 06:46:08` | `cowrie.client.version` |
| `2026-06-10 06:46:08` | `cowrie.client.kex` |
| `2026-06-10 06:46:09` | `cowrie.login.success` |
| `2026-06-10 06:46:09` | `cowrie.direct-tcpip.request` |
| `2026-06-10 06:46:09` | `cowrie.direct-tcpip.data` |
| `2026-06-10 06:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d006bedf3120

| Field | Detail |
|---|---|
| **Source IP** | `34.38.45[.]137` |
| **First Seen** | 2026-06-10 06:51 |
| **Last Seen** | 2026-06-10 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:51:03` | `cowrie.session.connect` |
| `2026-06-10 06:51:03` | `cowrie.client.version` |
| `2026-06-10 06:51:04` | `cowrie.client.kex` |
| `2026-06-10 06:51:06` | `cowrie.login.success` |
| `2026-06-10 06:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.45[.]137` to AbuseIPDB if not already reported
- [ ] Block `34.38.45[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8243a7e13a7d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 06:52 |
| **Last Seen** | 2026-06-10 06:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:52:40` | `cowrie.session.connect` |
| `2026-06-10 06:52:40` | `cowrie.client.version` |
| `2026-06-10 06:52:40` | `cowrie.client.kex` |
| `2026-06-10 06:52:41` | `cowrie.login.success` |
| `2026-06-10 06:52:41` | `cowrie.direct-tcpip.request` |
| `2026-06-10 06:52:41` | `cowrie.direct-tcpip.data` |
| `2026-06-10 06:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40e3752ec36

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 07:10 |
| **Last Seen** | 2026-06-10 07:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:10:40` | `cowrie.session.connect` |
| `2026-06-10 07:10:40` | `cowrie.client.version` |
| `2026-06-10 07:10:40` | `cowrie.client.kex` |
| `2026-06-10 07:10:40` | `cowrie.login.success` |
| `2026-06-10 07:10:40` | `cowrie.direct-tcpip.request` |
| `2026-06-10 07:10:40` | `cowrie.direct-tcpip.data` |
| `2026-06-10 07:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d84ad373aaa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 07:13 |
| **Last Seen** | 2026-06-10 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:13:29` | `cowrie.session.connect` |
| `2026-06-10 07:13:29` | `cowrie.client.version` |
| `2026-06-10 07:13:30` | `cowrie.client.kex` |
| `2026-06-10 07:13:31` | `cowrie.login.success` |
| `2026-06-10 07:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879f2c36b0bf

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 07:13 |
| **Last Seen** | 2026-06-10 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:13:30` | `cowrie.session.connect` |
| `2026-06-10 07:13:30` | `cowrie.client.version` |
| `2026-06-10 07:13:30` | `cowrie.client.kex` |
| `2026-06-10 07:13:31` | `cowrie.login.success` |
| `2026-06-10 07:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ab1ad9e4b4

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-10 07:30 |
| **Last Seen** | 2026-06-10 07:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:30:31` | `cowrie.session.connect` |
| `2026-06-10 07:30:31` | `cowrie.client.version` |
| `2026-06-10 07:30:31` | `cowrie.client.kex` |
| `2026-06-10 07:30:31` | `cowrie.login.success` |
| `2026-06-10 07:30:32` | `cowrie.session.params` |
| `2026-06-10 07:30:32` | `cowrie.command.input` |
| `2026-06-10 07:30:32` | `cowrie.log.closed` |
| `2026-06-10 07:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5463657ad0

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-10 07:30 |
| **Last Seen** | 2026-06-10 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:30:36` | `cowrie.session.connect` |
| `2026-06-10 07:30:36` | `cowrie.client.version` |
| `2026-06-10 07:30:36` | `cowrie.client.kex` |
| `2026-06-10 07:30:37` | `cowrie.login.success` |
| `2026-06-10 07:30:37` | `cowrie.session.params` |
| `2026-06-10 07:30:37` | `cowrie.command.input` |
| `2026-06-10 07:30:37` | `cowrie.log.closed` |
| `2026-06-10 07:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5919b3daff0d

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-06-10 07:30 |
| **Last Seen** | 2026-06-10 07:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:30:44` | `cowrie.session.connect` |
| `2026-06-10 07:30:45` | `cowrie.client.version` |
| `2026-06-10 07:30:45` | `cowrie.client.kex` |
| `2026-06-10 07:30:46` | `cowrie.login.success` |
| `2026-06-10 07:30:46` | `cowrie.session.params` |
| `2026-06-10 07:30:46` | `cowrie.command.input` |
| `2026-06-10 07:30:47` | `cowrie.log.closed` |
| `2026-06-10 07:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6379cb4d3d5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 07:35 |
| **Last Seen** | 2026-06-10 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:35:55` | `cowrie.session.connect` |
| `2026-06-10 07:35:55` | `cowrie.client.version` |
| `2026-06-10 07:35:55` | `cowrie.client.kex` |
| `2026-06-10 07:35:55` | `cowrie.login.success` |
| `2026-06-10 07:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d4fa557fb3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 07:35 |
| **Last Seen** | 2026-06-10 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:35:55` | `cowrie.session.connect` |
| `2026-06-10 07:35:55` | `cowrie.client.version` |
| `2026-06-10 07:35:55` | `cowrie.client.kex` |
| `2026-06-10 07:35:55` | `cowrie.login.success` |
| `2026-06-10 07:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78bbcd9dcbf1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 07:36 |
| **Last Seen** | 2026-06-10 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:36:01` | `cowrie.session.connect` |
| `2026-06-10 07:36:01` | `cowrie.client.version` |
| `2026-06-10 07:36:01` | `cowrie.client.kex` |
| `2026-06-10 07:36:02` | `cowrie.login.success` |
| `2026-06-10 07:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cad7c3a899b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 07:36 |
| **Last Seen** | 2026-06-10 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:36:02` | `cowrie.session.connect` |
| `2026-06-10 07:36:02` | `cowrie.client.version` |
| `2026-06-10 07:36:02` | `cowrie.client.kex` |
| `2026-06-10 07:36:03` | `cowrie.login.success` |
| `2026-06-10 07:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daee165862ce

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 07:51 |
| **Last Seen** | 2026-06-10 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:51:01` | `cowrie.session.connect` |
| `2026-06-10 07:51:01` | `cowrie.client.version` |
| `2026-06-10 07:51:01` | `cowrie.client.kex` |
| `2026-06-10 07:51:02` | `cowrie.login.success` |
| `2026-06-10 07:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78e4061bd9e

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 07:51 |
| **Last Seen** | 2026-06-10 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:51:01` | `cowrie.session.connect` |
| `2026-06-10 07:51:01` | `cowrie.client.version` |
| `2026-06-10 07:51:01` | `cowrie.client.kex` |
| `2026-06-10 07:51:02` | `cowrie.login.success` |
| `2026-06-10 07:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4706e94fb8a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 07:51 |
| **Last Seen** | 2026-06-10 07:53 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:51:20` | `cowrie.session.connect` |
| `2026-06-10 07:51:20` | `cowrie.client.version` |
| `2026-06-10 07:51:21` | `cowrie.client.kex` |
| `2026-06-10 07:51:22` | `cowrie.login.success` |
| `2026-06-10 07:51:24` | `cowrie.session.file_upload` |
| `2026-06-10 07:51:25` | `cowrie.session.params` |
| `2026-06-10 07:51:25` | `cowrie.command.input` |
| `2026-06-10 07:51:25` | `cowrie.command.input` |
| `2026-06-10 07:51:25` | `cowrie.command.input` |
| `2026-06-10 07:51:25` | `cowrie.command.failed` |
| `2026-06-10 07:51:25` | `cowrie.log.closed` |
| `2026-06-10 07:51:26` | `cowrie.session.params` |
| `2026-06-10 07:51:26` | `cowrie.command.input` |
| `2026-06-10 07:51:27` | `cowrie.log.closed` |
| `2026-06-10 07:51:28` | `cowrie.session.params` |
| `2026-06-10 07:51:28` | `cowrie.command.input` |
| `2026-06-10 07:51:28` | `cowrie.log.closed` |
| `2026-06-10 07:51:29` | `cowrie.session.params` |
| `2026-06-10 07:51:29` | `cowrie.command.input` |
| `2026-06-10 07:51:29` | `cowrie.command.failed` |
| `2026-06-10 07:51:29` | `cowrie.command.failed` |
| `2026-06-10 07:52:30` | `cowrie.session.params` |
| `2026-06-10 07:52:30` | `cowrie.command.input` |
| `2026-06-10 07:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a5c94866e1

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 07:53 |
| **Last Seen** | 2026-06-10 07:55 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:53:47` | `cowrie.session.connect` |
| `2026-06-10 07:53:47` | `cowrie.client.version` |
| `2026-06-10 07:53:47` | `cowrie.client.kex` |
| `2026-06-10 07:53:48` | `cowrie.login.success` |
| `2026-06-10 07:53:50` | `cowrie.session.file_upload` |
| `2026-06-10 07:53:51` | `cowrie.session.params` |
| `2026-06-10 07:53:51` | `cowrie.command.input` |
| `2026-06-10 07:53:51` | `cowrie.command.input` |
| `2026-06-10 07:53:51` | `cowrie.command.input` |
| `2026-06-10 07:53:51` | `cowrie.command.failed` |
| `2026-06-10 07:53:52` | `cowrie.log.closed` |
| `2026-06-10 07:53:53` | `cowrie.session.params` |
| `2026-06-10 07:53:53` | `cowrie.command.input` |
| `2026-06-10 07:53:53` | `cowrie.log.closed` |
| `2026-06-10 07:53:54` | `cowrie.session.params` |
| `2026-06-10 07:53:54` | `cowrie.command.input` |
| `2026-06-10 07:53:54` | `cowrie.log.closed` |
| `2026-06-10 07:53:56` | `cowrie.session.params` |
| `2026-06-10 07:53:56` | `cowrie.command.input` |
| `2026-06-10 07:53:56` | `cowrie.command.failed` |
| `2026-06-10 07:53:56` | `cowrie.command.failed` |
| `2026-06-10 07:54:57` | `cowrie.session.params` |
| `2026-06-10 07:54:57` | `cowrie.command.input` |
| `2026-06-10 07:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb70d9b1f83

| Field | Detail |
|---|---|
| **Source IP** | `56.124.92[.]130` |
| **First Seen** | 2026-06-10 07:54 |
| **Last Seen** | 2026-06-10 07:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:54:57` | `cowrie.session.connect` |
| `2026-06-10 07:54:57` | `cowrie.client.version` |
| `2026-06-10 07:54:58` | `cowrie.client.kex` |
| `2026-06-10 07:55:00` | `cowrie.login.success` |
| `2026-06-10 07:55:01` | `cowrie.session.params` |
| `2026-06-10 07:55:01` | `cowrie.command.input` |
| `2026-06-10 07:55:02` | `cowrie.log.closed` |
| `2026-06-10 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `56.124.92[.]130` to AbuseIPDB if not already reported
- [ ] Block `56.124.92[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4f5e9433a0

| Field | Detail |
|---|---|
| **Source IP** | `56.124.92[.]130` |
| **First Seen** | 2026-06-10 07:55 |
| **Last Seen** | 2026-06-10 07:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:55:02` | `cowrie.session.connect` |
| `2026-06-10 07:55:02` | `cowrie.client.version` |
| `2026-06-10 07:55:02` | `cowrie.client.kex` |
| `2026-06-10 07:55:04` | `cowrie.login.success` |
| `2026-06-10 07:55:06` | `cowrie.session.params` |
| `2026-06-10 07:55:06` | `cowrie.command.input` |
| `2026-06-10 07:55:07` | `cowrie.log.closed` |
| `2026-06-10 07:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `56.124.92[.]130` to AbuseIPDB if not already reported
- [ ] Block `56.124.92[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228a320bafcd

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 07:55 |
| **Last Seen** | 2026-06-10 07:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 07:55:04` | `cowrie.session.connect` |
| `2026-06-10 07:55:04` | `cowrie.client.version` |
| `2026-06-10 07:55:04` | `cowrie.client.kex` |
| `2026-06-10 07:55:05` | `cowrie.login.success` |
| `2026-06-10 07:55:05` | `cowrie.direct-tcpip.request` |
| `2026-06-10 07:55:05` | `cowrie.direct-tcpip.data` |
| `2026-06-10 07:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08fb8a20dd17

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 08:07 |
| **Last Seen** | 2026-06-10 08:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:07:30` | `cowrie.session.connect` |
| `2026-06-10 08:07:30` | `cowrie.client.version` |
| `2026-06-10 08:07:30` | `cowrie.client.kex` |
| `2026-06-10 08:07:31` | `cowrie.login.success` |
| `2026-06-10 08:07:31` | `cowrie.direct-tcpip.request` |
| `2026-06-10 08:07:31` | `cowrie.direct-tcpip.data` |
| `2026-06-10 08:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5cb6249ea1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]41` |
| **First Seen** | 2026-06-10 08:13 |
| **Last Seen** | 2026-06-10 08:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:13:46` | `cowrie.session.connect` |
| `2026-06-10 08:13:46` | `cowrie.login.success` |
| `2026-06-10 08:13:47` | `cowrie.session.params` |
| `2026-06-10 08:13:47` | `cowrie.command.input` |
| `2026-06-10 08:13:48` | `cowrie.command.input` |
| `2026-06-10 08:13:48` | `cowrie.command.input` |
| `2026-06-10 08:13:49` | `cowrie.command.input` |
| `2026-06-10 08:13:49` | `cowrie.command.failed` |
| `2026-06-10 08:13:50` | `cowrie.log.closed` |
| `2026-06-10 08:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]41` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0662bce2e0e4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 08:19 |
| **Last Seen** | 2026-06-10 08:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:19:39` | `cowrie.session.connect` |
| `2026-06-10 08:19:39` | `cowrie.client.version` |
| `2026-06-10 08:19:39` | `cowrie.client.kex` |
| `2026-06-10 08:19:39` | `cowrie.login.success` |
| `2026-06-10 08:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571b97b35fdf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 08:19 |
| **Last Seen** | 2026-06-10 08:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:19:39` | `cowrie.session.connect` |
| `2026-06-10 08:19:39` | `cowrie.client.version` |
| `2026-06-10 08:19:39` | `cowrie.client.kex` |
| `2026-06-10 08:19:39` | `cowrie.login.success` |
| `2026-06-10 08:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882b7a8131a9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 08:21 |
| **Last Seen** | 2026-06-10 08:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:21:52` | `cowrie.session.connect` |
| `2026-06-10 08:21:52` | `cowrie.client.version` |
| `2026-06-10 08:21:52` | `cowrie.client.kex` |
| `2026-06-10 08:21:52` | `cowrie.login.success` |
| `2026-06-10 08:21:53` | `cowrie.direct-tcpip.request` |
| `2026-06-10 08:21:53` | `cowrie.direct-tcpip.data` |
| `2026-06-10 08:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccacc719885a

| Field | Detail |
|---|---|
| **Source IP** | `56.124.92[.]130` |
| **First Seen** | 2026-06-10 08:38 |
| **Last Seen** | 2026-06-10 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:38:25` | `cowrie.session.connect` |
| `2026-06-10 08:38:25` | `cowrie.client.version` |
| `2026-06-10 08:38:25` | `cowrie.client.kex` |
| `2026-06-10 08:38:26` | `cowrie.login.success` |
| `2026-06-10 08:38:26` | `cowrie.session.params` |
| `2026-06-10 08:38:26` | `cowrie.command.input` |
| `2026-06-10 08:38:27` | `cowrie.log.closed` |
| `2026-06-10 08:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `56.124.92[.]130` to AbuseIPDB if not already reported
- [ ] Block `56.124.92[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65556dce3e47

| Field | Detail |
|---|---|
| **Source IP** | `56.124.92[.]130` |
| **First Seen** | 2026-06-10 08:38 |
| **Last Seen** | 2026-06-10 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:38:27` | `cowrie.session.connect` |
| `2026-06-10 08:38:27` | `cowrie.client.version` |
| `2026-06-10 08:38:27` | `cowrie.client.kex` |
| `2026-06-10 08:38:27` | `cowrie.login.success` |
| `2026-06-10 08:38:28` | `cowrie.session.params` |
| `2026-06-10 08:38:28` | `cowrie.command.input` |
| `2026-06-10 08:38:28` | `cowrie.log.closed` |
| `2026-06-10 08:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `56.124.92[.]130` to AbuseIPDB if not already reported
- [ ] Block `56.124.92[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.150[.]219` | **769** | 2026-06-10 03:05 | 2026-06-10 08:53 | 737m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.89[.]181` | **30** | 2026-06-10 05:44 | 2026-06-10 05:45 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.174[.]174` | **30** | 2026-06-10 04:57 | 2026-06-10 04:58 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.215[.]249` | **30** | 2026-06-10 04:23 | 2026-06-10 04:23 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **22** | 2026-06-10 03:52 | 2026-06-10 08:42 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `104.155.37[.]162` | **3** | 2026-06-10 06:51 | 2026-06-10 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.150.194[.]114` | **2** | 2026-06-10 05:19 | 2026-06-10 05:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.174.155[.]67` | 1 | 2026-06-10 08:52 | 2026-06-10 08:53 | 42s | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | 1 | 2026-06-10 08:06 | 2026-06-10 08:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.51.60[.]134` | 1 | 2026-06-10 07:53 | 2026-06-10 07:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-10 04:10 | 2026-06-10 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-10 03:44 | 2026-06-10 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.245.11[.]15` | 1 | 2026-06-10 08:08 | 2026-06-10 08:08 | 5s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]214` | 1 | 2026-06-10 06:23 | 2026-06-10 06:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]41` | 1 | 2026-06-10 04:05 | 2026-06-10 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]41` | 1 | 2026-06-10 08:13 | 2026-06-10 08:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.176.167[.]30` | 1 | 2026-06-10 08:33 | 2026-06-10 08:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | 1 | 2026-06-10 04:50 | 2026-06-10 04:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.38.45[.]137` | 1 | 2026-06-10 06:51 | 2026-06-10 06:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-10 07:09 | 2026-06-10 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-06-10 04:45 | 2026-06-10 04:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-06-10 08:44 | 2026-06-10 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.161.128[.]68` | 1 | 2026-06-10 08:03 | 2026-06-10 08:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]142` | 1 | 2026-06-10 07:54 | 2026-06-10 07:54 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]202` | 1 | 2026-06-10 07:35 | 2026-06-10 07:36 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | 1 | 2026-06-10 06:31 | 2026-06-10 06:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]46` | 1 | 2026-06-10 04:29 | 2026-06-10 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.134.142[.]242` | 1 | 2026-06-10 08:04 | 2026-06-10 08:04 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `34.79.215[.]249` | BE | Google LLC | **100** ⚠️ | 0 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `176.65.139[.]214` | NL | Storm Industries | **100** ⚠️ | 35 |
| `104.236.83[.]40` | US | DigitalOcean, LLC | **100** ⚠️ | 39 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `104.155.37[.]162` | BE | Google LLC | **100** ⚠️ | 1 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `51.161.128[.]68` | AU | OVH Australia PTY LTD | **100** ⚠️ | 26 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 79 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 11 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1003 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 52 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 28 recon entry/entries in table (7 group(s) consolidating 886 session(s)).

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
_Report time: 2026-06-10T10:10:33Z_

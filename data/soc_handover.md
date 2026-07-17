# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-17 |
| **Generated At** | 2026-07-17T21:00:02Z |
| **Shift Time** | 21:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **124** |
| Confirmed Threats | **105** |
| False Positives Filtered | **19** (15.3%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **28** |
| High Severity Cases | **51** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **73** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **11** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **59** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `admin` | 10 |
| `test` | 5 |
| `support` | 4 |
| `guest` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root2` | 5 |
| `admin@123` | 5 |
| `000000` | 4 |
| `admin12345678` | 4 |
| `guest2003` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root2` | 5 |
| `root` | `admin@123` | 5 |
| `root` | `000000` | 4 |
| `admin` | `admin12345678` | 4 |
| `guest` | `guest2003` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `thomas` | `thomas` | `65.20.211.96` | 2026-07-17T18:55:48 |
| `default` | `default2012` | `67.85.146.216` | 2026-07-17T18:58:34 |
| `thomas` | `thomas` | `49.124.149.54` | 2026-07-17T18:59:07 |
| `thomas` | `thomas` | `210.177.143.61` | 2026-07-17T18:59:16 |
| `root` | `ubuntu` | `197.248.15.98` | 2026-07-17T19:00:01 |
| `test` | `1111` | `111.70.32.53` | 2026-07-17T19:00:57 |
| `test` | `1111` | `10.0.0.73` | 2026-07-17T19:04:30 |
| `root` | `Pa55word2009` | `185.242.3.195` | 2026-07-17T19:09:57 |
| `root` | `root2` | `210.206.24.237` | 2026-07-17T19:14:58 |
| `root` | `root2` | `51.75.142.157` | 2026-07-17T19:15:05 |
| `root` | `` | `156.226.175.58` | 2026-07-17T19:15:11 |
| `root` | `root2` | `182.42.113.10` | 2026-07-17T19:18:33 |
| `root` | `root2` | `60.223.250.50` | 2026-07-17T19:18:42 |
| `root` | `root2` | `10.0.0.73` | 2026-07-17T19:18:53 |
| `default` | `default12345678` | `49.124.151.27` | 2026-07-17T19:21:40 |
| `root` | `Pa55word2009` | `10.0.0.73` | 2026-07-17T19:23:57 |
| `root` | `000000` | `202.72.196.75` | 2026-07-17T19:24:08 |
| `root` | `000000` | `106.0.166.123` | 2026-07-17T19:24:17 |
| `root` | `000000` | `10.0.0.73` | 2026-07-17T19:24:31 |
| `default` | `default12345678` | `178.178.222.52` | 2026-07-17T19:24:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-17T19:27:40 |
| `test` | `p@ssw0rd` | `10.0.0.73` | 2026-07-17T19:29:30 |
| `admin` | `admin12345678` | `178.178.194.137` | 2026-07-17T19:45:24 |
| `admin` | `admin12345678` | `113.140.95.250` | 2026-07-17T19:45:32 |
| `root` | `admin@123` | `222.86.168.224` | 2026-07-17T19:46:10 |
| `admin` | `admin12345678` | `211.223.41.90` | 2026-07-17T19:48:44 |
| `admin` | `admin12345678` | `91.219.196.17` | 2026-07-17T19:48:51 |
| `root` | `admin@123` | `27.107.102.154` | 2026-07-17T19:49:27 |
| `root` | `admin@123` | `82.102.188.117` | 2026-07-17T19:49:36 |
| `root` | `admin@123` | `10.0.0.73` | 2026-07-17T19:49:57 |
| `admin` | `admin` | `47.95.234.23` | 2026-07-17T20:00:43 |
| `ubuntu` | `asd123456` | `185.242.3.195` | 2026-07-17T20:02:52 |
| `admin` | `marketing` | `10.0.0.73` | 2026-07-17T20:06:59 |
| `guest` | `guest2003` | `45.178.227.0` | 2026-07-17T20:08:51 |
| `guest` | `guest2003` | `78.187.230.168` | 2026-07-17T20:08:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-17T20:10:36 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-17T20:10:36 |
| `nobody` | `1234567890` | `194.31.8.12` | 2026-07-17T20:11:17 |
| `nobody` | `1234567890` | `180.76.104.208` | 2026-07-17T20:11:25 |
| `guest` | `guest2003` | `125.23.255.134` | 2026-07-17T20:12:18 |
| `guest` | `guest2003` | `218.206.136.24` | 2026-07-17T20:12:34 |
| `nobody` | `1234567890` | `186.103.136.43` | 2026-07-17T20:14:44 |
| `nobody` | `1234567890` | `218.202.143.68` | 2026-07-17T20:14:52 |
| `ubuntu` | `asd123456` | `10.0.0.73` | 2026-07-17T20:16:56 |
| `support` | `123qwe` | `223.99.212.58` | 2026-07-17T20:17:10 |
| `support` | `123qwe` | `90.230.168.26` | 2026-07-17T20:17:17 |
| `support` | `123qwe` | `10.0.0.73` | 2026-07-17T20:17:31 |
| `blank` | `abc123` | `196.191.151.172` | 2026-07-17T20:31:19 |
| `blank` | `abc123` | `36.74.212.98` | 2026-07-17T20:31:29 |
| `root` | `` | `94.154.43.10` | 2026-07-17T20:32:43 |
| `admin` | `admin2015` | `109.207.41.125` | 2026-07-17T20:37:56 |
| `admin` | `admin2015` | `110.227.215.90` | 2026-07-17T20:38:04 |
| `admin` | `admin2015` | `10.0.0.73` | 2026-07-17T20:38:23 |
| `user` | `654321` | `90.228.229.182` | 2026-07-17T20:38:42 |
| `root` | `1` | `195.178.110.228` | 2026-07-17T20:45:28 |
| `root` | `12` | `195.178.110.228` | 2026-07-17T20:47:12 |
| `root` | `123` | `195.178.110.228` | 2026-07-17T20:49:00 |
| `root` | `1234` | `195.178.110.228` | 2026-07-17T20:50:49 |
| `root` | `12345` | `195.178.110.228` | 2026-07-17T20:52:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **124** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 38 |
| Go SSH scanner | 18 |
| Unknown | 7 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 38 | 38 |
| `2ec37a7cc8da...` | Mirai/variant | 6 | 1 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 38 | 38 | Mirai/variant |
| `95420f9d932d...` | Unknown | 6 | 4 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

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
Source IPs: `195.178.110.228`

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
Source IPs: `94.154.43.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **59** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (51)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f99fd0cc8b3c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-07-17 18:55 |
| **Last Seen** | 2026-07-17 18:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:55:46` | `cowrie.session.connect` |
| `2026-07-17 18:55:46` | `cowrie.client.version` |
| `2026-07-17 18:55:46` | `cowrie.client.kex` |
| `2026-07-17 18:55:48` | `cowrie.login.success` |
| `2026-07-17 18:55:48` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22af795cb576

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-17 18:58 |
| **Last Seen** | 2026-07-17 18:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:58:32` | `cowrie.session.connect` |
| `2026-07-17 18:58:32` | `cowrie.client.version` |
| `2026-07-17 18:58:32` | `cowrie.client.kex` |
| `2026-07-17 18:58:34` | `cowrie.login.success` |
| `2026-07-17 18:58:34` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86039a3bf76

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]54` |
| **First Seen** | 2026-07-17 18:59 |
| **Last Seen** | 2026-07-17 18:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:59:04` | `cowrie.session.connect` |
| `2026-07-17 18:59:05` | `cowrie.client.version` |
| `2026-07-17 18:59:05` | `cowrie.client.kex` |
| `2026-07-17 18:59:07` | `cowrie.login.success` |
| `2026-07-17 18:59:08` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]54` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d649e3de2e1d

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-17 18:59 |
| **Last Seen** | 2026-07-17 18:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:59:13` | `cowrie.session.connect` |
| `2026-07-17 18:59:14` | `cowrie.client.version` |
| `2026-07-17 18:59:14` | `cowrie.client.kex` |
| `2026-07-17 18:59:16` | `cowrie.login.success` |
| `2026-07-17 18:59:17` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6926638b2145

| Field | Detail |
|---|---|
| **Source IP** | `197.248.15[.]98` |
| **First Seen** | 2026-07-17 19:00 |
| **Last Seen** | 2026-07-17 19:01 |
| **Session Duration** | 91s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:00:00` | `cowrie.session.connect` |
| `2026-07-17 19:00:00` | `cowrie.client.version` |
| `2026-07-17 19:00:01` | `cowrie.client.kex` |
| `2026-07-17 19:00:01` | `cowrie.login.success` |
| `2026-07-17 19:01:31` | `cowrie.session.file_upload` |
| `2026-07-17 19:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.15[.]98` to AbuseIPDB if not already reported
- [ ] Block `197.248.15[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba5772fe5ba

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-17 19:00 |
| **Last Seen** | 2026-07-17 19:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:00:54` | `cowrie.session.connect` |
| `2026-07-17 19:00:55` | `cowrie.client.version` |
| `2026-07-17 19:00:55` | `cowrie.client.kex` |
| `2026-07-17 19:00:57` | `cowrie.login.success` |
| `2026-07-17 19:00:58` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c266ff8f3d88

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 19:09 |
| **Last Seen** | 2026-07-17 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:09:57` | `cowrie.session.connect` |
| `2026-07-17 19:09:57` | `cowrie.client.version` |
| `2026-07-17 19:09:57` | `cowrie.client.kex` |
| `2026-07-17 19:09:57` | `cowrie.login.success` |
| `2026-07-17 19:09:58` | `cowrie.session.params` |
| `2026-07-17 19:09:58` | `cowrie.command.input` |
| `2026-07-17 19:09:58` | `cowrie.log.closed` |
| `2026-07-17 19:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c2edb01e44

| Field | Detail |
|---|---|
| **Source IP** | `210.206.24[.]237` |
| **First Seen** | 2026-07-17 19:14 |
| **Last Seen** | 2026-07-17 19:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:14:54` | `cowrie.session.connect` |
| `2026-07-17 19:14:55` | `cowrie.client.version` |
| `2026-07-17 19:14:55` | `cowrie.client.kex` |
| `2026-07-17 19:14:58` | `cowrie.login.success` |
| `2026-07-17 19:14:58` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.206.24[.]237` to AbuseIPDB if not already reported
- [ ] Block `210.206.24[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0991995e89

| Field | Detail |
|---|---|
| **Source IP** | `51.75.142[.]157` |
| **First Seen** | 2026-07-17 19:15 |
| **Last Seen** | 2026-07-17 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:15:04` | `cowrie.session.connect` |
| `2026-07-17 19:15:05` | `cowrie.client.version` |
| `2026-07-17 19:15:05` | `cowrie.client.kex` |
| `2026-07-17 19:15:05` | `cowrie.login.success` |
| `2026-07-17 19:15:06` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.142[.]157` to AbuseIPDB if not already reported
- [ ] Block `51.75.142[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ac6097852a

| Field | Detail |
|---|---|
| **Source IP** | `156.226.175[.]58` |
| **First Seen** | 2026-07-17 19:15 |
| **Last Seen** | 2026-07-17 19:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:15:09` | `cowrie.session.connect` |
| `2026-07-17 19:15:10` | `cowrie.telnet.option` |
| `2026-07-17 19:15:11` | `cowrie.login.success` |
| `2026-07-17 19:15:11` | `cowrie.session.params` |
| `2026-07-17 19:15:12` | `cowrie.telnet.option` |
| `2026-07-17 19:15:12` | `cowrie.telnet.option` |
| `2026-07-17 19:15:17` | `cowrie.command.input` |
| `2026-07-17 19:15:19` | `cowrie.log.closed` |
| `2026-07-17 19:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.226.175[.]58` to AbuseIPDB if not already reported
- [ ] Block `156.226.175[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401efab5df13

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-07-17 19:18 |
| **Last Seen** | 2026-07-17 19:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:18:31` | `cowrie.session.connect` |
| `2026-07-17 19:18:31` | `cowrie.client.version` |
| `2026-07-17 19:18:31` | `cowrie.client.kex` |
| `2026-07-17 19:18:33` | `cowrie.login.success` |
| `2026-07-17 19:18:34` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b0ec102522

| Field | Detail |
|---|---|
| **Source IP** | `60.223.250[.]50` |
| **First Seen** | 2026-07-17 19:18 |
| **Last Seen** | 2026-07-17 19:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:18:39` | `cowrie.session.connect` |
| `2026-07-17 19:18:40` | `cowrie.client.version` |
| `2026-07-17 19:18:40` | `cowrie.client.kex` |
| `2026-07-17 19:18:42` | `cowrie.login.success` |
| `2026-07-17 19:18:43` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.250[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.223.250[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e079e49d2396

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]27` |
| **First Seen** | 2026-07-17 19:21 |
| **Last Seen** | 2026-07-17 19:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:21:37` | `cowrie.session.connect` |
| `2026-07-17 19:21:38` | `cowrie.client.version` |
| `2026-07-17 19:21:38` | `cowrie.client.kex` |
| `2026-07-17 19:21:40` | `cowrie.login.success` |
| `2026-07-17 19:21:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]27` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d238ca29f330

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-17 19:24 |
| **Last Seen** | 2026-07-17 19:25 |
| **Session Duration** | 99s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:24:05` | `cowrie.session.connect` |
| `2026-07-17 19:24:06` | `cowrie.client.version` |
| `2026-07-17 19:24:06` | `cowrie.client.kex` |
| `2026-07-17 19:24:08` | `cowrie.login.success` |
| `2026-07-17 19:24:09` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996f2299a367

| Field | Detail |
|---|---|
| **Source IP** | `106.0.166[.]123` |
| **First Seen** | 2026-07-17 19:24 |
| **Last Seen** | 2026-07-17 19:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:24:14` | `cowrie.session.connect` |
| `2026-07-17 19:24:15` | `cowrie.client.version` |
| `2026-07-17 19:24:15` | `cowrie.client.kex` |
| `2026-07-17 19:24:17` | `cowrie.login.success` |
| `2026-07-17 19:24:17` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.0.166[.]123` to AbuseIPDB if not already reported
- [ ] Block `106.0.166[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e92df848a6

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-17 19:24 |
| **Last Seen** | 2026-07-17 19:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:24:40` | `cowrie.session.connect` |
| `2026-07-17 19:24:40` | `cowrie.client.version` |
| `2026-07-17 19:24:40` | `cowrie.client.kex` |
| `2026-07-17 19:24:42` | `cowrie.login.success` |
| `2026-07-17 19:24:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c438c5e0102

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 19:26 |
| **Last Seen** | 2026-07-17 19:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:26:59` | `cowrie.session.connect` |
| `2026-07-17 19:27:00` | `cowrie.client.version` |
| `2026-07-17 19:27:00` | `cowrie.client.kex` |
| `2026-07-17 19:27:01` | `cowrie.login.success` |
| `2026-07-17 19:27:02` | `cowrie.session.params` |
| `2026-07-17 19:27:02` | `cowrie.command.input` |
| `2026-07-17 19:27:03` | `cowrie.log.closed` |
| `2026-07-17 19:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2de51d03473

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 19:27 |
| **Last Seen** | 2026-07-17 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:27:39` | `cowrie.session.connect` |
| `2026-07-17 19:27:39` | `cowrie.client.version` |
| `2026-07-17 19:27:40` | `cowrie.client.kex` |
| `2026-07-17 19:27:40` | `cowrie.login.success` |
| `2026-07-17 19:27:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:27:40` | `cowrie.direct-tcpip.data` |
| `2026-07-17 19:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f5164266ef

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-07-17 19:45 |
| **Last Seen** | 2026-07-17 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:45:22` | `cowrie.session.connect` |
| `2026-07-17 19:45:22` | `cowrie.client.version` |
| `2026-07-17 19:45:22` | `cowrie.client.kex` |
| `2026-07-17 19:45:24` | `cowrie.login.success` |
| `2026-07-17 19:45:24` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda61efe9e95

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-17 19:45 |
| **Last Seen** | 2026-07-17 19:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:45:29` | `cowrie.session.connect` |
| `2026-07-17 19:45:30` | `cowrie.client.version` |
| `2026-07-17 19:45:30` | `cowrie.client.kex` |
| `2026-07-17 19:45:32` | `cowrie.login.success` |
| `2026-07-17 19:45:33` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70f3c404be9

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-17 19:46 |
| **Last Seen** | 2026-07-17 19:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:46:07` | `cowrie.session.connect` |
| `2026-07-17 19:46:07` | `cowrie.client.version` |
| `2026-07-17 19:46:07` | `cowrie.client.kex` |
| `2026-07-17 19:46:10` | `cowrie.login.success` |
| `2026-07-17 19:46:10` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4a5cdc4102

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-07-17 19:48 |
| **Last Seen** | 2026-07-17 19:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:48:40` | `cowrie.session.connect` |
| `2026-07-17 19:48:41` | `cowrie.client.version` |
| `2026-07-17 19:48:41` | `cowrie.client.kex` |
| `2026-07-17 19:48:44` | `cowrie.login.success` |
| `2026-07-17 19:48:44` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fa25312fe4

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-07-17 19:48 |
| **Last Seen** | 2026-07-17 19:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:48:49` | `cowrie.session.connect` |
| `2026-07-17 19:48:50` | `cowrie.client.version` |
| `2026-07-17 19:48:50` | `cowrie.client.kex` |
| `2026-07-17 19:48:51` | `cowrie.login.success` |
| `2026-07-17 19:48:51` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af415b17d04

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-17 19:49 |
| **Last Seen** | 2026-07-17 19:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:49:24` | `cowrie.session.connect` |
| `2026-07-17 19:49:25` | `cowrie.client.version` |
| `2026-07-17 19:49:25` | `cowrie.client.kex` |
| `2026-07-17 19:49:27` | `cowrie.login.success` |
| `2026-07-17 19:49:28` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d514a86d59d

| Field | Detail |
|---|---|
| **Source IP** | `82.102.188[.]117` |
| **First Seen** | 2026-07-17 19:49 |
| **Last Seen** | 2026-07-17 19:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:49:33` | `cowrie.session.connect` |
| `2026-07-17 19:49:34` | `cowrie.client.version` |
| `2026-07-17 19:49:34` | `cowrie.client.kex` |
| `2026-07-17 19:49:36` | `cowrie.login.success` |
| `2026-07-17 19:49:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 19:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.188[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.102.188[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ef0823bf87

| Field | Detail |
|---|---|
| **Source IP** | `47.95.234[.]23` |
| **First Seen** | 2026-07-17 19:59 |
| **Last Seen** | 2026-07-17 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 19:59:42` | `cowrie.session.connect` |
| `2026-07-17 19:59:42` | `cowrie.telnet.option` |
| `2026-07-17 19:59:43` | `cowrie.telnet.option` |
| `2026-07-17 20:00:43` | `cowrie.login.success` |
| `2026-07-17 20:00:43` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.95.234[.]23` to AbuseIPDB if not already reported
- [ ] Block `47.95.234[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b12d76281f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 20:02 |
| **Last Seen** | 2026-07-17 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:02:51` | `cowrie.session.connect` |
| `2026-07-17 20:02:51` | `cowrie.client.version` |
| `2026-07-17 20:02:51` | `cowrie.client.kex` |
| `2026-07-17 20:02:52` | `cowrie.login.success` |
| `2026-07-17 20:02:53` | `cowrie.session.params` |
| `2026-07-17 20:02:53` | `cowrie.command.input` |
| `2026-07-17 20:02:53` | `cowrie.log.closed` |
| `2026-07-17 20:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e06dc51bc2

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-17 20:08 |
| **Last Seen** | 2026-07-17 20:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:08:48` | `cowrie.session.connect` |
| `2026-07-17 20:08:49` | `cowrie.client.version` |
| `2026-07-17 20:08:49` | `cowrie.client.kex` |
| `2026-07-17 20:08:51` | `cowrie.login.success` |
| `2026-07-17 20:08:51` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90089fd8764a

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-17 20:08 |
| **Last Seen** | 2026-07-17 20:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:08:56` | `cowrie.session.connect` |
| `2026-07-17 20:08:57` | `cowrie.client.version` |
| `2026-07-17 20:08:57` | `cowrie.client.kex` |
| `2026-07-17 20:08:58` | `cowrie.login.success` |
| `2026-07-17 20:08:58` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6b02a24f01

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 20:10 |
| **Last Seen** | 2026-07-17 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:10:35` | `cowrie.session.connect` |
| `2026-07-17 20:10:35` | `cowrie.client.version` |
| `2026-07-17 20:10:36` | `cowrie.client.kex` |
| `2026-07-17 20:10:36` | `cowrie.login.success` |
| `2026-07-17 20:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b26277e7f8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 20:10 |
| **Last Seen** | 2026-07-17 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:10:35` | `cowrie.session.connect` |
| `2026-07-17 20:10:35` | `cowrie.client.version` |
| `2026-07-17 20:10:36` | `cowrie.client.kex` |
| `2026-07-17 20:10:36` | `cowrie.login.success` |
| `2026-07-17 20:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018c32d726ac

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-07-17 20:11 |
| **Last Seen** | 2026-07-17 20:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:11:14` | `cowrie.session.connect` |
| `2026-07-17 20:11:16` | `cowrie.client.version` |
| `2026-07-17 20:11:16` | `cowrie.client.kex` |
| `2026-07-17 20:11:17` | `cowrie.login.success` |
| `2026-07-17 20:11:17` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1cfaf00230

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-07-17 20:11 |
| **Last Seen** | 2026-07-17 20:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:11:23` | `cowrie.session.connect` |
| `2026-07-17 20:11:23` | `cowrie.client.version` |
| `2026-07-17 20:11:23` | `cowrie.client.kex` |
| `2026-07-17 20:11:25` | `cowrie.login.success` |
| `2026-07-17 20:11:25` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f436478549

| Field | Detail |
|---|---|
| **Source IP** | `125.23.255[.]134` |
| **First Seen** | 2026-07-17 20:12 |
| **Last Seen** | 2026-07-17 20:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:12:12` | `cowrie.session.connect` |
| `2026-07-17 20:12:14` | `cowrie.client.version` |
| `2026-07-17 20:12:14` | `cowrie.client.kex` |
| `2026-07-17 20:12:18` | `cowrie.login.success` |
| `2026-07-17 20:12:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.255[.]134` to AbuseIPDB if not already reported
- [ ] Block `125.23.255[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6cecdc0076

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-17 20:12 |
| **Last Seen** | 2026-07-17 20:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:12:29` | `cowrie.session.connect` |
| `2026-07-17 20:12:31` | `cowrie.client.version` |
| `2026-07-17 20:12:31` | `cowrie.client.kex` |
| `2026-07-17 20:12:34` | `cowrie.login.success` |
| `2026-07-17 20:12:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d9ca49ecb0

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-17 20:14 |
| **Last Seen** | 2026-07-17 20:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:14:41` | `cowrie.session.connect` |
| `2026-07-17 20:14:42` | `cowrie.client.version` |
| `2026-07-17 20:14:42` | `cowrie.client.kex` |
| `2026-07-17 20:14:44` | `cowrie.login.success` |
| `2026-07-17 20:14:44` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9316febf75bd

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-17 20:14 |
| **Last Seen** | 2026-07-17 20:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:14:50` | `cowrie.session.connect` |
| `2026-07-17 20:14:50` | `cowrie.client.version` |
| `2026-07-17 20:14:50` | `cowrie.client.kex` |
| `2026-07-17 20:14:52` | `cowrie.login.success` |
| `2026-07-17 20:14:53` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbcbcf2191ba

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-07-17 20:17 |
| **Last Seen** | 2026-07-17 20:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:17:06` | `cowrie.session.connect` |
| `2026-07-17 20:17:07` | `cowrie.client.version` |
| `2026-07-17 20:17:07` | `cowrie.client.kex` |
| `2026-07-17 20:17:10` | `cowrie.login.success` |
| `2026-07-17 20:17:11` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabdfba9346f

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-17 20:17 |
| **Last Seen** | 2026-07-17 20:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:17:16` | `cowrie.session.connect` |
| `2026-07-17 20:17:16` | `cowrie.client.version` |
| `2026-07-17 20:17:16` | `cowrie.client.kex` |
| `2026-07-17 20:17:17` | `cowrie.login.success` |
| `2026-07-17 20:17:18` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f177d226b9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 20:20 |
| **Last Seen** | 2026-07-17 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:20:00` | `cowrie.session.connect` |
| `2026-07-17 20:20:00` | `cowrie.client.version` |
| `2026-07-17 20:20:00` | `cowrie.client.kex` |
| `2026-07-17 20:20:00` | `cowrie.login.success` |
| `2026-07-17 20:20:01` | `cowrie.session.params` |
| `2026-07-17 20:20:01` | `cowrie.command.input` |
| `2026-07-17 20:20:01` | `cowrie.log.closed` |
| `2026-07-17 20:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a1426c9b38

| Field | Detail |
|---|---|
| **Source IP** | `196.191.151[.]172` |
| **First Seen** | 2026-07-17 20:31 |
| **Last Seen** | 2026-07-17 20:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:31:18` | `cowrie.session.connect` |
| `2026-07-17 20:31:18` | `cowrie.client.version` |
| `2026-07-17 20:31:18` | `cowrie.client.kex` |
| `2026-07-17 20:31:19` | `cowrie.login.success` |
| `2026-07-17 20:31:20` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.151[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.191.151[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c01bf70ada7

| Field | Detail |
|---|---|
| **Source IP** | `36.74.212[.]98` |
| **First Seen** | 2026-07-17 20:31 |
| **Last Seen** | 2026-07-17 20:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:31:26` | `cowrie.session.connect` |
| `2026-07-17 20:31:26` | `cowrie.client.version` |
| `2026-07-17 20:31:26` | `cowrie.client.kex` |
| `2026-07-17 20:31:29` | `cowrie.login.success` |
| `2026-07-17 20:31:29` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.74.212[.]98` to AbuseIPDB if not already reported
- [ ] Block `36.74.212[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dfd536ca485

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]10` |
| **First Seen** | 2026-07-17 20:32 |
| **Last Seen** | 2026-07-17 20:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:32:42` | `cowrie.session.connect` |
| `2026-07-17 20:32:43` | `cowrie.login.success` |
| `2026-07-17 20:32:43` | `cowrie.session.params` |
| `2026-07-17 20:32:44` | `cowrie.command.input` |
| `2026-07-17 20:32:44` | `cowrie.command.input` |
| `2026-07-17 20:32:45` | `cowrie.command.input` |
| `2026-07-17 20:32:46` | `cowrie.command.input` |
| `2026-07-17 20:32:46` | `cowrie.command.failed` |
| `2026-07-17 20:32:47` | `cowrie.log.closed` |
| `2026-07-17 20:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]10` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1ba2c5f04d

| Field | Detail |
|---|---|
| **Source IP** | `109.207.41[.]125` |
| **First Seen** | 2026-07-17 20:37 |
| **Last Seen** | 2026-07-17 20:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:37:54` | `cowrie.session.connect` |
| `2026-07-17 20:37:55` | `cowrie.client.version` |
| `2026-07-17 20:37:55` | `cowrie.client.kex` |
| `2026-07-17 20:37:56` | `cowrie.login.success` |
| `2026-07-17 20:37:56` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.207.41[.]125` to AbuseIPDB if not already reported
- [ ] Block `109.207.41[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d09a6b4658

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-07-17 20:38 |
| **Last Seen** | 2026-07-17 20:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:38:02` | `cowrie.session.connect` |
| `2026-07-17 20:38:03` | `cowrie.client.version` |
| `2026-07-17 20:38:03` | `cowrie.client.kex` |
| `2026-07-17 20:38:04` | `cowrie.login.success` |
| `2026-07-17 20:38:05` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772c6cf01738

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-07-17 20:38 |
| **Last Seen** | 2026-07-17 20:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:38:41` | `cowrie.session.connect` |
| `2026-07-17 20:38:41` | `cowrie.client.version` |
| `2026-07-17 20:38:41` | `cowrie.client.kex` |
| `2026-07-17 20:38:42` | `cowrie.login.success` |
| `2026-07-17 20:38:43` | `cowrie.direct-tcpip.request` |
| `2026-07-17 20:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e542f67de510

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-17 20:45 |
| **Last Seen** | 2026-07-17 20:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:45:26` | `cowrie.session.connect` |
| `2026-07-17 20:45:26` | `cowrie.client.version` |
| `2026-07-17 20:45:26` | `cowrie.client.kex` |
| `2026-07-17 20:45:28` | `cowrie.login.success` |
| `2026-07-17 20:45:30` | `cowrie.session.params` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.success` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.command.input` |
| `2026-07-17 20:45:30` | `cowrie.log.closed` |
| `2026-07-17 20:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5521a0bb73

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-17 20:47 |
| **Last Seen** | 2026-07-17 20:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:47:10` | `cowrie.session.connect` |
| `2026-07-17 20:47:10` | `cowrie.client.version` |
| `2026-07-17 20:47:10` | `cowrie.client.kex` |
| `2026-07-17 20:47:12` | `cowrie.login.success` |
| `2026-07-17 20:47:14` | `cowrie.session.params` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.success` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.command.input` |
| `2026-07-17 20:47:14` | `cowrie.log.closed` |
| `2026-07-17 20:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e76cb8fac0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-17 20:48 |
| **Last Seen** | 2026-07-17 20:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:48:58` | `cowrie.session.connect` |
| `2026-07-17 20:48:58` | `cowrie.client.version` |
| `2026-07-17 20:48:58` | `cowrie.client.kex` |
| `2026-07-17 20:49:00` | `cowrie.login.success` |
| `2026-07-17 20:49:01` | `cowrie.session.params` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.success` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:01` | `cowrie.command.input` |
| `2026-07-17 20:49:02` | `cowrie.log.closed` |
| `2026-07-17 20:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0701f6ad9341

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-17 20:50 |
| **Last Seen** | 2026-07-17 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:50:48` | `cowrie.session.connect` |
| `2026-07-17 20:50:48` | `cowrie.client.version` |
| `2026-07-17 20:50:48` | `cowrie.client.kex` |
| `2026-07-17 20:50:49` | `cowrie.login.success` |
| `2026-07-17 20:50:50` | `cowrie.session.params` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.success` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.command.input` |
| `2026-07-17 20:50:50` | `cowrie.log.closed` |
| `2026-07-17 20:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacad22056d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-17 20:52 |
| **Last Seen** | 2026-07-17 20:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 20:52:41` | `cowrie.session.connect` |
| `2026-07-17 20:52:42` | `cowrie.client.version` |
| `2026-07-17 20:52:42` | `cowrie.client.kex` |
| `2026-07-17 20:52:43` | `cowrie.login.success` |
| `2026-07-17 20:52:44` | `cowrie.session.params` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.success` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:44` | `cowrie.command.input` |
| `2026-07-17 20:52:45` | `cowrie.log.closed` |
| `2026-07-17 20:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **7** | 2026-07-17 19:08 | 2026-07-17 20:48 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]192` | **5** | 2026-07-17 20:50 | 2026-07-17 20:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]67` | **4** | 2026-07-17 20:51 | 2026-07-17 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-17 19:37 | 2026-07-17 20:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]218` | **3** | 2026-07-17 19:37 | 2026-07-17 19:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-17 19:19 | 2026-07-17 19:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | **3** | 2026-07-17 20:51 | 2026-07-17 20:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-17 20:00 | 2026-07-17 20:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]115` | **2** | 2026-07-17 20:21 | 2026-07-17 20:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-07-17 20:29 | 2026-07-17 20:54 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.14[.]234` | **2** | 2026-07-17 20:00 | 2026-07-17 20:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]43` | **2** | 2026-07-17 20:52 | 2026-07-17 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-07-17 19:03 | 2026-07-17 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.4[.]155` | 1 | 2026-07-17 20:39 | 2026-07-17 20:40 | 11s | 0 | `T1592` | 🟢 LOW |
| `197.155.225[.]93` | 1 | 2026-07-17 19:53 | 2026-07-17 19:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `211.247.127[.]250` | 1 | 2026-07-17 19:50 | 2026-07-17 19:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `219.89.198[.]191` | 1 | 2026-07-17 19:24 | 2026-07-17 19:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.82.97[.]51` | 1 | 2026-07-17 19:21 | 2026-07-17 19:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-17 19:04 | 2026-07-17 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-17 19:36 | 2026-07-17 19:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-17 20:35 | 2026-07-17 20:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]30` | 1 | 2026-07-17 19:04 | 2026-07-17 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.129.176[.]156` | 1 | 2026-07-17 20:23 | 2026-07-17 20:23 | 14s | 0 | `T1592` | 🟢 LOW |
| `5.255.97[.]209` | 1 | 2026-07-17 19:16 | 2026-07-17 19:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-17 19:42 | 2026-07-17 19:43 | 46s | 0 | `T1592` | 🟢 LOW |
| `83.239.84[.]130` | 1 | 2026-07-17 19:39 | 2026-07-17 19:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]10` | 1 | 2026-07-17 20:32 | 2026-07-17 20:32 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `182.42.113[.]10` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `223.82.97[.]51` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `197.155.225[.]93` | ZW | LIQUID Zimbabwe MPLS Core | **100** ⚠️ | 50 |
| `222.86.168[.]224` | CN | CHINANET Guizhou province network | **100** ⚠️ | 50 |
| `78.187.230[.]168` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 41 |
| `210.206.24[.]237` | KR | LG Uplus | **100** ⚠️ | 4 |
| `5.255.97[.]209` | NL | The Infrastructure Group B.V. | **100** ⚠️ | 18 |
| `66.132.172[.]192` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `116.255.226[.]73` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 24 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 51 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 6 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 5 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 124 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (15.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 51 priority case(s) shown individually · 27 recon entry/entries in table (12 group(s) consolidating 39 session(s)).

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
_Report time: 2026-07-17T21:00:02Z_

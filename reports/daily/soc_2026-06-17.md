# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-17 |
| **Generated At** | 2026-06-17T18:24:40Z |
| **Shift Time** | 18:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **49** |
| Confirmed Threats | **32** |
| False Positives Filtered | **17** (34.7%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **12** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **41** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **3** |
| Unique Usernames | **1** |
| Unique Passwords | **3** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123@@@` | 3 |
| `LeitboGi0ro` | 3 |
| `smo@@kkklss` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `123@@@` | 3 |
| `root` | `LeitboGi0ro` | 3 |
| `root` | `smo@@kkklss` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `129.153.145.135` | 2026-06-17T14:57:43 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-17T14:57:43 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-17T15:15:27 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-17T15:15:27 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-17T16:46:04 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-17T16:46:04 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-17T16:46:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **49** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 16 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 2 |
| Unknown | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 2 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 15 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **25** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS8151` | UNINET | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS3258` | xTom Japan Corporation | 1 | HIGH |
| `AS134762` | CHINANET Liaoning province Dalian MAN network | 1 | MEDIUM |
| `AS132124` | Information and Communication Technology Agency of Sri Lanka | 1 | HIGH |
| `AS35916` | MULTACOM CORPORATION | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4d4b39067874

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 14:57 |
| **Last Seen** | 2026-06-17 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:57:43` | `cowrie.session.connect` |
| `2026-06-17 14:57:43` | `cowrie.client.version` |
| `2026-06-17 14:57:43` | `cowrie.client.kex` |
| `2026-06-17 14:57:43` | `cowrie.login.success` |
| `2026-06-17 14:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ba37858dee

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 14:57 |
| **Last Seen** | 2026-06-17 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:57:43` | `cowrie.session.connect` |
| `2026-06-17 14:57:43` | `cowrie.client.version` |
| `2026-06-17 14:57:43` | `cowrie.client.kex` |
| `2026-06-17 14:57:43` | `cowrie.login.success` |
| `2026-06-17 14:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f2fdf81305

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-17 15:15 |
| **Last Seen** | 2026-06-17 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 15:15:26` | `cowrie.session.connect` |
| `2026-06-17 15:15:26` | `cowrie.client.version` |
| `2026-06-17 15:15:27` | `cowrie.client.kex` |
| `2026-06-17 15:15:27` | `cowrie.login.success` |
| `2026-06-17 15:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0d4db4a717

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-17 15:15 |
| **Last Seen** | 2026-06-17 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 15:15:27` | `cowrie.session.connect` |
| `2026-06-17 15:15:27` | `cowrie.client.version` |
| `2026-06-17 15:15:27` | `cowrie.client.kex` |
| `2026-06-17 15:15:27` | `cowrie.login.success` |
| `2026-06-17 15:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1200ac50a9b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 16:46 |
| **Last Seen** | 2026-06-17 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 16:46:03` | `cowrie.session.connect` |
| `2026-06-17 16:46:03` | `cowrie.client.version` |
| `2026-06-17 16:46:03` | `cowrie.client.kex` |
| `2026-06-17 16:46:04` | `cowrie.login.success` |
| `2026-06-17 16:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ae26cf4c90

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 16:46 |
| **Last Seen** | 2026-06-17 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 16:46:03` | `cowrie.session.connect` |
| `2026-06-17 16:46:03` | `cowrie.client.version` |
| `2026-06-17 16:46:03` | `cowrie.client.kex` |
| `2026-06-17 16:46:04` | `cowrie.login.success` |
| `2026-06-17 16:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6da0ca8970

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 16:46 |
| **Last Seen** | 2026-06-17 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 16:46:09` | `cowrie.session.connect` |
| `2026-06-17 16:46:09` | `cowrie.client.version` |
| `2026-06-17 16:46:09` | `cowrie.client.kex` |
| `2026-06-17 16:46:10` | `cowrie.login.success` |
| `2026-06-17 16:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178a8691d380

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 16:46 |
| **Last Seen** | 2026-06-17 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 16:46:10` | `cowrie.session.connect` |
| `2026-06-17 16:46:10` | `cowrie.client.version` |
| `2026-06-17 16:46:10` | `cowrie.client.kex` |
| `2026-06-17 16:46:11` | `cowrie.login.success` |
| `2026-06-17 16:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **2** | 2026-06-17 15:59 | 2026-06-17 16:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]141` | **2** | 2026-06-17 15:03 | 2026-06-17 15:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.132.26[.]232` | **2** | 2026-06-17 14:57 | 2026-06-17 15:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]189` | 1 | 2026-06-17 16:26 | 2026-06-17 16:26 | 3s | 0 | `T1592` | 🟢 LOW |
| `117.64.67[.]159` | 1 | 2026-06-17 15:18 | 2026-06-17 15:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `161.153.4[.]94` | 1 | 2026-06-17 16:02 | 2026-06-17 16:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `162.243.174[.]209` | 1 | 2026-06-17 15:44 | 2026-06-17 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `163.47.43[.]17` | 1 | 2026-06-17 16:21 | 2026-06-17 16:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.125.252[.]215` | 1 | 2026-06-17 15:30 | 2026-06-17 15:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | 1 | 2026-06-17 15:44 | 2026-06-17 15:44 | 36s | 0 | `T1592` | 🟢 LOW |
| `187.224.15[.]95` | 1 | 2026-06-17 16:04 | 2026-06-17 16:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.115.189[.]194` | 1 | 2026-06-17 16:33 | 2026-06-17 16:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `198.11.179[.]228` | 1 | 2026-06-17 15:42 | 2026-06-17 15:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.212.242[.]22` | 1 | 2026-06-17 15:37 | 2026-06-17 15:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-06-17 15:05 | 2026-06-17 15:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]139` | 1 | 2026-06-17 16:38 | 2026-06-17 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-17 16:05 | 2026-06-17 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.8.112[.]224` | 1 | 2026-06-17 15:04 | 2026-06-17 15:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `48.193.44[.]21` | 1 | 2026-06-17 16:15 | 2026-06-17 16:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.136.165[.]202` | 1 | 2026-06-17 14:55 | 2026-06-17 14:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]221` | 1 | 2026-06-17 15:57 | 2026-06-17 15:57 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `161.153.4[.]94` | US | Oracle Corporation | **100** ⚠️ | 5 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `61.136.165[.]202` | CN | CHINANET Hubei province network | **100** ⚠️ | 3 |
| `45.142.193[.]139` | NL | Limited Network LTD | **100** ⚠️ | 23 |
| `190.115.189[.]194` | HT | Télécommunications de Haití (Teleco) | **100** ⚠️ | 9 |
| `117.64.67[.]159` | CN | CHINANET anhui province network | **100** ⚠️ | 4 |
| `183.91.11[.]226` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 4 |
| `176.125.252[.]215` | IT | Open Fiber S.P.A. | **100** ⚠️ | 13 |
| `162.243.174[.]209` | US | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `48.193.44[.]21` | ID | Microsoft Limited | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 49 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (34.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 21 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
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
_Report time: 2026-06-17T18:24:40Z_

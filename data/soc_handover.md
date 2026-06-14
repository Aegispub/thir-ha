# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T12:00:46Z |
| **Shift Time** | 12:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **188** |
| Confirmed Threats | **169** |
| False Positives Filtered | **19** (10.1%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **10** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **179** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **13** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **2** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `LeitboGi0ro` | 2 |
| `123@@@` | 2 |
| `smo@@kkklss` | 2 |
| `Host: 129.80.119.236:23` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `123@@@` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.38` | 2026-06-14T09:05:35 |
| `root` | `123456` | `80.94.92.178` | 2026-06-14T09:10:08 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-14T09:21:08 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-14T09:21:08 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T10:30:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-14T10:30:04 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T10:30:04 |
| `root` | `---fuck_you----` | `204.141.229.119` | 2026-06-14T10:33:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **188** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 15 |
| Go SSH scanner | 8 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `f93d28ee0c77...` | Modern SSH client | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 14 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f93d28ee0c77...` | libssh | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **22** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS15557` | Societe Francaise Du Radiotelephone - SFR SA | 1 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 1 | MEDIUM |
| `AS398019` | Dynu Systems Incorporated | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a285d15afc09

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]38` |
| **First Seen** | 2026-06-14 09:05 |
| **Last Seen** | 2026-06-14 09:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:05:35` | `cowrie.session.connect` |
| `2026-06-14 09:05:35` | `cowrie.login.success` |
| `2026-06-14 09:05:36` | `cowrie.session.params` |
| `2026-06-14 09:05:36` | `cowrie.command.input` |
| `2026-06-14 09:05:36` | `cowrie.command.input` |
| `2026-06-14 09:05:36` | `cowrie.command.failed` |
| `2026-06-14 09:05:36` | `cowrie.command.input` |
| `2026-06-14 09:05:36` | `cowrie.command.failed` |
| `2026-06-14 09:05:36` | `cowrie.command.input` |
| `2026-06-14 09:05:36` | `cowrie.log.closed` |
| `2026-06-14 09:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]38` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e14fedd1b1a6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]178` |
| **First Seen** | 2026-06-14 09:10 |
| **Last Seen** | 2026-06-14 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /proc/self/status` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:10:07` | `cowrie.session.connect` |
| `2026-06-14 09:10:07` | `cowrie.client.version` |
| `2026-06-14 09:10:08` | `cowrie.client.kex` |
| `2026-06-14 09:10:08` | `cowrie.login.success` |
| `2026-06-14 09:10:09` | `cowrie.session.params` |
| `2026-06-14 09:10:09` | `cowrie.command.input` |
| `2026-06-14 09:10:09` | `cowrie.log.closed` |
| `2026-06-14 09:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]178` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d8f210df25

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 09:21 |
| **Last Seen** | 2026-06-14 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:21:07` | `cowrie.session.connect` |
| `2026-06-14 09:21:07` | `cowrie.client.version` |
| `2026-06-14 09:21:07` | `cowrie.client.kex` |
| `2026-06-14 09:21:08` | `cowrie.login.success` |
| `2026-06-14 09:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f386bc164f2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 09:21 |
| **Last Seen** | 2026-06-14 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:21:07` | `cowrie.session.connect` |
| `2026-06-14 09:21:07` | `cowrie.client.version` |
| `2026-06-14 09:21:08` | `cowrie.client.kex` |
| `2026-06-14 09:21:08` | `cowrie.login.success` |
| `2026-06-14 09:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2d0dc01cf0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 10:30 |
| **Last Seen** | 2026-06-14 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:30:04` | `cowrie.session.connect` |
| `2026-06-14 10:30:04` | `cowrie.client.version` |
| `2026-06-14 10:30:04` | `cowrie.client.kex` |
| `2026-06-14 10:30:04` | `cowrie.login.success` |
| `2026-06-14 10:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730559bdda07

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 10:30 |
| **Last Seen** | 2026-06-14 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:30:04` | `cowrie.session.connect` |
| `2026-06-14 10:30:04` | `cowrie.client.version` |
| `2026-06-14 10:30:04` | `cowrie.client.kex` |
| `2026-06-14 10:30:04` | `cowrie.login.success` |
| `2026-06-14 10:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab7fb160472

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 10:30 |
| **Last Seen** | 2026-06-14 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:30:04` | `cowrie.session.connect` |
| `2026-06-14 10:30:04` | `cowrie.client.version` |
| `2026-06-14 10:30:04` | `cowrie.client.kex` |
| `2026-06-14 10:30:04` | `cowrie.login.success` |
| `2026-06-14 10:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5064a590432

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 10:30 |
| **Last Seen** | 2026-06-14 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:30:14` | `cowrie.session.connect` |
| `2026-06-14 10:30:14` | `cowrie.client.version` |
| `2026-06-14 10:30:14` | `cowrie.client.kex` |
| `2026-06-14 10:30:14` | `cowrie.login.success` |
| `2026-06-14 10:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.93[.]206` | **122** | 2026-06-14 08:55 | 2026-06-14 10:54 | 95m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **10** | 2026-06-14 08:57 | 2026-06-14 10:49 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **4** | 2026-06-14 09:13 | 2026-06-14 10:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `135.237.127[.]190` | **2** | 2026-06-14 09:36 | 2026-06-14 09:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-14 09:22 | 2026-06-14 10:22 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-14 10:38 | 2026-06-14 10:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]187` | **2** | 2026-06-14 10:34 | 2026-06-14 10:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.149.231[.]45` | **2** | 2026-06-14 09:58 | 2026-06-14 10:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.18.108[.]189` | **2** | 2026-06-14 09:24 | 2026-06-14 09:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | **2** | 2026-06-14 09:37 | 2026-06-14 10:08 | 1m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]21` | **2** | 2026-06-14 09:39 | 2026-06-14 10:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.81.62[.]90` | 1 | 2026-06-14 09:57 | 2026-06-14 09:58 | 34s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-06-14 09:33 | 2026-06-14 09:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.203.209[.]226` | 1 | 2026-06-14 09:01 | 2026-06-14 09:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-06-14 10:03 | 2026-06-14 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-14 10:36 | 2026-06-14 10:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-06-14 09:33 | 2026-06-14 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]103` | 1 | 2026-06-14 10:44 | 2026-06-14 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-14 09:41 | 2026-06-14 09:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `84.6.37[.]37` | 1 | 2026-06-14 09:55 | 2026-06-14 09:56 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 3 |
| `3.149.231[.]45` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `183.203.209[.]226` | CN | China Mobile Communications Corporation | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `69.11.71[.]166` | CA | SaskTel Wide Area Network Engineering Center | **100** ⚠️ | 2 |
| `3.18.108[.]189` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `45.82.78[.]103` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 188 cases |
| Tool 34  | Credential Extractor        | ✅ 13 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (10.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 20 recon entry/entries in table (11 group(s) consolidating 152 session(s)).

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
_Report time: 2026-06-14T12:00:46Z_

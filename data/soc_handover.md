# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T14:15:12Z |
| **Shift Time** | 14:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **89** |
| Confirmed Threats | **86** |
| False Positives Filtered | **3** (3.4%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **10** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **3** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `GET / HTTP/1.1` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `Host: 129.80.119.236:23` | 2 |
| `123@@@` | 1 |
| `LeitboGi0ro` | 1 |
| `12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 2 |
| `root` | `123@@@` | 1 |
| `root` | `LeitboGi0ro` | 1 |
| `user` | `12345678` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `140.245.67.111` | 2026-06-13T11:44:53 |
| `root` | `LeitboGi0ro` | `140.245.67.111` | 2026-06-13T11:44:55 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.122` | 2026-06-13T11:58:14 |
| `user` | `12345678` | `50.46.141.125` | 2026-06-13T12:25:25 |
| `user` | `12345678~` | `50.46.141.125` | 2026-06-13T12:25:26 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.251.92.23` | 2026-06-13T12:25:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **89** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 6 |
| Paramiko (Python) | 2 |
| OpenSSH | 2 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `c8c5fbf80b7b...` | Mirai/variant | 2 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `c8c5fbf80b7b...` | OpenSSH | 2 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **17** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS20055` | Wholesail networks LLC | 1 | HIGH |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |
| `AS26599` | TELEFÔNICA BRASIL S.A | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ab210a2ad2d6

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-13 11:44 |
| **Last Seen** | 2026-06-13 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 11:44:52` | `cowrie.session.connect` |
| `2026-06-13 11:44:52` | `cowrie.client.version` |
| `2026-06-13 11:44:53` | `cowrie.client.kex` |
| `2026-06-13 11:44:53` | `cowrie.login.success` |
| `2026-06-13 11:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcbe6afab84f

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-13 11:44 |
| **Last Seen** | 2026-06-13 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 11:44:54` | `cowrie.session.connect` |
| `2026-06-13 11:44:54` | `cowrie.client.version` |
| `2026-06-13 11:44:54` | `cowrie.client.kex` |
| `2026-06-13 11:44:55` | `cowrie.login.success` |
| `2026-06-13 11:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dc5e910a81

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]122` |
| **First Seen** | 2026-06-13 11:58 |
| **Last Seen** | 2026-06-13 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 11:58:14` | `cowrie.session.connect` |
| `2026-06-13 11:58:14` | `cowrie.login.success` |
| `2026-06-13 11:58:15` | `cowrie.session.params` |
| `2026-06-13 11:58:15` | `cowrie.command.input` |
| `2026-06-13 11:58:15` | `cowrie.command.input` |
| `2026-06-13 11:58:15` | `cowrie.command.failed` |
| `2026-06-13 11:58:15` | `cowrie.command.input` |
| `2026-06-13 11:58:15` | `cowrie.command.failed` |
| `2026-06-13 11:58:15` | `cowrie.command.input` |
| `2026-06-13 11:58:15` | `cowrie.log.closed` |
| `2026-06-13 11:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]122` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d0584ede76

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-13 12:25 |
| **Last Seen** | 2026-06-13 12:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 12:25:24` | `cowrie.session.connect` |
| `2026-06-13 12:25:24` | `cowrie.client.version` |
| `2026-06-13 12:25:24` | `cowrie.client.kex` |
| `2026-06-13 12:25:25` | `cowrie.login.success` |
| `2026-06-13 12:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35aeea1b46e5

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-13 12:25 |
| **Last Seen** | 2026-06-13 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 12:25:25` | `cowrie.session.connect` |
| `2026-06-13 12:25:25` | `cowrie.client.version` |
| `2026-06-13 12:25:26` | `cowrie.client.kex` |
| `2026-06-13 12:25:26` | `cowrie.login.success` |
| `2026-06-13 12:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44078168b82c

| Field | Detail |
|---|---|
| **Source IP** | `47.251.92[.]23` |
| **First Seen** | 2026-06-13 12:25 |
| **Last Seen** | 2026-06-13 12:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 12:25:50` | `cowrie.session.connect` |
| `2026-06-13 12:25:50` | `cowrie.login.success` |
| `2026-06-13 12:25:50` | `cowrie.session.params` |
| `2026-06-13 12:25:50` | `cowrie.command.input` |
| `2026-06-13 12:25:50` | `cowrie.command.failed` |
| `2026-06-13 12:25:50` | `cowrie.command.input` |
| `2026-06-13 12:25:50` | `cowrie.command.failed` |
| `2026-06-13 12:25:50` | `cowrie.command.input` |
| `2026-06-13 12:25:53` | `cowrie.log.closed` |
| `2026-06-13 12:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.92[.]23` to AbuseIPDB if not already reported
- [ ] Block `47.251.92[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **43** | 2026-06-13 10:58 | 2026-06-13 12:50 | 31m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **10** | 2026-06-13 11:05 | 2026-06-13 12:41 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **4** | 2026-06-13 11:52 | 2026-06-13 12:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | **3** | 2026-06-13 12:37 | 2026-06-13 12:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.251.92[.]23` | **3** | 2026-06-13 12:25 | 2026-06-13 12:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-13 11:37 | 2026-06-13 12:36 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.36[.]234` | **2** | 2026-06-13 11:25 | 2026-06-13 11:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.169[.]214` | **2** | 2026-06-13 12:11 | 2026-06-13 12:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `82.207.50[.]182` | **2** | 2026-06-13 12:19 | 2026-06-13 12:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.168.218[.]19` | 1 | 2026-06-13 11:22 | 2026-06-13 11:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `198.199.94[.]79` | 1 | 2026-06-13 12:29 | 2026-06-13 12:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `2.187.251[.]104` | 1 | 2026-06-13 11:56 | 2026-06-13 11:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-13 11:38 | 2026-06-13 11:39 | 36s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-06-13 12:37 | 2026-06-13 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-06-13 12:38 | 2026-06-13 12:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-06-13 12:40 | 2026-06-13 12:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-13 12:54 | 2026-06-13 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.219.236[.]6` | 1 | 2026-06-13 11:47 | 2026-06-13 11:48 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `140.245.67[.]111` | KR | Oracle Corporation | **100** ⚠️ | 1 |
| `18.116.36[.]234` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `50.46.141[.]125` | US | Ziply Fiber | **100** ⚠️ | 20 |
| `172.235.40[.]131` | US | Linode | **100** ⚠️ | 50 |
| `188.168.218[.]19` | RU | Limited Liability Company TTK-Svyaz | **100** ⚠️ | 0 |
| `77.90.185[.]16` | LT | Limited Network LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 12 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 89 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 71 session(s)).

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
_Report time: 2026-06-13T14:15:12Z_

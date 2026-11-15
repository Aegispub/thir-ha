# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-15 |
| **Generated At** | 2026-11-15T18:13:37Z |
| **Shift Time** | 18:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **605** |
| Confirmed Threats | **548** |
| False Positives Filtered | **57** (9.4%) |
| Unique Attacker IPs | **319** |
| Countries of Origin | **53** |
| High Severity Cases | **418** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **187** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2095** |
| Unique Credential Pairs | **1444** |
| Unique Usernames | **461** |
| Unique Passwords | **1000** |
| Successful Auth Pairs | **1832** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 736 |
| `admin` | 148 |
| `support` | 62 |
| `ubuntu` | 49 |
| `guest` | 38 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 95 |
| `admin` | 70 |
| `root` | 58 |
| `123` | 49 |
| `1234` | 40 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 44 |
| `root` | `root` | 42 |
| `rootssssss23424123123` | `rootssssss23424123123` | 32 |
| `root` | `root3245gs5662d34111111111` | 28 |
| `support` | `support` | 27 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `deploy` | `deploy` | `109.160.32.116` | 2026-11-15T02:55:06 |
| `web` | `1` | `109.160.32.116` | 2026-11-15T02:55:11 |
| `ubnt` | `ubnt` | `10.0.0.73` | 2026-11-15T02:55:11 |
| `orange` | `orange` | `109.160.32.116` | 2026-11-15T02:55:15 |
| `ls` | `qwe123!@` | `109.160.32.116` | 2026-11-15T02:55:20 |
| `root` | `admin` | `10.0.0.73` | 2026-11-15T02:55:22 |
| `manager` | `friend` | `10.0.0.73` | 2026-11-15T02:55:24 |
| `root` | `admin1` | `109.160.32.116` | 2026-11-15T02:55:25 |
| `ftpuser1` | `123456` | `109.160.32.116` | 2026-11-15T02:55:30 |
| `cheryl` | `cheryl` | `109.160.32.116` | 2026-11-15T02:55:35 |
| `admin1` | `123123` | `109.160.32.116` | 2026-11-15T02:55:40 |
| `root` | `linevps` | `109.160.32.116` | 2026-11-15T02:55:44 |
| `user10` | `user10` | `109.160.32.116` | 2026-11-15T02:55:49 |
| `oracle` | `oracle123` | `109.160.32.116` | 2026-11-15T02:55:54 |
| `user1` | `pass123` | `109.160.32.116` | 2026-11-15T02:56:00 |
| `almalinux` | `almalinux` | `109.160.32.116` | 2026-11-15T02:56:05 |
| `ubnt` | `ubnt` | `80.94.95.118` | 2026-11-15T02:56:08 |
| `root` | `Wu889318!` | `109.160.32.116` | 2026-11-15T02:56:10 |
| `root` | `qwertyuiop1` | `109.160.32.116` | 2026-11-15T02:56:15 |
| `runner` | `1234` | `109.160.32.116` | 2026-11-15T02:56:20 |
_… 1812 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **605** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 221 |
| OpenSSH | 156 |
| libssh | 32 |
| Unknown | 8 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 145 | 136 |
| `2ec37a7cc8da...` | Mirai/variant | 118 | 3 |
| `16443846184e...` | Generic scanner | 43 | 4 |
| `f555226df196...` | Mirai/variant | 28 | 15 |
| `7d01d047ace6...` | Mirai/variant | 24 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 145 | 136 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 118 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 43 | 4 | Generic scanner |
| `f555226df196...` | libssh | 28 | 15 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 24 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 11 | 6 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 5 | 5 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **140** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1059.004, T1082, T1592, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 25 | 14 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
cat /proc/cpuinfo
```
```
uname -m
```
```
dd if=/bin/busybox bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n' || dd if=/bin/sh bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n'
```
```
file /bin/busybox 2>/dev/null || file /bin/sh 2>/dev/null
```
Source IPs: `180.93.193.100`

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `50.6.201.228`, `118.107.139.224`, `103.78.1.160`, `122.168.123.73`, `115.191.38.87`, `117.50.44.85`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **319** |
| Unique ASNs | **145** |
| High-Risk ASNs | **129** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 76 | HIGH |
| `AS4766` | Korea Telecom | 16 | HIGH |
| `AS22773` | Cox Communications Inc. | 12 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS15169` | Google LLC | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS18881` | TELEFÔNICA BRASIL S.A | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (409)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eef0a8aadf24

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]116` |
| **First Seen** | 2026-11-15 02:55 |
| **Last Seen** | 2026-11-15 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:55:05` | `cowrie.session.connect` |
| `2026-11-15 02:55:05` | `cowrie.client.version` |
| `2026-11-15 02:55:05` | `cowrie.client.kex` |
| `2026-11-15 02:55:06` | `cowrie.login.success` |
| `2026-11-15 02:55:07` | `cowrie.session.params` |
| `2026-11-15 02:55:07` | `cowrie.command.input` |
| `2026-11-15 02:55:07` | `cowrie.log.closed` |
| `2026-11-15 02:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]116` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963be259916e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-15 02:56 |
| **Last Seen** | 2026-11-15 02:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:56:06` | `cowrie.session.connect` |
| `2026-11-15 02:56:06` | `cowrie.client.version` |
| `2026-11-15 02:56:07` | `cowrie.client.kex` |
| `2026-11-15 02:56:08` | `cowrie.login.success` |
| `2026-11-15 02:56:08` | `cowrie.direct-tcpip.request` |
| `2026-11-15 02:56:08` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 02:56:08` | `cowrie.direct-tcpip.data` |
| `2026-11-15 02:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448fdc6200f8

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-15 02:56 |
| **Last Seen** | 2026-11-15 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:56:21` | `cowrie.session.connect` |
| `2026-11-15 02:56:21` | `cowrie.client.version` |
| `2026-11-15 02:56:21` | `cowrie.client.kex` |
| `2026-11-15 02:56:21` | `cowrie.login.success` |
| `2026-11-15 02:56:21` | `cowrie.direct-tcpip.request` |
| `2026-11-15 02:56:22` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 02:56:22` | `cowrie.direct-tcpip.data` |
| `2026-11-15 02:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1311a522b7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 02:56 |
| **Last Seen** | 2026-11-15 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_80b2403d55ef842d6c49d24b9bfa2af2_small_control'"'"' '"'"'check_80b2403d55ef842d6c49d24b9bfa2af2'"'"'', printf '\n%s|%s\n' 'check_80b2403d55ef842d6c49d24b9bfa2af2_small_control' 'check_80b2403d55ef842d6c49d24b9bfa2af2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_80b2403d55ef842d6c49d24b9bfa2af2_small_math'"'"' "$((46*590+64))"', (46*590+64, printf '\n%s|%s\n' 'check_80b2403d55ef842d6c49d24b9bfa2af2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:56:38` | `cowrie.session.connect` |
| `2026-11-15 02:56:38` | `cowrie.client.version` |
| `2026-11-15 02:56:38` | `cowrie.client.kex` |
| `2026-11-15 02:56:40` | `cowrie.login.success` |
| `2026-11-15 02:56:42` | `cowrie.client.size` |
| `2026-11-15 02:56:43` | `cowrie.session.params` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| `2026-11-15 02:56:44` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e03364fd8c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-15 02:56 |
| **Last Seen** | 2026-11-15 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:56:48` | `cowrie.session.connect` |
| `2026-11-15 02:56:48` | `cowrie.client.version` |
| `2026-11-15 02:56:48` | `cowrie.client.kex` |
| `2026-11-15 02:56:49` | `cowrie.login.success` |
| `2026-11-15 02:56:49` | `cowrie.direct-tcpip.request` |
| `2026-11-15 02:56:49` | `cowrie.direct-tcpip.ja4` |
| `2026-11-15 02:56:49` | `cowrie.direct-tcpip.data` |
| `2026-11-15 02:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17e6388fabb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 02:58 |
| **Last Seen** | 2026-11-15 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_125dbd0a288f77569e2375ce45e1d910_small_control'"'"' '"'"'check_125dbd0a288f77569e2375ce45e1d910'"'"'', printf '\n%s|%s\n' 'check_125dbd0a288f77569e2375ce45e1d910_small_control' 'check_125dbd0a288f77569e2375ce45e1d910', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_125dbd0a288f77569e2375ce45e1d910_small_math'"'"' "$((714*827+46))"', (714*827+46, printf '\n%s|%s\n' 'check_125dbd0a288f77569e2375ce45e1d910_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 02:58:29` | `cowrie.session.connect` |
| `2026-11-15 02:58:29` | `cowrie.client.version` |
| `2026-11-15 02:58:29` | `cowrie.client.kex` |
| `2026-11-15 02:58:32` | `cowrie.login.success` |
| `2026-11-15 02:58:34` | `cowrie.client.size` |
| `2026-11-15 02:58:34` | `cowrie.session.params` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| `2026-11-15 02:58:35` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8517a5784f52

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:00 |
| **Last Seen** | 2026-11-15 03:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_41318e9521ab3db2b9056874bf9942a8_small_control'"'"' '"'"'check_41318e9521ab3db2b9056874bf9942a8'"'"'', printf '\n%s|%s\n' 'check_41318e9521ab3db2b9056874bf9942a8_small_control' 'check_41318e9521ab3db2b9056874bf9942a8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_41318e9521ab3db2b9056874bf9942a8_small_math'"'"' "$((738*826+6))"', (738*826+6, printf '\n%s|%s\n' 'check_41318e9521ab3db2b9056874bf9942a8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:00:20` | `cowrie.session.connect` |
| `2026-11-15 03:00:20` | `cowrie.client.version` |
| `2026-11-15 03:00:20` | `cowrie.client.kex` |
| `2026-11-15 03:00:22` | `cowrie.login.success` |
| `2026-11-15 03:00:24` | `cowrie.client.size` |
| `2026-11-15 03:00:25` | `cowrie.session.params` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| `2026-11-15 03:00:26` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135ef448cc5b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-15 03:01 |
| **Last Seen** | 2026-11-15 03:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:01:12` | `cowrie.session.connect` |
| `2026-11-15 03:01:12` | `cowrie.login.success` |
| `2026-11-15 03:01:13` | `cowrie.session.params` |
| `2026-11-15 03:01:14` | `cowrie.log.closed` |
| `2026-11-15 03:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea6a2170bff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:02 |
| **Last Seen** | 2026-11-15 03:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_05964d2cdde2803c1a9613c5ffd8a4a4_small_control'"'"' '"'"'check_05964d2cdde2803c1a9613c5ffd8a4a4'"'"'', printf '\n%s|%s\n' 'check_05964d2cdde2803c1a9613c5ffd8a4a4_small_control' 'check_05964d2cdde2803c1a9613c5ffd8a4a4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_05964d2cdde2803c1a9613c5ffd8a4a4_small_math'"'"' "$((434*928+73))"', (434*928+73, printf '\n%s|%s\n' 'check_05964d2cdde2803c1a9613c5ffd8a4a4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:02:10` | `cowrie.session.connect` |
| `2026-11-15 03:02:10` | `cowrie.client.version` |
| `2026-11-15 03:02:10` | `cowrie.client.kex` |
| `2026-11-15 03:02:13` | `cowrie.login.success` |
| `2026-11-15 03:02:14` | `cowrie.client.size` |
| `2026-11-15 03:02:15` | `cowrie.session.params` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| `2026-11-15 03:02:16` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661ebbd45876

| Field | Detail |
|---|---|
| **Source IP** | `103.12.197[.]122` |
| **First Seen** | 2026-11-15 03:04 |
| **Last Seen** | 2026-11-15 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:04:53` | `cowrie.session.connect` |
| `2026-11-15 03:04:54` | `cowrie.client.version` |
| `2026-11-15 03:04:54` | `cowrie.client.kex` |
| `2026-11-15 03:04:56` | `cowrie.login.success` |
| `2026-11-15 03:04:56` | `cowrie.direct-tcpip.request` |
| `2026-11-15 03:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.12.197[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.12.197[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de908e0eaf8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:05 |
| **Last Seen** | 2026-11-15 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8efb5b0edd2bc55f73c87885d7a91b2d_small_control'"'"' '"'"'check_8efb5b0edd2bc55f73c87885d7a91b2d'"'"'', printf '\n%s|%s\n' 'check_8efb5b0edd2bc55f73c87885d7a91b2d_small_control' 'check_8efb5b0edd2bc55f73c87885d7a91b2d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8efb5b0edd2bc55f73c87885d7a91b2d_small_math'"'"' "$((712*518+35))"', (712*518+35, printf '\n%s|%s\n' 'check_8efb5b0edd2bc55f73c87885d7a91b2d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:05:48` | `cowrie.session.connect` |
| `2026-11-15 03:05:49` | `cowrie.client.version` |
| `2026-11-15 03:05:49` | `cowrie.client.kex` |
| `2026-11-15 03:05:51` | `cowrie.login.success` |
| `2026-11-15 03:05:52` | `cowrie.client.size` |
| `2026-11-15 03:05:53` | `cowrie.session.params` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| `2026-11-15 03:05:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7719d7d68e5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:07 |
| **Last Seen** | 2026-11-15 03:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b91777fd750e350f81dd7a72e28d400c_small_control'"'"' '"'"'check_b91777fd750e350f81dd7a72e28d400c'"'"'', printf '\n%s|%s\n' 'check_b91777fd750e350f81dd7a72e28d400c_small_control' 'check_b91777fd750e350f81dd7a72e28d400c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b91777fd750e350f81dd7a72e28d400c_small_math'"'"' "$((525*988+48))"', (525*988+48, printf '\n%s|%s\n' 'check_b91777fd750e350f81dd7a72e28d400c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:07:37` | `cowrie.session.connect` |
| `2026-11-15 03:07:37` | `cowrie.client.version` |
| `2026-11-15 03:07:37` | `cowrie.client.kex` |
| `2026-11-15 03:07:39` | `cowrie.login.success` |
| `2026-11-15 03:07:41` | `cowrie.client.size` |
| `2026-11-15 03:07:42` | `cowrie.session.params` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| `2026-11-15 03:07:42` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ac94f16df9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:09 |
| **Last Seen** | 2026-11-15 03:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9e6a733b7fa6208d6b8ce1ac61070d68_small_control'"'"' '"'"'check_9e6a733b7fa6208d6b8ce1ac61070d68'"'"'', printf '\n%s|%s\n' 'check_9e6a733b7fa6208d6b8ce1ac61070d68_small_control' 'check_9e6a733b7fa6208d6b8ce1ac61070d68', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9e6a733b7fa6208d6b8ce1ac61070d68_small_math'"'"' "$((675*761+9))"', (675*761+9, printf '\n%s|%s\n' 'check_9e6a733b7fa6208d6b8ce1ac61070d68_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:09:24` | `cowrie.session.connect` |
| `2026-11-15 03:09:25` | `cowrie.client.version` |
| `2026-11-15 03:09:25` | `cowrie.client.kex` |
| `2026-11-15 03:09:26` | `cowrie.login.success` |
| `2026-11-15 03:09:28` | `cowrie.client.size` |
| `2026-11-15 03:09:29` | `cowrie.session.params` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| `2026-11-15 03:09:29` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8274311a8d5b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:11 |
| **Last Seen** | 2026-11-15 03:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_818d1dc7d835027c5851735ec2097b6a_small_control'"'"' '"'"'check_818d1dc7d835027c5851735ec2097b6a'"'"'', printf '\n%s|%s\n' 'check_818d1dc7d835027c5851735ec2097b6a_small_control' 'check_818d1dc7d835027c5851735ec2097b6a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_818d1dc7d835027c5851735ec2097b6a_small_math'"'"' "$((265*687+89))"', (265*687+89, printf '\n%s|%s\n' 'check_818d1dc7d835027c5851735ec2097b6a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:11:15` | `cowrie.session.connect` |
| `2026-11-15 03:11:15` | `cowrie.client.version` |
| `2026-11-15 03:11:16` | `cowrie.client.kex` |
| `2026-11-15 03:11:17` | `cowrie.login.success` |
| `2026-11-15 03:11:19` | `cowrie.client.size` |
| `2026-11-15 03:11:20` | `cowrie.session.params` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| `2026-11-15 03:11:21` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e452953fb827

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-15 03:12 |
| **Last Seen** | 2026-11-15 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:12:10` | `cowrie.session.connect` |
| `2026-11-15 03:12:10` | `cowrie.login.success` |
| `2026-11-15 03:12:11` | `cowrie.session.params` |
| `2026-11-15 03:12:11` | `cowrie.log.closed` |
| `2026-11-15 03:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8bf111fc6d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:13 |
| **Last Seen** | 2026-11-15 03:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0870bcdd9b4f5cb7b8f659144c9683f8_small_control'"'"' '"'"'check_0870bcdd9b4f5cb7b8f659144c9683f8'"'"'', printf '\n%s|%s\n' 'check_0870bcdd9b4f5cb7b8f659144c9683f8_small_control' 'check_0870bcdd9b4f5cb7b8f659144c9683f8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0870bcdd9b4f5cb7b8f659144c9683f8_small_math'"'"' "$((167*782+27))"', (167*782+27, printf '\n%s|%s\n' 'check_0870bcdd9b4f5cb7b8f659144c9683f8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:13:09` | `cowrie.session.connect` |
| `2026-11-15 03:13:09` | `cowrie.client.version` |
| `2026-11-15 03:13:09` | `cowrie.client.kex` |
| `2026-11-15 03:13:13` | `cowrie.login.success` |
| `2026-11-15 03:13:14` | `cowrie.client.size` |
| `2026-11-15 03:13:15` | `cowrie.session.params` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:15` | `cowrie.command.input` |
| `2026-11-15 03:13:16` | `cowrie.command.input` |
| `2026-11-15 03:13:16` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-024b2f325009

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-15 03:13 |
| **Last Seen** | 2026-11-15 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:13:20` | `cowrie.session.connect` |
| `2026-11-15 03:13:20` | `cowrie.client.version` |
| `2026-11-15 03:13:20` | `cowrie.client.kex` |
| `2026-11-15 03:13:20` | `cowrie.login.success` |
| `2026-11-15 03:13:21` | `cowrie.direct-tcpip.request` |
| `2026-11-15 03:13:21` | `cowrie.direct-tcpip.data` |
| `2026-11-15 03:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6c81d4e9c2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:15 |
| **Last Seen** | 2026-11-15 03:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_811d58f357dab8bb0a14072324c0056c_small_control'"'"' '"'"'check_811d58f357dab8bb0a14072324c0056c'"'"'', printf '\n%s|%s\n' 'check_811d58f357dab8bb0a14072324c0056c_small_control' 'check_811d58f357dab8bb0a14072324c0056c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_811d58f357dab8bb0a14072324c0056c_small_math'"'"' "$((153*970+74))"', (153*970+74, printf '\n%s|%s\n' 'check_811d58f357dab8bb0a14072324c0056c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:15:03` | `cowrie.session.connect` |
| `2026-11-15 03:15:03` | `cowrie.client.version` |
| `2026-11-15 03:15:03` | `cowrie.client.kex` |
| `2026-11-15 03:15:05` | `cowrie.login.success` |
| `2026-11-15 03:15:07` | `cowrie.client.size` |
| `2026-11-15 03:15:07` | `cowrie.session.params` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| `2026-11-15 03:15:08` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c929ec6f855a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:16 |
| **Last Seen** | 2026-11-15 03:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6524fd7c51e71a0f4c928d6624062837_small_control'"'"' '"'"'check_6524fd7c51e71a0f4c928d6624062837'"'"'', printf '\n%s|%s\n' 'check_6524fd7c51e71a0f4c928d6624062837_small_control' 'check_6524fd7c51e71a0f4c928d6624062837', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6524fd7c51e71a0f4c928d6624062837_small_math'"'"' "$((968*478+91))"', (968*478+91, printf '\n%s|%s\n' 'check_6524fd7c51e71a0f4c928d6624062837_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:16:58` | `cowrie.session.connect` |
| `2026-11-15 03:16:58` | `cowrie.client.version` |
| `2026-11-15 03:16:58` | `cowrie.client.kex` |
| `2026-11-15 03:17:00` | `cowrie.login.success` |
| `2026-11-15 03:17:01` | `cowrie.client.size` |
| `2026-11-15 03:17:01` | `cowrie.session.params` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| `2026-11-15 03:17:02` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f012d077104

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:18 |
| **Last Seen** | 2026-11-15 03:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_765c7074cfc50c828b4f653f87b15362_small_control'"'"' '"'"'check_765c7074cfc50c828b4f653f87b15362'"'"'', printf '\n%s|%s\n' 'check_765c7074cfc50c828b4f653f87b15362_small_control' 'check_765c7074cfc50c828b4f653f87b15362', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_765c7074cfc50c828b4f653f87b15362_small_math'"'"' "$((391*50+37))"', (391*50+37, printf '\n%s|%s\n' 'check_765c7074cfc50c828b4f653f87b15362_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:18:55` | `cowrie.session.connect` |
| `2026-11-15 03:18:55` | `cowrie.client.version` |
| `2026-11-15 03:18:55` | `cowrie.client.kex` |
| `2026-11-15 03:18:57` | `cowrie.login.success` |
| `2026-11-15 03:18:58` | `cowrie.client.size` |
| `2026-11-15 03:18:59` | `cowrie.session.params` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| `2026-11-15 03:18:59` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5669262e0b7e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:20 |
| **Last Seen** | 2026-11-15 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_de7dab68b55c63c39d3ac5033c676922_small_control'"'"' '"'"'check_de7dab68b55c63c39d3ac5033c676922'"'"'', printf '\n%s|%s\n' 'check_de7dab68b55c63c39d3ac5033c676922_small_control' 'check_de7dab68b55c63c39d3ac5033c676922', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_de7dab68b55c63c39d3ac5033c676922_small_math'"'"' "$((129*277+19))"', (129*277+19, printf '\n%s|%s\n' 'check_de7dab68b55c63c39d3ac5033c676922_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:20:51` | `cowrie.session.connect` |
| `2026-11-15 03:20:51` | `cowrie.client.version` |
| `2026-11-15 03:20:51` | `cowrie.client.kex` |
| `2026-11-15 03:20:52` | `cowrie.login.success` |
| `2026-11-15 03:20:54` | `cowrie.client.size` |
| `2026-11-15 03:20:55` | `cowrie.session.params` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| `2026-11-15 03:20:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712191d5bf2a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:22 |
| **Last Seen** | 2026-11-15 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_275ac663ef5271182602d2361053da85_small_control'"'"' '"'"'check_275ac663ef5271182602d2361053da85'"'"'', printf '\n%s|%s\n' 'check_275ac663ef5271182602d2361053da85_small_control' 'check_275ac663ef5271182602d2361053da85', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_275ac663ef5271182602d2361053da85_small_math'"'"' "$((105*247+84))"', (105*247+84, printf '\n%s|%s\n' 'check_275ac663ef5271182602d2361053da85_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:22:42` | `cowrie.session.connect` |
| `2026-11-15 03:22:42` | `cowrie.client.version` |
| `2026-11-15 03:22:42` | `cowrie.client.kex` |
| `2026-11-15 03:22:43` | `cowrie.login.success` |
| `2026-11-15 03:22:44` | `cowrie.client.size` |
| `2026-11-15 03:22:45` | `cowrie.session.params` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| `2026-11-15 03:22:45` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c560fab6eb6a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:24 |
| **Last Seen** | 2026-11-15 03:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60273683732fb99246d1e80b764342f9_small_control'"'"' '"'"'check_60273683732fb99246d1e80b764342f9'"'"'', printf '\n%s|%s\n' 'check_60273683732fb99246d1e80b764342f9_small_control' 'check_60273683732fb99246d1e80b764342f9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60273683732fb99246d1e80b764342f9_small_math'"'"' "$((688*82+75))"', (688*82+75, printf '\n%s|%s\n' 'check_60273683732fb99246d1e80b764342f9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:24:31` | `cowrie.session.connect` |
| `2026-11-15 03:24:31` | `cowrie.client.version` |
| `2026-11-15 03:24:31` | `cowrie.client.kex` |
| `2026-11-15 03:24:32` | `cowrie.login.success` |
| `2026-11-15 03:24:33` | `cowrie.client.size` |
| `2026-11-15 03:24:34` | `cowrie.session.params` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| `2026-11-15 03:24:35` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d677e9263b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:26 |
| **Last Seen** | 2026-11-15 03:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d2413f1dbf64aa38752edf9dd27354f8_small_control'"'"' '"'"'check_d2413f1dbf64aa38752edf9dd27354f8'"'"'', printf '\n%s|%s\n' 'check_d2413f1dbf64aa38752edf9dd27354f8_small_control' 'check_d2413f1dbf64aa38752edf9dd27354f8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d2413f1dbf64aa38752edf9dd27354f8_small_math'"'"' "$((985*302+88))"', (985*302+88, printf '\n%s|%s\n' 'check_d2413f1dbf64aa38752edf9dd27354f8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:26:23` | `cowrie.session.connect` |
| `2026-11-15 03:26:23` | `cowrie.client.version` |
| `2026-11-15 03:26:23` | `cowrie.client.kex` |
| `2026-11-15 03:26:24` | `cowrie.login.success` |
| `2026-11-15 03:26:25` | `cowrie.client.size` |
| `2026-11-15 03:26:25` | `cowrie.session.params` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| `2026-11-15 03:26:26` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986cb3255145

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-11-15 03:28 |
| **Last Seen** | 2026-11-15 03:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0a8c4c59f4a767b0108703d87122704a_small_control'"'"' '"'"'check_0a8c4c59f4a767b0108703d87122704a'"'"'', printf '\n%s|%s\n' 'check_0a8c4c59f4a767b0108703d87122704a_small_control' 'check_0a8c4c59f4a767b0108703d87122704a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0a8c4c59f4a767b0108703d87122704a_small_math'"'"' "$((707*717+82))"', (707*717+82, printf '\n%s|%s\n' 'check_0a8c4c59f4a767b0108703d87122704a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-15 03:28:13` | `cowrie.session.connect` |
| `2026-11-15 03:28:14` | `cowrie.client.version` |
| `2026-11-15 03:28:14` | `cowrie.client.kex` |
| `2026-11-15 03:28:15` | `cowrie.login.success` |
| `2026-11-15 03:28:16` | `cowrie.client.size` |
| `2026-11-15 03:28:16` | `cowrie.session.params` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:16` | `cowrie.command.input` |
| `2026-11-15 03:28:17` | `cowrie.command.input` |
| `2026-11-15 03:28:17` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (384) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-7622c56480fd | HIGH | `2.57.122[.]168` | 2026-11-15 03:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2f94ea855397 | HIGH | `2.57.122[.]168` | 2026-11-15 03:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e721a91dbb1e | HIGH | `2.57.122[.]168` | 2026-11-15 03:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0ea4173c7784 | HIGH | `2.57.122[.]168` | 2026-11-15 03:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d9c2d69eacaa | HIGH | `77.53.79[.]11` | 2026-11-15 03:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1bea1aadc5a5 | HIGH | `83.166.50[.]15` | 2026-11-15 03:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11892f6cb040 | HIGH | `2.57.122[.]168` | 2026-11-15 03:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6951a15071a3 | HIGH | `2.57.122[.]168` | 2026-11-15 03:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3114c68e2dd3 | HIGH | `2.57.122[.]168` | 2026-11-15 03:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c80eedba3456 | HIGH | `2.57.122[.]168` | 2026-11-15 03:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-11dfab37d723 | HIGH | `112.53.123[.]118` | 2026-11-15 03:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7023234ac611 | HIGH | `2.57.122[.]168` | 2026-11-15 03:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-86c4c700a37e | HIGH | `2.57.122[.]168` | 2026-11-15 03:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5268e67194e6 | HIGH | `191.7.159[.]201` | 2026-11-15 03:55 | Y | 1 | 0 | `T1078 · T1592` |
| IR-55926d51ca6f | HIGH | `125.130.102[.]172` | 2026-11-15 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-add8c9627754 | HIGH | `1.172.102[.]101` | 2026-11-15 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ac46d896d66a | HIGH | `109.160.32[.]116` | 2026-11-15 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-12b55c6d5880 | HIGH | `191.7.159[.]201` | 2026-11-15 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4aeedbc571a4 | HIGH | `181.95.241[.]200` | 2026-11-15 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4a31e964fff9 | HIGH | `38.186.75[.]113` | 2026-11-15 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-adc36a2a4130 | HIGH | `191.7.159[.]201` | 2026-11-15 04:07 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-ed74ca9fb987 | HIGH | `37.157.111[.]122` | 2026-11-15 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74db13091bb2 | HIGH | `73.183.115[.]109` | 2026-11-15 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5185946c1145 | HIGH | `195.178.110[.]78` | 2026-11-15 04:11 | Y | 0 | 0 | `T1078` |
| IR-9e289be3b60a | HIGH | `78.128.112[.]74` | 2026-11-15 04:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-179238ccea5d | HIGH | `191.7.159[.]201` | 2026-11-15 04:17 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-5ff73e1385b4 | HIGH | `77.239.124[.]252` | 2026-11-15 04:18 | Y | 0 | 0 | `T1078` |
| IR-bd691d2d43ac | HIGH | `176.53.159[.]196` | 2026-11-15 04:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7a5350d4703 | HIGH | `216.232.226[.]217` | 2026-11-15 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1146081c9503 | HIGH | `136.56.34[.]147` | 2026-11-15 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fb20887b370 | HIGH | `191.7.159[.]201` | 2026-11-15 04:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bb532df80505 | HIGH | `122.168.123[.]73` | 2026-11-15 04:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3826694eee4d | HIGH | `122.168.123[.]73` | 2026-11-15 04:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-00f12474096b | HIGH | `182.70.254[.]196` | 2026-11-15 04:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3ff127a0a8d7 | HIGH | `193.32.162[.]15` | 2026-11-15 04:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-480e6ded36b8 | HIGH | `191.7.159[.]201` | 2026-11-15 04:49 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-cb222c9a6c23 | HIGH | `217.211.237[.]213` | 2026-11-15 04:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b9e79c20dd96 | HIGH | `125.69.76[.]148` | 2026-11-15 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-37cb3ee61e26 | HIGH | `195.178.110[.]26` | 2026-11-15 04:53 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3329adf70c19 | HIGH | `80.94.95[.]118` | 2026-11-15 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01a2c76220a4 | HIGH | `138.226.239[.]233` | 2026-11-15 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-abf813e8e6e7 | HIGH | `77.90.185[.]29` | 2026-11-15 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bb84de539b7b | HIGH | `111.70.49[.]182` | 2026-11-15 05:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79b17b11b156 | HIGH | `196.188.93[.]169` | 2026-11-15 05:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1084683993f2 | HIGH | `222.75.225[.]206` | 2026-11-15 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f228b38491f7 | HIGH | `185.255.212[.]178` | 2026-11-15 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c46228d08055 | HIGH | `70.167.235[.]132` | 2026-11-15 05:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f27d3f99a652 | HIGH | `78.70.41[.]148` | 2026-11-15 05:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c9cbaf98550 | HIGH | `191.7.159[.]201` | 2026-11-15 05:08 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-1b925b2c88a9 | HIGH | `182.95.181[.]50` | 2026-11-15 05:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-905cd3a4dac6 | HIGH | `191.7.159[.]201` | 2026-11-15 05:27 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-75896b20d636 | HIGH | `220.246.47[.]169` | 2026-11-15 05:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad9317ad0eda | HIGH | `156.229.21[.]54` | 2026-11-15 05:44 | Y | 0 | 0 | `T1078` |
| IR-c1608833b7af | HIGH | `156.229.21[.]54` | 2026-11-15 05:45 | Y | 2 | 0 | `T1078` |
| IR-9d68be238e85 | HIGH | `191.7.159[.]201` | 2026-11-15 05:47 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-6fa08889da95 | HIGH | `117.50.44[.]85` | 2026-11-15 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a4126b38f113 | HIGH | `195.178.110[.]26` | 2026-11-15 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-59ee9a8d05ef | HIGH | `187.16.96[.]250` | 2026-11-15 06:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-796934705313 | HIGH | `187.16.96[.]250` | 2026-11-15 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c2c53b56909 | HIGH | `191.7.159[.]201` | 2026-11-15 06:07 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-fa6c0844acf8 | HIGH | `80.94.92[.]55` | 2026-11-15 06:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-75158cda3236 | HIGH | `201.86.46[.]145` | 2026-11-15 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6cbebbaab4a | HIGH | `80.94.92[.]55` | 2026-11-15 06:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4cbed7fbca68 | HIGH | `77.239.124[.]252` | 2026-11-15 06:18 | Y | 0 | 0 | `T1078` |
| IR-f23dc2124913 | HIGH | `80.94.92[.]55` | 2026-11-15 06:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dcb45e000f01 | HIGH | `80.94.92[.]55` | 2026-11-15 06:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-afe52e772545 | HIGH | `172.184.111[.]202` | 2026-11-15 06:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0c74042f58a0 | HIGH | `172.184.111[.]202` | 2026-11-15 06:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-39b1f5a02e01 | HIGH | `180.93.193[.]100` | 2026-11-15 06:24 | Y | 6 | 0 | `T1059.004 · T1078 · T1083` |
| IR-54ac3e97feba | HIGH | `217.208.90[.]253` | 2026-11-15 06:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79062afca0c6 | HIGH | `80.94.92[.]55` | 2026-11-15 06:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-20361e33ceea | HIGH | `191.7.159[.]201` | 2026-11-15 06:27 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-8808d66a3b3e | HIGH | `78.66.44[.]23` | 2026-11-15 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01a8a48cfd65 | HIGH | `222.174.184[.]86` | 2026-11-15 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ba10f9a49ca | HIGH | `176.53.159[.]196` | 2026-11-15 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2058146dbb3 | HIGH | `80.94.92[.]55` | 2026-11-15 06:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bcce5e6e4dd4 | HIGH | `80.94.92[.]55` | 2026-11-15 06:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d296c5a748e2 | HIGH | `80.94.92[.]55` | 2026-11-15 06:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-568cddb6750d | HIGH | `79.162.203[.]47` | 2026-11-15 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7732c62cd7cb | HIGH | `116.230.66[.]189` | 2026-11-15 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-503d8c25eb38 | HIGH | `80.94.92[.]55` | 2026-11-15 06:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f415c8412cc8 | HIGH | `197.5.145[.]150` | 2026-11-15 06:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c9fa9475ecce | HIGH | `197.5.145[.]150` | 2026-11-15 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cbd066f86378 | HIGH | `80.94.92[.]55` | 2026-11-15 06:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-336bf26c3c65 | HIGH | `80.94.92[.]55` | 2026-11-15 06:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ddfcab384f83 | HIGH | `191.7.159[.]201` | 2026-11-15 06:47 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-fe02f67f4a32 | HIGH | `80.94.92[.]55` | 2026-11-15 06:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f28ebb1464b0 | HIGH | `14.145.200[.]69` | 2026-11-15 06:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-919c3be890f5 | HIGH | `78.70.41[.]148` | 2026-11-15 06:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc4cb3bec418 | HIGH | `80.94.92[.]55` | 2026-11-15 06:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6fb9483b8b0c | HIGH | `80.94.92[.]55` | 2026-11-15 06:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-712509268267 | HIGH | `160.119.66[.]206` | 2026-11-15 07:00 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-33a00f9ed3e3 | HIGH | `160.119.66[.]206` | 2026-11-15 07:00 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-8e8185857449 | HIGH | `80.94.92[.]55` | 2026-11-15 07:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4cd4694854c8 | HIGH | `138.226.239[.]234` | 2026-11-15 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0301b2da48e9 | HIGH | `77.90.185[.]29` | 2026-11-15 07:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8980bfc2b11 | HIGH | `80.94.95[.]118` | 2026-11-15 07:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7b5884b459a | HIGH | `80.94.92[.]55` | 2026-11-15 07:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-99c3e6dc8c4b | HIGH | `115.191.38[.]87` | 2026-11-15 07:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-551794b4423b | HIGH | `115.191.38[.]87` | 2026-11-15 07:06 | Y | 0 | 0 | `T1078 · T1592` |
_… 284 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.208[.]221` | **3** | 2026-11-15 02:55 | 2026-11-15 06:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **3** | 2026-11-15 07:14 | 2026-11-15 10:12 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-15 12:47 | 2026-11-15 16:00 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-15 15:56 | 2026-11-15 16:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-15 03:12 | 2026-11-15 04:11 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-15 15:05 | 2026-11-15 16:20 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-15 03:01 | 2026-11-15 04:18 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-15 06:18 | 2026-11-15 08:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-11-15 11:54 | 2026-11-15 12:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.217.247[.]153` | 1 | 2026-11-15 03:24 | 2026-11-15 03:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.124.135[.]239` | 1 | 2026-11-15 08:33 | 2026-11-15 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.137[.]17` | 1 | 2026-11-15 06:57 | 2026-11-15 06:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]110` | 1 | 2026-11-15 16:41 | 2026-11-15 16:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]116` | 1 | 2026-11-15 03:09 | 2026-11-15 03:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.28.153[.]193` | 1 | 2026-11-15 11:40 | 2026-11-15 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.45.141[.]72` | 1 | 2026-11-15 06:55 | 2026-11-15 06:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.53.123[.]118` | 1 | 2026-11-15 03:10 | 2026-11-15 03:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.42.70[.]26` | 1 | 2026-11-15 09:17 | 2026-11-15 09:17 | 15s | 0 | `T1592` | 🟢 LOW |
| `116.147.151[.]46` | 1 | 2026-11-15 07:46 | 2026-11-15 07:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.59.15[.]123` | 1 | 2026-11-15 11:30 | 2026-11-15 11:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `117.72.81[.]242` | 1 | 2026-11-15 08:55 | 2026-11-15 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.86[.]156` | 1 | 2026-11-15 16:45 | 2026-11-15 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.167.57[.]19` | 1 | 2026-11-15 11:19 | 2026-11-15 11:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `123.163.52[.]74` | 1 | 2026-11-15 13:53 | 2026-11-15 13:53 | 49s | 0 | `T1592` | 🟢 LOW |
| `123.57.212[.]79` | 1 | 2026-11-15 05:21 | 2026-11-15 05:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `138.226.239[.]7` | 1 | 2026-11-15 05:21 | 2026-11-15 05:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `146.120.251[.]229` | 1 | 2026-11-15 08:43 | 2026-11-15 08:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `146.168.191[.]176` | 1 | 2026-11-15 13:52 | 2026-11-15 13:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `151.237.28[.]235` | 1 | 2026-11-15 12:50 | 2026-11-15 12:50 | 28s | 0 | `T1592` | 🟢 LOW |
| `156.229.21[.]54` | 1 | 2026-11-15 05:44 | 2026-11-15 05:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.230.208[.]221` | 1 | 2026-11-15 08:09 | 2026-11-15 08:09 | 32s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-15 16:29 | 2026-11-15 16:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.195.25[.]35` | 1 | 2026-11-15 03:45 | 2026-11-15 03:46 | 33s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]245` | 1 | 2026-11-15 08:32 | 2026-11-15 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.245.19[.]230` | 1 | 2026-11-15 08:26 | 2026-11-15 08:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.203.243[.]177` | 1 | 2026-11-15 06:12 | 2026-11-15 06:13 | 16s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-11-15 08:54 | 2026-11-15 08:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.37.170[.]132` | 1 | 2026-11-15 08:57 | 2026-11-15 08:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.0.225[.]227` | 1 | 2026-11-15 15:04 | 2026-11-15 15:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-15 06:29 | 2026-11-15 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-11-15 06:24 | 2026-11-15 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.92.204[.]124` | 1 | 2026-11-15 08:50 | 2026-11-15 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.159.162[.]210` | 1 | 2026-11-15 15:13 | 2026-11-15 15:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.177.72[.]64` | 1 | 2026-11-15 13:22 | 2026-11-15 13:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.41.177[.]58` | 1 | 2026-11-15 13:02 | 2026-11-15 13:02 | 34s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-15 06:15 | 2026-11-15 06:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-15 04:42 | 2026-11-15 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-15 15:04 | 2026-11-15 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-15 10:04 | 2026-11-15 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]6` | 1 | 2026-11-15 04:34 | 2026-11-15 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-15 10:13 | 2026-11-15 10:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]26` | 1 | 2026-11-15 04:50 | 2026-11-15 04:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-15 12:27 | 2026-11-15 12:27 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `196.115.59[.]152` | 1 | 2026-11-15 05:30 | 2026-11-15 05:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]49` | 1 | 2026-11-15 11:38 | 2026-11-15 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-11-15 03:03 | 2026-11-15 03:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.29.44[.]88` | 1 | 2026-11-15 13:24 | 2026-11-15 13:25 | 9s | 0 | `T1592` | 🟢 LOW |
| `206.189.180[.]166` | 1 | 2026-11-15 15:22 | 2026-11-15 15:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.105.71[.]4` | 1 | 2026-11-15 05:09 | 2026-11-15 05:09 | 21s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]244` | 1 | 2026-11-15 03:02 | 2026-11-15 03:03 | 15s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]26` | 1 | 2026-11-15 08:33 | 2026-11-15 08:33 | 28s | 0 | `T1592` | 🟢 LOW |
| `211.193.149[.]175` | 1 | 2026-11-15 09:31 | 2026-11-15 09:31 | 23s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-11-15 14:17 | 2026-11-15 14:17 | 19s | 0 | `T1592` | 🟢 LOW |
| `213.207.249[.]4` | 1 | 2026-11-15 08:55 | 2026-11-15 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.230.93[.]53` | 1 | 2026-11-15 06:29 | 2026-11-15 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.78[.]130` | 1 | 2026-11-15 07:39 | 2026-11-15 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.121.165[.]165` | 1 | 2026-11-15 04:38 | 2026-11-15 04:38 | 8s | 0 | `T1592` | 🟢 LOW |
| `220.77.86[.]237` | 1 | 2026-11-15 02:56 | 2026-11-15 02:57 | 29s | 0 | `T1592` | 🟢 LOW |
| `221.120.41[.]24` | 1 | 2026-11-15 07:33 | 2026-11-15 07:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `221.156.173[.]44` | 1 | 2026-11-15 08:47 | 2026-11-15 08:47 | 20s | 0 | `T1592` | 🟢 LOW |
| `221.156.173[.]44` | 1 | 2026-11-15 12:35 | 2026-11-15 12:36 | 22s | 0 | `T1592` | 🟢 LOW |
| `222.222.124[.]164` | 1 | 2026-11-15 05:48 | 2026-11-15 05:50 | 107s | 0 | `T1592` | 🟢 LOW |
| `223.107.146[.]186` | 1 | 2026-11-15 11:42 | 2026-11-15 11:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.166.28[.]79` | 1 | 2026-11-15 08:30 | 2026-11-15 08:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-15 07:52 | 2026-11-15 07:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.24.141[.]220` | 1 | 2026-11-15 15:35 | 2026-11-15 15:35 | 31s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]248` | 1 | 2026-11-15 08:54 | 2026-11-15 08:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.43.49[.]139` | 1 | 2026-11-15 05:06 | 2026-11-15 05:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `34.1.227[.]183` | 1 | 2026-11-15 14:48 | 2026-11-15 14:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.197[.]24` | 1 | 2026-11-15 12:22 | 2026-11-15 12:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.89[.]32` | 1 | 2026-11-15 12:09 | 2026-11-15 12:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.134[.]11` | 1 | 2026-11-15 14:34 | 2026-11-15 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.174[.]154` | 1 | 2026-11-15 15:10 | 2026-11-15 15:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.243[.]124` | 1 | 2026-11-15 13:46 | 2026-11-15 13:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.214.246[.]158` | 1 | 2026-11-15 15:56 | 2026-11-15 15:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `40.124.171[.]144` | 1 | 2026-11-15 11:32 | 2026-11-15 11:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `43.103.52[.]44` | 1 | 2026-11-15 12:50 | 2026-11-15 12:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-15 07:05 | 2026-11-15 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-15 16:08 | 2026-11-15 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.172.18[.]74` | 1 | 2026-11-15 11:03 | 2026-11-15 11:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-15 08:14 | 2026-11-15 08:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.9.46[.]131` | 1 | 2026-11-15 12:10 | 2026-11-15 12:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.201.48[.]21` | 1 | 2026-11-15 07:43 | 2026-11-15 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.113.195[.]222` | 1 | 2026-11-15 15:17 | 2026-11-15 15:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `47.36.30[.]53` | 1 | 2026-11-15 13:54 | 2026-11-15 13:54 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]8` | 1 | 2026-11-15 11:36 | 2026-11-15 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]50` | 1 | 2026-11-15 15:31 | 2026-11-15 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-15 05:16 | 2026-11-15 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.84.33[.]150` | 1 | 2026-11-15 07:47 | 2026-11-15 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-11-15 06:28 | 2026-11-15 06:28 | 16s | 0 | `T1592` | 🟢 LOW |
| `59.92.62[.]89` | 1 | 2026-11-15 08:52 | 2026-11-15 08:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `60.167.176[.]116` | 1 | 2026-11-15 09:58 | 2026-11-15 10:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-11-15 15:20 | 2026-11-15 15:20 | 27s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-11-15 04:03 | 2026-11-15 04:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-11-15 07:37 | 2026-11-15 07:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | 1 | 2026-11-15 03:44 | 2026-11-15 03:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]165` | 1 | 2026-11-15 04:59 | 2026-11-15 04:59 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]212` | 1 | 2026-11-15 13:05 | 2026-11-15 13:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.71.9[.]51` | 1 | 2026-11-15 10:17 | 2026-11-15 10:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `73.50.80[.]82` | 1 | 2026-11-15 05:14 | 2026-11-15 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-15 12:08 | 2026-11-15 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-15 15:18 | 2026-11-15 15:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-15 10:31 | 2026-11-15 10:32 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-15 11:17 | 2026-11-15 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.93.8[.]6` | 1 | 2026-11-15 09:39 | 2026-11-15 09:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-15 04:12 | 2026-11-15 04:12 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-15 08:41 | 2026-11-15 08:41 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-15 13:09 | 2026-11-15 13:09 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.177.162[.]148` | 1 | 2026-11-15 03:38 | 2026-11-15 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-15 06:36 | 2026-11-15 06:36 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-11-15 11:13 | 2026-11-15 11:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.238.183[.]206` | 1 | 2026-11-15 08:12 | 2026-11-15 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.23.122[.]73` | 1 | 2026-11-15 05:12 | 2026-11-15 05:13 | 14s | 0 | `T1592` | 🟢 LOW |
| `90.188.229[.]179` | 1 | 2026-11-15 07:01 | 2026-11-15 07:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `93.118.139[.]170` | 1 | 2026-11-15 05:05 | 2026-11-15 05:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `95.105.71[.]239` | 1 | 2026-11-15 11:45 | 2026-11-15 11:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.165.182[.]238` | 1 | 2026-11-15 05:09 | 2026-11-15 05:11 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `36.93.154[.]207` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 50 |
| `35.210.89[.]32` | BE | Google LLC | **100** ⚠️ | 5 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `90.188.229[.]179` | RU | PJSC Rostelecom | **100** ⚠️ | 3 |
| `77.90.185[.]14` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `120.29.143[.]194` | KR | CMB Kwangju Broadcasting | **100** ⚠️ | 21 |
| `121.141.6[.]41` | KR | Korea Telecom | **100** ⚠️ | 2 |
| `70.184.96[.]161` | US | Cox Communications | **100** ⚠️ | 4 |
| `111.70.49[.]182` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `49.124.151[.]8` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 420 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 418 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 116 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 6 |
| AbuseIPDB score 12 below threshold 25 | 5 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 605 cases |
| Tool 34  | Credential Extractor        | ✅ 2095 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 140 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 319 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 145 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 409 priority case(s) shown individually · 127 recon entry/entries in table (9 group(s) consolidating 21 session(s)).

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
_Report time: 2026-11-15T18:13:37Z_

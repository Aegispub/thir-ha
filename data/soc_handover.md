# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-21 |
| **Generated At** | 2026-11-21T04:44:12Z |
| **Shift Time** | 04:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **72** |
| Confirmed Threats | **52** |
| False Positives Filtered | **20** (27.8%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **19** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1309** |
| Unique Credential Pairs | **1261** |
| Unique Usernames | **410** |
| Unique Passwords | **846** |
| Successful Auth Pairs | **1282** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 488 |
| `admin` | 42 |
| `ubuntu` | 39 |
| `user` | 27 |
| `deploy` | 23 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 74 |
| `123` | 40 |
| `1234` | 28 |
| `root` | 24 |
| `12345678` | 18 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 10 |
| `root` | `root` | 8 |
| `rootssssss23424123123` | `rootssssss23424123123` | 6 |
| `root` | `root3245gs5662d34111111111` | 6 |
| `support` | `support` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-11-21T00:01:51 |
| `root` | `123qwerty` | `92.118.39.56` | 2026-11-21T00:06:54 |
| `root` | `321` | `92.118.39.56` | 2026-11-21T00:13:44 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-21T00:17:21 |
| `root` | `54321` | `92.118.39.56` | 2026-11-21T00:20:06 |
| `admin` | `2023` | `10.0.0.73` | 2026-11-21T00:22:14 |
| `support` | `support` | `10.0.0.73` | 2026-11-21T00:25:47 |
| `root` | `------fuck------` | `117.251.72.2` | 2026-11-21T00:40:54 |
| `admin` | `1qaz2wsx` | `138.226.239.234` | 2026-11-21T00:54:16 |
| `nobody` | `` | `80.94.95.118` | 2026-11-21T00:54:44 |
| `nobody` | `` | `10.0.0.73` | 2026-11-21T00:55:09 |
| `root` | `admin` | `10.0.0.73` | 2026-11-21T00:55:33 |
| `usuario` | `usuario` | `80.94.95.118` | 2026-11-21T00:56:32 |
| `mysql` | `` | `10.0.0.73` | 2026-11-21T00:57:25 |
| `git` | `git` | `10.0.0.73` | 2026-11-21T00:57:38 |
| `support` | `supportAtlanta` | `138.226.239.234` | 2026-11-21T00:58:16 |
| `git` | `git` | `80.94.95.118` | 2026-11-21T00:58:58 |
| `nobody` | `` | `138.226.239.234` | 2026-11-21T01:01:04 |
| `root` | `bash` | `109.160.32.153` | 2026-11-21T01:14:24 |
| `root` | `encore` | `109.160.32.153` | 2026-11-21T01:14:31 |
_… 1262 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **72** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 16 |
| libssh | 9 |
| Unknown | 2 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 6 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 4 | 1 |
| `0a07365cc01f...` | Generic scanner | 4 | 1 |
| `7d01d047ace6...` | Mirai/variant | 2 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 6 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `35.210.61.208`, `218.150.184.241`, `67.52.95.38`, `112.161.75.207`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **24** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 20 | HIGH |
| `AS15169` | Google LLC | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS47890` | UNMANAGED LTD | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb48f4e59fa4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-21 00:01 |
| **Last Seen** | 2026-11-21 00:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:01:50` | `cowrie.session.connect` |
| `2026-11-21 00:01:50` | `cowrie.client.version` |
| `2026-11-21 00:01:50` | `cowrie.client.kex` |
| `2026-11-21 00:01:51` | `cowrie.login.success` |
| `2026-11-21 00:01:51` | `cowrie.direct-tcpip.request` |
| `2026-11-21 00:01:51` | `cowrie.direct-tcpip.data` |
| `2026-11-21 00:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77341ee6032d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]56` |
| **First Seen** | 2026-11-21 00:06 |
| **Last Seen** | 2026-11-21 00:07 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3dbf13d1cccad61fe5de40afb840f00e_small_control'"'"' '"'"'check_3dbf13d1cccad61fe5de40afb840f00e'"'"'', printf '\n%s|%s\n' 'check_3dbf13d1cccad61fe5de40afb840f00e_small_control' 'check_3dbf13d1cccad61fe5de40afb840f00e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3dbf13d1cccad61fe5de40afb840f00e_small_math'"'"' "$((853*119+94))"', (853*119+94, printf '\n%s|%s\n' 'check_3dbf13d1cccad61fe5de40afb840f00e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:06:46` | `cowrie.session.connect` |
| `2026-11-21 00:06:48` | `cowrie.client.version` |
| `2026-11-21 00:06:48` | `cowrie.client.kex` |
| `2026-11-21 00:06:54` | `cowrie.login.success` |
| `2026-11-21 00:07:00` | `cowrie.client.size` |
| `2026-11-21 00:07:03` | `cowrie.session.params` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| `2026-11-21 00:07:06` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]56` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f169a309ee9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]56` |
| **First Seen** | 2026-11-21 00:13 |
| **Last Seen** | 2026-11-21 00:14 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d7fe7e69cf95ac22451a1450d45c53d5_small_control'"'"' '"'"'check_d7fe7e69cf95ac22451a1450d45c53d5'"'"'', printf '\n%s|%s\n' 'check_d7fe7e69cf95ac22451a1450d45c53d5_small_control' 'check_d7fe7e69cf95ac22451a1450d45c53d5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d7fe7e69cf95ac22451a1450d45c53d5_small_math'"'"' "$((460*650+5))"', (460*650+5, printf '\n%s|%s\n' 'check_d7fe7e69cf95ac22451a1450d45c53d5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:13:36` | `cowrie.session.connect` |
| `2026-11-21 00:13:38` | `cowrie.client.version` |
| `2026-11-21 00:13:38` | `cowrie.client.kex` |
| `2026-11-21 00:13:44` | `cowrie.login.success` |
| `2026-11-21 00:13:49` | `cowrie.client.size` |
| `2026-11-21 00:13:52` | `cowrie.session.params` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| `2026-11-21 00:13:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]56` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c1a2310231

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-21 00:17 |
| **Last Seen** | 2026-11-21 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:17:20` | `cowrie.session.connect` |
| `2026-11-21 00:17:21` | `cowrie.login.success` |
| `2026-11-21 00:17:21` | `cowrie.session.params` |
| `2026-11-21 00:17:21` | `cowrie.log.closed` |
| `2026-11-21 00:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563af08b8782

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]56` |
| **First Seen** | 2026-11-21 00:19 |
| **Last Seen** | 2026-11-21 00:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:19:57` | `cowrie.session.connect` |
| `2026-11-21 00:19:58` | `cowrie.client.version` |
| `2026-11-21 00:19:58` | `cowrie.client.kex` |
| `2026-11-21 00:20:06` | `cowrie.login.success` |
| `2026-11-21 00:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]56` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58510c774e1b

| Field | Detail |
|---|---|
| **Source IP** | `117.251.72[.]2` |
| **First Seen** | 2026-11-21 00:40 |
| **Last Seen** | 2026-11-21 00:41 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:40:23` | `cowrie.session.connect` |
| `2026-11-21 00:40:27` | `cowrie.client.version` |
| `2026-11-21 00:40:27` | `cowrie.client.kex` |
| `2026-11-21 00:40:54` | `cowrie.login.success` |
| `2026-11-21 00:41:06` | `cowrie.session.params` |
| `2026-11-21 00:41:06` | `cowrie.command.input` |
| `2026-11-21 00:41:16` | `cowrie.log.closed` |
| `2026-11-21 00:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.251.72[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.251.72[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a12cefc9ee8

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-21 00:54 |
| **Last Seen** | 2026-11-21 00:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:54:16` | `cowrie.session.connect` |
| `2026-11-21 00:54:16` | `cowrie.client.version` |
| `2026-11-21 00:54:16` | `cowrie.client.kex` |
| `2026-11-21 00:54:16` | `cowrie.login.success` |
| `2026-11-21 00:54:16` | `cowrie.direct-tcpip.request` |
| `2026-11-21 00:54:17` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 00:54:17` | `cowrie.direct-tcpip.data` |
| `2026-11-21 00:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f5f77f107b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-21 00:54 |
| **Last Seen** | 2026-11-21 00:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 00:54:43` | `cowrie.session.connect` |
| `2026-11-21 00:54:43` | `cowrie.client.version` |
| `2026-11-21 00:54:44` | `cowrie.client.kex` |
| `2026-11-21 00:54:44` | `cowrie.login.success` |
| `2026-11-21 00:54:44` | `cowrie.direct-tcpip.request` |
| `2026-11-21 00:54:44` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 00:54:44` | `cowrie.direct-tcpip.data` |
| `2026-11-21 00:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366272bdf20a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]153` |
| **First Seen** | 2026-11-21 01:14 |
| **Last Seen** | 2026-11-21 01:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 01:14:23` | `cowrie.session.connect` |
| `2026-11-21 01:14:23` | `cowrie.client.version` |
| `2026-11-21 01:14:23` | `cowrie.client.kex` |
| `2026-11-21 01:14:24` | `cowrie.login.success` |
| `2026-11-21 01:14:25` | `cowrie.session.params` |
| `2026-11-21 01:14:25` | `cowrie.command.input` |
| `2026-11-21 01:14:25` | `cowrie.log.closed` |
| `2026-11-21 01:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]153` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b5f062907e

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-11-21 01:19 |
| **Last Seen** | 2026-11-21 01:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 01:19:33` | `cowrie.session.connect` |
| `2026-11-21 01:19:33` | `cowrie.client.version` |
| `2026-11-21 01:19:33` | `cowrie.client.kex` |
| `2026-11-21 01:19:33` | `cowrie.login.success` |
| `2026-11-21 01:19:34` | `cowrie.session.params` |
| `2026-11-21 01:19:34` | `cowrie.command.input` |
| `2026-11-21 01:19:34` | `cowrie.command.failed` |
| `2026-11-21 01:19:34` | `cowrie.log.closed` |
| `2026-11-21 01:19:35` | `cowrie.session.params` |
| `2026-11-21 01:19:35` | `cowrie.command.input` |
| `2026-11-21 01:19:35` | `cowrie.session.file_download` |
| `2026-11-21 01:19:35` | `cowrie.log.closed` |
| `2026-11-21 01:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4023c4fd0de

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-11-21 01:19 |
| **Last Seen** | 2026-11-21 01:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 01:19:35` | `cowrie.session.connect` |
| `2026-11-21 01:19:35` | `cowrie.client.version` |
| `2026-11-21 01:19:35` | `cowrie.client.kex` |
| `2026-11-21 01:19:36` | `cowrie.login.success` |
| `2026-11-21 01:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7454c65e0fbc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-21 01:21 |
| **Last Seen** | 2026-11-21 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 01:21:45` | `cowrie.session.connect` |
| `2026-11-21 01:21:45` | `cowrie.login.success` |
| `2026-11-21 01:21:46` | `cowrie.session.params` |
| `2026-11-21 01:21:46` | `cowrie.log.closed` |
| `2026-11-21 01:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95595e05680f

| Field | Detail |
|---|---|
| **Source IP** | `169.128.70[.]53` |
| **First Seen** | 2026-11-21 01:26 |
| **Last Seen** | 2026-11-21 01:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 01:26:25` | `cowrie.session.connect` |
| `2026-11-21 01:26:26` | `cowrie.login.success` |
| `2026-11-21 01:26:26` | `cowrie.session.params` |
| `2026-11-21 01:26:27` | `cowrie.command.input` |
| `2026-11-21 01:26:27` | `cowrie.command.input` |
| `2026-11-21 01:26:28` | `cowrie.command.input` |
| `2026-11-21 01:26:29` | `cowrie.command.input` |
| `2026-11-21 01:26:29` | `cowrie.command.failed` |
| `2026-11-21 01:26:29` | `cowrie.log.closed` |
| `2026-11-21 01:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.128.70[.]53` to AbuseIPDB if not already reported
- [ ] Block `169.128.70[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff6e75f2bb5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]153` |
| **First Seen** | 2026-11-21 02:00 |
| **Last Seen** | 2026-11-21 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:00:04` | `cowrie.session.connect` |
| `2026-11-21 02:00:04` | `cowrie.client.version` |
| `2026-11-21 02:00:04` | `cowrie.client.kex` |
| `2026-11-21 02:00:04` | `cowrie.login.success` |
| `2026-11-21 02:00:05` | `cowrie.session.params` |
| `2026-11-21 02:00:05` | `cowrie.command.input` |
| `2026-11-21 02:00:05` | `cowrie.log.closed` |
| `2026-11-21 02:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]153` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f19cc3424a1

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]158` |
| **First Seen** | 2026-11-21 02:00 |
| **Last Seen** | 2026-11-21 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:00:25` | `cowrie.session.connect` |
| `2026-11-21 02:00:25` | `cowrie.client.version` |
| `2026-11-21 02:00:25` | `cowrie.client.kex` |
| `2026-11-21 02:00:25` | `cowrie.login.success` |
| `2026-11-21 02:00:26` | `cowrie.direct-tcpip.request` |
| `2026-11-21 02:00:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-11-21 02:00:26` | `cowrie.direct-tcpip.data` |
| `2026-11-21 02:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]158` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24449e7a2716

| Field | Detail |
|---|---|
| **Source IP** | `67.52.95[.]38` |
| **First Seen** | 2026-11-21 02:09 |
| **Last Seen** | 2026-11-21 02:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:09:09` | `cowrie.session.connect` |
| `2026-11-21 02:09:09` | `cowrie.client.version` |
| `2026-11-21 02:09:09` | `cowrie.client.kex` |
| `2026-11-21 02:09:10` | `cowrie.login.success` |
| `2026-11-21 02:09:11` | `cowrie.session.params` |
| `2026-11-21 02:09:11` | `cowrie.command.input` |
| `2026-11-21 02:09:11` | `cowrie.command.failed` |
| `2026-11-21 02:09:11` | `cowrie.log.closed` |
| `2026-11-21 02:09:12` | `cowrie.session.params` |
| `2026-11-21 02:09:12` | `cowrie.command.input` |
| `2026-11-21 02:09:12` | `cowrie.session.file_download` |
| `2026-11-21 02:09:12` | `cowrie.log.closed` |
| `2026-11-21 02:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.52.95[.]38` to AbuseIPDB if not already reported
- [ ] Block `67.52.95[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58d5d5a0287

| Field | Detail |
|---|---|
| **Source IP** | `67.52.95[.]38` |
| **First Seen** | 2026-11-21 02:09 |
| **Last Seen** | 2026-11-21 02:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:09:12` | `cowrie.session.connect` |
| `2026-11-21 02:09:12` | `cowrie.client.version` |
| `2026-11-21 02:09:12` | `cowrie.client.kex` |
| `2026-11-21 02:09:12` | `cowrie.login.success` |
| `2026-11-21 02:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.52.95[.]38` to AbuseIPDB if not already reported
- [ ] Block `67.52.95[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649afe28b6ba

| Field | Detail |
|---|---|
| **Source IP** | `112.161.75[.]207` |
| **First Seen** | 2026-11-21 02:10 |
| **Last Seen** | 2026-11-21 02:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:10:14` | `cowrie.session.connect` |
| `2026-11-21 02:10:14` | `cowrie.client.version` |
| `2026-11-21 02:10:14` | `cowrie.client.kex` |
| `2026-11-21 02:10:15` | `cowrie.login.success` |
| `2026-11-21 02:10:16` | `cowrie.session.params` |
| `2026-11-21 02:10:16` | `cowrie.command.input` |
| `2026-11-21 02:10:16` | `cowrie.command.failed` |
| `2026-11-21 02:10:16` | `cowrie.log.closed` |
| `2026-11-21 02:10:17` | `cowrie.session.params` |
| `2026-11-21 02:10:17` | `cowrie.command.input` |
| `2026-11-21 02:10:17` | `cowrie.session.file_download` |
| `2026-11-21 02:10:17` | `cowrie.log.closed` |
| `2026-11-21 02:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.75[.]207` to AbuseIPDB if not already reported
- [ ] Block `112.161.75[.]207` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e3d4563973

| Field | Detail |
|---|---|
| **Source IP** | `112.161.75[.]207` |
| **First Seen** | 2026-11-21 02:10 |
| **Last Seen** | 2026-11-21 02:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:10:18` | `cowrie.session.connect` |
| `2026-11-21 02:10:18` | `cowrie.client.version` |
| `2026-11-21 02:10:18` | `cowrie.client.kex` |
| `2026-11-21 02:10:19` | `cowrie.login.success` |
| `2026-11-21 02:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.75[.]207` to AbuseIPDB if not already reported
- [ ] Block `112.161.75[.]207` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b561372231

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-21 02:11 |
| **Last Seen** | 2026-11-21 02:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:11:58` | `cowrie.session.connect` |
| `2026-11-21 02:11:59` | `cowrie.login.success` |
| `2026-11-21 02:11:59` | `cowrie.session.params` |
| `2026-11-21 02:11:59` | `cowrie.log.closed` |
| `2026-11-21 02:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6020c17f9dd7

| Field | Detail |
|---|---|
| **Source IP** | `218.150.184[.]241` |
| **First Seen** | 2026-11-21 02:12 |
| **Last Seen** | 2026-11-21 02:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:12:38` | `cowrie.session.connect` |
| `2026-11-21 02:12:38` | `cowrie.client.version` |
| `2026-11-21 02:12:38` | `cowrie.client.kex` |
| `2026-11-21 02:12:39` | `cowrie.login.success` |
| `2026-11-21 02:12:40` | `cowrie.session.params` |
| `2026-11-21 02:12:40` | `cowrie.command.input` |
| `2026-11-21 02:12:40` | `cowrie.command.failed` |
| `2026-11-21 02:12:40` | `cowrie.log.closed` |
| `2026-11-21 02:12:41` | `cowrie.session.params` |
| `2026-11-21 02:12:41` | `cowrie.command.input` |
| `2026-11-21 02:12:41` | `cowrie.session.file_download` |
| `2026-11-21 02:12:41` | `cowrie.log.closed` |
| `2026-11-21 02:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.150.184[.]241` to AbuseIPDB if not already reported
- [ ] Block `218.150.184[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf4a1270283

| Field | Detail |
|---|---|
| **Source IP** | `218.150.184[.]241` |
| **First Seen** | 2026-11-21 02:12 |
| **Last Seen** | 2026-11-21 02:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:12:42` | `cowrie.session.connect` |
| `2026-11-21 02:12:42` | `cowrie.client.version` |
| `2026-11-21 02:12:42` | `cowrie.client.kex` |
| `2026-11-21 02:12:43` | `cowrie.login.success` |
| `2026-11-21 02:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.150.184[.]241` to AbuseIPDB if not already reported
- [ ] Block `218.150.184[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b18259f4eb8

| Field | Detail |
|---|---|
| **Source IP** | `35.206.163[.]19` |
| **First Seen** | 2026-11-21 02:17 |
| **Last Seen** | 2026-11-21 02:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:17:35` | `cowrie.session.connect` |
| `2026-11-21 02:17:35` | `cowrie.client.version` |
| `2026-11-21 02:17:35` | `cowrie.client.kex` |
| `2026-11-21 02:17:37` | `cowrie.login.success` |
| `2026-11-21 02:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.206.163[.]19` to AbuseIPDB if not already reported
- [ ] Block `35.206.163[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbaceb0ec21

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]6` |
| **First Seen** | 2026-11-21 02:20 |
| **Last Seen** | 2026-11-21 02:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: identity, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:20:27` | `cowrie.session.connect` |
| `2026-11-21 02:20:27` | `cowrie.login.success` |
| `2026-11-21 02:20:28` | `cowrie.session.params` |
| `2026-11-21 02:20:28` | `cowrie.command.input` |
| `2026-11-21 02:20:28` | `cowrie.command.input` |
| `2026-11-21 02:20:28` | `cowrie.command.failed` |
| `2026-11-21 02:20:28` | `cowrie.command.input` |
| `2026-11-21 02:20:28` | `cowrie.command.failed` |
| `2026-11-21 02:20:28` | `cowrie.command.input` |
| `2026-11-21 02:20:28` | `cowrie.command.failed` |
| `2026-11-21 02:20:28` | `cowrie.command.input` |
| `2026-11-21 02:20:28` | `cowrie.log.closed` |
| `2026-11-21 02:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcdb729f339

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-21 02:24 |
| **Last Seen** | 2026-11-21 02:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:24:49` | `cowrie.session.connect` |
| `2026-11-21 02:24:50` | `cowrie.login.success` |
| `2026-11-21 02:24:50` | `cowrie.session.params` |
| `2026-11-21 02:24:50` | `cowrie.log.closed` |
| `2026-11-21 02:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (2) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e40268ac1ade | HIGH | `193.32.162[.]15` | 2026-11-21 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c54a1243da6e | HIGH | `109.160.32[.]153` | 2026-11-21 02:55 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]153` | **2** | 2026-11-21 01:13 | 2026-11-21 02:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.5.22[.]163` | **2** | 2026-11-21 01:00 | 2026-11-21 02:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-21 01:21 | 2026-11-21 02:11 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `106.13.186[.]96` | 1 | 2026-11-21 00:01 | 2026-11-21 00:01 | 301s | 0 | `T1592` | 🟢 LOW |
| `117.251.72[.]2` | 1 | 2026-11-21 00:40 | 2026-11-21 00:40 | 5s | 0 | `T1592` | 🟢 LOW |
| `121.40.84[.]227` | 1 | 2026-11-21 02:52 | 2026-11-21 02:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-21 00:22 | 2026-11-21 00:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-21 01:26 | 2026-11-21 01:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-11-21 01:13 | 2026-11-21 01:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-21 00:57 | 2026-11-21 00:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]192` | 1 | 2026-11-21 02:17 | 2026-11-21 02:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-21 02:39 | 2026-11-21 02:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.163[.]19` | 1 | 2026-11-21 02:17 | 2026-11-21 02:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.12[.]136` | 1 | 2026-11-21 02:18 | 2026-11-21 02:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.234.200[.]10` | 1 | 2026-11-21 01:19 | 2026-11-21 01:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `74.138.165[.]86` | 1 | 2026-11-21 01:16 | 2026-11-21 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.110.132[.]80` | 1 | 2026-11-21 02:42 | 2026-11-21 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-21 01:32 | 2026-11-21 01:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-21 00:17 | 2026-11-21 00:17 | 2s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-21 02:24 | 2026-11-21 02:24 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]56` | 1 | 2026-11-21 00:03 | 2026-11-21 00:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-11-21 01:51 | 2026-11-21 01:53 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `112.161.75[.]207` | KR | Korea Telecom | **100** ⚠️ | 15 |
| `77.239.124[.]252` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 26 |
| `193.187.110[.]158` | FI | Cyberaegis Casa S.R.L. | **100** ⚠️ | 2 |
| `35.210.12[.]136` | BE | Google LLC | **100** ⚠️ | 11 |
| `77.239.124[.]132` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 5 |
| `76.110.132[.]80` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 3 |
| `67.52.95[.]38` | US | HILTON GRAND VACATIONS CLUB | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 72 cases |
| Tool 34  | Credential Extractor        | ✅ 1309 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (27.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 22 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-21T04:44:12Z_

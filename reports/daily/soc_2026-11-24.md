# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-24 |
| **Generated At** | 2026-11-24T21:42:58Z |
| **Shift Time** | 21:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **386** |
| Confirmed Threats | **325** |
| False Positives Filtered | **61** (15.8%) |
| Unique Attacker IPs | **169** |
| Countries of Origin | **41** |
| High Severity Cases | **205** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **181** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1753** |
| Unique Credential Pairs | **1555** |
| Unique Usernames | **429** |
| Unique Passwords | **1094** |
| Successful Auth Pairs | **1654** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 773 |
| `admin` | 60 |
| `ubuntu` | 44 |
| `support` | 26 |
| `user` | 25 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 80 |
| `123` | 43 |
| `` | 42 |
| `1234` | 34 |
| `rootssssss23424123123` | 24 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 24 |
| `support` | `support` | 23 |
| `nobody` | `` | 18 |
| `git` | `git` | 13 |
| `root` | `root3245gs5662d34111111111` | 13 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2023!` | `78.128.112.74` | 2026-11-24T07:09:51 |
| `root` | `1!` | `78.128.112.74` | 2026-11-24T07:09:51 |
| `support` | `support` | `176.53.159.196` | 2026-11-24T07:12:07 |
| `admin` | `test` | `10.0.0.73` | 2026-11-24T07:32:36 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-24T07:41:16 |
| `root` | `111111` | `195.178.110.228` | 2026-11-24T07:46:09 |
| `root` | `123` | `195.178.110.228` | 2026-11-24T07:47:51 |
| `root` | `123123` | `195.178.110.228` | 2026-11-24T07:49:37 |
| `root` | `123321` | `195.178.110.228` | 2026-11-24T07:51:35 |
| `root` | `1234` | `195.178.110.228` | 2026-11-24T07:53:30 |
| `root` | `12345` | `195.178.110.228` | 2026-11-24T07:55:26 |
| `support` | `support` | `10.0.0.73` | 2026-11-24T08:14:46 |
| `nobody` | `` | `138.226.239.233` | 2026-11-24T08:54:54 |
| `admin` | `1qaz2wsx` | `138.226.239.234` | 2026-11-24T08:54:55 |
| `git` | `git` | `138.226.239.233` | 2026-11-24T08:57:50 |
| `git` | `git` | `10.0.0.73` | 2026-11-24T09:01:15 |
| `nobody` | `` | `10.0.0.73` | 2026-11-24T09:02:38 |
| `root` | `harald` | `10.0.0.73` | 2026-11-24T09:06:05 |
| `root` | `goldfing` | `10.0.0.73` | 2026-11-24T09:06:07 |
| `root` | `gohome` | `10.0.0.73` | 2026-11-24T09:06:09 |
_… 1634 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **386** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 149 |
| libssh | 50 |
| Paramiko (Python) | 11 |
| Unknown | 6 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 114 | 5 |
| `f555226df196...` | Mirai/variant | 45 | 23 |
| `7d01d047ace6...` | Mirai/variant | 11 | 2 |
| `4c94058d5e9e...` | libssh-based | 10 | 1 |
| `16443846184e...` | Generic scanner | 7 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 114 | 5 | Mirai/variant |
| `f555226df196...` | libssh | 45 | 23 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 11 | 2 | Mirai/variant |
| `4c94058d5e9e...` | Paramiko (Python) | 10 | 1 | libssh-based |
| `16443846184e...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 4 | 4 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **121** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 27 | 24 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.88.137.213`, `58.222.244.226`, `45.126.43.245`, `200.90.8.90`, `103.165.227.178`, `197.227.8.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **169** |
| Unique ASNs | **77** |
| High-Risk ASNs | **62** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 41 | HIGH |
| `AS398324` | Censys, Inc. | 14 | HIGH |
| `AS396982` | Google LLC | 9 | LOW |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS393406` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (194)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b2434f76a28d

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-24 07:09 |
| **Last Seen** | 2026-11-24 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:09:50` | `cowrie.session.connect` |
| `2026-11-24 07:09:50` | `cowrie.client.version` |
| `2026-11-24 07:09:50` | `cowrie.client.kex` |
| `2026-11-24 07:09:51` | `cowrie.login.success` |
| `2026-11-24 07:09:52` | `cowrie.session.params` |
| `2026-11-24 07:09:52` | `cowrie.command.input` |
| `2026-11-24 07:09:52` | `cowrie.log.closed` |
| `2026-11-24 07:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d158c05d3e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-24 07:12 |
| **Last Seen** | 2026-11-24 07:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:12:07` | `cowrie.session.connect` |
| `2026-11-24 07:12:07` | `cowrie.client.version` |
| `2026-11-24 07:12:07` | `cowrie.client.kex` |
| `2026-11-24 07:12:07` | `cowrie.login.success` |
| `2026-11-24 07:12:08` | `cowrie.direct-tcpip.request` |
| `2026-11-24 07:12:08` | `cowrie.direct-tcpip.data` |
| `2026-11-24 07:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ceda011a9c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-24 07:41 |
| **Last Seen** | 2026-11-24 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:41:16` | `cowrie.session.connect` |
| `2026-11-24 07:41:16` | `cowrie.login.success` |
| `2026-11-24 07:41:17` | `cowrie.session.params` |
| `2026-11-24 07:41:17` | `cowrie.log.closed` |
| `2026-11-24 07:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830c80db3e02

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:46 |
| **Last Seen** | 2026-11-24 07:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_85dc2e0250571df18ffae1f6afaf3844_small_control'"'"' '"'"'check_85dc2e0250571df18ffae1f6afaf3844'"'"'', printf '\n%s|%s\n' 'check_85dc2e0250571df18ffae1f6afaf3844_small_control' 'check_85dc2e0250571df18ffae1f6afaf3844', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_85dc2e0250571df18ffae1f6afaf3844_small_math'"'"' "$((371*878+28))"', (371*878+28, printf '\n%s|%s\n' 'check_85dc2e0250571df18ffae1f6afaf3844_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:46:06` | `cowrie.session.connect` |
| `2026-11-24 07:46:07` | `cowrie.client.version` |
| `2026-11-24 07:46:07` | `cowrie.client.kex` |
| `2026-11-24 07:46:09` | `cowrie.login.success` |
| `2026-11-24 07:46:11` | `cowrie.client.size` |
| `2026-11-24 07:46:12` | `cowrie.session.params` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| `2026-11-24 07:46:12` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3a28d7cabc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:47 |
| **Last Seen** | 2026-11-24 07:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7c64e2003295bd947eab8bdc090bcee3_small_control'"'"' '"'"'check_7c64e2003295bd947eab8bdc090bcee3'"'"'', printf '\n%s|%s\n' 'check_7c64e2003295bd947eab8bdc090bcee3_small_control' 'check_7c64e2003295bd947eab8bdc090bcee3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7c64e2003295bd947eab8bdc090bcee3_small_math'"'"' "$((938*379+29))"', (938*379+29, printf '\n%s|%s\n' 'check_7c64e2003295bd947eab8bdc090bcee3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:47:48` | `cowrie.session.connect` |
| `2026-11-24 07:47:48` | `cowrie.client.version` |
| `2026-11-24 07:47:48` | `cowrie.client.kex` |
| `2026-11-24 07:47:51` | `cowrie.login.success` |
| `2026-11-24 07:47:53` | `cowrie.client.size` |
| `2026-11-24 07:47:53` | `cowrie.session.params` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| `2026-11-24 07:47:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bd4b6971d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:49 |
| **Last Seen** | 2026-11-24 07:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1c55988dde68e0862bd2d509e715f118_small_control'"'"' '"'"'check_1c55988dde68e0862bd2d509e715f118'"'"'', printf '\n%s|%s\n' 'check_1c55988dde68e0862bd2d509e715f118_small_control' 'check_1c55988dde68e0862bd2d509e715f118', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1c55988dde68e0862bd2d509e715f118_small_math'"'"' "$((275*405+76))"', (275*405+76, printf '\n%s|%s\n' 'check_1c55988dde68e0862bd2d509e715f118_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:49:33` | `cowrie.session.connect` |
| `2026-11-24 07:49:34` | `cowrie.client.version` |
| `2026-11-24 07:49:34` | `cowrie.client.kex` |
| `2026-11-24 07:49:37` | `cowrie.login.success` |
| `2026-11-24 07:49:39` | `cowrie.client.size` |
| `2026-11-24 07:49:40` | `cowrie.session.params` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| `2026-11-24 07:49:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c886ed75e82

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:51 |
| **Last Seen** | 2026-11-24 07:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2b5a51df6f930d5b985d2d4ae1e1ea3e_small_control'"'"' '"'"'check_2b5a51df6f930d5b985d2d4ae1e1ea3e'"'"'', printf '\n%s|%s\n' 'check_2b5a51df6f930d5b985d2d4ae1e1ea3e_small_control' 'check_2b5a51df6f930d5b985d2d4ae1e1ea3e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2b5a51df6f930d5b985d2d4ae1e1ea3e_small_math'"'"' "$((132*149+41))"', (132*149+41, printf '\n%s|%s\n' 'check_2b5a51df6f930d5b985d2d4ae1e1ea3e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:51:31` | `cowrie.session.connect` |
| `2026-11-24 07:51:32` | `cowrie.client.version` |
| `2026-11-24 07:51:32` | `cowrie.client.kex` |
| `2026-11-24 07:51:35` | `cowrie.login.success` |
| `2026-11-24 07:51:37` | `cowrie.client.size` |
| `2026-11-24 07:51:38` | `cowrie.session.params` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| `2026-11-24 07:51:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88d2db7840e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:53 |
| **Last Seen** | 2026-11-24 07:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f5b685cb989583d015a637a1bc4e6e83_small_control'"'"' '"'"'check_f5b685cb989583d015a637a1bc4e6e83'"'"'', printf '\n%s|%s\n' 'check_f5b685cb989583d015a637a1bc4e6e83_small_control' 'check_f5b685cb989583d015a637a1bc4e6e83', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f5b685cb989583d015a637a1bc4e6e83_small_math'"'"' "$((92*558+47))"', (92*558+47, printf '\n%s|%s\n' 'check_f5b685cb989583d015a637a1bc4e6e83_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:53:25` | `cowrie.session.connect` |
| `2026-11-24 07:53:26` | `cowrie.client.version` |
| `2026-11-24 07:53:26` | `cowrie.client.kex` |
| `2026-11-24 07:53:30` | `cowrie.login.success` |
| `2026-11-24 07:53:33` | `cowrie.client.size` |
| `2026-11-24 07:53:34` | `cowrie.session.params` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| `2026-11-24 07:53:35` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43840f361585

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-24 07:55 |
| **Last Seen** | 2026-11-24 07:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c22a74bb79f6f69de2be717ad5db3329_small_control'"'"' '"'"'check_c22a74bb79f6f69de2be717ad5db3329'"'"'', printf '\n%s|%s\n' 'check_c22a74bb79f6f69de2be717ad5db3329_small_control' 'check_c22a74bb79f6f69de2be717ad5db3329', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c22a74bb79f6f69de2be717ad5db3329_small_math'"'"' "$((854*154+43))"', (854*154+43, printf '\n%s|%s\n' 'check_c22a74bb79f6f69de2be717ad5db3329_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 07:55:19` | `cowrie.session.connect` |
| `2026-11-24 07:55:20` | `cowrie.client.version` |
| `2026-11-24 07:55:20` | `cowrie.client.kex` |
| `2026-11-24 07:55:26` | `cowrie.login.success` |
| `2026-11-24 07:55:29` | `cowrie.client.size` |
| `2026-11-24 07:55:31` | `cowrie.session.params` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| `2026-11-24 07:55:33` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2ee6d304c4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-24 08:17 |
| **Last Seen** | 2026-11-24 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 08:17:23` | `cowrie.session.connect` |
| `2026-11-24 08:17:23` | `cowrie.login.success` |
| `2026-11-24 08:17:24` | `cowrie.session.params` |
| `2026-11-24 08:17:24` | `cowrie.log.closed` |
| `2026-11-24 08:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41fd2a810e10

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-24 08:54 |
| **Last Seen** | 2026-11-24 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 08:54:53` | `cowrie.session.connect` |
| `2026-11-24 08:54:53` | `cowrie.client.version` |
| `2026-11-24 08:54:53` | `cowrie.client.kex` |
| `2026-11-24 08:54:54` | `cowrie.login.success` |
| `2026-11-24 08:54:54` | `cowrie.direct-tcpip.request` |
| `2026-11-24 08:54:54` | `cowrie.direct-tcpip.ja4` |
| `2026-11-24 08:54:54` | `cowrie.direct-tcpip.data` |
| `2026-11-24 08:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a589d808a3

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-24 08:54 |
| **Last Seen** | 2026-11-24 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 08:54:54` | `cowrie.session.connect` |
| `2026-11-24 08:54:54` | `cowrie.client.version` |
| `2026-11-24 08:54:54` | `cowrie.client.kex` |
| `2026-11-24 08:54:55` | `cowrie.login.success` |
| `2026-11-24 08:54:55` | `cowrie.direct-tcpip.request` |
| `2026-11-24 08:54:55` | `cowrie.direct-tcpip.ja4` |
| `2026-11-24 08:54:55` | `cowrie.direct-tcpip.data` |
| `2026-11-24 08:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7da6371914

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]121` |
| **First Seen** | 2026-11-24 09:20 |
| **Last Seen** | 2026-11-24 09:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 09:20:19` | `cowrie.session.connect` |
| `2026-11-24 09:20:24` | `cowrie.telnet.option` |
| `2026-11-24 09:20:28` | `cowrie.login.success` |
| `2026-11-24 09:20:28` | `cowrie.session.params` |
| `2026-11-24 09:20:28` | `cowrie.telnet.option` |
| `2026-11-24 09:20:28` | `cowrie.telnet.option` |
| `2026-11-24 09:20:32` | `cowrie.log.closed` |
| `2026-11-24 09:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]121` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb722c324a01

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-24 09:22 |
| **Last Seen** | 2026-11-24 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 09:22:39` | `cowrie.session.connect` |
| `2026-11-24 09:22:39` | `cowrie.client.version` |
| `2026-11-24 09:22:39` | `cowrie.client.kex` |
| `2026-11-24 09:22:40` | `cowrie.login.success` |
| `2026-11-24 09:22:40` | `cowrie.direct-tcpip.request` |
| `2026-11-24 09:22:40` | `cowrie.direct-tcpip.data` |
| `2026-11-24 09:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-513b42a231da

| Field | Detail |
|---|---|
| **Source IP** | `199.165.159[.]81` |
| **First Seen** | 2026-11-24 09:49 |
| **Last Seen** | 2026-11-24 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 09:49:05` | `cowrie.session.connect` |
| `2026-11-24 09:49:05` | `cowrie.login.success` |
| `2026-11-24 09:49:06` | `cowrie.session.params` |
| `2026-11-24 09:49:06` | `cowrie.command.input` |
| `2026-11-24 09:49:06` | `cowrie.command.input` |
| `2026-11-24 09:49:06` | `cowrie.command.failed` |
| `2026-11-24 09:49:06` | `cowrie.command.input` |
| `2026-11-24 09:49:06` | `cowrie.command.failed` |
| `2026-11-24 09:49:06` | `cowrie.command.input` |
| `2026-11-24 09:49:06` | `cowrie.log.closed` |
| `2026-11-24 09:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.165.159[.]81` to AbuseIPDB if not already reported
- [ ] Block `199.165.159[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21b16eb1318

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:02 |
| **Last Seen** | 2026-11-24 10:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9c966e6ad941f52efa32f33bd26fa803_small_control'"'"' '"'"'check_9c966e6ad941f52efa32f33bd26fa803'"'"'', printf '\n%s|%s\n' 'check_9c966e6ad941f52efa32f33bd26fa803_small_control' 'check_9c966e6ad941f52efa32f33bd26fa803', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9c966e6ad941f52efa32f33bd26fa803_small_math'"'"' "$((207*519+26))"', (207*519+26, printf '\n%s|%s\n' 'check_9c966e6ad941f52efa32f33bd26fa803_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:02:44` | `cowrie.session.connect` |
| `2026-11-24 10:02:45` | `cowrie.client.version` |
| `2026-11-24 10:02:45` | `cowrie.client.kex` |
| `2026-11-24 10:02:48` | `cowrie.login.success` |
| `2026-11-24 10:02:51` | `cowrie.client.size` |
| `2026-11-24 10:02:52` | `cowrie.session.params` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| `2026-11-24 10:02:53` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ad2cda35fb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:05 |
| **Last Seen** | 2026-11-24 10:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ee7205526856645862ecea7edd0f115e_small_control'"'"' '"'"'check_ee7205526856645862ecea7edd0f115e'"'"'', printf '\n%s|%s\n' 'check_ee7205526856645862ecea7edd0f115e_small_control' 'check_ee7205526856645862ecea7edd0f115e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ee7205526856645862ecea7edd0f115e_small_math'"'"' "$((226*372+30))"', (226*372+30, printf '\n%s|%s\n' 'check_ee7205526856645862ecea7edd0f115e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:05:14` | `cowrie.session.connect` |
| `2026-11-24 10:05:15` | `cowrie.client.version` |
| `2026-11-24 10:05:15` | `cowrie.client.kex` |
| `2026-11-24 10:05:19` | `cowrie.login.success` |
| `2026-11-24 10:05:21` | `cowrie.client.size` |
| `2026-11-24 10:05:22` | `cowrie.session.params` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| `2026-11-24 10:05:25` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6763e13a74c1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:07 |
| **Last Seen** | 2026-11-24 10:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42c97fbafc07b1e9f14d474290264195_small_control'"'"' '"'"'check_42c97fbafc07b1e9f14d474290264195'"'"'', printf '\n%s|%s\n' 'check_42c97fbafc07b1e9f14d474290264195_small_control' 'check_42c97fbafc07b1e9f14d474290264195', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42c97fbafc07b1e9f14d474290264195_small_math'"'"' "$((149*987+26))"', (149*987+26, printf '\n%s|%s\n' 'check_42c97fbafc07b1e9f14d474290264195_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:07:41` | `cowrie.session.connect` |
| `2026-11-24 10:07:42` | `cowrie.client.version` |
| `2026-11-24 10:07:42` | `cowrie.client.kex` |
| `2026-11-24 10:07:46` | `cowrie.login.success` |
| `2026-11-24 10:07:49` | `cowrie.client.size` |
| `2026-11-24 10:07:50` | `cowrie.session.params` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| `2026-11-24 10:07:50` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275c0a048a74

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-24 10:08 |
| **Last Seen** | 2026-11-24 10:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:08:03` | `cowrie.session.connect` |
| `2026-11-24 10:08:03` | `cowrie.client.version` |
| `2026-11-24 10:08:03` | `cowrie.client.kex` |
| `2026-11-24 10:08:04` | `cowrie.login.success` |
| `2026-11-24 10:08:04` | `cowrie.direct-tcpip.request` |
| `2026-11-24 10:08:04` | `cowrie.direct-tcpip.data` |
| `2026-11-24 10:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e7dc94f195

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:10 |
| **Last Seen** | 2026-11-24 10:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d306f5b0334d2278f24c1d8226371126_small_control'"'"' '"'"'check_d306f5b0334d2278f24c1d8226371126'"'"'', printf '\n%s|%s\n' 'check_d306f5b0334d2278f24c1d8226371126_small_control' 'check_d306f5b0334d2278f24c1d8226371126', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d306f5b0334d2278f24c1d8226371126_small_math'"'"' "$((185*464+91))"', (185*464+91, printf '\n%s|%s\n' 'check_d306f5b0334d2278f24c1d8226371126_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:10:09` | `cowrie.session.connect` |
| `2026-11-24 10:10:10` | `cowrie.client.version` |
| `2026-11-24 10:10:10` | `cowrie.client.kex` |
| `2026-11-24 10:10:14` | `cowrie.login.success` |
| `2026-11-24 10:10:17` | `cowrie.client.size` |
| `2026-11-24 10:10:18` | `cowrie.session.params` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| `2026-11-24 10:10:19` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b0d0499780

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:12 |
| **Last Seen** | 2026-11-24 10:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f34284064fac75135b334530c20e3875_small_control'"'"' '"'"'check_f34284064fac75135b334530c20e3875'"'"'', printf '\n%s|%s\n' 'check_f34284064fac75135b334530c20e3875_small_control' 'check_f34284064fac75135b334530c20e3875', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f34284064fac75135b334530c20e3875_small_math'"'"' "$((461*105+1))"', (461*105+1, printf '\n%s|%s\n' 'check_f34284064fac75135b334530c20e3875_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:12:55` | `cowrie.session.connect` |
| `2026-11-24 10:12:56` | `cowrie.client.version` |
| `2026-11-24 10:12:56` | `cowrie.client.kex` |
| `2026-11-24 10:12:59` | `cowrie.login.success` |
| `2026-11-24 10:13:01` | `cowrie.client.size` |
| `2026-11-24 10:13:04` | `cowrie.session.params` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| `2026-11-24 10:13:05` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47079ece2863

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:15 |
| **Last Seen** | 2026-11-24 10:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b881d2196ef37666f498cacf2e7180fa_small_control'"'"' '"'"'check_b881d2196ef37666f498cacf2e7180fa'"'"'', printf '\n%s|%s\n' 'check_b881d2196ef37666f498cacf2e7180fa_small_control' 'check_b881d2196ef37666f498cacf2e7180fa', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b881d2196ef37666f498cacf2e7180fa_small_math'"'"' "$((375*272+92))"', (375*272+92, printf '\n%s|%s\n' 'check_b881d2196ef37666f498cacf2e7180fa_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:15:10` | `cowrie.session.connect` |
| `2026-11-24 10:15:10` | `cowrie.client.version` |
| `2026-11-24 10:15:10` | `cowrie.client.kex` |
| `2026-11-24 10:15:15` | `cowrie.login.success` |
| `2026-11-24 10:15:17` | `cowrie.client.size` |
| `2026-11-24 10:15:18` | `cowrie.session.params` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| `2026-11-24 10:15:19` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d8d2d42e13

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:19 |
| **Last Seen** | 2026-11-24 10:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_daff9d2f836948f26fa75504fddce9af_small_control'"'"' '"'"'check_daff9d2f836948f26fa75504fddce9af'"'"'', printf '\n%s|%s\n' 'check_daff9d2f836948f26fa75504fddce9af_small_control' 'check_daff9d2f836948f26fa75504fddce9af', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_daff9d2f836948f26fa75504fddce9af_small_math'"'"' "$((232*600+95))"', (232*600+95, printf '\n%s|%s\n' 'check_daff9d2f836948f26fa75504fddce9af_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:19:39` | `cowrie.session.connect` |
| `2026-11-24 10:19:39` | `cowrie.client.version` |
| `2026-11-24 10:19:39` | `cowrie.client.kex` |
| `2026-11-24 10:19:43` | `cowrie.login.success` |
| `2026-11-24 10:19:46` | `cowrie.client.size` |
| `2026-11-24 10:19:47` | `cowrie.session.params` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| `2026-11-24 10:19:48` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae2e476dfda

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]43` |
| **First Seen** | 2026-11-24 10:21 |
| **Last Seen** | 2026-11-24 10:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:21:22` | `cowrie.session.connect` |
| `2026-11-24 10:21:22` | `cowrie.client.version` |
| `2026-11-24 10:21:22` | `cowrie.client.kex` |
| `2026-11-24 10:21:23` | `cowrie.login.success` |
| `2026-11-24 10:21:24` | `cowrie.session.params` |
| `2026-11-24 10:21:24` | `cowrie.command.input` |
| `2026-11-24 10:21:24` | `cowrie.log.closed` |
| `2026-11-24 10:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]43` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7afde99a721

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-24 10:21 |
| **Last Seen** | 2026-11-24 10:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42ac5bb533ce630665b309a5026e0f04_small_control'"'"' '"'"'check_42ac5bb533ce630665b309a5026e0f04'"'"'', printf '\n%s|%s\n' 'check_42ac5bb533ce630665b309a5026e0f04_small_control' 'check_42ac5bb533ce630665b309a5026e0f04', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_42ac5bb533ce630665b309a5026e0f04_small_math'"'"' "$((120*685+94))"', (120*685+94, printf '\n%s|%s\n' 'check_42ac5bb533ce630665b309a5026e0f04_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-24 10:21:50` | `cowrie.session.connect` |
| `2026-11-24 10:21:51` | `cowrie.client.version` |
| `2026-11-24 10:21:51` | `cowrie.client.kex` |
| `2026-11-24 10:21:55` | `cowrie.login.success` |
| `2026-11-24 10:21:58` | `cowrie.client.size` |
| `2026-11-24 10:21:59` | `cowrie.session.params` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| `2026-11-24 10:22:00` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (169) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-a9ebe5cce88c | HIGH | `193.32.162[.]84` | 2026-11-24 10:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-699e2f7aacc0 | HIGH | `193.32.162[.]84` | 2026-11-24 10:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0a98afdf624d | HIGH | `193.32.162[.]84` | 2026-11-24 10:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-add3771544a9 | HIGH | `193.32.162[.]84` | 2026-11-24 10:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-891a684cb20e | HIGH | `193.32.162[.]84` | 2026-11-24 10:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8d02d97145f3 | HIGH | `193.32.162[.]84` | 2026-11-24 10:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1863b9784748 | HIGH | `193.32.162[.]84` | 2026-11-24 10:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08949a70b349 | HIGH | `193.32.162[.]84` | 2026-11-24 10:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7d42ed324bbf | HIGH | `193.32.162[.]84` | 2026-11-24 10:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-135a1cfbf490 | HIGH | `193.32.162[.]84` | 2026-11-24 10:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-49013ba92e08 | HIGH | `193.32.162[.]84` | 2026-11-24 10:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d1cdc3b966a | HIGH | `193.32.162[.]84` | 2026-11-24 10:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d539777d8759 | HIGH | `193.32.162[.]84` | 2026-11-24 10:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8ad53db82b86 | HIGH | `193.32.162[.]84` | 2026-11-24 10:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-46005828ee01 | HIGH | `193.32.162[.]84` | 2026-11-24 10:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ea0b0cf8c324 | HIGH | `193.32.162[.]84` | 2026-11-24 10:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-448c1eb4ed6e | HIGH | `193.32.162[.]84` | 2026-11-24 10:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d8d3175787c9 | HIGH | `193.32.162[.]84` | 2026-11-24 11:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-67db00e82261 | HIGH | `193.32.162[.]84` | 2026-11-24 11:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-aac0dd333c9f | HIGH | `193.32.162[.]84` | 2026-11-24 11:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f8e96ec67f59 | HIGH | `138.226.239[.]233` | 2026-11-24 11:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96ee0bc5507a | HIGH | `193.32.162[.]84` | 2026-11-24 11:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f00b1eb367f0 | HIGH | `138.226.239[.]234` | 2026-11-24 11:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ff46cef85f8 | HIGH | `193.32.162[.]84` | 2026-11-24 11:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-127440d94ebc | HIGH | `193.32.162[.]84` | 2026-11-24 11:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-49a48b207460 | HIGH | `193.32.162[.]84` | 2026-11-24 11:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-07abe4b7ddcc | HIGH | `193.32.162[.]84` | 2026-11-24 11:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ba353317020b | HIGH | `193.32.162[.]84` | 2026-11-24 11:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ca0b25afa41c | HIGH | `45.135.194[.]105` | 2026-11-24 11:19 | Y | 0 | 0 | `T1078` |
| IR-4ee04e7bf205 | HIGH | `193.32.162[.]84` | 2026-11-24 11:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5b94ec274218 | HIGH | `193.32.162[.]84` | 2026-11-24 11:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a7aaa58acb9b | HIGH | `193.32.162[.]84` | 2026-11-24 11:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dd26dbeefc51 | HIGH | `193.32.162[.]84` | 2026-11-24 11:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-41e56f58972b | HIGH | `193.32.162[.]84` | 2026-11-24 11:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6c1bfebddfaf | HIGH | `78.128.112[.]74` | 2026-11-24 11:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ddf6e4dd4381 | HIGH | `193.32.162[.]84` | 2026-11-24 11:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fb3c68eb84e1 | HIGH | `193.32.162[.]84` | 2026-11-24 11:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de4eeb23f2ea | HIGH | `193.32.162[.]84` | 2026-11-24 11:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a9ad439e2976 | HIGH | `193.32.162[.]84` | 2026-11-24 11:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-811121bf6c83 | HIGH | `193.32.162[.]84` | 2026-11-24 11:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d444b0739625 | HIGH | `193.32.162[.]84` | 2026-11-24 11:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-396579a39aac | HIGH | `193.32.162[.]84` | 2026-11-24 11:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-be00d3e79bfc | HIGH | `193.32.162[.]84` | 2026-11-24 11:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c347f6da8b04 | HIGH | `193.32.162[.]84` | 2026-11-24 11:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6ad57dc0d4ca | HIGH | `193.32.162[.]84` | 2026-11-24 11:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9a1ee4ac5564 | HIGH | `193.32.162[.]84` | 2026-11-24 11:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dcdc5a3fb59b | HIGH | `193.32.162[.]84` | 2026-11-24 11:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7a60b197027a | HIGH | `193.187.110[.]158` | 2026-11-24 11:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6346e6e9ebb6 | HIGH | `193.32.162[.]84` | 2026-11-24 11:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3e47b78d39c6 | HIGH | `193.32.162[.]84` | 2026-11-24 12:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5f083bccaa6c | HIGH | `193.32.162[.]84` | 2026-11-24 12:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f4b69ca1f72 | HIGH | `193.32.162[.]84` | 2026-11-24 12:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d4c13eb42073 | HIGH | `193.32.162[.]84` | 2026-11-24 12:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ae31d55d24d6 | HIGH | `193.32.162[.]84` | 2026-11-24 12:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4aac5be27d93 | HIGH | `193.32.162[.]84` | 2026-11-24 12:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-20dae328c0f4 | HIGH | `193.32.162[.]84` | 2026-11-24 12:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e69d168db61b | HIGH | `193.32.162[.]84` | 2026-11-24 12:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f139ddb927c1 | HIGH | `193.32.162[.]84` | 2026-11-24 12:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-920f5d9a17e4 | HIGH | `193.32.162[.]84` | 2026-11-24 12:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4ee1fbc04544 | HIGH | `193.32.162[.]84` | 2026-11-24 12:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-05541e60d17a | HIGH | `193.32.162[.]84` | 2026-11-24 12:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e36687630013 | HIGH | `193.32.162[.]84` | 2026-11-24 12:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2b53c2b289dd | HIGH | `193.32.162[.]84` | 2026-11-24 12:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7346173880e6 | HIGH | `193.32.162[.]84` | 2026-11-24 12:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8b9aa0a80cc9 | HIGH | `193.32.162[.]84` | 2026-11-24 12:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d61dba917618 | HIGH | `193.32.162[.]84` | 2026-11-24 12:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8f5788069cb2 | HIGH | `193.32.162[.]84` | 2026-11-24 12:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ac602d4b1980 | HIGH | `193.32.162[.]84` | 2026-11-24 12:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ce3fe27ea785 | HIGH | `193.32.162[.]84` | 2026-11-24 12:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8b17c7261dcb | HIGH | `193.32.162[.]84` | 2026-11-24 12:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7ec38cda43d3 | HIGH | `193.32.162[.]84` | 2026-11-24 12:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6f77c225316c | HIGH | `193.32.162[.]84` | 2026-11-24 12:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b88af81112b9 | HIGH | `193.32.162[.]84` | 2026-11-24 12:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5c9e3371a8c5 | HIGH | `193.32.162[.]84` | 2026-11-24 12:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ef9130f61a64 | HIGH | `203.156.216[.]10` | 2026-11-24 12:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ee5432b1e5e5 | HIGH | `193.32.162[.]84` | 2026-11-24 12:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6fb40b45d30e | HIGH | `193.32.162[.]84` | 2026-11-24 12:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d06f8f6b8861 | HIGH | `193.32.162[.]84` | 2026-11-24 12:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8604d8b36cd5 | HIGH | `176.53.159[.]196` | 2026-11-24 12:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bad87ccdb815 | HIGH | `138.226.239[.]233` | 2026-11-24 13:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8057ac04952a | HIGH | `138.226.239[.]234` | 2026-11-24 13:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-14d84d2db17e | HIGH | `185.242.226[.]60` | 2026-11-24 13:50 | Y | 3 | 0 | `T1078` |
| IR-b498d682f2f9 | HIGH | `92.118.39[.]56` | 2026-11-24 14:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-788ce87af34e | HIGH | `179.183.49[.]86` | 2026-11-24 14:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34e221e4e565 | HIGH | `179.183.49[.]86` | 2026-11-24 14:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-072c4e4a9b1b | HIGH | `176.53.159[.]196` | 2026-11-24 14:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23ac63751215 | HIGH | `79.3.96[.]178` | 2026-11-24 14:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-df0309101312 | HIGH | `79.3.96[.]178` | 2026-11-24 14:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d9d2c2273fd | HIGH | `45.126.43[.]245` | 2026-11-24 15:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-85af977c37ca | HIGH | `45.126.43[.]245` | 2026-11-24 15:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4812d2411687 | HIGH | `58.222.244[.]226` | 2026-11-24 15:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e108adf6d3f0 | HIGH | `58.222.244[.]226` | 2026-11-24 15:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-263a23b0244a | HIGH | `187.107.27[.]62` | 2026-11-24 15:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1e5efc707523 | HIGH | `187.107.27[.]62` | 2026-11-24 15:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3f33faaa1301 | HIGH | `138.226.239[.]234` | 2026-11-24 15:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40b4eb3c734b | HIGH | `195.178.110[.]227` | 2026-11-24 15:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-846f5abb348a | HIGH | `195.178.110[.]227` | 2026-11-24 15:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5b262c26934a | HIGH | `195.178.110[.]227` | 2026-11-24 15:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1c1b7b17c412 | HIGH | `45.79.207[.]110` | 2026-11-24 15:38 | Y | 0 | 0 | `T1078` |
| IR-71236cb2c573 | HIGH | `195.178.110[.]227` | 2026-11-24 15:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 69 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `193.32.162[.]84` | **3** | 2026-11-24 09:59 | 2026-11-24 12:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.220.0[.]26` | **3** | 2026-11-24 17:55 | 2026-11-24 20:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `49.216.126[.]0` | **3** | 2026-11-24 11:51 | 2026-11-24 15:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `70.61.94[.]82` | **3** | 2026-11-24 15:11 | 2026-11-24 18:12 | 1m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **3** | 2026-11-24 15:21 | 2026-11-24 18:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-24 07:25 | 2026-11-24 08:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-24 11:06 | 2026-11-24 12:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-24 15:26 | 2026-11-24 16:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `183.109.238[.]204` | **2** | 2026-11-24 13:50 | 2026-11-24 14:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-11-24 15:43 | 2026-11-24 16:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-11-24 07:57 | 2026-11-24 08:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `59.3.218[.]15` | **2** | 2026-11-24 12:49 | 2026-11-24 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-24 09:26 | 2026-11-24 10:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-24 07:41 | 2026-11-24 08:17 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `101.126.4[.]215` | 1 | 2026-11-24 20:24 | 2026-11-24 20:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.185.146[.]140` | 1 | 2026-11-24 19:14 | 2026-11-24 19:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.143.23[.]186` | 1 | 2026-11-24 13:42 | 2026-11-24 13:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]43` | 1 | 2026-11-24 10:20 | 2026-11-24 10:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-24 08:09 | 2026-11-24 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-24 11:33 | 2026-11-24 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-24 20:20 | 2026-11-24 20:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.47.255[.]44` | 1 | 2026-11-24 15:47 | 2026-11-24 15:47 | 24s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-24 19:40 | 2026-11-24 19:41 | 50s | 0 | `T1592` | 🟢 LOW |
| `14.118.169[.]129` | 1 | 2026-11-24 20:49 | 2026-11-24 20:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.161.246[.]179` | 1 | 2026-11-24 14:51 | 2026-11-24 14:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]14` | 1 | 2026-11-24 16:54 | 2026-11-24 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]153` | 1 | 2026-11-24 16:57 | 2026-11-24 16:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]84` | 1 | 2026-11-24 17:16 | 2026-11-24 17:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.81.90[.]36` | 1 | 2026-11-24 12:35 | 2026-11-24 12:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-24 07:36 | 2026-11-24 07:36 | 5s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-11-24 14:59 | 2026-11-24 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-24 07:40 | 2026-11-24 07:41 | 36s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-24 16:00 | 2026-11-24 16:01 | 33s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-24 19:52 | 2026-11-24 19:52 | 35s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-11-24 13:52 | 2026-11-24 13:53 | 27s | 0 | `T1592` | 🟢 LOW |
| `170.64.147[.]115` | 1 | 2026-11-24 15:40 | 2026-11-24 15:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.112.105[.]77` | 1 | 2026-11-24 12:45 | 2026-11-24 12:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `177.55.91[.]194` | 1 | 2026-11-24 18:22 | 2026-11-24 18:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-24 08:44 | 2026-11-24 08:44 | 9s | 0 | `T1592` | 🟢 LOW |
| `181.115.192[.]10` | 1 | 2026-11-24 12:39 | 2026-11-24 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.119.67[.]204` | 1 | 2026-11-24 08:48 | 2026-11-24 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.119.67[.]205` | 1 | 2026-11-24 08:48 | 2026-11-24 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.119.67[.]206` | 1 | 2026-11-24 08:48 | 2026-11-24 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.175.139[.]6` | 1 | 2026-11-24 15:36 | 2026-11-24 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.84.144[.]28` | 1 | 2026-11-24 15:19 | 2026-11-24 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]60` | 1 | 2026-11-24 13:50 | 2026-11-24 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.79.6[.]215` | 1 | 2026-11-24 20:49 | 2026-11-24 20:49 | 12s | 0 | `T1592` | 🟢 LOW |
| `186.244.247[.]8` | 1 | 2026-11-24 16:09 | 2026-11-24 16:09 | 4s | 0 | `T1592` | 🟢 LOW |
| `187.220.224[.]137` | 1 | 2026-11-24 06:55 | 2026-11-24 06:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.151.78[.]34` | 1 | 2026-11-24 18:23 | 2026-11-24 18:24 | 17s | 0 | `T1592` | 🟢 LOW |
| `193.30.245[.]66` | 1 | 2026-11-24 11:35 | 2026-11-24 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.39.227[.]65` | 1 | 2026-11-24 19:04 | 2026-11-24 19:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]121` | 1 | 2026-11-24 11:39 | 2026-11-24 11:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-24 19:39 | 2026-11-24 19:39 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.42.57[.]189` | 1 | 2026-11-24 19:13 | 2026-11-24 19:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.98.162[.]226` | 1 | 2026-11-24 20:22 | 2026-11-24 20:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.156.216[.]10` | 1 | 2026-11-24 12:44 | 2026-11-24 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-11-24 16:18 | 2026-11-24 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.82.215[.]158` | 1 | 2026-11-24 08:33 | 2026-11-24 08:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `222.109.132[.]225` | 1 | 2026-11-24 14:00 | 2026-11-24 14:00 | 18s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-11-24 14:31 | 2026-11-24 14:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-24 16:31 | 2026-11-24 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.94.194[.]173` | 1 | 2026-11-24 16:51 | 2026-11-24 16:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `31.129.11[.]242` | 1 | 2026-11-24 14:23 | 2026-11-24 14:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | 1 | 2026-11-24 12:03 | 2026-11-24 12:04 | 55s | 0 | `T1592` | 🟢 LOW |
| `44.220.188[.]136` | 1 | 2026-11-24 16:01 | 2026-11-24 16:01 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-24 08:40 | 2026-11-24 08:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-24 15:37 | 2026-11-24 15:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.115.92[.]162` | 1 | 2026-11-24 19:43 | 2026-11-24 19:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `48.217.235[.]69` | 1 | 2026-11-24 14:58 | 2026-11-24 14:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `59.25.46[.]18` | 1 | 2026-11-24 08:49 | 2026-11-24 08:49 | 27s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-11-24 16:24 | 2026-11-24 16:25 | 32s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-24 10:19 | 2026-11-24 10:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-24 19:23 | 2026-11-24 19:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-24 13:15 | 2026-11-24 13:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]194` | 1 | 2026-11-24 19:49 | 2026-11-24 19:50 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]73` | 1 | 2026-11-24 10:48 | 2026-11-24 10:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]176` | 1 | 2026-11-24 10:31 | 2026-11-24 10:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]213` | 1 | 2026-11-24 15:46 | 2026-11-24 15:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]215` | 1 | 2026-11-24 10:32 | 2026-11-24 10:33 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]221` | 1 | 2026-11-24 10:49 | 2026-11-24 10:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]160` | 1 | 2026-11-24 19:51 | 2026-11-24 19:51 | 7s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]178` | 1 | 2026-11-24 10:52 | 2026-11-24 10:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]181` | 1 | 2026-11-24 10:49 | 2026-11-24 10:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | 1 | 2026-11-24 10:52 | 2026-11-24 10:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | 1 | 2026-11-24 14:47 | 2026-11-24 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | 1 | 2026-11-24 10:52 | 2026-11-24 10:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]196` | 1 | 2026-11-24 10:51 | 2026-11-24 10:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]32` | 1 | 2026-11-24 10:52 | 2026-11-24 10:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | 1 | 2026-11-24 06:56 | 2026-11-24 06:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | 1 | 2026-11-24 18:42 | 2026-11-24 18:42 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]223` | 1 | 2026-11-24 10:51 | 2026-11-24 10:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]230` | 1 | 2026-11-24 10:32 | 2026-11-24 10:32 | 19s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | 1 | 2026-11-24 15:24 | 2026-11-24 15:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `75.191.72[.]108` | 1 | 2026-11-24 16:29 | 2026-11-24 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.186.87[.]66` | 1 | 2026-11-24 20:22 | 2026-11-24 20:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]121` | 1 | 2026-11-24 09:20 | 2026-11-24 09:20 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-24 14:39 | 2026-11-24 14:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-24 20:38 | 2026-11-24 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-24 07:09 | 2026-11-24 07:09 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-24 11:30 | 2026-11-24 11:30 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-24 15:49 | 2026-11-24 15:49 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-24 20:10 | 2026-11-24 20:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.134.239[.]76` | 1 | 2026-11-24 09:37 | 2026-11-24 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]139` | 1 | 2026-11-24 14:46 | 2026-11-24 14:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.186.230[.]14` | 1 | 2026-11-24 18:50 | 2026-11-24 18:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]196` | 1 | 2026-11-24 10:14 | 2026-11-24 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]203` | 1 | 2026-11-24 20:24 | 2026-11-24 20:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.164.137[.]109` | 1 | 2026-11-24 12:21 | 2026-11-24 12:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]56` | 1 | 2026-11-24 14:13 | 2026-11-24 14:13 | 9s | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]125` | 1 | 2026-11-24 11:43 | 2026-11-24 11:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `95.85.244[.]17` | 1 | 2026-11-24 08:53 | 2026-11-24 08:53 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `194.39.227[.]65` | UA | New Information Systems PP | **100** ⚠️ | 10 |
| `193.30.245[.]66` | UA | PP Kabel-Plus | **100** ⚠️ | 5 |
| `223.83.183[.]254` | CN | China Mobile Communications Corporation | **100** ⚠️ | 24 |
| `185.79.6[.]215` | ES | INSTALACIONES Y SERVICIOS MOWITEL S.L. | **100** ⚠️ | 4 |
| `87.236.176[.]203` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `103.185.146[.]140` | TH | Y.U.T Corporate Company Limited | **100** ⚠️ | 4 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `181.115.192[.]10` | BO | Entel S.A. - EntelNet | **100** ⚠️ | 37 |
| `220.82.215[.]158` | KR | Jeonbukbonbujang | **100** ⚠️ | 24 |
| `164.152.250[.]192` | BR | Oracle Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 219 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 205 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 106 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 26 |

---

## 🔕 False Positive Summary (61 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 10 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 386 cases |
| Tool 34  | Credential Extractor        | ✅ 1753 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 121 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 169 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 61 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 77 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 194 priority case(s) shown individually · 112 recon entry/entries in table (14 group(s) consolidating 33 session(s)).

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
_Report time: 2026-11-24T21:42:58Z_

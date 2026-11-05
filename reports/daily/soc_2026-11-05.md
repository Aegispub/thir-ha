# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-05 |
| **Generated At** | 2026-11-05T04:05:48Z |
| **Shift Time** | 04:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **95** |
| Confirmed Threats | **71** |
| False Positives Filtered | **24** (25.3%) |
| Unique Attacker IPs | **61** |
| Countries of Origin | **22** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1206** |
| Unique Credential Pairs | **1157** |
| Unique Usernames | **407** |
| Unique Passwords | **770** |
| Successful Auth Pairs | **1180** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 400 |
| `ubuntu` | 37 |
| `admin` | 30 |
| `user` | 25 |
| `deploy` | 21 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 67 |
| `123` | 40 |
| `1234` | 23 |
| `12345678` | 18 |
| `password` | 16 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 10 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `support` | `support` | 6 |
| `root` | `` | 4 |
| `dev` | `dev` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz@WSX3edc` | `77.239.124.153` | 2026-11-05T00:00:01 |
| `root` | `dkflbckfd` | `77.239.124.153` | 2026-11-05T00:00:07 |
| `openvpn` | `12345678` | `77.239.124.153` | 2026-11-05T00:00:14 |
| `root` | `redhat123` | `77.239.124.153` | 2026-11-05T00:00:21 |
| `gns3` | `gns3` | `77.239.124.153` | 2026-11-05T00:00:29 |
| `claude` | `123` | `77.239.124.153` | 2026-11-05T00:00:36 |
| `root` | `Zza123456` | `77.239.124.153` | 2026-11-05T00:00:43 |
| `root` | `pass1234` | `77.239.124.153` | 2026-11-05T00:00:50 |
| `codex` | `12345` | `77.239.124.153` | 2026-11-05T00:00:56 |
| `steam` | `steam123` | `77.239.124.153` | 2026-11-05T00:01:03 |
| `sftp` | `Abcd1234` | `77.239.124.153` | 2026-11-05T00:01:09 |
| `trader` | `12345678` | `77.239.124.153` | 2026-11-05T00:01:15 |
| `root` | `Yun@wocloud.szkj` | `77.239.124.153` | 2026-11-05T00:01:22 |
| `fanshu` | `fanshu` | `77.239.124.153` | 2026-11-05T00:01:29 |
| `root` | `Ff123123.` | `77.239.124.153` | 2026-11-05T00:01:36 |
| `root` | `abcd@1234!` | `77.239.124.153` | 2026-11-05T00:01:42 |
| `root` | `abcd12345` | `77.239.124.153` | 2026-11-05T00:01:48 |
| `www` | `!QAZ2wsx` | `77.239.124.153` | 2026-11-05T00:01:54 |
| `admin` | `E4IuG88G` | `77.239.124.153` | 2026-11-05T00:02:00 |
| `admin` | `!QAZ2wsx` | `77.239.124.153` | 2026-11-05T00:02:07 |
_… 1160 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **95** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 25 |
| Perl Net::SSH | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 20 | 11 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 20 | 11 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **15** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 11 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.172.186.3`, `23.95.110.131`, `195.86.192.66`, `124.43.4.17`, `160.16.105.184`, `79.3.96.178`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **61** |
| Unique ASNs | **33** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 24 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS984` | OCTOPUS WEB SOLUTION INC | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-11f0c70b9268

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]153` |
| **First Seen** | 2026-11-05 00:00 |
| **Last Seen** | 2026-11-05 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:00:00` | `cowrie.session.connect` |
| `2026-11-05 00:00:00` | `cowrie.client.version` |
| `2026-11-05 00:00:00` | `cowrie.client.kex` |
| `2026-11-05 00:00:01` | `cowrie.login.success` |
| `2026-11-05 00:00:01` | `cowrie.session.params` |
| `2026-11-05 00:00:01` | `cowrie.command.input` |
| `2026-11-05 00:00:02` | `cowrie.log.closed` |
| `2026-11-05 00:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]153` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1e2e3dec27

| Field | Detail |
|---|---|
| **Source IP** | `172.172.186[.]3` |
| **First Seen** | 2026-11-05 00:03 |
| **Last Seen** | 2026-11-05 00:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:03:15` | `cowrie.session.connect` |
| `2026-11-05 00:03:15` | `cowrie.client.version` |
| `2026-11-05 00:03:15` | `cowrie.client.kex` |
| `2026-11-05 00:03:16` | `cowrie.login.success` |
| `2026-11-05 00:03:16` | `cowrie.session.params` |
| `2026-11-05 00:03:16` | `cowrie.command.input` |
| `2026-11-05 00:03:16` | `cowrie.command.failed` |
| `2026-11-05 00:03:16` | `cowrie.log.closed` |
| `2026-11-05 00:03:17` | `cowrie.session.params` |
| `2026-11-05 00:03:17` | `cowrie.command.input` |
| `2026-11-05 00:03:17` | `cowrie.session.file_download` |
| `2026-11-05 00:03:17` | `cowrie.log.closed` |
| `2026-11-05 00:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.186[.]3` to AbuseIPDB if not already reported
- [ ] Block `172.172.186[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729ed9f38f4a

| Field | Detail |
|---|---|
| **Source IP** | `179.43.153[.]2` |
| **First Seen** | 2026-11-05 00:03 |
| **Last Seen** | 2026-11-05 00:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:03:15` | `cowrie.session.connect` |
| `2026-11-05 00:03:15` | `cowrie.client.version` |
| `2026-11-05 00:03:16` | `cowrie.client.kex` |
| `2026-11-05 00:03:17` | `cowrie.login.success` |
| `2026-11-05 00:03:18` | `cowrie.session.params` |
| `2026-11-05 00:03:18` | `cowrie.command.input` |
| `2026-11-05 00:03:18` | `cowrie.log.closed` |
| `2026-11-05 00:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.153[.]2` to AbuseIPDB if not already reported
- [ ] Block `179.43.153[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5228cf2f90

| Field | Detail |
|---|---|
| **Source IP** | `172.172.186[.]3` |
| **First Seen** | 2026-11-05 00:03 |
| **Last Seen** | 2026-11-05 00:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:03:17` | `cowrie.session.connect` |
| `2026-11-05 00:03:17` | `cowrie.client.version` |
| `2026-11-05 00:03:17` | `cowrie.client.kex` |
| `2026-11-05 00:03:17` | `cowrie.login.success` |
| `2026-11-05 00:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.186[.]3` to AbuseIPDB if not already reported
- [ ] Block `172.172.186[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0231d3cc55cb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:03 |
| **Last Seen** | 2026-11-05 00:07 |
| **Session Duration** | 228s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_73ea57e36f3fa398a372ba0868159901_small_control'"'"' '"'"'check_73ea57e36f3fa398a372ba0868159901'"'"'', printf '\n%s|%s\n' 'check_73ea57e36f3fa398a372ba0868159901_small_control' 'check_73ea57e36f3fa398a372ba0868159901', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_73ea57e36f3fa398a372ba0868159901_small_math'"'"' "$((762*698+90))"', (762*698+90, printf '\n%s|%s\n' 'check_73ea57e36f3fa398a372ba0868159901_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:03:47` | `cowrie.session.connect` |
| `2026-11-05 00:03:48` | `cowrie.client.version` |
| `2026-11-05 00:03:48` | `cowrie.client.kex` |
| `2026-11-05 00:03:56` | `cowrie.login.success` |
| `2026-11-05 00:04:00` | `cowrie.client.size` |
| `2026-11-05 00:04:03` | `cowrie.session.params` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| `2026-11-05 00:04:04` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffeb5362a210

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:08 |
| **Last Seen** | 2026-11-05 00:11 |
| **Session Duration** | 179s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bcdbdb7f0cebe9ff5a48e008114d396c_small_control'"'"' '"'"'check_bcdbdb7f0cebe9ff5a48e008114d396c'"'"'', printf '\n%s|%s\n' 'check_bcdbdb7f0cebe9ff5a48e008114d396c_small_control' 'check_bcdbdb7f0cebe9ff5a48e008114d396c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bcdbdb7f0cebe9ff5a48e008114d396c_small_math'"'"' "$((492*696+42))"', (492*696+42, printf '\n%s|%s\n' 'check_bcdbdb7f0cebe9ff5a48e008114d396c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:08:38` | `cowrie.session.connect` |
| `2026-11-05 00:08:39` | `cowrie.client.version` |
| `2026-11-05 00:08:39` | `cowrie.client.kex` |
| `2026-11-05 00:08:41` | `cowrie.login.success` |
| `2026-11-05 00:08:43` | `cowrie.client.size` |
| `2026-11-05 00:08:45` | `cowrie.session.params` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| `2026-11-05 00:08:47` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc92a9a5ab2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:12 |
| **Last Seen** | 2026-11-05 00:16 |
| **Session Duration** | 191s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_07c21cde1b490d8b398264d6a75fb203_small_control'"'"' '"'"'check_07c21cde1b490d8b398264d6a75fb203'"'"'', printf '\n%s|%s\n' 'check_07c21cde1b490d8b398264d6a75fb203_small_control' 'check_07c21cde1b490d8b398264d6a75fb203', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_07c21cde1b490d8b398264d6a75fb203_small_math'"'"' "$((990*454+47))"', (990*454+47, printf '\n%s|%s\n' 'check_07c21cde1b490d8b398264d6a75fb203_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:12:49` | `cowrie.session.connect` |
| `2026-11-05 00:12:50` | `cowrie.client.version` |
| `2026-11-05 00:12:50` | `cowrie.client.kex` |
| `2026-11-05 00:13:13` | `cowrie.login.success` |
| `2026-11-05 00:13:16` | `cowrie.client.size` |
| `2026-11-05 00:13:17` | `cowrie.session.params` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| `2026-11-05 00:13:18` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc19323df1f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:17 |
| **Last Seen** | 2026-11-05 00:19 |
| **Session Duration** | 154s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60c0ad2c0a60e430550643bad52e127d_small_control'"'"' '"'"'check_60c0ad2c0a60e430550643bad52e127d'"'"'', printf '\n%s|%s\n' 'check_60c0ad2c0a60e430550643bad52e127d_small_control' 'check_60c0ad2c0a60e430550643bad52e127d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_60c0ad2c0a60e430550643bad52e127d_small_math'"'"' "$((841*729+34))"', (841*729+34, printf '\n%s|%s\n' 'check_60c0ad2c0a60e430550643bad52e127d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:17:21` | `cowrie.session.connect` |
| `2026-11-05 00:17:22` | `cowrie.client.version` |
| `2026-11-05 00:17:22` | `cowrie.client.kex` |
| `2026-11-05 00:17:25` | `cowrie.login.success` |
| `2026-11-05 00:17:28` | `cowrie.client.size` |
| `2026-11-05 00:17:30` | `cowrie.session.params` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| `2026-11-05 00:17:31` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2fd26bbe58

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:20 |
| **Last Seen** | 2026-11-05 00:23 |
| **Session Duration** | 188s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f9b15aaaf402ed031467e30cc008b7b8_small_control'"'"' '"'"'check_f9b15aaaf402ed031467e30cc008b7b8'"'"'', printf '\n%s|%s\n' 'check_f9b15aaaf402ed031467e30cc008b7b8_small_control' 'check_f9b15aaaf402ed031467e30cc008b7b8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f9b15aaaf402ed031467e30cc008b7b8_small_math'"'"' "$((114*418+96))"', (114*418+96, printf '\n%s|%s\n' 'check_f9b15aaaf402ed031467e30cc008b7b8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:20:49` | `cowrie.session.connect` |
| `2026-11-05 00:20:51` | `cowrie.client.version` |
| `2026-11-05 00:20:51` | `cowrie.client.kex` |
| `2026-11-05 00:20:56` | `cowrie.login.success` |
| `2026-11-05 00:21:00` | `cowrie.client.size` |
| `2026-11-05 00:21:01` | `cowrie.session.params` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| `2026-11-05 00:21:02` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb384edc335

| Field | Detail |
|---|---|
| **Source IP** | `91.186.216[.]80` |
| **First Seen** | 2026-11-05 00:22 |
| **Last Seen** | 2026-11-05 00:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:22:48` | `cowrie.session.connect` |
| `2026-11-05 00:22:48` | `cowrie.login.success` |
| `2026-11-05 00:22:49` | `cowrie.session.params` |
| `2026-11-05 00:22:49` | `cowrie.command.input` |
| `2026-11-05 00:22:50` | `cowrie.log.closed` |
| `2026-11-05 00:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.186.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `91.186.216[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79cd7f4d0123

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:25 |
| **Last Seen** | 2026-11-05 00:28 |
| **Session Duration** | 177s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1401f2241c19c58086f9a947efe5419_small_control'"'"' '"'"'check_e1401f2241c19c58086f9a947efe5419'"'"'', printf '\n%s|%s\n' 'check_e1401f2241c19c58086f9a947efe5419_small_control' 'check_e1401f2241c19c58086f9a947efe5419', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1401f2241c19c58086f9a947efe5419_small_math'"'"' "$((836*43+47))"', (836*43+47, printf '\n%s|%s\n' 'check_e1401f2241c19c58086f9a947efe5419_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:25:25` | `cowrie.session.connect` |
| `2026-11-05 00:25:25` | `cowrie.client.version` |
| `2026-11-05 00:25:25` | `cowrie.client.kex` |
| `2026-11-05 00:25:30` | `cowrie.login.success` |
| `2026-11-05 00:25:33` | `cowrie.client.size` |
| `2026-11-05 00:25:34` | `cowrie.session.params` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| `2026-11-05 00:25:37` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb5cea200ec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:29 |
| **Last Seen** | 2026-11-05 00:32 |
| **Session Duration** | 179s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2cb4e41e50c4bad0ac1dd24846644e6f_small_control'"'"' '"'"'check_2cb4e41e50c4bad0ac1dd24846644e6f'"'"'', printf '\n%s|%s\n' 'check_2cb4e41e50c4bad0ac1dd24846644e6f_small_control' 'check_2cb4e41e50c4bad0ac1dd24846644e6f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2cb4e41e50c4bad0ac1dd24846644e6f_small_math'"'"' "$((478*921+96))"', (478*921+96, printf '\n%s|%s\n' 'check_2cb4e41e50c4bad0ac1dd24846644e6f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:29:36` | `cowrie.session.connect` |
| `2026-11-05 00:29:37` | `cowrie.client.version` |
| `2026-11-05 00:29:37` | `cowrie.client.kex` |
| `2026-11-05 00:29:42` | `cowrie.login.success` |
| `2026-11-05 00:29:45` | `cowrie.client.size` |
| `2026-11-05 00:29:47` | `cowrie.session.params` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| `2026-11-05 00:29:51` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f122252ac3a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.86[.]183` |
| **First Seen** | 2026-11-05 00:31 |
| **Last Seen** | 2026-11-05 00:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:31:02` | `cowrie.session.connect` |
| `2026-11-05 00:31:02` | `cowrie.client.version` |
| `2026-11-05 00:31:02` | `cowrie.client.kex` |
| `2026-11-05 00:31:03` | `cowrie.login.success` |
| `2026-11-05 00:31:05` | `cowrie.session.params` |
| `2026-11-05 00:31:05` | `cowrie.command.input` |
| `2026-11-05 00:31:05` | `cowrie.command.failed` |
| `2026-11-05 00:31:05` | `cowrie.log.closed` |
| `2026-11-05 00:31:06` | `cowrie.session.params` |
| `2026-11-05 00:31:06` | `cowrie.command.input` |
| `2026-11-05 00:31:06` | `cowrie.session.file_download` |
| `2026-11-05 00:31:06` | `cowrie.log.closed` |
| `2026-11-05 00:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.86[.]183` to AbuseIPDB if not already reported
- [ ] Block `14.103.86[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b883e5af73f2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.86[.]183` |
| **First Seen** | 2026-11-05 00:31 |
| **Last Seen** | 2026-11-05 00:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:31:07` | `cowrie.session.connect` |
| `2026-11-05 00:31:07` | `cowrie.client.version` |
| `2026-11-05 00:31:07` | `cowrie.client.kex` |
| `2026-11-05 00:31:08` | `cowrie.login.success` |
| `2026-11-05 00:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.86[.]183` to AbuseIPDB if not already reported
- [ ] Block `14.103.86[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a6ffadac49

| Field | Detail |
|---|---|
| **Source IP** | `160.16.105[.]184` |
| **First Seen** | 2026-11-05 00:33 |
| **Last Seen** | 2026-11-05 00:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:33:21` | `cowrie.session.connect` |
| `2026-11-05 00:33:21` | `cowrie.client.version` |
| `2026-11-05 00:33:22` | `cowrie.client.kex` |
| `2026-11-05 00:33:22` | `cowrie.login.success` |
| `2026-11-05 00:33:23` | `cowrie.session.params` |
| `2026-11-05 00:33:23` | `cowrie.command.input` |
| `2026-11-05 00:33:23` | `cowrie.command.failed` |
| `2026-11-05 00:33:23` | `cowrie.log.closed` |
| `2026-11-05 00:33:24` | `cowrie.session.params` |
| `2026-11-05 00:33:24` | `cowrie.command.input` |
| `2026-11-05 00:33:25` | `cowrie.session.file_download` |
| `2026-11-05 00:33:25` | `cowrie.log.closed` |
| `2026-11-05 00:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.16.105[.]184` to AbuseIPDB if not already reported
- [ ] Block `160.16.105[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827cf686dfdc

| Field | Detail |
|---|---|
| **Source IP** | `160.16.105[.]184` |
| **First Seen** | 2026-11-05 00:33 |
| **Last Seen** | 2026-11-05 00:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:33:25` | `cowrie.session.connect` |
| `2026-11-05 00:33:25` | `cowrie.client.version` |
| `2026-11-05 00:33:25` | `cowrie.client.kex` |
| `2026-11-05 00:33:26` | `cowrie.login.success` |
| `2026-11-05 00:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.16.105[.]184` to AbuseIPDB if not already reported
- [ ] Block `160.16.105[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a677984ba371

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:33 |
| **Last Seen** | 2026-11-05 00:36 |
| **Session Duration** | 172s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a6b6731940d809b9ef828b0ac5340827_small_control'"'"' '"'"'check_a6b6731940d809b9ef828b0ac5340827'"'"'', printf '\n%s|%s\n' 'check_a6b6731940d809b9ef828b0ac5340827_small_control' 'check_a6b6731940d809b9ef828b0ac5340827', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a6b6731940d809b9ef828b0ac5340827_small_math'"'"' "$((805*727+96))"', (805*727+96, printf '\n%s|%s\n' 'check_a6b6731940d809b9ef828b0ac5340827_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:33:26` | `cowrie.session.connect` |
| `2026-11-05 00:33:28` | `cowrie.client.version` |
| `2026-11-05 00:33:28` | `cowrie.client.kex` |
| `2026-11-05 00:33:37` | `cowrie.login.success` |
| `2026-11-05 00:33:40` | `cowrie.client.size` |
| `2026-11-05 00:33:44` | `cowrie.session.params` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| `2026-11-05 00:33:44` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8997f06d474

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-05 00:37 |
| **Last Seen** | 2026-11-05 00:39 |
| **Session Duration** | 92s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_241395d8f5ed9f897ff7ed9bfd6099c3_small_control'"'"' '"'"'check_241395d8f5ed9f897ff7ed9bfd6099c3'"'"'', printf '\n%s|%s\n' 'check_241395d8f5ed9f897ff7ed9bfd6099c3_small_control' 'check_241395d8f5ed9f897ff7ed9bfd6099c3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_241395d8f5ed9f897ff7ed9bfd6099c3_small_math'"'"' "$((263*703+21))"', (263*703+21, printf '\n%s|%s\n' 'check_241395d8f5ed9f897ff7ed9bfd6099c3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:37:54` | `cowrie.session.connect` |
| `2026-11-05 00:37:55` | `cowrie.client.version` |
| `2026-11-05 00:37:55` | `cowrie.client.kex` |
| `2026-11-05 00:38:01` | `cowrie.login.success` |
| `2026-11-05 00:38:06` | `cowrie.client.size` |
| `2026-11-05 00:38:07` | `cowrie.session.params` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| `2026-11-05 00:38:09` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d060335bc5b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-05 00:47 |
| **Last Seen** | 2026-11-05 00:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, cat /proc, >` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:47:14` | `cowrie.session.connect` |
| `2026-11-05 00:47:14` | `cowrie.login.success` |
| `2026-11-05 00:47:15` | `cowrie.session.params` |
| `2026-11-05 00:47:15` | `cowrie.command.input` |
| `2026-11-05 00:47:16` | `cowrie.command.input` |
| `2026-11-05 00:47:16` | `cowrie.command.input` |
| `2026-11-05 00:47:19` | `cowrie.log.closed` |
| `2026-11-05 00:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5a2c924a2c

| Field | Detail |
|---|---|
| **Source IP** | `159.192.123[.]159` |
| **First Seen** | 2026-11-05 00:53 |
| **Last Seen** | 2026-11-05 00:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 00:53:08` | `cowrie.session.connect` |
| `2026-11-05 00:53:08` | `cowrie.client.version` |
| `2026-11-05 00:53:08` | `cowrie.client.kex` |
| `2026-11-05 00:53:09` | `cowrie.login.success` |
| `2026-11-05 00:53:10` | `cowrie.session.params` |
| `2026-11-05 00:53:10` | `cowrie.command.input` |
| `2026-11-05 00:53:11` | `cowrie.log.closed` |
| `2026-11-05 00:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.192.123[.]159` to AbuseIPDB if not already reported
- [ ] Block `159.192.123[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56d8a52f835

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]150` |
| **First Seen** | 2026-11-05 01:01 |
| **Last Seen** | 2026-11-05 01:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 01:01:05` | `cowrie.session.connect` |
| `2026-11-05 01:01:05` | `cowrie.client.version` |
| `2026-11-05 01:01:05` | `cowrie.client.kex` |
| `2026-11-05 01:01:06` | `cowrie.login.success` |
| `2026-11-05 01:01:06` | `cowrie.session.params` |
| `2026-11-05 01:01:06` | `cowrie.command.input` |
| `2026-11-05 01:01:06` | `cowrie.command.failed` |
| `2026-11-05 01:01:07` | `cowrie.log.closed` |
| `2026-11-05 01:01:07` | `cowrie.session.params` |
| `2026-11-05 01:01:07` | `cowrie.command.input` |
| `2026-11-05 01:01:07` | `cowrie.session.file_download` |
| `2026-11-05 01:01:07` | `cowrie.log.closed` |
| `2026-11-05 01:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]150` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644be78b313c

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]150` |
| **First Seen** | 2026-11-05 01:01 |
| **Last Seen** | 2026-11-05 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 01:01:08` | `cowrie.session.connect` |
| `2026-11-05 01:01:08` | `cowrie.client.version` |
| `2026-11-05 01:01:08` | `cowrie.client.kex` |
| `2026-11-05 01:01:08` | `cowrie.login.success` |
| `2026-11-05 01:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]150` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79fec77e904

| Field | Detail |
|---|---|
| **Source IP** | `23.95.110[.]131` |
| **First Seen** | 2026-11-05 01:03 |
| **Last Seen** | 2026-11-05 01:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 01:03:51` | `cowrie.session.connect` |
| `2026-11-05 01:03:51` | `cowrie.client.version` |
| `2026-11-05 01:03:51` | `cowrie.client.kex` |
| `2026-11-05 01:03:52` | `cowrie.login.success` |
| `2026-11-05 01:03:52` | `cowrie.session.params` |
| `2026-11-05 01:03:52` | `cowrie.command.input` |
| `2026-11-05 01:03:52` | `cowrie.command.failed` |
| `2026-11-05 01:03:52` | `cowrie.log.closed` |
| `2026-11-05 01:03:53` | `cowrie.session.params` |
| `2026-11-05 01:03:53` | `cowrie.command.input` |
| `2026-11-05 01:03:53` | `cowrie.session.file_download` |
| `2026-11-05 01:03:53` | `cowrie.log.closed` |
| `2026-11-05 01:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.95.110[.]131` to AbuseIPDB if not already reported
- [ ] Block `23.95.110[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83af6962c400

| Field | Detail |
|---|---|
| **Source IP** | `23.95.110[.]131` |
| **First Seen** | 2026-11-05 01:03 |
| **Last Seen** | 2026-11-05 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 01:03:53` | `cowrie.session.connect` |
| `2026-11-05 01:03:53` | `cowrie.client.version` |
| `2026-11-05 01:03:53` | `cowrie.client.kex` |
| `2026-11-05 01:03:53` | `cowrie.login.success` |
| `2026-11-05 01:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.95.110[.]131` to AbuseIPDB if not already reported
- [ ] Block `23.95.110[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5c63ac8a36

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-05 01:14 |
| **Last Seen** | 2026-11-05 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 01:14:53` | `cowrie.session.connect` |
| `2026-11-05 01:14:53` | `cowrie.client.version` |
| `2026-11-05 01:14:53` | `cowrie.client.kex` |
| `2026-11-05 01:14:53` | `cowrie.login.success` |
| `2026-11-05 01:14:53` | `cowrie.direct-tcpip.request` |
| `2026-11-05 01:14:53` | `cowrie.direct-tcpip.data` |
| `2026-11-05 01:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (17) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-f77e89d3ff4d | HIGH | `79.3.96[.]178` | 2026-11-05 01:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0b0c71c4cb5b | HIGH | `79.3.96[.]178` | 2026-11-05 01:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4f6bf3458334 | HIGH | `124.43.4[.]17` | 2026-11-05 01:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4f7d39bdd687 | HIGH | `124.43.4[.]17` | 2026-11-05 01:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-58bfbd588191 | HIGH | `77.239.124[.]153` | 2026-11-05 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5803eadc24e4 | HIGH | `193.32.162[.]15` | 2026-11-05 02:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba0917912391 | HIGH | `176.53.159[.]196` | 2026-11-05 02:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fccdc407e8d9 | HIGH | `103.250.10[.]42` | 2026-11-05 02:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-684190e73e53 | HIGH | `103.250.10[.]42` | 2026-11-05 02:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ff4462b04b7f | HIGH | `195.178.110[.]78` | 2026-11-05 02:29 | Y | 3 | 0 | `T1078 · T1083` |
| IR-428d3095d3cb | HIGH | `203.83.234[.]180` | 2026-11-05 02:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d07cf444191c | HIGH | `203.83.234[.]180` | 2026-11-05 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d369c32f74ba | HIGH | `195.86.192[.]66` | 2026-11-05 02:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-526b8266dfb3 | HIGH | `195.86.192[.]66` | 2026-11-05 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f8f68edd53a | HIGH | `36.163.118[.]106` | 2026-11-05 02:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9756c0d12039 | HIGH | `49.0.24[.]107` | 2026-11-05 02:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dd2480b830ec | HIGH | `49.0.24[.]107` | 2026-11-05 02:54 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **2** | 2026-11-05 01:07 | 2026-11-05 02:06 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-05 00:25 | 2026-11-05 02:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.80.39[.]74` | 1 | 2026-11-05 02:39 | 2026-11-05 02:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.114[.]236` | 1 | 2026-11-05 00:00 | 2026-11-05 00:00 | 302s | 0 | `T1592` | 🟢 LOW |
| `118.196.45[.]105` | 1 | 2026-11-05 02:37 | 2026-11-05 02:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.224.78[.]164` | 1 | 2026-11-05 02:06 | 2026-11-05 02:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.191[.]90` | 1 | 2026-11-05 00:22 | 2026-11-05 00:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.122.102[.]148` | 1 | 2026-11-05 00:32 | 2026-11-05 00:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.246.218[.]62` | 1 | 2026-11-05 00:01 | 2026-11-05 00:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]34` | 1 | 2026-11-05 01:09 | 2026-11-05 01:09 | 4s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-05 02:06 | 2026-11-05 02:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-11-05 02:05 | 2026-11-05 02:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.44.143[.]169` | 1 | 2026-11-05 01:41 | 2026-11-05 01:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]194` | 1 | 2026-11-05 01:31 | 2026-11-05 01:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `191.113.92[.]33` | 1 | 2026-11-05 00:10 | 2026-11-05 00:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-05 02:04 | 2026-11-05 02:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.163.118[.]106` | 1 | 2026-11-05 02:42 | 2026-11-05 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.240.164[.]208` | 1 | 2026-11-05 00:33 | 2026-11-05 00:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-05 01:07 | 2026-11-05 01:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-05 02:48 | 2026-11-05 02:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-05 00:37 | 2026-11-05 00:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-05 00:38 | 2026-11-05 00:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | 1 | 2026-11-05 01:50 | 2026-11-05 01:51 | 93s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]205` | 1 | 2026-11-05 02:18 | 2026-11-05 02:18 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-11-05 02:40 | 2026-11-05 02:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.240.192[.]82` | 1 | 2026-11-05 02:37 | 2026-11-05 02:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]153` | 1 | 2026-11-05 00:16 | 2026-11-05 00:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `140.246.218[.]62` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 7 |
| `42.240.164[.]208` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 29 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `151.243.11[.]34` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 10 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.148.10[.]151` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `191.113.92[.]33` | CL | TELEFÓNICA CHILE S.A. | **100** ⚠️ | 0 |
| `118.196.114[.]236` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 40 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `47.120.30[.]67` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 95 cases |
| Tool 34  | Credential Extractor        | ✅ 1206 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 15 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 61 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (25.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 27 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-05T04:05:48Z_

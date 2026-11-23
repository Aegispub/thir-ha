# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-23 |
| **Generated At** | 2026-11-23T23:03:43Z |
| **Shift Time** | 23:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1477** |
| Confirmed Threats | **1368** |
| False Positives Filtered | **109** (7.4%) |
| Unique Attacker IPs | **951** |
| Countries of Origin | **89** |
| High Severity Cases | **1143** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **334** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3521** |
| Unique Credential Pairs | **1604** |
| Unique Usernames | **456** |
| Unique Passwords | **1058** |
| Successful Auth Pairs | **2724** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1043 |
| `admin` | 248 |
| `supervisor` | 198 |
| `support` | 161 |
| `operator` | 129 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 98 |
| `admin` | 78 |
| `1234` | 60 |
| `root` | 59 |
| `password` | 48 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 42 |
| `admin` | `admin` | 38 |
| `root` | `root` | 36 |
| `rootssssss23424123123` | `rootssssss23424123123` | 30 |
| `nobody` | `` | 27 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123123` | `92.118.39.75` | 2026-11-23T02:56:16 |
| `root` | `12345678` | `193.32.162.84` | 2026-11-23T02:56:56 |
| `root` | `123321` | `92.118.39.75` | 2026-11-23T02:58:02 |
| `root` | `123456789` | `193.32.162.84` | 2026-11-23T02:59:05 |
| `root` | `1234` | `92.118.39.75` | 2026-11-23T02:59:46 |
| `root` | `1234567890` | `193.32.162.84` | 2026-11-23T03:01:12 |
| `root` | `12345` | `92.118.39.75` | 2026-11-23T03:01:31 |
| `root` | `123abc` | `193.32.162.84` | 2026-11-23T03:03:20 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-23T03:04:47 |
| `root` | `1234567` | `92.118.39.75` | 2026-11-23T03:05:04 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-11-23T03:05:28 |
| `root` | `12345678` | `92.118.39.75` | 2026-11-23T03:07:14 |
| `root` | `P@ssw0rd123` | `193.32.162.84` | 2026-11-23T03:07:38 |
| `root` | `123456789` | `92.118.39.75` | 2026-11-23T03:09:22 |
| `root` | `abc123` | `193.32.162.84` | 2026-11-23T03:09:48 |
| `support` | `support` | `10.0.0.73` | 2026-11-23T03:10:52 |
| `root` | `1234abcd` | `92.118.39.75` | 2026-11-23T03:11:34 |
| `root` | `admin123` | `193.32.162.84` | 2026-11-23T03:12:15 |
| `root` | `123abc` | `92.118.39.75` | 2026-11-23T03:13:51 |
| `root` | `letmein` | `193.32.162.84` | 2026-11-23T03:14:29 |
_… 2704 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1477** |
| Sessions with Fingerprint | **35** |
| Unique HASSH Fingerprints | **35** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 866 |
| Go SSH scanner | 261 |
| libssh | 35 |
| PuTTY | 6 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 845 | 694 |
| `2ec37a7cc8da...` | Mirai/variant | 200 | 5 |
| `f555226df196...` | Mirai/variant | 20 | 10 |
| `7d01d047ace6...` | Mirai/variant | 16 | 2 |
| `eff4c24daffc...` | Modern SSH client | 11 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 845 | 694 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 200 | 5 | Mirai/variant |
| `f555226df196...` | libssh | 20 | 10 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 16 | 2 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 15 | 15 | — |
| `eff4c24daffc...` | Go SSH scanner | 11 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 10 | 5 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 8 | 4 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **208** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 15 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
cat /proc/mounts; /bin/busybox ZCJRH
```
Source IPs: `85.50.7.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.96.173.169`, `49.75.185.71`, `119.246.15.94`, `79.34.224.119`, `178.253.95.34`, `8.137.84.60`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **951** |
| Unique ASNs | **324** |
| High-Risk ASNs | **220** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 140 | HIGH |
| `AS4134` | CHINANET BACKBONE | 55 | HIGH |
| `AS4766` | Korea Telecom | 51 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 31 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 26 | HIGH |
| `AS22773` | Cox Communications, LLC | 16 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 16 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 15 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1120)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9e868cfdc6f2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 02:56 |
| **Last Seen** | 2026-11-23 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39f2bb8e061c3d73911a627f2d27cd61_small_control'"'"' '"'"'check_39f2bb8e061c3d73911a627f2d27cd61'"'"'', printf '\n%s|%s\n' 'check_39f2bb8e061c3d73911a627f2d27cd61_small_control' 'check_39f2bb8e061c3d73911a627f2d27cd61', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_39f2bb8e061c3d73911a627f2d27cd61_small_math'"'"' "$((877*447+91))"', (877*447+91, printf '\n%s|%s\n' 'check_39f2bb8e061c3d73911a627f2d27cd61_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:56:13` | `cowrie.session.connect` |
| `2026-11-23 02:56:13` | `cowrie.client.version` |
| `2026-11-23 02:56:13` | `cowrie.client.kex` |
| `2026-11-23 02:56:16` | `cowrie.login.success` |
| `2026-11-23 02:56:18` | `cowrie.client.size` |
| `2026-11-23 02:56:18` | `cowrie.session.params` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| `2026-11-23 02:56:19` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc770546e1a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:56 |
| **Last Seen** | 2026-11-23 02:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_96778cc9e9a4f95f52278ee4de41db3f_small_control'"'"' '"'"'check_96778cc9e9a4f95f52278ee4de41db3f'"'"'', printf '\n%s|%s\n' 'check_96778cc9e9a4f95f52278ee4de41db3f_small_control' 'check_96778cc9e9a4f95f52278ee4de41db3f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_96778cc9e9a4f95f52278ee4de41db3f_small_math'"'"' "$((634*366+11))"', (634*366+11, printf '\n%s|%s\n' 'check_96778cc9e9a4f95f52278ee4de41db3f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:56:53` | `cowrie.session.connect` |
| `2026-11-23 02:56:53` | `cowrie.client.version` |
| `2026-11-23 02:56:53` | `cowrie.client.kex` |
| `2026-11-23 02:56:56` | `cowrie.login.success` |
| `2026-11-23 02:56:58` | `cowrie.client.size` |
| `2026-11-23 02:56:58` | `cowrie.session.params` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| `2026-11-23 02:56:59` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc371248d63

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 02:57 |
| **Last Seen** | 2026-11-23 02:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f558228c38f70f92bdd545353c26362c_small_control'"'"' '"'"'check_f558228c38f70f92bdd545353c26362c'"'"'', printf '\n%s|%s\n' 'check_f558228c38f70f92bdd545353c26362c_small_control' 'check_f558228c38f70f92bdd545353c26362c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f558228c38f70f92bdd545353c26362c_small_math'"'"' "$((995*917+50))"', (995*917+50, printf '\n%s|%s\n' 'check_f558228c38f70f92bdd545353c26362c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:57:59` | `cowrie.session.connect` |
| `2026-11-23 02:57:59` | `cowrie.client.version` |
| `2026-11-23 02:57:59` | `cowrie.client.kex` |
| `2026-11-23 02:58:02` | `cowrie.login.success` |
| `2026-11-23 02:58:04` | `cowrie.client.size` |
| `2026-11-23 02:58:05` | `cowrie.session.params` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| `2026-11-23 02:58:06` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa15e7ec40cd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 02:59 |
| **Last Seen** | 2026-11-23 02:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_586e981d7ba3680e3ee12dd3f132e6f7_small_control'"'"' '"'"'check_586e981d7ba3680e3ee12dd3f132e6f7'"'"'', printf '\n%s|%s\n' 'check_586e981d7ba3680e3ee12dd3f132e6f7_small_control' 'check_586e981d7ba3680e3ee12dd3f132e6f7', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_586e981d7ba3680e3ee12dd3f132e6f7_small_math'"'"' "$((705*293+38))"', (705*293+38, printf '\n%s|%s\n' 'check_586e981d7ba3680e3ee12dd3f132e6f7_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:59:01` | `cowrie.session.connect` |
| `2026-11-23 02:59:02` | `cowrie.client.version` |
| `2026-11-23 02:59:02` | `cowrie.client.kex` |
| `2026-11-23 02:59:05` | `cowrie.login.success` |
| `2026-11-23 02:59:07` | `cowrie.client.size` |
| `2026-11-23 02:59:08` | `cowrie.session.params` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| `2026-11-23 02:59:09` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892d873542a0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 02:59 |
| **Last Seen** | 2026-11-23 02:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c2efd439ab47a407fb5461645bf9ada3_small_control'"'"' '"'"'check_c2efd439ab47a407fb5461645bf9ada3'"'"'', printf '\n%s|%s\n' 'check_c2efd439ab47a407fb5461645bf9ada3_small_control' 'check_c2efd439ab47a407fb5461645bf9ada3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c2efd439ab47a407fb5461645bf9ada3_small_math'"'"' "$((54*816+46))"', (54*816+46, printf '\n%s|%s\n' 'check_c2efd439ab47a407fb5461645bf9ada3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 02:59:43` | `cowrie.session.connect` |
| `2026-11-23 02:59:43` | `cowrie.client.version` |
| `2026-11-23 02:59:43` | `cowrie.client.kex` |
| `2026-11-23 02:59:46` | `cowrie.login.success` |
| `2026-11-23 02:59:48` | `cowrie.client.size` |
| `2026-11-23 02:59:48` | `cowrie.session.params` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| `2026-11-23 02:59:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239548602dd3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:01 |
| **Last Seen** | 2026-11-23 03:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3a262e7d4479276e3aa8e2aa88430fc0_small_control'"'"' '"'"'check_3a262e7d4479276e3aa8e2aa88430fc0'"'"'', printf '\n%s|%s\n' 'check_3a262e7d4479276e3aa8e2aa88430fc0_small_control' 'check_3a262e7d4479276e3aa8e2aa88430fc0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3a262e7d4479276e3aa8e2aa88430fc0_small_math'"'"' "$((929*10+46))"', (929*10+46, printf '\n%s|%s\n' 'check_3a262e7d4479276e3aa8e2aa88430fc0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:01:08` | `cowrie.session.connect` |
| `2026-11-23 03:01:09` | `cowrie.client.version` |
| `2026-11-23 03:01:09` | `cowrie.client.kex` |
| `2026-11-23 03:01:12` | `cowrie.login.success` |
| `2026-11-23 03:01:15` | `cowrie.client.size` |
| `2026-11-23 03:01:15` | `cowrie.session.params` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| `2026-11-23 03:01:16` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dee5c617e8b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:01 |
| **Last Seen** | 2026-11-23 03:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_20c241f5211b985e9ac2d09000f0c7ee_small_control'"'"' '"'"'check_20c241f5211b985e9ac2d09000f0c7ee'"'"'', printf '\n%s|%s\n' 'check_20c241f5211b985e9ac2d09000f0c7ee_small_control' 'check_20c241f5211b985e9ac2d09000f0c7ee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_20c241f5211b985e9ac2d09000f0c7ee_small_math'"'"' "$((411*39+45))"', (411*39+45, printf '\n%s|%s\n' 'check_20c241f5211b985e9ac2d09000f0c7ee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:01:29` | `cowrie.session.connect` |
| `2026-11-23 03:01:29` | `cowrie.client.version` |
| `2026-11-23 03:01:29` | `cowrie.client.kex` |
| `2026-11-23 03:01:31` | `cowrie.login.success` |
| `2026-11-23 03:01:33` | `cowrie.client.size` |
| `2026-11-23 03:01:34` | `cowrie.session.params` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| `2026-11-23 03:01:35` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4055245eb678

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:03 |
| **Last Seen** | 2026-11-23 03:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3c740e97ebe2769892423c7ad0bac0a2_small_control'"'"' '"'"'check_3c740e97ebe2769892423c7ad0bac0a2'"'"'', printf '\n%s|%s\n' 'check_3c740e97ebe2769892423c7ad0bac0a2_small_control' 'check_3c740e97ebe2769892423c7ad0bac0a2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3c740e97ebe2769892423c7ad0bac0a2_small_math'"'"' "$((522*763+54))"', (522*763+54, printf '\n%s|%s\n' 'check_3c740e97ebe2769892423c7ad0bac0a2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:03:16` | `cowrie.session.connect` |
| `2026-11-23 03:03:17` | `cowrie.client.version` |
| `2026-11-23 03:03:17` | `cowrie.client.kex` |
| `2026-11-23 03:03:20` | `cowrie.login.success` |
| `2026-11-23 03:03:21` | `cowrie.client.size` |
| `2026-11-23 03:03:22` | `cowrie.session.params` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| `2026-11-23 03:03:23` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1cb338f0ec4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-23 03:04 |
| **Last Seen** | 2026-11-23 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:04:47` | `cowrie.session.connect` |
| `2026-11-23 03:04:47` | `cowrie.login.success` |
| `2026-11-23 03:04:48` | `cowrie.session.params` |
| `2026-11-23 03:04:48` | `cowrie.log.closed` |
| `2026-11-23 03:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd7386fe35f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:05 |
| **Last Seen** | 2026-11-23 03:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1a48789bcd600c34cdfdede611eff16e_small_control'"'"' '"'"'check_1a48789bcd600c34cdfdede611eff16e'"'"'', printf '\n%s|%s\n' 'check_1a48789bcd600c34cdfdede611eff16e_small_control' 'check_1a48789bcd600c34cdfdede611eff16e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1a48789bcd600c34cdfdede611eff16e_small_math'"'"' "$((747*155+36))"', (747*155+36, printf '\n%s|%s\n' 'check_1a48789bcd600c34cdfdede611eff16e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:05:00` | `cowrie.session.connect` |
| `2026-11-23 03:05:01` | `cowrie.client.version` |
| `2026-11-23 03:05:01` | `cowrie.client.kex` |
| `2026-11-23 03:05:04` | `cowrie.login.success` |
| `2026-11-23 03:05:07` | `cowrie.client.size` |
| `2026-11-23 03:05:07` | `cowrie.session.params` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| `2026-11-23 03:05:08` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b04124972c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:05 |
| **Last Seen** | 2026-11-23 03:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d82037999fb0f2e7fb84add9b8ce3cd3_small_control'"'"' '"'"'check_d82037999fb0f2e7fb84add9b8ce3cd3'"'"'', printf '\n%s|%s\n' 'check_d82037999fb0f2e7fb84add9b8ce3cd3_small_control' 'check_d82037999fb0f2e7fb84add9b8ce3cd3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d82037999fb0f2e7fb84add9b8ce3cd3_small_math'"'"' "$((494*360+39))"', (494*360+39, printf '\n%s|%s\n' 'check_d82037999fb0f2e7fb84add9b8ce3cd3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:05:24` | `cowrie.session.connect` |
| `2026-11-23 03:05:25` | `cowrie.client.version` |
| `2026-11-23 03:05:25` | `cowrie.client.kex` |
| `2026-11-23 03:05:28` | `cowrie.login.success` |
| `2026-11-23 03:05:30` | `cowrie.client.size` |
| `2026-11-23 03:05:31` | `cowrie.session.params` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| `2026-11-23 03:05:31` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51da3a415ec9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:07 |
| **Last Seen** | 2026-11-23 03:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a9d68817d0eb3c18ee6d36955a797999_small_control'"'"' '"'"'check_a9d68817d0eb3c18ee6d36955a797999'"'"'', printf '\n%s|%s\n' 'check_a9d68817d0eb3c18ee6d36955a797999_small_control' 'check_a9d68817d0eb3c18ee6d36955a797999', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a9d68817d0eb3c18ee6d36955a797999_small_math'"'"' "$((608*155+23))"', (608*155+23, printf '\n%s|%s\n' 'check_a9d68817d0eb3c18ee6d36955a797999_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:07:10` | `cowrie.session.connect` |
| `2026-11-23 03:07:11` | `cowrie.client.version` |
| `2026-11-23 03:07:11` | `cowrie.client.kex` |
| `2026-11-23 03:07:14` | `cowrie.login.success` |
| `2026-11-23 03:07:16` | `cowrie.client.size` |
| `2026-11-23 03:07:17` | `cowrie.session.params` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| `2026-11-23 03:07:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb50882c0575

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:07 |
| **Last Seen** | 2026-11-23 03:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d7752ee7224241ff9ae5624213b3cc4c_small_control'"'"' '"'"'check_d7752ee7224241ff9ae5624213b3cc4c'"'"'', printf '\n%s|%s\n' 'check_d7752ee7224241ff9ae5624213b3cc4c_small_control' 'check_d7752ee7224241ff9ae5624213b3cc4c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d7752ee7224241ff9ae5624213b3cc4c_small_math'"'"' "$((323*116+62))"', (323*116+62, printf '\n%s|%s\n' 'check_d7752ee7224241ff9ae5624213b3cc4c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:07:35` | `cowrie.session.connect` |
| `2026-11-23 03:07:35` | `cowrie.client.version` |
| `2026-11-23 03:07:35` | `cowrie.client.kex` |
| `2026-11-23 03:07:38` | `cowrie.login.success` |
| `2026-11-23 03:07:40` | `cowrie.client.size` |
| `2026-11-23 03:07:41` | `cowrie.session.params` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| `2026-11-23 03:07:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4d971b89d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:09 |
| **Last Seen** | 2026-11-23 03:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7bde3dbe659a3dd8b4ef80b04d592b7f_small_control'"'"' '"'"'check_7bde3dbe659a3dd8b4ef80b04d592b7f'"'"'', printf '\n%s|%s\n' 'check_7bde3dbe659a3dd8b4ef80b04d592b7f_small_control' 'check_7bde3dbe659a3dd8b4ef80b04d592b7f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7bde3dbe659a3dd8b4ef80b04d592b7f_small_math'"'"' "$((804*942+89))"', (804*942+89, printf '\n%s|%s\n' 'check_7bde3dbe659a3dd8b4ef80b04d592b7f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:09:18` | `cowrie.session.connect` |
| `2026-11-23 03:09:19` | `cowrie.client.version` |
| `2026-11-23 03:09:19` | `cowrie.client.kex` |
| `2026-11-23 03:09:22` | `cowrie.login.success` |
| `2026-11-23 03:09:25` | `cowrie.client.size` |
| `2026-11-23 03:09:26` | `cowrie.session.params` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| `2026-11-23 03:09:27` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089261d205d9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:09 |
| **Last Seen** | 2026-11-23 03:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_02368dcfccead15e3f157dc330882ce3_small_control'"'"' '"'"'check_02368dcfccead15e3f157dc330882ce3'"'"'', printf '\n%s|%s\n' 'check_02368dcfccead15e3f157dc330882ce3_small_control' 'check_02368dcfccead15e3f157dc330882ce3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_02368dcfccead15e3f157dc330882ce3_small_math'"'"' "$((567*628+82))"', (567*628+82, printf '\n%s|%s\n' 'check_02368dcfccead15e3f157dc330882ce3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:09:45` | `cowrie.session.connect` |
| `2026-11-23 03:09:45` | `cowrie.client.version` |
| `2026-11-23 03:09:45` | `cowrie.client.kex` |
| `2026-11-23 03:09:48` | `cowrie.login.success` |
| `2026-11-23 03:09:50` | `cowrie.client.size` |
| `2026-11-23 03:09:51` | `cowrie.session.params` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| `2026-11-23 03:09:52` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8683b6e716af

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:11 |
| **Last Seen** | 2026-11-23 03:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_57b40a9462355ffca251a786e9072d0f_small_control'"'"' '"'"'check_57b40a9462355ffca251a786e9072d0f'"'"'', printf '\n%s|%s\n' 'check_57b40a9462355ffca251a786e9072d0f_small_control' 'check_57b40a9462355ffca251a786e9072d0f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_57b40a9462355ffca251a786e9072d0f_small_math'"'"' "$((519*727+46))"', (519*727+46, printf '\n%s|%s\n' 'check_57b40a9462355ffca251a786e9072d0f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:11:30` | `cowrie.session.connect` |
| `2026-11-23 03:11:30` | `cowrie.client.version` |
| `2026-11-23 03:11:30` | `cowrie.client.kex` |
| `2026-11-23 03:11:34` | `cowrie.login.success` |
| `2026-11-23 03:11:36` | `cowrie.client.size` |
| `2026-11-23 03:11:37` | `cowrie.session.params` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| `2026-11-23 03:11:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045b617fac66

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:12 |
| **Last Seen** | 2026-11-23 03:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_48804ac779d30628df7fb873b882ab25_small_control'"'"' '"'"'check_48804ac779d30628df7fb873b882ab25'"'"'', printf '\n%s|%s\n' 'check_48804ac779d30628df7fb873b882ab25_small_control' 'check_48804ac779d30628df7fb873b882ab25', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_48804ac779d30628df7fb873b882ab25_small_math'"'"' "$((615*315+34))"', (615*315+34, printf '\n%s|%s\n' 'check_48804ac779d30628df7fb873b882ab25_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:12:11` | `cowrie.session.connect` |
| `2026-11-23 03:12:12` | `cowrie.client.version` |
| `2026-11-23 03:12:12` | `cowrie.client.kex` |
| `2026-11-23 03:12:15` | `cowrie.login.success` |
| `2026-11-23 03:12:17` | `cowrie.client.size` |
| `2026-11-23 03:12:17` | `cowrie.session.params` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| `2026-11-23 03:12:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a39c1312411

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:13 |
| **Last Seen** | 2026-11-23 03:14 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2f8b359a0b7a0f43728ea150ecd441f9_small_control'"'"' '"'"'check_2f8b359a0b7a0f43728ea150ecd441f9'"'"'', printf '\n%s|%s\n' 'check_2f8b359a0b7a0f43728ea150ecd441f9_small_control' 'check_2f8b359a0b7a0f43728ea150ecd441f9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2f8b359a0b7a0f43728ea150ecd441f9_small_math'"'"' "$((208*840+47))"', (208*840+47, printf '\n%s|%s\n' 'check_2f8b359a0b7a0f43728ea150ecd441f9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:13:46` | `cowrie.session.connect` |
| `2026-11-23 03:13:47` | `cowrie.client.version` |
| `2026-11-23 03:13:47` | `cowrie.client.kex` |
| `2026-11-23 03:13:51` | `cowrie.login.success` |
| `2026-11-23 03:13:55` | `cowrie.client.size` |
| `2026-11-23 03:13:56` | `cowrie.session.params` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| `2026-11-23 03:13:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f157c94913bf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:14 |
| **Last Seen** | 2026-11-23 03:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b42fae90dc05570fe705556943be50d0_small_control'"'"' '"'"'check_b42fae90dc05570fe705556943be50d0'"'"'', printf '\n%s|%s\n' 'check_b42fae90dc05570fe705556943be50d0_small_control' 'check_b42fae90dc05570fe705556943be50d0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b42fae90dc05570fe705556943be50d0_small_math'"'"' "$((266*94+53))"', (266*94+53, printf '\n%s|%s\n' 'check_b42fae90dc05570fe705556943be50d0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:14:24` | `cowrie.session.connect` |
| `2026-11-23 03:14:24` | `cowrie.client.version` |
| `2026-11-23 03:14:24` | `cowrie.client.kex` |
| `2026-11-23 03:14:29` | `cowrie.login.success` |
| `2026-11-23 03:14:31` | `cowrie.client.size` |
| `2026-11-23 03:14:32` | `cowrie.session.params` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| `2026-11-23 03:14:32` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283a8a9c9da3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:15 |
| **Last Seen** | 2026-11-23 03:16 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1494a211eff0a989e035a78ca95aa63_small_control'"'"' '"'"'check_e1494a211eff0a989e035a78ca95aa63'"'"'', printf '\n%s|%s\n' 'check_e1494a211eff0a989e035a78ca95aa63_small_control' 'check_e1494a211eff0a989e035a78ca95aa63', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e1494a211eff0a989e035a78ca95aa63_small_math'"'"' "$((845*149+56))"', (845*149+56, printf '\n%s|%s\n' 'check_e1494a211eff0a989e035a78ca95aa63_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:15:57` | `cowrie.session.connect` |
| `2026-11-23 03:15:58` | `cowrie.client.version` |
| `2026-11-23 03:15:58` | `cowrie.client.kex` |
| `2026-11-23 03:16:03` | `cowrie.login.success` |
| `2026-11-23 03:16:06` | `cowrie.client.size` |
| `2026-11-23 03:16:07` | `cowrie.session.params` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| `2026-11-23 03:16:08` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d275801ca4bd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:16 |
| **Last Seen** | 2026-11-23 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6207c65c4712854cdacda356b2511690_small_control'"'"' '"'"'check_6207c65c4712854cdacda356b2511690'"'"'', printf '\n%s|%s\n' 'check_6207c65c4712854cdacda356b2511690_small_control' 'check_6207c65c4712854cdacda356b2511690', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6207c65c4712854cdacda356b2511690_small_math'"'"' "$((171*240+70))"', (171*240+70, printf '\n%s|%s\n' 'check_6207c65c4712854cdacda356b2511690_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:16:36` | `cowrie.session.connect` |
| `2026-11-23 03:16:36` | `cowrie.client.version` |
| `2026-11-23 03:16:36` | `cowrie.client.kex` |
| `2026-11-23 03:16:38` | `cowrie.login.success` |
| `2026-11-23 03:16:40` | `cowrie.client.size` |
| `2026-11-23 03:16:41` | `cowrie.session.params` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| `2026-11-23 03:16:42` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbae9ef674db

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-23 03:18 |
| **Last Seen** | 2026-11-23 03:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:18:04` | `cowrie.session.connect` |
| `2026-11-23 03:18:04` | `cowrie.client.version` |
| `2026-11-23 03:18:04` | `cowrie.client.kex` |
| `2026-11-23 03:18:05` | `cowrie.login.success` |
| `2026-11-23 03:18:05` | `cowrie.direct-tcpip.request` |
| `2026-11-23 03:18:05` | `cowrie.direct-tcpip.data` |
| `2026-11-23 03:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d945aefaf9f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:18 |
| **Last Seen** | 2026-11-23 03:18 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_18e2c911b9c9e1ce7f1e0ae34980c5b0_small_control'"'"' '"'"'check_18e2c911b9c9e1ce7f1e0ae34980c5b0'"'"'', printf '\n%s|%s\n' 'check_18e2c911b9c9e1ce7f1e0ae34980c5b0_small_control' 'check_18e2c911b9c9e1ce7f1e0ae34980c5b0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_18e2c911b9c9e1ce7f1e0ae34980c5b0_small_math'"'"' "$((389*933+66))"', (389*933+66, printf '\n%s|%s\n' 'check_18e2c911b9c9e1ce7f1e0ae34980c5b0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:18:10` | `cowrie.session.connect` |
| `2026-11-23 03:18:11` | `cowrie.client.version` |
| `2026-11-23 03:18:11` | `cowrie.client.kex` |
| `2026-11-23 03:18:15` | `cowrie.login.success` |
| `2026-11-23 03:18:18` | `cowrie.client.size` |
| `2026-11-23 03:18:19` | `cowrie.session.params` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| `2026-11-23 03:18:20` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e9cf535285

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-23 03:18 |
| **Last Seen** | 2026-11-23 03:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee_small_control'"'"' '"'"'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee'"'"'', printf '\n%s|%s\n' 'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee_small_control' 'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee_small_math'"'"' "$((440*672+47))"', (440*672+47, printf '\n%s|%s\n' 'check_1cfa53eac2dfc1f7bd7a2c3d0b0a4bee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:18:42` | `cowrie.session.connect` |
| `2026-11-23 03:18:42` | `cowrie.client.version` |
| `2026-11-23 03:18:42` | `cowrie.client.kex` |
| `2026-11-23 03:18:45` | `cowrie.login.success` |
| `2026-11-23 03:18:48` | `cowrie.client.size` |
| `2026-11-23 03:18:48` | `cowrie.session.params` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| `2026-11-23 03:18:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1459148f02c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]75` |
| **First Seen** | 2026-11-23 03:20 |
| **Last Seen** | 2026-11-23 03:20 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5c32d0ce0d50a2d73895fc237a69dae9_small_control'"'"' '"'"'check_5c32d0ce0d50a2d73895fc237a69dae9'"'"'', printf '\n%s|%s\n' 'check_5c32d0ce0d50a2d73895fc237a69dae9_small_control' 'check_5c32d0ce0d50a2d73895fc237a69dae9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5c32d0ce0d50a2d73895fc237a69dae9_small_math'"'"' "$((672*932+32))"', (672*932+32, printf '\n%s|%s\n' 'check_5c32d0ce0d50a2d73895fc237a69dae9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-23 03:20:18` | `cowrie.session.connect` |
| `2026-11-23 03:20:19` | `cowrie.client.version` |
| `2026-11-23 03:20:19` | `cowrie.client.kex` |
| `2026-11-23 03:20:24` | `cowrie.login.success` |
| `2026-11-23 03:20:27` | `cowrie.client.size` |
| `2026-11-23 03:20:28` | `cowrie.session.params` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:29` | `cowrie.command.input` |
| `2026-11-23 03:20:30` | `cowrie.command.input` |
| `2026-11-23 03:20:30` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]75` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (1095) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-58df32438f4a | HIGH | `92.118.39[.]75` | 2026-11-23 03:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fe76b98679f7 | HIGH | `193.32.162[.]84` | 2026-11-23 03:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3389efe21408 | HIGH | `92.118.39[.]75` | 2026-11-23 03:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-eebd19a11b23 | HIGH | `193.32.162[.]84` | 2026-11-23 03:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dd4714e7987b | HIGH | `92.118.39[.]75` | 2026-11-23 03:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-560022d147af | HIGH | `193.32.162[.]84` | 2026-11-23 03:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-58d71b4e6b3e | HIGH | `92.118.39[.]75` | 2026-11-23 03:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-774f72e0edb6 | HIGH | `193.32.162[.]84` | 2026-11-23 03:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-226dda3e2f24 | HIGH | `92.118.39[.]75` | 2026-11-23 03:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-92d175da7864 | HIGH | `193.32.162[.]84` | 2026-11-23 03:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1c960a8f81c3 | HIGH | `92.118.39[.]75` | 2026-11-23 03:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c6feb7f63003 | HIGH | `193.32.162[.]84` | 2026-11-23 03:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8b9fe64aa7dc | HIGH | `92.118.39[.]75` | 2026-11-23 03:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c841d6286577 | HIGH | `193.32.162[.]84` | 2026-11-23 03:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e77c3f7a1d38 | HIGH | `193.32.162[.]84` | 2026-11-23 03:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ee959f3b5973 | HIGH | `193.32.162[.]84` | 2026-11-23 03:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-07456d49ff22 | HIGH | `92.118.39[.]75` | 2026-11-23 03:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-52cc87932055 | HIGH | `193.32.162[.]84` | 2026-11-23 03:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bd66d1986447 | HIGH | `92.118.39[.]75` | 2026-11-23 03:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a12148cf4fe0 | HIGH | `193.32.162[.]84` | 2026-11-23 03:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-24f3f093ce83 | HIGH | `92.118.39[.]75` | 2026-11-23 03:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d10fcddd060b | HIGH | `193.32.162[.]84` | 2026-11-23 03:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7df5b7fe5d94 | HIGH | `92.118.39[.]75` | 2026-11-23 03:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6fe7e0313225 | HIGH | `193.32.162[.]84` | 2026-11-23 03:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e38e38d4dfb6 | HIGH | `92.118.39[.]75` | 2026-11-23 03:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f3b6825868ee | HIGH | `92.118.39[.]75` | 2026-11-23 03:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-075e85b3a58d | HIGH | `77.239.124[.]252` | 2026-11-23 04:22 | Y | 0 | 0 | `T1078` |
| IR-d56d47ff18e4 | HIGH | `185.42.212[.]207` | 2026-11-23 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9de6c4457edf | HIGH | `185.42.212[.]207` | 2026-11-23 04:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1e1eab7b48b1 | HIGH | `217.60.240[.]6` | 2026-11-23 04:36 | Y | 4 | 0 | `T1078` |
| IR-f66c9381c028 | HIGH | `217.60.240[.]247` | 2026-11-23 04:36 | Y | 4 | 0 | `T1078` |
| IR-816c806da52b | HIGH | `172.104.11[.]46` | 2026-11-23 04:41 | Y | 3 | 0 | `T1078` |
| IR-47d987b84ec6 | HIGH | `103.235.74[.]131` | 2026-11-23 04:46 | Y | 1 | 0 | `T1078 · T1592` |
| IR-edea66d8cc79 | HIGH | `138.226.239[.]233` | 2026-11-23 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad450b26b90c | HIGH | `138.124.124[.]210` | 2026-11-23 04:57 | Y | 0 | 0 | `T1078` |
| IR-a93d31d60860 | HIGH | `138.124.116[.]194` | 2026-11-23 04:59 | Y | 0 | 0 | `T1078` |
| IR-97862ead089b | HIGH | `78.128.112[.]74` | 2026-11-23 05:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d7601e2dafac | HIGH | `176.53.159[.]196` | 2026-11-23 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-353dca366c90 | HIGH | `176.53.159[.]196` | 2026-11-23 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84c09075e3e7 | HIGH | `77.239.124[.]252` | 2026-11-23 06:05 | Y | 0 | 0 | `T1078` |
| IR-3cd10f963f10 | HIGH | `109.63.182[.]58` | 2026-11-23 06:23 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-5d67d3f86363 | HIGH | `50.116.49[.]221` | 2026-11-23 06:49 | Y | 3 | 0 | `T1078` |
| IR-bd5885679e00 | HIGH | `138.226.239[.]233` | 2026-11-23 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-162ee0daf7d1 | HIGH | `138.226.239[.]234` | 2026-11-23 07:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd5c683f14ab | HIGH | `104.244.79[.]113` | 2026-11-23 07:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-647cef208c57 | HIGH | `174.161.29[.]214` | 2026-11-23 07:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de00c8878de9 | HIGH | `211.230.3[.]71` | 2026-11-23 07:45 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-e06af0a18e63 | HIGH | `193.32.162[.]84` | 2026-11-23 07:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3db42b41f93d | HIGH | `193.32.162[.]84` | 2026-11-23 07:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c3764a0aebec | HIGH | `193.32.162[.]84` | 2026-11-23 07:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-648b64025d96 | HIGH | `193.32.162[.]84` | 2026-11-23 07:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-40f09a12236c | HIGH | `193.32.162[.]84` | 2026-11-23 07:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-46dd77c82001 | HIGH | `193.32.162[.]84` | 2026-11-23 08:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2982060cb813 | HIGH | `193.32.162[.]84` | 2026-11-23 08:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-30f9bb6cabfb | HIGH | `193.32.162[.]84` | 2026-11-23 08:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-828d3ef88b40 | HIGH | `193.32.162[.]84` | 2026-11-23 08:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb37d9e0c5cd | HIGH | `193.32.162[.]84` | 2026-11-23 08:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5cbcd4112c6b | HIGH | `193.32.162[.]84` | 2026-11-23 08:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c3a1feb991eb | HIGH | `193.32.162[.]84` | 2026-11-23 08:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b245071bf132 | HIGH | `193.32.162[.]84` | 2026-11-23 08:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a2cb3e1d3d28 | HIGH | `193.32.162[.]84` | 2026-11-23 08:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-819d054f1c68 | HIGH | `193.32.162[.]84` | 2026-11-23 08:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bf60e667ddb0 | HIGH | `193.32.162[.]84` | 2026-11-23 08:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-adfbe5ed0249 | HIGH | `193.32.162[.]84` | 2026-11-23 08:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dd77be9ba2d6 | HIGH | `193.32.162[.]84` | 2026-11-23 08:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9a4598fd0cff | HIGH | `193.32.162[.]84` | 2026-11-23 08:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-96de10a8d473 | HIGH | `193.32.162[.]84` | 2026-11-23 08:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f6970367e3ff | HIGH | `193.32.162[.]84` | 2026-11-23 08:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b0d5141373c | HIGH | `77.239.124[.]252` | 2026-11-23 08:42 | Y | 0 | 0 | `T1078` |
| IR-97e4cbf4c6e0 | HIGH | `176.53.159[.]196` | 2026-11-23 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a87e38b2e52a | HIGH | `138.226.239[.]233` | 2026-11-23 09:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8f55fb2346e | HIGH | `78.128.112[.]74` | 2026-11-23 09:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5ed837c322fc | HIGH | `200.63.168[.]90` | 2026-11-23 09:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f74489960e25 | HIGH | `200.63.168[.]90` | 2026-11-23 09:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a99ed83600bf | HIGH | `2.57.122[.]150` | 2026-11-23 09:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6b0ae6a2c256 | HIGH | `2.57.122[.]150` | 2026-11-23 09:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b290cfda0872 | HIGH | `2.57.122[.]150` | 2026-11-23 10:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bd1694316346 | HIGH | `2.57.122[.]150` | 2026-11-23 10:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e384b7ef40f1 | HIGH | `2.57.122[.]150` | 2026-11-23 10:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7edd00a8a0b7 | HIGH | `2.57.122[.]150` | 2026-11-23 10:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e8b2599426a4 | HIGH | `117.50.70[.]125` | 2026-11-23 10:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b68d94db7a06 | HIGH | `117.50.70[.]125` | 2026-11-23 10:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-94c86790e2e1 | HIGH | `119.96.173[.]169` | 2026-11-23 10:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-040d584f94e6 | HIGH | `119.96.173[.]169` | 2026-11-23 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55f50ae822f3 | HIGH | `2.57.122[.]150` | 2026-11-23 10:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b1f3108d69bd | HIGH | `49.75.185[.]71` | 2026-11-23 10:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c21598363ba5 | HIGH | `49.75.185[.]71` | 2026-11-23 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d01109a5f0c | HIGH | `170.245.120[.]109` | 2026-11-23 10:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0654694b826f | HIGH | `170.245.120[.]109` | 2026-11-23 10:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b14e6859f39a | HIGH | `2.57.122[.]150` | 2026-11-23 10:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5649455d00c5 | HIGH | `2.57.122[.]150` | 2026-11-23 10:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3fab64423e6a | HIGH | `2.57.122[.]150` | 2026-11-23 10:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-81458ecd7f2c | HIGH | `2.57.122[.]150` | 2026-11-23 10:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cf848a5c6f4a | HIGH | `176.53.159[.]196` | 2026-11-23 10:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f94f0e30196 | HIGH | `2.57.122[.]150` | 2026-11-23 10:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e36aa0158646 | HIGH | `2.57.122[.]150` | 2026-11-23 10:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7df26fff0dd7 | HIGH | `2.57.122[.]150` | 2026-11-23 10:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-538f9cf5a3ee | HIGH | `2.57.122[.]150` | 2026-11-23 10:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-73827f3155c4 | HIGH | `2.57.122[.]150` | 2026-11-23 10:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-df4eed5e6367 | HIGH | `2.57.122[.]150` | 2026-11-23 10:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 995 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `77.239.124[.]252` | **4** | 2026-11-23 08:42 | 2026-11-23 14:11 | 0m | 4 | `T1110.001` | 🟢 LOW |
| `1.171.25[.]108` | **3** | 2026-11-23 11:45 | 2026-11-23 14:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **3** | 2026-11-23 03:17 | 2026-11-23 06:16 | 3m | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | **3** | 2026-11-23 18:44 | 2026-11-23 22:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-23 03:04 | 2026-11-23 06:05 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `8.243.73[.]199` | **3** | 2026-11-23 19:01 | 2026-11-23 22:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]144` | **2** | 2026-11-23 15:12 | 2026-11-23 16:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.84.166[.]194` | **2** | 2026-11-23 03:01 | 2026-11-23 04:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | **2** | 2026-11-23 21:31 | 2026-11-23 22:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `187.115.144[.]103` | **2** | 2026-11-23 17:12 | 2026-11-23 18:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-11-23 07:44 | 2026-11-23 08:04 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-11-23 09:53 | 2026-11-23 10:07 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.255.211[.]238` | **2** | 2026-11-23 16:59 | 2026-11-23 18:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `63.42.190[.]239` | **2** | 2026-11-23 17:18 | 2026-11-23 19:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | **2** | 2026-11-23 20:22 | 2026-11-23 22:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-23 11:26 | 2026-11-23 12:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-23 15:22 | 2026-11-23 16:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-23 16:17 | 2026-11-23 18:05 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-23 20:28 | 2026-11-23 22:21 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `1.171.25[.]108` | 1 | 2026-11-23 17:16 | 2026-11-23 17:16 | 28s | 0 | `T1592` | 🟢 LOW |
| `1.54.235[.]25` | 1 | 2026-11-23 22:48 | 2026-11-23 22:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.220.45[.]186` | 1 | 2026-11-23 20:46 | 2026-11-23 20:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `103.159.167[.]129` | 1 | 2026-11-23 18:27 | 2026-11-23 18:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-23 22:38 | 2026-11-23 22:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.235.74[.]131` | 1 | 2026-11-23 04:46 | 2026-11-23 04:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-11-23 20:26 | 2026-11-23 20:28 | 117s | 0 | `T1592` | 🟢 LOW |
| `103.68.22[.]115` | 1 | 2026-11-23 16:41 | 2026-11-23 16:41 | 7s | 0 | `T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-11-23 16:35 | 2026-11-23 16:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.0.166[.]123` | 1 | 2026-11-23 16:58 | 2026-11-23 16:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-23 17:37 | 2026-11-23 17:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.70.13[.]54` | 1 | 2026-11-23 21:37 | 2026-11-23 21:38 | 16s | 0 | `T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-11-23 18:30 | 2026-11-23 18:31 | 43s | 0 | `T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-11-23 20:59 | 2026-11-23 21:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.255.146[.]141` | 1 | 2026-11-23 18:43 | 2026-11-23 18:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.53.130[.]4` | 1 | 2026-11-23 18:41 | 2026-11-23 18:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-11-23 22:22 | 2026-11-23 22:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `117.26.73[.]12` | 1 | 2026-11-23 12:37 | 2026-11-23 12:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.113.15[.]18` | 1 | 2026-11-23 22:26 | 2026-11-23 22:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.43[.]158` | 1 | 2026-11-23 05:58 | 2026-11-23 05:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.26.37[.]105` | 1 | 2026-11-23 17:41 | 2026-11-23 17:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.40.157[.]149` | 1 | 2026-11-23 21:32 | 2026-11-23 21:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.209.67[.]122` | 1 | 2026-11-23 17:57 | 2026-11-23 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.163.134[.]183` | 1 | 2026-11-23 09:42 | 2026-11-23 09:42 | 20s | 0 | `T1592` | 🟢 LOW |
| `121.46.71[.]52` | 1 | 2026-11-23 08:41 | 2026-11-23 08:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.170.98[.]139` | 1 | 2026-11-23 17:14 | 2026-11-23 17:14 | 1s | 0 | `T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-11-23 21:31 | 2026-11-23 21:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.163.52[.]74` | 1 | 2026-11-23 22:30 | 2026-11-23 22:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.239.129[.]2` | 1 | 2026-11-23 17:00 | 2026-11-23 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.20.207[.]154` | 1 | 2026-11-23 17:19 | 2026-11-23 17:19 | 9s | 0 | `T1592` | 🟢 LOW |
| `125.72.150[.]250` | 1 | 2026-11-23 21:53 | 2026-11-23 21:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.86.25[.]198` | 1 | 2026-11-23 22:22 | 2026-11-23 22:22 | 11s | 0 | `T1592` | 🟢 LOW |
| `134.209.218[.]180` | 1 | 2026-11-23 05:17 | 2026-11-23 05:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `136.158.34[.]146` | 1 | 2026-11-23 21:48 | 2026-11-23 21:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-23 11:47 | 2026-11-23 11:48 | 36s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-23 19:45 | 2026-11-23 19:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.43.215[.]175` | 1 | 2026-11-23 22:36 | 2026-11-23 22:37 | 31s | 0 | `T1592` | 🟢 LOW |
| `143.203.219[.]50` | 1 | 2026-11-23 19:53 | 2026-11-23 19:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `156.54.179[.]52` | 1 | 2026-11-23 13:45 | 2026-11-23 13:45 | 11s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-23 19:27 | 2026-11-23 19:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-23 03:57 | 2026-11-23 03:57 | 7s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-23 19:06 | 2026-11-23 19:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `171.11.199[.]148` | 1 | 2026-11-23 11:30 | 2026-11-23 11:32 | 82s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]46` | 1 | 2026-11-23 04:41 | 2026-11-23 04:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | 1 | 2026-11-23 19:09 | 2026-11-23 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.61.115[.]27` | 1 | 2026-11-23 20:23 | 2026-11-23 20:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-11-23 18:39 | 2026-11-23 18:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]227` | 1 | 2026-11-23 06:56 | 2026-11-23 06:56 | 24s | 0 | `T1592` | 🟢 LOW |
| `175.206.251[.]46` | 1 | 2026-11-23 08:07 | 2026-11-23 08:07 | 15s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-11-23 19:18 | 2026-11-23 19:18 | 33s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]135` | 1 | 2026-11-23 17:18 | 2026-11-23 17:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-23 04:36 | 2026-11-23 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.92.204[.]91` | 1 | 2026-11-23 15:17 | 2026-11-23 15:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.167.234[.]154` | 1 | 2026-11-23 22:33 | 2026-11-23 22:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-11-23 22:44 | 2026-11-23 22:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.237.142[.]82` | 1 | 2026-11-23 21:18 | 2026-11-23 21:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]254` | 1 | 2026-11-23 07:00 | 2026-11-23 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-11-23 20:38 | 2026-11-23 20:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-11-23 03:55 | 2026-11-23 03:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `185.42.212[.]207` | 1 | 2026-11-23 03:58 | 2026-11-23 03:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.18.162[.]14` | 1 | 2026-11-23 08:37 | 2026-11-23 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.239.41[.]74` | 1 | 2026-11-23 17:00 | 2026-11-23 17:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `188.151.78[.]34` | 1 | 2026-11-23 12:57 | 2026-11-23 12:58 | 23s | 0 | `T1592` | 🟢 LOW |
| `188.59.41[.]146` | 1 | 2026-11-23 18:24 | 2026-11-23 18:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.166.133[.]40` | 1 | 2026-11-23 12:24 | 2026-11-23 12:24 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.246.147[.]152` | 1 | 2026-11-23 08:55 | 2026-11-23 08:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-23 03:20 | 2026-11-23 03:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `194.154.92[.]163` | 1 | 2026-11-23 18:04 | 2026-11-23 18:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.160.206[.]226` | 1 | 2026-11-23 17:31 | 2026-11-23 17:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-23 16:38 | 2026-11-23 16:39 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]71` | 1 | 2026-11-23 12:44 | 2026-11-23 12:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `196.191.142[.]67` | 1 | 2026-11-23 17:35 | 2026-11-23 17:35 | 18s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-11-23 21:09 | 2026-11-23 21:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `198.179.70[.]19` | 1 | 2026-11-23 18:37 | 2026-11-23 18:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `2.179.187[.]110` | 1 | 2026-11-23 19:13 | 2026-11-23 19:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-11-23 18:07 | 2026-11-23 18:08 | 27s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-11-23 22:39 | 2026-11-23 22:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `20.65.178[.]120` | 1 | 2026-11-23 07:34 | 2026-11-23 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.84.40[.]178` | 1 | 2026-11-23 22:27 | 2026-11-23 22:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.153.86[.]250` | 1 | 2026-11-23 20:07 | 2026-11-23 20:07 | 21s | 0 | `T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-11-23 16:57 | 2026-11-23 16:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `203.172.213[.]166` | 1 | 2026-11-23 22:32 | 2026-11-23 22:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `203.193.137[.]250` | 1 | 2026-11-23 17:14 | 2026-11-23 17:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `211.185.14[.]39` | 1 | 2026-11-23 19:14 | 2026-11-23 19:15 | 23s | 0 | `T1592` | 🟢 LOW |
| `211.194.41[.]69` | 1 | 2026-11-23 15:28 | 2026-11-23 15:28 | 17s | 0 | `T1592` | 🟢 LOW |
| `211.230.3[.]71` | 1 | 2026-11-23 07:44 | 2026-11-23 07:44 | 14s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]91` | 1 | 2026-11-23 05:07 | 2026-11-23 05:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]91` | 1 | 2026-11-23 16:46 | 2026-11-23 16:46 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]98` | 1 | 2026-11-23 03:19 | 2026-11-23 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.59.165[.]109` | 1 | 2026-11-23 21:32 | 2026-11-23 21:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `216.238.123[.]63` | 1 | 2026-11-23 05:31 | 2026-11-23 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.22.0[.]200` | 1 | 2026-11-23 17:13 | 2026-11-23 17:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.4.214[.]115` | 1 | 2026-11-23 22:28 | 2026-11-23 22:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `220.94.124[.]233` | 1 | 2026-11-23 21:24 | 2026-11-23 21:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.120.77[.]34` | 1 | 2026-11-23 21:16 | 2026-11-23 21:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.199.172[.]66` | 1 | 2026-11-23 18:27 | 2026-11-23 18:28 | 19s | 0 | `T1592` | 🟢 LOW |
| `222.111.148[.]139` | 1 | 2026-11-23 19:14 | 2026-11-23 19:14 | 5s | 0 | `T1592` | 🟢 LOW |
| `222.120.176[.]6` | 1 | 2026-11-23 17:26 | 2026-11-23 17:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.92.61[.]242` | 1 | 2026-11-23 16:15 | 2026-11-23 16:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `222.92.61[.]242` | 1 | 2026-11-23 20:26 | 2026-11-23 20:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.98.44[.]218` | 1 | 2026-11-23 20:51 | 2026-11-23 20:51 | 9s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-23 11:15 | 2026-11-23 11:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `27.115.113[.]138` | 1 | 2026-11-23 22:42 | 2026-11-23 22:42 | 24s | 0 | `T1592` | 🟢 LOW |
| `27.188.184[.]13` | 1 | 2026-11-23 19:18 | 2026-11-23 19:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.192.21[.]87` | 1 | 2026-11-23 15:41 | 2026-11-23 15:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `27.24.141[.]161` | 1 | 2026-11-23 17:49 | 2026-11-23 17:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-23 06:34 | 2026-11-23 06:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.173.2[.]182` | 1 | 2026-11-23 16:54 | 2026-11-23 16:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.173.66[.]222` | 1 | 2026-11-23 16:53 | 2026-11-23 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.173.67[.]115` | 1 | 2026-11-23 21:26 | 2026-11-23 21:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.3.84[.]41` | 1 | 2026-11-23 14:16 | 2026-11-23 14:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.3.87[.]227` | 1 | 2026-11-23 14:16 | 2026-11-23 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.3.90[.]202` | 1 | 2026-11-23 13:42 | 2026-11-23 13:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.145[.]207` | 1 | 2026-11-23 11:47 | 2026-11-23 11:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.214.151[.]154` | 1 | 2026-11-23 13:56 | 2026-11-23 13:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.242[.]121` | 1 | 2026-11-23 14:24 | 2026-11-23 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.153.164[.]122` | 1 | 2026-11-23 22:13 | 2026-11-23 22:14 | 53s | 0 | `T1592` | 🟢 LOW |
| `36.93.154[.]207` | 1 | 2026-11-23 17:44 | 2026-11-23 17:44 | 3s | 0 | `T1592` | 🟢 LOW |
| `40.67.177[.]106` | 1 | 2026-11-23 11:55 | 2026-11-23 11:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `43.103.47[.]73` | 1 | 2026-11-23 12:17 | 2026-11-23 12:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-23 09:37 | 2026-11-23 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-23 18:51 | 2026-11-23 18:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.10.56[.]170` | 1 | 2026-11-23 21:41 | 2026-11-23 21:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.139.177[.]11` | 1 | 2026-11-23 20:45 | 2026-11-23 20:45 | 22s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-23 17:34 | 2026-11-23 17:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.52.232[.]89` | 1 | 2026-11-23 18:12 | 2026-11-23 18:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]192` | 1 | 2026-11-23 16:44 | 2026-11-23 16:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]248` | 1 | 2026-11-23 21:22 | 2026-11-23 21:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]14` | 1 | 2026-11-23 20:45 | 2026-11-23 20:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.239.240[.]2` | 1 | 2026-11-23 17:20 | 2026-11-23 17:20 | 7s | 0 | `T1592` | 🟢 LOW |
| `50.116.49[.]221` | 1 | 2026-11-23 06:49 | 2026-11-23 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.99.187[.]8` | 1 | 2026-11-23 08:25 | 2026-11-23 08:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.247.18[.]34` | 1 | 2026-11-23 20:46 | 2026-11-23 20:46 | 4s | 0 | `T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-11-23 21:07 | 2026-11-23 21:07 | 9s | 0 | `T1592` | 🟢 LOW |
| `60.166.8[.]174` | 1 | 2026-11-23 16:38 | 2026-11-23 16:39 | 40s | 0 | `T1592` | 🟢 LOW |
| `61.133.160[.]28` | 1 | 2026-11-23 19:21 | 2026-11-23 19:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-11-23 16:32 | 2026-11-23 16:33 | 57s | 0 | `T1592` | 🟢 LOW |
| `61.218.153[.]56` | 1 | 2026-11-23 16:01 | 2026-11-23 16:01 | 24s | 0 | `T1592` | 🟢 LOW |
| `62.183.54[.]253` | 1 | 2026-11-23 16:17 | 2026-11-23 16:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.183.54[.]253` | 1 | 2026-11-23 20:26 | 2026-11-23 20:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-23 19:14 | 2026-11-23 19:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-23 07:05 | 2026-11-23 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-23 10:13 | 2026-11-23 10:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-23 16:10 | 2026-11-23 16:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-11-23 08:17 | 2026-11-23 08:17 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-23 03:02 | 2026-11-23 03:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-11-23 12:11 | 2026-11-23 12:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]105` | 1 | 2026-11-23 18:21 | 2026-11-23 18:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]24` | 1 | 2026-11-23 21:49 | 2026-11-23 21:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]66` | 1 | 2026-11-23 14:11 | 2026-11-23 14:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]46` | 1 | 2026-11-23 13:30 | 2026-11-23 13:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]161` | 1 | 2026-11-23 21:49 | 2026-11-23 21:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]196` | 1 | 2026-11-23 21:50 | 2026-11-23 21:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]202` | 1 | 2026-11-23 09:32 | 2026-11-23 09:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]32` | 1 | 2026-11-23 18:33 | 2026-11-23 18:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]74` | 1 | 2026-11-23 14:31 | 2026-11-23 14:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]85` | 1 | 2026-11-23 09:31 | 2026-11-23 09:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]94` | 1 | 2026-11-23 09:33 | 2026-11-23 09:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-11-23 11:30 | 2026-11-23 11:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-11-23 09:35 | 2026-11-23 09:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `68.8.214[.]30` | 1 | 2026-11-23 21:05 | 2026-11-23 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.127.19[.]244` | 1 | 2026-11-23 13:10 | 2026-11-23 13:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.235.27[.]139` | 1 | 2026-11-23 19:13 | 2026-11-23 19:13 | 6s | 0 | `T1592` | 🟢 LOW |
| `71.6.154[.]144` | 1 | 2026-11-23 07:22 | 2026-11-23 07:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-11-23 18:39 | 2026-11-23 18:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]22` | 1 | 2026-11-23 13:14 | 2026-11-23 13:14 | 7s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-11-23 06:59 | 2026-11-23 06:59 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-23 05:48 | 2026-11-23 05:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-23 09:18 | 2026-11-23 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-23 04:37 | 2026-11-23 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-23 07:07 | 2026-11-23 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-23 18:44 | 2026-11-23 18:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-23 22:47 | 2026-11-23 22:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.38.254[.]255` | 1 | 2026-11-23 08:57 | 2026-11-23 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 05:10 | 2026-11-23 05:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 09:30 | 2026-11-23 09:30 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 13:51 | 2026-11-23 13:51 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 18:10 | 2026-11-23 18:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-23 22:31 | 2026-11-23 22:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.189.111[.]176` | 1 | 2026-11-23 09:55 | 2026-11-23 09:55 | 16s | 0 | `T1592` | 🟢 LOW |
| `79.124.56[.]242` | 1 | 2026-11-23 04:05 | 2026-11-23 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.124.56[.]242` | 1 | 2026-11-23 14:49 | 2026-11-23 14:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.148.247[.]39` | 1 | 2026-11-23 18:39 | 2026-11-23 18:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `81.9.29[.]40` | 1 | 2026-11-23 06:21 | 2026-11-23 06:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `83.149.29[.]222` | 1 | 2026-11-23 19:13 | 2026-11-23 19:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.72[.]64` | 1 | 2026-11-23 19:14 | 2026-11-23 19:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]24` | 1 | 2026-11-23 13:31 | 2026-11-23 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]28` | 1 | 2026-11-23 09:34 | 2026-11-23 09:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]36` | 1 | 2026-11-23 22:44 | 2026-11-23 22:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]53` | 1 | 2026-11-23 04:28 | 2026-11-23 04:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]53` | 1 | 2026-11-23 17:40 | 2026-11-23 17:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.104.244[.]228` | 1 | 2026-11-23 18:41 | 2026-11-23 18:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `86.18.41[.]255` | 1 | 2026-11-23 11:54 | 2026-11-23 11:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]121` | 1 | 2026-11-23 13:18 | 2026-11-23 13:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-11-23 18:39 | 2026-11-23 18:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.208.118[.]252` | 1 | 2026-11-23 18:39 | 2026-11-23 18:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.15.42[.]30` | 1 | 2026-11-23 06:52 | 2026-11-23 06:52 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-11-23 04:26 | 2026-11-23 04:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-23 03:03 | 2026-11-23 03:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-23 12:41 | 2026-11-23 12:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]78` | 1 | 2026-11-23 21:45 | 2026-11-23 21:45 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]125` | 1 | 2026-11-23 21:19 | 2026-11-23 21:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.199.23[.]52` | 1 | 2026-11-23 03:41 | 2026-11-23 03:41 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `79.124.56[.]242` | BG | Tamatiya EOOD | **100** ⚠️ | 33 |
| `116.48.143[.]166` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `46.151.178[.]14` | NL | SINO WORLDWIDE TRADING LIMITED | **100** ⚠️ | 50 |
| `112.30.127[.]9` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `178.216.165[.]187` | RU | Morton-Telekom Ltd | **100** ⚠️ | 50 |
| `103.29.185[.]162` | ID | PT Pascal Indonesia | **100** ⚠️ | 50 |
| `62.183.82[.]70` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `210.0.90[.]82` | AU | AAPT Limited | **100** ⚠️ | 50 |
| `109.173.38[.]135` | RU | PJSC Rostelecom | **100** ⚠️ | 32 |
| `155.212.17[.]174` | RU | PI LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 1176 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1143 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 196 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |

---

## 🔕 False Positive Summary (109 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 7 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 10 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 43 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1477 cases |
| Tool 34  | Credential Extractor        | ✅ 3521 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 35 fingerprints |
| Tool 36  | Command Clustering          | ✅ 208 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 951 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 109 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 324 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1120 priority case(s) shown individually · 222 recon entry/entries in table (19 group(s) consolidating 45 session(s)).

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
_Report time: 2026-11-23T23:03:43Z_

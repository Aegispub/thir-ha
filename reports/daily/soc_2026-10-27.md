# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-27 |
| **Generated At** | 2026-10-27T02:48:46Z |
| **Shift Time** | 02:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **36** |
| Confirmed Threats | **27** |
| False Positives Filtered | **9** (25.0%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **17** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1924** |
| Unique Credential Pairs | **1848** |
| Unique Usernames | **233** |
| Unique Passwords | **1690** |
| Successful Auth Pairs | **1923** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1548 |
| `ubuntu` | 22 |
| `deploy` | 11 |
| `admin` | 10 |
| `user` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 37 |
| `123` | 22 |
| `1234` | 13 |
| `root` | 10 |
| `12345678` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 5 |
| `support` | `support` | 3 |
| `root` | `1q2w3e` | 3 |
| `root` | `1qaz!QAZ` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `12345678` | `77.239.124.158` | 2026-10-27T00:00:00 |
| `root` | `chambery` | `10.0.0.73` | 2026-10-27T00:00:01 |
| `root` | `cer` | `10.0.0.73` | 2026-10-27T00:00:03 |
| `root` | `billabong` | `10.0.0.73` | 2026-10-27T00:00:05 |
| `ubuntu` | `.` | `77.239.124.158` | 2026-10-27T00:00:06 |
| `root` | `757575` | `10.0.0.73` | 2026-10-27T00:00:09 |
| `root` | `q1w2e3r4` | `77.239.124.158` | 2026-10-27T00:00:11 |
| `root` | `7539511` | `10.0.0.73` | 2026-10-27T00:00:11 |
| `root` | `4j9r4rnTtP` | `10.0.0.73` | 2026-10-27T00:00:14 |
| `root` | `2512` | `10.0.0.73` | 2026-10-27T00:00:16 |
| `rocky` | `Aa112211` | `77.239.124.158` | 2026-10-27T00:00:17 |
| `root` | `159874` | `10.0.0.73` | 2026-10-27T00:00:19 |
| `root` | `159263` | `10.0.0.73` | 2026-10-27T00:00:21 |
| `webadmin` | `123456` | `77.239.124.158` | 2026-10-27T00:00:23 |
| `root` | `073116838` | `10.0.0.73` | 2026-10-27T00:00:24 |
| `root` | `Admin@12345` | `164.30.17.82` | 2026-10-27T00:00:26 |
| `root` | `zelda` | `10.0.0.73` | 2026-10-27T00:00:27 |
| `root` | `utnubu` | `77.239.124.158` | 2026-10-27T00:00:28 |
| `root` | `youpi` | `10.0.0.73` | 2026-10-27T00:00:30 |
| `root` | `tonnerre` | `10.0.0.73` | 2026-10-27T00:00:32 |
_… 1903 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **36** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 14 |
| Go SSH scanner | 5 |
| OpenSSH | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 11 | 6 |
| `0a07365cc01f...` | Generic scanner | 2 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 11 | 6 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 2 | 2 | — |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 1 | 1 | Modern SSH client |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `113.164.66.10`, `128.1.42.111`, `46.101.100.197`, `79.108.220.136`, `66.116.225.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS26337` | Oso Grande IP Services, LLC | 1 | HIGH |
| `AS134420` | Chongqing Telecom | 1 | HIGH |
| `AS9534` | Binariang Berhad | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5798e8db9456

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]158` |
| **First Seen** | 2026-10-27 00:00 |
| **Last Seen** | 2026-10-27 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:00:00` | `cowrie.session.connect` |
| `2026-10-27 00:00:00` | `cowrie.client.version` |
| `2026-10-27 00:00:00` | `cowrie.client.kex` |
| `2026-10-27 00:00:00` | `cowrie.login.success` |
| `2026-10-27 00:00:01` | `cowrie.session.params` |
| `2026-10-27 00:00:01` | `cowrie.command.input` |
| `2026-10-27 00:00:01` | `cowrie.log.closed` |
| `2026-10-27 00:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]158` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef8e85e26608

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-27 00:00 |
| **Last Seen** | 2026-10-27 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:00:24` | `cowrie.session.connect` |
| `2026-10-27 00:00:25` | `cowrie.client.version` |
| `2026-10-27 00:00:25` | `cowrie.client.kex` |
| `2026-10-27 00:00:26` | `cowrie.login.success` |
| `2026-10-27 00:00:27` | `cowrie.session.params` |
| `2026-10-27 00:00:27` | `cowrie.command.input` |
| `2026-10-27 00:00:27` | `cowrie.log.closed` |
| `2026-10-27 00:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33510f00bb39

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-27 00:12 |
| **Last Seen** | 2026-10-27 00:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:12:58` | `cowrie.session.connect` |
| `2026-10-27 00:12:58` | `cowrie.client.version` |
| `2026-10-27 00:12:58` | `cowrie.client.kex` |
| `2026-10-27 00:12:59` | `cowrie.login.success` |
| `2026-10-27 00:12:59` | `cowrie.direct-tcpip.request` |
| `2026-10-27 00:12:59` | `cowrie.direct-tcpip.data` |
| `2026-10-27 00:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd040e9a4f16

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-27 00:15 |
| **Last Seen** | 2026-10-27 00:15 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:15:29` | `cowrie.session.connect` |
| `2026-10-27 00:15:29` | `cowrie.client.version` |
| `2026-10-27 00:15:30` | `cowrie.client.kex` |
| `2026-10-27 00:15:30` | `cowrie.login.success` |
| `2026-10-27 00:15:34` | `cowrie.direct-tcpip.request` |
| `2026-10-27 00:15:38` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 00:15:38` | `cowrie.direct-tcpip.data` |
| `2026-10-27 00:15:42` | `cowrie.direct-tcpip.request` |
| `2026-10-27 00:15:47` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 00:15:47` | `cowrie.direct-tcpip.data` |
| `2026-10-27 00:15:50` | `cowrie.direct-tcpip.request` |
| `2026-10-27 00:15:51` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 00:15:51` | `cowrie.direct-tcpip.data` |
| `2026-10-27 00:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9716dc0fe1be

| Field | Detail |
|---|---|
| **Source IP** | `113.249.121[.]140` |
| **First Seen** | 2026-10-27 00:49 |
| **Last Seen** | 2026-10-27 00:54 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:49:24` | `cowrie.session.connect` |
| `2026-10-27 00:49:24` | `cowrie.client.version` |
| `2026-10-27 00:49:24` | `cowrie.client.kex` |
| `2026-10-27 00:49:26` | `cowrie.login.success` |
| `2026-10-27 00:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.121[.]140` to AbuseIPDB if not already reported
- [ ] Block `113.249.121[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75bf7703479

| Field | Detail |
|---|---|
| **Source IP** | `79.108.220[.]136` |
| **First Seen** | 2026-10-27 00:51 |
| **Last Seen** | 2026-10-27 00:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:51:16` | `cowrie.session.connect` |
| `2026-10-27 00:51:16` | `cowrie.client.version` |
| `2026-10-27 00:51:16` | `cowrie.client.kex` |
| `2026-10-27 00:51:18` | `cowrie.login.success` |
| `2026-10-27 00:51:19` | `cowrie.session.params` |
| `2026-10-27 00:51:19` | `cowrie.command.input` |
| `2026-10-27 00:51:19` | `cowrie.command.failed` |
| `2026-10-27 00:51:20` | `cowrie.log.closed` |
| `2026-10-27 00:51:20` | `cowrie.session.params` |
| `2026-10-27 00:51:20` | `cowrie.command.input` |
| `2026-10-27 00:51:21` | `cowrie.session.file_download` |
| `2026-10-27 00:51:21` | `cowrie.log.closed` |
| `2026-10-27 00:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.108.220[.]136` to AbuseIPDB if not already reported
- [ ] Block `79.108.220[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc04ccde154

| Field | Detail |
|---|---|
| **Source IP** | `79.108.220[.]136` |
| **First Seen** | 2026-10-27 00:51 |
| **Last Seen** | 2026-10-27 00:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:51:21` | `cowrie.session.connect` |
| `2026-10-27 00:51:21` | `cowrie.client.version` |
| `2026-10-27 00:51:22` | `cowrie.client.kex` |
| `2026-10-27 00:51:23` | `cowrie.login.success` |
| `2026-10-27 00:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.108.220[.]136` to AbuseIPDB if not already reported
- [ ] Block `79.108.220[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5566ed0195

| Field | Detail |
|---|---|
| **Source IP** | `46.101.100[.]197` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:13` | `cowrie.session.connect` |
| `2026-10-27 00:52:13` | `cowrie.client.version` |
| `2026-10-27 00:52:13` | `cowrie.client.kex` |
| `2026-10-27 00:52:14` | `cowrie.login.success` |
| `2026-10-27 00:52:14` | `cowrie.session.params` |
| `2026-10-27 00:52:14` | `cowrie.command.input` |
| `2026-10-27 00:52:14` | `cowrie.command.failed` |
| `2026-10-27 00:52:15` | `cowrie.log.closed` |
| `2026-10-27 00:52:15` | `cowrie.session.params` |
| `2026-10-27 00:52:15` | `cowrie.command.input` |
| `2026-10-27 00:52:15` | `cowrie.session.file_download` |
| `2026-10-27 00:52:15` | `cowrie.log.closed` |
| `2026-10-27 00:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.100[.]197` to AbuseIPDB if not already reported
- [ ] Block `46.101.100[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd96e39913d

| Field | Detail |
|---|---|
| **Source IP** | `128.1.42[.]111` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:15` | `cowrie.session.connect` |
| `2026-10-27 00:52:15` | `cowrie.client.version` |
| `2026-10-27 00:52:15` | `cowrie.client.kex` |
| `2026-10-27 00:52:17` | `cowrie.login.success` |
| `2026-10-27 00:52:18` | `cowrie.session.params` |
| `2026-10-27 00:52:18` | `cowrie.command.input` |
| `2026-10-27 00:52:18` | `cowrie.command.failed` |
| `2026-10-27 00:52:18` | `cowrie.log.closed` |
| `2026-10-27 00:52:19` | `cowrie.session.params` |
| `2026-10-27 00:52:19` | `cowrie.command.input` |
| `2026-10-27 00:52:19` | `cowrie.session.file_download` |
| `2026-10-27 00:52:19` | `cowrie.log.closed` |
| `2026-10-27 00:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.42[.]111` to AbuseIPDB if not already reported
- [ ] Block `128.1.42[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7935f0b38063

| Field | Detail |
|---|---|
| **Source IP** | `46.101.100[.]197` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:15` | `cowrie.session.connect` |
| `2026-10-27 00:52:15` | `cowrie.client.version` |
| `2026-10-27 00:52:16` | `cowrie.client.kex` |
| `2026-10-27 00:52:17` | `cowrie.login.success` |
| `2026-10-27 00:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.100[.]197` to AbuseIPDB if not already reported
- [ ] Block `46.101.100[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10adc4948bb

| Field | Detail |
|---|---|
| **Source IP** | `128.1.42[.]111` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:19` | `cowrie.session.connect` |
| `2026-10-27 00:52:19` | `cowrie.client.version` |
| `2026-10-27 00:52:19` | `cowrie.client.kex` |
| `2026-10-27 00:52:20` | `cowrie.login.success` |
| `2026-10-27 00:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.42[.]111` to AbuseIPDB if not already reported
- [ ] Block `128.1.42[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f209c5f2315

| Field | Detail |
|---|---|
| **Source IP** | `119.96.159[.]237` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:44` | `cowrie.session.connect` |
| `2026-10-27 00:52:44` | `cowrie.client.version` |
| `2026-10-27 00:52:44` | `cowrie.client.kex` |
| `2026-10-27 00:52:46` | `cowrie.login.success` |
| `2026-10-27 00:52:47` | `cowrie.session.params` |
| `2026-10-27 00:52:47` | `cowrie.command.input` |
| `2026-10-27 00:52:47` | `cowrie.command.failed` |
| `2026-10-27 00:52:48` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.159[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.96.159[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bff7610b2fe

| Field | Detail |
|---|---|
| **Source IP** | `119.96.159[.]237` |
| **First Seen** | 2026-10-27 00:52 |
| **Last Seen** | 2026-10-27 00:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:52:56` | `cowrie.session.connect` |
| `2026-10-27 00:52:56` | `cowrie.client.version` |
| `2026-10-27 00:52:56` | `cowrie.client.kex` |
| `2026-10-27 00:52:57` | `cowrie.login.success` |
| `2026-10-27 00:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.159[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.96.159[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53810099282

| Field | Detail |
|---|---|
| **Source IP** | `113.164.66[.]10` |
| **First Seen** | 2026-10-27 00:54 |
| **Last Seen** | 2026-10-27 00:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:54:16` | `cowrie.session.connect` |
| `2026-10-27 00:54:16` | `cowrie.client.version` |
| `2026-10-27 00:54:17` | `cowrie.client.kex` |
| `2026-10-27 00:54:18` | `cowrie.login.success` |
| `2026-10-27 00:54:19` | `cowrie.session.params` |
| `2026-10-27 00:54:19` | `cowrie.command.input` |
| `2026-10-27 00:54:19` | `cowrie.command.failed` |
| `2026-10-27 00:54:20` | `cowrie.log.closed` |
| `2026-10-27 00:54:21` | `cowrie.session.params` |
| `2026-10-27 00:54:21` | `cowrie.command.input` |
| `2026-10-27 00:54:21` | `cowrie.session.file_download` |
| `2026-10-27 00:54:21` | `cowrie.log.closed` |
| `2026-10-27 00:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.164.66[.]10` to AbuseIPDB if not already reported
- [ ] Block `113.164.66[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc7b62d7ddf

| Field | Detail |
|---|---|
| **Source IP** | `113.164.66[.]10` |
| **First Seen** | 2026-10-27 00:54 |
| **Last Seen** | 2026-10-27 00:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:54:22` | `cowrie.session.connect` |
| `2026-10-27 00:54:22` | `cowrie.client.version` |
| `2026-10-27 00:54:22` | `cowrie.client.kex` |
| `2026-10-27 00:54:23` | `cowrie.login.success` |
| `2026-10-27 00:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.164.66[.]10` to AbuseIPDB if not already reported
- [ ] Block `113.164.66[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fa7ee15e50

| Field | Detail |
|---|---|
| **Source IP** | `66.116.225[.]71` |
| **First Seen** | 2026-10-27 00:54 |
| **Last Seen** | 2026-10-27 00:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:54:33` | `cowrie.session.connect` |
| `2026-10-27 00:54:33` | `cowrie.client.version` |
| `2026-10-27 00:54:34` | `cowrie.client.kex` |
| `2026-10-27 00:54:35` | `cowrie.login.success` |
| `2026-10-27 00:54:36` | `cowrie.session.params` |
| `2026-10-27 00:54:36` | `cowrie.command.input` |
| `2026-10-27 00:54:36` | `cowrie.command.failed` |
| `2026-10-27 00:54:37` | `cowrie.log.closed` |
| `2026-10-27 00:54:37` | `cowrie.session.params` |
| `2026-10-27 00:54:37` | `cowrie.command.input` |
| `2026-10-27 00:54:38` | `cowrie.session.file_download` |
| `2026-10-27 00:54:38` | `cowrie.log.closed` |
| `2026-10-27 00:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.225[.]71` to AbuseIPDB if not already reported
- [ ] Block `66.116.225[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752f3ef26568

| Field | Detail |
|---|---|
| **Source IP** | `66.116.225[.]71` |
| **First Seen** | 2026-10-27 00:54 |
| **Last Seen** | 2026-10-27 00:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:54:38` | `cowrie.session.connect` |
| `2026-10-27 00:54:38` | `cowrie.client.version` |
| `2026-10-27 00:54:38` | `cowrie.client.kex` |
| `2026-10-27 00:54:40` | `cowrie.login.success` |
| `2026-10-27 00:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.225[.]71` to AbuseIPDB if not already reported
- [ ] Block `66.116.225[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.45[.]34` | 1 | 2026-10-27 00:50 | 2026-10-27 00:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.58.219[.]98` | 1 | 2026-10-27 00:24 | 2026-10-27 00:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-27 00:07 | 2026-10-27 00:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-27 00:26 | 2026-10-27 00:27 | 35s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-10-27 00:40 | 2026-10-27 00:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-27 00:40 | 2026-10-27 00:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]137` | 1 | 2026-10-27 00:24 | 2026-10-27 00:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.41.184[.]119` | 1 | 2026-10-27 00:42 | 2026-10-27 00:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]158` | 1 | 2026-10-27 00:17 | 2026-10-27 00:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.128.1[.]200` | 1 | 2026-10-27 00:07 | 2026-10-27 00:08 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `119.96.159[.]237` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `143.198.208[.]150` | SG | DigitalOcean, LLC | **100** ⚠️ | 29 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `36.41.184[.]119` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `123.58.219[.]98` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 11 |
| `185.191.236[.]38` | CH | Fidel Ernesto Geronimo Ramirez trading as Global Business Consulting, Geronimo Ramirez | **100** ⚠️ | 50 |
| `170.231.237[.]214` | CH | GRUPO PANAGLOBAL 15 S.A | **100** ⚠️ | 37 |
| `80.94.95[.]118` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `213.230.92[.]137` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 36 cases |
| Tool 34  | Credential Extractor        | ✅ 1924 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (25.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 10 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-27T02:48:46Z_

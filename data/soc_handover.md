# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-31 |
| **Generated At** | 2026-10-31T03:07:53Z |
| **Shift Time** | 03:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **47** |
| False Positives Filtered | **13** (21.7%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **21** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **48** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **12** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `support` | 13 |
| `345gs5662d34` | 5 |
| `bp` | 2 |
| `toni` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 13 |
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `admin` | 3 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 13 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `admin` | `admin` | 2 |
| `root` | `Hc123456` | 1 |
| `root` | `3245gs5662d34` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Hc123456` | `104.208.108.166` | 2026-10-31T00:01:07 |
| `345gs5662d34` | `345gs5662d34` | `104.208.108.166` | 2026-10-31T00:01:11 |
| `root` | `3245gs5662d34` | `104.208.108.166` | 2026-10-31T00:01:12 |
| `root` | `---fuck_you----` | `182.92.131.52` | 2026-10-31T00:12:06 |
| `support` | `support` | `10.0.0.73` | 2026-10-31T00:14:14 |
| `support` | `support` | `176.53.159.196` | 2026-10-31T00:16:35 |
| `root` | `admin` | `80.94.95.118` | 2026-10-31T00:19:25 |
| `firedancer` | `firedancer` | `179.43.153.10` | 2026-10-31T01:12:55 |
| `lighthouse` | `lighthouse` | `179.43.153.10` | 2026-10-31T01:14:24 |
| `lhconsensus` | `lhconsensus` | `179.43.153.10` | 2026-10-31T01:15:59 |
| `ubuntu` | `ubuntu` | `179.43.153.10` | 2026-10-31T01:17:28 |
| `bp` | `bp` | `152.32.191.191` | 2026-10-31T01:42:12 |
| `345gs5662d34` | `345gs5662d34` | `152.32.191.191` | 2026-10-31T01:42:15 |
| `bp` | `3245gs5662d34` | `152.32.191.191` | 2026-10-31T01:42:17 |
| `toni` | `toni123` | `114.130.85.36` | 2026-10-31T01:53:39 |
| `345gs5662d34` | `345gs5662d34` | `114.130.85.36` | 2026-10-31T01:53:43 |
| `toni` | `3245gs5662d34` | `114.130.85.36` | 2026-10-31T01:53:45 |
| `admin` | `admin` | `193.187.110.159` | 2026-10-31T02:10:48 |
| `root` | `111111` | `92.118.39.71` | 2026-10-31T02:16:43 |
| `root` | `123` | `92.118.39.71` | 2026-10-31T02:18:37 |
_… 16 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **60** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 16 |
| libssh | 13 |
| OpenSSH | 3 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 5 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `390ffe68a68c...` | Modern SSH client | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `104.208.108.166`, `75.112.23.30`, `114.130.85.36`, `152.32.191.191`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **21** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | LOW |
| `AS136188` | NINGBO, ZHEJIANG Province, P.R.China. | 1 | HIGH |
| `AS42555` | OPTICCOM- BULGARIA Ltd. | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS27901` | Pacifico Cable SPA. | 1 | MEDIUM |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-97c753b57134

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-10-31 00:01 |
| **Last Seen** | 2026-10-31 00:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 00:01:06` | `cowrie.session.connect` |
| `2026-10-31 00:01:06` | `cowrie.client.version` |
| `2026-10-31 00:01:07` | `cowrie.client.kex` |
| `2026-10-31 00:01:07` | `cowrie.login.success` |
| `2026-10-31 00:01:08` | `cowrie.session.params` |
| `2026-10-31 00:01:08` | `cowrie.command.input` |
| `2026-10-31 00:01:08` | `cowrie.command.failed` |
| `2026-10-31 00:01:09` | `cowrie.log.closed` |
| `2026-10-31 00:01:10` | `cowrie.session.params` |
| `2026-10-31 00:01:10` | `cowrie.command.input` |
| `2026-10-31 00:01:10` | `cowrie.session.file_download` |
| `2026-10-31 00:01:10` | `cowrie.log.closed` |
| `2026-10-31 00:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8b7bc736e4

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-10-31 00:01 |
| **Last Seen** | 2026-10-31 00:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 00:01:10` | `cowrie.session.connect` |
| `2026-10-31 00:01:10` | `cowrie.client.version` |
| `2026-10-31 00:01:10` | `cowrie.client.kex` |
| `2026-10-31 00:01:11` | `cowrie.login.success` |
| `2026-10-31 00:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db17302104d

| Field | Detail |
|---|---|
| **Source IP** | `182.92.131[.]52` |
| **First Seen** | 2026-10-31 00:11 |
| **Last Seen** | 2026-10-31 00:12 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 00:11:17` | `cowrie.session.connect` |
| `2026-10-31 00:12:03` | `cowrie.client.version` |
| `2026-10-31 00:12:03` | `cowrie.client.kex` |
| `2026-10-31 00:12:06` | `cowrie.login.success` |
| `2026-10-31 00:12:09` | `cowrie.session.params` |
| `2026-10-31 00:12:09` | `cowrie.command.input` |
| `2026-10-31 00:12:10` | `cowrie.log.closed` |
| `2026-10-31 00:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.131[.]52` to AbuseIPDB if not already reported
- [ ] Block `182.92.131[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89907906788e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-31 00:16 |
| **Last Seen** | 2026-10-31 00:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 00:16:34` | `cowrie.session.connect` |
| `2026-10-31 00:16:34` | `cowrie.client.version` |
| `2026-10-31 00:16:35` | `cowrie.client.kex` |
| `2026-10-31 00:16:35` | `cowrie.login.success` |
| `2026-10-31 00:16:35` | `cowrie.direct-tcpip.request` |
| `2026-10-31 00:16:35` | `cowrie.direct-tcpip.data` |
| `2026-10-31 00:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6e11be85c2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-31 00:19 |
| **Last Seen** | 2026-10-31 00:19 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 00:19:24` | `cowrie.session.connect` |
| `2026-10-31 00:19:24` | `cowrie.client.version` |
| `2026-10-31 00:19:24` | `cowrie.client.kex` |
| `2026-10-31 00:19:25` | `cowrie.login.success` |
| `2026-10-31 00:19:32` | `cowrie.direct-tcpip.request` |
| `2026-10-31 00:19:38` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 00:19:38` | `cowrie.direct-tcpip.data` |
| `2026-10-31 00:19:41` | `cowrie.direct-tcpip.request` |
| `2026-10-31 00:19:43` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 00:19:43` | `cowrie.direct-tcpip.data` |
| `2026-10-31 00:19:51` | `cowrie.direct-tcpip.request` |
| `2026-10-31 00:19:52` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 00:19:52` | `cowrie.direct-tcpip.data` |
| `2026-10-31 00:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62308882496c

| Field | Detail |
|---|---|
| **Source IP** | `179.43.153[.]10` |
| **First Seen** | 2026-10-31 01:12 |
| **Last Seen** | 2026-10-31 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 01:12:55` | `cowrie.session.connect` |
| `2026-10-31 01:12:55` | `cowrie.client.version` |
| `2026-10-31 01:12:55` | `cowrie.client.kex` |
| `2026-10-31 01:12:55` | `cowrie.login.success` |
| `2026-10-31 01:12:56` | `cowrie.session.params` |
| `2026-10-31 01:12:56` | `cowrie.command.input` |
| `2026-10-31 01:12:56` | `cowrie.log.closed` |
| `2026-10-31 01:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.153[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.43.153[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b601bccb8f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.191[.]191` |
| **First Seen** | 2026-10-31 01:42 |
| **Last Seen** | 2026-10-31 01:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 01:42:10` | `cowrie.session.connect` |
| `2026-10-31 01:42:10` | `cowrie.client.version` |
| `2026-10-31 01:42:11` | `cowrie.client.kex` |
| `2026-10-31 01:42:12` | `cowrie.login.success` |
| `2026-10-31 01:42:12` | `cowrie.session.params` |
| `2026-10-31 01:42:12` | `cowrie.command.input` |
| `2026-10-31 01:42:12` | `cowrie.command.failed` |
| `2026-10-31 01:42:13` | `cowrie.log.closed` |
| `2026-10-31 01:42:14` | `cowrie.session.params` |
| `2026-10-31 01:42:14` | `cowrie.command.input` |
| `2026-10-31 01:42:14` | `cowrie.session.file_download` |
| `2026-10-31 01:42:14` | `cowrie.log.closed` |
| `2026-10-31 01:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.191[.]191` to AbuseIPDB if not already reported
- [ ] Block `152.32.191[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d0288ccdf1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.191[.]191` |
| **First Seen** | 2026-10-31 01:42 |
| **Last Seen** | 2026-10-31 01:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 01:42:14` | `cowrie.session.connect` |
| `2026-10-31 01:42:14` | `cowrie.client.version` |
| `2026-10-31 01:42:14` | `cowrie.client.kex` |
| `2026-10-31 01:42:15` | `cowrie.login.success` |
| `2026-10-31 01:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.191[.]191` to AbuseIPDB if not already reported
- [ ] Block `152.32.191[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852d64419f6e

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-10-31 01:53 |
| **Last Seen** | 2026-10-31 01:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 01:53:38` | `cowrie.session.connect` |
| `2026-10-31 01:53:38` | `cowrie.client.version` |
| `2026-10-31 01:53:38` | `cowrie.client.kex` |
| `2026-10-31 01:53:39` | `cowrie.login.success` |
| `2026-10-31 01:53:40` | `cowrie.session.params` |
| `2026-10-31 01:53:40` | `cowrie.command.input` |
| `2026-10-31 01:53:40` | `cowrie.command.failed` |
| `2026-10-31 01:53:41` | `cowrie.log.closed` |
| `2026-10-31 01:53:41` | `cowrie.session.params` |
| `2026-10-31 01:53:41` | `cowrie.command.input` |
| `2026-10-31 01:53:42` | `cowrie.session.file_download` |
| `2026-10-31 01:53:42` | `cowrie.log.closed` |
| `2026-10-31 01:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3cf663ba2f3

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-10-31 01:53 |
| **Last Seen** | 2026-10-31 01:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 01:53:42` | `cowrie.session.connect` |
| `2026-10-31 01:53:42` | `cowrie.client.version` |
| `2026-10-31 01:53:42` | `cowrie.client.kex` |
| `2026-10-31 01:53:43` | `cowrie.login.success` |
| `2026-10-31 01:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82778ab15bcb

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]159` |
| **First Seen** | 2026-10-31 02:10 |
| **Last Seen** | 2026-10-31 02:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:10:47` | `cowrie.session.connect` |
| `2026-10-31 02:10:47` | `cowrie.client.version` |
| `2026-10-31 02:10:48` | `cowrie.client.kex` |
| `2026-10-31 02:10:48` | `cowrie.login.success` |
| `2026-10-31 02:10:48` | `cowrie.direct-tcpip.request` |
| `2026-10-31 02:10:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-31 02:10:48` | `cowrie.direct-tcpip.data` |
| `2026-10-31 02:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]159` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82bac35cf97

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-31 02:16 |
| **Last Seen** | 2026-10-31 02:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:16:38` | `cowrie.session.connect` |
| `2026-10-31 02:16:38` | `cowrie.client.version` |
| `2026-10-31 02:16:38` | `cowrie.client.kex` |
| `2026-10-31 02:16:38` | `cowrie.login.success` |
| `2026-10-31 02:16:38` | `cowrie.direct-tcpip.request` |
| `2026-10-31 02:16:38` | `cowrie.direct-tcpip.data` |
| `2026-10-31 02:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb62d0575f29

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:16 |
| **Last Seen** | 2026-10-31 02:17 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b903fa351ae8e556546ad213b26b8f3b_small_control'"'"' '"'"'check_b903fa351ae8e556546ad213b26b8f3b'"'"'', printf '\n%s|%s\n' 'check_b903fa351ae8e556546ad213b26b8f3b_small_control' 'check_b903fa351ae8e556546ad213b26b8f3b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b903fa351ae8e556546ad213b26b8f3b_small_math'"'"' "$((505*630+28))"', (505*630+28, printf '\n%s|%s\n' 'check_b903fa351ae8e556546ad213b26b8f3b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:16:39` | `cowrie.session.connect` |
| `2026-10-31 02:16:40` | `cowrie.client.version` |
| `2026-10-31 02:16:40` | `cowrie.client.kex` |
| `2026-10-31 02:16:43` | `cowrie.login.success` |
| `2026-10-31 02:16:44` | `cowrie.client.size` |
| `2026-10-31 02:16:47` | `cowrie.session.params` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| `2026-10-31 02:16:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c06a1c28c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:18 |
| **Last Seen** | 2026-10-31 02:19 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_249b49729ac25d9996f175a43a4d637c_small_control'"'"' '"'"'check_249b49729ac25d9996f175a43a4d637c'"'"'', printf '\n%s|%s\n' 'check_249b49729ac25d9996f175a43a4d637c_small_control' 'check_249b49729ac25d9996f175a43a4d637c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_249b49729ac25d9996f175a43a4d637c_small_math'"'"' "$((399*965+60))"', (399*965+60, printf '\n%s|%s\n' 'check_249b49729ac25d9996f175a43a4d637c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:18:35` | `cowrie.session.connect` |
| `2026-10-31 02:18:35` | `cowrie.client.version` |
| `2026-10-31 02:18:35` | `cowrie.client.kex` |
| `2026-10-31 02:18:37` | `cowrie.login.success` |
| `2026-10-31 02:18:38` | `cowrie.client.size` |
| `2026-10-31 02:18:39` | `cowrie.session.params` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| `2026-10-31 02:18:39` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42e4b4b9e07

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:20 |
| **Last Seen** | 2026-10-31 02:21 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3c0b7c74f7fb3b238b8c63ce37f7f27d_small_control'"'"' '"'"'check_3c0b7c74f7fb3b238b8c63ce37f7f27d'"'"'', printf '\n%s|%s\n' 'check_3c0b7c74f7fb3b238b8c63ce37f7f27d_small_control' 'check_3c0b7c74f7fb3b238b8c63ce37f7f27d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3c0b7c74f7fb3b238b8c63ce37f7f27d_small_math'"'"' "$((417*149+46))"', (417*149+46, printf '\n%s|%s\n' 'check_3c0b7c74f7fb3b238b8c63ce37f7f27d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:20:42` | `cowrie.session.connect` |
| `2026-10-31 02:20:42` | `cowrie.client.version` |
| `2026-10-31 02:20:42` | `cowrie.client.kex` |
| `2026-10-31 02:20:44` | `cowrie.login.success` |
| `2026-10-31 02:20:45` | `cowrie.client.size` |
| `2026-10-31 02:20:46` | `cowrie.session.params` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| `2026-10-31 02:20:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe279c862f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:22 |
| **Last Seen** | 2026-10-31 02:23 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8cc538a4d1f7080fbfe93ea537d1dd90_small_control'"'"' '"'"'check_8cc538a4d1f7080fbfe93ea537d1dd90'"'"'', printf '\n%s|%s\n' 'check_8cc538a4d1f7080fbfe93ea537d1dd90_small_control' 'check_8cc538a4d1f7080fbfe93ea537d1dd90', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8cc538a4d1f7080fbfe93ea537d1dd90_small_math'"'"' "$((146*627+51))"', (146*627+51, printf '\n%s|%s\n' 'check_8cc538a4d1f7080fbfe93ea537d1dd90_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:22:52` | `cowrie.session.connect` |
| `2026-10-31 02:22:52` | `cowrie.client.version` |
| `2026-10-31 02:22:52` | `cowrie.client.kex` |
| `2026-10-31 02:22:53` | `cowrie.login.success` |
| `2026-10-31 02:22:55` | `cowrie.client.size` |
| `2026-10-31 02:22:55` | `cowrie.session.params` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| `2026-10-31 02:22:55` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48e76c63b27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:25 |
| **Last Seen** | 2026-10-31 02:25 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bae723b035e31f122b1faf494645a72c_small_control'"'"' '"'"'check_bae723b035e31f122b1faf494645a72c'"'"'', printf '\n%s|%s\n' 'check_bae723b035e31f122b1faf494645a72c_small_control' 'check_bae723b035e31f122b1faf494645a72c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bae723b035e31f122b1faf494645a72c_small_math'"'"' "$((989*218+27))"', (989*218+27, printf '\n%s|%s\n' 'check_bae723b035e31f122b1faf494645a72c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:25:05` | `cowrie.session.connect` |
| `2026-10-31 02:25:05` | `cowrie.client.version` |
| `2026-10-31 02:25:05` | `cowrie.client.kex` |
| `2026-10-31 02:25:06` | `cowrie.login.success` |
| `2026-10-31 02:25:07` | `cowrie.client.size` |
| `2026-10-31 02:25:07` | `cowrie.session.params` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| `2026-10-31 02:25:08` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81230be242c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:27 |
| **Last Seen** | 2026-10-31 02:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_76ac7f24ce9c25d277709fedceb8db4b_small_control'"'"' '"'"'check_76ac7f24ce9c25d277709fedceb8db4b'"'"'', printf '\n%s|%s\n' 'check_76ac7f24ce9c25d277709fedceb8db4b_small_control' 'check_76ac7f24ce9c25d277709fedceb8db4b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_76ac7f24ce9c25d277709fedceb8db4b_small_math'"'"' "$((471*837+20))"', (471*837+20, printf '\n%s|%s\n' 'check_76ac7f24ce9c25d277709fedceb8db4b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:27:25` | `cowrie.session.connect` |
| `2026-10-31 02:27:25` | `cowrie.client.version` |
| `2026-10-31 02:27:25` | `cowrie.client.kex` |
| `2026-10-31 02:27:26` | `cowrie.login.success` |
| `2026-10-31 02:27:27` | `cowrie.client.size` |
| `2026-10-31 02:27:27` | `cowrie.session.params` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| `2026-10-31 02:27:27` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edbc2465a0d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:31 |
| **Last Seen** | 2026-10-31 02:32 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29c5d6796d270d33deddc675b2f0ffbc_small_control'"'"' '"'"'check_29c5d6796d270d33deddc675b2f0ffbc'"'"'', printf '\n%s|%s\n' 'check_29c5d6796d270d33deddc675b2f0ffbc_small_control' 'check_29c5d6796d270d33deddc675b2f0ffbc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_29c5d6796d270d33deddc675b2f0ffbc_small_math'"'"' "$((724*401+24))"', (724*401+24, printf '\n%s|%s\n' 'check_29c5d6796d270d33deddc675b2f0ffbc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:31:44` | `cowrie.session.connect` |
| `2026-10-31 02:31:44` | `cowrie.client.version` |
| `2026-10-31 02:31:44` | `cowrie.client.kex` |
| `2026-10-31 02:31:45` | `cowrie.login.success` |
| `2026-10-31 02:31:46` | `cowrie.client.size` |
| `2026-10-31 02:31:46` | `cowrie.session.params` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:46` | `cowrie.command.input` |
| `2026-10-31 02:31:47` | `cowrie.command.input` |
| `2026-10-31 02:31:47` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9105b93273d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:33 |
| **Last Seen** | 2026-10-31 02:34 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f2e69b02b34c73101556c37835376d3b_small_control'"'"' '"'"'check_f2e69b02b34c73101556c37835376d3b'"'"'', printf '\n%s|%s\n' 'check_f2e69b02b34c73101556c37835376d3b_small_control' 'check_f2e69b02b34c73101556c37835376d3b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f2e69b02b34c73101556c37835376d3b_small_math'"'"' "$((369*43+6))"', (369*43+6, printf '\n%s|%s\n' 'check_f2e69b02b34c73101556c37835376d3b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:33:51` | `cowrie.session.connect` |
| `2026-10-31 02:33:51` | `cowrie.client.version` |
| `2026-10-31 02:33:52` | `cowrie.client.kex` |
| `2026-10-31 02:33:53` | `cowrie.login.success` |
| `2026-10-31 02:33:53` | `cowrie.client.size` |
| `2026-10-31 02:33:54` | `cowrie.session.params` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| `2026-10-31 02:33:54` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d276c10fde7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-31 02:35 |
| **Last Seen** | 2026-10-31 02:36 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1524f67befeab2390080e4ad05795758_small_control'"'"' '"'"'check_1524f67befeab2390080e4ad05795758'"'"'', printf '\n%s|%s\n' 'check_1524f67befeab2390080e4ad05795758_small_control' 'check_1524f67befeab2390080e4ad05795758', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1524f67befeab2390080e4ad05795758_small_math'"'"' "$((428*667+78))"', (428*667+78, printf '\n%s|%s\n' 'check_1524f67befeab2390080e4ad05795758_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:35:52` | `cowrie.session.connect` |
| `2026-10-31 02:35:52` | `cowrie.client.version` |
| `2026-10-31 02:35:52` | `cowrie.client.kex` |
| `2026-10-31 02:35:54` | `cowrie.login.success` |
| `2026-10-31 02:35:55` | `cowrie.client.size` |
| `2026-10-31 02:35:55` | `cowrie.session.params` |
| `2026-10-31 02:35:55` | `cowrie.command.input` |
| `2026-10-31 02:35:55` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| `2026-10-31 02:35:56` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a33636d6745b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-31 02:46 |
| **Last Seen** | 2026-10-31 02:46 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:46:20` | `cowrie.session.connect` |
| `2026-10-31 02:46:20` | `cowrie.client.version` |
| `2026-10-31 02:46:20` | `cowrie.client.kex` |
| `2026-10-31 02:46:20` | `cowrie.login.success` |
| `2026-10-31 02:46:31` | `cowrie.direct-tcpip.request` |
| `2026-10-31 02:46:34` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 02:46:34` | `cowrie.direct-tcpip.data` |
| `2026-10-31 02:46:37` | `cowrie.direct-tcpip.request` |
| `2026-10-31 02:46:43` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 02:46:43` | `cowrie.direct-tcpip.data` |
| `2026-10-31 02:46:49` | `cowrie.direct-tcpip.request` |
| `2026-10-31 02:46:51` | `cowrie.direct-tcpip.ja4` |
| `2026-10-31 02:46:51` | `cowrie.direct-tcpip.data` |
| `2026-10-31 02:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0c5056353d

| Field | Detail |
|---|---|
| **Source IP** | `75.112.23[.]30` |
| **First Seen** | 2026-10-31 02:48 |
| **Last Seen** | 2026-10-31 02:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:48:08` | `cowrie.session.connect` |
| `2026-10-31 02:48:08` | `cowrie.client.version` |
| `2026-10-31 02:48:08` | `cowrie.client.kex` |
| `2026-10-31 02:48:08` | `cowrie.login.success` |
| `2026-10-31 02:48:08` | `cowrie.session.params` |
| `2026-10-31 02:48:08` | `cowrie.command.input` |
| `2026-10-31 02:48:08` | `cowrie.command.failed` |
| `2026-10-31 02:48:09` | `cowrie.log.closed` |
| `2026-10-31 02:48:09` | `cowrie.session.params` |
| `2026-10-31 02:48:09` | `cowrie.command.input` |
| `2026-10-31 02:48:09` | `cowrie.session.file_download` |
| `2026-10-31 02:48:09` | `cowrie.log.closed` |
| `2026-10-31 02:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.112.23[.]30` to AbuseIPDB if not already reported
- [ ] Block `75.112.23[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514677846a48

| Field | Detail |
|---|---|
| **Source IP** | `75.112.23[.]30` |
| **First Seen** | 2026-10-31 02:48 |
| **Last Seen** | 2026-10-31 02:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 02:48:09` | `cowrie.session.connect` |
| `2026-10-31 02:48:09` | `cowrie.client.version` |
| `2026-10-31 02:48:09` | `cowrie.client.kex` |
| `2026-10-31 02:48:10` | `cowrie.login.success` |
| `2026-10-31 02:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.112.23[.]30` to AbuseIPDB if not already reported
- [ ] Block `75.112.23[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **2** | 2026-10-31 00:14 | 2026-10-31 02:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.42.1[.]52` | 1 | 2026-10-31 02:01 | 2026-10-31 02:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-31 00:01 | 2026-10-31 00:03 | 70s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-31 02:06 | 2026-10-31 02:07 | 77s | 0 | `T1592` | 🟢 LOW |
| `159.75.115[.]184` | 1 | 2026-10-31 02:53 | 2026-10-31 02:54 | 43s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | 1 | 2026-10-31 01:09 | 2026-10-31 01:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-10-31 01:10 | 2026-10-31 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.60.80[.]69` | 1 | 2026-10-31 02:25 | 2026-10-31 02:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.92.131[.]52` | 1 | 2026-10-31 00:11 | 2026-10-31 00:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.17.237[.]123` | 1 | 2026-10-31 00:51 | 2026-10-31 00:52 | 32s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | 1 | 2026-10-31 02:35 | 2026-10-31 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.44.213[.]144` | 1 | 2026-10-31 02:43 | 2026-10-31 02:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `211.107.189[.]125` | 1 | 2026-10-31 00:08 | 2026-10-31 00:08 | 19s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-31 00:55 | 2026-10-31 00:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.82.209[.]93` | 1 | 2026-10-31 01:28 | 2026-10-31 01:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `46.201.200[.]63` | 1 | 2026-10-31 00:15 | 2026-10-31 00:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-10-31 01:08 | 2026-10-31 01:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]39` | 1 | 2026-10-31 00:26 | 2026-10-31 00:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-10-31 00:26 | 2026-10-31 00:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-10-31 01:33 | 2026-10-31 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-31 01:29 | 2026-10-31 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-10-31 02:29 | 2026-10-31 02:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `104.208.108[.]166` | HK | Microsoft Corporation | **100** ⚠️ | 50 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `46.201.200[.]63` | UA | JSC Ukrtelecom | **100** ⚠️ | 1 |
| `80.94.95[.]118` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `159.75.115[.]184` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 7 |
| `3.82.209[.]93` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 19 |
| `64.62.197[.]182` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `202.44.213[.]144` | TH | Internet Thailand Company Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 48 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (21.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 22 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-10-31T03:07:53Z_

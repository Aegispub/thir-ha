# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-31 |
| **Generated At** | 2026-10-31T16:30:12Z |
| **Shift Time** | 16:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **381** |
| Confirmed Threats | **345** |
| False Positives Filtered | **36** (9.4%) |
| Unique Attacker IPs | **215** |
| Countries of Origin | **52** |
| High Severity Cases | **233** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **148** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1718** |
| Unique Credential Pairs | **1399** |
| Unique Usernames | **472** |
| Unique Passwords | **900** |
| Successful Auth Pairs | **1590** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 563 |
| `345gs5662d34` | 111 |
| `support` | 57 |
| `admin` | 50 |
| `ubuntu` | 42 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 111 |
| `3245gs5662d34` | 110 |
| `123456` | 83 |
| `support` | 54 |
| `123` | 48 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 111 |
| `support` | `support` | 54 |
| `root` | `3245gs5662d34` | 43 |
| `root` | `admin` | 8 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-10-31T03:04:00 |
| `firedancer` | `firedancer` | `179.43.153.10` | 2026-10-31T03:14:29 |
| `lighthouse` | `lighthouse` | `179.43.153.10` | 2026-10-31T03:15:58 |
| `lhconsensus` | `lhconsensus` | `179.43.153.10` | 2026-10-31T03:17:29 |
| `ubuntu` | `ubuntu` | `179.43.153.10` | 2026-10-31T03:18:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `66.228.62.150` | 2026-10-31T03:47:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.239.71.239` | 2026-10-31T03:47:37 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `185.191.236.38` | 2026-10-31T03:48:25 |
| `dockeruser` | `dockeruserpass` | `43.161.246.189` | 2026-10-31T04:03:48 |
| `345gs5662d34` | `345gs5662d34` | `43.161.246.189` | 2026-10-31T04:03:52 |
| `dockeruser` | `3245gs5662d34` | `43.161.246.189` | 2026-10-31T04:03:53 |
| `root` | `asd@1234` | `223.93.164.218` | 2026-10-31T04:05:43 |
| `ll` | `ll@123` | `43.98.162.26` | 2026-10-31T04:06:09 |
| `345gs5662d34` | `345gs5662d34` | `43.98.162.26` | 2026-10-31T04:06:13 |
| `ll` | `3245gs5662d34` | `43.98.162.26` | 2026-10-31T04:06:15 |
| `root` | `Yr123456` | `52.237.80.79` | 2026-10-31T04:07:09 |
| `345gs5662d34` | `345gs5662d34` | `52.237.80.79` | 2026-10-31T04:07:13 |
| `root` | `3245gs5662d34` | `52.237.80.79` | 2026-10-31T04:07:14 |
| `root` | `123123456` | `69.5.20.205` | 2026-10-31T04:09:56 |
| `345gs5662d34` | `345gs5662d34` | `69.5.20.205` | 2026-10-31T04:10:00 |
_… 1570 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **381** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 167 |
| Go SSH scanner | 75 |
| OpenSSH | 7 |
| Unknown | 3 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 138 | 71 |
| `2ec37a7cc8da...` | Mirai/variant | 50 | 3 |
| `03a80b21afa8...` | Modern SSH client | 10 | 6 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `390ffe68a68c...` | Modern SSH client | 6 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 138 | 71 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 50 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 7 | — |
| `03a80b21afa8...` | libssh | 10 | 6 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 6 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **66** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 72 | 66 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "jitsi\n0rxP9rK1D7fY\n0rxP9rK1D7fY"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `27.17.30.150`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.192.46.29`, `103.48.192.48`, `78.109.200.147`, `119.246.15.94`, `182.79.112.190`, `203.145.143.163`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **215** |
| Unique ASNs | **96** |
| High-Risk ASNs | **69** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 67 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS15169` | Google LLC | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (229)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e133ad7ca945

| Field | Detail |
|---|---|
| **Source IP** | `179.43.153[.]10` |
| **First Seen** | 2026-10-31 03:14 |
| **Last Seen** | 2026-10-31 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 03:14:29` | `cowrie.session.connect` |
| `2026-10-31 03:14:29` | `cowrie.client.version` |
| `2026-10-31 03:14:29` | `cowrie.client.kex` |
| `2026-10-31 03:14:29` | `cowrie.login.success` |
| `2026-10-31 03:14:30` | `cowrie.session.params` |
| `2026-10-31 03:14:30` | `cowrie.command.input` |
| `2026-10-31 03:14:30` | `cowrie.log.closed` |
| `2026-10-31 03:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.153[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.43.153[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ce833e052b

| Field | Detail |
|---|---|
| **Source IP** | `66.228.62[.]150` |
| **First Seen** | 2026-10-31 03:47 |
| **Last Seen** | 2026-10-31 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 03:47:19` | `cowrie.session.connect` |
| `2026-10-31 03:47:19` | `cowrie.login.success` |
| `2026-10-31 03:47:20` | `cowrie.session.params` |
| `2026-10-31 03:47:20` | `cowrie.command.input` |
| `2026-10-31 03:47:20` | `cowrie.command.failed` |
| `2026-10-31 03:47:20` | `cowrie.command.input` |
| `2026-10-31 03:47:20` | `cowrie.command.failed` |
| `2026-10-31 03:47:20` | `cowrie.command.input` |
| `2026-10-31 03:47:20` | `cowrie.command.failed` |
| `2026-10-31 03:47:20` | `cowrie.command.input` |
| `2026-10-31 03:47:20` | `cowrie.log.closed` |
| `2026-10-31 03:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.62[.]150` to AbuseIPDB if not already reported
- [ ] Block `66.228.62[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274c1de4c2d2

| Field | Detail |
|---|---|
| **Source IP** | `172.239.71[.]239` |
| **First Seen** | 2026-10-31 03:47 |
| **Last Seen** | 2026-10-31 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 03:47:37` | `cowrie.session.connect` |
| `2026-10-31 03:47:37` | `cowrie.login.success` |
| `2026-10-31 03:47:38` | `cowrie.session.params` |
| `2026-10-31 03:47:38` | `cowrie.command.input` |
| `2026-10-31 03:47:38` | `cowrie.command.input` |
| `2026-10-31 03:47:38` | `cowrie.command.failed` |
| `2026-10-31 03:47:38` | `cowrie.command.input` |
| `2026-10-31 03:47:38` | `cowrie.command.failed` |
| `2026-10-31 03:47:38` | `cowrie.command.input` |
| `2026-10-31 03:47:38` | `cowrie.log.closed` |
| `2026-10-31 03:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.239.71[.]239` to AbuseIPDB if not already reported
- [ ] Block `172.239.71[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f63fe84f85

| Field | Detail |
|---|---|
| **Source IP** | `185.191.236[.]38` |
| **First Seen** | 2026-10-31 03:48 |
| **Last Seen** | 2026-10-31 03:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: identity, Accept-Language: en-US;q=0.8,en;q=0.7, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 03:48:25` | `cowrie.session.connect` |
| `2026-10-31 03:48:25` | `cowrie.login.success` |
| `2026-10-31 03:48:26` | `cowrie.session.params` |
| `2026-10-31 03:48:26` | `cowrie.command.input` |
| `2026-10-31 03:48:26` | `cowrie.command.failed` |
| `2026-10-31 03:48:26` | `cowrie.command.input` |
| `2026-10-31 03:48:26` | `cowrie.command.failed` |
| `2026-10-31 03:48:26` | `cowrie.command.input` |
| `2026-10-31 03:48:26` | `cowrie.command.failed` |
| `2026-10-31 03:48:26` | `cowrie.command.input` |
| `2026-10-31 03:48:26` | `cowrie.command.input` |
| `2026-10-31 03:48:30` | `cowrie.log.closed` |
| `2026-10-31 03:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.191.236[.]38` to AbuseIPDB if not already reported
- [ ] Block `185.191.236[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e5be189a67

| Field | Detail |
|---|---|
| **Source IP** | `43.161.246[.]189` |
| **First Seen** | 2026-10-31 04:03 |
| **Last Seen** | 2026-10-31 04:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:03:47` | `cowrie.session.connect` |
| `2026-10-31 04:03:47` | `cowrie.client.version` |
| `2026-10-31 04:03:47` | `cowrie.client.kex` |
| `2026-10-31 04:03:48` | `cowrie.login.success` |
| `2026-10-31 04:03:49` | `cowrie.session.params` |
| `2026-10-31 04:03:49` | `cowrie.command.input` |
| `2026-10-31 04:03:49` | `cowrie.command.failed` |
| `2026-10-31 04:03:49` | `cowrie.log.closed` |
| `2026-10-31 04:03:50` | `cowrie.session.params` |
| `2026-10-31 04:03:50` | `cowrie.command.input` |
| `2026-10-31 04:03:50` | `cowrie.session.file_download` |
| `2026-10-31 04:03:50` | `cowrie.log.closed` |
| `2026-10-31 04:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.161.246[.]189` to AbuseIPDB if not already reported
- [ ] Block `43.161.246[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7b12143b21

| Field | Detail |
|---|---|
| **Source IP** | `43.161.246[.]189` |
| **First Seen** | 2026-10-31 04:03 |
| **Last Seen** | 2026-10-31 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:03:51` | `cowrie.session.connect` |
| `2026-10-31 04:03:51` | `cowrie.client.version` |
| `2026-10-31 04:03:51` | `cowrie.client.kex` |
| `2026-10-31 04:03:52` | `cowrie.login.success` |
| `2026-10-31 04:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.161.246[.]189` to AbuseIPDB if not already reported
- [ ] Block `43.161.246[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58c28e683ce

| Field | Detail |
|---|---|
| **Source IP** | `223.93.164[.]218` |
| **First Seen** | 2026-10-31 04:05 |
| **Last Seen** | 2026-10-31 04:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:05:41` | `cowrie.session.connect` |
| `2026-10-31 04:05:41` | `cowrie.client.version` |
| `2026-10-31 04:05:42` | `cowrie.client.kex` |
| `2026-10-31 04:05:43` | `cowrie.login.success` |
| `2026-10-31 04:05:44` | `cowrie.session.params` |
| `2026-10-31 04:05:44` | `cowrie.command.input` |
| `2026-10-31 04:05:44` | `cowrie.command.failed` |
| `2026-10-31 04:05:44` | `cowrie.log.closed` |
| `2026-10-31 04:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.93.164[.]218` to AbuseIPDB if not already reported
- [ ] Block `223.93.164[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f2357327e5

| Field | Detail |
|---|---|
| **Source IP** | `43.98.162[.]26` |
| **First Seen** | 2026-10-31 04:06 |
| **Last Seen** | 2026-10-31 04:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:06:08` | `cowrie.session.connect` |
| `2026-10-31 04:06:08` | `cowrie.client.version` |
| `2026-10-31 04:06:08` | `cowrie.client.kex` |
| `2026-10-31 04:06:09` | `cowrie.login.success` |
| `2026-10-31 04:06:10` | `cowrie.session.params` |
| `2026-10-31 04:06:10` | `cowrie.command.input` |
| `2026-10-31 04:06:10` | `cowrie.command.failed` |
| `2026-10-31 04:06:10` | `cowrie.log.closed` |
| `2026-10-31 04:06:11` | `cowrie.session.params` |
| `2026-10-31 04:06:11` | `cowrie.command.input` |
| `2026-10-31 04:06:12` | `cowrie.session.file_download` |
| `2026-10-31 04:06:12` | `cowrie.log.closed` |
| `2026-10-31 04:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.162[.]26` to AbuseIPDB if not already reported
- [ ] Block `43.98.162[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c3aebc3f13

| Field | Detail |
|---|---|
| **Source IP** | `43.98.162[.]26` |
| **First Seen** | 2026-10-31 04:06 |
| **Last Seen** | 2026-10-31 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:06:12` | `cowrie.session.connect` |
| `2026-10-31 04:06:12` | `cowrie.client.version` |
| `2026-10-31 04:06:12` | `cowrie.client.kex` |
| `2026-10-31 04:06:13` | `cowrie.login.success` |
| `2026-10-31 04:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.98.162[.]26` to AbuseIPDB if not already reported
- [ ] Block `43.98.162[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d348eb9898

| Field | Detail |
|---|---|
| **Source IP** | `52.237.80[.]79` |
| **First Seen** | 2026-10-31 04:07 |
| **Last Seen** | 2026-10-31 04:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:07:08` | `cowrie.session.connect` |
| `2026-10-31 04:07:08` | `cowrie.client.version` |
| `2026-10-31 04:07:08` | `cowrie.client.kex` |
| `2026-10-31 04:07:09` | `cowrie.login.success` |
| `2026-10-31 04:07:10` | `cowrie.session.params` |
| `2026-10-31 04:07:10` | `cowrie.command.input` |
| `2026-10-31 04:07:10` | `cowrie.command.failed` |
| `2026-10-31 04:07:10` | `cowrie.log.closed` |
| `2026-10-31 04:07:11` | `cowrie.session.params` |
| `2026-10-31 04:07:11` | `cowrie.command.input` |
| `2026-10-31 04:07:11` | `cowrie.session.file_download` |
| `2026-10-31 04:07:11` | `cowrie.log.closed` |
| `2026-10-31 04:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.80[.]79` to AbuseIPDB if not already reported
- [ ] Block `52.237.80[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ef02668488

| Field | Detail |
|---|---|
| **Source IP** | `52.237.80[.]79` |
| **First Seen** | 2026-10-31 04:07 |
| **Last Seen** | 2026-10-31 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:07:12` | `cowrie.session.connect` |
| `2026-10-31 04:07:12` | `cowrie.client.version` |
| `2026-10-31 04:07:12` | `cowrie.client.kex` |
| `2026-10-31 04:07:13` | `cowrie.login.success` |
| `2026-10-31 04:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.80[.]79` to AbuseIPDB if not already reported
- [ ] Block `52.237.80[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5585e1d49060

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]205` |
| **First Seen** | 2026-10-31 04:09 |
| **Last Seen** | 2026-10-31 04:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:09:54` | `cowrie.session.connect` |
| `2026-10-31 04:09:54` | `cowrie.client.version` |
| `2026-10-31 04:09:55` | `cowrie.client.kex` |
| `2026-10-31 04:09:56` | `cowrie.login.success` |
| `2026-10-31 04:09:57` | `cowrie.session.params` |
| `2026-10-31 04:09:57` | `cowrie.command.input` |
| `2026-10-31 04:09:57` | `cowrie.command.failed` |
| `2026-10-31 04:09:57` | `cowrie.log.closed` |
| `2026-10-31 04:09:58` | `cowrie.session.params` |
| `2026-10-31 04:09:58` | `cowrie.command.input` |
| `2026-10-31 04:09:58` | `cowrie.session.file_download` |
| `2026-10-31 04:09:58` | `cowrie.log.closed` |
| `2026-10-31 04:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a7b6a825c2

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]205` |
| **First Seen** | 2026-10-31 04:09 |
| **Last Seen** | 2026-10-31 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:09:59` | `cowrie.session.connect` |
| `2026-10-31 04:09:59` | `cowrie.client.version` |
| `2026-10-31 04:09:59` | `cowrie.client.kex` |
| `2026-10-31 04:10:00` | `cowrie.login.success` |
| `2026-10-31 04:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb1f88bd4b8

| Field | Detail |
|---|---|
| **Source IP** | `104.218.166[.]62` |
| **First Seen** | 2026-10-31 04:11 |
| **Last Seen** | 2026-10-31 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:11:16` | `cowrie.session.connect` |
| `2026-10-31 04:11:16` | `cowrie.client.version` |
| `2026-10-31 04:11:16` | `cowrie.client.kex` |
| `2026-10-31 04:11:17` | `cowrie.login.success` |
| `2026-10-31 04:11:18` | `cowrie.session.params` |
| `2026-10-31 04:11:18` | `cowrie.command.input` |
| `2026-10-31 04:11:18` | `cowrie.command.failed` |
| `2026-10-31 04:11:19` | `cowrie.log.closed` |
| `2026-10-31 04:11:19` | `cowrie.session.params` |
| `2026-10-31 04:11:19` | `cowrie.command.input` |
| `2026-10-31 04:11:20` | `cowrie.session.file_download` |
| `2026-10-31 04:11:20` | `cowrie.log.closed` |
| `2026-10-31 04:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.166[.]62` to AbuseIPDB if not already reported
- [ ] Block `104.218.166[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ca5b72b91b

| Field | Detail |
|---|---|
| **Source IP** | `104.218.166[.]62` |
| **First Seen** | 2026-10-31 04:11 |
| **Last Seen** | 2026-10-31 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:11:20` | `cowrie.session.connect` |
| `2026-10-31 04:11:20` | `cowrie.client.version` |
| `2026-10-31 04:11:20` | `cowrie.client.kex` |
| `2026-10-31 04:11:21` | `cowrie.login.success` |
| `2026-10-31 04:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.166[.]62` to AbuseIPDB if not already reported
- [ ] Block `104.218.166[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3752a46f44

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-31 04:19 |
| **Last Seen** | 2026-10-31 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:19:10` | `cowrie.session.connect` |
| `2026-10-31 04:19:10` | `cowrie.client.version` |
| `2026-10-31 04:19:10` | `cowrie.client.kex` |
| `2026-10-31 04:19:10` | `cowrie.login.success` |
| `2026-10-31 04:19:10` | `cowrie.direct-tcpip.request` |
| `2026-10-31 04:19:10` | `cowrie.direct-tcpip.data` |
| `2026-10-31 04:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c15ea7559bc

| Field | Detail |
|---|---|
| **Source IP** | `8.211.150[.]32` |
| **First Seen** | 2026-10-31 04:29 |
| **Last Seen** | 2026-10-31 04:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:29:19` | `cowrie.session.connect` |
| `2026-10-31 04:29:19` | `cowrie.login.success` |
| `2026-10-31 04:29:20` | `cowrie.session.params` |
| `2026-10-31 04:29:20` | `cowrie.command.input` |
| `2026-10-31 04:29:20` | `cowrie.command.failed` |
| `2026-10-31 04:29:20` | `cowrie.command.input` |
| `2026-10-31 04:29:20` | `cowrie.command.failed` |
| `2026-10-31 04:29:20` | `cowrie.command.input` |
| `2026-10-31 04:29:22` | `cowrie.log.closed` |
| `2026-10-31 04:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.211.150[.]32` to AbuseIPDB if not already reported
- [ ] Block `8.211.150[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4081fc988401

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-10-31 04:31 |
| **Last Seen** | 2026-10-31 04:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:31:04` | `cowrie.session.connect` |
| `2026-10-31 04:31:04` | `cowrie.client.version` |
| `2026-10-31 04:31:04` | `cowrie.client.kex` |
| `2026-10-31 04:31:05` | `cowrie.login.success` |
| `2026-10-31 04:31:06` | `cowrie.session.params` |
| `2026-10-31 04:31:06` | `cowrie.command.input` |
| `2026-10-31 04:31:06` | `cowrie.log.closed` |
| `2026-10-31 04:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29542fb5976

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-10-31 04:31 |
| **Last Seen** | 2026-10-31 04:31 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:31:25` | `cowrie.session.connect` |
| `2026-10-31 04:31:25` | `cowrie.client.version` |
| `2026-10-31 04:31:25` | `cowrie.client.kex` |
| `2026-10-31 04:31:26` | `cowrie.login.success` |
| `2026-10-31 04:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19dc05024af2

| Field | Detail |
|---|---|
| **Source IP** | `178.253.95[.]34` |
| **First Seen** | 2026-10-31 04:48 |
| **Last Seen** | 2026-10-31 04:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:48:34` | `cowrie.session.connect` |
| `2026-10-31 04:48:34` | `cowrie.client.version` |
| `2026-10-31 04:48:34` | `cowrie.client.kex` |
| `2026-10-31 04:48:35` | `cowrie.login.success` |
| `2026-10-31 04:48:35` | `cowrie.session.params` |
| `2026-10-31 04:48:35` | `cowrie.command.input` |
| `2026-10-31 04:48:35` | `cowrie.command.failed` |
| `2026-10-31 04:48:36` | `cowrie.log.closed` |
| `2026-10-31 04:48:37` | `cowrie.session.params` |
| `2026-10-31 04:48:37` | `cowrie.command.input` |
| `2026-10-31 04:48:37` | `cowrie.session.file_download` |
| `2026-10-31 04:48:37` | `cowrie.log.closed` |
| `2026-10-31 04:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.253.95[.]34` to AbuseIPDB if not already reported
- [ ] Block `178.253.95[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e181a8f9fbb6

| Field | Detail |
|---|---|
| **Source IP** | `178.253.95[.]34` |
| **First Seen** | 2026-10-31 04:48 |
| **Last Seen** | 2026-10-31 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:48:37` | `cowrie.session.connect` |
| `2026-10-31 04:48:37` | `cowrie.client.version` |
| `2026-10-31 04:48:37` | `cowrie.client.kex` |
| `2026-10-31 04:48:38` | `cowrie.login.success` |
| `2026-10-31 04:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.253.95[.]34` to AbuseIPDB if not already reported
- [ ] Block `178.253.95[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c236d5cfa3

| Field | Detail |
|---|---|
| **Source IP** | `50.6.193[.]166` |
| **First Seen** | 2026-10-31 04:50 |
| **Last Seen** | 2026-10-31 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:50:19` | `cowrie.session.connect` |
| `2026-10-31 04:50:19` | `cowrie.client.version` |
| `2026-10-31 04:50:19` | `cowrie.client.kex` |
| `2026-10-31 04:50:19` | `cowrie.login.success` |
| `2026-10-31 04:50:19` | `cowrie.session.params` |
| `2026-10-31 04:50:19` | `cowrie.command.input` |
| `2026-10-31 04:50:19` | `cowrie.command.failed` |
| `2026-10-31 04:50:19` | `cowrie.log.closed` |
| `2026-10-31 04:50:20` | `cowrie.session.params` |
| `2026-10-31 04:50:20` | `cowrie.command.input` |
| `2026-10-31 04:50:20` | `cowrie.session.file_download` |
| `2026-10-31 04:50:20` | `cowrie.log.closed` |
| `2026-10-31 04:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.193[.]166` to AbuseIPDB if not already reported
- [ ] Block `50.6.193[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8074e8727699

| Field | Detail |
|---|---|
| **Source IP** | `50.6.193[.]166` |
| **First Seen** | 2026-10-31 04:50 |
| **Last Seen** | 2026-10-31 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:50:20` | `cowrie.session.connect` |
| `2026-10-31 04:50:20` | `cowrie.client.version` |
| `2026-10-31 04:50:20` | `cowrie.client.kex` |
| `2026-10-31 04:50:20` | `cowrie.login.success` |
| `2026-10-31 04:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.193[.]166` to AbuseIPDB if not already reported
- [ ] Block `50.6.193[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be502123bc01

| Field | Detail |
|---|---|
| **Source IP** | `20.40.44[.]6` |
| **First Seen** | 2026-10-31 04:50 |
| **Last Seen** | 2026-10-31 04:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:50:21` | `cowrie.session.connect` |
| `2026-10-31 04:50:21` | `cowrie.client.version` |
| `2026-10-31 04:50:21` | `cowrie.client.kex` |
| `2026-10-31 04:50:21` | `cowrie.login.success` |
| `2026-10-31 04:50:22` | `cowrie.session.params` |
| `2026-10-31 04:50:22` | `cowrie.command.input` |
| `2026-10-31 04:50:22` | `cowrie.command.failed` |
| `2026-10-31 04:50:23` | `cowrie.log.closed` |
| `2026-10-31 04:50:24` | `cowrie.session.params` |
| `2026-10-31 04:50:24` | `cowrie.command.input` |
| `2026-10-31 04:50:24` | `cowrie.session.file_download` |
| `2026-10-31 04:50:24` | `cowrie.log.closed` |
| `2026-10-31 04:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.40.44[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.40.44[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39f4227c302

| Field | Detail |
|---|---|
| **Source IP** | `20.40.44[.]6` |
| **First Seen** | 2026-10-31 04:50 |
| **Last Seen** | 2026-10-31 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-31 04:50:24` | `cowrie.session.connect` |
| `2026-10-31 04:50:24` | `cowrie.client.version` |
| `2026-10-31 04:50:24` | `cowrie.client.kex` |
| `2026-10-31 04:50:25` | `cowrie.login.success` |
| `2026-10-31 04:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.40.44[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.40.44[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (204) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-882ca1dccca6 | HIGH | `66.116.224[.]143` | 2026-10-31 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d4e161433830 | HIGH | `123.58.210[.]247` | 2026-10-31 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9696b3135a27 | HIGH | `66.116.224[.]143` | 2026-10-31 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-82b81b6d9e81 | HIGH | `123.58.210[.]247` | 2026-10-31 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a61e4abc1839 | HIGH | `117.247.23[.]131` | 2026-10-31 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d9226e056526 | HIGH | `117.247.23[.]131` | 2026-10-31 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80a1507159d9 | HIGH | `43.159.39[.]203` | 2026-10-31 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d9e6b82b2c4f | HIGH | `43.159.39[.]203` | 2026-10-31 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b699510ae25a | HIGH | `103.154.77[.]48` | 2026-10-31 04:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-beb66dd4cebc | HIGH | `103.154.77[.]48` | 2026-10-31 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd15e910f558 | HIGH | `187.212.13[.]248` | 2026-10-31 04:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-31e745818d8c | HIGH | `187.212.13[.]248` | 2026-10-31 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-27465a27742a | HIGH | `129.121.138[.]211` | 2026-10-31 04:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-75da49f15670 | HIGH | `129.121.138[.]211` | 2026-10-31 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b9ba2de44e62 | HIGH | `190.129.122[.]185` | 2026-10-31 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4e92bad865a8 | HIGH | `190.129.122[.]185` | 2026-10-31 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fff1a0aff47 | HIGH | `138.226.239[.]233` | 2026-10-31 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2aed8e4a5015 | HIGH | `92.118.39[.]77` | 2026-10-31 05:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9342d47e6855 | HIGH | `92.118.39[.]77` | 2026-10-31 05:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-458bbf33edac | HIGH | `92.118.39[.]77` | 2026-10-31 05:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-85352b301339 | HIGH | `92.118.39[.]77` | 2026-10-31 05:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7424935ae6e2 | HIGH | `92.118.39[.]77` | 2026-10-31 05:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1d96470df1a2 | HIGH | `92.118.39[.]77` | 2026-10-31 05:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-34765e55e390 | HIGH | `92.118.39[.]77` | 2026-10-31 05:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8883056fea4e | HIGH | `92.118.39[.]77` | 2026-10-31 05:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-199357bac85f | HIGH | `92.118.39[.]77` | 2026-10-31 05:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ffed3c4380fe | HIGH | `92.118.39[.]77` | 2026-10-31 05:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c1d3c33cbd3e | HIGH | `92.118.39[.]77` | 2026-10-31 05:25 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-65db7a6fbb83 | HIGH | `92.118.39[.]77` | 2026-10-31 05:28 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-17e3332bc863 | HIGH | `92.118.39[.]77` | 2026-10-31 05:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-3443bd3cd926 | HIGH | `92.118.39[.]77` | 2026-10-31 05:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9a1f0f5a1dec | HIGH | `35.210.235[.]198` | 2026-10-31 05:34 | Y | 2 | 0 | `T1078` |
| IR-8a89160aeac1 | HIGH | `35.210.235[.]198` | 2026-10-31 05:34 | Y | 1 | 0 | `T1078` |
| IR-2bf681796186 | HIGH | `35.210.235[.]198` | 2026-10-31 05:34 | Y | 0 | 0 | `T1078` |
| IR-26415cc5963d | HIGH | `92.118.39[.]77` | 2026-10-31 05:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8ad7ba13b6df | HIGH | `92.118.39[.]77` | 2026-10-31 05:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e30cd69c1b25 | HIGH | `92.118.39[.]77` | 2026-10-31 05:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e80cdb4605df | HIGH | `92.118.39[.]77` | 2026-10-31 05:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e553ceafff37 | HIGH | `92.118.39[.]77` | 2026-10-31 05:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-29abb5c5e731 | HIGH | `92.118.39[.]77` | 2026-10-31 05:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-aac2b5c042d1 | HIGH | `92.118.39[.]77` | 2026-10-31 05:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5baa5c1eddab | HIGH | `123.58.210[.]247` | 2026-10-31 06:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8ac71e40fc5f | HIGH | `123.58.210[.]247` | 2026-10-31 06:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9ad2883e44d3 | HIGH | `202.165.25[.]43` | 2026-10-31 06:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9668246865a2 | HIGH | `176.53.159[.]196` | 2026-10-31 06:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0665d8cb18b6 | HIGH | `202.165.25[.]43` | 2026-10-31 06:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6978b2c4b781 | HIGH | `201.17.146[.]173` | 2026-10-31 06:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-694cf97f8347 | HIGH | `201.17.146[.]173` | 2026-10-31 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9970e6255c5 | HIGH | `35.210.41[.]209` | 2026-10-31 06:11 | Y | 2 | 0 | `T1078` |
| IR-ee2a878d3ae4 | HIGH | `35.210.41[.]209` | 2026-10-31 06:11 | Y | 1 | 0 | `T1078` |
| IR-3878a1e5065b | HIGH | `35.210.41[.]209` | 2026-10-31 06:11 | Y | 0 | 0 | `T1078` |
| IR-77b907f6837e | HIGH | `35.210.8[.]195` | 2026-10-31 07:03 | Y | 2 | 0 | `T1078` |
| IR-1cca27effc9d | HIGH | `35.210.8[.]195` | 2026-10-31 07:03 | Y | 1 | 0 | `T1078` |
| IR-2f0c180bfad1 | HIGH | `35.210.8[.]195` | 2026-10-31 07:03 | Y | 0 | 0 | `T1078` |
| IR-76d479188446 | HIGH | `35.210.200[.]154` | 2026-10-31 07:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d63ec8a76e51 | HIGH | `197.5.145[.]150` | 2026-10-31 07:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a380460c574 | HIGH | `197.5.145[.]150` | 2026-10-31 07:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f78a50c51f7 | HIGH | `80.94.95[.]118` | 2026-10-31 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0285cb3cb16 | HIGH | `119.246.15[.]94` | 2026-10-31 07:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cf4cd4a46f73 | HIGH | `119.246.15[.]94` | 2026-10-31 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c2e20363978 | HIGH | `195.178.110[.]232` | 2026-10-31 07:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-12a663bd3fcb | HIGH | `195.178.110[.]232` | 2026-10-31 07:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-640f4b24007a | HIGH | `195.178.110[.]232` | 2026-10-31 07:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2583a6500de6 | HIGH | `195.178.110[.]232` | 2026-10-31 07:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-27a5aac4da04 | HIGH | `195.178.110[.]232` | 2026-10-31 07:57 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7a28fed50ed8 | HIGH | `195.178.110[.]232` | 2026-10-31 07:59 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cb9e015cee9f | HIGH | `46.6.124[.]199` | 2026-10-31 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d3ed558522a2 | HIGH | `46.6.124[.]199` | 2026-10-31 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2df5190367bc | HIGH | `115.190.181[.]18` | 2026-10-31 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6026e1df5362 | HIGH | `115.190.181[.]18` | 2026-10-31 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-386cfd499587 | HIGH | `195.178.110[.]232` | 2026-10-31 08:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d64dea8ed16a | HIGH | `172.214.209[.]153` | 2026-10-31 08:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-78eea1572dbb | HIGH | `172.214.209[.]153` | 2026-10-31 08:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05bd08d4be6b | HIGH | `59.36.75[.]227` | 2026-10-31 08:03 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-553e7070d67f | HIGH | `101.96.202[.]48` | 2026-10-31 08:04 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e4fbe35c3e00 | HIGH | `203.145.143[.]163` | 2026-10-31 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1e6e64d1d7a5 | HIGH | `203.145.143[.]163` | 2026-10-31 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4367f59fd057 | HIGH | `118.99.115[.]16` | 2026-10-31 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-432d17890570 | HIGH | `118.99.115[.]16` | 2026-10-31 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe72357942a7 | HIGH | `201.149.53[.]243` | 2026-10-31 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9ac4dce5d95c | HIGH | `201.149.53[.]243` | 2026-10-31 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a3189cca0af | HIGH | `129.121.115[.]165` | 2026-10-31 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1b1ccba440c9 | HIGH | `129.121.115[.]165` | 2026-10-31 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca241965c536 | HIGH | `195.178.110[.]232` | 2026-10-31 08:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-98cafc743de6 | HIGH | `165.154.147[.]69` | 2026-10-31 08:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-66723d5494bd | HIGH | `165.154.147[.]69` | 2026-10-31 08:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2106138baf6f | HIGH | `43.172.91[.]126` | 2026-10-31 08:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d940daa08174 | HIGH | `43.172.91[.]126` | 2026-10-31 08:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d30e421f9860 | HIGH | `50.6.171[.]219` | 2026-10-31 08:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2cb25946b0e2 | HIGH | `50.6.171[.]219` | 2026-10-31 08:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aee85e9060a9 | HIGH | `36.134.69[.]15` | 2026-10-31 08:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-374d03453210 | HIGH | `195.178.110[.]232` | 2026-10-31 08:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fe250cb492b9 | HIGH | `95.188.91[.]101` | 2026-10-31 08:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3cde7490f892 | HIGH | `182.79.112[.]190` | 2026-10-31 08:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c46d018e09ac | HIGH | `95.188.91[.]101` | 2026-10-31 08:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-419385ecc3a1 | HIGH | `182.79.112[.]190` | 2026-10-31 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-958ec5ea1202 | HIGH | `66.116.224[.]33` | 2026-10-31 08:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-936043ce11dc | HIGH | `222.220.102[.]32` | 2026-10-31 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60db557961e6 | HIGH | `66.116.224[.]33` | 2026-10-31 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-326126e6724c | HIGH | `102.88.137[.]80` | 2026-10-31 08:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 104 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **3** | 2026-10-31 02:56 | 2026-10-31 06:19 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-31 03:21 | 2026-10-31 06:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-31 08:25 | 2026-10-31 12:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-31 08:23 | 2026-10-31 10:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-10-31 07:37 | 2026-10-31 08:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.155.196[.]217` | **2** | 2026-10-31 11:35 | 2026-10-31 12:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]151` | **2** | 2026-10-31 11:31 | 2026-10-31 12:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.178.204[.]214` | 1 | 2026-10-31 13:38 | 2026-10-31 13:38 | 33s | 0 | `T1592` | 🟢 LOW |
| `104.168.85[.]59` | 1 | 2026-10-31 11:29 | 2026-10-31 11:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.176.110[.]197` | 1 | 2026-10-31 04:49 | 2026-10-31 04:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-10-31 08:07 | 2026-10-31 08:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-10-31 06:09 | 2026-10-31 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.145[.]176` | 1 | 2026-10-31 13:42 | 2026-10-31 13:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.89.185[.]26` | 1 | 2026-10-31 09:15 | 2026-10-31 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.110[.]18` | 1 | 2026-10-31 14:16 | 2026-10-31 14:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.194.228[.]101` | 1 | 2026-10-31 14:46 | 2026-10-31 14:47 | 11s | 0 | `T1592` | 🟢 LOW |
| `118.196.118[.]181` | 1 | 2026-10-31 08:46 | 2026-10-31 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.198.96[.]190` | 1 | 2026-10-31 14:13 | 2026-10-31 14:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.186.5[.]64` | 1 | 2026-10-31 04:12 | 2026-10-31 04:13 | 18s | 0 | `T1592` | 🟢 LOW |
| `134.33.66[.]242` | 1 | 2026-10-31 07:21 | 2026-10-31 07:21 | 9s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-31 12:26 | 2026-10-31 12:28 | 101s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-31 14:34 | 2026-10-31 14:35 | 48s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-31 14:27 | 2026-10-31 14:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.29.201[.]186` | 1 | 2026-10-31 08:44 | 2026-10-31 08:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-31 03:48 | 2026-10-31 03:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]239` | 1 | 2026-10-31 03:47 | 2026-10-31 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.205.251[.]191` | 1 | 2026-10-31 07:16 | 2026-10-31 07:16 | 26s | 0 | `T1592` | 🟢 LOW |
| `177.222.217[.]34` | 1 | 2026-10-31 10:09 | 2026-10-31 10:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-10-31 03:12 | 2026-10-31 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-31 10:01 | 2026-10-31 10:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-10-31 08:04 | 2026-10-31 08:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-10-31 11:32 | 2026-10-31 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.222.230[.]188` | 1 | 2026-10-31 04:52 | 2026-10-31 04:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.171.71[.]1` | 1 | 2026-10-31 04:22 | 2026-10-31 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-31 03:48 | 2026-10-31 03:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `188.95.93[.]18` | 1 | 2026-10-31 11:09 | 2026-10-31 11:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `191.101.96[.]217` | 1 | 2026-10-31 04:14 | 2026-10-31 04:15 | 18s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-10-31 10:09 | 2026-10-31 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.39.227[.]65` | 1 | 2026-10-31 09:45 | 2026-10-31 09:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]17` | 1 | 2026-10-31 04:03 | 2026-10-31 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]177` | 1 | 2026-10-31 11:36 | 2026-10-31 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.102.90[.]153` | 1 | 2026-10-31 09:05 | 2026-10-31 09:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.169.55[.]114` | 1 | 2026-10-31 11:21 | 2026-10-31 11:21 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]228` | 1 | 2026-10-31 10:37 | 2026-10-31 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.56.2[.]72` | 1 | 2026-10-31 10:28 | 2026-10-31 10:28 | 15s | 0 | `T1592` | 🟢 LOW |
| `203.89.28[.]114` | 1 | 2026-10-31 11:25 | 2026-10-31 11:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.154.203[.]31` | 1 | 2026-10-31 04:58 | 2026-10-31 04:59 | 20s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-10-31 08:07 | 2026-10-31 08:08 | 21s | 0 | `T1592` | 🟢 LOW |
| `211.54.230[.]146` | 1 | 2026-10-31 03:20 | 2026-10-31 03:20 | 23s | 0 | `T1592` | 🟢 LOW |
| `218.172.35[.]211` | 1 | 2026-10-31 03:53 | 2026-10-31 03:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `220.71.232[.]148` | 1 | 2026-10-31 07:59 | 2026-10-31 07:59 | 21s | 0 | `T1592` | 🟢 LOW |
| `220.87.110[.]141` | 1 | 2026-10-31 06:46 | 2026-10-31 06:46 | 28s | 0 | `T1592` | 🟢 LOW |
| `223.16.154[.]241` | 1 | 2026-10-31 02:55 | 2026-10-31 02:55 | 20s | 0 | `T1592` | 🟢 LOW |
| `27.17.30[.]150` | 1 | 2026-10-31 14:40 | 2026-10-31 14:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-31 11:45 | 2026-10-31 11:46 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.41.89[.]193` | 1 | 2026-10-31 11:32 | 2026-10-31 11:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.43.50[.]70` | 1 | 2026-10-31 10:22 | 2026-10-31 10:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.187.231[.]181` | 1 | 2026-10-31 04:31 | 2026-10-31 04:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.210.200[.]154` | 1 | 2026-10-31 07:10 | 2026-10-31 07:10 | 5s | 0 | `T1592` | 🟢 LOW |
| `35.210.235[.]198` | 1 | 2026-10-31 05:33 | 2026-10-31 05:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `35.210.41[.]209` | 1 | 2026-10-31 06:11 | 2026-10-31 06:11 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.210.45[.]130` | 1 | 2026-10-31 07:11 | 2026-10-31 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.8[.]195` | 1 | 2026-10-31 07:03 | 2026-10-31 07:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.134.69[.]15` | 1 | 2026-10-31 08:06 | 2026-10-31 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.186.51[.]88` | 1 | 2026-10-31 05:52 | 2026-10-31 05:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.232.180[.]223` | 1 | 2026-10-31 11:42 | 2026-10-31 11:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-10-31 04:04 | 2026-10-31 04:05 | 60s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-10-31 06:54 | 2026-10-31 06:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-10-31 11:12 | 2026-10-31 11:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `43.103.0[.]141` | 1 | 2026-10-31 07:39 | 2026-10-31 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.248.196[.]163` | 1 | 2026-10-31 11:53 | 2026-10-31 11:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-31 13:04 | 2026-10-31 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-31 04:04 | 2026-10-31 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-10-31 03:46 | 2026-10-31 03:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-10-31 09:36 | 2026-10-31 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]102` | 1 | 2026-10-31 03:54 | 2026-10-31 03:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.101.165[.]12` | 1 | 2026-10-31 04:58 | 2026-10-31 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.64.143[.]35` | 1 | 2026-10-31 07:22 | 2026-10-31 07:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-31 04:21 | 2026-10-31 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.49.26[.]202` | 1 | 2026-10-31 08:11 | 2026-10-31 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-10-31 06:03 | 2026-10-31 06:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.28.174[.]77` | 1 | 2026-10-31 13:26 | 2026-10-31 13:26 | 21s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-10-31 13:41 | 2026-10-31 13:41 | 16s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-10-31 14:54 | 2026-10-31 14:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.76.97[.]173` | 1 | 2026-10-31 03:34 | 2026-10-31 03:35 | 23s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-10-31 07:01 | 2026-10-31 07:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]143` | 1 | 2026-10-31 05:32 | 2026-10-31 05:32 | 22s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]31` | 1 | 2026-10-31 04:22 | 2026-10-31 04:22 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | 1 | 2026-10-31 06:34 | 2026-10-31 06:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | 1 | 2026-10-31 07:45 | 2026-10-31 07:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]75` | 1 | 2026-10-31 03:33 | 2026-10-31 03:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]80` | 1 | 2026-10-31 03:32 | 2026-10-31 03:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]204` | 1 | 2026-10-31 10:41 | 2026-10-31 10:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.235.138[.]110` | 1 | 2026-10-31 11:15 | 2026-10-31 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-31 06:04 | 2026-10-31 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-31 10:10 | 2026-10-31 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-31 11:06 | 2026-10-31 11:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.95.9[.]20` | 1 | 2026-10-31 03:43 | 2026-10-31 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-10-31 04:37 | 2026-10-31 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.211.150[.]32` | 1 | 2026-10-31 04:28 | 2026-10-31 04:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-31 08:57 | 2026-10-31 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-10-31 10:44 | 2026-10-31 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-10-31 10:45 | 2026-10-31 10:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.235.147[.]32` | 1 | 2026-10-31 10:01 | 2026-10-31 10:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-10-31 05:15 | 2026-10-31 05:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-10-31 08:04 | 2026-10-31 08:04 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `197.5.145[.]150` | TN | ATI - Agence Tunisienne Internet | **100** ⚠️ | 50 |
| `43.103.0[.]141` | HK | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 3 |
| `43.172.91[.]126` | US | ACEVILLE PTE.LTD. | **100** ⚠️ | 14 |
| `50.6.195[.]83` | US | Newfold Digital, Inc. | **100** ⚠️ | 5 |
| `85.217.149[.]56` | CA | Modat B.V. | **100** ⚠️ | 50 |
| `80.94.92[.]234` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `95.188.91[.]101` | RU | OJSC Rostelecom | **100** ⚠️ | 50 |
| `38.110.46[.]238` | US | Georgia Institute of Technology | **100** ⚠️ | 5 |
| `66.116.224[.]33` | IN | P.D.R Solutions FZC | **100** ⚠️ | 39 |
| `20.102.90[.]153` | US | Microsoft Corporation | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 258 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 233 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 117 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 73 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 49 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 381 cases |
| Tool 34  | Credential Extractor        | ✅ 1718 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 66 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 215 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 96 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 229 priority case(s) shown individually · 106 recon entry/entries in table (7 group(s) consolidating 17 session(s)).

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
_Report time: 2026-10-31T16:30:12Z_

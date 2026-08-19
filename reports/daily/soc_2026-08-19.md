# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T18:40:54Z |
| **Shift Time** | 18:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **487** |
| Confirmed Threats | **473** |
| False Positives Filtered | **14** (2.9%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **27** |
| High Severity Cases | **71** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **416** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **26** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **80** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `default` | 14 |
| `guest` | 8 |
| `admin` | 8 |
| `config` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 9 |
| `config2010` | 6 |
| `default2015` | 5 |
| `abc123` | 5 |
| `maintenance` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `config2010` | 6 |
| `default` | `default2015` | 5 |
| `default` | `abc123` | 5 |
| `unknown` | `maintenance` | 4 |
| `guest` | `guest2013` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `maintenance` | `10.0.0.73` | 2026-08-19T14:56:57 |
| `default` | `default2015` | `111.171.125.94` | 2026-08-19T14:57:06 |
| `root` | `1` | `110.173.190.221` | 2026-08-19T14:58:17 |
| `operator` | `operator2010` | `182.135.63.175` | 2026-08-19T14:58:29 |
| `unknown` | `maintenance` | `222.120.176.6` | 2026-08-19T14:58:32 |
| `operator` | `operator2010` | `65.20.141.202` | 2026-08-19T14:58:38 |
| `test` | `test` | `85.158.145.129` | 2026-08-19T14:58:40 |
| `forum` | `forum` | `85.158.145.129` | 2026-08-19T15:04:36 |
| `default` | `default2015` | `10.0.0.73` | 2026-08-19T15:08:44 |
| `freebsd` | `123456` | `85.158.145.129` | 2026-08-19T15:10:33 |
| `root` | `12` | `110.173.190.221` | 2026-08-19T15:10:46 |
| `guest` | `guest2013` | `10.0.0.73` | 2026-08-19T15:13:51 |
| `unknown` | `maintenance` | `62.183.82.70` | 2026-08-19T15:14:38 |
| `unknown` | `maintenance` | `65.20.233.110` | 2026-08-19T15:14:46 |
| `freebsd` | `freebsd` | `85.158.145.129` | 2026-08-19T15:16:30 |
| `ftp01` | `123456` | `85.158.145.129` | 2026-08-19T15:22:26 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `93.152.208.38` | 2026-08-19T15:23:04 |
| `root` | `123` | `110.173.190.221` | 2026-08-19T15:23:14 |
| `default` | `default2015` | `182.156.80.11` | 2026-08-19T15:25:46 |
| `default` | `default2015` | `200.159.14.187` | 2026-08-19T15:25:59 |
| `ftp01` | `ftp01` | `85.158.145.129` | 2026-08-19T15:28:23 |
| `admin` | `admin2020` | `203.75.170.63` | 2026-08-19T15:31:03 |
| `default` | `default2025` | `10.0.0.73` | 2026-08-19T15:31:04 |
| `guest` | `guest2013` | `178.214.160.4` | 2026-08-19T15:32:30 |
| `guest` | `guest2013` | `46.101.9.55` | 2026-08-19T15:32:36 |
| `guest` | `guest2013` | `203.198.173.145` | 2026-08-19T15:32:41 |
| `ftp1` | `123456` | `85.158.145.129` | 2026-08-19T15:34:20 |
| `root` | `1234` | `110.173.190.221` | 2026-08-19T15:35:46 |
| `ftp123` | `123456` | `85.158.145.129` | 2026-08-19T15:40:16 |
| `admin` | `admin2020` | `10.0.0.73` | 2026-08-19T15:42:36 |
| `ftp` | `123456` | `85.158.145.129` | 2026-08-19T15:46:13 |
| `default` | `abc123` | `10.0.0.73` | 2026-08-19T15:47:58 |
| `root` | `12345` | `110.173.190.221` | 2026-08-19T15:48:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-19T15:48:37 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-19T15:48:38 |
| `default` | `default2025` | `132.251.252.112` | 2026-08-19T15:48:58 |
| `default` | `default2025` | `39.183.162.243` | 2026-08-19T15:49:12 |
| `ftp123` | `ftp123` | `85.158.145.129` | 2026-08-19T15:52:10 |
| `ftp1` | `ftp1` | `85.158.145.129` | 2026-08-19T15:58:07 |
| `admin` | `admin2020` | `180.94.74.82` | 2026-08-19T15:59:41 |
| `ftp2` | `ftp2` | `85.158.145.129` | 2026-08-19T16:04:04 |
| `default` | `abc123` | `112.28.73.142` | 2026-08-19T16:06:18 |
| `default` | `abc123` | `124.239.129.2` | 2026-08-19T16:06:30 |
| `default` | `abc123` | `103.67.152.201` | 2026-08-19T16:06:34 |
| `admin` | `admin2021` | `181.212.174.166` | 2026-08-19T16:06:43 |
| `admin` | `admin2021` | `117.250.19.91` | 2026-08-19T16:07:02 |
| `ftpadm` | `ftpadm` | `85.158.145.129` | 2026-08-19T16:10:01 |
| `root` | `123321` | `110.173.190.221` | 2026-08-19T16:13:14 |
| `ftphome` | `123456` | `85.158.145.129` | 2026-08-19T16:15:58 |
| `blank` | `blank2013` | `10.0.0.73` | 2026-08-19T16:16:23 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T16:20:41 |
| `config` | `config2010` | `10.0.0.73` | 2026-08-19T16:21:35 |
| `brian` | `123` | `51.178.84.57` | 2026-08-19T16:21:47 |
| `345gs5662d34` | `345gs5662d34` | `51.178.84.57` | 2026-08-19T16:21:49 |
| `brian` | `3245gs5662d34` | `51.178.84.57` | 2026-08-19T16:21:50 |
| `ftpsecure` | `123456` | `85.158.145.129` | 2026-08-19T16:21:54 |
| `admin` | `admin2021` | `217.24.185.98` | 2026-08-19T16:22:38 |
| `admin` | `admin2021` | `61.169.54.150` | 2026-08-19T16:22:52 |
| `root` | `123123` | `110.173.190.221` | 2026-08-19T16:25:46 |
| `ftpsecure` | `ftpsecure` | `85.158.145.129` | 2026-08-19T16:27:51 |
| `blank` | `blank2013` | `112.194.142.167` | 2026-08-19T16:33:24 |
| `blank` | `blank2013` | `122.165.72.15` | 2026-08-19T16:33:33 |
| `ftpuser` | `123456` | `85.158.145.129` | 2026-08-19T16:33:47 |
| `root` | `1020` | `110.173.190.221` | 2026-08-19T16:38:16 |
| `support` | `support2013` | `123.123.196.140` | 2026-08-19T16:38:37 |
| `guest` | `guest2017` | `10.0.0.73` | 2026-08-19T16:38:58 |
| `ftpuser1` | `ftpuser1` | `85.158.145.129` | 2026-08-19T16:39:44 |
| `config` | `config2010` | `123.52.202.92` | 2026-08-19T16:39:57 |
| `config` | `config2010` | `195.222.57.183` | 2026-08-19T16:40:04 |
| `config` | `config2010` | `121.178.185.141` | 2026-08-19T16:40:08 |
| `config` | `config2010` | `125.35.109.214` | 2026-08-19T16:40:16 |
| `guest` | `guest2017` | `58.245.210.70` | 2026-08-19T16:40:33 |
| `guest` | `guest2017` | `65.20.158.10` | 2026-08-19T16:40:42 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T16:45:15 |
| `ftpuser` | `ftpuser` | `85.158.145.129` | 2026-08-19T16:45:41 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-19T16:47:54 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-19T16:47:56 |
| `support` | `support2013` | `10.0.0.73` | 2026-08-19T16:50:15 |
| `root` | `102030` | `110.173.190.221` | 2026-08-19T16:50:52 |
| `ftpusr` | `ftpusr` | `85.158.145.129` | 2026-08-19T16:51:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **487** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 32 |
| Go SSH scanner | 31 |
| libssh | 7 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
Source IPs: `51.178.84.57`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **56** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4808` | China Unicom Beijing Province Network | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (71)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-33616a9649ec

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-19 14:57 |
| **Last Seen** | 2026-08-19 14:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:57:03` | `cowrie.session.connect` |
| `2026-08-19 14:57:04` | `cowrie.client.version` |
| `2026-08-19 14:57:04` | `cowrie.client.kex` |
| `2026-08-19 14:57:06` | `cowrie.login.success` |
| `2026-08-19 14:57:07` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358bd0dd923a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 14:58 |
| **Last Seen** | 2026-08-19 14:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:58:08` | `cowrie.session.connect` |
| `2026-08-19 14:58:10` | `cowrie.client.version` |
| `2026-08-19 14:58:10` | `cowrie.client.kex` |
| `2026-08-19 14:58:17` | `cowrie.login.success` |
| `2026-08-19 14:58:21` | `cowrie.session.params` |
| `2026-08-19 14:58:21` | `cowrie.command.input` |
| `2026-08-19 14:58:22` | `cowrie.log.closed` |
| `2026-08-19 14:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b951dc0da27a

| Field | Detail |
|---|---|
| **Source IP** | `182.135.63[.]175` |
| **First Seen** | 2026-08-19 14:58 |
| **Last Seen** | 2026-08-19 14:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:58:25` | `cowrie.session.connect` |
| `2026-08-19 14:58:26` | `cowrie.client.version` |
| `2026-08-19 14:58:26` | `cowrie.client.kex` |
| `2026-08-19 14:58:29` | `cowrie.login.success` |
| `2026-08-19 14:58:30` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.135.63[.]175` to AbuseIPDB if not already reported
- [ ] Block `182.135.63[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00691c2dd0bc

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-08-19 14:58 |
| **Last Seen** | 2026-08-19 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:58:28` | `cowrie.session.connect` |
| `2026-08-19 14:58:29` | `cowrie.client.version` |
| `2026-08-19 14:58:29` | `cowrie.client.kex` |
| `2026-08-19 14:58:32` | `cowrie.login.success` |
| `2026-08-19 14:58:32` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3e0e4ea58b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-08-19 14:58 |
| **Last Seen** | 2026-08-19 14:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:58:35` | `cowrie.session.connect` |
| `2026-08-19 14:58:36` | `cowrie.client.version` |
| `2026-08-19 14:58:36` | `cowrie.client.kex` |
| `2026-08-19 14:58:38` | `cowrie.login.success` |
| `2026-08-19 14:58:38` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b469eac5f784

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:58 |
| **Last Seen** | 2026-08-19 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:58:39` | `cowrie.session.connect` |
| `2026-08-19 14:58:39` | `cowrie.client.version` |
| `2026-08-19 14:58:39` | `cowrie.client.kex` |
| `2026-08-19 14:58:40` | `cowrie.login.success` |
| `2026-08-19 14:58:40` | `cowrie.session.params` |
| `2026-08-19 14:58:40` | `cowrie.command.input` |
| `2026-08-19 14:58:41` | `cowrie.log.closed` |
| `2026-08-19 14:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f579d08bea4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:04 |
| **Last Seen** | 2026-08-19 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:04:36` | `cowrie.session.connect` |
| `2026-08-19 15:04:36` | `cowrie.client.version` |
| `2026-08-19 15:04:36` | `cowrie.client.kex` |
| `2026-08-19 15:04:36` | `cowrie.login.success` |
| `2026-08-19 15:04:37` | `cowrie.session.params` |
| `2026-08-19 15:04:37` | `cowrie.command.input` |
| `2026-08-19 15:04:37` | `cowrie.log.closed` |
| `2026-08-19 15:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a63e02787cd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:10 |
| **Last Seen** | 2026-08-19 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:10:32` | `cowrie.session.connect` |
| `2026-08-19 15:10:32` | `cowrie.client.version` |
| `2026-08-19 15:10:32` | `cowrie.client.kex` |
| `2026-08-19 15:10:33` | `cowrie.login.success` |
| `2026-08-19 15:10:33` | `cowrie.session.params` |
| `2026-08-19 15:10:33` | `cowrie.command.input` |
| `2026-08-19 15:10:34` | `cowrie.log.closed` |
| `2026-08-19 15:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce34249168c5

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 15:10 |
| **Last Seen** | 2026-08-19 15:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:10:37` | `cowrie.session.connect` |
| `2026-08-19 15:10:39` | `cowrie.client.version` |
| `2026-08-19 15:10:39` | `cowrie.client.kex` |
| `2026-08-19 15:10:46` | `cowrie.login.success` |
| `2026-08-19 15:10:50` | `cowrie.session.params` |
| `2026-08-19 15:10:50` | `cowrie.command.input` |
| `2026-08-19 15:10:51` | `cowrie.log.closed` |
| `2026-08-19 15:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef688796b7a0

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-08-19 15:14 |
| **Last Seen** | 2026-08-19 15:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:14:37` | `cowrie.session.connect` |
| `2026-08-19 15:14:37` | `cowrie.client.version` |
| `2026-08-19 15:14:37` | `cowrie.client.kex` |
| `2026-08-19 15:14:38` | `cowrie.login.success` |
| `2026-08-19 15:14:39` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52849d3f9b40

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-08-19 15:14 |
| **Last Seen** | 2026-08-19 15:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:14:44` | `cowrie.session.connect` |
| `2026-08-19 15:14:45` | `cowrie.client.version` |
| `2026-08-19 15:14:45` | `cowrie.client.kex` |
| `2026-08-19 15:14:46` | `cowrie.login.success` |
| `2026-08-19 15:14:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbee414bc9e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:16 |
| **Last Seen** | 2026-08-19 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:16:29` | `cowrie.session.connect` |
| `2026-08-19 15:16:29` | `cowrie.client.version` |
| `2026-08-19 15:16:29` | `cowrie.client.kex` |
| `2026-08-19 15:16:30` | `cowrie.login.success` |
| `2026-08-19 15:16:30` | `cowrie.session.params` |
| `2026-08-19 15:16:30` | `cowrie.command.input` |
| `2026-08-19 15:16:31` | `cowrie.log.closed` |
| `2026-08-19 15:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d54f57f7b75

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:22 |
| **Last Seen** | 2026-08-19 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:22:26` | `cowrie.session.connect` |
| `2026-08-19 15:22:26` | `cowrie.client.version` |
| `2026-08-19 15:22:26` | `cowrie.client.kex` |
| `2026-08-19 15:22:26` | `cowrie.login.success` |
| `2026-08-19 15:22:27` | `cowrie.session.params` |
| `2026-08-19 15:22:27` | `cowrie.command.input` |
| `2026-08-19 15:22:27` | `cowrie.log.closed` |
| `2026-08-19 15:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c21769464c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.208[.]38` |
| **First Seen** | 2026-08-19 15:23 |
| **Last Seen** | 2026-08-19 15:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7, Accept-Encoding: gzip, deflate, br, Accept-Language: en-US,en;q=0.9, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:23:04` | `cowrie.session.connect` |
| `2026-08-19 15:23:04` | `cowrie.login.success` |
| `2026-08-19 15:23:04` | `cowrie.session.params` |
| `2026-08-19 15:23:04` | `cowrie.command.input` |
| `2026-08-19 15:23:04` | `cowrie.command.input` |
| `2026-08-19 15:23:04` | `cowrie.command.failed` |
| `2026-08-19 15:23:05` | `cowrie.command.input` |
| `2026-08-19 15:23:05` | `cowrie.command.failed` |
| `2026-08-19 15:23:05` | `cowrie.command.input` |
| `2026-08-19 15:23:05` | `cowrie.command.failed` |
| `2026-08-19 15:23:05` | `cowrie.command.input` |
| `2026-08-19 15:23:05` | `cowrie.command.failed` |
| `2026-08-19 15:23:05` | `cowrie.command.input` |
| `2026-08-19 15:23:05` | `cowrie.log.closed` |
| `2026-08-19 15:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.208[.]38` to AbuseIPDB if not already reported
- [ ] Block `93.152.208[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0cf2ca34457

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 15:23 |
| **Last Seen** | 2026-08-19 15:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:23:06` | `cowrie.session.connect` |
| `2026-08-19 15:23:07` | `cowrie.client.version` |
| `2026-08-19 15:23:07` | `cowrie.client.kex` |
| `2026-08-19 15:23:14` | `cowrie.login.success` |
| `2026-08-19 15:23:18` | `cowrie.session.params` |
| `2026-08-19 15:23:18` | `cowrie.command.input` |
| `2026-08-19 15:23:20` | `cowrie.log.closed` |
| `2026-08-19 15:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9d7bbd0bcf

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-19 15:25 |
| **Last Seen** | 2026-08-19 15:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:25:43` | `cowrie.session.connect` |
| `2026-08-19 15:25:43` | `cowrie.client.version` |
| `2026-08-19 15:25:43` | `cowrie.client.kex` |
| `2026-08-19 15:25:46` | `cowrie.login.success` |
| `2026-08-19 15:25:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d65c7c0974

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-08-19 15:25 |
| **Last Seen** | 2026-08-19 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:25:57` | `cowrie.session.connect` |
| `2026-08-19 15:25:57` | `cowrie.client.version` |
| `2026-08-19 15:25:57` | `cowrie.client.kex` |
| `2026-08-19 15:25:59` | `cowrie.login.success` |
| `2026-08-19 15:26:00` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342317fe5372

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:28 |
| **Last Seen** | 2026-08-19 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:28:23` | `cowrie.session.connect` |
| `2026-08-19 15:28:23` | `cowrie.client.version` |
| `2026-08-19 15:28:23` | `cowrie.client.kex` |
| `2026-08-19 15:28:23` | `cowrie.login.success` |
| `2026-08-19 15:28:23` | `cowrie.session.params` |
| `2026-08-19 15:28:23` | `cowrie.command.input` |
| `2026-08-19 15:28:24` | `cowrie.log.closed` |
| `2026-08-19 15:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788b77f82de9

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-19 15:31 |
| **Last Seen** | 2026-08-19 15:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:31:00` | `cowrie.session.connect` |
| `2026-08-19 15:31:01` | `cowrie.client.version` |
| `2026-08-19 15:31:01` | `cowrie.client.kex` |
| `2026-08-19 15:31:03` | `cowrie.login.success` |
| `2026-08-19 15:31:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122e68dc2f7d

| Field | Detail |
|---|---|
| **Source IP** | `178.214.160[.]4` |
| **First Seen** | 2026-08-19 15:32 |
| **Last Seen** | 2026-08-19 15:32 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:32:19` | `cowrie.session.connect` |
| `2026-08-19 15:32:23` | `cowrie.client.version` |
| `2026-08-19 15:32:23` | `cowrie.client.kex` |
| `2026-08-19 15:32:30` | `cowrie.login.success` |
| `2026-08-19 15:32:34` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.214.160[.]4` to AbuseIPDB if not already reported
- [ ] Block `178.214.160[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5484b6d3b9d7

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-19 15:32 |
| **Last Seen** | 2026-08-19 15:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:32:35` | `cowrie.session.connect` |
| `2026-08-19 15:32:35` | `cowrie.client.version` |
| `2026-08-19 15:32:35` | `cowrie.client.kex` |
| `2026-08-19 15:32:36` | `cowrie.login.success` |
| `2026-08-19 15:32:36` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d369c8f66b

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]145` |
| **First Seen** | 2026-08-19 15:32 |
| **Last Seen** | 2026-08-19 15:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:32:38` | `cowrie.session.connect` |
| `2026-08-19 15:32:38` | `cowrie.client.version` |
| `2026-08-19 15:32:38` | `cowrie.client.kex` |
| `2026-08-19 15:32:41` | `cowrie.login.success` |
| `2026-08-19 15:32:41` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]145` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde082032087

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:34 |
| **Last Seen** | 2026-08-19 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:34:19` | `cowrie.session.connect` |
| `2026-08-19 15:34:19` | `cowrie.client.version` |
| `2026-08-19 15:34:19` | `cowrie.client.kex` |
| `2026-08-19 15:34:20` | `cowrie.login.success` |
| `2026-08-19 15:34:20` | `cowrie.session.params` |
| `2026-08-19 15:34:20` | `cowrie.command.input` |
| `2026-08-19 15:34:21` | `cowrie.log.closed` |
| `2026-08-19 15:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42d08c2d9fc

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 15:35 |
| **Last Seen** | 2026-08-19 15:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:35:38` | `cowrie.session.connect` |
| `2026-08-19 15:35:39` | `cowrie.client.version` |
| `2026-08-19 15:35:39` | `cowrie.client.kex` |
| `2026-08-19 15:35:46` | `cowrie.login.success` |
| `2026-08-19 15:35:50` | `cowrie.session.params` |
| `2026-08-19 15:35:50` | `cowrie.command.input` |
| `2026-08-19 15:35:52` | `cowrie.log.closed` |
| `2026-08-19 15:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9369b29c3f6

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:40 |
| **Last Seen** | 2026-08-19 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:40:16` | `cowrie.session.connect` |
| `2026-08-19 15:40:16` | `cowrie.client.version` |
| `2026-08-19 15:40:16` | `cowrie.client.kex` |
| `2026-08-19 15:40:16` | `cowrie.login.success` |
| `2026-08-19 15:40:17` | `cowrie.session.params` |
| `2026-08-19 15:40:17` | `cowrie.command.input` |
| `2026-08-19 15:40:17` | `cowrie.log.closed` |
| `2026-08-19 15:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91bfa1b9ce74

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:46 |
| **Last Seen** | 2026-08-19 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:46:13` | `cowrie.session.connect` |
| `2026-08-19 15:46:13` | `cowrie.client.version` |
| `2026-08-19 15:46:13` | `cowrie.client.kex` |
| `2026-08-19 15:46:13` | `cowrie.login.success` |
| `2026-08-19 15:46:14` | `cowrie.session.params` |
| `2026-08-19 15:46:14` | `cowrie.command.input` |
| `2026-08-19 15:46:14` | `cowrie.log.closed` |
| `2026-08-19 15:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3d60bee466

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 15:48 |
| **Last Seen** | 2026-08-19 15:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:48:08` | `cowrie.session.connect` |
| `2026-08-19 15:48:09` | `cowrie.client.version` |
| `2026-08-19 15:48:09` | `cowrie.client.kex` |
| `2026-08-19 15:48:16` | `cowrie.login.success` |
| `2026-08-19 15:48:20` | `cowrie.session.params` |
| `2026-08-19 15:48:20` | `cowrie.command.input` |
| `2026-08-19 15:48:22` | `cowrie.log.closed` |
| `2026-08-19 15:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d6f7a4f559

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 15:48 |
| **Last Seen** | 2026-08-19 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:48:36` | `cowrie.session.connect` |
| `2026-08-19 15:48:36` | `cowrie.client.version` |
| `2026-08-19 15:48:36` | `cowrie.client.kex` |
| `2026-08-19 15:48:37` | `cowrie.login.success` |
| `2026-08-19 15:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f398b8494f0f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 15:48 |
| **Last Seen** | 2026-08-19 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:48:37` | `cowrie.session.connect` |
| `2026-08-19 15:48:37` | `cowrie.client.version` |
| `2026-08-19 15:48:37` | `cowrie.client.kex` |
| `2026-08-19 15:48:38` | `cowrie.login.success` |
| `2026-08-19 15:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2802cf67245

| Field | Detail |
|---|---|
| **Source IP** | `132.251.252[.]112` |
| **First Seen** | 2026-08-19 15:48 |
| **Last Seen** | 2026-08-19 15:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:48:55` | `cowrie.session.connect` |
| `2026-08-19 15:48:56` | `cowrie.client.version` |
| `2026-08-19 15:48:56` | `cowrie.client.kex` |
| `2026-08-19 15:48:58` | `cowrie.login.success` |
| `2026-08-19 15:48:58` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.251.252[.]112` to AbuseIPDB if not already reported
- [ ] Block `132.251.252[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635020b1eafe

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-08-19 15:49 |
| **Last Seen** | 2026-08-19 15:49 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:49:05` | `cowrie.session.connect` |
| `2026-08-19 15:49:07` | `cowrie.client.version` |
| `2026-08-19 15:49:07` | `cowrie.client.kex` |
| `2026-08-19 15:49:12` | `cowrie.login.success` |
| `2026-08-19 15:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c36a3d6d09

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:52 |
| **Last Seen** | 2026-08-19 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:52:10` | `cowrie.session.connect` |
| `2026-08-19 15:52:10` | `cowrie.client.version` |
| `2026-08-19 15:52:10` | `cowrie.client.kex` |
| `2026-08-19 15:52:10` | `cowrie.login.success` |
| `2026-08-19 15:52:11` | `cowrie.session.params` |
| `2026-08-19 15:52:11` | `cowrie.command.input` |
| `2026-08-19 15:52:11` | `cowrie.log.closed` |
| `2026-08-19 15:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca81f35634e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 15:58 |
| **Last Seen** | 2026-08-19 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:58:07` | `cowrie.session.connect` |
| `2026-08-19 15:58:07` | `cowrie.client.version` |
| `2026-08-19 15:58:07` | `cowrie.client.kex` |
| `2026-08-19 15:58:07` | `cowrie.login.success` |
| `2026-08-19 15:58:08` | `cowrie.session.params` |
| `2026-08-19 15:58:08` | `cowrie.command.input` |
| `2026-08-19 15:58:08` | `cowrie.log.closed` |
| `2026-08-19 15:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260b7242a6f2

| Field | Detail |
|---|---|
| **Source IP** | `180.94.74[.]82` |
| **First Seen** | 2026-08-19 15:59 |
| **Last Seen** | 2026-08-19 15:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 15:59:39` | `cowrie.session.connect` |
| `2026-08-19 15:59:39` | `cowrie.client.version` |
| `2026-08-19 15:59:39` | `cowrie.client.kex` |
| `2026-08-19 15:59:41` | `cowrie.login.success` |
| `2026-08-19 15:59:41` | `cowrie.direct-tcpip.request` |
| `2026-08-19 15:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.74[.]82` to AbuseIPDB if not already reported
- [ ] Block `180.94.74[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52785403ad87

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:04 |
| **Last Seen** | 2026-08-19 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:04:04` | `cowrie.session.connect` |
| `2026-08-19 16:04:04` | `cowrie.client.version` |
| `2026-08-19 16:04:04` | `cowrie.client.kex` |
| `2026-08-19 16:04:04` | `cowrie.login.success` |
| `2026-08-19 16:04:05` | `cowrie.session.params` |
| `2026-08-19 16:04:05` | `cowrie.command.input` |
| `2026-08-19 16:04:05` | `cowrie.log.closed` |
| `2026-08-19 16:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b544f0764748

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-08-19 16:06 |
| **Last Seen** | 2026-08-19 16:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:06:14` | `cowrie.session.connect` |
| `2026-08-19 16:06:15` | `cowrie.client.version` |
| `2026-08-19 16:06:15` | `cowrie.client.kex` |
| `2026-08-19 16:06:18` | `cowrie.login.success` |
| `2026-08-19 16:06:20` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6857d075532

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-19 16:06 |
| **Last Seen** | 2026-08-19 16:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:06:26` | `cowrie.session.connect` |
| `2026-08-19 16:06:28` | `cowrie.client.version` |
| `2026-08-19 16:06:28` | `cowrie.client.kex` |
| `2026-08-19 16:06:30` | `cowrie.login.success` |
| `2026-08-19 16:06:31` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eccd29e0682

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-08-19 16:06 |
| **Last Seen** | 2026-08-19 16:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:06:31` | `cowrie.session.connect` |
| `2026-08-19 16:06:32` | `cowrie.client.version` |
| `2026-08-19 16:06:32` | `cowrie.client.kex` |
| `2026-08-19 16:06:34` | `cowrie.login.success` |
| `2026-08-19 16:06:35` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46bf7a31d33

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-19 16:06 |
| **Last Seen** | 2026-08-19 16:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:06:40` | `cowrie.session.connect` |
| `2026-08-19 16:06:41` | `cowrie.client.version` |
| `2026-08-19 16:06:41` | `cowrie.client.kex` |
| `2026-08-19 16:06:43` | `cowrie.login.success` |
| `2026-08-19 16:06:44` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda798cf6fe4

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-08-19 16:06 |
| **Last Seen** | 2026-08-19 16:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:06:50` | `cowrie.session.connect` |
| `2026-08-19 16:06:51` | `cowrie.client.version` |
| `2026-08-19 16:06:51` | `cowrie.client.kex` |
| `2026-08-19 16:07:02` | `cowrie.login.success` |
| `2026-08-19 16:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d9fe9aab20

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:10 |
| **Last Seen** | 2026-08-19 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:10:01` | `cowrie.session.connect` |
| `2026-08-19 16:10:01` | `cowrie.client.version` |
| `2026-08-19 16:10:01` | `cowrie.client.kex` |
| `2026-08-19 16:10:01` | `cowrie.login.success` |
| `2026-08-19 16:10:02` | `cowrie.session.params` |
| `2026-08-19 16:10:02` | `cowrie.command.input` |
| `2026-08-19 16:10:02` | `cowrie.log.closed` |
| `2026-08-19 16:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6068998bcd

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 16:13 |
| **Last Seen** | 2026-08-19 16:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:13:06` | `cowrie.session.connect` |
| `2026-08-19 16:13:07` | `cowrie.client.version` |
| `2026-08-19 16:13:07` | `cowrie.client.kex` |
| `2026-08-19 16:13:14` | `cowrie.login.success` |
| `2026-08-19 16:13:19` | `cowrie.session.params` |
| `2026-08-19 16:13:19` | `cowrie.command.input` |
| `2026-08-19 16:13:20` | `cowrie.log.closed` |
| `2026-08-19 16:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab96e94335f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:15 |
| **Last Seen** | 2026-08-19 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:15:57` | `cowrie.session.connect` |
| `2026-08-19 16:15:57` | `cowrie.client.version` |
| `2026-08-19 16:15:57` | `cowrie.client.kex` |
| `2026-08-19 16:15:58` | `cowrie.login.success` |
| `2026-08-19 16:15:59` | `cowrie.session.params` |
| `2026-08-19 16:15:59` | `cowrie.command.input` |
| `2026-08-19 16:15:59` | `cowrie.log.closed` |
| `2026-08-19 16:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4fc7813ccc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 16:20 |
| **Last Seen** | 2026-08-19 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:20:41` | `cowrie.session.connect` |
| `2026-08-19 16:20:41` | `cowrie.client.version` |
| `2026-08-19 16:20:41` | `cowrie.client.kex` |
| `2026-08-19 16:20:41` | `cowrie.login.success` |
| `2026-08-19 16:20:41` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:20:41` | `cowrie.direct-tcpip.data` |
| `2026-08-19 16:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d03d33c8e1

| Field | Detail |
|---|---|
| **Source IP** | `51.178.84[.]57` |
| **First Seen** | 2026-08-19 16:21 |
| **Last Seen** | 2026-08-19 16:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:21:46` | `cowrie.session.connect` |
| `2026-08-19 16:21:46` | `cowrie.client.version` |
| `2026-08-19 16:21:47` | `cowrie.client.kex` |
| `2026-08-19 16:21:47` | `cowrie.login.success` |
| `2026-08-19 16:21:48` | `cowrie.session.params` |
| `2026-08-19 16:21:48` | `cowrie.command.input` |
| `2026-08-19 16:21:48` | `cowrie.command.failed` |
| `2026-08-19 16:21:48` | `cowrie.log.closed` |
| `2026-08-19 16:21:49` | `cowrie.session.params` |
| `2026-08-19 16:21:49` | `cowrie.command.input` |
| `2026-08-19 16:21:49` | `cowrie.session.file_download` |
| `2026-08-19 16:21:49` | `cowrie.log.closed` |
| `2026-08-19 16:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.84[.]57` to AbuseIPDB if not already reported
- [ ] Block `51.178.84[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e126cbd01af

| Field | Detail |
|---|---|
| **Source IP** | `51.178.84[.]57` |
| **First Seen** | 2026-08-19 16:21 |
| **Last Seen** | 2026-08-19 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:21:49` | `cowrie.session.connect` |
| `2026-08-19 16:21:49` | `cowrie.client.version` |
| `2026-08-19 16:21:49` | `cowrie.client.kex` |
| `2026-08-19 16:21:49` | `cowrie.login.success` |
| `2026-08-19 16:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.84[.]57` to AbuseIPDB if not already reported
- [ ] Block `51.178.84[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9dfe835ec42

| Field | Detail |
|---|---|
| **Source IP** | `51.178.84[.]57` |
| **First Seen** | 2026-08-19 16:21 |
| **Last Seen** | 2026-08-19 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:21:49` | `cowrie.session.connect` |
| `2026-08-19 16:21:49` | `cowrie.client.version` |
| `2026-08-19 16:21:49` | `cowrie.client.kex` |
| `2026-08-19 16:21:50` | `cowrie.login.success` |
| `2026-08-19 16:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.84[.]57` to AbuseIPDB if not already reported
- [ ] Block `51.178.84[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a661bb1e5a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:21 |
| **Last Seen** | 2026-08-19 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:21:54` | `cowrie.session.connect` |
| `2026-08-19 16:21:54` | `cowrie.client.version` |
| `2026-08-19 16:21:54` | `cowrie.client.kex` |
| `2026-08-19 16:21:54` | `cowrie.login.success` |
| `2026-08-19 16:21:55` | `cowrie.session.params` |
| `2026-08-19 16:21:55` | `cowrie.command.input` |
| `2026-08-19 16:21:55` | `cowrie.log.closed` |
| `2026-08-19 16:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9821d16b3ec3

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-19 16:22 |
| **Last Seen** | 2026-08-19 16:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:22:36` | `cowrie.session.connect` |
| `2026-08-19 16:22:37` | `cowrie.client.version` |
| `2026-08-19 16:22:37` | `cowrie.client.kex` |
| `2026-08-19 16:22:38` | `cowrie.login.success` |
| `2026-08-19 16:22:39` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d283d1ac52

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-19 16:22 |
| **Last Seen** | 2026-08-19 16:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:22:48` | `cowrie.session.connect` |
| `2026-08-19 16:22:50` | `cowrie.client.version` |
| `2026-08-19 16:22:50` | `cowrie.client.kex` |
| `2026-08-19 16:22:52` | `cowrie.login.success` |
| `2026-08-19 16:22:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d2ca9b1915f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 16:25 |
| **Last Seen** | 2026-08-19 16:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:25:37` | `cowrie.session.connect` |
| `2026-08-19 16:25:40` | `cowrie.client.version` |
| `2026-08-19 16:25:40` | `cowrie.client.kex` |
| `2026-08-19 16:25:46` | `cowrie.login.success` |
| `2026-08-19 16:25:50` | `cowrie.session.params` |
| `2026-08-19 16:25:50` | `cowrie.command.input` |
| `2026-08-19 16:25:51` | `cowrie.log.closed` |
| `2026-08-19 16:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c65f9a42ade

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:27 |
| **Last Seen** | 2026-08-19 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:27:50` | `cowrie.session.connect` |
| `2026-08-19 16:27:50` | `cowrie.client.version` |
| `2026-08-19 16:27:51` | `cowrie.client.kex` |
| `2026-08-19 16:27:51` | `cowrie.login.success` |
| `2026-08-19 16:27:52` | `cowrie.session.params` |
| `2026-08-19 16:27:52` | `cowrie.command.input` |
| `2026-08-19 16:27:52` | `cowrie.log.closed` |
| `2026-08-19 16:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb1cb941a3c

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-08-19 16:33 |
| **Last Seen** | 2026-08-19 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:33:20` | `cowrie.session.connect` |
| `2026-08-19 16:33:21` | `cowrie.client.version` |
| `2026-08-19 16:33:21` | `cowrie.client.kex` |
| `2026-08-19 16:33:24` | `cowrie.login.success` |
| `2026-08-19 16:33:25` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5aecf2cc752

| Field | Detail |
|---|---|
| **Source IP** | `122.165.72[.]15` |
| **First Seen** | 2026-08-19 16:33 |
| **Last Seen** | 2026-08-19 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:33:30` | `cowrie.session.connect` |
| `2026-08-19 16:33:31` | `cowrie.client.version` |
| `2026-08-19 16:33:31` | `cowrie.client.kex` |
| `2026-08-19 16:33:33` | `cowrie.login.success` |
| `2026-08-19 16:33:34` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.165.72[.]15` to AbuseIPDB if not already reported
- [ ] Block `122.165.72[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e794fbb0333

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:33 |
| **Last Seen** | 2026-08-19 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:33:47` | `cowrie.session.connect` |
| `2026-08-19 16:33:47` | `cowrie.client.version` |
| `2026-08-19 16:33:47` | `cowrie.client.kex` |
| `2026-08-19 16:33:47` | `cowrie.login.success` |
| `2026-08-19 16:33:48` | `cowrie.session.params` |
| `2026-08-19 16:33:48` | `cowrie.command.input` |
| `2026-08-19 16:33:48` | `cowrie.log.closed` |
| `2026-08-19 16:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb2955ad781

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 16:38 |
| **Last Seen** | 2026-08-19 16:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:38:08` | `cowrie.session.connect` |
| `2026-08-19 16:38:09` | `cowrie.client.version` |
| `2026-08-19 16:38:09` | `cowrie.client.kex` |
| `2026-08-19 16:38:16` | `cowrie.login.success` |
| `2026-08-19 16:38:19` | `cowrie.session.params` |
| `2026-08-19 16:38:19` | `cowrie.command.input` |
| `2026-08-19 16:38:21` | `cowrie.log.closed` |
| `2026-08-19 16:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7e9d919f8e

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-19 16:38 |
| **Last Seen** | 2026-08-19 16:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:38:34` | `cowrie.session.connect` |
| `2026-08-19 16:38:35` | `cowrie.client.version` |
| `2026-08-19 16:38:35` | `cowrie.client.kex` |
| `2026-08-19 16:38:37` | `cowrie.login.success` |
| `2026-08-19 16:38:38` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbc1db25c9b

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:39 |
| **Last Seen** | 2026-08-19 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:39:44` | `cowrie.session.connect` |
| `2026-08-19 16:39:44` | `cowrie.client.version` |
| `2026-08-19 16:39:44` | `cowrie.client.kex` |
| `2026-08-19 16:39:44` | `cowrie.login.success` |
| `2026-08-19 16:39:45` | `cowrie.session.params` |
| `2026-08-19 16:39:45` | `cowrie.command.input` |
| `2026-08-19 16:39:45` | `cowrie.log.closed` |
| `2026-08-19 16:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8232ab26abbb

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-19 16:39 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:39:52` | `cowrie.session.connect` |
| `2026-08-19 16:39:54` | `cowrie.client.version` |
| `2026-08-19 16:39:54` | `cowrie.client.kex` |
| `2026-08-19 16:39:57` | `cowrie.login.success` |
| `2026-08-19 16:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdd19ac4959

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-19 16:40 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:40:03` | `cowrie.session.connect` |
| `2026-08-19 16:40:04` | `cowrie.client.version` |
| `2026-08-19 16:40:04` | `cowrie.client.kex` |
| `2026-08-19 16:40:04` | `cowrie.login.success` |
| `2026-08-19 16:40:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37b4917fc1c

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-19 16:40 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:40:04` | `cowrie.session.connect` |
| `2026-08-19 16:40:05` | `cowrie.client.version` |
| `2026-08-19 16:40:05` | `cowrie.client.kex` |
| `2026-08-19 16:40:08` | `cowrie.login.success` |
| `2026-08-19 16:40:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff30def8b04a

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-08-19 16:40 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:40:14` | `cowrie.session.connect` |
| `2026-08-19 16:40:14` | `cowrie.client.version` |
| `2026-08-19 16:40:14` | `cowrie.client.kex` |
| `2026-08-19 16:40:16` | `cowrie.login.success` |
| `2026-08-19 16:40:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7b7a4e9484

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-19 16:40 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:40:30` | `cowrie.session.connect` |
| `2026-08-19 16:40:30` | `cowrie.client.version` |
| `2026-08-19 16:40:30` | `cowrie.client.kex` |
| `2026-08-19 16:40:33` | `cowrie.login.success` |
| `2026-08-19 16:40:34` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e77ca735a7b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-19 16:40 |
| **Last Seen** | 2026-08-19 16:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:40:40` | `cowrie.session.connect` |
| `2026-08-19 16:40:40` | `cowrie.client.version` |
| `2026-08-19 16:40:40` | `cowrie.client.kex` |
| `2026-08-19 16:40:42` | `cowrie.login.success` |
| `2026-08-19 16:40:43` | `cowrie.direct-tcpip.request` |
| `2026-08-19 16:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d41e3d61bd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:45 |
| **Last Seen** | 2026-08-19 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:45:40` | `cowrie.session.connect` |
| `2026-08-19 16:45:40` | `cowrie.client.version` |
| `2026-08-19 16:45:40` | `cowrie.client.kex` |
| `2026-08-19 16:45:41` | `cowrie.login.success` |
| `2026-08-19 16:45:41` | `cowrie.session.params` |
| `2026-08-19 16:45:41` | `cowrie.command.input` |
| `2026-08-19 16:45:41` | `cowrie.log.closed` |
| `2026-08-19 16:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168332158c96

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 16:47 |
| **Last Seen** | 2026-08-19 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:47:53` | `cowrie.session.connect` |
| `2026-08-19 16:47:53` | `cowrie.client.version` |
| `2026-08-19 16:47:53` | `cowrie.client.kex` |
| `2026-08-19 16:47:54` | `cowrie.login.success` |
| `2026-08-19 16:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f03c06e1d6

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 16:47 |
| **Last Seen** | 2026-08-19 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:47:55` | `cowrie.session.connect` |
| `2026-08-19 16:47:55` | `cowrie.client.version` |
| `2026-08-19 16:47:55` | `cowrie.client.kex` |
| `2026-08-19 16:47:56` | `cowrie.login.success` |
| `2026-08-19 16:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72649ba050e

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 16:48 |
| **Last Seen** | 2026-08-19 16:50 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:48:02` | `cowrie.session.connect` |
| `2026-08-19 16:48:02` | `cowrie.client.version` |
| `2026-08-19 16:48:02` | `cowrie.client.kex` |
| `2026-08-19 16:48:02` | `cowrie.login.success` |
| `2026-08-19 16:48:03` | `cowrie.session.file_upload` |
| `2026-08-19 16:48:04` | `cowrie.session.params` |
| `2026-08-19 16:48:04` | `cowrie.command.input` |
| `2026-08-19 16:48:04` | `cowrie.command.input` |
| `2026-08-19 16:48:04` | `cowrie.command.input` |
| `2026-08-19 16:48:04` | `cowrie.command.failed` |
| `2026-08-19 16:48:04` | `cowrie.log.closed` |
| `2026-08-19 16:48:05` | `cowrie.session.params` |
| `2026-08-19 16:48:05` | `cowrie.command.input` |
| `2026-08-19 16:48:05` | `cowrie.log.closed` |
| `2026-08-19 16:48:06` | `cowrie.session.params` |
| `2026-08-19 16:48:06` | `cowrie.command.input` |
| `2026-08-19 16:48:06` | `cowrie.log.closed` |
| `2026-08-19 16:48:06` | `cowrie.session.params` |
| `2026-08-19 16:48:06` | `cowrie.command.input` |
| `2026-08-19 16:48:06` | `cowrie.command.failed` |
| `2026-08-19 16:48:06` | `cowrie.command.failed` |
| `2026-08-19 16:49:07` | `cowrie.session.params` |
| `2026-08-19 16:49:07` | `cowrie.command.input` |
| `2026-08-19 16:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a937fe25d5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 16:50 |
| **Last Seen** | 2026-08-19 16:52 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:50:08` | `cowrie.session.connect` |
| `2026-08-19 16:50:08` | `cowrie.client.version` |
| `2026-08-19 16:50:08` | `cowrie.client.kex` |
| `2026-08-19 16:50:08` | `cowrie.login.success` |
| `2026-08-19 16:50:09` | `cowrie.session.file_upload` |
| `2026-08-19 16:50:10` | `cowrie.session.params` |
| `2026-08-19 16:50:10` | `cowrie.command.input` |
| `2026-08-19 16:50:10` | `cowrie.command.input` |
| `2026-08-19 16:50:10` | `cowrie.command.input` |
| `2026-08-19 16:50:10` | `cowrie.command.failed` |
| `2026-08-19 16:50:10` | `cowrie.log.closed` |
| `2026-08-19 16:50:11` | `cowrie.session.params` |
| `2026-08-19 16:50:11` | `cowrie.command.input` |
| `2026-08-19 16:50:11` | `cowrie.log.closed` |
| `2026-08-19 16:50:12` | `cowrie.session.params` |
| `2026-08-19 16:50:12` | `cowrie.command.input` |
| `2026-08-19 16:50:12` | `cowrie.log.closed` |
| `2026-08-19 16:50:13` | `cowrie.session.params` |
| `2026-08-19 16:50:13` | `cowrie.command.input` |
| `2026-08-19 16:50:13` | `cowrie.command.failed` |
| `2026-08-19 16:50:13` | `cowrie.command.failed` |
| `2026-08-19 16:51:13` | `cowrie.session.params` |
| `2026-08-19 16:51:13` | `cowrie.command.input` |
| `2026-08-19 16:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2dd8e9fff3c

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 16:50 |
| **Last Seen** | 2026-08-19 16:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:50:45` | `cowrie.session.connect` |
| `2026-08-19 16:50:46` | `cowrie.client.version` |
| `2026-08-19 16:50:46` | `cowrie.client.kex` |
| `2026-08-19 16:50:52` | `cowrie.login.success` |
| `2026-08-19 16:50:56` | `cowrie.session.params` |
| `2026-08-19 16:50:56` | `cowrie.command.input` |
| `2026-08-19 16:50:58` | `cowrie.log.closed` |
| `2026-08-19 16:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab7101e18a3

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 16:51 |
| **Last Seen** | 2026-08-19 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 16:51:37` | `cowrie.session.connect` |
| `2026-08-19 16:51:37` | `cowrie.client.version` |
| `2026-08-19 16:51:37` | `cowrie.client.kex` |
| `2026-08-19 16:51:37` | `cowrie.login.success` |
| `2026-08-19 16:51:38` | `cowrie.session.params` |
| `2026-08-19 16:51:38` | `cowrie.command.input` |
| `2026-08-19 16:51:38` | `cowrie.log.closed` |
| `2026-08-19 16:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **376** | 2026-08-19 14:55 | 2026-08-19 16:54 | 465m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-19 15:16 | 2026-08-19 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.180.22[.]170` | **2** | 2026-08-19 15:35 | 2026-08-19 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.204.148[.]68` | **2** | 2026-08-19 16:20 | 2026-08-19 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | **2** | 2026-08-19 14:58 | 2026-08-19 15:00 | 4m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-19 16:32 | 2026-08-19 16:33 | 37s | 0 | `T1592` | 🟢 LOW |
| `110.173.190[.]221` | 1 | 2026-08-19 16:00 | 2026-08-19 16:00 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.229[.]201` | 1 | 2026-08-19 15:59 | 2026-08-19 16:00 | 14s | 0 | `T1592` | 🟢 LOW |
| `137.175.205[.]63` | 1 | 2026-08-19 15:36 | 2026-08-19 15:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.197.128[.]253` | 1 | 2026-08-19 16:46 | 2026-08-19 16:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.106.29[.]187` | 1 | 2026-08-19 16:27 | 2026-08-19 16:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `186.239.41[.]74` | 1 | 2026-08-19 14:59 | 2026-08-19 14:59 | 1s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-08-19 16:02 | 2026-08-19 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-19 15:02 | 2026-08-19 15:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]54` | 1 | 2026-08-19 16:38 | 2026-08-19 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-19 14:57 | 2026-08-19 14:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-08-19 15:30 | 2026-08-19 15:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-08-19 15:32 | 2026-08-19 15:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]96` | 1 | 2026-08-19 15:18 | 2026-08-19 15:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-19 15:37 | 2026-08-19 15:39 | 74s | 0 | `T1592` | 🟢 LOW |
| `93.152.208[.]38` | 1 | 2026-08-19 15:23 | 2026-08-19 15:23 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `102.204.148[.]68` | KE | KONNEKT Smart Life LTD | **100** ⚠️ | 3 |
| `83.226.181[.]38` | SE | Telenor Sverige AB | **100** ⚠️ | 34 |
| `85.158.145[.]129` | NL | cukman-kresimir | **100** ⚠️ | 0 |
| `112.28.73[.]142` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `178.214.160[.]4` | UA | Likhno Dmitriy trading as Luganet | **100** ⚠️ | 9 |
| `186.239.41[.]74` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `46.101.9[.]55` | GB | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `65.20.158[.]10` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 78 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 71 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 487 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (2.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 71 priority case(s) shown individually · 21 recon entry/entries in table (5 group(s) consolidating 386 session(s)).

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
_Report time: 2026-08-19T18:40:54Z_

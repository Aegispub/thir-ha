# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-16 |
| **Generated At** | 2026-07-16T19:18:34Z |
| **Shift Time** | 19:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **194** |
| Confirmed Threats | **173** |
| False Positives Filtered | **21** (10.8%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **21** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **157** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **13** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `test` | 12 |
| `support` | 8 |
| `admin` | 6 |
| `user` | 6 |
| `root` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `administrator` | 6 |
| `123123123` | 5 |
| `support` | 4 |
| `net` | 4 |
| `jenkins` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `administrator` | 6 |
| `user` | `123123123` | 5 |
| `support` | `support` | 4 |
| `net` | `net` | 4 |
| `jenkins` | `jenkins` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `qwerty01` | `124.133.10.66` | 2026-07-16T16:58:06 |
| `admin` | `qwerty01` | `65.20.141.202` | 2026-07-16T16:58:19 |
| `support` | `support` | `176.53.159.196` | 2026-07-16T16:58:19 |
| `admin` | `qwerty01` | `10.0.0.73` | 2026-07-16T16:58:34 |
| `support` | `support` | `10.0.0.73` | 2026-07-16T16:59:41 |
| `test` | `qwerty1234` | `62.182.132.94` | 2026-07-16T17:13:43 |
| `test` | `qwerty1234` | `10.0.0.73` | 2026-07-16T17:17:18 |
| `admin` | `zhone` | `49.124.151.62` | 2026-07-16T17:19:41 |
| `admin` | `zhone` | `201.63.52.54` | 2026-07-16T17:22:55 |
| `admin` | `zhone` | `211.247.127.250` | 2026-07-16T17:23:03 |
| `ubuntu` | `q1w2e3` | `185.242.3.195` | 2026-07-16T17:27:16 |
| `support` | `support55` | `122.166.253.226` | 2026-07-16T17:31:29 |
| `support` | `support55` | `182.76.36.62` | 2026-07-16T17:35:12 |
| `support` | `support55` | `10.0.0.73` | 2026-07-16T17:35:24 |
| `user` | `123123123` | `222.186.68.153` | 2026-07-16T17:38:28 |
| `ubuntu` | `q1w2e3` | `10.0.0.73` | 2026-07-16T17:40:41 |
| `root` | `ADMIN` | `103.61.122.229` | 2026-07-16T17:41:46 |
| `user` | `123123123` | `112.120.115.152` | 2026-07-16T17:41:55 |
| `user` | `123123123` | `146.190.215.195` | 2026-07-16T17:42:02 |
| `user` | `123123123` | `10.0.0.73` | 2026-07-16T17:42:18 |
| `user` | `112233` | `10.0.0.73` | 2026-07-16T17:48:25 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-16T17:53:43 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-16T17:53:44 |
| `net` | `net` | `111.70.39.214` | 2026-07-16T17:56:52 |
| `net` | `net` | `112.27.38.203` | 2026-07-16T17:57:06 |
| `net` | `net` | `10.0.0.73` | 2026-07-16T18:00:30 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-16T18:04:20 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-16T18:04:20 |
| `test` | `0000` | `177.135.206.10` | 2026-07-16T18:06:34 |
| `test` | `0000` | `10.0.0.73` | 2026-07-16T18:06:58 |
| `support` | `qwerty12345` | `78.187.9.111` | 2026-07-16T18:12:38 |
| `yuqisun` | `yuqisun` | `185.242.3.195` | 2026-07-16T18:18:45 |
| `jenkins` | `jenkins` | `49.124.152.30` | 2026-07-16T18:21:36 |
| `jenkins` | `jenkins` | `60.220.241.50` | 2026-07-16T18:21:44 |
| `sam` | `sam` | `101.96.231.24` | 2026-07-16T18:22:10 |
| `345gs5662d34` | `345gs5662d34` | `101.96.231.24` | 2026-07-16T18:22:14 |
| `sam` | `3245gs5662d34` | `101.96.231.24` | 2026-07-16T18:22:16 |
| `jenkins` | `jenkins` | `10.0.0.73` | 2026-07-16T18:25:29 |
| `test` | `administrator` | `94.205.250.78` | 2026-07-16T18:27:58 |
| `test` | `administrator` | `188.43.204.45` | 2026-07-16T18:28:10 |
| `test` | `administrator` | `178.178.222.58` | 2026-07-16T18:31:25 |
| `test` | `administrator` | `112.196.52.107` | 2026-07-16T18:31:38 |
| `test` | `administrator` | `10.0.0.73` | 2026-07-16T18:31:46 |
| `yuqisun` | `yuqisun` | `10.0.0.73` | 2026-07-16T18:32:22 |
| `administrator` | `admin` | `104.152.58.233` | 2026-07-16T18:37:28 |
| `administrator` | `admin` | `10.0.0.73` | 2026-07-16T18:37:51 |
| `ubuntu` | `ADMIN` | `103.61.122.229` | 2026-07-16T18:41:35 |
| `gast` | `gast` | `10.0.0.73` | 2026-07-16T18:50:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **194** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 28 |
| Go SSH scanner | 10 |
| Paramiko (Python) | 5 |
| libssh | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `16443846184e...` | Generic scanner | 6 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `101.96.231.24`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **47** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS213790` | Limited Network LTD | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a3a937974f41

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-07-16 16:58 |
| **Last Seen** | 2026-07-16 16:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 16:58:04` | `cowrie.session.connect` |
| `2026-07-16 16:58:04` | `cowrie.client.version` |
| `2026-07-16 16:58:04` | `cowrie.client.kex` |
| `2026-07-16 16:58:06` | `cowrie.login.success` |
| `2026-07-16 16:58:07` | `cowrie.direct-tcpip.request` |
| `2026-07-16 16:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c416be60f07

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-16 16:58 |
| **Last Seen** | 2026-07-16 16:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 16:58:17` | `cowrie.session.connect` |
| `2026-07-16 16:58:18` | `cowrie.client.version` |
| `2026-07-16 16:58:18` | `cowrie.client.kex` |
| `2026-07-16 16:58:19` | `cowrie.login.success` |
| `2026-07-16 16:58:19` | `cowrie.direct-tcpip.request` |
| `2026-07-16 16:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f2c8572cf0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 16:58 |
| **Last Seen** | 2026-07-16 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 16:58:19` | `cowrie.session.connect` |
| `2026-07-16 16:58:19` | `cowrie.client.version` |
| `2026-07-16 16:58:19` | `cowrie.client.kex` |
| `2026-07-16 16:58:19` | `cowrie.login.success` |
| `2026-07-16 16:58:20` | `cowrie.direct-tcpip.request` |
| `2026-07-16 16:58:20` | `cowrie.direct-tcpip.data` |
| `2026-07-16 16:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e62fcdecc13

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-16 17:13 |
| **Last Seen** | 2026-07-16 17:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:13:42` | `cowrie.session.connect` |
| `2026-07-16 17:13:42` | `cowrie.client.version` |
| `2026-07-16 17:13:42` | `cowrie.client.kex` |
| `2026-07-16 17:13:43` | `cowrie.login.success` |
| `2026-07-16 17:13:44` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d1976073cb

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]62` |
| **First Seen** | 2026-07-16 17:19 |
| **Last Seen** | 2026-07-16 17:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:19:38` | `cowrie.session.connect` |
| `2026-07-16 17:19:38` | `cowrie.client.version` |
| `2026-07-16 17:19:38` | `cowrie.client.kex` |
| `2026-07-16 17:19:41` | `cowrie.login.success` |
| `2026-07-16 17:19:41` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]62` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a0a5eb811e

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-16 17:22 |
| **Last Seen** | 2026-07-16 17:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:22:52` | `cowrie.session.connect` |
| `2026-07-16 17:22:53` | `cowrie.client.version` |
| `2026-07-16 17:22:53` | `cowrie.client.kex` |
| `2026-07-16 17:22:55` | `cowrie.login.success` |
| `2026-07-16 17:22:55` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53b29568cc2

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-16 17:23 |
| **Last Seen** | 2026-07-16 17:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:23:00` | `cowrie.session.connect` |
| `2026-07-16 17:23:01` | `cowrie.client.version` |
| `2026-07-16 17:23:01` | `cowrie.client.kex` |
| `2026-07-16 17:23:03` | `cowrie.login.success` |
| `2026-07-16 17:23:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf8d43b9bbc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 17:27 |
| **Last Seen** | 2026-07-16 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:27:16` | `cowrie.session.connect` |
| `2026-07-16 17:27:16` | `cowrie.client.version` |
| `2026-07-16 17:27:16` | `cowrie.client.kex` |
| `2026-07-16 17:27:16` | `cowrie.login.success` |
| `2026-07-16 17:27:17` | `cowrie.session.params` |
| `2026-07-16 17:27:17` | `cowrie.command.input` |
| `2026-07-16 17:27:17` | `cowrie.log.closed` |
| `2026-07-16 17:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570662411480

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-16 17:31 |
| **Last Seen** | 2026-07-16 17:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:31:26` | `cowrie.session.connect` |
| `2026-07-16 17:31:27` | `cowrie.client.version` |
| `2026-07-16 17:31:27` | `cowrie.client.kex` |
| `2026-07-16 17:31:29` | `cowrie.login.success` |
| `2026-07-16 17:31:29` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d471816f2beb

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-16 17:35 |
| **Last Seen** | 2026-07-16 17:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:35:09` | `cowrie.session.connect` |
| `2026-07-16 17:35:10` | `cowrie.client.version` |
| `2026-07-16 17:35:10` | `cowrie.client.kex` |
| `2026-07-16 17:35:12` | `cowrie.login.success` |
| `2026-07-16 17:35:12` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fa69d6d7688

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-16 17:38 |
| **Last Seen** | 2026-07-16 17:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:38:25` | `cowrie.session.connect` |
| `2026-07-16 17:38:25` | `cowrie.client.version` |
| `2026-07-16 17:38:25` | `cowrie.client.kex` |
| `2026-07-16 17:38:28` | `cowrie.login.success` |
| `2026-07-16 17:38:29` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356202c7c71a

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 17:41 |
| **Last Seen** | 2026-07-16 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:41:45` | `cowrie.session.connect` |
| `2026-07-16 17:41:45` | `cowrie.client.version` |
| `2026-07-16 17:41:45` | `cowrie.client.kex` |
| `2026-07-16 17:41:46` | `cowrie.login.success` |
| `2026-07-16 17:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba671ad1a6af

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-16 17:41 |
| **Last Seen** | 2026-07-16 17:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:41:52` | `cowrie.session.connect` |
| `2026-07-16 17:41:53` | `cowrie.client.version` |
| `2026-07-16 17:41:53` | `cowrie.client.kex` |
| `2026-07-16 17:41:55` | `cowrie.login.success` |
| `2026-07-16 17:41:56` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d5c412c770

| Field | Detail |
|---|---|
| **Source IP** | `146.190.215[.]195` |
| **First Seen** | 2026-07-16 17:42 |
| **Last Seen** | 2026-07-16 17:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:42:00` | `cowrie.session.connect` |
| `2026-07-16 17:42:01` | `cowrie.client.version` |
| `2026-07-16 17:42:01` | `cowrie.client.kex` |
| `2026-07-16 17:42:02` | `cowrie.login.success` |
| `2026-07-16 17:42:02` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.215[.]195` to AbuseIPDB if not already reported
- [ ] Block `146.190.215[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3f35f38838

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 17:43 |
| **Last Seen** | 2026-07-16 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:43:45` | `cowrie.session.connect` |
| `2026-07-16 17:43:45` | `cowrie.client.version` |
| `2026-07-16 17:43:45` | `cowrie.client.kex` |
| `2026-07-16 17:43:45` | `cowrie.login.success` |
| `2026-07-16 17:43:46` | `cowrie.session.params` |
| `2026-07-16 17:43:46` | `cowrie.command.input` |
| `2026-07-16 17:43:46` | `cowrie.log.closed` |
| `2026-07-16 17:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bd08c9c503

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 17:53 |
| **Last Seen** | 2026-07-16 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:53:43` | `cowrie.session.connect` |
| `2026-07-16 17:53:43` | `cowrie.client.version` |
| `2026-07-16 17:53:43` | `cowrie.client.kex` |
| `2026-07-16 17:53:43` | `cowrie.login.success` |
| `2026-07-16 17:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d0bb4eb9b4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 17:53 |
| **Last Seen** | 2026-07-16 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:53:44` | `cowrie.session.connect` |
| `2026-07-16 17:53:44` | `cowrie.client.version` |
| `2026-07-16 17:53:44` | `cowrie.client.kex` |
| `2026-07-16 17:53:44` | `cowrie.login.success` |
| `2026-07-16 17:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667c1b6410a5

| Field | Detail |
|---|---|
| **Source IP** | `111.70.39[.]214` |
| **First Seen** | 2026-07-16 17:56 |
| **Last Seen** | 2026-07-16 17:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:56:49` | `cowrie.session.connect` |
| `2026-07-16 17:56:50` | `cowrie.client.version` |
| `2026-07-16 17:56:50` | `cowrie.client.kex` |
| `2026-07-16 17:56:52` | `cowrie.login.success` |
| `2026-07-16 17:56:53` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.39[.]214` to AbuseIPDB if not already reported
- [ ] Block `111.70.39[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f144b9b3d8af

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-07-16 17:57 |
| **Last Seen** | 2026-07-16 17:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 17:57:02` | `cowrie.session.connect` |
| `2026-07-16 17:57:02` | `cowrie.client.version` |
| `2026-07-16 17:57:02` | `cowrie.client.kex` |
| `2026-07-16 17:57:06` | `cowrie.login.success` |
| `2026-07-16 17:57:07` | `cowrie.direct-tcpip.request` |
| `2026-07-16 17:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f8f32e4590

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 18:04 |
| **Last Seen** | 2026-07-16 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:04:19` | `cowrie.session.connect` |
| `2026-07-16 18:04:19` | `cowrie.client.version` |
| `2026-07-16 18:04:19` | `cowrie.client.kex` |
| `2026-07-16 18:04:20` | `cowrie.login.success` |
| `2026-07-16 18:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7e1c4f2a8f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 18:04 |
| **Last Seen** | 2026-07-16 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:04:19` | `cowrie.session.connect` |
| `2026-07-16 18:04:19` | `cowrie.client.version` |
| `2026-07-16 18:04:19` | `cowrie.client.kex` |
| `2026-07-16 18:04:20` | `cowrie.login.success` |
| `2026-07-16 18:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a93b9c61cd

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-07-16 18:06 |
| **Last Seen** | 2026-07-16 18:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:06:32` | `cowrie.session.connect` |
| `2026-07-16 18:06:32` | `cowrie.client.version` |
| `2026-07-16 18:06:32` | `cowrie.client.kex` |
| `2026-07-16 18:06:34` | `cowrie.login.success` |
| `2026-07-16 18:06:34` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59972c368fe4

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-16 18:12 |
| **Last Seen** | 2026-07-16 18:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:12:37` | `cowrie.session.connect` |
| `2026-07-16 18:12:37` | `cowrie.client.version` |
| `2026-07-16 18:12:37` | `cowrie.client.kex` |
| `2026-07-16 18:12:38` | `cowrie.login.success` |
| `2026-07-16 18:12:38` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11424323bb8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 18:16 |
| **Last Seen** | 2026-07-16 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:16:04` | `cowrie.session.connect` |
| `2026-07-16 18:16:04` | `cowrie.client.version` |
| `2026-07-16 18:16:04` | `cowrie.client.kex` |
| `2026-07-16 18:16:05` | `cowrie.login.success` |
| `2026-07-16 18:16:05` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:16:05` | `cowrie.direct-tcpip.data` |
| `2026-07-16 18:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62916687de71

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 18:18 |
| **Last Seen** | 2026-07-16 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:18:44` | `cowrie.session.connect` |
| `2026-07-16 18:18:44` | `cowrie.client.version` |
| `2026-07-16 18:18:44` | `cowrie.client.kex` |
| `2026-07-16 18:18:45` | `cowrie.login.success` |
| `2026-07-16 18:18:45` | `cowrie.session.params` |
| `2026-07-16 18:18:45` | `cowrie.command.input` |
| `2026-07-16 18:18:45` | `cowrie.log.closed` |
| `2026-07-16 18:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8465a2e595dd

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]30` |
| **First Seen** | 2026-07-16 18:21 |
| **Last Seen** | 2026-07-16 18:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:21:31` | `cowrie.session.connect` |
| `2026-07-16 18:21:32` | `cowrie.client.version` |
| `2026-07-16 18:21:32` | `cowrie.client.kex` |
| `2026-07-16 18:21:36` | `cowrie.login.success` |
| `2026-07-16 18:21:36` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]30` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e913c9b9bea8

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-07-16 18:21 |
| **Last Seen** | 2026-07-16 18:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:21:41` | `cowrie.session.connect` |
| `2026-07-16 18:21:42` | `cowrie.client.version` |
| `2026-07-16 18:21:42` | `cowrie.client.kex` |
| `2026-07-16 18:21:44` | `cowrie.login.success` |
| `2026-07-16 18:21:44` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc1eb9067a3

| Field | Detail |
|---|---|
| **Source IP** | `101.96.231[.]24` |
| **First Seen** | 2026-07-16 18:22 |
| **Last Seen** | 2026-07-16 18:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:22:08` | `cowrie.session.connect` |
| `2026-07-16 18:22:08` | `cowrie.client.version` |
| `2026-07-16 18:22:09` | `cowrie.client.kex` |
| `2026-07-16 18:22:10` | `cowrie.login.success` |
| `2026-07-16 18:22:11` | `cowrie.session.params` |
| `2026-07-16 18:22:11` | `cowrie.command.input` |
| `2026-07-16 18:22:11` | `cowrie.command.failed` |
| `2026-07-16 18:22:11` | `cowrie.log.closed` |
| `2026-07-16 18:22:12` | `cowrie.session.params` |
| `2026-07-16 18:22:12` | `cowrie.command.input` |
| `2026-07-16 18:22:12` | `cowrie.session.file_download` |
| `2026-07-16 18:22:12` | `cowrie.log.closed` |
| `2026-07-16 18:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `101.96.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433c27791a7e

| Field | Detail |
|---|---|
| **Source IP** | `101.96.231[.]24` |
| **First Seen** | 2026-07-16 18:22 |
| **Last Seen** | 2026-07-16 18:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:22:12` | `cowrie.session.connect` |
| `2026-07-16 18:22:12` | `cowrie.client.version` |
| `2026-07-16 18:22:13` | `cowrie.client.kex` |
| `2026-07-16 18:22:14` | `cowrie.login.success` |
| `2026-07-16 18:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `101.96.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f9872d72da

| Field | Detail |
|---|---|
| **Source IP** | `101.96.231[.]24` |
| **First Seen** | 2026-07-16 18:22 |
| **Last Seen** | 2026-07-16 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:22:15` | `cowrie.session.connect` |
| `2026-07-16 18:22:15` | `cowrie.client.version` |
| `2026-07-16 18:22:15` | `cowrie.client.kex` |
| `2026-07-16 18:22:16` | `cowrie.login.success` |
| `2026-07-16 18:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `101.96.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e451b127918

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-16 18:27 |
| **Last Seen** | 2026-07-16 18:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:27:56` | `cowrie.session.connect` |
| `2026-07-16 18:27:56` | `cowrie.client.version` |
| `2026-07-16 18:27:56` | `cowrie.client.kex` |
| `2026-07-16 18:27:58` | `cowrie.login.success` |
| `2026-07-16 18:27:58` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0def1e85d21

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-16 18:28 |
| **Last Seen** | 2026-07-16 18:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:28:08` | `cowrie.session.connect` |
| `2026-07-16 18:28:08` | `cowrie.client.version` |
| `2026-07-16 18:28:08` | `cowrie.client.kex` |
| `2026-07-16 18:28:10` | `cowrie.login.success` |
| `2026-07-16 18:28:10` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09911c613233

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-16 18:31 |
| **Last Seen** | 2026-07-16 18:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:31:22` | `cowrie.session.connect` |
| `2026-07-16 18:31:22` | `cowrie.client.version` |
| `2026-07-16 18:31:22` | `cowrie.client.kex` |
| `2026-07-16 18:31:25` | `cowrie.login.success` |
| `2026-07-16 18:31:25` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76ab244dcb3

| Field | Detail |
|---|---|
| **Source IP** | `112.196.52[.]107` |
| **First Seen** | 2026-07-16 18:31 |
| **Last Seen** | 2026-07-16 18:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:31:35` | `cowrie.session.connect` |
| `2026-07-16 18:31:36` | `cowrie.client.version` |
| `2026-07-16 18:31:36` | `cowrie.client.kex` |
| `2026-07-16 18:31:38` | `cowrie.login.success` |
| `2026-07-16 18:31:39` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.52[.]107` to AbuseIPDB if not already reported
- [ ] Block `112.196.52[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b089cfce90e2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 18:35 |
| **Last Seen** | 2026-07-16 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:35:24` | `cowrie.session.connect` |
| `2026-07-16 18:35:24` | `cowrie.client.version` |
| `2026-07-16 18:35:24` | `cowrie.client.kex` |
| `2026-07-16 18:35:25` | `cowrie.login.success` |
| `2026-07-16 18:35:26` | `cowrie.session.params` |
| `2026-07-16 18:35:26` | `cowrie.command.input` |
| `2026-07-16 18:35:26` | `cowrie.log.closed` |
| `2026-07-16 18:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac00bc4f465c

| Field | Detail |
|---|---|
| **Source IP** | `104.152.58[.]233` |
| **First Seen** | 2026-07-16 18:37 |
| **Last Seen** | 2026-07-16 18:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:37:26` | `cowrie.session.connect` |
| `2026-07-16 18:37:27` | `cowrie.client.version` |
| `2026-07-16 18:37:27` | `cowrie.client.kex` |
| `2026-07-16 18:37:28` | `cowrie.login.success` |
| `2026-07-16 18:37:28` | `cowrie.direct-tcpip.request` |
| `2026-07-16 18:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.152.58[.]233` to AbuseIPDB if not already reported
- [ ] Block `104.152.58[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01af4f1c01e

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 18:41 |
| **Last Seen** | 2026-07-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 18:41:33` | `cowrie.session.connect` |
| `2026-07-16 18:41:33` | `cowrie.client.version` |
| `2026-07-16 18:41:34` | `cowrie.client.kex` |
| `2026-07-16 18:41:35` | `cowrie.login.success` |
| `2026-07-16 18:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **88** | 2026-07-16 16:55 | 2026-07-16 18:54 | 59m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.73[.]100` | **10** | 2026-07-16 16:55 | 2026-07-16 18:53 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-07-16 18:13 | 2026-07-16 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-16 17:26 | 2026-07-16 18:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-16 18:18 | 2026-07-16 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | **3** | 2026-07-16 17:56 | 2026-07-16 17:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]138` | **3** | 2026-07-16 18:51 | 2026-07-16 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | **3** | 2026-07-16 18:51 | 2026-07-16 18:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]87` | **3** | 2026-07-16 18:52 | 2026-07-16 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-16 16:56 | 2026-07-16 16:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-07-16 17:57 | 2026-07-16 17:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `118.106.202[.]169` | 1 | 2026-07-16 18:50 | 2026-07-16 18:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.76.103[.]111` | 1 | 2026-07-16 18:36 | 2026-07-16 18:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.156.80[.]11` | 1 | 2026-07-16 17:35 | 2026-07-16 17:35 | 7s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-07-16 18:37 | 2026-07-16 18:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.154.65[.]146` | 1 | 2026-07-16 18:34 | 2026-07-16 18:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]113` | 1 | 2026-07-16 17:33 | 2026-07-16 17:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-16 18:12 | 2026-07-16 18:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.220.185[.]122` | 1 | 2026-07-16 17:54 | 2026-07-16 17:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-16 18:13 | 2026-07-16 18:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-07-16 17:57 | 2026-07-16 17:57 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `178.178.222[.]58` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `183.171.236[.]113` | MY | Celcom Axiata Berhad | **100** ⚠️ | 40 |
| `101.96.231[.]24` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 4 |
| `177.135.206[.]10` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `66.132.172[.]138` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `118.106.202[.]169` | JP | Chubu Telecommunications Co.,Inc. | **100** ⚠️ | 42 |
| `124.133.10[.]66` | CN | JINAN SONGJIAN NETBAR | **100** ⚠️ | 46 |
| `146.190.215[.]195` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `136.116.189[.]132` | US | Google LLC | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 194 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (10.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 21 recon entry/entries in table (10 group(s) consolidating 125 session(s)).

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
_Report time: 2026-07-16T19:18:34Z_

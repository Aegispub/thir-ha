# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T19:18:17Z |
| **Shift Time** | 19:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **142** |
| Confirmed Threats | **130** |
| False Positives Filtered | **12** (8.5%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **27** |
| High Severity Cases | **78** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **24** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **90** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 10 |
| `test` | 7 |
| `config` | 6 |
| `centos` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 11 |
| `345gs5662d34` | 10 |
| `root` | 5 |
| `4` | 5 |
| `66666` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `centos` | `root` | 5 |
| `root` | `4` | 5 |
| `config` | `66666` | 5 |
| `oracle` | `12345` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `config` | `333` | `10.0.0.73` | 2026-07-26T16:56:16 |
| `centos` | `root` | `122.170.111.140` | 2026-07-26T16:57:40 |
| `centos` | `root` | `49.124.151.16` | 2026-07-26T16:57:50 |
| `centos` | `root` | `175.198.18.3` | 2026-07-26T17:01:17 |
| `centos` | `root` | `123.123.196.140` | 2026-07-26T17:01:29 |
| `centos` | `root` | `10.0.0.73` | 2026-07-26T17:01:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T17:08:51 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T17:08:51 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-26T17:08:57 |
| `nobody` | `222` | `203.192.247.84` | 2026-07-26T17:14:41 |
| `nobody` | `222` | `111.70.32.51` | 2026-07-26T17:14:54 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-26T17:15:28 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-26T17:15:53 |
| `nobody` | `222` | `10.0.0.73` | 2026-07-26T17:18:26 |
| `root` | `Xx123456@` | `115.191.27.238` | 2026-07-26T17:20:48 |
| `user` | `user99` | `10.0.0.73` | 2026-07-26T17:20:50 |
| `345gs5662d34` | `345gs5662d34` | `115.191.27.238` | 2026-07-26T17:20:52 |
| `root` | `3245gs5662d34` | `115.191.27.238` | 2026-07-26T17:20:54 |
| `root` | `A123a123` | `4.184.246.230` | 2026-07-26T17:22:08 |
| `345gs5662d34` | `345gs5662d34` | `4.184.246.230` | 2026-07-26T17:22:11 |
| `root` | `3245gs5662d34` | `4.184.246.230` | 2026-07-26T17:22:12 |
| `ronaldo` | `ronaldo` | `23.81.36.46` | 2026-07-26T17:22:24 |
| `345gs5662d34` | `345gs5662d34` | `23.81.36.46` | 2026-07-26T17:22:26 |
| `ronaldo` | `3245gs5662d34` | `23.81.36.46` | 2026-07-26T17:22:27 |
| `ubnt` | `8888888` | `138.219.13.21` | 2026-07-26T17:25:40 |
| `myuser` | `myuser@123` | `211.95.159.159` | 2026-07-26T17:25:49 |
| `345gs5662d34` | `345gs5662d34` | `211.95.159.159` | 2026-07-26T17:25:53 |
| `myuser` | `3245gs5662d34` | `211.95.159.159` | 2026-07-26T17:25:55 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-26T17:30:32 |
| `root` | `4` | `81.214.75.248` | 2026-07-26T17:39:07 |
| `esadmin` | `esadmin` | `79.3.96.178` | 2026-07-26T17:40:37 |
| `345gs5662d34` | `345gs5662d34` | `79.3.96.178` | 2026-07-26T17:40:40 |
| `esadmin` | `3245gs5662d34` | `79.3.96.178` | 2026-07-26T17:40:41 |
| `root` | `4` | `58.57.154.146` | 2026-07-26T17:42:32 |
| `root` | `4` | `36.154.134.146` | 2026-07-26T17:42:41 |
| `root` | `4` | `10.0.0.73` | 2026-07-26T17:42:56 |
| `test` | `666666` | `175.206.1.60` | 2026-07-26T17:44:49 |
| `test` | `666666` | `65.20.138.3` | 2026-07-26T17:44:57 |
| `test` | `666666` | `10.0.0.73` | 2026-07-26T17:45:13 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-26T17:45:50 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-26T17:45:50 |
| `config` | `66666` | `117.70.94.155` | 2026-07-26T17:46:46 |
| `adam` | `1` | `124.40.252.3` | 2026-07-26T17:47:38 |
| `345gs5662d34` | `345gs5662d34` | `124.40.252.3` | 2026-07-26T17:47:44 |
| `adam` | `3245gs5662d34` | `124.40.252.3` | 2026-07-26T17:47:47 |
| `config` | `66666` | `208.96.233.67` | 2026-07-26T17:49:59 |
| `config` | `66666` | `201.28.237.90` | 2026-07-26T17:50:07 |
| `star` | `star` | `61.129.41.146` | 2026-07-26T17:50:08 |
| `config` | `66666` | `10.0.0.73` | 2026-07-26T17:50:22 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `185.180.141.50` | 2026-07-26T17:51:27 |
| `blank` | `22222` | `2.55.125.200` | 2026-07-26T18:03:20 |
| `blank` | `22222` | `177.174.0.3` | 2026-07-26T18:03:32 |
| `oracle` | `12345` | `87.117.32.22` | 2026-07-26T18:05:31 |
| `oracle` | `12345` | `112.6.11.184` | 2026-07-26T18:05:46 |
| `blank` | `22222` | `113.200.216.246` | 2026-07-26T18:06:53 |
| `oracle` | `12345` | `59.120.8.61` | 2026-07-26T18:08:58 |
| `oracle` | `12345` | `103.83.23.169` | 2026-07-26T18:09:06 |
| `oracle` | `12345` | `10.0.0.73` | 2026-07-26T18:09:17 |
| `deploy` | `a` | `101.96.230.94` | 2026-07-26T18:09:19 |
| `root` | `Market123` | `223.123.124.70` | 2026-07-26T18:09:28 |
| `345gs5662d34` | `345gs5662d34` | `223.123.124.70` | 2026-07-26T18:09:32 |
| `root` | `3245gs5662d34` | `223.123.124.70` | 2026-07-26T18:09:34 |
| `deploy` | `3245gs5662d34` | `101.96.230.94` | 2026-07-26T18:09:48 |
| `root` | `12131415` | `163.7.9.55` | 2026-07-26T18:09:55 |
| `345gs5662d34` | `345gs5662d34` | `163.7.9.55` | 2026-07-26T18:09:59 |
| `root` | `3245gs5662d34` | `163.7.9.55` | 2026-07-26T18:10:01 |
| `default` | `2222` | `178.178.194.151` | 2026-07-26T18:11:05 |
| `default` | `2222` | `154.146.238.122` | 2026-07-26T18:11:12 |
| `default` | `2222` | `220.80.223.144` | 2026-07-26T18:14:29 |
| `default` | `2222` | `211.53.58.10` | 2026-07-26T18:14:47 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T18:17:38 |
| `root` | `﻿------fuck------` | `218.87.194.83` | 2026-07-26T18:20:05 |
| `pi` | `dietpi` | `101.13.4.124` | 2026-07-26T18:29:50 |
| `test` | `000` | `58.22.255.28` | 2026-07-26T18:31:18 |
| `test` | `000` | `186.179.80.12` | 2026-07-26T18:31:26 |
| `test` | `000` | `10.0.0.73` | 2026-07-26T18:31:36 |
| `jirka` | `jirka` | `88.147.30.59` | 2026-07-26T18:32:53 |
| `345gs5662d34` | `345gs5662d34` | `88.147.30.59` | 2026-07-26T18:32:56 |
| `jirka` | `3245gs5662d34` | `88.147.30.59` | 2026-07-26T18:32:57 |
| `pi` | `dietpi` | `119.160.166.237` | 2026-07-26T18:33:15 |
| `pi` | `dietpi` | `70.91.135.181` | 2026-07-26T18:33:27 |
| `pi` | `dietpi` | `10.0.0.73` | 2026-07-26T18:33:37 |
| `operator` | `operator2019` | `65.20.217.64` | 2026-07-26T18:35:32 |
| `postgres` | `p0stgr3s` | `88.147.30.59` | 2026-07-26T18:37:22 |
| `postgres` | `3245gs5662d34` | `88.147.30.59` | 2026-07-26T18:37:26 |
| `operator` | `operator2019` | `178.178.222.55` | 2026-07-26T18:38:47 |
| `operator` | `operator2019` | `10.0.0.73` | 2026-07-26T18:39:16 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T18:43:24 |
| `user` | `user333` | `202.72.196.75` | 2026-07-26T18:54:12 |
| `user` | `user333` | `103.68.22.115` | 2026-07-26T18:54:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **142** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |
| OpenSSH | 35 |
| Paramiko (Python) | 7 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 35 | 35 |
| `f555226df196...` | Mirai/variant | 26 | 9 |
| `03a80b21afa8...` | Modern SSH client | 9 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `6372ee695756...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 35 | 35 | Mirai/variant |
| `f555226df196...` | libssh | 26 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 11 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `88.147.30.59`, `23.81.36.46`, `4.184.246.230`, `163.7.9.55`, `124.40.252.3`, `79.3.96.178`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **58** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (78)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b66ea26e0c8d

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-07-26 16:57 |
| **Last Seen** | 2026-07-26 16:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:57:38` | `cowrie.session.connect` |
| `2026-07-26 16:57:39` | `cowrie.client.version` |
| `2026-07-26 16:57:39` | `cowrie.client.kex` |
| `2026-07-26 16:57:40` | `cowrie.login.success` |
| `2026-07-26 16:57:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4a32311630

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]16` |
| **First Seen** | 2026-07-26 16:57 |
| **Last Seen** | 2026-07-26 16:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:57:47` | `cowrie.session.connect` |
| `2026-07-26 16:57:47` | `cowrie.client.version` |
| `2026-07-26 16:57:47` | `cowrie.client.kex` |
| `2026-07-26 16:57:50` | `cowrie.login.success` |
| `2026-07-26 16:57:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]16` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0c6596e2d6

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-26 17:01 |
| **Last Seen** | 2026-07-26 17:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:01:11` | `cowrie.session.connect` |
| `2026-07-26 17:01:12` | `cowrie.client.version` |
| `2026-07-26 17:01:12` | `cowrie.client.kex` |
| `2026-07-26 17:01:17` | `cowrie.login.success` |
| `2026-07-26 17:01:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3be39a1d06

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-07-26 17:01 |
| **Last Seen** | 2026-07-26 17:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:01:27` | `cowrie.session.connect` |
| `2026-07-26 17:01:27` | `cowrie.client.version` |
| `2026-07-26 17:01:27` | `cowrie.client.kex` |
| `2026-07-26 17:01:29` | `cowrie.login.success` |
| `2026-07-26 17:01:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c6768a4337

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 17:08 |
| **Last Seen** | 2026-07-26 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:08:51` | `cowrie.session.connect` |
| `2026-07-26 17:08:51` | `cowrie.client.version` |
| `2026-07-26 17:08:51` | `cowrie.client.kex` |
| `2026-07-26 17:08:51` | `cowrie.login.success` |
| `2026-07-26 17:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0f14c97930

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 17:08 |
| **Last Seen** | 2026-07-26 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:08:51` | `cowrie.session.connect` |
| `2026-07-26 17:08:51` | `cowrie.client.version` |
| `2026-07-26 17:08:51` | `cowrie.client.kex` |
| `2026-07-26 17:08:51` | `cowrie.login.success` |
| `2026-07-26 17:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079eac1a75bb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 17:08 |
| **Last Seen** | 2026-07-26 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:08:57` | `cowrie.session.connect` |
| `2026-07-26 17:08:57` | `cowrie.client.version` |
| `2026-07-26 17:08:57` | `cowrie.client.kex` |
| `2026-07-26 17:08:57` | `cowrie.login.success` |
| `2026-07-26 17:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18091dd4ed8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 17:08 |
| **Last Seen** | 2026-07-26 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:08:57` | `cowrie.session.connect` |
| `2026-07-26 17:08:57` | `cowrie.client.version` |
| `2026-07-26 17:08:57` | `cowrie.client.kex` |
| `2026-07-26 17:08:57` | `cowrie.login.success` |
| `2026-07-26 17:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a09c55b4ee

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-07-26 17:14 |
| **Last Seen** | 2026-07-26 17:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:14:38` | `cowrie.session.connect` |
| `2026-07-26 17:14:39` | `cowrie.client.version` |
| `2026-07-26 17:14:39` | `cowrie.client.kex` |
| `2026-07-26 17:14:41` | `cowrie.login.success` |
| `2026-07-26 17:14:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03e1b8ef2cf

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-07-26 17:14 |
| **Last Seen** | 2026-07-26 17:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:14:51` | `cowrie.session.connect` |
| `2026-07-26 17:14:52` | `cowrie.client.version` |
| `2026-07-26 17:14:52` | `cowrie.client.kex` |
| `2026-07-26 17:14:54` | `cowrie.login.success` |
| `2026-07-26 17:14:55` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9a7a642a52

| Field | Detail |
|---|---|
| **Source IP** | `115.191.27[.]238` |
| **First Seen** | 2026-07-26 17:20 |
| **Last Seen** | 2026-07-26 17:20 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:20:36` | `cowrie.session.connect` |
| `2026-07-26 17:20:47` | `cowrie.client.version` |
| `2026-07-26 17:20:47` | `cowrie.client.kex` |
| `2026-07-26 17:20:48` | `cowrie.login.success` |
| `2026-07-26 17:20:49` | `cowrie.session.params` |
| `2026-07-26 17:20:49` | `cowrie.command.input` |
| `2026-07-26 17:20:49` | `cowrie.command.failed` |
| `2026-07-26 17:20:49` | `cowrie.log.closed` |
| `2026-07-26 17:20:50` | `cowrie.session.params` |
| `2026-07-26 17:20:50` | `cowrie.command.input` |
| `2026-07-26 17:20:50` | `cowrie.session.file_download` |
| `2026-07-26 17:20:50` | `cowrie.log.closed` |
| `2026-07-26 17:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `115.191.27[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3bb2405260

| Field | Detail |
|---|---|
| **Source IP** | `115.191.27[.]238` |
| **First Seen** | 2026-07-26 17:20 |
| **Last Seen** | 2026-07-26 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:20:51` | `cowrie.session.connect` |
| `2026-07-26 17:20:51` | `cowrie.client.version` |
| `2026-07-26 17:20:51` | `cowrie.client.kex` |
| `2026-07-26 17:20:52` | `cowrie.login.success` |
| `2026-07-26 17:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `115.191.27[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c90cbd9f45

| Field | Detail |
|---|---|
| **Source IP** | `115.191.27[.]238` |
| **First Seen** | 2026-07-26 17:20 |
| **Last Seen** | 2026-07-26 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:20:53` | `cowrie.session.connect` |
| `2026-07-26 17:20:53` | `cowrie.client.version` |
| `2026-07-26 17:20:53` | `cowrie.client.kex` |
| `2026-07-26 17:20:54` | `cowrie.login.success` |
| `2026-07-26 17:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `115.191.27[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc8839f04dc

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:08` | `cowrie.session.connect` |
| `2026-07-26 17:22:08` | `cowrie.client.version` |
| `2026-07-26 17:22:08` | `cowrie.client.kex` |
| `2026-07-26 17:22:08` | `cowrie.login.success` |
| `2026-07-26 17:22:09` | `cowrie.session.params` |
| `2026-07-26 17:22:09` | `cowrie.command.input` |
| `2026-07-26 17:22:09` | `cowrie.command.failed` |
| `2026-07-26 17:22:09` | `cowrie.log.closed` |
| `2026-07-26 17:22:10` | `cowrie.session.params` |
| `2026-07-26 17:22:10` | `cowrie.command.input` |
| `2026-07-26 17:22:10` | `cowrie.session.file_download` |
| `2026-07-26 17:22:10` | `cowrie.log.closed` |
| `2026-07-26 17:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1a1502fc7f

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:10` | `cowrie.session.connect` |
| `2026-07-26 17:22:10` | `cowrie.client.version` |
| `2026-07-26 17:22:11` | `cowrie.client.kex` |
| `2026-07-26 17:22:11` | `cowrie.login.success` |
| `2026-07-26 17:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd62e3f1bcf

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:11` | `cowrie.session.connect` |
| `2026-07-26 17:22:11` | `cowrie.client.version` |
| `2026-07-26 17:22:11` | `cowrie.client.kex` |
| `2026-07-26 17:22:12` | `cowrie.login.success` |
| `2026-07-26 17:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0194da56fbf

| Field | Detail |
|---|---|
| **Source IP** | `23.81.36[.]46` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:23` | `cowrie.session.connect` |
| `2026-07-26 17:22:23` | `cowrie.client.version` |
| `2026-07-26 17:22:23` | `cowrie.client.kex` |
| `2026-07-26 17:22:24` | `cowrie.login.success` |
| `2026-07-26 17:22:24` | `cowrie.session.params` |
| `2026-07-26 17:22:24` | `cowrie.command.input` |
| `2026-07-26 17:22:24` | `cowrie.command.failed` |
| `2026-07-26 17:22:25` | `cowrie.log.closed` |
| `2026-07-26 17:22:25` | `cowrie.session.params` |
| `2026-07-26 17:22:25` | `cowrie.command.input` |
| `2026-07-26 17:22:25` | `cowrie.session.file_download` |
| `2026-07-26 17:22:25` | `cowrie.log.closed` |
| `2026-07-26 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.81.36[.]46` to AbuseIPDB if not already reported
- [ ] Block `23.81.36[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38aa1b87af2

| Field | Detail |
|---|---|
| **Source IP** | `23.81.36[.]46` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:26` | `cowrie.session.connect` |
| `2026-07-26 17:22:26` | `cowrie.client.version` |
| `2026-07-26 17:22:26` | `cowrie.client.kex` |
| `2026-07-26 17:22:26` | `cowrie.login.success` |
| `2026-07-26 17:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.81.36[.]46` to AbuseIPDB if not already reported
- [ ] Block `23.81.36[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e0c19b3e0b

| Field | Detail |
|---|---|
| **Source IP** | `23.81.36[.]46` |
| **First Seen** | 2026-07-26 17:22 |
| **Last Seen** | 2026-07-26 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:22:26` | `cowrie.session.connect` |
| `2026-07-26 17:22:26` | `cowrie.client.version` |
| `2026-07-26 17:22:26` | `cowrie.client.kex` |
| `2026-07-26 17:22:27` | `cowrie.login.success` |
| `2026-07-26 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.81.36[.]46` to AbuseIPDB if not already reported
- [ ] Block `23.81.36[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19113605f736

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-26 17:25 |
| **Last Seen** | 2026-07-26 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:25:38` | `cowrie.session.connect` |
| `2026-07-26 17:25:38` | `cowrie.client.version` |
| `2026-07-26 17:25:38` | `cowrie.client.kex` |
| `2026-07-26 17:25:40` | `cowrie.login.success` |
| `2026-07-26 17:25:40` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4153a87cc0

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-07-26 17:25 |
| **Last Seen** | 2026-07-26 17:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:25:47` | `cowrie.session.connect` |
| `2026-07-26 17:25:47` | `cowrie.client.version` |
| `2026-07-26 17:25:47` | `cowrie.client.kex` |
| `2026-07-26 17:25:49` | `cowrie.login.success` |
| `2026-07-26 17:25:50` | `cowrie.session.params` |
| `2026-07-26 17:25:50` | `cowrie.command.input` |
| `2026-07-26 17:25:50` | `cowrie.command.failed` |
| `2026-07-26 17:25:50` | `cowrie.log.closed` |
| `2026-07-26 17:25:51` | `cowrie.session.params` |
| `2026-07-26 17:25:51` | `cowrie.command.input` |
| `2026-07-26 17:25:52` | `cowrie.session.file_download` |
| `2026-07-26 17:25:52` | `cowrie.log.closed` |
| `2026-07-26 17:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f009d44eca84

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-07-26 17:25 |
| **Last Seen** | 2026-07-26 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:25:52` | `cowrie.session.connect` |
| `2026-07-26 17:25:52` | `cowrie.client.version` |
| `2026-07-26 17:25:52` | `cowrie.client.kex` |
| `2026-07-26 17:25:53` | `cowrie.login.success` |
| `2026-07-26 17:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616449b4e38b

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-07-26 17:25 |
| **Last Seen** | 2026-07-26 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:25:54` | `cowrie.session.connect` |
| `2026-07-26 17:25:54` | `cowrie.client.version` |
| `2026-07-26 17:25:54` | `cowrie.client.kex` |
| `2026-07-26 17:25:55` | `cowrie.login.success` |
| `2026-07-26 17:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbd06cfc6d8

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-07-26 17:39 |
| **Last Seen** | 2026-07-26 17:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:39:05` | `cowrie.session.connect` |
| `2026-07-26 17:39:06` | `cowrie.client.version` |
| `2026-07-26 17:39:06` | `cowrie.client.kex` |
| `2026-07-26 17:39:07` | `cowrie.login.success` |
| `2026-07-26 17:39:07` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9636ace290c7

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-07-26 17:40 |
| **Last Seen** | 2026-07-26 17:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:40:36` | `cowrie.session.connect` |
| `2026-07-26 17:40:36` | `cowrie.client.version` |
| `2026-07-26 17:40:36` | `cowrie.client.kex` |
| `2026-07-26 17:40:37` | `cowrie.login.success` |
| `2026-07-26 17:40:38` | `cowrie.session.params` |
| `2026-07-26 17:40:38` | `cowrie.command.input` |
| `2026-07-26 17:40:38` | `cowrie.command.failed` |
| `2026-07-26 17:40:38` | `cowrie.log.closed` |
| `2026-07-26 17:40:39` | `cowrie.session.params` |
| `2026-07-26 17:40:39` | `cowrie.command.input` |
| `2026-07-26 17:40:39` | `cowrie.session.file_download` |
| `2026-07-26 17:40:39` | `cowrie.log.closed` |
| `2026-07-26 17:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9cb48a770b9

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-07-26 17:40 |
| **Last Seen** | 2026-07-26 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:40:39` | `cowrie.session.connect` |
| `2026-07-26 17:40:39` | `cowrie.client.version` |
| `2026-07-26 17:40:39` | `cowrie.client.kex` |
| `2026-07-26 17:40:40` | `cowrie.login.success` |
| `2026-07-26 17:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b336e2e63c6d

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-07-26 17:40 |
| **Last Seen** | 2026-07-26 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:40:40` | `cowrie.session.connect` |
| `2026-07-26 17:40:40` | `cowrie.client.version` |
| `2026-07-26 17:40:40` | `cowrie.client.kex` |
| `2026-07-26 17:40:41` | `cowrie.login.success` |
| `2026-07-26 17:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d5ae88d5cb

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-26 17:42 |
| **Last Seen** | 2026-07-26 17:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:42:29` | `cowrie.session.connect` |
| `2026-07-26 17:42:30` | `cowrie.client.version` |
| `2026-07-26 17:42:30` | `cowrie.client.kex` |
| `2026-07-26 17:42:32` | `cowrie.login.success` |
| `2026-07-26 17:42:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4925881e84f

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-07-26 17:42 |
| **Last Seen** | 2026-07-26 17:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:42:37` | `cowrie.session.connect` |
| `2026-07-26 17:42:38` | `cowrie.client.version` |
| `2026-07-26 17:42:38` | `cowrie.client.kex` |
| `2026-07-26 17:42:41` | `cowrie.login.success` |
| `2026-07-26 17:42:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce14b2dea1a

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-26 17:44 |
| **Last Seen** | 2026-07-26 17:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:44:47` | `cowrie.session.connect` |
| `2026-07-26 17:44:47` | `cowrie.client.version` |
| `2026-07-26 17:44:47` | `cowrie.client.kex` |
| `2026-07-26 17:44:49` | `cowrie.login.success` |
| `2026-07-26 17:44:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf62b0610c3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-26 17:44 |
| **Last Seen** | 2026-07-26 17:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:44:55` | `cowrie.session.connect` |
| `2026-07-26 17:44:55` | `cowrie.client.version` |
| `2026-07-26 17:44:55` | `cowrie.client.kex` |
| `2026-07-26 17:44:57` | `cowrie.login.success` |
| `2026-07-26 17:44:57` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49e0f3f17db

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-26 17:45 |
| **Last Seen** | 2026-07-26 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:45:49` | `cowrie.session.connect` |
| `2026-07-26 17:45:49` | `cowrie.client.version` |
| `2026-07-26 17:45:49` | `cowrie.client.kex` |
| `2026-07-26 17:45:50` | `cowrie.login.success` |
| `2026-07-26 17:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c149ee4c9688

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-26 17:45 |
| **Last Seen** | 2026-07-26 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:45:49` | `cowrie.session.connect` |
| `2026-07-26 17:45:49` | `cowrie.client.version` |
| `2026-07-26 17:45:49` | `cowrie.client.kex` |
| `2026-07-26 17:45:50` | `cowrie.login.success` |
| `2026-07-26 17:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ed7586e4ac

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-26 17:46 |
| **Last Seen** | 2026-07-26 17:48 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:46:08` | `cowrie.session.connect` |
| `2026-07-26 17:46:08` | `cowrie.client.version` |
| `2026-07-26 17:46:08` | `cowrie.client.kex` |
| `2026-07-26 17:46:09` | `cowrie.login.success` |
| `2026-07-26 17:46:11` | `cowrie.session.file_upload` |
| `2026-07-26 17:46:12` | `cowrie.session.params` |
| `2026-07-26 17:46:12` | `cowrie.command.input` |
| `2026-07-26 17:46:12` | `cowrie.command.input` |
| `2026-07-26 17:46:12` | `cowrie.command.input` |
| `2026-07-26 17:46:12` | `cowrie.command.failed` |
| `2026-07-26 17:46:12` | `cowrie.log.closed` |
| `2026-07-26 17:46:13` | `cowrie.session.params` |
| `2026-07-26 17:46:13` | `cowrie.command.input` |
| `2026-07-26 17:46:13` | `cowrie.log.closed` |
| `2026-07-26 17:46:14` | `cowrie.session.params` |
| `2026-07-26 17:46:14` | `cowrie.command.input` |
| `2026-07-26 17:46:15` | `cowrie.log.closed` |
| `2026-07-26 17:46:15` | `cowrie.session.params` |
| `2026-07-26 17:46:15` | `cowrie.command.input` |
| `2026-07-26 17:46:15` | `cowrie.command.failed` |
| `2026-07-26 17:46:15` | `cowrie.command.failed` |
| `2026-07-26 17:47:17` | `cowrie.session.params` |
| `2026-07-26 17:47:17` | `cowrie.command.input` |
| `2026-07-26 17:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab5b6426af2

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-26 17:46 |
| **Last Seen** | 2026-07-26 17:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:46:40` | `cowrie.session.connect` |
| `2026-07-26 17:46:41` | `cowrie.client.version` |
| `2026-07-26 17:46:41` | `cowrie.client.kex` |
| `2026-07-26 17:46:46` | `cowrie.login.success` |
| `2026-07-26 17:46:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba45bba2c0a7

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-07-26 17:47 |
| **Last Seen** | 2026-07-26 17:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:47:36` | `cowrie.session.connect` |
| `2026-07-26 17:47:36` | `cowrie.client.version` |
| `2026-07-26 17:47:37` | `cowrie.client.kex` |
| `2026-07-26 17:47:38` | `cowrie.login.success` |
| `2026-07-26 17:47:40` | `cowrie.session.params` |
| `2026-07-26 17:47:40` | `cowrie.command.input` |
| `2026-07-26 17:47:40` | `cowrie.command.failed` |
| `2026-07-26 17:47:40` | `cowrie.log.closed` |
| `2026-07-26 17:47:41` | `cowrie.session.params` |
| `2026-07-26 17:47:41` | `cowrie.command.input` |
| `2026-07-26 17:47:42` | `cowrie.session.file_download` |
| `2026-07-26 17:47:42` | `cowrie.log.closed` |
| `2026-07-26 17:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6621dcdbac88

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-07-26 17:47 |
| **Last Seen** | 2026-07-26 17:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:47:42` | `cowrie.session.connect` |
| `2026-07-26 17:47:42` | `cowrie.client.version` |
| `2026-07-26 17:47:43` | `cowrie.client.kex` |
| `2026-07-26 17:47:44` | `cowrie.login.success` |
| `2026-07-26 17:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44a8ab17505

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-07-26 17:47 |
| **Last Seen** | 2026-07-26 17:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:47:45` | `cowrie.session.connect` |
| `2026-07-26 17:47:45` | `cowrie.client.version` |
| `2026-07-26 17:47:45` | `cowrie.client.kex` |
| `2026-07-26 17:47:47` | `cowrie.login.success` |
| `2026-07-26 17:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacf2093ca38

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-26 17:49 |
| **Last Seen** | 2026-07-26 17:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:49:58` | `cowrie.session.connect` |
| `2026-07-26 17:49:58` | `cowrie.client.version` |
| `2026-07-26 17:49:58` | `cowrie.client.kex` |
| `2026-07-26 17:49:59` | `cowrie.login.success` |
| `2026-07-26 17:49:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aae1306df71

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-26 17:50 |
| **Last Seen** | 2026-07-26 17:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:50:04` | `cowrie.session.connect` |
| `2026-07-26 17:50:05` | `cowrie.client.version` |
| `2026-07-26 17:50:05` | `cowrie.client.kex` |
| `2026-07-26 17:50:07` | `cowrie.login.success` |
| `2026-07-26 17:50:07` | `cowrie.direct-tcpip.request` |
| `2026-07-26 17:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fc19a0dd10

| Field | Detail |
|---|---|
| **Source IP** | `61.129.41[.]146` |
| **First Seen** | 2026-07-26 17:50 |
| **Last Seen** | 2026-07-26 17:55 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:50:06` | `cowrie.session.connect` |
| `2026-07-26 17:50:06` | `cowrie.client.version` |
| `2026-07-26 17:50:07` | `cowrie.client.kex` |
| `2026-07-26 17:50:08` | `cowrie.login.success` |
| `2026-07-26 17:50:09` | `cowrie.session.params` |
| `2026-07-26 17:50:09` | `cowrie.command.input` |
| `2026-07-26 17:50:09` | `cowrie.command.failed` |
| `2026-07-26 17:50:09` | `cowrie.log.closed` |
| `2026-07-26 17:50:10` | `cowrie.session.params` |
| `2026-07-26 17:50:10` | `cowrie.command.input` |
| `2026-07-26 17:50:10` | `cowrie.session.file_download` |
| `2026-07-26 17:50:10` | `cowrie.log.closed` |
| `2026-07-26 17:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.129.41[.]146` to AbuseIPDB if not already reported
- [ ] Block `61.129.41[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05fd0ca4890b

| Field | Detail |
|---|---|
| **Source IP** | `185.180.141[.]50` |
| **First Seen** | 2026-07-26 17:51 |
| **Last Seen** | 2026-07-26 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 17:51:27` | `cowrie.session.connect` |
| `2026-07-26 17:51:27` | `cowrie.login.success` |
| `2026-07-26 17:51:28` | `cowrie.session.params` |
| `2026-07-26 17:51:28` | `cowrie.command.input` |
| `2026-07-26 17:51:28` | `cowrie.command.input` |
| `2026-07-26 17:51:28` | `cowrie.command.failed` |
| `2026-07-26 17:51:28` | `cowrie.command.input` |
| `2026-07-26 17:51:28` | `cowrie.command.failed` |
| `2026-07-26 17:51:28` | `cowrie.command.input` |
| `2026-07-26 17:51:28` | `cowrie.log.closed` |
| `2026-07-26 17:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.180.141[.]50` to AbuseIPDB if not already reported
- [ ] Block `185.180.141[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c817d0d719cd

| Field | Detail |
|---|---|
| **Source IP** | `2.55.125[.]200` |
| **First Seen** | 2026-07-26 18:03 |
| **Last Seen** | 2026-07-26 18:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:03:19` | `cowrie.session.connect` |
| `2026-07-26 18:03:19` | `cowrie.client.version` |
| `2026-07-26 18:03:19` | `cowrie.client.kex` |
| `2026-07-26 18:03:20` | `cowrie.login.success` |
| `2026-07-26 18:03:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.125[.]200` to AbuseIPDB if not already reported
- [ ] Block `2.55.125[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9a942a19e6

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-26 18:03 |
| **Last Seen** | 2026-07-26 18:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:03:30` | `cowrie.session.connect` |
| `2026-07-26 18:03:31` | `cowrie.client.version` |
| `2026-07-26 18:03:31` | `cowrie.client.kex` |
| `2026-07-26 18:03:32` | `cowrie.login.success` |
| `2026-07-26 18:03:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba608467e51

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-07-26 18:05 |
| **Last Seen** | 2026-07-26 18:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:05:29` | `cowrie.session.connect` |
| `2026-07-26 18:05:29` | `cowrie.client.version` |
| `2026-07-26 18:05:29` | `cowrie.client.kex` |
| `2026-07-26 18:05:31` | `cowrie.login.success` |
| `2026-07-26 18:05:31` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485976d2e7c7

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-07-26 18:05 |
| **Last Seen** | 2026-07-26 18:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:05:42` | `cowrie.session.connect` |
| `2026-07-26 18:05:43` | `cowrie.client.version` |
| `2026-07-26 18:05:43` | `cowrie.client.kex` |
| `2026-07-26 18:05:46` | `cowrie.login.success` |
| `2026-07-26 18:05:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71796cf8cf4b

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-07-26 18:06 |
| **Last Seen** | 2026-07-26 18:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:06:50` | `cowrie.session.connect` |
| `2026-07-26 18:06:51` | `cowrie.client.version` |
| `2026-07-26 18:06:51` | `cowrie.client.kex` |
| `2026-07-26 18:06:53` | `cowrie.login.success` |
| `2026-07-26 18:06:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d0f736aada

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-07-26 18:08 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:08:56` | `cowrie.session.connect` |
| `2026-07-26 18:08:56` | `cowrie.client.version` |
| `2026-07-26 18:08:56` | `cowrie.client.kex` |
| `2026-07-26 18:08:58` | `cowrie.login.success` |
| `2026-07-26 18:08:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da71a84cccdd

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:04` | `cowrie.session.connect` |
| `2026-07-26 18:09:04` | `cowrie.client.version` |
| `2026-07-26 18:09:04` | `cowrie.client.kex` |
| `2026-07-26 18:09:06` | `cowrie.login.success` |
| `2026-07-26 18:09:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda69d74a557

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:17` | `cowrie.session.connect` |
| `2026-07-26 18:09:18` | `cowrie.client.version` |
| `2026-07-26 18:09:18` | `cowrie.client.kex` |
| `2026-07-26 18:09:19` | `cowrie.login.success` |
| `2026-07-26 18:09:20` | `cowrie.session.params` |
| `2026-07-26 18:09:20` | `cowrie.command.input` |
| `2026-07-26 18:09:20` | `cowrie.command.failed` |
| `2026-07-26 18:09:21` | `cowrie.log.closed` |
| `2026-07-26 18:09:21` | `cowrie.session.params` |
| `2026-07-26 18:09:21` | `cowrie.command.input` |
| `2026-07-26 18:09:21` | `cowrie.session.file_download` |
| `2026-07-26 18:09:21` | `cowrie.log.closed` |
| `2026-07-26 18:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef43880e68bf

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:27` | `cowrie.session.connect` |
| `2026-07-26 18:09:27` | `cowrie.client.version` |
| `2026-07-26 18:09:27` | `cowrie.client.kex` |
| `2026-07-26 18:09:28` | `cowrie.login.success` |
| `2026-07-26 18:09:29` | `cowrie.session.params` |
| `2026-07-26 18:09:29` | `cowrie.command.input` |
| `2026-07-26 18:09:29` | `cowrie.command.failed` |
| `2026-07-26 18:09:30` | `cowrie.log.closed` |
| `2026-07-26 18:09:31` | `cowrie.session.params` |
| `2026-07-26 18:09:31` | `cowrie.command.input` |
| `2026-07-26 18:09:31` | `cowrie.session.file_download` |
| `2026-07-26 18:09:31` | `cowrie.log.closed` |
| `2026-07-26 18:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d3056da324

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:31` | `cowrie.session.connect` |
| `2026-07-26 18:09:31` | `cowrie.client.version` |
| `2026-07-26 18:09:31` | `cowrie.client.kex` |
| `2026-07-26 18:09:32` | `cowrie.login.success` |
| `2026-07-26 18:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e27a9e17a4a

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:33` | `cowrie.session.connect` |
| `2026-07-26 18:09:33` | `cowrie.client.version` |
| `2026-07-26 18:09:33` | `cowrie.client.kex` |
| `2026-07-26 18:09:34` | `cowrie.login.success` |
| `2026-07-26 18:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec75e71850e4

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:36` | `cowrie.session.connect` |
| `2026-07-26 18:09:47` | `cowrie.client.version` |
| `2026-07-26 18:09:47` | `cowrie.client.kex` |
| `2026-07-26 18:09:48` | `cowrie.login.success` |
| `2026-07-26 18:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b97643233d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:54` | `cowrie.session.connect` |
| `2026-07-26 18:09:54` | `cowrie.client.version` |
| `2026-07-26 18:09:54` | `cowrie.client.kex` |
| `2026-07-26 18:09:55` | `cowrie.login.success` |
| `2026-07-26 18:09:56` | `cowrie.session.params` |
| `2026-07-26 18:09:56` | `cowrie.command.input` |
| `2026-07-26 18:09:56` | `cowrie.command.failed` |
| `2026-07-26 18:09:57` | `cowrie.log.closed` |
| `2026-07-26 18:09:57` | `cowrie.session.params` |
| `2026-07-26 18:09:57` | `cowrie.command.input` |
| `2026-07-26 18:09:58` | `cowrie.session.file_download` |
| `2026-07-26 18:09:58` | `cowrie.log.closed` |
| `2026-07-26 18:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fbf0d9b355

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-26 18:09 |
| **Last Seen** | 2026-07-26 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:09:58` | `cowrie.session.connect` |
| `2026-07-26 18:09:58` | `cowrie.client.version` |
| `2026-07-26 18:09:58` | `cowrie.client.kex` |
| `2026-07-26 18:09:59` | `cowrie.login.success` |
| `2026-07-26 18:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ae7097743e

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-26 18:10 |
| **Last Seen** | 2026-07-26 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:10:00` | `cowrie.session.connect` |
| `2026-07-26 18:10:00` | `cowrie.client.version` |
| `2026-07-26 18:10:00` | `cowrie.client.kex` |
| `2026-07-26 18:10:01` | `cowrie.login.success` |
| `2026-07-26 18:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21adae1b6347

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-07-26 18:11 |
| **Last Seen** | 2026-07-26 18:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:11:03` | `cowrie.session.connect` |
| `2026-07-26 18:11:04` | `cowrie.client.version` |
| `2026-07-26 18:11:04` | `cowrie.client.kex` |
| `2026-07-26 18:11:05` | `cowrie.login.success` |
| `2026-07-26 18:11:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dec64f4241a

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-07-26 18:11 |
| **Last Seen** | 2026-07-26 18:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:11:10` | `cowrie.session.connect` |
| `2026-07-26 18:11:11` | `cowrie.client.version` |
| `2026-07-26 18:11:11` | `cowrie.client.kex` |
| `2026-07-26 18:11:12` | `cowrie.login.success` |
| `2026-07-26 18:11:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfb3398e269

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-26 18:14 |
| **Last Seen** | 2026-07-26 18:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:14:26` | `cowrie.session.connect` |
| `2026-07-26 18:14:27` | `cowrie.client.version` |
| `2026-07-26 18:14:27` | `cowrie.client.kex` |
| `2026-07-26 18:14:29` | `cowrie.login.success` |
| `2026-07-26 18:14:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8272f8fdd8b

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-07-26 18:14 |
| **Last Seen** | 2026-07-26 18:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:14:40` | `cowrie.session.connect` |
| `2026-07-26 18:14:42` | `cowrie.client.version` |
| `2026-07-26 18:14:42` | `cowrie.client.kex` |
| `2026-07-26 18:14:47` | `cowrie.login.success` |
| `2026-07-26 18:14:48` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38af86856b56

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 18:17 |
| **Last Seen** | 2026-07-26 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:17:37` | `cowrie.session.connect` |
| `2026-07-26 18:17:37` | `cowrie.client.version` |
| `2026-07-26 18:17:37` | `cowrie.client.kex` |
| `2026-07-26 18:17:38` | `cowrie.login.success` |
| `2026-07-26 18:17:38` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:17:38` | `cowrie.direct-tcpip.data` |
| `2026-07-26 18:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98345db2e280

| Field | Detail |
|---|---|
| **Source IP** | `218.87.194[.]83` |
| **First Seen** | 2026-07-26 18:20 |
| **Last Seen** | 2026-07-26 18:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:20:04` | `cowrie.session.connect` |
| `2026-07-26 18:20:04` | `cowrie.client.version` |
| `2026-07-26 18:20:04` | `cowrie.client.kex` |
| `2026-07-26 18:20:05` | `cowrie.login.success` |
| `2026-07-26 18:20:06` | `cowrie.session.params` |
| `2026-07-26 18:20:06` | `cowrie.command.input` |
| `2026-07-26 18:20:06` | `cowrie.log.closed` |
| `2026-07-26 18:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.87.194[.]83` to AbuseIPDB if not already reported
- [ ] Block `218.87.194[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d5f5881d1d

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-07-26 18:29 |
| **Last Seen** | 2026-07-26 18:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:29:48` | `cowrie.session.connect` |
| `2026-07-26 18:29:48` | `cowrie.client.version` |
| `2026-07-26 18:29:48` | `cowrie.client.kex` |
| `2026-07-26 18:29:50` | `cowrie.login.success` |
| `2026-07-26 18:29:51` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5038944421

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-26 18:31 |
| **Last Seen** | 2026-07-26 18:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:31:15` | `cowrie.session.connect` |
| `2026-07-26 18:31:16` | `cowrie.client.version` |
| `2026-07-26 18:31:16` | `cowrie.client.kex` |
| `2026-07-26 18:31:18` | `cowrie.login.success` |
| `2026-07-26 18:31:18` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdcfac7a194a

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-07-26 18:31 |
| **Last Seen** | 2026-07-26 18:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:31:24` | `cowrie.session.connect` |
| `2026-07-26 18:31:25` | `cowrie.client.version` |
| `2026-07-26 18:31:25` | `cowrie.client.kex` |
| `2026-07-26 18:31:26` | `cowrie.login.success` |
| `2026-07-26 18:31:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292c63aab141

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:32 |
| **Last Seen** | 2026-07-26 18:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:32:53` | `cowrie.session.connect` |
| `2026-07-26 18:32:53` | `cowrie.client.version` |
| `2026-07-26 18:32:53` | `cowrie.client.kex` |
| `2026-07-26 18:32:53` | `cowrie.login.success` |
| `2026-07-26 18:32:54` | `cowrie.session.params` |
| `2026-07-26 18:32:54` | `cowrie.command.input` |
| `2026-07-26 18:32:54` | `cowrie.command.failed` |
| `2026-07-26 18:32:54` | `cowrie.log.closed` |
| `2026-07-26 18:32:55` | `cowrie.session.params` |
| `2026-07-26 18:32:55` | `cowrie.command.input` |
| `2026-07-26 18:32:55` | `cowrie.session.file_download` |
| `2026-07-26 18:32:55` | `cowrie.log.closed` |
| `2026-07-26 18:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28cf6277ef3

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:32 |
| **Last Seen** | 2026-07-26 18:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:32:55` | `cowrie.session.connect` |
| `2026-07-26 18:32:55` | `cowrie.client.version` |
| `2026-07-26 18:32:55` | `cowrie.client.kex` |
| `2026-07-26 18:32:56` | `cowrie.login.success` |
| `2026-07-26 18:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-364cf9815914

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:32 |
| **Last Seen** | 2026-07-26 18:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:32:56` | `cowrie.session.connect` |
| `2026-07-26 18:32:56` | `cowrie.client.version` |
| `2026-07-26 18:32:56` | `cowrie.client.kex` |
| `2026-07-26 18:32:57` | `cowrie.login.success` |
| `2026-07-26 18:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5427b3f0b772

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-07-26 18:33 |
| **Last Seen** | 2026-07-26 18:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:33:11` | `cowrie.session.connect` |
| `2026-07-26 18:33:12` | `cowrie.client.version` |
| `2026-07-26 18:33:12` | `cowrie.client.kex` |
| `2026-07-26 18:33:15` | `cowrie.login.success` |
| `2026-07-26 18:33:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7cf9163b7c

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-07-26 18:33 |
| **Last Seen** | 2026-07-26 18:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:33:25` | `cowrie.session.connect` |
| `2026-07-26 18:33:26` | `cowrie.client.version` |
| `2026-07-26 18:33:26` | `cowrie.client.kex` |
| `2026-07-26 18:33:27` | `cowrie.login.success` |
| `2026-07-26 18:33:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06599451f973

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-26 18:35 |
| **Last Seen** | 2026-07-26 18:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:35:31` | `cowrie.session.connect` |
| `2026-07-26 18:35:31` | `cowrie.client.version` |
| `2026-07-26 18:35:31` | `cowrie.client.kex` |
| `2026-07-26 18:35:32` | `cowrie.login.success` |
| `2026-07-26 18:35:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882515a61346

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:37 |
| **Last Seen** | 2026-07-26 18:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:37:22` | `cowrie.session.connect` |
| `2026-07-26 18:37:22` | `cowrie.client.version` |
| `2026-07-26 18:37:22` | `cowrie.client.kex` |
| `2026-07-26 18:37:22` | `cowrie.login.success` |
| `2026-07-26 18:37:23` | `cowrie.session.params` |
| `2026-07-26 18:37:23` | `cowrie.command.input` |
| `2026-07-26 18:37:23` | `cowrie.command.failed` |
| `2026-07-26 18:37:23` | `cowrie.log.closed` |
| `2026-07-26 18:37:24` | `cowrie.session.params` |
| `2026-07-26 18:37:24` | `cowrie.command.input` |
| `2026-07-26 18:37:24` | `cowrie.session.file_download` |
| `2026-07-26 18:37:24` | `cowrie.log.closed` |
| `2026-07-26 18:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df7206c5b86

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:37 |
| **Last Seen** | 2026-07-26 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:37:25` | `cowrie.session.connect` |
| `2026-07-26 18:37:25` | `cowrie.client.version` |
| `2026-07-26 18:37:25` | `cowrie.client.kex` |
| `2026-07-26 18:37:25` | `cowrie.login.success` |
| `2026-07-26 18:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fb4d4effde

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-07-26 18:37 |
| **Last Seen** | 2026-07-26 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:37:25` | `cowrie.session.connect` |
| `2026-07-26 18:37:25` | `cowrie.client.version` |
| `2026-07-26 18:37:26` | `cowrie.client.kex` |
| `2026-07-26 18:37:26` | `cowrie.login.success` |
| `2026-07-26 18:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0485022bf62e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-26 18:38 |
| **Last Seen** | 2026-07-26 18:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:38:45` | `cowrie.session.connect` |
| `2026-07-26 18:38:46` | `cowrie.client.version` |
| `2026-07-26 18:38:46` | `cowrie.client.kex` |
| `2026-07-26 18:38:47` | `cowrie.login.success` |
| `2026-07-26 18:38:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ac63821342

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-26 18:54 |
| **Last Seen** | 2026-07-26 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:54:09` | `cowrie.session.connect` |
| `2026-07-26 18:54:10` | `cowrie.client.version` |
| `2026-07-26 18:54:10` | `cowrie.client.kex` |
| `2026-07-26 18:54:12` | `cowrie.login.success` |
| `2026-07-26 18:54:12` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cd0b6bb817

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-26 18:54 |
| **Last Seen** | 2026-07-26 18:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:54:18` | `cowrie.session.connect` |
| `2026-07-26 18:54:19` | `cowrie.client.version` |
| `2026-07-26 18:54:19` | `cowrie.client.kex` |
| `2026-07-26 18:54:21` | `cowrie.login.success` |
| `2026-07-26 18:54:22` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `217.60.195[.]127` | **11** | 2026-07-26 17:51 | 2026-07-26 18:07 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-26 17:14 | 2026-07-26 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]47` | **4** | 2026-07-26 17:51 | 2026-07-26 17:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | **4** | 2026-07-26 17:18 | 2026-07-26 17:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]49` | **3** | 2026-07-26 17:51 | 2026-07-26 17:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-26 18:44 | 2026-07-26 18:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-26 17:24 | 2026-07-26 17:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-26 17:43 | 2026-07-26 17:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-07-26 17:10 | 2026-07-26 18:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]48` | **2** | 2026-07-26 17:51 | 2026-07-26 17:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **2** | 2026-07-26 18:52 | 2026-07-26 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.230[.]94` | 1 | 2026-07-26 18:09 | 2026-07-26 18:10 | 46s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-07-26 18:08 | 2026-07-26 18:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `182.95.153[.]122` | 1 | 2026-07-26 17:40 | 2026-07-26 17:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]50` | 1 | 2026-07-26 17:51 | 2026-07-26 17:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `190.112.191[.]60` | 1 | 2026-07-26 18:04 | 2026-07-26 18:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.23.95[.]14` | 1 | 2026-07-26 17:18 | 2026-07-26 17:18 | 5s | 0 | `T1592` | 🟢 LOW |
| `218.87.194[.]83` | 1 | 2026-07-26 18:20 | 2026-07-26 18:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]2` | 1 | 2026-07-26 17:18 | 2026-07-26 17:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.129.41[.]146` | 1 | 2026-07-26 17:50 | 2026-07-26 17:52 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `81.214.75[.]248` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `111.70.32[.]51` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |
| `66.132.195[.]82` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `103.68.22[.]115` | IN | Anonet Network Private Limited | **100** ⚠️ | 17 |
| `123.123.196[.]140` | CN | China Unicom Beijing province network | **100** ⚠️ | 6 |
| `36.154.134[.]146` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `208.96.233[.]67` | CA | Cogeco Connexion inc | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 78 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 142 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (8.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 78 priority case(s) shown individually · 20 recon entry/entries in table (11 group(s) consolidating 43 session(s)).

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
_Report time: 2026-07-26T19:18:17Z_

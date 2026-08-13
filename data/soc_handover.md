# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-13 |
| **Generated At** | 2026-08-13T11:06:19Z |
| **Shift Time** | 11:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **143** |
| Confirmed Threats | **119** |
| False Positives Filtered | **24** (16.8%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **31** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **91** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **16** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **58** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 15 |
| `root` | 14 |
| `nobody` | 9 |
| `345gs5662d34` | 6 |
| `blank` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `qwerty12345` | 5 |
| `test` | 5 |
| `` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `admin` | `qwerty12345` | 5 |
| `blank` | `test` | 5 |
| `admin` | `` | 4 |
| `root` | `LeitboGi0ro` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `oracle` | `oracle321` | `203.25.208.110` | 2026-08-13T08:56:02 |
| `345gs5662d34` | `345gs5662d34` | `203.25.208.110` | 2026-08-13T08:56:06 |
| `oracle` | `3245gs5662d34` | `203.25.208.110` | 2026-08-13T08:56:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-13T08:59:20 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-13T08:59:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.236.228.86` | 2026-08-13T09:01:59 |
| `support` | `support` | `176.53.159.196` | 2026-08-13T09:02:14 |
| `nobody` | `pass` | `10.0.0.73` | 2026-08-13T09:06:22 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-13T09:07:21 |
| `root` | `987654321` | `10.0.0.73` | 2026-08-13T09:07:33 |
| `admin` | `admin` | `185.126.5.240` | 2026-08-13T09:10:32 |
| `support` | `support` | `10.0.0.73` | 2026-08-13T09:17:35 |
| `centos` | `123123123` | `113.28.86.1` | 2026-08-13T09:20:03 |
| `centos` | `123123123` | `203.192.211.180` | 2026-08-13T09:20:11 |
| `centos` | `123123123` | `62.201.212.54` | 2026-08-13T09:20:23 |
| `nobody` | `pass` | `65.20.149.239` | 2026-08-13T09:23:45 |
| `nobody` | `pass` | `203.123.219.137` | 2026-08-13T09:23:58 |
| `nobody` | `maintenance` | `77.89.245.118` | 2026-08-13T09:29:07 |
| `nobody` | `maintenance` | `155.212.17.174` | 2026-08-13T09:29:19 |
| `guest` | `12345678` | `120.48.135.189` | 2026-08-13T09:34:24 |
| `root` | `root55` | `10.0.0.73` | 2026-08-13T09:35:53 |
| `admin` | `admin2005` | `83.239.84.130` | 2026-08-13T09:43:58 |
| `root` | `root55` | `65.20.134.97` | 2026-08-13T09:54:41 |
| `nobody` | `maintenance` | `183.247.171.186` | 2026-08-13T09:58:13 |
| `admin` | `admin2005` | `179.181.133.153` | 2026-08-13T10:00:24 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-13T10:00:24 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-13T10:00:25 |
| `admin` | `admin2005` | `122.170.100.253` | 2026-08-13T10:00:32 |
| `root` | `tongshi` | `46.249.102.182` | 2026-08-13T10:03:14 |
| `345gs5662d34` | `345gs5662d34` | `46.249.102.182` | 2026-08-13T10:03:16 |
| `root` | `3245gs5662d34` | `46.249.102.182` | 2026-08-13T10:03:17 |
| `system` | `12345` | `135.125.235.107` | 2026-08-13T10:06:14 |
| `345gs5662d34` | `345gs5662d34` | `135.125.235.107` | 2026-08-13T10:06:16 |
| `system` | `3245gs5662d34` | `135.125.235.107` | 2026-08-13T10:06:17 |
| `admin` | `qwerty12345` | `10.0.0.73` | 2026-08-13T10:10:26 |
| `nobody` | `p@ssw0rd` | `10.0.0.73` | 2026-08-13T10:15:13 |
| `blank` | `test` | `10.0.0.73` | 2026-08-13T10:16:50 |
| `blank` | `test` | `188.219.104.210` | 2026-08-13T10:18:35 |
| `blank` | `test` | `221.182.185.190` | 2026-08-13T10:18:48 |
| `admin` | `qwerty12345` | `202.82.20.241` | 2026-08-13T10:29:13 |
| `admin` | `qwerty12345` | `196.188.93.169` | 2026-08-13T10:29:25 |
| `admin` | `qwerty12345` | `183.63.220.210` | 2026-08-13T10:29:27 |
| `admin` | `qwerty12345` | `165.227.129.203` | 2026-08-13T10:29:35 |
| `nobody` | `p@ssw0rd` | `60.249.251.88` | 2026-08-13T10:32:51 |
| `blank` | `test` | `49.124.152.253` | 2026-08-13T10:35:04 |
| `debian` | `123654` | `103.158.138.179` | 2026-08-13T10:37:53 |
| `debian` | `123654` | `177.174.89.99` | 2026-08-13T10:38:01 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-13T10:47:21 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-13T10:49:50 |
| `username` | `12345` | `182.253.221.210` | 2026-08-13T10:52:05 |
| `345gs5662d34` | `345gs5662d34` | `182.253.221.210` | 2026-08-13T10:52:09 |
| `username` | `3245gs5662d34` | `182.253.221.210` | 2026-08-13T10:52:11 |
| `postgres` | `P0$tgr3$` | `2.59.163.225` | 2026-08-13T10:52:50 |
| `345gs5662d34` | `345gs5662d34` | `2.59.163.225` | 2026-08-13T10:52:53 |
| `postgres` | `3245gs5662d34` | `2.59.163.225` | 2026-08-13T10:52:54 |
| `mega` | `mega` | `192.109.220.3` | 2026-08-13T10:54:55 |
| `345gs5662d34` | `345gs5662d34` | `192.109.220.3` | 2026-08-13T10:54:58 |
| `mega` | `3245gs5662d34` | `192.109.220.3` | 2026-08-13T10:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **143** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 24 |
| OpenSSH | 22 |
| Paramiko (Python) | 6 |
| Go SSH scanner | 5 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 22 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.25.208.110`, `192.109.220.3`, `46.249.102.182`, `2.59.163.225`, `182.253.221.210`, `135.125.235.107`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **62** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS33363` | Charter Communications, Inc | 2 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b721eb9f9ad5

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:56 |
| **Last Seen** | 2026-08-13 08:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:56:00` | `cowrie.session.connect` |
| `2026-08-13 08:56:00` | `cowrie.client.version` |
| `2026-08-13 08:56:01` | `cowrie.client.kex` |
| `2026-08-13 08:56:02` | `cowrie.login.success` |
| `2026-08-13 08:56:03` | `cowrie.session.params` |
| `2026-08-13 08:56:03` | `cowrie.command.input` |
| `2026-08-13 08:56:03` | `cowrie.command.failed` |
| `2026-08-13 08:56:03` | `cowrie.log.closed` |
| `2026-08-13 08:56:04` | `cowrie.session.params` |
| `2026-08-13 08:56:04` | `cowrie.command.input` |
| `2026-08-13 08:56:04` | `cowrie.session.file_download` |
| `2026-08-13 08:56:04` | `cowrie.log.closed` |
| `2026-08-13 08:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b432cd64584

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:56 |
| **Last Seen** | 2026-08-13 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:56:05` | `cowrie.session.connect` |
| `2026-08-13 08:56:05` | `cowrie.client.version` |
| `2026-08-13 08:56:05` | `cowrie.client.kex` |
| `2026-08-13 08:56:06` | `cowrie.login.success` |
| `2026-08-13 08:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b7eb21a258

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:56 |
| **Last Seen** | 2026-08-13 08:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:56:07` | `cowrie.session.connect` |
| `2026-08-13 08:56:07` | `cowrie.client.version` |
| `2026-08-13 08:56:07` | `cowrie.client.kex` |
| `2026-08-13 08:56:09` | `cowrie.login.success` |
| `2026-08-13 08:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53da2beff4f7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-13 08:59 |
| **Last Seen** | 2026-08-13 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:59:19` | `cowrie.session.connect` |
| `2026-08-13 08:59:19` | `cowrie.client.version` |
| `2026-08-13 08:59:20` | `cowrie.client.kex` |
| `2026-08-13 08:59:20` | `cowrie.login.success` |
| `2026-08-13 08:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0ef33eb573

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-13 08:59 |
| **Last Seen** | 2026-08-13 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:59:20` | `cowrie.session.connect` |
| `2026-08-13 08:59:20` | `cowrie.client.version` |
| `2026-08-13 08:59:20` | `cowrie.client.kex` |
| `2026-08-13 08:59:21` | `cowrie.login.success` |
| `2026-08-13 08:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e56cdb28a52

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]86` |
| **First Seen** | 2026-08-13 09:01 |
| **Last Seen** | 2026-08-13 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:01:59` | `cowrie.session.connect` |
| `2026-08-13 09:01:59` | `cowrie.login.success` |
| `2026-08-13 09:01:59` | `cowrie.session.params` |
| `2026-08-13 09:01:59` | `cowrie.command.input` |
| `2026-08-13 09:01:59` | `cowrie.command.input` |
| `2026-08-13 09:01:59` | `cowrie.command.failed` |
| `2026-08-13 09:01:59` | `cowrie.command.input` |
| `2026-08-13 09:01:59` | `cowrie.command.failed` |
| `2026-08-13 09:01:59` | `cowrie.command.input` |
| `2026-08-13 09:01:59` | `cowrie.log.closed` |
| `2026-08-13 09:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]86` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf802b512df1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 09:02 |
| **Last Seen** | 2026-08-13 09:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:02:13` | `cowrie.session.connect` |
| `2026-08-13 09:02:13` | `cowrie.client.version` |
| `2026-08-13 09:02:13` | `cowrie.client.kex` |
| `2026-08-13 09:02:14` | `cowrie.login.success` |
| `2026-08-13 09:02:14` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:02:14` | `cowrie.direct-tcpip.data` |
| `2026-08-13 09:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37fde2fda09c

| Field | Detail |
|---|---|
| **Source IP** | `185.126.5[.]240` |
| **First Seen** | 2026-08-13 09:10 |
| **Last Seen** | 2026-08-13 09:11 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:10:31` | `cowrie.session.connect` |
| `2026-08-13 09:10:32` | `cowrie.telnet.option` |
| `2026-08-13 09:10:32` | `cowrie.telnet.option` |
| `2026-08-13 09:10:32` | `cowrie.login.success` |
| `2026-08-13 09:10:33` | `cowrie.session.params` |
| `2026-08-13 09:10:33` | `cowrie.telnet.option` |
| `2026-08-13 09:10:33` | `cowrie.telnet.option` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.failed` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:10:33` | `cowrie.command.input` |
| `2026-08-13 09:11:34` | `cowrie.log.closed` |
| `2026-08-13 09:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.126.5[.]240` to AbuseIPDB if not already reported
- [ ] Block `185.126.5[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc500535c599

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-08-13 09:20 |
| **Last Seen** | 2026-08-13 09:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:20:01` | `cowrie.session.connect` |
| `2026-08-13 09:20:02` | `cowrie.client.version` |
| `2026-08-13 09:20:02` | `cowrie.client.kex` |
| `2026-08-13 09:20:03` | `cowrie.login.success` |
| `2026-08-13 09:20:04` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ebad08af06

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-13 09:20 |
| **Last Seen** | 2026-08-13 09:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:20:09` | `cowrie.session.connect` |
| `2026-08-13 09:20:10` | `cowrie.client.version` |
| `2026-08-13 09:20:10` | `cowrie.client.kex` |
| `2026-08-13 09:20:11` | `cowrie.login.success` |
| `2026-08-13 09:20:12` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3916000ac78

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-13 09:20 |
| **Last Seen** | 2026-08-13 09:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:20:22` | `cowrie.session.connect` |
| `2026-08-13 09:20:22` | `cowrie.client.version` |
| `2026-08-13 09:20:22` | `cowrie.client.kex` |
| `2026-08-13 09:20:23` | `cowrie.login.success` |
| `2026-08-13 09:20:24` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757667d255cf

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-08-13 09:23 |
| **Last Seen** | 2026-08-13 09:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:23:43` | `cowrie.session.connect` |
| `2026-08-13 09:23:43` | `cowrie.client.version` |
| `2026-08-13 09:23:43` | `cowrie.client.kex` |
| `2026-08-13 09:23:45` | `cowrie.login.success` |
| `2026-08-13 09:23:45` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb18c093cf81

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-08-13 09:23 |
| **Last Seen** | 2026-08-13 09:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:23:55` | `cowrie.session.connect` |
| `2026-08-13 09:23:55` | `cowrie.client.version` |
| `2026-08-13 09:23:55` | `cowrie.client.kex` |
| `2026-08-13 09:23:58` | `cowrie.login.success` |
| `2026-08-13 09:23:59` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b27456bd33

| Field | Detail |
|---|---|
| **Source IP** | `77.89.245[.]118` |
| **First Seen** | 2026-08-13 09:29 |
| **Last Seen** | 2026-08-13 09:34 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:29:06` | `cowrie.session.connect` |
| `2026-08-13 09:29:07` | `cowrie.client.version` |
| `2026-08-13 09:29:07` | `cowrie.client.kex` |
| `2026-08-13 09:29:07` | `cowrie.login.success` |
| `2026-08-13 09:29:08` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.89.245[.]118` to AbuseIPDB if not already reported
- [ ] Block `77.89.245[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3a752ee759c

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-13 09:29 |
| **Last Seen** | 2026-08-13 09:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:29:17` | `cowrie.session.connect` |
| `2026-08-13 09:29:18` | `cowrie.client.version` |
| `2026-08-13 09:29:18` | `cowrie.client.kex` |
| `2026-08-13 09:29:19` | `cowrie.login.success` |
| `2026-08-13 09:29:19` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c6223a734e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-08-13 09:34 |
| **Last Seen** | 2026-08-13 09:39 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:34:22` | `cowrie.session.connect` |
| `2026-08-13 09:34:22` | `cowrie.client.version` |
| `2026-08-13 09:34:23` | `cowrie.client.kex` |
| `2026-08-13 09:34:24` | `cowrie.login.success` |
| `2026-08-13 09:34:25` | `cowrie.session.params` |
| `2026-08-13 09:34:25` | `cowrie.command.input` |
| `2026-08-13 09:34:25` | `cowrie.command.failed` |
| `2026-08-13 09:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd68e2cced2

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-08-13 09:43 |
| **Last Seen** | 2026-08-13 09:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:43:56` | `cowrie.session.connect` |
| `2026-08-13 09:43:57` | `cowrie.client.version` |
| `2026-08-13 09:43:57` | `cowrie.client.kex` |
| `2026-08-13 09:43:58` | `cowrie.login.success` |
| `2026-08-13 09:43:58` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2caf71c730

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-13 09:54 |
| **Last Seen** | 2026-08-13 09:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:54:40` | `cowrie.session.connect` |
| `2026-08-13 09:54:40` | `cowrie.client.version` |
| `2026-08-13 09:54:40` | `cowrie.client.kex` |
| `2026-08-13 09:54:41` | `cowrie.login.success` |
| `2026-08-13 09:54:41` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a044930826aa

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-13 09:58 |
| **Last Seen** | 2026-08-13 09:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:58:08` | `cowrie.session.connect` |
| `2026-08-13 09:58:09` | `cowrie.client.version` |
| `2026-08-13 09:58:09` | `cowrie.client.kex` |
| `2026-08-13 09:58:13` | `cowrie.login.success` |
| `2026-08-13 09:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80886d753698

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 09:59 |
| **Last Seen** | 2026-08-13 09:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 09:59:21` | `cowrie.session.connect` |
| `2026-08-13 09:59:21` | `cowrie.client.version` |
| `2026-08-13 09:59:22` | `cowrie.client.kex` |
| `2026-08-13 09:59:22` | `cowrie.login.success` |
| `2026-08-13 09:59:22` | `cowrie.direct-tcpip.request` |
| `2026-08-13 09:59:22` | `cowrie.direct-tcpip.data` |
| `2026-08-13 09:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac60aefe750

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-13 10:00 |
| **Last Seen** | 2026-08-13 10:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:00:21` | `cowrie.session.connect` |
| `2026-08-13 10:00:22` | `cowrie.client.version` |
| `2026-08-13 10:00:22` | `cowrie.client.kex` |
| `2026-08-13 10:00:24` | `cowrie.login.success` |
| `2026-08-13 10:00:24` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671fde64aeb5

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-13 10:00 |
| **Last Seen** | 2026-08-13 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:00:23` | `cowrie.session.connect` |
| `2026-08-13 10:00:23` | `cowrie.client.version` |
| `2026-08-13 10:00:24` | `cowrie.client.kex` |
| `2026-08-13 10:00:24` | `cowrie.login.success` |
| `2026-08-13 10:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6c536e6e8c

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-13 10:00 |
| **Last Seen** | 2026-08-13 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:00:24` | `cowrie.session.connect` |
| `2026-08-13 10:00:24` | `cowrie.client.version` |
| `2026-08-13 10:00:24` | `cowrie.client.kex` |
| `2026-08-13 10:00:25` | `cowrie.login.success` |
| `2026-08-13 10:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeee0df75e61

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-13 10:00 |
| **Last Seen** | 2026-08-13 10:02 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:00:26` | `cowrie.session.connect` |
| `2026-08-13 10:00:26` | `cowrie.client.version` |
| `2026-08-13 10:00:26` | `cowrie.client.kex` |
| `2026-08-13 10:00:27` | `cowrie.login.success` |
| `2026-08-13 10:00:29` | `cowrie.session.file_upload` |
| `2026-08-13 10:00:30` | `cowrie.session.params` |
| `2026-08-13 10:00:30` | `cowrie.command.input` |
| `2026-08-13 10:00:30` | `cowrie.command.input` |
| `2026-08-13 10:00:30` | `cowrie.command.input` |
| `2026-08-13 10:00:30` | `cowrie.command.failed` |
| `2026-08-13 10:00:30` | `cowrie.log.closed` |
| `2026-08-13 10:00:31` | `cowrie.session.params` |
| `2026-08-13 10:00:31` | `cowrie.command.input` |
| `2026-08-13 10:00:31` | `cowrie.log.closed` |
| `2026-08-13 10:00:32` | `cowrie.session.params` |
| `2026-08-13 10:00:32` | `cowrie.command.input` |
| `2026-08-13 10:00:33` | `cowrie.log.closed` |
| `2026-08-13 10:00:34` | `cowrie.session.params` |
| `2026-08-13 10:00:34` | `cowrie.command.input` |
| `2026-08-13 10:00:34` | `cowrie.command.failed` |
| `2026-08-13 10:00:34` | `cowrie.command.failed` |
| `2026-08-13 10:01:35` | `cowrie.session.params` |
| `2026-08-13 10:01:35` | `cowrie.command.input` |
| `2026-08-13 10:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c483a989e819

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-13 10:00 |
| **Last Seen** | 2026-08-13 10:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:00:29` | `cowrie.session.connect` |
| `2026-08-13 10:00:30` | `cowrie.client.version` |
| `2026-08-13 10:00:30` | `cowrie.client.kex` |
| `2026-08-13 10:00:32` | `cowrie.login.success` |
| `2026-08-13 10:00:32` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b890662d95

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-13 10:02 |
| **Last Seen** | 2026-08-13 10:04 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:02:37` | `cowrie.session.connect` |
| `2026-08-13 10:02:37` | `cowrie.client.version` |
| `2026-08-13 10:02:37` | `cowrie.client.kex` |
| `2026-08-13 10:02:38` | `cowrie.login.success` |
| `2026-08-13 10:02:40` | `cowrie.session.file_upload` |
| `2026-08-13 10:02:41` | `cowrie.session.params` |
| `2026-08-13 10:02:41` | `cowrie.command.input` |
| `2026-08-13 10:02:41` | `cowrie.command.input` |
| `2026-08-13 10:02:41` | `cowrie.command.input` |
| `2026-08-13 10:02:41` | `cowrie.command.failed` |
| `2026-08-13 10:02:41` | `cowrie.log.closed` |
| `2026-08-13 10:02:42` | `cowrie.session.params` |
| `2026-08-13 10:02:42` | `cowrie.command.input` |
| `2026-08-13 10:02:42` | `cowrie.log.closed` |
| `2026-08-13 10:02:43` | `cowrie.session.params` |
| `2026-08-13 10:02:43` | `cowrie.command.input` |
| `2026-08-13 10:02:43` | `cowrie.log.closed` |
| `2026-08-13 10:02:45` | `cowrie.session.params` |
| `2026-08-13 10:02:45` | `cowrie.command.input` |
| `2026-08-13 10:02:45` | `cowrie.command.failed` |
| `2026-08-13 10:02:45` | `cowrie.command.failed` |
| `2026-08-13 10:03:46` | `cowrie.session.params` |
| `2026-08-13 10:03:46` | `cowrie.command.input` |
| `2026-08-13 10:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a146278c4343

| Field | Detail |
|---|---|
| **Source IP** | `46.249.102[.]182` |
| **First Seen** | 2026-08-13 10:03 |
| **Last Seen** | 2026-08-13 10:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:03:13` | `cowrie.session.connect` |
| `2026-08-13 10:03:13` | `cowrie.client.version` |
| `2026-08-13 10:03:13` | `cowrie.client.kex` |
| `2026-08-13 10:03:14` | `cowrie.login.success` |
| `2026-08-13 10:03:15` | `cowrie.session.params` |
| `2026-08-13 10:03:15` | `cowrie.command.input` |
| `2026-08-13 10:03:15` | `cowrie.command.failed` |
| `2026-08-13 10:03:15` | `cowrie.log.closed` |
| `2026-08-13 10:03:15` | `cowrie.session.params` |
| `2026-08-13 10:03:15` | `cowrie.command.input` |
| `2026-08-13 10:03:16` | `cowrie.session.file_download` |
| `2026-08-13 10:03:16` | `cowrie.log.closed` |
| `2026-08-13 10:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.249.102[.]182` to AbuseIPDB if not already reported
- [ ] Block `46.249.102[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4ad8d98145

| Field | Detail |
|---|---|
| **Source IP** | `46.249.102[.]182` |
| **First Seen** | 2026-08-13 10:03 |
| **Last Seen** | 2026-08-13 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:03:16` | `cowrie.session.connect` |
| `2026-08-13 10:03:16` | `cowrie.client.version` |
| `2026-08-13 10:03:16` | `cowrie.client.kex` |
| `2026-08-13 10:03:16` | `cowrie.login.success` |
| `2026-08-13 10:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.249.102[.]182` to AbuseIPDB if not already reported
- [ ] Block `46.249.102[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d2aa4a12c1

| Field | Detail |
|---|---|
| **Source IP** | `46.249.102[.]182` |
| **First Seen** | 2026-08-13 10:03 |
| **Last Seen** | 2026-08-13 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:03:16` | `cowrie.session.connect` |
| `2026-08-13 10:03:16` | `cowrie.client.version` |
| `2026-08-13 10:03:16` | `cowrie.client.kex` |
| `2026-08-13 10:03:17` | `cowrie.login.success` |
| `2026-08-13 10:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.249.102[.]182` to AbuseIPDB if not already reported
- [ ] Block `46.249.102[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c0817785f6

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-13 10:06 |
| **Last Seen** | 2026-08-13 10:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:06:13` | `cowrie.session.connect` |
| `2026-08-13 10:06:13` | `cowrie.client.version` |
| `2026-08-13 10:06:13` | `cowrie.client.kex` |
| `2026-08-13 10:06:14` | `cowrie.login.success` |
| `2026-08-13 10:06:14` | `cowrie.session.params` |
| `2026-08-13 10:06:14` | `cowrie.command.input` |
| `2026-08-13 10:06:14` | `cowrie.command.failed` |
| `2026-08-13 10:06:15` | `cowrie.log.closed` |
| `2026-08-13 10:06:15` | `cowrie.session.params` |
| `2026-08-13 10:06:15` | `cowrie.command.input` |
| `2026-08-13 10:06:16` | `cowrie.session.file_download` |
| `2026-08-13 10:06:16` | `cowrie.log.closed` |
| `2026-08-13 10:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b43e9c0de8

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-13 10:06 |
| **Last Seen** | 2026-08-13 10:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:06:16` | `cowrie.session.connect` |
| `2026-08-13 10:06:16` | `cowrie.client.version` |
| `2026-08-13 10:06:16` | `cowrie.client.kex` |
| `2026-08-13 10:06:16` | `cowrie.login.success` |
| `2026-08-13 10:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256be0465068

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-13 10:06 |
| **Last Seen** | 2026-08-13 10:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:06:16` | `cowrie.session.connect` |
| `2026-08-13 10:06:16` | `cowrie.client.version` |
| `2026-08-13 10:06:16` | `cowrie.client.kex` |
| `2026-08-13 10:06:17` | `cowrie.login.success` |
| `2026-08-13 10:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6362b88c0251

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-08-13 10:18 |
| **Last Seen** | 2026-08-13 10:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:18:33` | `cowrie.session.connect` |
| `2026-08-13 10:18:34` | `cowrie.client.version` |
| `2026-08-13 10:18:34` | `cowrie.client.kex` |
| `2026-08-13 10:18:35` | `cowrie.login.success` |
| `2026-08-13 10:18:35` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0893eb6859

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-13 10:18 |
| **Last Seen** | 2026-08-13 10:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:18:45` | `cowrie.session.connect` |
| `2026-08-13 10:18:45` | `cowrie.client.version` |
| `2026-08-13 10:18:45` | `cowrie.client.kex` |
| `2026-08-13 10:18:48` | `cowrie.login.success` |
| `2026-08-13 10:18:49` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e8a345d5f0b

| Field | Detail |
|---|---|
| **Source IP** | `202.82.20[.]241` |
| **First Seen** | 2026-08-13 10:29 |
| **Last Seen** | 2026-08-13 10:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:29:10` | `cowrie.session.connect` |
| `2026-08-13 10:29:11` | `cowrie.client.version` |
| `2026-08-13 10:29:11` | `cowrie.client.kex` |
| `2026-08-13 10:29:13` | `cowrie.login.success` |
| `2026-08-13 10:29:14` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.82.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `202.82.20[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd86030fb9d

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-13 10:29 |
| **Last Seen** | 2026-08-13 10:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:29:23` | `cowrie.session.connect` |
| `2026-08-13 10:29:24` | `cowrie.client.version` |
| `2026-08-13 10:29:24` | `cowrie.client.kex` |
| `2026-08-13 10:29:25` | `cowrie.login.success` |
| `2026-08-13 10:29:25` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725bf84332de

| Field | Detail |
|---|---|
| **Source IP** | `183.63.220[.]210` |
| **First Seen** | 2026-08-13 10:29 |
| **Last Seen** | 2026-08-13 10:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:29:24` | `cowrie.session.connect` |
| `2026-08-13 10:29:25` | `cowrie.client.version` |
| `2026-08-13 10:29:26` | `cowrie.client.kex` |
| `2026-08-13 10:29:27` | `cowrie.login.success` |
| `2026-08-13 10:29:29` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.63.220[.]210` to AbuseIPDB if not already reported
- [ ] Block `183.63.220[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e88c20cd2e

| Field | Detail |
|---|---|
| **Source IP** | `165.227.129[.]203` |
| **First Seen** | 2026-08-13 10:29 |
| **Last Seen** | 2026-08-13 10:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:29:35` | `cowrie.session.connect` |
| `2026-08-13 10:29:35` | `cowrie.client.version` |
| `2026-08-13 10:29:35` | `cowrie.client.kex` |
| `2026-08-13 10:29:35` | `cowrie.login.success` |
| `2026-08-13 10:29:36` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `165.227.129[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ca623d9628

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-08-13 10:32 |
| **Last Seen** | 2026-08-13 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:32:47` | `cowrie.session.connect` |
| `2026-08-13 10:32:48` | `cowrie.client.version` |
| `2026-08-13 10:32:48` | `cowrie.client.kex` |
| `2026-08-13 10:32:51` | `cowrie.login.success` |
| `2026-08-13 10:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338278d820cd

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]253` |
| **First Seen** | 2026-08-13 10:35 |
| **Last Seen** | 2026-08-13 10:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:35:02` | `cowrie.session.connect` |
| `2026-08-13 10:35:02` | `cowrie.client.version` |
| `2026-08-13 10:35:02` | `cowrie.client.kex` |
| `2026-08-13 10:35:04` | `cowrie.login.success` |
| `2026-08-13 10:35:05` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9af6c5c29b4

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-13 10:37 |
| **Last Seen** | 2026-08-13 10:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:37:50` | `cowrie.session.connect` |
| `2026-08-13 10:37:51` | `cowrie.client.version` |
| `2026-08-13 10:37:51` | `cowrie.client.kex` |
| `2026-08-13 10:37:53` | `cowrie.login.success` |
| `2026-08-13 10:37:53` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c5926af5da

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-13 10:37 |
| **Last Seen** | 2026-08-13 10:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:37:59` | `cowrie.session.connect` |
| `2026-08-13 10:37:59` | `cowrie.client.version` |
| `2026-08-13 10:37:59` | `cowrie.client.kex` |
| `2026-08-13 10:38:01` | `cowrie.login.success` |
| `2026-08-13 10:38:01` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf8de8df8a3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 10:47 |
| **Last Seen** | 2026-08-13 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:47:18` | `cowrie.session.connect` |
| `2026-08-13 10:47:18` | `cowrie.client.version` |
| `2026-08-13 10:47:18` | `cowrie.client.kex` |
| `2026-08-13 10:47:19` | `cowrie.login.success` |
| `2026-08-13 10:47:19` | `cowrie.direct-tcpip.request` |
| `2026-08-13 10:47:19` | `cowrie.direct-tcpip.data` |
| `2026-08-13 10:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312e78758bfb

| Field | Detail |
|---|---|
| **Source IP** | `182.253.221[.]210` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:03` | `cowrie.session.connect` |
| `2026-08-13 10:52:03` | `cowrie.client.version` |
| `2026-08-13 10:52:04` | `cowrie.client.kex` |
| `2026-08-13 10:52:05` | `cowrie.login.success` |
| `2026-08-13 10:52:06` | `cowrie.session.params` |
| `2026-08-13 10:52:06` | `cowrie.command.input` |
| `2026-08-13 10:52:06` | `cowrie.command.failed` |
| `2026-08-13 10:52:06` | `cowrie.log.closed` |
| `2026-08-13 10:52:07` | `cowrie.session.params` |
| `2026-08-13 10:52:07` | `cowrie.command.input` |
| `2026-08-13 10:52:07` | `cowrie.session.file_download` |
| `2026-08-13 10:52:07` | `cowrie.log.closed` |
| `2026-08-13 10:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `182.253.221[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bdeea9328b

| Field | Detail |
|---|---|
| **Source IP** | `182.253.221[.]210` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:07` | `cowrie.session.connect` |
| `2026-08-13 10:52:07` | `cowrie.client.version` |
| `2026-08-13 10:52:08` | `cowrie.client.kex` |
| `2026-08-13 10:52:09` | `cowrie.login.success` |
| `2026-08-13 10:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `182.253.221[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0034b26ceac

| Field | Detail |
|---|---|
| **Source IP** | `182.253.221[.]210` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:09` | `cowrie.session.connect` |
| `2026-08-13 10:52:09` | `cowrie.client.version` |
| `2026-08-13 10:52:10` | `cowrie.client.kex` |
| `2026-08-13 10:52:11` | `cowrie.login.success` |
| `2026-08-13 10:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `182.253.221[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a9cb88514f

| Field | Detail |
|---|---|
| **Source IP** | `2.59.163[.]225` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:50` | `cowrie.session.connect` |
| `2026-08-13 10:52:50` | `cowrie.client.version` |
| `2026-08-13 10:52:50` | `cowrie.client.kex` |
| `2026-08-13 10:52:50` | `cowrie.login.success` |
| `2026-08-13 10:52:51` | `cowrie.session.params` |
| `2026-08-13 10:52:51` | `cowrie.command.input` |
| `2026-08-13 10:52:51` | `cowrie.command.failed` |
| `2026-08-13 10:52:52` | `cowrie.log.closed` |
| `2026-08-13 10:52:52` | `cowrie.session.params` |
| `2026-08-13 10:52:52` | `cowrie.command.input` |
| `2026-08-13 10:52:52` | `cowrie.session.file_download` |
| `2026-08-13 10:52:52` | `cowrie.log.closed` |
| `2026-08-13 10:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.59.163[.]225` to AbuseIPDB if not already reported
- [ ] Block `2.59.163[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab5292d4047

| Field | Detail |
|---|---|
| **Source IP** | `2.59.163[.]225` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:53` | `cowrie.session.connect` |
| `2026-08-13 10:52:53` | `cowrie.client.version` |
| `2026-08-13 10:52:53` | `cowrie.client.kex` |
| `2026-08-13 10:52:53` | `cowrie.login.success` |
| `2026-08-13 10:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.59.163[.]225` to AbuseIPDB if not already reported
- [ ] Block `2.59.163[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42f618f0df4d

| Field | Detail |
|---|---|
| **Source IP** | `2.59.163[.]225` |
| **First Seen** | 2026-08-13 10:52 |
| **Last Seen** | 2026-08-13 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:52:53` | `cowrie.session.connect` |
| `2026-08-13 10:52:53` | `cowrie.client.version` |
| `2026-08-13 10:52:54` | `cowrie.client.kex` |
| `2026-08-13 10:52:54` | `cowrie.login.success` |
| `2026-08-13 10:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.59.163[.]225` to AbuseIPDB if not already reported
- [ ] Block `2.59.163[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0c30dbdc1e

| Field | Detail |
|---|---|
| **Source IP** | `192.109.220[.]3` |
| **First Seen** | 2026-08-13 10:54 |
| **Last Seen** | 2026-08-13 10:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:54:55` | `cowrie.session.connect` |
| `2026-08-13 10:54:55` | `cowrie.client.version` |
| `2026-08-13 10:54:55` | `cowrie.client.kex` |
| `2026-08-13 10:54:55` | `cowrie.login.success` |
| `2026-08-13 10:54:56` | `cowrie.session.params` |
| `2026-08-13 10:54:56` | `cowrie.command.input` |
| `2026-08-13 10:54:56` | `cowrie.command.failed` |
| `2026-08-13 10:54:56` | `cowrie.log.closed` |
| `2026-08-13 10:54:57` | `cowrie.session.params` |
| `2026-08-13 10:54:57` | `cowrie.command.input` |
| `2026-08-13 10:54:57` | `cowrie.session.file_download` |
| `2026-08-13 10:54:57` | `cowrie.log.closed` |
| `2026-08-13 10:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.220[.]3` to AbuseIPDB if not already reported
- [ ] Block `192.109.220[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d248ba9e509

| Field | Detail |
|---|---|
| **Source IP** | `192.109.220[.]3` |
| **First Seen** | 2026-08-13 10:54 |
| **Last Seen** | 2026-08-13 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:54:58` | `cowrie.session.connect` |
| `2026-08-13 10:54:58` | `cowrie.client.version` |
| `2026-08-13 10:54:58` | `cowrie.client.kex` |
| `2026-08-13 10:54:58` | `cowrie.login.success` |
| `2026-08-13 10:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.220[.]3` to AbuseIPDB if not already reported
- [ ] Block `192.109.220[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b210c51b853

| Field | Detail |
|---|---|
| **Source IP** | `192.109.220[.]3` |
| **First Seen** | 2026-08-13 10:54 |
| **Last Seen** | 2026-08-13 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 10:54:59` | `cowrie.session.connect` |
| `2026-08-13 10:54:59` | `cowrie.client.version` |
| `2026-08-13 10:54:59` | `cowrie.client.kex` |
| `2026-08-13 10:54:59` | `cowrie.login.success` |
| `2026-08-13 10:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.220[.]3` to AbuseIPDB if not already reported
- [ ] Block `192.109.220[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **21** | 2026-08-13 08:55 | 2026-08-13 10:50 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-13 09:12 | 2026-08-13 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.151.84[.]117` | **3** | 2026-08-13 09:11 | 2026-08-13 09:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-13 09:59 | 2026-08-13 09:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-13 10:14 | 2026-08-13 10:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `203.25.208[.]110` | **3** | 2026-08-13 08:55 | 2026-08-13 09:00 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]136` | **3** | 2026-08-13 09:55 | 2026-08-13 09:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]175` | **3** | 2026-08-13 09:56 | 2026-08-13 09:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]196` | **3** | 2026-08-13 09:55 | 2026-08-13 09:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-13 09:24 | 2026-08-13 09:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-13 08:55 | 2026-08-13 09:56 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `71.90.30[.]53` | **2** | 2026-08-13 10:04 | 2026-08-13 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.210.23[.]1` | 1 | 2026-08-13 09:19 | 2026-08-13 09:19 | 14s | 0 | `T1592` | 🟢 LOW |
| `122.224.164[.]194` | 1 | 2026-08-13 09:29 | 2026-08-13 09:30 | 55s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | 1 | 2026-08-13 09:01 | 2026-08-13 09:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-13 09:36 | 2026-08-13 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.38.203[.]75` | 1 | 2026-08-13 10:50 | 2026-08-13 10:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-08-13 10:54 | 2026-08-13 10:54 | 9s | 0 | `T1592` | 🟢 LOW |
| `193.107.177[.]43` | 1 | 2026-08-13 09:40 | 2026-08-13 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.226.76[.]34` | 1 | 2026-08-13 09:53 | 2026-08-13 09:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `218.21.246[.]238` | 1 | 2026-08-13 09:25 | 2026-08-13 09:26 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-08-13 10:04 | 2026-08-13 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-13 10:35 | 2026-08-13 10:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-13 09:36 | 2026-08-13 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]94` | 1 | 2026-08-13 10:27 | 2026-08-13 10:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-13 10:34 | 2026-08-13 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.252.68[.]147` | 1 | 2026-08-13 09:13 | 2026-08-13 09:13 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 47/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `60.249.251[.]88` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `221.182.185[.]190` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `62.201.212[.]54` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `172.236.228[.]86` | US | Linode | **100** ⚠️ | 50 |
| `46.249.102[.]182` | DE | Deployish Limited | **100** ⚠️ | 2 |
| `193.226.76[.]34` | GB | Virtono Networks SRL | **100** ⚠️ | 2 |
| `65.20.149[.]239` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 143 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (16.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 27 recon entry/entries in table (12 group(s) consolidating 52 session(s)).

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
_Report time: 2026-08-13T11:06:19Z_

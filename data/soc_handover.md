# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T22:32:41Z |
| **Shift Time** | 22:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **110** |
| Confirmed Threats | **98** |
| False Positives Filtered | **12** (10.9%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **16** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **69** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **47** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **6** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `ubuntu` | 12 |
| `support` | 3 |
| `pi` | 2 |
| `345gs5662d34` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 3 |
| `` | 2 |
| `abcd1234` | 2 |
| `qwe123123` | 1 |
| `123@admin` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 3 |
| `root` | `` | 2 |
| `pi` | `abcd1234` | 2 |
| `ubuntu` | `qwe123123` | 1 |
| `root` | `123@admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `qwe123123` | `217.60.255.130` | 2026-08-25T19:00:26 |
| `root` | `123@admin` | `217.60.255.130` | 2026-08-25T19:00:30 |
| `ubuntu` | `qwer1234` | `217.60.255.130` | 2026-08-25T19:10:08 |
| `root` | `Cisco@123` | `217.60.255.130` | 2026-08-25T19:10:12 |
| `ubuntu` | `Aa123456789` | `217.60.255.130` | 2026-08-25T19:19:41 |
| `root` | `asdfghjkl` | `217.60.255.130` | 2026-08-25T19:19:45 |
| `ubuntu` | `qwer123` | `217.60.255.130` | 2026-08-25T19:29:22 |
| `root` | `asdf` | `217.60.255.130` | 2026-08-25T19:29:26 |
| `ubuntu` | `test2` | `217.60.255.130` | 2026-08-25T19:38:54 |
| `root` | `admin!23` | `217.60.255.130` | 2026-08-25T19:38:58 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T19:47:08 |
| `ubuntu` | `123456789Aa` | `217.60.255.130` | 2026-08-25T19:48:16 |
| `root` | `1234@A` | `217.60.255.130` | 2026-08-25T19:48:23 |
| `root` | `aA@12345678` | `115.178.75.242` | 2026-08-25T19:53:26 |
| `345gs5662d34` | `345gs5662d34` | `115.178.75.242` | 2026-08-25T19:53:30 |
| `root` | `3245gs5662d34` | `115.178.75.242` | 2026-08-25T19:53:31 |
| `root` | `﻿------fuck------` | `87.106.200.201` | 2026-08-25T19:54:15 |
| `ubuntu` | `A12345678` | `217.60.255.130` | 2026-08-25T19:58:09 |
| `root` | `Temp@123` | `217.60.255.130` | 2026-08-25T19:58:12 |
| `ubuntu` | `QWE123asd` | `217.60.255.130` | 2026-08-25T20:07:49 |
| `root` | `India123` | `217.60.255.130` | 2026-08-25T20:07:53 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T20:10:42 |
| `ubuntu` | `1qazxsW@` | `217.60.255.130` | 2026-08-25T20:17:15 |
| `root` | `Trinity@123` | `217.60.255.130` | 2026-08-25T20:17:20 |
| `ubuntu` | `123!@#123` | `217.60.255.130` | 2026-08-25T20:27:01 |
| `root` | `Techno@123` | `217.60.255.130` | 2026-08-25T20:27:04 |
| `ubuntu` | `Hotspot123` | `217.60.255.130` | 2026-08-25T20:36:41 |
| `root` | `admin@admin` | `217.60.255.130` | 2026-08-25T20:36:45 |
| `root` | `111111` | `195.178.110.227` | 2026-08-25T20:38:01 |
| `root` | `123` | `195.178.110.227` | 2026-08-25T20:39:41 |
| `root` | `123123` | `195.178.110.227` | 2026-08-25T20:41:32 |
| `root` | `123321` | `195.178.110.227` | 2026-08-25T20:43:20 |
| `root` | `1234` | `195.178.110.227` | 2026-08-25T20:45:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.215` | 2026-08-25T20:45:12 |
| `ubuntu` | `Fastway@123` | `217.60.255.130` | 2026-08-25T20:46:05 |
| `root` | `ubuntu123` | `217.60.255.130` | 2026-08-25T20:46:09 |
| `root` | `12345` | `195.178.110.227` | 2026-08-25T20:46:45 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-25T20:49:58 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-25T20:50:06 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-25T20:51:39 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-25T20:53:22 |
| `root` | `1234abcd` | `195.178.110.227` | 2026-08-25T20:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **110** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 34 |
| Go SSH scanner | 23 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `bc3aee897af7...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `bc3aee897af7...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.178.75.242`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **30** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 1 | HIGH |
| `AS701` | Verizon Business | 1 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4ef4ee242621

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:00 |
| **Last Seen** | 2026-08-25 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:00:25` | `cowrie.session.connect` |
| `2026-08-25 19:00:25` | `cowrie.client.version` |
| `2026-08-25 19:00:25` | `cowrie.client.kex` |
| `2026-08-25 19:00:26` | `cowrie.login.success` |
| `2026-08-25 19:00:26` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:00:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:00:27` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6fe3897c4b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:00 |
| **Last Seen** | 2026-08-25 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:00:29` | `cowrie.session.connect` |
| `2026-08-25 19:00:29` | `cowrie.client.version` |
| `2026-08-25 19:00:29` | `cowrie.client.kex` |
| `2026-08-25 19:00:30` | `cowrie.login.success` |
| `2026-08-25 19:00:30` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:00:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:00:31` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3812cddc4885

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:10 |
| **Last Seen** | 2026-08-25 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:10:07` | `cowrie.session.connect` |
| `2026-08-25 19:10:07` | `cowrie.client.version` |
| `2026-08-25 19:10:08` | `cowrie.client.kex` |
| `2026-08-25 19:10:08` | `cowrie.login.success` |
| `2026-08-25 19:10:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:10:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:10:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c49ba2c6a72

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:10 |
| **Last Seen** | 2026-08-25 19:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:10:11` | `cowrie.session.connect` |
| `2026-08-25 19:10:11` | `cowrie.client.version` |
| `2026-08-25 19:10:11` | `cowrie.client.kex` |
| `2026-08-25 19:10:12` | `cowrie.login.success` |
| `2026-08-25 19:10:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:10:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:10:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f29d199dd58

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:19 |
| **Last Seen** | 2026-08-25 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:19:40` | `cowrie.session.connect` |
| `2026-08-25 19:19:40` | `cowrie.client.version` |
| `2026-08-25 19:19:40` | `cowrie.client.kex` |
| `2026-08-25 19:19:41` | `cowrie.login.success` |
| `2026-08-25 19:19:41` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:19:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:19:41` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5eb9cf6b616

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:19 |
| **Last Seen** | 2026-08-25 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:19:43` | `cowrie.session.connect` |
| `2026-08-25 19:19:43` | `cowrie.client.version` |
| `2026-08-25 19:19:43` | `cowrie.client.kex` |
| `2026-08-25 19:19:45` | `cowrie.login.success` |
| `2026-08-25 19:19:45` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:19:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:19:45` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63fae1ab7cf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:29 |
| **Last Seen** | 2026-08-25 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:29:21` | `cowrie.session.connect` |
| `2026-08-25 19:29:21` | `cowrie.client.version` |
| `2026-08-25 19:29:21` | `cowrie.client.kex` |
| `2026-08-25 19:29:22` | `cowrie.login.success` |
| `2026-08-25 19:29:22` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:29:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:29:22` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9db2862b0b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:29 |
| **Last Seen** | 2026-08-25 19:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:29:25` | `cowrie.session.connect` |
| `2026-08-25 19:29:25` | `cowrie.client.version` |
| `2026-08-25 19:29:25` | `cowrie.client.kex` |
| `2026-08-25 19:29:26` | `cowrie.login.success` |
| `2026-08-25 19:29:26` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:29:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:29:27` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9d773e26b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:38 |
| **Last Seen** | 2026-08-25 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:38:52` | `cowrie.session.connect` |
| `2026-08-25 19:38:52` | `cowrie.client.version` |
| `2026-08-25 19:38:53` | `cowrie.client.kex` |
| `2026-08-25 19:38:54` | `cowrie.login.success` |
| `2026-08-25 19:38:54` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:38:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:38:54` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddb54614fc5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:38 |
| **Last Seen** | 2026-08-25 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:38:57` | `cowrie.session.connect` |
| `2026-08-25 19:38:57` | `cowrie.client.version` |
| `2026-08-25 19:38:57` | `cowrie.client.kex` |
| `2026-08-25 19:38:58` | `cowrie.login.success` |
| `2026-08-25 19:38:58` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:38:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:38:58` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80aaa65ea7d2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 19:47 |
| **Last Seen** | 2026-08-25 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:47:08` | `cowrie.session.connect` |
| `2026-08-25 19:47:08` | `cowrie.client.version` |
| `2026-08-25 19:47:08` | `cowrie.client.kex` |
| `2026-08-25 19:47:08` | `cowrie.login.success` |
| `2026-08-25 19:47:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:47:08` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e59a757ca38

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:48 |
| **Last Seen** | 2026-08-25 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:48:15` | `cowrie.session.connect` |
| `2026-08-25 19:48:15` | `cowrie.client.version` |
| `2026-08-25 19:48:16` | `cowrie.client.kex` |
| `2026-08-25 19:48:16` | `cowrie.login.success` |
| `2026-08-25 19:48:17` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:48:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:48:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa161c63f11

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:48 |
| **Last Seen** | 2026-08-25 19:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:48:20` | `cowrie.session.connect` |
| `2026-08-25 19:48:20` | `cowrie.client.version` |
| `2026-08-25 19:48:21` | `cowrie.client.kex` |
| `2026-08-25 19:48:23` | `cowrie.login.success` |
| `2026-08-25 19:48:23` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:48:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:48:23` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236ae7ad5c44

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-08-25 19:53 |
| **Last Seen** | 2026-08-25 19:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:53:25` | `cowrie.session.connect` |
| `2026-08-25 19:53:25` | `cowrie.client.version` |
| `2026-08-25 19:53:25` | `cowrie.client.kex` |
| `2026-08-25 19:53:26` | `cowrie.login.success` |
| `2026-08-25 19:53:27` | `cowrie.session.params` |
| `2026-08-25 19:53:27` | `cowrie.command.input` |
| `2026-08-25 19:53:27` | `cowrie.command.failed` |
| `2026-08-25 19:53:27` | `cowrie.log.closed` |
| `2026-08-25 19:53:28` | `cowrie.session.params` |
| `2026-08-25 19:53:28` | `cowrie.command.input` |
| `2026-08-25 19:53:29` | `cowrie.session.file_download` |
| `2026-08-25 19:53:29` | `cowrie.log.closed` |
| `2026-08-25 19:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a57f59e13cac

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-08-25 19:53 |
| **Last Seen** | 2026-08-25 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:53:29` | `cowrie.session.connect` |
| `2026-08-25 19:53:29` | `cowrie.client.version` |
| `2026-08-25 19:53:29` | `cowrie.client.kex` |
| `2026-08-25 19:53:30` | `cowrie.login.success` |
| `2026-08-25 19:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc5deffa9e0

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-08-25 19:53 |
| **Last Seen** | 2026-08-25 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:53:30` | `cowrie.session.connect` |
| `2026-08-25 19:53:30` | `cowrie.client.version` |
| `2026-08-25 19:53:30` | `cowrie.client.kex` |
| `2026-08-25 19:53:31` | `cowrie.login.success` |
| `2026-08-25 19:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0893f58943fe

| Field | Detail |
|---|---|
| **Source IP** | `87.106.200[.]201` |
| **First Seen** | 2026-08-25 19:54 |
| **Last Seen** | 2026-08-25 19:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:54:11` | `cowrie.session.connect` |
| `2026-08-25 19:54:12` | `cowrie.client.version` |
| `2026-08-25 19:54:12` | `cowrie.client.kex` |
| `2026-08-25 19:54:15` | `cowrie.login.success` |
| `2026-08-25 19:54:16` | `cowrie.session.params` |
| `2026-08-25 19:54:16` | `cowrie.command.input` |
| `2026-08-25 19:54:17` | `cowrie.log.closed` |
| `2026-08-25 19:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.200[.]201` to AbuseIPDB if not already reported
- [ ] Block `87.106.200[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb4ea97fe61

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:58 |
| **Last Seen** | 2026-08-25 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:58:07` | `cowrie.session.connect` |
| `2026-08-25 19:58:07` | `cowrie.client.version` |
| `2026-08-25 19:58:07` | `cowrie.client.kex` |
| `2026-08-25 19:58:09` | `cowrie.login.success` |
| `2026-08-25 19:58:09` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:58:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:58:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950da0a2b206

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 19:58 |
| **Last Seen** | 2026-08-25 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 19:58:11` | `cowrie.session.connect` |
| `2026-08-25 19:58:11` | `cowrie.client.version` |
| `2026-08-25 19:58:11` | `cowrie.client.kex` |
| `2026-08-25 19:58:12` | `cowrie.login.success` |
| `2026-08-25 19:58:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 19:58:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 19:58:12` | `cowrie.direct-tcpip.data` |
| `2026-08-25 19:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b9454d9bfc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:07 |
| **Last Seen** | 2026-08-25 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:07:47` | `cowrie.session.connect` |
| `2026-08-25 20:07:47` | `cowrie.client.version` |
| `2026-08-25 20:07:48` | `cowrie.client.kex` |
| `2026-08-25 20:07:49` | `cowrie.login.success` |
| `2026-08-25 20:07:49` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:07:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:07:49` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1694a3b73177

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:07 |
| **Last Seen** | 2026-08-25 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:07:52` | `cowrie.session.connect` |
| `2026-08-25 20:07:52` | `cowrie.client.version` |
| `2026-08-25 20:07:52` | `cowrie.client.kex` |
| `2026-08-25 20:07:53` | `cowrie.login.success` |
| `2026-08-25 20:07:53` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:07:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:07:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c00d1b4ade

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:17 |
| **Last Seen** | 2026-08-25 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:17:14` | `cowrie.session.connect` |
| `2026-08-25 20:17:14` | `cowrie.client.version` |
| `2026-08-25 20:17:14` | `cowrie.client.kex` |
| `2026-08-25 20:17:15` | `cowrie.login.success` |
| `2026-08-25 20:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:17:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:17:15` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7800d38fed4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:17 |
| **Last Seen** | 2026-08-25 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:17:18` | `cowrie.session.connect` |
| `2026-08-25 20:17:18` | `cowrie.client.version` |
| `2026-08-25 20:17:19` | `cowrie.client.kex` |
| `2026-08-25 20:17:20` | `cowrie.login.success` |
| `2026-08-25 20:17:20` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:17:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:17:20` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6de8bc056a6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:26 |
| **Last Seen** | 2026-08-25 20:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:26:58` | `cowrie.session.connect` |
| `2026-08-25 20:26:58` | `cowrie.client.version` |
| `2026-08-25 20:26:58` | `cowrie.client.kex` |
| `2026-08-25 20:27:01` | `cowrie.login.success` |
| `2026-08-25 20:27:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:27:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:27:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c74e29b0f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:27 |
| **Last Seen** | 2026-08-25 20:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:27:02` | `cowrie.session.connect` |
| `2026-08-25 20:27:02` | `cowrie.client.version` |
| `2026-08-25 20:27:02` | `cowrie.client.kex` |
| `2026-08-25 20:27:04` | `cowrie.login.success` |
| `2026-08-25 20:27:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:27:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:27:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8eaa5f68d57

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 20:31 |
| **Last Seen** | 2026-08-25 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:31:05` | `cowrie.session.connect` |
| `2026-08-25 20:31:05` | `cowrie.client.version` |
| `2026-08-25 20:31:05` | `cowrie.client.kex` |
| `2026-08-25 20:31:05` | `cowrie.login.success` |
| `2026-08-25 20:31:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:31:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87bf81a65314

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:36 |
| **Last Seen** | 2026-08-25 20:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:36:40` | `cowrie.session.connect` |
| `2026-08-25 20:36:40` | `cowrie.client.version` |
| `2026-08-25 20:36:40` | `cowrie.client.kex` |
| `2026-08-25 20:36:41` | `cowrie.login.success` |
| `2026-08-25 20:36:42` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:36:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:36:42` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dba3cfc8070

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:36 |
| **Last Seen** | 2026-08-25 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:36:44` | `cowrie.session.connect` |
| `2026-08-25 20:36:44` | `cowrie.client.version` |
| `2026-08-25 20:36:44` | `cowrie.client.kex` |
| `2026-08-25 20:36:45` | `cowrie.login.success` |
| `2026-08-25 20:36:45` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:36:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:36:45` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cae963d16154

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:37 |
| **Last Seen** | 2026-08-25 20:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:37:59` | `cowrie.session.connect` |
| `2026-08-25 20:37:59` | `cowrie.client.version` |
| `2026-08-25 20:37:59` | `cowrie.client.kex` |
| `2026-08-25 20:38:01` | `cowrie.login.success` |
| `2026-08-25 20:38:02` | `cowrie.session.params` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.success` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.command.input` |
| `2026-08-25 20:38:02` | `cowrie.log.closed` |
| `2026-08-25 20:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12577ac7eca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:39 |
| **Last Seen** | 2026-08-25 20:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:39:40` | `cowrie.session.connect` |
| `2026-08-25 20:39:40` | `cowrie.client.version` |
| `2026-08-25 20:39:40` | `cowrie.client.kex` |
| `2026-08-25 20:39:41` | `cowrie.login.success` |
| `2026-08-25 20:39:42` | `cowrie.session.params` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.success` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.command.input` |
| `2026-08-25 20:39:42` | `cowrie.log.closed` |
| `2026-08-25 20:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990e00ce5b3b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:41 |
| **Last Seen** | 2026-08-25 20:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:41:30` | `cowrie.session.connect` |
| `2026-08-25 20:41:31` | `cowrie.client.version` |
| `2026-08-25 20:41:31` | `cowrie.client.kex` |
| `2026-08-25 20:41:32` | `cowrie.login.success` |
| `2026-08-25 20:41:33` | `cowrie.session.params` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.success` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:33` | `cowrie.command.input` |
| `2026-08-25 20:41:34` | `cowrie.log.closed` |
| `2026-08-25 20:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd8b8f258e5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:43 |
| **Last Seen** | 2026-08-25 20:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:43:18` | `cowrie.session.connect` |
| `2026-08-25 20:43:18` | `cowrie.client.version` |
| `2026-08-25 20:43:18` | `cowrie.client.kex` |
| `2026-08-25 20:43:20` | `cowrie.login.success` |
| `2026-08-25 20:43:22` | `cowrie.session.params` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.success` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.command.input` |
| `2026-08-25 20:43:22` | `cowrie.log.closed` |
| `2026-08-25 20:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc13087265a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:45 |
| **Last Seen** | 2026-08-25 20:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:45:03` | `cowrie.session.connect` |
| `2026-08-25 20:45:03` | `cowrie.client.version` |
| `2026-08-25 20:45:03` | `cowrie.client.kex` |
| `2026-08-25 20:45:05` | `cowrie.login.success` |
| `2026-08-25 20:45:06` | `cowrie.session.params` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.success` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:06` | `cowrie.command.input` |
| `2026-08-25 20:45:07` | `cowrie.log.closed` |
| `2026-08-25 20:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97dbe6e14769

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:46 |
| **Last Seen** | 2026-08-25 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:46:04` | `cowrie.session.connect` |
| `2026-08-25 20:46:04` | `cowrie.client.version` |
| `2026-08-25 20:46:04` | `cowrie.client.kex` |
| `2026-08-25 20:46:05` | `cowrie.login.success` |
| `2026-08-25 20:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:46:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:46:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afaad9fbb37f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 20:46 |
| **Last Seen** | 2026-08-25 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:46:08` | `cowrie.session.connect` |
| `2026-08-25 20:46:08` | `cowrie.client.version` |
| `2026-08-25 20:46:09` | `cowrie.client.kex` |
| `2026-08-25 20:46:09` | `cowrie.login.success` |
| `2026-08-25 20:46:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 20:46:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 20:46:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 20:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9693a0d05f59

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:46 |
| **Last Seen** | 2026-08-25 20:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:46:44` | `cowrie.session.connect` |
| `2026-08-25 20:46:44` | `cowrie.client.version` |
| `2026-08-25 20:46:44` | `cowrie.client.kex` |
| `2026-08-25 20:46:45` | `cowrie.login.success` |
| `2026-08-25 20:46:47` | `cowrie.session.params` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.success` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.command.input` |
| `2026-08-25 20:46:47` | `cowrie.log.closed` |
| `2026-08-25 20:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba90bb785e5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:50 |
| **Last Seen** | 2026-08-25 20:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:50:03` | `cowrie.session.connect` |
| `2026-08-25 20:50:04` | `cowrie.client.version` |
| `2026-08-25 20:50:04` | `cowrie.client.kex` |
| `2026-08-25 20:50:06` | `cowrie.login.success` |
| `2026-08-25 20:50:08` | `cowrie.session.params` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.success` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.command.input` |
| `2026-08-25 20:50:08` | `cowrie.log.closed` |
| `2026-08-25 20:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa070550abad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:51 |
| **Last Seen** | 2026-08-25 20:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:51:38` | `cowrie.session.connect` |
| `2026-08-25 20:51:38` | `cowrie.client.version` |
| `2026-08-25 20:51:38` | `cowrie.client.kex` |
| `2026-08-25 20:51:39` | `cowrie.login.success` |
| `2026-08-25 20:51:41` | `cowrie.session.params` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.success` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.command.input` |
| `2026-08-25 20:51:41` | `cowrie.log.closed` |
| `2026-08-25 20:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eafa5b0f791

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:53 |
| **Last Seen** | 2026-08-25 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:53:20` | `cowrie.session.connect` |
| `2026-08-25 20:53:21` | `cowrie.client.version` |
| `2026-08-25 20:53:21` | `cowrie.client.kex` |
| `2026-08-25 20:53:22` | `cowrie.login.success` |
| `2026-08-25 20:53:24` | `cowrie.session.params` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.success` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.command.input` |
| `2026-08-25 20:53:24` | `cowrie.log.closed` |
| `2026-08-25 20:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14211a93d11c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-25 20:54 |
| **Last Seen** | 2026-08-25 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 20:54:59` | `cowrie.session.connect` |
| `2026-08-25 20:55:00` | `cowrie.client.version` |
| `2026-08-25 20:55:00` | `cowrie.client.kex` |
| `2026-08-25 20:55:02` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **20** | 2026-08-25 18:55 | 2026-08-25 20:54 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-25 18:57 | 2026-08-25 20:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | **4** | 2026-08-25 19:18 | 2026-08-25 20:12 | 3m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]245` | **3** | 2026-08-25 20:38 | 2026-08-25 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `173.40.169[.]86` | **3** | 2026-08-25 20:35 | 2026-08-25 20:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `184.93.137[.]139` | **2** | 2026-08-25 19:04 | 2026-08-25 19:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-08-25 20:32 | 2026-08-25 20:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.149.196[.]217` | 1 | 2026-08-25 19:52 | 2026-08-25 19:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.165.140[.]102` | 1 | 2026-08-25 20:36 | 2026-08-25 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-25 20:17 | 2026-08-25 20:17 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.29.247[.]56` | 1 | 2026-08-25 19:49 | 2026-08-25 19:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-08-25 19:57 | 2026-08-25 19:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.30.48[.]27` | 1 | 2026-08-25 19:21 | 2026-08-25 19:21 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.76.228[.]20` | 1 | 2026-08-25 19:39 | 2026-08-25 19:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-25 19:39 | 2026-08-25 19:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.186.105[.]187` | 1 | 2026-08-25 19:21 | 2026-08-25 19:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-25 20:37 | 2026-08-25 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-25 20:37 | 2026-08-25 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-25 19:44 | 2026-08-25 19:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-25 19:07 | 2026-08-25 19:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]229` | 1 | 2026-08-25 20:20 | 2026-08-25 20:20 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-25 19:44 | 2026-08-25 19:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.108.116[.]140` | 1 | 2026-08-25 20:52 | 2026-08-25 20:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-08-25 19:07 | 2026-08-25 19:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-08-25 19:23 | 2026-08-25 19:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.106.200[.]201` | 1 | 2026-08-25 19:54 | 2026-08-25 19:54 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `45.186.105[.]187` | GT | INFINITUM S.A. | **100** ⚠️ | 0 |
| `117.149.196[.]217` | CN | China Mobile Communications Corporation | **100** ⚠️ | 15 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `119.165.140[.]102` | CN | China Unicom Shandong Province Network | **100** ⚠️ | 4 |
| `134.209.229[.]23` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `66.132.224[.]229` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `184.93.137[.]139` | US | Charter Communications Inc | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 10 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 110 cases |
| Tool 34  | Credential Extractor        | ✅ 47 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 26 recon entry/entries in table (7 group(s) consolidating 39 session(s)).

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
_Report time: 2026-08-25T22:32:41Z_
